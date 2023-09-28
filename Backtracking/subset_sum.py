"""
Subset problem
Given an set with positive integers, 
find the possible subsets whose sum is equal to target sum

Example 
set = {3, 34, 4, 12, 5, 2}
sum = 9
This is true because (4, 5) = 9
"""


def is_subset_sum(n, options, target):
    if target == 0:
        return True
    if n==0 and target!=0:
        return False
    #If the last element is greater than the sum, then it will be ignored
    if options[n-1]>target:
        return is_subset_sum(n-1, options, target)
    
    
    #checking if we can get subset by (1) Including the last element, (2)excluding the last element
    return is_subset_sum(n-1, options, target) or is_subset_sum(n-1, options, target-options[n-1])

if __name__=="__main__":
    #given_set = [3, 34, 4, 12, 5, 2] 
    #given_sum = 9  #True

    given_set = [3, 34, 4, 12, 5, 2]
    given_sum = 30  #False

    n = len(given_set)
    if is_subset_sum(n, given_set, given_sum):
        print("Found a subset")
    else:
        print("No such subset exists")
