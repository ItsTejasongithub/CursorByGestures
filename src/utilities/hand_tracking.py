import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.mp_drawing = mp.solutions.drawing_utils

    def track(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_frame)
        landmarks = None

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                landmarks = self.extract_landmarks(hand_landmarks)

        return frame, landmarks

    def extract_landmarks(self, hand_landmarks):
        return {
            "wrist": (hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x,
                      hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].y),
            "thumb_tip": (hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x,
                          hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y),
            "index_finger_tip": (hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                                 hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y),
            "middle_finger_tip": (hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
                                  hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y),
            "ring_finger_tip": (hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x,
                                hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y),
            "pinky_tip": (hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x,
                          hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y),
        }
