import sys
import glob
import cv2
import numpy as np

# 1

folder_path = '/Users/junho/Desktop/main/big_data/lecture/week9/data/images'
img_files = glob.glob(f'{folder_path}/*.jpg')
img_files
if not img_files:
    print("there are no jpg files in 'image' folder. ")
    sys.exit()

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('image load fail')
        break

    cv2.imshow('image',img)
    if cv2.waitKey(1000) >= 0:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()

# 2
cat_bmp_path = '/Users/junho/Desktop/main/big_data/lecture/week9/data/cat.bmp'
img1 = cv2.imread(cat_bmp_path,cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(cat_bmp_path,cv2.IMREAD_COLOR)
print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img1.ndim)
print(img2.ndim)

h,w = img2.shape[:2]
print(f'img2 size : {w} x {h}')
if len(img1.shape) == 2:
    print('img1 is grayscale')
elif len(img1.shape) == 3:
    print('img1 is truecolor')

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()

for y in range(h):
    for x in range(w):
        img1[y,x] = 255
        img2[y,x] = (0,0,255) # cmap

# img1[:,:] = 255
# img2[:,:] = (0,0,255)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()
cv2.destroyAllWindows()

# 3 ndarray initialize
img1 = np.empty((240,320),dtype=np.uint8) # gray scale img
img2 = np.zeros((240,320,3),dtype=np.uint8) # color : black (0,0,0) : default
img3 = np.ones((240,320),dtype=np.uint8) # gray : black
img4 = np.full((240,320,3),dtype=np.uint8)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 4
img1 = cv2.imread('../main/big_data/lecture/week9/data/movies/HappyFish.jpg')
img2 = img1
img3 = img1.copy()
# img2 는 같은 메모리 : 둘중 하나만 바꾸어도 변화
# img3 는 복사본 : 자유롭게 사용

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()
cv2.destroyAllWindows()


img1 = cv2.imread('../main/big_data/lecture/week9/data/movies/HappyFish.jpg')
img2 = img1[40:120,30:150]
img3 = img1[40:120,30:150].copy()

img2.fill(0)
img2.shape
img3.shape

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()
cv2.destroyAllWindows()