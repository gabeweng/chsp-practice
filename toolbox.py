#inputs

arr = input().split() #array of strings
arr = list(map(int, input().split())) #array of integers


#itertools
from itertools import permutations

'''


product('ABCD', repeat=2) #exactly like nested for loop

AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

permutations('ABCD', 2) #like above but no repeating elemetnts

AB AC AD BA BC BD CA CB CD DA DB DC

combinations('ABCD', 2) #subarrays (essentailly there will be AB but no BA)

AB AC AD BC BD CD

combinations_with_replacement('ABCD', 2) #subarrays but repeat for some reason?

AA AB AC AD BB BC BD CC CD DD'''