"""
Powet Set Lexicographic Order
Given a string, print all substrings in
lexicographical order
"""

def permute_set(string, n, ind=-1, cur=''):
    if ind == n:
        return
    
    if len(cur)>0:
        print(cur)

    for i in range(ind+1, n):
        cur += string[i]
        permute_set(string, n, i, cur)
        cur=cur[:len(cur)-1]

def power_set(string):
    #Sorting a string before working on it
    string = ''.join(sorted(string))
    permute_set(string, len(string))

if __name__=="__main__":
    string = 'cab'
    power_set(string)