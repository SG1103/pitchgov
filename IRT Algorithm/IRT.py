import numpy as np

def logistic(theta, b):
    """ Logistic Item Response Theory Model: Probability of a correct response """
    return 1 / (1 + np.exp(-1.7 * (theta - b)))

# Example usage
theta = 0.5  # ability of the test taker
b = np.linspace(1, 9, 9)  # difficulty levels from 1 to 9
probabilities = logistic(theta, b)

print("Probabilities of Correct Response:", probabilities)
