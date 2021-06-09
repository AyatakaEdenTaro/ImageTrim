import shutil
import cv2

BEFORE_IMAGE_PATH = "./before/report.png"
AFTER_IMAGE_PATH = "./after/report.png"

shutil.copyfile(BEFORE_IMAGE_PATH, AFTER_IMAGE_PATH)

img = cv2.imread(AFTER_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

print(img.shape)

get_trim_x = img.shape[1]
get_trim_y = img.shape[0]

for x in range(img.shape[1]):
    if img[0][x] == 0:
        get_trim_x = x
        break

for y in range(img.shape[0]):
    if img[y][0] == 0:
        get_trim_y = y
        break

print(get_trim_x)
print(get_trim_y)

trim_img = img[0 : get_trim_y,0 : get_trim_x]
cv2.imwrite(AFTER_IMAGE_PATH, trim_img)



"""
print(img.size)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        r,g,b = img.getpixel((x,y))
        if(x==0):
            if(r==0 and g==0 and b==0):
                print("黒になったy座標"+str(y))
        elif(y==0):
            if(r==0 and g==0 and b==0):
                print("黒になったx座標"+str(x))
"""
