import cv2
import mediapipe as mp
import serial

# Used to convert protobuf message to a dictionary.
from google.protobuf.json_format import MessageToDict

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,model_complexity=1,min_detection_confidence=0.75,min_tracking_confidence=0.75,max_num_hands=2)

# Start capturing video from webcam
cam = cv2.VideoCapture(0)

# Establish serial communication with Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600) 

while True:
    # Read video frame by frame
    success, img = cam.read()

    # Check if frame was read successfully
    if not success:
        print("Failed to read frame from webcam")
        break

    # Flip the image(frame)
    img = cv2.flip(img, 1)

    # Convert BGR image to RGB image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    results = hands.process(imgRGB)

    # Variable to keep track if any hands are detected
    hands_detected = False

    # If hands are present in image(frame)
    if results.multi_hand_landmarks:

        # If both hands are present
        if len(results.multi_handedness) == 2:
            # Display 'Both Hands' on the image
            cv2.putText(img, 'Both Hands', (250, 50),cv2.FONT_ITALIC, 0.9 , (255, 0, 0), 3) 
            arduino.write(b'B')  # Send 'BB' to Arduino to set pin 3 and pin 4 high
            hands_detected = True

        # If only one hand is present
        else:
            for i in results.multi_handedness:
                # Return whether it is Right or Left Hand
                label = MessageToDict(i)['classification'][0]['label']

                if label == 'Left':
                    # Display 'Left Hand' on
                    # left side of window
                    cv2.putText(img, label+' Hand',
                                (20, 75),
                                cv2.FONT_ITALIC,
                                0.9, (255, 0, 0), 3)
                    arduino.write(b'L')  # Send 'L' to Arduino to set pin 3 high
                    hands_detected = True

                if label == 'Right':
                    # Display 'Right Hand'
                    # on right side of window
                    cv2.putText(img, label+' Hand', (460, 75),
                                cv2.FONT_ITALIC,
                                0.9, (255, 0, 0), 3)
                    arduino.write(b'R')  # Send 'R' to Arduino to set pin 4 high
                    hands_detected = True

    # If no hands are detected
    if not hands_detected:
        cv2.putText(img, 'No Hands', (250, 50),
                    cv2.FONT_ITALIC,
                    0.9, (255, 0, 0), 3)
        arduino.write(b'N')  # Send 'LL' to Arduino to set pin 3 and pin 4 low

    # Display Video and when 'q'
    # is entered, destroy the window
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Close the serial connection
arduino.close()