import cv2
import numpy as np

def average(image):
  '''Converts an image to greyscale by using average technique.

     'image' is a three dimensional array(num_rows,num_columns,num_channels), 
     where number channels is 3.
 
     'output' is a two dimensional array(rows,columns)
  '''

  num_rows = image.shape[0]
  num_cols = image.shape[1]

  output_float = np.zeros((num_rows, num_cols), dtype = float)

  for i in range(0, num_rows):
    for j in range(0, num_cols):
      r = float(image[i,j,2]);
      g = float(image[i,j,1]);
      b = float(image[i,j,0]);
      output_float[i,j] = (r+g+b)/3.0;

  output = output_float.astype(image.dtype)

  return output

#input2 = cv2.imread('./images/sasmita.jpg')
#output2 = average(input2);
#cv2.imwrite('./output/sasmita_average.jpg', output2);
