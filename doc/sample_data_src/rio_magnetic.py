# Copyright (c) 2017 The Verde Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
"""
[DEPRECATED] Magnetic data from Rio de Janeiro
==============================================

.. warning::

    All sample datasets in Verde are deprecated and will be
    **removed in Verde v2.0.0**.
    The tutorials/examples will transition to using
    `Ensaio <https://www.fatiando.org/ensaio/>`__ instead.

We provide sample total-field magnetic anomaly data from an airborne survey of
Rio de Janeiro, Brazil, from the 1970s. The data are made available by the
Geological Survey of Brazil (CPRM) through their `GEOSGB portal
<http://geosgb.cprm.gov.br/>`__. See the documentation for
:func:`verde.datasets.fetch_rio_magnetic` for more details.
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import verde as vd

# The data are in a pandas.DataFrame
data = vd.datasets.fetch_rio_magnetic()
print(data.head())

# Make a Mercator map of the data using Cartopy
crs = ccrs.PlateCarree()
plt.figure(figsize=(7, 5))
ax = plt.axes(projection=ccrs.Mercator())
ax.set_title("Total-field Magnetic Anomaly of Rio de Janeiro")
# Since the data is diverging (going from negative to positive) we need to
# center our colorbar on 0. To do this, we calculate the maximum absolute value
# of the data to set vmin and vmax.
maxabs = vd.maxabs(data.total_field_anomaly_nt)
# Cartopy requires setting the projection of the original data through the
# transform argument. Use PlateCarree for geographic data.
plt.scatter(
    data.longitude,
    data.latitude,
    c=data.total_field_anomaly_nt,
    s=1,
    cmap="seismic",
    vmin=-maxabs,
    vmax=maxabs,
    transform=crs,
)
plt.colorbar(pad=0.01).set_label("nT")
# Set the proper ticks for a Cartopy map
vd.datasets.setup_rio_magnetic_map(ax)
plt.show()
