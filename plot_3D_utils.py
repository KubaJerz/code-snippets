import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from plotly.offline import plot
import plotly.graph_objects as go

def plot_3d_surface_matplotlib(func, x_range=(-5, 5), y_range=(-5, 5), resolution=100, 
                               cmap='BuPu_r', alpha=0.8, trajectory=None):
    """
    Create a 3D surface plot using matplotlib.
    
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
    x = np.linspace(*x_range, resolution)
    y = np.linspace(*y_range, resolution)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surface = ax.plot_surface(X, Y, Z, cmap=cmap, alpha=alpha)

    if trajectory:
        traj_x = np.linspace(trajectory[0][0], trajectory[0][1], 15)
        traj_y = np.linspace(trajectory[1][0], trajectory[1][1], 15)
        traj_z = func(np.array(traj_x), np.array(traj_y))
        ax.plot(traj_x, traj_y, traj_z, 'r--', linewidth=2, label='Trajectory')
        ax.legend()

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'3D Plot of z = f(x, y)')

    fig.colorbar(surface, shrink=0.5, aspect=5)

    return fig, ax

def plot_3d_surface_plotly(func, x_range=(-5, 5), y_range=(-5, 5), resolution=100, 
                           colorscale=[[0, 'purple'], [1, 'blue']], opacity=0.99, 
                           trajectories=None, show_axis=False, show_in_browser=False):
    """
    Create a 3D surface plot using plotly.
    
    Parameters:
    - func: Function to plot, should take two arguments (x, y)
    - x_range, y_range: Tuples defining the range for x and y axes
    - resolution: Number of points along each axis
    - colorscale: Colorscale for the surface
    - opacity: Opacity of the surface
    - trajectories: Optional list of dictionaries, each containing 'points' (list of (x0, x1) and (y0, y0) start and end points to plot as a line) 
                    and 'properties' (dict with line properties)
                    and 'traj_resolution' the Number of points along trajectorie
    - show_axis: Toggle to turn on and off grid lines and more
    - show_in_browser: Optional to render in browesr
    
    Returns:
    - fig: The plotly figure object
    """
    x = np.linspace(*x_range, resolution)
    y = np.linspace(*y_range, resolution)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    surface = go.Surface(x=X, y=Y, z=Z, colorscale=colorscale, showscale=False, opacity=opacity)

    data = [surface]

    if trajectories:
        for traj in trajectories:
            traj_x = np.linspace(traj['points'][0][0], traj['points'][0][1], traj['traj_resolution'])
            traj_y = np.linspace(traj['points'][1][0], traj['points'][1][1], traj['traj_resolution'])
            traj_z = func(np.array(traj_x), np.array(traj_y))
            line = go.Scatter3d(x=traj_x, y=traj_y, z=traj_z, mode='lines', **traj['properties'])
            data.append(line)

    if not show_axis:
        layout = go.Layout(
            scene=dict(
                xaxis=dict(showticklabels=False, showgrid=False, zeroline=False, showline=False),
                yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, showline=False),
                zaxis=dict(showticklabels=False, showgrid=False, zeroline=False, showline=False)
            ),
            showlegend=False,
            margin=dict(l=0, r=0, b=0, t=0)
        )
    else:
        layout = go.Layout(
            showlegend=False,
            margin=dict(l=0, r=0, b=0, t=0)
        )

    fig = go.Figure(data=data, layout=layout)
    if show_in_browser:
        plot(fig, filename='3d_plot.html', auto_open=True)
        print('plotted in browser so returned NONE')
        return None
    else:
        return fig