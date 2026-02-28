import cv2
import math
import csv
from datetime import datetime

# HOG Person Detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# Camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not opened")
    exit()

# Tracking Variables

person_id = 0
trackers = {}   # id : (cx, cy)
counted_ids = set()

# Entry/Exit
entry_count = 0
exit_count = 0

# Virtual line (horizontal)
line_y = 250

# Zone example (single rectangle zone)
zone = (100, 100, 500, 400)  # x1, y1, x2, y2
zone_counts = {"Zone 1": 0}


# Function to calculate distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# Main Loop

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 600))

    # Detect people
    boxes, _ = hog.detectMultiScale(frame, winStride=(8,8))

    new_trackers = {}

    for (x, y, w, h) in boxes:
        cx = x + w // 2
        cy = y + h // 2

        matched = False

        for id, (px, py) in trackers.items():
            if distance((cx, cy), (px, py)) < 50:
                new_trackers[id] = (cx, cy)
                matched = True

                # Entry / Exit Logic
                if py < line_y and cy >= line_y and id not in counted_ids:
                    entry_count += 1
                    counted_ids.add(id)

                elif py > line_y and cy <= line_y and id not in counted_ids:
                    exit_count += 1
                    counted_ids.add(id)

                break

        if not matched:
            person_id += 1
            new_trackers[person_id] = (cx, cy)

        # Draw bounding box
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.circle(frame, (cx,cy), 4, (0,0,255), -1)

    trackers = new_trackers

    
    # Zone Counting
    
    x1, y1, x2, y2 = zone
    cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)

    inside_count = 0
    for id, (cx, cy) in trackers.items():
        if x1 < cx < x2 and y1 < cy < y2:
            inside_count += 1

    zone_counts["Zone 1"] = inside_count

    
    # Draw Virtual Line

    cv2.line(frame, (0,line_y), (800,line_y), (0,0,255), 2)

    
    # Dashboard Panel
    
    cv2.putText(frame, f"Total Tracked: {len(trackers)}",
                (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(frame, f"Zone 1 Count: {zone_counts['Zone 1']}",
                (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    cv2.putText(frame, f"Entry: {entry_count}",
                (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    cv2.putText(frame, f"Exit: {exit_count}",
                (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    cv2.imshow("CrowdCount - Milestone 3", frame)

    # Save data to CSV every frame (simple version)
    with open("count_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            zone_counts["Zone 1"],
            entry_count,
            exit_count
        ])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()