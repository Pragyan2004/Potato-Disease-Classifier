#  Potato Disease Classifier

A Flask-based web application for detecting and classifying potato plant diseases using deep learning.  
The system can identify **Early Blight**, **Late Blight**, and **Healthy potato plants** from leaf images.

---

## Features

- **Image Analysis:** Upload potato leaf images for AI-powered disease detection  
- **Disease Information:** Detailed information about Early Blight and Late Blight diseases  
- **Treatment Plans:** Step-by-step treatment recommendations for identified diseases  
- **Field Management:** Track field health and crop rotation history  
- **Community Forum:** Connect with other farmers and experts  
- **Dashboard:** Visual statistics and health monitoring  

---

## Supported Diseases

### Early Blight (*Alternaria solani*)
- Circular brown lesions with concentric rings  
- Yellow halos around spots  
- Moderate severity, 7–10 days to rot  

### Late Blight (*Phytophthora infestans*)
- Water-soaked lesions turning brown/black  
- White fungal growth under leaves  
- Severe, 3–5 days to complete destruction  

### Healthy Plants
- No disease symptoms detected  
- Maintenance recommendations  

---

## Technology Stack

- **Backend:** Flask (Python)  
- **Machine Learning:** PyTorch with DenseNet-121 architecture  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Styling:** Custom CSS (purple/orange/red color scheme)  
- **Image Processing:** PIL, TorchVision transforms  

---

## Installation

**Clone the repository:**
   
   git clone https://github.com/Pragyan2004/Potato-Disease-Classifier.git
   
   cd potato-disease-classifier


**Usage**

Start the Flask development server:

    python app.py


Open your browser and navigate to:

http://localhost:5000


**Features available:**

Upload potato leaf images for analysis
View disease information and treatment plans
Monitor field health statistics
Access community discussions

**Image Upload Guidelines**

Take photos in good lighting conditions
Focus on leaves showing potential symptoms
Capture both upper and lower leaf surfaces
Include a scale reference if possible
Avoid blurry or shadowed images
Supported formats: JPG, PNG, JPEG (Max 5MB)

**Model Information**

Architecture: DenseNet-121
Training Data: Thousands of potato leaf images
Accuracy: >95% in classifying Early Blight, Late Blight, and Healthy plants

**Training the Model**

Prepare a dataset of labeled potato leaf images
Split into train/validation/test sets
Use transfer learning with DenseNet-121
Train with appropriate hyperparameters
Save as densenet121_best.pth

# ScreenShoots

<img width="761" height="925" alt="Screenshot 2025-09-13 154432" src="https://github.com/user-attachments/assets/5f274689-592f-4b39-ac48-21269bf93e72" />
<img width="770" height="873" alt="Screenshot 2025-09-13 154421" src="https://github.com/user-attachments/assets/e4e0a5b5-187e-4dcb-b497-b5fd71d47f5e" />
<img width="765" height="924" alt="Screenshot 2025-09-13 154410" src="https://github.com/user-attachments/assets/7a7c075c-d803-4275-86c5-69fcd96722cb" />
<img width="809" height="848" alt="Screenshot 2025-09-13 154356" src="https://github.com/user-attachments/assets/e8512344-a2b3-4988-8be6-dab24b99972a" />
<img width="779" height="920" alt="Screenshot 2025-09-13 154346" src="https://github.com/user-attachments/assets/1799fe1b-750f-44ac-addc-ae1baf913191" />
<img width="776" height="760" alt="Screenshot 2025-09-13 154332" src="https://github.com/user-attachments/assets/42b278bb-1725-4044-abfe-12789ae89c80" />
<img width="781" height="624" alt="Screenshot 2025-09-13 154320" src="https://github.com/user-attachments/assets/540b5667-189e-461d-be0d-adad7112a63a" />
<img width="755" height="849" alt="Screenshot 2025-09-13 154235" src="https://github.com/user-attachments/assets/00906692-1523-481e-aad2-267ed32cb255" />



