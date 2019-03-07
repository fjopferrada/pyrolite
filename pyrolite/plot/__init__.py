import matplotlib.pyplot as plt
import pandas as pd
import logging
import numpy as np

logging.getLogger(__name__).addHandler(logging.NullHandler())
logger = logging.getLogger(__name__)

from ..util.pd import to_frame
from ..util.meta import get_additional_params
from ..geochem import common_elements, REE
from . import density
from . import spider
from . import ternary

# pyroplot added to __all__ for docs
__all__ = ["density", "spider", "ternary", "pyroplot"]

import pandas as pd


@pd.api.extensions.register_series_accessor("pyroplot")
@pd.api.extensions.register_dataframe_accessor("pyroplot")
class pyroplot(object):
    """
    Custom dataframe accessor for pyrolite plotting.

    Note
    -----
    This accessor enables the coexistence of array-based plotting functions and
    methods for pandas objects. This enables some separation of concerns.
    """
    def __init__(self, obj):
        self._validate(obj)
        self._obj = obj

    @staticmethod
    def _validate(obj):
        pass

    def density(self, components: list = None, ax=None, axlabels=True, **kwargs):
        r"""
        Passes the pandas object to :func:`~pyrolite.plot.density.density` (see
        `Other Parameters`, below).

        Parameters
        -----------
        components : :class:`list`, None
            Elements or compositional components to plot.
        ax : :class:`matplotlib.axes.Axes`, None
            The subplot to draw on.
        axlabels : :class:`bool`, True
            Whether to add x-y axis labels.

        Other Parameters
        ------------------
        {otherparams}

        Returns
        -------
        :class:`matplotlib.axes.Axes`
            Axes on which the density diagram is plotted.

        Note
        ----
            * Additional keyword arguments are forwarded to :func:`~pyrolite.plot.density.density`.
        """
        obj = to_frame(self._obj)
        try:
            if obj.columns.size not in [2, 3]:
                assert len(components) in [2, 3]

            if components is None:
                components = obj.columns.values
        except:
            msg = "Suggest components or provide a slice of the dataframe."
            raise AssertionError(msg)

        fontsize = kwargs.get("fontsize", 12.0)
        ax = density.density(self._obj.loc[:, components].values, ax=ax, **kwargs)
        if axlabels:
            ax.set_xlabel(components[0], fontsize=fontsize)
            ax.set_ylabel(components[1], fontsize=fontsize)
        return ax

    def ternary(self, components: list = None, ax=None, **kwargs):
        r"""
        Ternary scatter plot. Passes the pandas object to
        :func:`~pyrolite.plot.ternary.ternary` (see `Other Parameters`, below).

        Parameters
        -----------
        components : :class:`list`, `None`
            Elements or compositional components to plot.
        ax : :class:`matplotlib.axes.Axes`, None
            The subplot to draw on.

        {otherparams}

        Returns
        -------
        :class:`matplotlib.axes.Axes`
            Axes on which the ternary diagram is plotted.
        """
        obj = to_frame(self._obj)

        try:
            if not obj.columns.size == 3:
                assert len(components) == 3

            if components is None:
                components = obj.columns.values
        except:
            msg = "Suggest components or provide a slice of the dataframe."
            raise AssertionError(msg)

        fontsize = kwargs.get("fontsize", 10.0)
        ax = ternary.ternary(self._obj.astype(np.float).values, **kwargs)
        tax = ax.tax
        # python-ternary uses "right, top, left"
        # Check if there's already labels
        if not len(tax._labels.keys()):
            tax.right_axis_label(components[0], fontsize=fontsize)
            tax.left_axis_label(components[1], fontsize=fontsize)
            tax.bottom_axis_label(components[2], fontsize=fontsize)
        return ax

    def spider(self, components: list = None, indexes: list = None, ax=None, **kwargs):
        r"""
        Spider plot. Additional keyword arguments are forwarded to
        :func:`~pyrolite.plot.spider.spider` (see below for additional parameters).

        Parameters
        -----------
        components : :class:`list`, `None`
            Elements or compositional components to plot.
        indexes :  :class:`list`, `None`
            Elements or compositional components to plot.
        ax : :class:`matplotlib.axes.Axes`, None
            The subplot to draw on.

        {otherparams}

        Returns
        -------
        :class:`matplotlib.axes.Axes`
            Axes on which the spider diagram is plotted.

        Todo
        ----
            * Add 'compositional data' filter for default components if None is given
        """
        obj = to_frame(self._obj)

        if components is None: # default to plotting elemental data, TODO
            components = [el for el in obj.columns if el in common_elements()]

        assert len(components) != 0

        ax = spider.spider(
            obj.loc[:, components].values,
            indexes=indexes,
            ax=ax,
            **kwargs
        )

        ax.set_xlabel("Element")
        ax.set_xticklabels(components, rotation=60)

        return ax

    def REE(self, ax=None, **kwargs):
        """Pass the pandas object to :func:`pyrolite.plot.spider.REE_v_radii`.

        Parameters
        ------------
        ax : :class:`matplotlib.axes.Axes`, None
            The subplot to draw on.

        {otherparams}

        Returns
        -------
        :class:`matplotlib.axes.Axes`
            Axes on which the REE plot is added.
        """
        obj = to_frame(self._obj)
        ree = REE()

        reedata = obj.loc[:, ree].values
        ax = spider.REE_v_radii(reedata, ree=ree, **kwargs)

        ax.set_ylabel(" $\mathrm{X / X_{Reference}}$")
        ax.set_xlabel("Element")
        return ax


# ideally we would i) check for the same params and ii) aggregate all others across
# inherited or chained functions. This simply imports the params from another docstring
_add_additional_parameters = True

pyroplot.density.__doc__ = pyroplot.density.__doc__.format(
    otherparams=[
        "",
        get_additional_params(
            pyroplot.density,
            density.density,
            header="Other Parameters",
            indent=8,
            subsections=True,
        ),
    ][_add_additional_parameters]
)

pyroplot.ternary.__doc__ = pyroplot.ternary.__doc__.format(
    otherparams=[
        "",
        get_additional_params(
            pyroplot.ternary,
            ternary.ternary,
            header="Other Parameters",
            indent=8,
            subsections=True,
        ),
    ][_add_additional_parameters]
)

pyroplot.spider.__doc__ = pyroplot.spider.__doc__.format(
    otherparams=[
        "",
        get_additional_params(
            pyroplot.spider,
            spider.spider,
            header="Other Parameters",
            indent=8,
            subsections=True,
        ),
    ][_add_additional_parameters]
)

pyroplot.REE.__doc__ = pyroplot.REE.__doc__.format(
    otherparams=[
        "",
        get_additional_params(
            REE,
            spider.REE_v_radii,
            header="Other Parameters",
            indent=8,
            subsections=True,
        ),
    ][_add_additional_parameters]
)