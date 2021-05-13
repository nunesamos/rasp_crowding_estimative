import cv2
import matplotlib.pyplot as plt
import numpy as np

def differenceImage(img1, img2):
  a = img1-img2
  b = np.uint8(img1<img2) * 254 + 1
  c = np.ones(img1.shape) * 50
  d = np.uint8(np.uint8(a * b) > c)
  print(d)
  return np.uint8(img1*d*0.8+img1*0.2)
  #return np.uint8(a*b)

img1 = cv2.imread('imgs/mercado5.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('imgs/fundo_mercado1.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('Processamento de Imagem')

imS = cv2.resize(differenceImage(img1, img2), (960, 540))  

#imS = cv2.resize(np.uint8(img1 * np.ones(img1.shape)*255), (960, 540))

plt.imshow(imS, cmap ='gray')
plt.show()

print(img1[0,1])
print(img2[0,1])
print(imS[0,1])
#print(differenceImage(img2[0,1,0], img1[0,1,0]))

if (img1[0,1,0] > img2[0,1,0]) :
    print("ok")

