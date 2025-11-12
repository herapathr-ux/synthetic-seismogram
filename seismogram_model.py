import matplotlib.pyplot as plt
import numpy as np

def travelTime(thickness, density, velocity, timeSamples):
    
    def r(rho1, v1, rho2, v2):
        return (rho2 * v2 - rho1 * v1) / (rho2 * v2 + rho1 * v1)
    
    def t(rho1, v1, rho2, v2):
        return (2 * rho1 * v1) / (rho1 * v1 + rho2 * v2)
    
    r1 = r(density[0], velocity[0], density[1], velocity[1])
    r2 = r(density[1], velocity[1], density[2], velocity[2])
    t1 = t(density[0], velocity[0], density[1], velocity[1])
    t2 = t(density[1], velocity[1], density[2], velocity[2])
    
    # Compute two-way travel times
    t0 = 2 * thickness[0] / velocity[0]
    t1 = t0 + 2 * thickness[1] / velocity[1]    ## Multiples to order N
    
    time_axis = np.linspace(0, t1 * 1.5, timeSamples)
    seismogram = np.zeros(timeSamples)
    
    # Simulate reflections
    idx1 = np.argmin(np.abs(time_axis - t0))
    idx2 = np.argmin(np.abs(time_axis - t1))
    
    seismogram[idx1] = r1
    seismogram[idx2] = r2
    
    # Apply a simple wavelet (Ricker wavelet)
    def ricker_wavelet(f, length, dt):
        t = np.linspace(-length/2, length/2, int(length/dt))
        w = (1 - 2 * (np.pi * f * t)**2) * np.exp(-(np.pi * f * t)**2)
        return w
    
    wavelet = ricker_wavelet(20, 0.1, time_axis[1] - time_axis[0])
    seismogram = np.convolve(seismogram, wavelet, mode='same')
    
    # Plot the seismogram
    plt.figure(figsize=(6, 4))
    plt.plot(seismogram, time_axis, 'k')
    plt.gca().invert_yaxis()
    plt.xlabel('Amplitude')
    plt.ylabel('Time (s)')
    plt.title('3 Layer Synthetic 1D Seismogram')
    plt.grid()
    plt.show()
    
# Example usage
thickness = [3, 60, 100]  # in metres
density = [1800, 2100, 2300]  # kg/m^3
velocity = [800, 1860, 4500]  # m/s
timeSamples = 500
travelTime(thickness, density, velocity, timeSamples)