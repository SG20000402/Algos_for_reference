"""
Parmutations of a String
Find all the possible different permutations of a given string
Eg. 
    Input -> 'ABC'
    Output -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

"""
# Returns the string
def print_op(st):
    return ''.join(st)

#Backtracking process
def permute(st, l, r):
    if l == r:
        print(print_op(st))
    else:
        #For each element in string, 2 values are interchanged, 
        # then the function is called so that different permutations 
        # within that change are created and printed
        for i in range(l, r):
            st[l], st[i] = st[i], st[l]
            permute(st, l+1, r)
            st[l], st[i] = st[i], st[l]

if __name__ == '__main__':
    string = 'ABCD'
    st = list(string)
    permute(st, 0, len(st))
    