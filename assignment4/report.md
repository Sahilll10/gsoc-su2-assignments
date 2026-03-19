# Assignment 4: Spatially Varying Wall Temperature

## Description

This assignment extends the CHT flat plate setup from Assignment 3 by applying a spatially varying wall temperature. Instead of time-varying but spatially uniform, the temperature now varies along the plate:
```
T_wall(x) = 300 + 50 * sin(2 * pi * x / 0.5)   [K]
```

This creates a periodic hot-cold pattern with wavelength 0.5 m and amplitude 50 K about a mean of 300 K.

## Implementation

The key change from Assignment 3 is inside the time loop. Instead of a single temperature for all vertices, the script iterates over all 200 vertices on the `plate` marker, reads each vertex x-coordinate via `MarkerCoordinates(MarkerID)(iVertex, 0)`, computes the local wall temperature, and calls `SetMarkerCustomTemperature` per vertex.

The non-uniform thermal boundary condition changes the local heat flux distribution along the plate, creating regions of higher and lower heat transfer that shift the boundary layer development compared to a uniform temperature case.

## Results

The simulation ran for 10 time steps successfully. All 10 iterations completed with the spatially varying BC applied at each step. The density residual reached below -5.9 per time step. The `launch_varying_temp.py` file contains the full implementation.
