from skimage.filters import median
from skimage.io import imread, imsave
from skimage.morphology import disk
from skimage import  img_as_ubyte, img_as_float


def median_blur(image):
    blur_img = median(image,disk(5))
    imsave('median.png',blur_img)
