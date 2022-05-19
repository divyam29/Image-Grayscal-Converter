import cv2
import glob
import os

for i,filename in enumerate(glob.glob('flower/*.jpg'),1):
    img = cv2.imread(filename)
    scale_percent = 50  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
    path = 'modified_images'
    cv2.imwrite(os.path.join(path, 'flower{}.jpg'.format(i)), gray)
