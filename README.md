# `leonard`: a simple light curve package

Store your light curves in a handy `LightCurve` object. 

Install with: 

```
pip install leonard
```

Getting started:

```python
from leonard import LightCurve, hat11_params, get_example_data

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

# Plot the light curve
transit.plot()
```

