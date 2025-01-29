import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Generate x values
x_values = np.linspace(-10, 10, 400)
y_sigmoid = sigmoid(x_values)
y_derivative = sigmoid_derivative(x_values)

# Plot the functions
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_sigmoid, label=r"$f(x) = \frac{1}{1 + e^{-x}}$", linewidth=2)
plt.plot(x_values, y_derivative, label=r"$f'(x) = f(x)(1 - f(x))$", linewidth=2, linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Sigmoid Function and Its Derivative")
plt.grid(True)

# Show the plot
plt.show()
