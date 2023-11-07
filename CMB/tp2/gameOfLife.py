import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def read_grid_from_file(filename):
    """Reads the grid from a file.

    Args:
        filename: The name of the file to read the grid from.

    Returns:
        A numpy array representing the grid.
    """

    with open(filename, "r") as f:
        data = f.read()

    # Split the data into lines and remove the last line (which is empty).
    data = data.split("\n")[:-1]

    # Convert the data to a numpy array.
    grid = np.array([[int(c) for c in line] for line in data])

    return grid

def update_grid(frameNum, grid, img, ax):

    """Evolves the grid for one time step and updates the plot.

    Args:
        frameNum: The frame number (used by FuncAnimation).
        grid: A numpy array representing the grid.
        img: The image plot object.
        ax: The axes object.

    Returns:
        A numpy array representing the evolved grid.
    """

    # Create a new grid to store the evolved .grid
    new_grid = np.zeros_like(grid)

    # Iterate over each cell in the grid.
    
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            
            # Count the number of alive neighbors of the cell.
            neighbors = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:  # Skip the current cell itself
                        continue
                    if (
                        0 <= i + di < grid.shape[0]
                        and 0 <= j + dj < grid.shape[1]
                        and grid[i + di][j + dj] == 1
                    ):
                        neighbors += 1


           # Apply the rules of Conway's Game of Life to determine the next state of the cell.
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:  # Apply underpopulation and overpopulation rules
                    new_grid[i][j] = 0
                else:  # Alive cells stay alive if they have 2 or 3 neighbors
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:  # Apply reproduction rule
                    new_grid[i][j] = 1
                    

    # Update the image data with the new grid.
    img.set_data(new_grid)
    ax.set_title(f'Conway\'s Game of Life - Frame {frameNum}')
    # Update the grid for the next iteration.
    grid[:] = new_grid[:]
    
    if frameNum == 50:
        time.sleep(3)
        plt.close()
        return

    return img


def generate_random_grid(rows, cols, density=0.5):
    """Generate a random grid with a given density of alive cells."""
    random_grid = np.random.randint(2, size=(rows, cols))
    return random_grid

def main():
    rows, cols = 30, 40  # Define o tamanho do grid
    density = 0.5  # Define a densidade de células vivas (50% nesse caso)
    
    # Gere o grid inicial aleatório.
    grid = generate_random_grid(rows, cols, density)
    
    # Create a figure and an axes object.
    fig, ax = plt.subplots()

    # Plot the initial state of the grid.
    img = ax.imshow(grid, cmap="gray")

    # Create the animation.
    ani = animation.FuncAnimation(
        fig, update_grid, fargs=(grid, img, ax), frames=51, interval=100
    )
    ani.save("C:/Users/Arthur Duarte/Desktop/AMU/Programming and Algorithms/CMB/tp2/animation.gif", writer="pillow")
    # Show the animation.
    
import subprocess


if __name__ == "__main__":
    main()
    subprocess.run(["C:/Users/Arthur Duarte/Desktop/AMU/Programming and Algorithms/CMB/tp2/animation.gif"], shell=True)

