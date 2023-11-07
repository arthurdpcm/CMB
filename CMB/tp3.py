import random
import sys
import matplotlib.pyplot as plt

def generate_random_sequence(n):
  return [random.random() for _ in range(n)]

def plot_sequence(n):
  xn = generate_random_sequence(n)
  fig, axs = plt.subplots(1, 3, figsize=(15, 5))
  axs[0].plot(range(n), xn, 'o')
  axs[0].set_xlabel('n')
  axs[0].set_ylabel('xn')
  axs[1].plot(xn[:-1], xn[1:], 'o')
  axs[1].set_xlabel('xn-1')
  axs[1].set_ylabel('xn')
  axs[2].hist(xn, bins=20)
  axs[2].set_xlabel('xn')
  axs[2].set_ylabel('Frequency')
  plt.show()
  return xn
def main():
  n = int(sys.argv[1])
  xn = plot_sequence(n)

  mean = sum(xn) / len(xn)
  median = sorted(xn)[len(xn) // 2]
  mode = max(xn, key=xn.count)

  print("Mean:", mean)
  print("Median:", median)
  print("Mode:", mode)

if __name__ == '__main__':
  main()

#The code generates a sequence of random numbers and plots them in three different ways.
# Each time the code is run,
# a different sequence of random numbers is generated and plotted.
# Therefore, the output will be different each time the code is run.
