# Face Detection Attendance System

A Python‑based desktop application for automated attendance tracking using face detection and recognition. Built with OpenCV, Tkinter and Pandas, 
this system replaces manual roll calls with a fast, accurate, and secure workflow.

---


## ⚙️ Installation & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/rohanroundhal/face-detection-system.git
   cd face-detection-system

## 🚀 Features

- **User Login & Registration**  
  Secure admin/staff access and student profile management (dept, course, semester, roll no., etc.).

- **Real‑Time Face Detection & Recognition**  
  - Haar Cascade classifier for face detection  
  - LBPH matching against a pre‑registered database  
  - Automatic mark‑attendance on match; prompts registration or alert on no‑match

- **Attendance Management**  
  - Timestamped logs written to CSV  
  - Import/Export CSV for easy data handling  
  - On‑screen table view of daily attendance

Install dependencies

bash
Copy
Edit
pip install opencv-python pandas face_recognition tk
Run the application

bash
Copy
Edit
python src/login.py
Workflow

Register new students (capture photos, save profiles)

Train the face‑recognizer model

Open Detect Face to mark attendance

View/Export attendance in the Attendance module

🔧 Technologies
Language: Python 3.x

GUI: Tkinter

Vision: OpenCV, Haar Cascades, LBPH

Data: Pandas (CSV import/export)

Storage: CSV‑based database (easily swap for MySQL or SQLite)

📈 Future Scope
LMS integration for automatic gradebooks

Mobile/web companion app for real‑time student access

Anti‑spoofing (liveness detection)

Multi‑modal attendance (face + RFID/Bluetooth)

📝 License
This project is released under the MIT License. See LICENSE for details.

css
Copy
Edit

Feel free to adjust paths, commands, or links to suit your repo layout!







