"""
Normalization
==============

A selection of reference compositions are included in pyrolite, and can be easily
accessed with :func:`pyrolite.geochem.norm.get_reference_composition` (see the list
at the bottom of the page for a complete list):
"""
import pandas as pd
import matplotlib.pyplot as plt
import pyrolite.plot
from pyrolite.geochem.ind import REE
from pyrolite.geochem.norm import get_reference_composition, all_reference_compositions

########################################################################################
chondrite = get_reference_composition("Chondrite_PON")
########################################################################################
# To use the compositions with a specific set of units, you can change them with
# :func:`~pyrolite.geochem.norm.Composition.set_units`:
#
CI = chondrite.set_units("ppm")
#########################################################################################
# The :func:`~pyrolite.geochem.pyrochem.normalize_to` method can be used to
# normalise DataFrames to a given reference (e.g. for spiderplots):
#
fig, ax = plt.subplots(1)

for name, ref in list(all_reference_compositions().items())[::2]:
    if name != "Chondrite_PON":
        ref.set_units("ppm")
        df = ref.comp.pyrochem.REE.pyrochem.normalize_to(CI, units="ppm")
        df.pyroplot.REE(unity_line=True, ax=ax, label=name)

ax.set_ylabel("X/X$_{Chondrite}$")
ax.legend(frameon=False, facecolor=None, loc="upper left", bbox_to_anchor=(1.0, 1.0))
plt.show()
########################################################################################
# .. seealso::
#
#   Examples:
#     `Pandas Lambda Ln(REE) Function <../lambdas/pandaslambdas.html>`__,
#     `Lambdas for Dimensional Reduction <../lambdas/lambdadimreduction.html>`__,
#     `REE Radii Plot <../plotting/REE_radii_plot.html>`__
#
# Currently available models include:
#
# |refcomps|
