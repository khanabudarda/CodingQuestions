# Counting the numbers of Squares on a chess board

# Creating the function
def countSquares(grid):
    sumSquares = 0
    sqs = grid
    for i in range(grid):
        sumSquares = sumSquares + (sqs * sqs)
        sqs = sqs - 1
    print(sumSquares)


# Calling the Fucntion
countSquares(8)
