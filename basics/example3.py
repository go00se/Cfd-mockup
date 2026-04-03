"""
Interactive Flow Simulator Demo
Drag obstacles and watch flow update in real-time!

MOCKUP
"""

import sys
sys.path.append('../src')
from simulate import FlowSimulator

# Create and run simulator
sim = FlowSimulator(x_range=(-5, 5), y_range=(-5, 5), grid_points=40)
print(f"Number of particles: {len(sim.particles)}")
print(f"First particle: {sim.particles[0]}")                                # This is basically creating test env then I call on FlowSimulator class to actually do this
print(f"U_current exists: {hasattr(sim, 'U_current')}")

# Run
sim.run()

'''
Number of particles: 50
First particle: {'x': -4.5, 'y': ..., 'age': ..., 'trail': []}
U_current exists: True
sim.run()
'''
# Should be the correct values?