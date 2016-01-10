#create a calculator
#1. ask for operator
#2. ask for values
#3. print answer

a= float(input('enter the first value: '))
b= float(input('enter the second value: '))
opr= raw_input('enter the operation to be performed: \n 1.  Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n')
ans=0

#print ("values scaned")
#print a
#print b

if opr=="1":
	ans= a+b
	print ans
elif opr=="2":
	ans= a-b 
	print ans
elif opr=="3":
	ans= a*b
	print ans
elif opr=="4":
	ans=a/b
	print ans
else:
	print("invalid entry")

