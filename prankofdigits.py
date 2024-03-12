from itertools import permutations

z=[2,3,7,1,9,0,4,8,5,6]
y=["5","3","0","1","6","8","9","2","7","4"]


def convert(num): #swaps index and value of a list
    new = [""]*10
    for i in range(10):
        new[int(num[i])]=str(i)
    return new

def swapdigits(num, key): #swaps the digits of a number according to the key (not same format as final answer)
    new=""
    for i in range(len(num)):


        new=new+key[int(num[i])]
    return new

def test(a,b,c, key): #tests if the converted equation is true
    if int(swapdigits(a,key)) + int(swapdigits(b,key)) == int(swapdigits(c,key)):
        return True
    else:
        return False
    
s = input()
d,c = s.split("=")
a,b = d.split("+")
zerotonine = [str(i) for i in range(10)]
permlist = list(permutations(zerotonine))
solution=""
for perm in permlist:
    if test(a,b,c,perm):        
        solution=convert(perm)
        break
print("".join(solution))
        
