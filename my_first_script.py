import numpy as np

def nerdy_computation(x):
    """Returns the sum of the squares of the first x natural numbers using numpy."""
    D = 0
    for i in range(x+1):
        D+= i**2
    return D

print("Hello MUDE! Let's compute something nerdy:")
result = nerdy_computation(10)
print(f"The sum of the squares of the first 10 natural numbers is {result}")
