import time
import numpy as np

size = 1_000_000

python_list = list(range(size))
numpy_array = np.arange(size)

# Python List
start = time.time()
python_result = [x * 2 for x in python_list]
python_time = time.time() - start

# NumPy Array
start = time.time()
numpy_result = numpy_array * 2
numpy_time = time.time() - start

print("Execution Time (Python List):", python_time, "seconds")
print("Execution Time (NumPy Array):", numpy_time, "seconds")
print("Speed Difference:", python_time - numpy_time, "seconds")
