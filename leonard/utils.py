"""
Utility functions for leonard
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from astropy.utils.data import download_file

__all__ = ['get_example_data']

example_data_url = ('http://staff.washington.edu/bmmorris/docs/'
                    'kplr010748390-2009291181958_slc.fits')


def get_example_data(cache=True):
    """
    Download example Kepler light curve of HAT-P-11.

    Parameters
    ----------
    cache : bool (optional)
        Cache the data file locally. Default is `True`.

    Returns
    -------
    path : str
        Path to the downloaded file.
    """
    return [download_file(example_data_url, cache=cache)]
