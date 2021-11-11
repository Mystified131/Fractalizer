import numpy as np
import PIL
from PIL import Image

def horizontal_set(ilist):
    imgs  = [ PIL.Image.open(i) for i in ilist ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    return(imgs_comb)

def vertical_set(ilist):
    imgs  = [ PIL.Image.open(i) for i in ilist ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    return(imgs_comb)

finalimg = horizontal_set(ilist)
finalimg.save( 'ThreeHoriz.jpg' )   