import matplotlib.pyplot as plt
import seaborn as sns
import torch
import numpy as np

def plot_dist(data, dist_plot=1, num_cols=None, figsize=(10, 6), save_path=None):
    """
    Plots the distribution of tensor data from a neural network's forward pass.

    Parameters:
    - data (torch.Tensor or numpy.ndarray): The tensor data to plot.
    - dist_plot (int): 
        - If 0, plots the distribution for each column in the tensor individually.
        - If 1 (default), plots the distribution of the entire flattened tensor.
    - num_cols (int, optional): Number of columns to plot if dist_plot=0. If None, plots all columns.
    - figsize (tuple, optinal): Figure size for the plot(s).
    - save_path (str, optional): Path to save the plot. If None, just displays the plot

    Returns:
    None
    """
    # Convert to numpy array if it's a torch tensor
    if isinstance(data, torch.Tensor):
        data_np = data.detach().cpu().numpy()
    elif isinstance(data, np.ndarray):
        data_np = data
    else:
        raise ValueError("Input data must be either a torch.Tensor or a numpy.ndarray")

    if dist_plot == 0:
        total_cols = data_np.shape[1]
        num_cols = num_cols or total_cols
        num_cols = min(num_cols, total_cols)  # make sure that  we dont exceed the actual number of columns

        for i in range(num_cols):
            plt.figure(figsize=figsize)
            sns.histplot(data_np[:, i], kde=True, stat='density')
            plt.xlabel('Value')
            plt.ylabel('Density')
            plt.title(f'Distribution of Column {i+1}')
            if save_path:
                plt.savefig(f'{save_path}_column_{i+1}.png')
                plt.close()
            else:
                plt.show()
    else:
        plt.figure(figsize=figsize)
        sns.histplot(data_np.flatten(), kde=True, stat='density', bins=30)
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.title('Distribution of the Entire Tensor')
        if save_path:
            plt.savefig(f'{save_path}_entire_tensor.png')
            plt.close()
        else:
            plt.show()

# Example:
# model = YourNeuralNetwork()
# input_data = torch.randn(100, 10)
# output, intermediate_results = model(input_data)
# plot_dist(intermediate_results[2], dist_plot=0, num_cols=5, save_path='layer_3_dist')