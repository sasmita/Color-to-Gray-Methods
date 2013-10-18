
# Author: Sisinty Sasmita Patra
# Runs all other techniques

import cv2
import sys
import time

import average, xyz_lum, yuv_lum, lab_lum, lab_lum_en, color2gray

in_file = sys.argv[1] + ".jpg"
in1 = cv2.imread(in_file)

# average
start = time.clock()
out1 = average.average(in1)
end = time.clock()

out_file = sys.argv[1] + "_out_avg.jpg"
cv2.imwrite(out_file, out1)
print "average : ", end - start, " seconds."

# xyz
start = time.clock()
out1 = xyz_lum.xyz_luminance(in1)
end = time.clock()
out_file = sys.argv[1] + "_out_xyz.jpg"
cv2.imwrite(out_file, out1)
print "xyz_lum : ", end - start, " seconds."

# yuv
start = time.clock()
out1 = yuv_lum.yuv_luminance(in1)
end = time.clock()

out_file = sys.argv[1] + "_out_yuv.jpg"
cv2.imwrite(out_file, out1)
print "yuv_lum : ", end - start, " seconds."

#lab
start = time.clock()
out1 = lab_lum.lab_luminance(in1)
end = time.clock()

out_file = sys.argv[1] + "_out_lab.jpg"
cv2.imwrite(out_file, out1)
print "lab_lum : ", end - start, " seconds."

#lab_en
start = time.clock()
out1 = lab_lum_en.lab_enhancement(in1)
end = time.clock()

out_file = sys.argv[1] + "_out_lab_en.jpg"
cv2.imwrite(out_file, out1)
print "lab_lum_en : ", end - start, " seconds."

#color2gray, 2 itns
start = time.clock()
out1 = color2gray.color2gray(in1, 2)
end = time.clock()

out_file = sys.argv[1] + "_out_color2gray_2.jpg"
cv2.imwrite(out_file, out1)
print "color2gray 2 itns: ", end - start, " seconds."

#color2gray, 10 itns
start = time.clock()
start = time.clock()
out1 = color2gray.color2gray(in1, 10)
end = time.clock()

out_file = sys.argv[1] + "_out_color2gray_10.jpg"
cv2.imwrite(out_file, out1)
print "color2gray 10 itns: ", end - start, " seconds."

#color2gray, 15 itns
start = time.clock()
start = time.clock()
out1 = color2gray.color2gray(in1, 15)
end = time.clock()

out_file = sys.argv[1] + "_out_color2gray_15.jpg"
cv2.imwrite(out_file, out1)
print "color2gray 15 itns: ", end - start, " seconds."
