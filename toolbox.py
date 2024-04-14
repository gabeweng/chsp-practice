#inputs

arr = input().split() #array of strings
arr = list(map(int, input().split())) #array of integers

"".join([1,2,3])

# initiating cool arrays
arr=[0]*10
arr=[0 for i in range(10)]
arr=[[[[0,0,0] for i in range(h)] for j in range(l)] for k in range(w)] # 4D array with arr[w][l][h] being the RBG value of the pixel at (w,l,h)
zerotonine = [str(i) for i in range(10)]

#itertools
from itertools import permutations

''' can be used with string, array, etc.
product('ABCD', repeat=2) #exactly like nested for loop
AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

permutations('ABCD', 2) #like above but no repeating elemetnts
AB AC AD BA BC BD CA CB CD DA DB DC

combinations('ABCD', 2) #subarrays (essentailly there will be AB but no BA)
AB AC AD BC BD CD

combinations_with_replacement('ABCD', 2) #subarrays but repeat for some reason?
AA AB AC AD BB BC BD CC CD DD'''