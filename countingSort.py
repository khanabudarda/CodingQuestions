# Counting sort is a sorting technique based on keys between a specific range.
# It works by counting the number of objects having distinct key values (kind of hashing).
# Then doing some arithmetic to calculate the position of each object in the output sequence.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Creating the function
def countingSort(array):
    countArr = [0] * (max(array)+1)
    countSumArr = countArr
    resArr = [0] * len(array)
    for i in array:
        countArr[i] = array.count(i)
    for i in range(1, len(countSumArr)):
        countSumArr[i] = countArr[i-1] + countArr[i]
    for i in array:
        countSumArr[i] = countSumArr[i] - 1
        resArr[countSumArr[i]] = i
    # Final Result
    print(resArr)


#array = [4, 3, 1, 6, 7, 1, 9]
array = []

# Taking inputs
numE = int(input("Enter the number of Elements: "))
for i in range(numE):
    inpN = int(input("Enter Element :"))
    array.append(inpN)

# Function Call
countingSort(array)
