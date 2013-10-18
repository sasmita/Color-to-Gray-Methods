import numpy as np
import cv2

def xyz_luminance(image):
  num_rows = image.shape[0]
  num_cols = image.shape[1]

  output_float = np.zeros((num_rows, num_cols), dtype = float)

  for i in range(0, num_rows):
    for j in range(0, num_cols):
      r = float(image[i, j, 2]);
      g = float(image[i, j, 1]);
      b = float(image[i, j, 0]);
      output_float[i, j] = (0.2126 * r)+(0.7152 * g)+(0.0722 * b)

  output = output_float.astype(image.dtype)

  return output

#input2 = cv2.imread('./images/sasmita.jpg')
#output2 = xyz_luminance(input2)
#cv2.imwrite('./output/sasmita_xyz_luminace.jpg', output2)

