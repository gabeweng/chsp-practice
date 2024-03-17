from itertools import permutations


# OUR rules for finding a string is that you turn each digit n to arr[n] (this takes less time)
# THEIR rules for finding a string is that you turn each digit n to the value i where arr[i] = n (aka searching for n in arr and returning the index)
# We convert our string at the end to fulfill their requirements

def convert(num): #swaps index and value of a list; turns our format to their format
    new = [""]*10
    for i in range(10):
        new[int(num[i])]=str(i)
    return new

def swapdigits(num, key): #swaps the digits of a number according to the key (not same format as final answer)
    new=""
    for i in range(len(num)): #0-9 
        new=new+key[int(num[i])]
        
    return new

def test(a,b,c, key): #tests if the equation converted by key is true ACCORDING TO OUR RULES; a,b,c are strings, key is a list
    if int(swapdigits(a,key)) + int(swapdigits(b,key)) == int(swapdigits(c,key)):
        return True
    else:
        return False
    
s = input() #A+B=C
d,c = s.split("=") 
a,b = d.split("+") #strings of a, b
zerotonine = [str(i) for i in range(10)] # ["0", "1", ... "8", "9"]
permlist = list(permutations(zerotonine)) #list of all permutations of 0-9 ["1","2","3"], ["3","2","1"], ["1","3","2"], ["2","1","3"], ["2","3","1"], ["3","1","2]

solution=""
for perm in permlist:
    if test(a,b,c,perm): #if the random string converts the equation ACCORDING TO OUR RULES
        solution=convert(perm) #change the string so it word BY THEIR RULES
        break
print("".join(solution))
        
