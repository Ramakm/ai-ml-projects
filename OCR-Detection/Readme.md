# 🚗 OCR Plate Detection (YOLO + EasyOCR)

This project is a **license plate detection and recognition system** built with free and open-source libraries.  
It uses **YOLOv8** for detecting license plates and **EasyOCR** for extracting the plate text.  
The frontend is a simple **Flask web app** with **HTML/CSS/JavaScript** and a **history page powered by LocalStorage**.

---

## Project Structure
```bash
hw6-plate-ui/
├── app.py                 # Flask backend
├── requirements.txt       # Dependencies
├── models/
│   └── best.pt            # YOLO trained model
├── static/
│   ├── styles.css         # Styling
│   ├── history.js         # JS for history page
│   └── uploads/           # Uploaded images
├── templates/
│   ├── index.html         # Upload page
│   └── history.html       # History page
└── utils/
    ├── image_processing.py # YOLO detection
    └── ocr.py             # OCR extraction


---

## ⚙️ Features

- Upload an image of a car  
- Detect license plate region using **YOLOv8**  
- Extract plate text using **EasyOCR**  
- Store recognition results in **browser LocalStorage**  
- View past results in a **History page**  
- Simple and clean UI  

---

## Tech Stack

- **Backend:** Flask (Python)  
- **AI/ML:** YOLOv8 (Ultralytics), EasyOCR  
- **Image Processing:** OpenCV, Pillow  
- **Frontend:** HTML5, CSS3, Vanilla JavaScript  
- **Storage:** LocalStorage (no external DB required)  

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/hw6-plate-ui.git
cd hw6-plate-ui
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add YOLO model

- Place your YOLO trained weights (best.pt) into the models/ folder.
- You can train your own model or use a pre-trained one.

### 5. Run the app
```bash
python app.py
```