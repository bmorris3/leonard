from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
from astropy.time import Time
from astropy.tests.helper import remote_data
from numpy.testing import assert_allclose

from ..lightcurve import LightCurve, hat11_params
from ..utils import get_example_data


def generate_example_light_curve():
    """
    This method locally generates inputs to test the LightCurve object.
    This allows us to *not* depend on remote data for some tests.
    """
    times = np.linspace(2455094.5984289846, 2455119.0377075179, 10000)
    fluxes = 10 + 0.01 * np.random.randn(len(times))
    errors = 0.01 * np.ones_like(fluxes)
    quarters = 99 * np.ones_like(fluxes)
    return dict(times=times, fluxes=fluxes, errors=errors, quarters=quarters,
                name='test light curve')


def test_lc_attributes():
    """
    Check that the light curve has the right attributes.

    You can test this locally with:

    python -c "from leonard.tests.test_lightcurve import test_lc_attributes as f; f()"
    """
    example_inputs = generate_example_light_curve()
    whole_lc = LightCurve(**example_inputs)

    assert hasattr(whole_lc, 'times')
    assert hasattr(whole_lc, 'fluxes')
    assert hasattr(whole_lc, 'errors')

    # Check that type casting happens as it's supposed to:
    assert isinstance(whole_lc.times, Time)

@remote_data
def test_normalization():
    """
    python -c "from leonard.tests.test_lightcurve import test_normalization as f; f()"
    """

    # Download (or retrieve cached) example Kepler light curve
    light_curve_paths = get_example_data()

    # Get the HAT-P-11 system properties
    params = hat11_params()

    # Construct light curve object from the raw data
    whole_lc = LightCurve.from_raw_fits(light_curve_paths, name='HAT11')

    # Mask the out of transit portions of the light curve
    transits_only_lc = LightCurve(**whole_lc.mask_out_of_transit(params))

    # Split up the light curve into a list of transit light curves
    transits = transits_only_lc.get_transit_light_curves(params)

    # Select one transit to work on
    transit = transits[3]

    # Remove a linear baseline trend from the light curve
    transit.remove_linear_baseline(params)

    # Verify that the light curve is appropriately normalized
    calculated_median_flux = np.median(transit.fluxes)
    expected_median_flux = 1.0
    absolute_tolerance = 0.01

    assert_allclose(calculated_median_flux, expected_median_flux,
                    atol=absolute_tolerance)
