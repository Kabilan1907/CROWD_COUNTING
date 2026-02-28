###🎥 CrowdCount – Milestone 3

Real-Time Person Detection, Tracking, Entry/Exit Counting & Zone Monitoring using OpenCV

📌 Project Overview

CrowdCount – Milestone 3 is a real-time computer vision system built using Python and OpenCV.

The system:

Detects people using HOG + SVM

Tracks each person with a unique ID

Counts Entry and Exit based on a virtual line

Monitors people inside a defined zone

Saves real-time data to a CSV file

Displays a live dashboard panel

This project is useful for:

Smart surveillance systems

Crowd monitoring

Shopping mall entry/exit tracking

Smart campus monitoring

Public area analytics

⚙️ Technologies Used

Python 3.x

OpenCV (cv2)

HOG Descriptor + SVM (Default People Detector)

CSV module

Math module

Datetime module

🚀 Features
✅ 1. Real-Time Person Detection

Uses OpenCV’s built-in HOG Person Detector to detect humans in each frame.

✅ 2. Unique Person Tracking

Each detected person is assigned a unique ID.

Tracking is based on center-point distance comparison.

Prevents duplicate counting across frames.

✅ 3. Entry / Exit Counting

A virtual horizontal line is placed on the screen.

When a person crosses:

Top → Bottom → Entry Count increases

Bottom → Top → Exit Count increases

Each ID is counted only once.

✅ 4. Zone Monitoring

A rectangular zone is defined.

Counts how many tracked people are currently inside the zone.

✅ 5. Live Dashboard

Displays:

Total Tracked Persons

Zone Count

Entry Count

Exit Count

✅ 6. CSV Data Logging

Every frame logs:

Timestamp

Zone count

Entry count

Exit count

Saved in:

count_data.csv
📂 Project Structure
CrowdCount/
│
├── main.py
├── count_data.csv (auto-generated)
└── README.md
🖥️ How It Works
1️⃣ Camera Initialization

The system captures live video using:

cv2.VideoCapture(0)
2️⃣ Person Detection

Uses:

cv2.HOGDescriptor_getDefaultPeopleDetector()

to detect humans in each frame.

3️⃣ Tracking Logic

Computes center point (cx, cy) for each bounding box.

Compares distance with previous frame positions.

If distance < 50 pixels → Same person.

Else → Assign new ID.

Distance Formula:

sqrt((x1 - x2)^2 + (y1 - y2)^2)
4️⃣ Entry / Exit Logic

Virtual line:

line_y = 250

Conditions:

If previous y < line and current y ≥ line → Entry

If previous y > line and current y ≤ line → Exit

5️⃣ Zone Counting

Zone defined as:

zone = (100, 100, 500, 400)

If center point lies inside rectangle → Counted in zone.

📊 Dashboard Display

The system shows:

Total Tracked

Zone 1 Count

Entry Count

Exit Count

Live video window title:

CrowdCount - Milestone 3

Press Q to quit.

📦 Installation & Setup
Step 1: Install Dependencies
pip install opencv-python
Step 2: Run the Program
python main.py
📈 Sample CSV Output
Timestamp	Zone 1	Entry	Exit
2026-02-28 10:01:02	3	1	0
2026-02-28 10:01:03	2	1	1
🔧 Customization Options

You can modify:

line_y → Change entry/exit position

zone → Adjust monitoring area

Distance threshold (50) → Improve tracking accuracy

Add multiple zones

Improve tracking using Deep SORT

⚠️ Limitations

Simple distance-based tracking (not highly robust)

May fail in heavy crowd situations

Sensitive to lighting changes

No deep learning model used

🌟 Future Improvements (Milestone 4 Ideas)

Use YOLO for better detection

Implement Deep SORT tracking

Add GUI controls

Store summarized CSV instead of frame-by-frame logging

Add graph visualization dashboard

📚 Use Case Applications

Smart City Surveillance

Campus Security

Railway Station Monitoring

Mall Crowd Analytics

Event Management

👨‍💻 Author

Kabilan
VSB Engineering College
Internship / Academic Project
