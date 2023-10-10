import numpy as np
import time
import matplotlib.pyplot as plt


def bubble_sort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
        i += 1
    return array


def insertion_sort(array):
  i = 1
  while i<len(array):
    x = array[i]
    j = i
    while j > 0 and array[j-1] > x:
      array[j] = array[j-1]
      j -= 1
    array[j] = x
    i += 1
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

def heapify(array, end):
  start = (end-1)//2
  while start >= 0:
    array = siftDown(array, start, end)
    start -= 1
  return array

def heapsort(array):
  array = heapify(array, len(array)-1)
  end = len(array)-1
  while end > 0:
    array[end], array[0] = array[0], array[end]
    end -= 1
    array = siftDown(array, 0, end)
  return array

# Measure the execution time multiple times and average the results
def measure_execution_time(algorithm, array):
  execution_times = []
  for i in range(10):
    start_time = time.perf_counter()
    algorithm(array.copy())
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)
  return np.mean(execution_times)

# Create an array of input sizes
input_sizes = np.arange(1, 100)

# Create empty lists to store the execution times
insertion_sort_times = []
bubble_sort_times = []
heap_sort_times = []

# For each input size, measure the execution time of each algorithm and average the results
for input_size in input_sizes:
  array = np.random.randint(1000, size=input_size)

  insertion_sort_time = measure_execution_time(insertion_sort, array)
  insertion_sort_times.append(insertion_sort_time)

  bubble_sort_time = measure_execution_time(bubble_sort, array)
  bubble_sort_times.append(bubble_sort_time)

  heap_sort_time = measure_execution_time(heapsort, array)
  heap_sort_times.append(heap_sort_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort')
plt.plot(input_sizes, bubble_sort_times, label='Bubble Sort')
plt.plot(input_sizes, heap_sort_times, label='Heap Sort')

plt.xlabel('Input size')
plt.ylabel('Execution time (seconds)')
plt.legend()
plt.title('Execution time of sorting algorithms depending on input size')
plt.grid(True)
plt.show()




