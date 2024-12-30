import cv2
from src.gesture_detection import detect_gestures
from src.utilities.hand_tracking import HandTracker

# Initialize hand tracker
hand_tracker = HandTracker()

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    processed_frame, actions = hand_tracker.process_frame(frame)
    detect_gestures(actions)

    cv2.imshow("Hand Gesture Mouse Control", processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
