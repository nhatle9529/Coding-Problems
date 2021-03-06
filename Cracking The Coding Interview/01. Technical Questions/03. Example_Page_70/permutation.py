'''
Example: Given a smaller string 5 and a bigger string b, design an algorithm to find all permutations
of the shorter string within the longer one. Print the location of each permutation.

e.g.
s: abbc
b: cbabadcbbabbcbabaabccbabc

Answer:
cbab
cbba
abbc
bcba
cbab
cbab
babc
'''

def find_permutation(s, b):
    '''
    Function find all required position.

    Arguments:
    s -- str
    b -- str 
    '''
    hash_table = [0] * 256

    for word in s:
        hash_table[ord(word)] += 1
    
    start, j, count, length = 0, 0, 0, len(s)
    temp_table = hash_table.copy()
    
    while j != len(b):
        if temp_table[ord(b[j])] > 0:
            temp_table[ord(b[j])] = temp_table[ord(b[j])] - 1
            count += 1
        
        if count == length:
            print(b[start: j+1])
            start, j, count, temp_table = start + 1, start + 1, 0, hash_table.copy()
        
        elif j - start + 1 == length:
            j, start, temp_table, count = start + 1, start + 1, hash_table.copy(), 0
        
        else:
            j += 1

s = 'abbc'
b = 'cbabadcbbabbcbabaabccbabc'

find_permutation(s, b)
