import random
import sys
import matplotlib.pyplot as plt

def generate_random_sequence(n):
    return [random.random() for _ in range(n)]

def plot_sequence(n):
    xn = generate_random_sequence(n)
    sorted_xn = sorted(xn)  # Sort the sequence

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    axs[0].scatter(range(n), xn, s=10, color='red') 
    axs[0].plot(range(n), xn, '-', label='Random Sequence') 
    
    axs[0].set_xlabel('n')
    axs[0].set_ylabel('xn')

    
    axs[1].scatter(xn[:-1], xn[1:], color='orange')
    axs[1].set_xlabel('xn-1')
    axs[1].set_ylabel('xn')
    
    axs[2].hist(xn, bins=20, color='purple')
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
