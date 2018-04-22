"""
This example demonstrates how to use NumPy to do image transition.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def image_load(filename):
    return plt.imread(filename)

def convert_bw(img):
    img = img.astype('uint8')
    print("Shape Original ndarray:")
    print(img.shape)
    print("Shape Original ndarray:")
    print(img)
    
    gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
    gray = gray.astype('uint8')
    
    print(gray)
    
    
    #b = np.average(img, axis=1).astype('uint8')
    #b = img.sum(axis=1)
    #b = b.astype('uint8')
    b = np.mean(img, -1).astype('uint8')
    
    
    
    
    print("Shape b ndarray:")
    print(b.shape)
    print("Shape b ndarray:")
    
    b = np.repeat(b,3).reshape(480,800,3)
    
    return b

    
    
    
    #b[np.newaxis,:]
    '''
    
    print(b)
    print(b.shape)
'''
    




def image_gen(file1, file2, steps=30):
    """Generator for image arrays."""
    img1 = image_load(file1)     # load the two image files into ndarrays
    img2 = image_load(file2)
    
    img2 = convert_bw(img2);
    
    
    if img1.shape != img2.shape:
        print("Error: the two images have different shapes.", file=sys.stderr)
        exit(2)
        
    # go from img1 to img2 than back to img1. s varies from 0 to 1 and then back to 0:
    svalues = np.hstack([np.linspace(0.0, 1.0, steps), np.linspace(1.0, 0, steps)])

    # construct now the list of images, so that we don't have to repeat that later:
    images = [np.uint8(img1 * (1.0 - s) + img2 * s) for s in svalues]    

    # get a  new image as a combination of img1 and img2
    while True:             # repeat all images in a loop
        for img in images:
           yield img 
            
fig = plt.figure()
# create image plot and indicate this is animated. Start with an image.
im = plt.imshow(image_load("florida-keys-800-480.jpg"), interpolation='none', animated=True)

# the two images must have the same shape:
imggen = image_gen("florida-keys-800-480.jpg", "Grand_Teton-800-480.jpg", steps=30)

# updatefig is called for each frame, each update interval:
def updatefig(*args):
    global imggen
    img_array = next(imggen)     # get next image animation frame
    im.set_array(img_array)       # set it. FuncAnimation will display it
    return (im,)

# create animation object that will call function updatefig every 60 ms
#%matplotlib qt
ani = animation.FuncAnimation(fig, updatefig, interval=60, blit=False)
plt.title("Image transformation")
plt.show()
