# CodeSnippets
Documentation of many Miscellaneous snippets of code that I use

#### plot_3d_surface_plotly

Creates an interactive 3D surface plot using Plotly.

```python
def plot_3d_surface_plotly(func, x_range=(-5, 5), y_range=(-5, 5), resolution=100, 
                           colorscale=[[0, 'purple'], [1, 'blue']], opacity=0.99, 
                           trajectories=None, show_axis=False, show_in_browser=False):
```

##### Parameters:

- `func` (callable): Function to plot. Should take two arguments (x, y) and return z values.
- `x_range` (tuple): Range for x-axis. Default is (-5, 5).
- `y_range` (tuple): Range for y-axis. Default is (-5, 5).
- `resolution` (int): Number of points along each axis. Default is 100.
- `colorscale` (list): Colorscale for the surface. Default is [[0, 'purple'], [1, 'blue']].
- `opacity` (float): Opacity of the surface. Default is 0.99.
- `trajectories` (list): Optional list of trajectories to plot. Each trajectory is a dictionary containing:
  - `'points'` (list): List of (x0, x1) and (y0, y1) start and end points to plot as a line.
  - `'properties'` (dict): Dictionary with line properties (color, width, dash, etc.).
  - `'traj_resolution'` (int): Number of points along the trajectory.
- `show_axis` (bool): Toggle to show or hide grid lines and axis labels. Default is False.
- `show_in_browser` (bool): Option to render the plot in a web browser. Default is False.

##### Returns:

- `fig` (plotly.graph_objs.Figure): The Plotly figure object, or None if `show_in_browser` is True.

### Usage Examples

### Example 1: Matplotlib Plot

```python
from plot_3D_utils import plot_3d_surface_matplotlib
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return (np.cos(x) - 0.1*y)**2 - 0.3*x + 2

fig, ax = plot_3d_surface_matplotlib(f1, trajectory=[(-3, -1), (0, 0)])
plt.show()
```

#### Example 2: Plotly Plot

```python
from plot_3D_utils import plot_3d_surface_plotly
import numpy as np
import plotly.io as pio

def f2(x, y):
    return 2 * np.cos(x + 2) + 1.5 * np.cos(0.65 * y) + 0.5 * x

trajectories = [
    {'points': [(2, 0.14), (-0.05, 0.353)], 
     'properties': {'line': dict(color='#cccccc', width=5, dash='dash')},
     'traj_resolution': 15},
    {'points': [(0.15, 0.353), (0.35, 0.35)], 
     'properties': {'line': dict(color='red', width=5, dash='solid')},
     'traj_resolution': 15}
]

fig = plot_3d_surface_plotly(f2, trajectories=trajectories, show_in_browser=True)
pio.show(fig)
```

#### Example 3: Detailed Plotly Example

```python
from plot_3D_utils import plot_3d_surface_plotly
import numpy as np
import plotly.io as pio

# Define the function to plot
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Define trajectories
trajectories = [
    {
        'points': [(-3, 3), (3, -3)],
        'properties': {'line': dict(color='red', width=4, dash='solid')},
        'traj_resolution': 50
    },
    {
        'points': [(-3, -3), (3, 3)],
        'properties': {'line': dict(color='green', width=4, dash='dash')},
        'traj_resolution': 50
    }
]

# Create the plot
fig = plot_3d_surface_plotly(
    f,
    x_range=(-5, 5),
    y_range=(-5, 5),
    resolution=150,
    colorscale=[[0, 'blue'], [0.5, 'white'], [1, 'red']],
    opacity=0.8,
    trajectories=trajectories,
    show_axis=True,
    show_in_browser=False
)

# Display the plot
pio.show(fig)
```

This example creates a 3D surface plot of the function f(x, y) = sin(sqrt(x^2 + y^2)) with two trajectories: a solid red line and a dashed green line. The surface uses a blue-white-red colorscale and is slightly transparent. Axis labels and grid lines are visible.

## Notes:

- If `show_in_browser` is set to True in `plot_3d_surface_plotly`, the function will open the plot in the default web browser and return None instead of the figure object.
- The `trajectories` parameter in `plot_3d_surface_plotly` allows for multiple paths to be drawn on the surface, each with customizable properties.
- Adjust the `resolution` parameter to balance between plot detail and performance. Higher values provide smoother surfaces but may slow down rendering.
```

---