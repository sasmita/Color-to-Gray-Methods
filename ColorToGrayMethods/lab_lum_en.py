import numpy as np
import cv2
from skimage import color

# image is in rgb color space
def lab_enhancement(image):
 
 lab = color.rgb2lab(image)

 l = lab[:, :, 0]
 h = l.flatten()

 minimum = min(h)
 maximum = max(h)

 num_rows = l.shape[0]
 num_cols = l.shape[1]

 result = np.zeros((num_rows, num_cols), dtype = l.dtype)

 for i in range(0,num_rows):
  for j in range(0, num_cols):
     x = l[i,j]
     res = (255/(maximum - minimum)) * (x - minimum)
     result[i, j] = res
 
 out = result.astype(image.dtype)  
 return out

#rgb = cv2.imread('images/sasmita.jpg')
#output1 = lab_enhancement(rgb)
#cv2.imwrite('./output/sasmita_lab_enhancement.jpg', output1)

