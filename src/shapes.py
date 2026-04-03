"""
Simple shape and coordinate script to add different shapes to simulator
should use coordinates for this

MOCKUP
"""
import numpy as np

def generate_circle(radius=1.0, num_points=50):
    theta = np.linspace(0, 2*np.pi, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y

def generate_rectangle(width=2.0, height=1.0, num_points=50):
    n = num_points // 4

    bottom= np.column_stack([np.linspace(-width/2, width/2, n ), np.full(n, -height/2)])
    top = np.column_stack([np.linspace(-width/2, width/2, n ), np.full(n, height/2)])
    left = np.column_stack([np.full(n, -width/2), np.linspace(-height/2, height/2, n)])
    right = np.column_stack([np.full(n, width/2), np.linspace(-height/2, height/2, n)])

    coords = np.vstack([bottom, right, top, left])
    return coords[:, 0], coords[:, 1]

def generate_ellipse(width=2.0, height=1.0, num_points=50):
    theta = np.linspace(0, 2*np.pi, num_points)
    x = (width/2) * np.cos(theta)
    y = (height/2) * np.sin(theta)
    return x, y

def generate_naca_airfoil(naca='0012', chord=2.0, num_points=100):
    """
    Generate NACA 4-digi airfoil coordinates
    naca: is a 4 digit string
    """
    m = int(naca[0]) / 100.0 # mac chamber
    p = int(naca[1]) / 10.0 # position of max camber
    t = int(naca[2:4]) /100.0 # thickness

    beta= np.linspace(0, np.pi, num_points//2)
    x= chord * (1 - np.cos(beta)) / 2

    yt = 5 * t * chord * (
        0.2969 * np.sqrt(x/chord) - 
        0.1260 * (x/chord) - 
        0.3516 * (x/chord)**2 + 
        0.2843 * (x/chord)**3 - 
        0.1015 * (x/chord)**4
    )

    if m == 0:
        xu = x
        yu = yt
        xl = x
        yl = -yt
    else:
        yc= np.where(x <p*chord, m * (x/(p**2)) * (2*p - x/chord), m * ((chord-x)/((1-p)**2)) * (1 + x/chord - 2*p))

        xu = x
        yu = yc + yt
        xl = x
        yl = yc - yt

        # Combine upper and lower surfaces
        x_airfoil = np.concatenate([xu, xl[::-1]])
        y_airfoil = np.concatenate([yu, yl[::-1]])

        # Center airfoil at origin
        x_airfoil -= chord/2
    return x_airfoil, y_airfoil

