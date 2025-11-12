# synthetic-seismogram
Simple synthetic 1D seismogram for 2 layered Earth model. Forward model to predict how seismic waves travel through the Earth using convolution of reflection coefficients derived from well log data with ricker wavelet.

Uses `scipy.signal.ricker` to generate wavelet. Input own values of wave speed, density and layer thickness per layer.
