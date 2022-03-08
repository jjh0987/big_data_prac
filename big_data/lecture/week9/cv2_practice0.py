import sys

import cv2
import matplotlib.pyplot as plt
print(cv2.__version__)
path = '../main/big_data/lecture/week9/data/cat.bmp'
img = cv2.imread(path)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

if img is None:
    print('image load failed')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
# cv2.destroyWindow('image')
# img write
cv2.imwrite('../main/big_data/lecture/week9/data/cat.png',img)

#
path = '../main/big_data/lecture/week9/data/cat.bmp'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
plt.imshow(img)
plt.imshow(img,cmap='gray')
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
img.shape

if img is None:
    print('image load failed')
    sys.exit()

# 확장자 변경
# img : bmp file
cv2.imwrite('../main/big_data/lecture/week9/data/cat_gray.png',img)

path = '../main/big_data/lecture/week9/data/cat_gray.png'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
cv2.imshow('../main/big_data/lecture/week9/data/cat_gray.png',img)
cv2.waitKey()
cv2.destroyAllWindows()

#
path = '../main/big_data/lecture/week9/data/cat.bmp'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey()

# 키 할당
while True:
    if cv2.waitKey() == ord('q'):
        cv2.destroyAllWindows()
        print(1)
        break


imgBGR = cv2.imread(path)
imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(imgRGB)
plt.imshow(imgBGR)

img_gray = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(img_gray,cmap='gray')

plt.subplot(121)
plt.axis('off')
plt.imshow(imgRGB)
plt.subplot(122)
plt.axis('off')
plt.imshow(img_gray,cmap='gray')
