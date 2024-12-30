import cv2
from utilities.hand_tracking import HandTracker
from gesture_detection import GestureHandler

# Initialize hand tracker and gesture handler
hand_tracker = HandTracker()
gesture_handler = GestureHandler()

# Start capturing video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    try:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video frame.")
            break

        frame = cv2.flip(frame, 1)
        frame, hand_landmarks = hand_tracker.track(frame)

        if hand_landmarks:
            # Process detected gestures
            gesture_handler.handle_gestures(hand_landmarks)

        # Show the video feed
        cv2.imshow("CursorByGestures", frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print(f"An error occurred: {e}")
        break

cap.release()
cv2.destroyAllWindows()
