"""
Biggest number after swaps
Given 2 numbers, s and k, find out
the biggest number you can get while switching the digits
in s k times 
"""

def find_max(string, k, maxm, x):
    #return if there are no swaps
    if k==0:
        return
    
    n=len(string)
    #Setting the current pos
    mx=string[x]
    for i in range(x+1, n):
        #Finding the max digit in the string and set it
        if int(string[i])>int(mx):
            mx=string[i]
    
    #if max not equal to string[x]
    if (mx!=string[x]):
        k-=1

    for i in range(x, n):
        #Finding the max value in the string and swapping it
        if (string[i]==mx):
            string[x], string[i] = string[i], string[x]
            new_string=''.join(string)
            #If the new number is greater than the old one, it will be selected
            if int(new_string) > int(maxm[0]):
                maxm[0] = new_string
            find_max(string, k, maxm, x+1)
            #Backtracking
            string[x], string[i] = string[i], string[x]


if __name__=="__main__":
    string = '129814999'
    k=4
    maxm=[string]
    string=[i for i in string]
    find_max(string, k, maxm, 0)
    print(maxm[0])