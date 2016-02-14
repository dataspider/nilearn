"""
Visualizing multiscale functional brain parcellations
=====================================================

This example shows how to download and fetch brain parcellations of
multiple networks using :func:`nilearn.datasets.fetch_atlas_basc_multiscale`
and visualize them using plotting function :func:`nilearn.plotting.plot_roi`.

We show here only three different networks of symmetric version. For more
details about different versions and different networks, please refer to its
documentation.
"""

################################################################################
# Fetching multiscale group brain parcellations
# Import datasets module and use fetch_atlas_basc_multiscale function
from nilearn import datasets

parcellations = datasets.fetch_atlas_basc_multiscale(version='sym')

# We show here networks of 64, 197, 444
networks_64 = parcellations['scale064']
networks_197 = parcellations['scale197']
networks_444 = parcellations['scale444']

################################################################################
# Visualizing brain parcellations
# Import plotting module and use plot_roi function, since the maps are in 3D
import matplotlib.pyplot as plt
from nilearn import plotting

# The coordinates of all plots are selected automatically by itself
# We manually change the colormap of our choice
plotting.plot_roi(networks_64, cmap=plotting.cm.bwr,
                  title='64 regions of brain clusters')

plotting.plot_roi(networks_197, cmap=plotting.cm.bwr,
                  title='197 regions of brain clusters')

plotting.plot_roi(networks_444, cmap=plotting.cm.bwr_r,
                  title='444 regions of brain clusters')

plotting.show()
