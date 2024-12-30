import pyautogui

class GestureHandler:
    def __init__(self):
        self.SCROLL_THRESHOLD = 20

    def handle_gestures(self, hand_landmarks):
        try:
            # Detect cursor movement
            cursor_position = self.detect_cursor_position(hand_landmarks)
            if cursor_position:
                pyautogui.moveTo(cursor_position["x"], cursor_position["y"])

            # Detect scrolling
            if self.detect_fist(hand_landmarks):
                self.handle_scroll(hand_landmarks)
        except Exception as e:
            print(f"Error in gesture handling: {e}")

    def detect_cursor_position(self, hand_landmarks):
        if "index_finger_tip" in hand_landmarks:
            index_finger = hand_landmarks["index_finger_tip"]
            # Map to screen resolution
            screen_width, screen_height = pyautogui.size()
            cursor_x = int(index_finger[0] * screen_width)
            cursor_y = int(index_finger[1] * screen_height)

            # Clamp coordinates
            cursor_x = max(0, min(cursor_x, screen_width - 1))
            cursor_y = max(0, min(cursor_y, screen_height - 1))

            print(f"Mapped Cursor Position: {cursor_x}, {cursor_y}")
            return {"x": cursor_x, "y": cursor_y}
        return None

    def detect_fist(self, hand_landmarks):
        wrist = hand_landmarks.get("wrist")
        fingertips = [hand_landmarks.get(key) for key in [
            "thumb_tip", "index_finger_tip", "middle_finger_tip",
            "ring_finger_tip", "pinky_tip"]]

        if wrist and all(fingertips):
            return all(self.calculate_distance(wrist, tip) < 0.1 for tip in fingertips)
        return False

    def handle_scroll(self, hand_landmarks):
        wrist = hand_landmarks.get("wrist")
        middle_finger = hand_landmarks.get("middle_finger_tip")
        if wrist and middle_finger:
            scroll_distance = int((wrist[1] - middle_finger[1]) * 100)
            if scroll_distance > self.SCROLL_THRESHOLD:
                pyautogui.scroll(-10)  # Scroll down
            elif scroll_distance < -self.SCROLL_THRESHOLD:
                pyautogui.scroll(10)  # Scroll up

    @staticmethod
    def calculate_distance(point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
