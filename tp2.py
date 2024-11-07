import cv2
import numpy as np
import matplotlib.pyplot as plt

from numpy.lib.shape_base import vsplit

img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
img[:] =img[:]/2
if img is None:
    print("Erreur : L'image n'a pas pu être chargée. Vérifiez le chemin du fichier.")
    exit()

imgNorm = np.zeros((img.shape), np.uint8)
h, w = img.shape
min = 255
max = 0
for y in range(h):
    for x in range(w):
        if img[y, x] > max:
            max = img[y, x]
        if img[y, x] < min:
            min = img[y, x]

for y in range(h):
    for x in range(w):
        imgNorm[y, x] = (img[y, x] - min) * 255 / (max - min)

cv2.imshow('image source', img)
cv2.imshow('image normal', imgNorm)

# TP2: Histograms
hist1 = np.zeros((256, 1), np.uint16)
for y in range(h):
    for x in range(w):
        hist1[img[y, x], 0] += 1

hist2 = cv2.calcHist([imgNorm], [0], None, [256], [0, 255])

plt.figure()
plt.title('Image normalisee')
plt.xlabel('GrayScale')
plt.ylabel('nbPixels')
plt.plot(hist2)
plt.plot(hist1)
plt.xlim([0, 255])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
