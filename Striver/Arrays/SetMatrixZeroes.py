from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = 1
    for i in range(rows):
        # checking if 0 is present in the 0th column or not
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # traversing in the reverse direction and
    # checking if the row or col has 0 or not
    # and setting values of matrix accordingly.
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0 == 0:
            matrix[i][0] = 0




if __name__ == "__main__":
    arr = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(arr)
    print("The Final Matrix is ")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()