import argparse
import numpy as np

def dfs(i, j):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1:
        matrix[i][j] = 0  # Mark the current cell as visited
        dfs(i + 1, j)  # Explore down
        dfs(i - 1, j)  # Explore up
        dfs(i, j + 1)  # Explore right
        dfs(i, j - 1)  # Explore left

def numIslands(matrix):
    num_islands = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                num_islands += 1
                dfs(i, j)
    return num_islands

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Islands task.")
    parser.add_argument("--matrix_values", default='1,1,1', type=str, required=True, help="Input the matrix values")
    parser.add_argument("--rows", default=1, type=int, required=True, help="Input the matrix rows")
    parser.add_argument("--columns", default=1, type=int, required=True, help="Input the matrix columns")
    # parse args
    args = parser.parse_args()
    values = [int(el) for el in args.matrix_values.split(",")]
    matrix = np.array(values).reshape(args.rows, args.columns)
    print(numIslands(matrix))

