"""
This script defines a function to plot the distribution of tensor data from a neural network's forward pass.
The `forward` method of the neural network returns intermediate results, and the `plot_dist` function
visualizes these results.

Example forward pass:

def forward(self, X):
    res = []
    x = self.l0(X)
    res.append(x)
    x = self.tanh0(x)
    res.append(x)
    x = self.l1(x)
    res.append(x)
    x = self.tanh1(x)
    res.append(x)
    logits = self.l2(x)
    res.append(logits)
    x = self.out(logits)
    res.append(x)
    return x, res

The `forward` method returns the final output `x` and a list `res` containing intermediate tensors from each layer.

Usage of plot_dist:

- To plot the distribution of a specific layer's output:
    plot_dist(res[layer_idx], dist_plot)

- Parameters:
    - data: A tensor from the list of intermediate results (`res`).
    - dist_plot: 
        - If 0, plots the distribution for each column in the tensor individually.
        - Otherwise, plots the distribution of the entire flattened tensor.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_dist(data, dist_plot):
    """
    Plots the distribution of tensor data.

    Parameters:
    - data (torch.Tensor): The tensor data to plot.
    - dist_plot (int): 
        - If 0, plots the distribution for each column in the tensor individually.
        - Otherwise, plots the distribution of the entire flattened tensor.

    Returns:
    None
    """
    data_np = data.detach().numpy()

    if dist_plot == 0:
        num_cols = data_np.shape[1]  # Number of columns in the tensor

        # Plot the distribution for each column individually
        for i in range(num_cols):
            sns.histplot(data_np[:, i], kde=True, stat='density')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.title(f'Distribution of Column {i+1}')
            plt.show()
    else:
        plt.hist(data_np.flatten(), bins=30)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Distribution of the Tensor')
        plt.show()
