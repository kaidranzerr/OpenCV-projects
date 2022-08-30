# STEP 1--> IMPORTING LIBRARIES
# STEP 2--> DETECTING THE FACE
# STEP 3--> SHOW THE FACE AND LANDMARKS ON IT
# STEP 4--> MOVE THE EYE TO MOVE THE CURSOR
# STEP 5--> WINK FOR CLICKING USING EYE MOUSE

import cv2
import mediapipe as mp
import pyautogui

# open webcam and capture face
cam = cv2.VideoCapture(0)

# detect the face
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# getting the screen size
screen_w, screen_h = pyautogui.size()
while True:
    # read every frame of the camera
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    # this will help us to detect all the landmarks on the face
    landmarks_points = output.multi_face_landmarks
    # frame width and height
    frame_h, frame_w, _ = frame.shape
    if landmarks_points:
        landmarks = landmarks_points[0].landmark
        # loop theough all the landmarks and draw some points
        # whenver working with images we use enumerate instead of range
        for id, landmark in enumerate(landmarks[474:478]):
            #enumerate will give us 2 things 1st is id/index and the second one is element landmark
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            #draw the circles on the specific landmarks
            cv2.circle(frame, (x, y), 1, (0, 255, 0))
            #this line means draw a circle with centre (x,y) and radius 1 unit with green color
            if id == 1:
                screen_x = screen_w/frame_w * x
                screen_y = screen_h/frame_h * y
                # time to move the cursor according to the eye
                pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            #top and bottom of left eye
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 1, (0, 255, 255))
            if(left[0].y-left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

# just adding another comment to edit code on github