## Synopsis
Do you have a stochastic trajectory of ![math](http://mathurl.com/y8nuzht2.png) and need to compute ![math](http://mathurl.com/y7fw6bk4.png) or another arbitrary ![math](http://mathurl.com/ybzzbmxf.png) ? Then the function in this Python file will be useful for you. Estimating such an ensemble average from a time-trajectory are often used in soft-matter physics, e.g. to investigate diffusion of a particle ![url](http://mathurl.com/y9ukbenk.png). 

## Usage
Usage is very easy. You simply call the function
```python
bins_out, result = compute_stochastich_mean(x,y,bins,func)
```
Here, `x` is an instance  of `numpy.array` of  `N` elements and represents the time-like variable and `y` is also a numpy array of `N` elements and represents the coordinate-like variable (![math](http://mathurl.com/2ub7uy2.png) in the above description). `bins_out` and `result` are a numpy array of length `len(bins)-1` since the last bin in `bins` does not have a right edge (and hence we cannot bin the data for the rightmost bin).  

## Installation
This is a single-file script. Just download and use right away!

## License
GPL. When using, please cite C.A.Miermans.
