import numpy as np
import cv2

def yuv_luminance(image):

  num_rows = image.shape[0]
  num_cols = image.shape[1]

  output_float = np.zeros((num_rows, num_cols), dtype = float)

  for i in range(0, num_rows):
    for j in range(0, num_cols):
      r = float(image[i, j, 2]);
      g = float(image[i, j, 1]);
      b = float(image[i, j, 0]);
      output_float[i, j] = (0.257 * r) + (0.504 * g) + (0.098 * b) + 16
 

  output = output_float.astype(image.dtype)

  return output

#input2 = cv2.imread('./images/sasmita.jpg')
#output2 = yuv_luminance(input2)
#cv2.imwrite('./output/sasmita_yuv_luminace.jpg', output2)
