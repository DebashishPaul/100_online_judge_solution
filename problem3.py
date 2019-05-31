import math

x=int(input())
for ini in range(x):
	p=int(input())
	if p%2==1:
		x=p%10  #31---->x=1
		y=p/10  #31--->3.1
		z=math.floor(y) #----->z=3

		for new in range(z):
			for new2 in range(x):
				print("*", end="")
				new2=new2+1
			print('\n')
		
	else:
		x=p%10
		y=p/10
		z=math.floor(y)

		for new3 in range(x):
			for new4 in range(new3):
				print(".", end="")
				new4=new4+1
x=x-1


