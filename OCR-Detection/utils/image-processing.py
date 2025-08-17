import cv2
from ultralytics import YOLO

model = YOLO("models/best.pt")

def detect_plate(image_path):
    results = model(image_path)
    boxes = results[0].boxes.xyxy.cpu().numpy()

    img = cv2.imread(image_path)
    if len(boxes) > 0:
        x1, y1, x2, y2 = map(int, boxes[0])
        plate = img[y1:y2, x1:x2]
        return plate
    return img
