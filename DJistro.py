#!/usr/bin
# ██████╗            ██╗██╗ ██████╗████████╗██████╗  █████╗
# ██╔══██╗           ██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
# ██║  ██║█████╗     ██║██║╚█████╗    ██║   ██████╔╝██║  ██║
# ██║  ██║╚════╝██╗  ██║██║ ╚═══██╗   ██║   ██╔══██╗██║  ██║
# ██████╔╝      ╚█████╔╝██║██████╔╝   ██║   ██║  ██║╚█████╔╝
# ╚═════╝        ╚════╝ ╚═╝╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚════╝
# Advance Tracking Tool
import cv2
import time
import mediapipe as mp
import pyttsx3 as pt


# Speak Detection Captured
def initialize_detection(x, y):
    engine = pt.init()
    engine.setProperty('volume', 1.0)  # Set volume (0.0 to 1.0)

    if x <= 30 and y <= 30:
        text = "detection captured camp one"

        engine.say(text)
        engine.runAndWait()

    if xsubOne >= 600 and ysubOne <= 30:
        text = "detection captured camp two"

        engine.say(text)
        engine.runAndWait()


# Setting Up for Video Capture
video_streaming = cv2.VideoCapture(0)
setting = mp.solutions.hands
hands = setting.Hands()
drawing_tools = mp.solutions.drawing_utils
drawing_style = mp.solutions.drawing_styles

cTime = 0
pTime = 0
xsubOne = None
ysubOne = None

while True:
    ret, frame = video_streaming.read()
    convertRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(convertRGB)

    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            for id, lm in enumerate(landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                cv2.putText(frame, "1", (5, 40), cv2.FONT_HERSHEY_PLAIN, 3, (3, 253, 69), 3)

                cv2.putText(frame, "2", (600, 40), cv2.FONT_HERSHEY_PLAIN, 3, (3, 253, 69), 3)

                if id == 8:
                    xsubOne, ysubOne = cx, cy
                    print(xsubOne, ysubOne)

                    if xsubOne <= 30 and ysubOne <= 30:
                        initialize_detection(xsubOne, ysubOne)

                    if xsubOne >= 600 and ysubOne <= 30:
                        initialize_detection(xsubOne, ysubOne)

            drawing_tools.draw_landmarks(
                frame, landmarks, setting.HAND_CONNECTIONS,
                landmark_drawing_spec=drawing_style.get_default_hand_landmarks_style(),
                connection_drawing_spec=mp.solutions.drawing_styles.DrawingSpec(
                    color=(3, 290, 69), thickness=1, circle_radius=1
                )
            )

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, f'{int(fps)}FPS', (288, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0, 0), 2)
    cv2.imshow("D-Jistro", frame)

    if cv2.waitKey(1) == 113:
        break

video_streaming.release()
cv2.destroyAllWindows()
