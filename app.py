import os
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash
from torchvision import transforms, models
import json
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class Config:
    CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
    DISEASE_INFO = {
        "Early Blight": {
            "severity": "Moderate",
            "rot_days": "7-10 days",
            "treatment": "Apply fungicides containing chlorothalonil or mancozeb. Remove infected leaves.",
            "prevention": "Rotate crops, ensure proper spacing, and avoid overhead watering.",
            "progression": "/static/images/disease-progression/early-blight.jpg"
        },
        "Late Blight": {
            "severity": "Severe",
            "rot_days": "3-5 days",
            "treatment": "Apply fungicides containing copper or metalaxyl immediately. Destroy infected plants.",
            "prevention": "Plant resistant varieties, ensure good air circulation, and avoid wet conditions.",
            "progression": "/static/images/disease-progression/late-blight.jpg"
        },
        "Healthy": {
            "severity": "None",
            "rot_days": "N/A",
            "treatment": "Maintain current care routine",
            "prevention": "Regular inspection, proper fertilization, and crop rotation",
            "progression": "/static/images/disease-progression/healthy.jpg"
        }
    }

config = Config()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.densenet121()
model.classifier = nn.Linear(model.classifier.in_features, 3)

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'densenet121_best.pth')
model.load_state_dict(torch.load(model_path, map_location=device))
model.eval()
def get_transform():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
def predict_image(image_path):
    transform = get_transform()
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(image)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        confidence, predicted = torch.max(probabilities, 0)
        predicted_class = config.CLASS_NAMES[predicted.item()]
        confidence = confidence.item() * 100
    
    return predicted_class, round(confidence, 2)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    """User dashboard with statistics"""
    stats = {
        'total_scans': 42,
        'healthy_count': 28,
        'diseased_count': 14,
        'last_scan': 'Potato___Late_blight',
        'treatment_plans': 3,
        'field_health': 76
    }
    
    distribution = {
        'Early Blight': 5,
        'Late Blight': 9,
        'Healthy': 28
    }
    
    recent_scans = [
        {'name': 'Field A - Row 3', 'date': '2023-07-15', 'status': 'Late Blight'},
        {'name': 'Field B - Row 1', 'date': '2023-07-14', 'status': 'Healthy'},
        {'name': 'Field C - Row 2', 'date': '2023-07-12', 'status': 'Early Blight'}
    ]
    
    return render_template('dashboard.html', stats=stats, distribution=distribution, recent_scans=recent_scans)

@app.route('/diseases')
def diseases():
    """Disease information library"""
    diseases = [
        {
            'name': 'Early Blight',
            'scientific': 'Alternaria solani',
            'symptoms': 'Circular brown lesions with concentric rings, yellow halos',
            'progression': '7-10 days to severe damage',
            'images': ['early-blight-1.jpg', 'early-blight-2.jpg']
        },
        {
            'name': 'Late Blight',
            'scientific': 'Phytophthora infestans',
            'symptoms': 'Water-soaked lesions that turn brown/black, white fungal growth',
            'progression': '3-5 days to complete destruction',
            'images': ['late-blight-1.jpg', 'late-blight-2.jpg']
        }
    ]
    return render_template('diseases.html', diseases=diseases)

@app.route('/treatments')
def treatments():
    """Treatment plans guide"""
    treatments = [
        {
            'disease': 'Early Blight',
            'steps': [
                {'day': 0, 'action': 'Apply chlorothalonil fungicide (1.5 lb/acre)'},
                {'day': 3, 'action': 'Remove severely infected leaves'},
                {'day': 7, 'action': 'Reapply fungicide + add potassium fertilizer'},
                {'day': 14, 'action': 'Monitor and apply neem oil as needed'}
            ],
            'prevention': 'Rotate crops, space plants properly, avoid overhead watering'
        },
        {
            'disease': 'Late Blight',
            'steps': [
                {'day': 0, 'action': 'Apply copper-based fungicide immediately'},
                {'day': 1, 'action': 'Remove and destroy infected plants (bag before removal)'},
                {'day': 2, 'action': 'Apply systemic fungicide (metalaxyl-based)'},
                {'day': 5, 'action': 'Reapply copper fungicide'},
                {'day': 7, 'action': 'Monitor field daily for new infections'}
            ],
            'prevention': 'Use resistant varieties, ensure good air circulation'
        }
    ]
    return render_template('treatments.html', treatments=treatments)

@app.route('/field')
def field():
    """Field management system"""
    fields = [
        {'name': 'North Field', 'size': '5 acres', 'crop': 'Potatoes', 
         'rotation': ['Tomatoes (2022)', 'Beans (2021)', 'Corn (2020)'], 
         'health': 82, 'last_scan': '2023-07-12'},
        {'name': 'South Field', 'size': '3.5 acres', 'crop': 'Potatoes', 
         'rotation': ['Carrots (2022)', 'Lettuce (2021)', 'Cabbage (2020)'], 
         'health': 68, 'last_scan': '2023-07-15'}
    ]
    
    recommendations = [
        'Plant marigolds between rows to deter pests',
        'Rotate with legumes next season to replenish nitrogen',
        'Add organic compost before next planting season'
    ]
    
    return render_template('field.html', fields=fields, recommendations=recommendations)

@app.route('/community')
def community():
    """Community forum"""
    topics = [
        {
            'title': 'Best fungicide for Late Blight?',
            'author': 'John Farmer',
            'date': '2023-07-10',
            'replies': 12,
            'tags': ['treatment', 'late-blight']
        },
        {
            'title': 'Early Blight resistant varieties?',
            'author': 'Sarah Grower',
            'date': '2023-07-08',
            'replies': 8,
            'tags': ['varieties', 'early-blight']
        },
        {
            'title': 'Crop rotation suggestions?',
            'author': 'Mike Agric',
            'date': '2023-07-05',
            'replies': 15,
            'tags': ['rotation', 'soil-health']
        }
    ]
    return render_template('community.html', topics=topics)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        if file:
            upload_dir = os.path.join('static', 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            
            upload_path = os.path.join(upload_dir, file.filename)
            file.save(upload_path)
            
            try:
                predicted_class, confidence = predict_image(upload_path)
                disease_info = config.DISEASE_INFO[predicted_class]
                
                timeline = []
                if predicted_class == "Early Blight":
                    timeline = [
                        {"day": 0, "action": "Remove infected leaves"},
                        {"day": 1, "action": "Apply chlorothalonil fungicide"},
                        {"day": 3, "action": "Monitor plant health"},
                        {"day": 7, "action": "Reapply fungicide if needed"}
                    ]
                elif predicted_class == "Late Blight":
                    timeline = [
                        {"day": 0, "action": "Isolate infected plants immediately"},
                        {"day": 0, "action": "Apply copper-based fungicide"},
                        {"day": 1, "action": "Remove and destroy severely infected plants"},
                        {"day": 2, "action": "Treat surrounding plants preventatively"},
                        {"day": 5, "action": "Reapply fungicide"}
                    ]
                else:
                    timeline = [
                        {"day": 0, "action": "Continue regular care routine"},
                        {"day": 7, "action": "Inspect plants for early signs"},
                        {"day": 14, "action": "Apply balanced fertilizer"},
                        {"day": 30, "action": "Rotate crops if in field"}
                    ]
                
                return render_template('results.html', 
                                       image_path=upload_path,
                                       predicted_class=predicted_class,
                                       confidence=confidence,
                                       disease_info=disease_info,
                                       timeline=timeline)
            except Exception as e:
                flash(f'Error processing image: {str(e)}', 'error')
                return redirect(request.url)
    
    return render_template('upload.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)