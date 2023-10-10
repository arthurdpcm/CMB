import numpy as np
import time
import matplotlib.pyplot as plt

def sort(array):
  array.sort()

def heapsort(array):
  heapify(array, len(array)-1)
  end = len(array)-1
  while end > 0:
    array[end], array[0] = array[0], array[end]
    end -= 1
    siftDown(array, 0, end)

def heapify(array, end):
  start = (end-1)//2
  while start >= 0:
    array = siftDown(array, start, end)
    start -= 1
  return array

def siftDown(array, start, end):
  root = start
  while 2*root+1 <= end:
    child = 2*root+1
    swap = root
    if array[swap] < array[child]:
      swap = child
    if child+1 <= end and array[swap] < array[child+1]:
      swap = child+1
    if swap == root:
      return array
    else:
      array[root], array[swap] = array[swap], array[root]
      root = swap
  return array

# Create an array of input sizes
input_sizes = np.arange(1, 100)

# Create empty lists to store the execution times
sort_times = []
heapsort_times = []

# For each input size, measure the execution time of each algorithm
for input_size in input_sizes:
  array = np.random.randint(1000, size=input_size)

  # Start the timer
  start_time = time.perf_counter()

  # Sort the array using the sort() method
  sort(array.copy())

  # Stop the timer
  end_time = time.perf_counter()

  # Calculate the execution time
  sort_time = end_time - start_time

  # Start the timer
  start_time = time.perf_counter()

  # Sort the array using the heapsort algorithm
  heapsort(array.copy())

  # Stop the timer
  end_time = time.perf_counter()

  # Calculate the execution time
  heapsort_time = end_time - start_time

  # Add the execution times to the lists
  sort_times.append(sort_time)
  heapsort_times.append(heapsort_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, sort_times, label='sort()')
plt.plot(input_sizes, heapsort_times, label='heapsort')

plt.xlabel('Input size')
plt.ylabel('Execution time (seconds)')
plt.legend()
plt.title('Execution time of the sort() method and the heapsort algorithm')
plt.grid(True)
plt.show()