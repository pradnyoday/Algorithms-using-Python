#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/rest-in-peace-21-1/
def rest_in_peace_21(num):
    if('21' in str(num)):return('The streak is broken!')
    elif(num % 21 != 0):return('The streak lives still in our heart!')
    else:return('The streak is broken!')
testcases = [120, 121, 231]
for num in testcases:
    print(rest_in_peace_21(num))