#https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/maximum-occurrence-9/

def max_occurance(string):
    hash = dict()
    occurance = 0
    char = ''
    for i in string:
        if(i in hash): hash[i] += 1
        else: hash[i] = 1
        if(hash[i] == occurance):
            char = chr(min(ord(i), ord(char)))
        if(hash[i] > occurance):
            occurance = hash[i]
            char = i
    return (char, occurance)
string = "aaaaAAAA"
print(max_occurance(string))