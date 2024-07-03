# CodeSnippets
Documentation of many different snippets of code that I use

---
## Neural Network Intermediate Layer Distribution Visualization

This script provides a function `plot_dist` to visualize the distribution of tensor data from a neural network's forward pass. It's particularly useful for analyzing the behavior of intermediate layers in a neural network.

### Function: `plot_dist`

#### Purpose
The `plot_dist` function allows you to plot the distribution of tensor data, either for individual columns or for the entire flattened tensor. This can help in understanding the activation patterns and potential issues like vanishing or exploding gradients in different layers of a neural network.

#### Parameters
- `data` (torch.Tensor or numpy.ndarray): The tensor data to plot, typically from an intermediate layer of a neural network.
- `dist_plot` (int): 
  - If 0, plots the distribution for each column in the tensor individually.
  - If 1 (default), plots the distribution of the entire flattened tensor.
- `num_cols` (int, optional): Number of columns to plot if `dist_plot=0`. If None, plots all columns.
- `figsize` (tuple, optinal): Figure size for the plot.
- `save_path` (str, optional): Path to save the plot. If None, displays the plot instead.

#### Usage Example
```python
model = YourNeuralNetwork()
input_data = torch.randn(100, 10)
output, intermediate_results = model(input_data)

# Plot distribution of the third layer's output, showing first 5 columns
plot_dist(intermediate_results[2], dist_plot=0, num_cols=5, save_path='layer_3_dist')

# Plot overall distribution of the output layer
plot_dist(output, dist_plot=1, save_path='output_dist')
```

---
## 3D Surface Plotting Utilities


This module provides functions to create 3D surface plots using both Matplotlib and Plotly.

### Dependencies

- numpy
- matplotlib
- mpl_toolkits.mplot3d
- plotly

#### Functions

#### plot_3d_surface_matplotlib

Creates a 3D surface plot using Matplotlib.

```python
def plot_3d_surface_matplotlib(func, x_range=(-5, 5), y_range=(-5, 5), resolution=100, 
                               cmap='BuPu_r', alpha=0.8, trajectory=None):
    """
    Parameters:
    - func: Function to plot, should take two arguments (x, y)
    - x_range, y_range: Tuples defining the range for x and y axes
    - resolution: Number of points along each axis
    - cmap: Colormap for the surface
    - alpha: Transparency of the surface
    - trajectory: Optional list of (x0, x1) and (y0, y0) points to plot as a line
    
    Returns:
    - fig, ax: The figure and axis objects
    """
```

    sdasfasdfsd


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