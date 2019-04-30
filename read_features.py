import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #sift = cv2.xfeatures2d.SIFT_create()
    #kp = sift.detect(frame, None)
    orb = cv2.ORB_create()
    feats= cv2.goodFeaturesToTrack(np.mean(frame, axis=2).astype(np.uint8),3000, qualityLevel=0.01, minDistance=3)
    #keypoints, descriptiors = orb.detectAndCompute(frame, None)

    #frame = cv2.drawKeypoints(frame, keypoints, None)
    for f in feats:
      u,v=map(lambda x: int(round(x)),f[0])
      cv2.circle(frame, (u,v), color=(0,255,0), radius=3)

    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
