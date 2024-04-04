#this is on bugfix file with some changes done in this file.
#fixed the bug that existed in a previous feature barnch and now able to merge
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

for value in random_values:
    print(f"Sigmoid output for {value}: {sigmoid(value)}")
