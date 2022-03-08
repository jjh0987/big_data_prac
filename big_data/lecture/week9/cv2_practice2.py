import sys
import glob
import cv2
import numpy as np

# 1 이미지 겹치기 : 마스킹 연산
src = cv2.imread('../main/big_data/lecture/week9/data/movies/airplane.bmp',cv2.IMREAD_COLOR)
mask = cv2.imread('../main/big_data/lecture/week9/data/movies/mask_plane.bmp',cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('../main/big_data/lecture/week9/data/movies/field.bmp',cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('image load fail')
    sys.exit()

cv2.copyTo(src,mask,dst) # mask 영역에 따라 src,dst 할당 : 흰 = src, 검 = dst
cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 2 영상 24frame
cap1 = cv2.VideoCapture('../main/big_data/lecture/week9/data/movies/video1.mp4')
cap2 = cv2.VideoCapture('../main/big_data/lecture/week9/data/movies/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed')
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT)) # 85
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT)) # 121
fps = cap1.get(cv2.CAP_PROP_FPS) # 24
effec_frames = int(fps*2)
delay = int(1000/24)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
# w*h = 1280 * 720
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # ?

# 출력 영상
out = cv2.VideoWriter('../main/big_data/lecture/week9/data/movies/output.avi',fourcc,fps,(w,h))
# flow : 원숭이 영상 뒷컷팅 - 변환점 - 코끼리 영상 앞컷팅
# 원숭이 영상 컷팅
for i in range(frame_cnt1 - effec_frames):
    ret1, frame1 = cap1.read() # 영상의 1 프레임 조각
    if not ret1:
        print('frame read error')

    out.write(frame1) # writing
    print('.')

    cv2.imshow('../main/big_data/lecture/week9/data/movies/output.avi',frame1)
    cv2.waitKey(delay)

# 변환점

for i in range(effec_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # ret : boolean
    if not ret1 or not ret2:
        print('frame read fail')
        sys.exit()

    dx = int(w/effec_frames)*i
    # effec_frames : 48

    frame = np.zeros((h,w,3),dtype=np.uint8)
    frame[:,0:dx,:] = frame2[:,0:dx,:] # width dx # 코끼리 왼쪾 출현
    frame[:,dx:w,:] = frame1[:,dx:w,:]

    out.write(frame) # writing
    print('.')

    cv2.imshow('../main/big_data/lecture/week9/data/movies/output.avi', frame)
    cv2.waitKey(delay)

for i in range(effec_frames,frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print('frame read error')
        sys.exit()

    out.write(frame2)
    print('.')

    cv2.imshow('../main/big_data/lecture/week9/data/movies/output.avi', frame2)
    cv2.waitKey(delay)

print('output.avi generated')

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
