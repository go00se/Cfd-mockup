"""
Test: Flow around cylinder using potential flow

MOCKUP
"""

import numpy as np
import sys
sys.path.append('../src')
from visualization import plot_streamlines, plot_streamlines_obstacles
from interactive1 import flow_around_cylinder

# Create grid
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Calculate flow around cylinder at origin
cylinder_x = 0.0
cylinder_y = 0.0
cylinder_radius = 0.5
freestream_velocity = 10.0

U, V, mask = flow_around_cylinder(X, Y, cylinder_x, cylinder_y, 
                                   cylinder_radius, freestream_velocity)

# Mask velocities inside cylinder (set to NaN so streamplot ignores them)
U[mask] = np.nan
V[mask] = np.nan

obstacles = [{'type': 'circle', 'x': cylinder_x, 'y': cylinder_y, 'radius': cylinder_radius}]

# WHEN RUN, A STREAMLINE AROUND A INVISIBLE CIRCLE AROUND CENTER SHOULD APPEAR


plot_streamlines_obstacles(X, Y, U, V, obstacles=obstacles, title="Flow Around Cylinder - Visible Cyllinder")
