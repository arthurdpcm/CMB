import numpy as np
import time
import matplotlib.pyplot as plt

def sequential_search(arr, target):
  for j in arr:
    if j == target:
      return j
  return -1

def binary_search(arr, target):
  low = 0
  high = len(arr)-1 
  while low <= high:
    mid = (low+high)//2
    if target == arr[mid]:
      return mid
    elif target < arr[mid]:
      high = mid-1
    else:
      low = mid+1
      
# Measure the execution time multiple times and average the results
def measure_execution_time(algorithm, array, target):
  execution_times = []
  for i in range(10):
    start_time = time.perf_counter()
    algorithm(array.copy(), target)
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)
  return np.mean(execution_times)

# Create an array of input sizes
input_sizes = np.arange(1, 100)

# Create empty lists to store the execution times
sequential_search_times = []
binary_search_times = []

# For each input size, measure the execution time of each algorithm and average the results
for input_size in input_sizes:
  array = np.random.randint(1000, size=input_size)

  sequential_search_time = measure_execution_time(sequential_search, array, array[-1])
  sequential_search_times.append(sequential_search_time)

  binary_search_time = measure_execution_time(binary_search, array, array[-1])
  binary_search_times.append(binary_search_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, sequential_search_times, label='Sequential Search')
plt.plot(input_sizes, binary_search_times, label='Binary Search')

plt.xlabel('Input size')
plt.ylabel('Execution time (seconds)')
plt.legend()
plt.title('Execution time of search algorithms depending on input size')
plt.grid(True)
plt.show()