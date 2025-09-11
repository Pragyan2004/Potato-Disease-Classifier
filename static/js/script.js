
document.addEventListener('DOMContentLoaded', function() {
    initAnimations();
    initFileUpload();
    initConfidenceMeters();
    initHealthBars();
});

function initAnimations() {
    const animatedElements = document.querySelectorAll('.card, .stat-card, .topic-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    animatedElements.forEach(element => {
        element.style.opacity = 0;
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(element);
    });
}

function initFileUpload() {
    const uploadArea = document.querySelector('.upload-area');
    const fileInput = document.querySelector('#file-input');
    
    if (uploadArea && fileInput) {
        uploadArea.addEventListener('click', () => {
            fileInput.click();
        });
        
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('drag-over');
        });
        
        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('drag-over');
        });
        
        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('drag-over');
            
            if (e.dataTransfer.files.length) {
                fileInput.files = e.dataTransfer.files;
                const event = new Event('change', { bubbles: true });
                fileInput.dispatchEvent(event);
            }
        });
        
        fileInput.addEventListener('change', () => {
            if (fileInput.files.length) {
                const fileName = fileInput.files[0].name;
                uploadArea.querySelector('p').textContent = `Selected file: ${fileName}`;
            }
        });
    }
}
function initConfidenceMeters() {
    const confidenceMeters = document.querySelectorAll('.confidence-fill');
    
    confidenceMeters.forEach(meter => {
        const width = meter.getAttribute('data-width');
        setTimeout(() => {
            meter.style.width = width + '%';
        }, 300);
    });
}

function initHealthBars() {
    const healthBars = document.querySelectorAll('.health-progress');
    
    healthBars.forEach(bar => {
        const width = bar.getAttribute('data-width');
        setTimeout(() => {
            bar.style.width = width + '%';
        
            if (width >= 80) {
                bar.style.backgroundColor = '#27ae60'; // Healthy green
            } else if (width >= 50) {
                bar.style.backgroundColor = '#f39c12'; // Warning orange
            } else {
                bar.style.backgroundColor = '#e74c3c'; // Danger red
            }
        }, 300);
    });
}
function showFlashMessage(message, type) {
    const messageEl = document.createElement('div');
    messageEl.className = `flash-message flash-${type}`;
    messageEl.textContent = message;
    messageEl.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 5px;
        color: white;
        z-index: 10000;
        animation: slideInRight 0.3s ease;
    `;
    
    if (type === 'error') {
        messageEl.style.backgroundColor = '#e74c3c';
    } else {
        messageEl.style.backgroundColor = '#27ae60';
    }
    document.body.appendChild(messageEl);
    setTimeout(() => {
        messageEl.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(messageEl);
        }, 300);
    }, 5000);
}
if (document.querySelector('.flash-messages')) {
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        const type = message.classList.contains('alert-error') ? 'error' : 'success';
        showFlashMessage(message.textContent, type);
        message.style.display = 'none';
    });
}

function animateValue(id, start, end, duration) {
    const obj = document.getElementById(id);
    if (!obj) return;
    
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = Math.floor(progress * (end - start) + start);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

function initNumberAnimations() {
    const animatedNumbers = document.querySelectorAll('.stat-number');
    animatedNumbers.forEach((element, index) => {
        const value = parseInt(element.textContent);
        element.setAttribute('id', `animated-value-${index}`);
        animateValue(`animated-value-${index}`, 0, value, 2000);
    });
}
function initCharts() {
    const diseaseCtx = document.getElementById('diseaseChart');
    if (diseaseCtx) {
    }
    
    const healthCtx = document.getElementById('fieldHealthChart');
    if (healthCtx) {
    }
}

window.addEventListener('load', function() {
    initNumberAnimations();
    initCharts();
});