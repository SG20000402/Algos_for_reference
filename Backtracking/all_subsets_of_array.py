"""
All subsets of an array
Given an array, print all the possible subsets of the array
Eg.
    Input -> [1, 2, 3]
    Output -> [1]
              [1, 2]
              [1, 2, 3]
              [1, 3]
              [2]
              [2, 3]
              [3]
    
    Input -> [2, 4]
    Output -> [2]
              [2, 4]
              [4]
"""

def create_subsets(s, result, subset, index):
    #Adding the subset to the result list
    result.append(subset[:])

    for i in range(index, len(s)):
        #Starting a process of creating a combination
        subset.append(s[i])
        # Creating the different combinations with the previously set value
        create_subsets(s, result, subset, i+1)
        subset.pop()

def subsets(s):
    subset = []
    result = []
    index = 0
    create_subsets(s, result, subset, index)
    return result

if __name__=="__main__":
    array = [1, 2, 3, 4]
    result = subsets(array)

    for subset in result:
        print(*subset)