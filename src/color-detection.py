import cv2
from utils import get_limits
from PIL import Image

# Define colors in BGR format
colors = {
    "Red": [0, 0, 255],
    "Yellow": [0, 255, 255],
    "Green": [0, 255, 0],
    "Blue": [255, 0, 0]
}

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert frame to HSV

    for color_name, bgr_value in colors.items():
        lowerLimit, upperLimit = get_limits(bgr_value)  # Get HSV limits
        mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)  # Apply mask

        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), bgr_value, 5)  # Draw bounding box
            cv2.putText(frame, f"Color: {color_name}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, bgr_value, 2, cv2.LINE_AA)

    cv2.imshow('Color Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
