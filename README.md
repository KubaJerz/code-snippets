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

---