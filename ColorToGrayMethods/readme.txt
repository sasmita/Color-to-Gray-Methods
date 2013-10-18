
To run the color to gray methods, please use the following command:

python allMethods.py <Path to input color image without extension>

Note: I simplified the program by not passing the file extension as the argument. My program adds the .jpg extension for input, and _out_<technique>.jpg for output images.

Example:

sasmita-mac:code Sasmita$ python allMethods.py images/flower62
average :  0.005561  seconds.
xyz_lum :  0.005978  seconds.
yuv_lum :  0.008313  seconds.
lab_lum :  0.006079  seconds.
lab_lum_en :  0.015271  seconds.
Warning: Maximum number of iterations has been exceeded.
         Current function value: 2876724.525422
         Iterations: 2
         Function evaluations: 25
         Gradient evaluations: 14
color2gray 2 itns:  386.085792  seconds.
....

Here input image is : images/flower62.jpg
Out images are : images/flower62_out_avg.jpg, images/flower62_out_lab.jpg, etc.
