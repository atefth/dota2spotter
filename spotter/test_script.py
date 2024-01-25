samp=r"spotter/assets/tmp/1.png"
t1p = r"spotter/assets/heroes/abaddon.png"
t2p = r"spotter/assets/heroes/nyx_assassin.png"

from PIL import Image, ImageEnhance
import cv2 as cv
import matplotlib.pyplot as plt
import PIL as pil
from skimage.metrics import structural_similarity as ssim

sim = cv.imread(samp, cv.IMREAD_GRAYSCALE)
t1im = cv.imread(t1p, cv.IMREAD_GRAYSCALE)
t2im = cv.imread(t2p, cv.IMREAD_GRAYSCALE)

# sim = Image.open(samp)
# t1im = Image.open(t1p)
# t2im = Image.open(t2p)

"""
#cv.imshow("",t1im)
plt.imshow(t1im)#, cmap='gray')
plt.show()
"""

# t1im = t1im.resize(sim.size, resample=Image.NEAREST, box=None, reducing_gap=None)
# t2im = t2im.resize(sim.size, resample=Image.NEAREST, box=None, reducing_gap=None)

t1im = cv.resize(t1im, (sim.shape[1], sim.shape[0]), interpolation=cv.INTER_NEAREST)
t2im = cv.resize(t2im, (sim.shape[1], sim.shape[0]), interpolation=cv.INTER_NEAREST)
# t1im_r = cv.resize(t1im, (251, 141))#, interpolation=cv.INTER_NEAREST)
# t2im = cv.resize(t2im, sim.shape)#, interpolation=cv.INTER_NEAREST)

"""
plt.imshow(t1im)#, cmap='gray')
plt.show()
"""
s1 = ssim(sim, t1im)
s2 = ssim(sim, t2im)
