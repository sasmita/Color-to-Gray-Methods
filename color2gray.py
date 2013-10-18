
import sys
import numpy as np
import cv2
from skimage import color
import math
from math import *
from scipy.optimize import minimize

# Global variables
theta = radians(180)
alpha = 8 
mu = 6

width = 0
height = 0
lab = 0

# crunch function
def crunch(x):
  res = alpha * tanh(x/alpha)
  return res

# modulus
def modulus(y):
   if y >= 0:
    return y
   elif y < 0:
    return -y

def target_difference(xi, yi, xj, yj):
  li = lab[xi, yi, 0] #luminance at ith pixel
  lj = lab[xj, yj, 0] #luminance at jth pixel

  l_diff = li - lj    #luminance difference

  ai = lab[xi, yi, 1]
  aj = lab[xj, yj, 1]

  a_diff = ai - aj

  bi = lab[xi, yi, 2]
  bj = lab[xj, yj, 2]

  b_diff = bi - bj

  # euclidean norm (c_diff_norm)
  c_diff_norm = sqrt((a_diff) ** 2 + (b_diff) ** 2)

  # v_theta vector
  v_theta_x = cos(theta)
  v_theta_y = sin(theta)

  # dot product
  dot_product = (a_diff * v_theta_x) + (b_diff * v_theta_y)

  p = modulus(l_diff)
  q = crunch(c_diff_norm)

  #finding delta_ij
  if p > q:
    return l_diff
  elif dot_product >= 0:
    return crunch(c_diff_norm)
  else:
    return crunch(-c_diff_norm)

def objective(g):
  
  res = 0
  for xi in range(0, height):
    for yi in range(0, width):
      for xj in range(xi - mu, xi + mu):
        for yj in range(yi - mu, yi + mu):

          if xj >= 0 and xj < height and yj >=0 and yj < width:
            i = xi * width + yi
            j = xj * width + yj

            g_diff = float(g[i]) - float(g[j])
            t_diff = target_difference(xi, yi, xj, yj)

            res = res + (g_diff - t_diff) ** 2

  return res

def objective_der(g):
  
  der = np.zeros_like(g)

  for xi in range(0, height):
    for yi in range(0, width):

      i = xi * width + yi;
      res = 0

      for xj in range (xi - mu, xi + mu):
        for yj in range (yi - mu, yi + mu):
          if xj >= 0 and xj < height and yj >=0 and yj < width:
            j = xj * width + yj
            g_diff = float(g[i]) - float(g[j])
            t_diff = target_difference(xi, yi, xj, yj)

            res = res + 2 * (g_diff - t_diff)

      der[i] = res 

  return der      

def color2gray(image, itns):

  global width
  global height
  global lab

  width = image.shape[1]
  height = image.shape[0]
 
 # Convert rgb to lab color space
  lab = color.rgb2lab(image);

  g0 = lab[:, :, 0]
  g0 = g0.astype(np.uint8)
  g0 = g0.flatten()

  # Solve Least square Optimization
  res = minimize(objective, g0, method='BFGS', jac=objective_der, options={'maxiter':itns, 'disp': True})
  
  output = res.x.reshape(height, width)
  output = output.astype(np.uint8)

  output += 50

  return output
