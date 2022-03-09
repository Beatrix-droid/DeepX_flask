import numpy as np


def predict_image(generator,mask):
    mask=np.array(mask)/255
    mask[mask>0.5]=1
    mask[mask<=0.5]=0
    mask = mask.reshape((1,256,256,3))
    img = generator(mask,training=True)[0]
    return np.array(img)
