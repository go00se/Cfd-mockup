"""

Potential Flow Interactive Example
- Alright the background for this project is that I want to make the first step toward interactive fluid flow using doublets

    Heres what the sim acc does:
    - The user can click and drag on the canvas to create a flow field
    - The flow field is represented as a grid of vectors that are updated based on the user's input
    - The flow field is visualized using arrows that show the direction and magnitude of the flow at each point
    - The user can also adjust the parameters of the flow field, such as the strength and the size of the arrows

MOCKUP 
"""

# Math/Equations Library
#----------------------------------------------------------------------------------------------------------------------
import numpy as np
from matplotlib.widgets import Slider

def uniform_flow(X,Y,U_inf, alpha= 0):
    """
        We are using X Y U and angle alpha as the variable to ccreate uniform flow

        Parameters
        ----------
        X, Y : 2D array
        U_inf : float
            The uniform flow velocity
        alpha : float
            The angle of the uniform flow in radians, default is 0 (horizontal flow)

    """
    U= U_inf * np.cos(alpha) * np.ones_like(X)
    V= U_inf * np.sin(alpha) * np.ones_like(Y)
    return U, V

def doublet(X, Y, x_doublet=0, y_doublet=0, strength=1.0):
    """
    Circular Flow

    We are creating doublets to model the flow around circular objects

    Parameters:
    -----------
    X, Y : 2D arrays
        Grid coordinates
    x_doublet, y_doublet : float
        Position of doublet (obstacle center)
    strength : float
        Doublet strength (controls obstacle size)
    
    Returns: 
    -----------
    U, V : 2D arrays
        Velocity components of the doublet flow
    """


    X_rel = X- x_doublet
    Y_rel = Y- y_doublet
    r_squared = X_rel**2 + Y_rel**2 + 1e-10

    U = -strength * (X_rel**2 - Y_rel**2) / r_squared**2
    V = -strength * (2 * X_rel * Y_rel) / r_squared**2
    return U, V

# creates waterflow around a cricle, and strenght controls how big the circle is.
# How does it work? Doublets are a mathematical trick which places two fluids fluid appearing and fluid disappearing at the same point, creating a flow pattern that mimics flow around a solid object. By adjusting the strength of the doublet, we can control the size of the obstacle it represents.

def flow_around_cylinder(X, Y, x_cyl=0, y_cyl=0, radius=1.0, U_inf=10.0):
    """

    Basically just combines uniform flow and doublet to create cylindrical flow

    """

    U_uniform, V_uniform = uniform_flow(X, Y, U_inf)
    doublet_strength = U_inf * radius**2
    U_doublet, V_doublet = doublet(X,Y, x_cyl, y_cyl, doublet_strength)
    
    # Super position, total velocity = sum of all velocities
    U_total = U_uniform + U_doublet
    V_total = V_uniform + V_doublet
    
    X_rel = X - x_cyl
    Y_rel = Y - y_cyl
    cylinder_mask = (X_rel**2 + Y_rel**2) <= radius**2

    return U_total, V_total, cylinder_mask
    
   