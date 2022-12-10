import matplotlib.pyplot as plt
import numpy as np
from gaussianPlumeModel import x,y,C1

def overlay_on_map():
    import scipy.io as sio

    # Overlay concentrations on map
    plt.ion()
    mat_contents = sio.loadmat('map') # We should upload our own map for the map.mat file
    plt.figure()
    plt.imshow(mat_contents['M'])
               
    plt.xlabel('x (m)') 
    plt.ylabel('y (m)') 
    cs=plt.contour(x,y,np.mean(C1,axis=2)*1e6, cmap='hot')
    plt.clabel(cs,cs.levels,inline=True, fmt='%.1f',fontsize=5)

    plt.show(block=False)
    plt.pause(0)
    plt.close()

    return
    
if __name__ == "__main__":
    overlay_on_map()
