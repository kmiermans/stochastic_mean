# Synopsis
Do you have a stochastic trajectory of ![math](http://mathurl.com/y8nuzht2.png) and need to compute ![math](http://mathurl.com/y7fw6bk4.png) or another arbitrary ![math](http://mathurl.com/ybzzbmxf.png) ? Then the function in this Python file will be useful for you. Estimating such an ensemble average from a time-trajectory are often used in soft-matter physics, e.g. to investigate diffusion of a particle ![url](http://mathurl.com/y9ukbenk.png). 

# Usage
Usage is very easy. You can run an example script (which shows a Matplotlib window) by simply running the script, i.e. `>>> python ComputeStochasticMean.py`. For your own usage, you simply call the function
```python
bins_out, result = compute_stochastic_mean(x,y,bins,func)
```
## Input
Here, `x` is an instance  of `numpy.array` of  `N` elements and represents the time-like variable and `y` is also a numpy array of `N` elements and represents the coordinate-like variable (![math](http://mathurl.com/2ub7uy2.png) in the above description). `func` is a function which takes two arguments, namely ![math](http://mathurl.com/y8c68jfr.png). There are three possibilities for `func` pre-defined, namely the identity (![url](http://mathurl.com/y8nqwu8w.png)), the MSD (![url](http://mathurl.com/y8ushpkv.png)) and the autocorrelator function (![url](http://mathurl.com/yddz5szw.png)).

## Output
`bins_out` and `result` are a numpy array of length `len(bins)-1` since the last bin in `bins` does not have a right edge (and hence we cannot bin the data for the rightmost bin).  

# Installation
This is a single-file script. Just download and use right away!

# License
GPL. When using, please cite C.A.Miermans.
