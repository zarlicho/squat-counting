import mediapipe as mp
import cv2
import time
# import tensorflow.keras
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
im_crop = []
count = 0
stage = None
while True:
    success, img = cap.read()
    list = []
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            list.append(lm)

    if len(list) != 0:
        h, w, c = img.shape
        wv = 308
        hb = 504
        apr = 10
        w1, w2 = int(list[6].x * w), int(list[6].y * h)
        h1, h2 = int(list[7].x * w), int(list[9].y * h)
        w2 = (w2- (h2 - w2))
        x1 = int(list[6].x)
        y1 = int(list[6].y)
        y1 = (y1- (y1 - y1))
        # print(w1, w2)
        if w2 < 260:
            stage="UP"
        if w2 > 320 and stage=="UP":
            stage="DOWN"
            count+=1
            # print(count)
        cv2.rectangle(img, (0,0), (225,73), (245,117,16), -1)
        cv2.putText(img, str(count), 
                (10,60), 
                cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 3, cv2.LINE_AA)
        im_crop = img[int(w2):int(w2+hb),
                    int(w1):int(w1+wv)]
        # cv2.rectangle(img, (w1 - apr, w2- apr), (h1+apr, h2+apr), (255,0,0), 2)
    cv2.imshow("image", img)
    #cv2.imshow('crop', im_crop)
    cv2.waitKey(1)
