import matplotlib.pyplot as plt
import numpy as np
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def differenceImage(img1, img2):
  a = img1-img2
  b = np.uint8(img1<img2) * 254 + 1
  c = np.ones(img1.shape) * 50
  d = np.uint8(np.uint8(a * b) > c)
  print(d)
  #return np.uint8(img1*d*0.8+img1*0.2)
  return np.uint8(a*b)

def main():
    
    ref_img = plt.imread('imgs/fundo_mercado1.jpg')
    # ref_img = cv2.blur(ref_img, (5, 5))
    test_img_o = plt.imread('imgs/mercado5.jpg')
    test_img = cv2.blur(test_img_o, (7, 7))


    x = rgb2gray(differenceImage(test_img,ref_img))
    x = x/x.max()

    plt.imshow(x, cmap ='gray')
    plt.show()
    plt.imsave('sub_ref_img.jpg', x)
    
    x = cv2.erode(x, np.ones([3, 3]))
    x = cv2.blur(x, (121, 121))

    plt.imshow(x, cmap ='gray')
    plt.show()
    plt.imsave('blur_sub.jpg', x)

    x = x > .125
    x = np.array(x).astype(np.double)

    x = cv2.morphologyEx(x, cv2.MORPH_OPEN, np.ones([19, 19]))
    x = cv2.morphologyEx(x, cv2.MORPH_OPEN, np.ones([19, 19]))

    test_img_o = np.array(test_img_o).astype(np.uint8)
    print(test_img_o.shape, x.shape)

    for n in range(x.shape[0]):
        for m in range(x.shape[1]):
            if x[n,m]==0.0:
                test_img_o[n,m,:] = np.array([0,0,0]).astype(np.uint8)

    plt.imshow(test_img_o, cmap ='gray')
    plt.show()

    plt.imsave('test_res4.jpg', test_img_o)

if __name__=='__main__':
    main()