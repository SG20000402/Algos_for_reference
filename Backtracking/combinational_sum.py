""" 
Combinational Sum
Given a positive integer array and a target, create unique arrays whose sum equals the target. 
A number from the array can be selected repeatedly
Eg.
    array -> [2, 4, 6, 8]
    target -> 8
    output ->
        [2,2,2,2]
        [2,2,4]
        [2,6]
        [4,4]
        [8]
"""

def com_sum(array, target):
    answer = []
    subset = []
    sum_bkt(array, target, answer, subset, 0)
    return answer

def sum_bkt(array, target, answer, subset, index):
    if target == 0:
        answer.append(list(subset))
        return
    else:
        for i in range(index, len(array)):
            if (target - array[i])>=0:
                subset.append(array[i])
                sum_bkt(array, target-array[i], answer, subset, i)
                subset.remove(array[i])




if __name__=='__main__':
    ar = [2, 4, 6, 8]
    target = 8

    answer = com_sum(ar, target)
    
    for i in answer:
        print(i)