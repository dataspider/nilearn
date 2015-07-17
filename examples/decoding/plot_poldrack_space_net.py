"""
SpaceNet on Jimura et al "mixed gambles" dataset.
==================================================

The segmenting power of SpaceNet is quiete visible here.
"""
# author: DOHMATOB Elvis Dopgima,
#         GRAMFORT Alexandre


### Load data ################################################################
from nilearn.datasets import fetch_mixed_gambles
data = fetch_mixed_gambles(n_subjects=16, make_Xy=True)
X, y, mask_img = data.X, data.y, data.mask_img


### Fit TV-L1 #################################################################
penalty = "tv-l1"
from nilearn.decoding import SpaceNetRegressor
decoder = SpaceNetRegressor(mask=mask_img, penalty=penalty,
                            eps=1e-1,  # prefer large alphas
                            memory="cache", verbose=2)
decoder.fit(X, y)  # fit

### Visualize TV-L1 weights
import matplotlib.pyplot as plt
from nilearn.plotting import plot_stat_map
from nilearn.image import mean_img
plot_stat_map(mean_img(decoder.coef_img_), title=penalty, display_mode="yz",
              cut_coords=[20, -2])


### Fit Graph-Net ##########################################################
penalty = "graph-net"
decoder = SpaceNetRegressor(mask=mask_img, penalty=penalty,
                            eps=1e-1,  # prefer large alphas
                            memory="cache", verbose=2)
decoder.fit(X, y)  # fit

### Visualize Graph-Net weights
plot_stat_map(mean_img(decoder.coef_img_), title=penalty, display_mode="yz",
              cut_coords=[20, -2])


plt.show()
