'''
Given two natural numbers (both not greater than 200), each number in the separate line, please print the sum of them.

Example
Input:
2
3

Output:
5
'''

val = int(input("Enter your first value: "))
val2=int(input("enter your second value: "))
x=200
if val<x and val2<x:
	sum=val+val2
	print(sum)
else:
    print("enter the value less than 200")
