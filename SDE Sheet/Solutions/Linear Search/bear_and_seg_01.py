#https://www.codechef.com/problems/SEGM01

def bear_and_seg_01(string):
    if('1' not in string):
        return 'NO'
    flag = 0
    seg = 0
    for i in string:
        if(i == '1'):
            if(not flag):
                seg += 1
                if(seg > 1):break
            flag = 1
        else:
            flag = 0
    if(seg > 1):return 'NO'
    else: return 'YES'

n = 6
tc = ["001111110","00110011","000","1111","101010101","101111111111"]
for i in tc:
    print(bear_and_seg_01(i))