import time
import numpy as np

# Python list
start = time.time()
lst = [i for i in range(1000000)]
lst = [i*2 for i in lst]
print("List Time:", time.time() - start)

# NumPy array
start = time.time()
arr = np.arange(1000000)
arr = arr * 2
print("NumPy Time:", time.time() - start)