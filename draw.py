from matplotlib.patches import Polygon, Rectangle
from matplotlib import pyplot as plt
import numpy as np

def sphere_to_cartesian(radial, pole, azimuth, degrees=True):
    """Convert spherical coordinates to Cartesian.

    Coordinate inputs can be scalar floats or numpy arrays.

    Parameters:
    radial: Radial distance.
    pole: Polar angle measured from +z axis.
    azimuth: Azimuthal angle measured from +x axis toward +y axis.
    degrees (bool): Set to False for radians.

    Returns:
    Cartesian coordinates in the form [x, y, z]
    """
    if degrees:
        # Convert degrees to radians
        pole = pole * np.pi / 180
        azimuth = azimuth * np.pi / 180

    x = radial * np.cos(azimuth) * np.sin(pole)
    y = radial * np.sin(azimuth) * np.sin(pole)
    z = radial * np.cos(pole)

    return [x, y, z]

def draw_phase(phase, n_points=150, bg_margin=0.2):
    """Draw a simple picture of the Moon at a given phase.

    The illuminated portion is modeled as a matplotlib polygon patch.
    The visible edge of the illuminated portion is a semicircle.
    The terminator is a great circle on the Moon of radial distance = 1.

    Parameters:
    phase (float): 0 deg is a new moon and 270 deg is third quarter.
    n_points (int): The number of points on the terminator.
    bg_margin (float): The background margin as a fraction of moon radius.
    """
    radial = np.repeat(1.0, n_points * 2)
    # Note that the polar angle reverses direction for the terminator to avoid
    # a discontinuity in the polygon.
    pole = np.append(np.linspace(0.0, 180.0, n_points),
                     np.linspace(180.0, 0.0, n_points))

    azimuth = np.array([])
    if phase >= 0 and phase < 180:
        # az_angle = 0 is the right edge of the illuminated portion.
        for az_angle in [0, phase]:
            azimuth = np.append(azimuth, np.repeat(az_angle, n_points))
    elif phase >= 180 and phase <= 360:
        # The terminator starts from the right edge of the picture.
        phase -= 180
        # az_angle = 180 is the left edge of the illuminated portion.
        for az_angle in [180, phase]:
            azimuth = np.append(azimuth, np.repeat(az_angle, n_points))
    else:
        raise ValueError('phase must be between 0 and 360 degrees.')

    # Only the x and z coordinates are required for a 2D picture.
    xyz = sphere_to_cartesian(radial, pole, azimuth)
    terminator_x, terminator_z = xyz[0], xyz[2]

    fig, ax = plt.subplots()
    ax.set_aspect(1)

    # Create a black background so the axes can be turned off.
    margin = 1 + bg_margin
    background = Rectangle((-margin, -margin), 2*margin, 2*margin,
                           fc='black', ec='None')
    ax.add_patch(background)

    # This gives the coordinates the right shape for the Polygon object.
    stack = np.stack((terminator_x, terminator_z), axis=-1)
    illuminated = Polygon(stack, closed=False, fc='white', ec='None')
    ax.add_patch(illuminated)

    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)
    plt.axis('off')
    plt.tight_layout()
