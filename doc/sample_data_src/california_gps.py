# Copyright (c) 2017 The Verde Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
[DEPRECATED] GPS velocities from California
===========================================

.. warning::

    All sample datasets in Verde are deprecated and will be
    **removed in Verde v2.0.0**.
    The tutorials/examples will transition to using
    `Ensaio <https://www.fatiando.org/ensaio/>`__ instead.

We provide sample 3-component GPS velocity data from the West coast of the U.S.
The data were cut from EarthScope Plate Boundary Observatory data provided by
UNAVCO. The velocities are in the North American tectonic plate reference
system (NAM08). The velocities and their associated standard deviations are in
meters/year.
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import verde as vd

# The data are in a pandas.DataFrame
data = vd.datasets.fetch_california_gps()
print(data.head())


# Make a plot of the data using Cartopy to handle projections and coastlines
crs = ccrs.PlateCarree()
fig, axes = plt.subplots(
    1, 2, figsize=(8, 4), subplot_kw=dict(projection=ccrs.Mercator())
)
# Plot the horizontal velocity vectors
ax = axes[0]
ax.set_title("GPS horizontal velocities")
ax.quiver(
    data.longitude.values,
    data.latitude.values,
    data.velocity_east.values,
    data.velocity_north.values,
    scale=0.3,
    transform=crs,
)
vd.datasets.setup_california_gps_map(ax)
# Plot the vertical velocity
ax = axes[1]
ax.set_title("Vertical velocity")
maxabs = vd.maxabs(data.velocity_up)
tmp = ax.scatter(
    data.longitude,
    data.latitude,
    c=data.velocity_up,
    s=10,
    vmin=-maxabs / 3,
    vmax=maxabs / 3,
    cmap="seismic",
    transform=crs,
)
plt.colorbar(tmp, ax=ax).set_label("meters/year")
vd.datasets.setup_california_gps_map(ax)
plt.show()
