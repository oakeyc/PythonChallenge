import numpy as np
from scipy.misc import imread, imsave
import pylab as plt
image_data = imread('test.jpg').astype(np.float32)

scaled_image_data = image_data / 255.
#print 'Size: ', image_data.size
#print 'Shape: ', image_data.shape
 
image_slice_red =  scaled_image_data[:,:,0]
image_slice_green =  scaled_image_data[:,:,1]
#print 'Size: ', image_slice_0.size
#print 'Shape: ', image_slice_0.shape
plt.subplot(221)
plt.imshow(image_slice_red)
plt.subplot(222)
plt.imshow(image_slice_green)
plt.subplot(223)
plt.subplot(224)
plt.imshow(scaled_image_data)  
plt.show()

