import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

    # Create a new grid to store the evolved grid.
    new_grid = np.zeros_like(grid)

    # Iterate over each cell in the grid.
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):

            # Count the number of alive neighbors of the cell.
            neighbors = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if (
                        0 <= i + di < grid.shape[0]
                        and 0 <= j + dj < grid.shape[1]
                        and grid[i + di][j + dj] == 1
                    ):
                        neighbors += 1

            # Apply the rules of Conway's Game of Life to determine the next state of the cell.
            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = grid[i][j]

    # Update the image data with the new grid.
    img.set_data(new_grid)
    ax.set_title(f'Conway\'s Game of Life - Frame {frameNum}')
    # Update the grid for the next iteration.
    grid[:] = new_grid[:]
    return img

def main():
    # Read the grid from the file.
    grid = read_grid_from_file("matrix.txt")

    # Create a figure and an axes object.
    fig, ax = plt.subplots()

    # Plot the initial state of the grid.
    img = ax.imshow(grid, cmap="gray")

    # Create the animation.
    ani = animation.FuncAnimation(
        fig, update_grid, fargs=(grid, img, ax), frames=50, interval=1000
    )

    # Show the animation.
    plt.show()

if __name__ == "__main__":
    main()