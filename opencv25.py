import cv2

CAMERA_ID = 0

cam = cv2.VideoCapture(CAMERA_ID)

if cam.isOpened() == False:
    print
    'Cannot open the camera-%d' % (CAMERA_ID)
    exit()

cv2.namedWindow('CAM Window')

while(True):
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('CAM Window', gray)

    key = cv2.waitKey(33)
    if key == ord('a'):
        print('break')
        bg = gray.copy()
        break

flag = False
while(True):
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray, bg)

    if flag:
        bin = cv2.threshold(diff, 117, 255, cv2.THRESH_BINARY)
        cv2.imshow('CAM Window', bin)
    else:
        cv2.imshow('CAM Window', bin)
        

    if key == ord('b'):
        flag = not flag
    
    if key == ord('q'):
        break