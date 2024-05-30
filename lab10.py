import numpy as np

def activation_function(x):
    return np.where(x >= 0, 1, 0)

def perceptron(inputs, weights, bias):
    weighted_sum = np.dot(inputs, weights) + bias
    return activation_function(weighted_sum)

training_data = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
])

weights = np.array([0.1, 0.1])
bias = 0.2
learning_rate = 0.1

for epoch in range(100):
    for data in training_data:
        inputs = data[:2]
        target_output = data[2]
        
        output = perceptron(inputs, weights, bias)
        
        error = target_output - output
        weights += learning_rate * error * inputs
        bias += learning_rate * error

test_data = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

for data in test_data:
    inputs = data
    output = perceptron(inputs, weights, bias)
    print(f"Input values: {inputs}, Predicted output: {output}")
