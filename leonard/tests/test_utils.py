"""
This is an example test module.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from ..utils import get_example_data

import os

from astropy.io import fits
from astropy.tests.helper import remote_data


def this_wont_get_run():
    raise ValueError("This function should not be touched by the tests "
                     "because its name doesnt start with `test_*`.")


@remote_data
def test_example_data():
    """
    This is a functional test, it tests the functionality of a whole
    function/method.

    You can test that this function works locally from the command line with:

    python -c "from leonard.tests.test_utils import get_example_data as f; f()"

    Note the ``remote_data`` decorator on this function -- this ensures that the
    test will only be run if the ``remote_data`` flag is activated on the
    testing options.
    """
    example_file_paths = get_example_data()

    # You `assert` the things that you should be True if the function is working
    assert len(example_file_paths) == 1
    assert os.path.exists(example_file_paths[0])

    data = fits.getdata(example_file_paths[0])

    expected_keys = ['TIME', 'SAP_FLUX']
    for card in expected_keys:
        assert card in data.names
