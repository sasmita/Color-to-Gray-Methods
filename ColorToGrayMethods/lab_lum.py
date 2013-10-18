import numpy as np
import cv2
from skimage import color

def lab_luminance(image):

   lab = color.rgb2lab(image)

   num_rows = image.shape[0]
   num_cols = image.shape[1]

   output = np.zeros((num_rows, num_cols), dtype = image.dtype)
   
   for i in range(0, num_rows):
     for j in range(0, num_cols):
       l = image[i,j,0];
       output[i, j] = l
 
   return output
  
#rgb = cv2.imread('./images/sasmita.jpg');
#output1 = lab_luminance(rgb);
#cv2.imwrite('./output/sasmita_lab_luminance.jpg', output1);

