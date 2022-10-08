#1
"""n = int(input("enter the number\n"))
i=0
s=0
while i<=n:
    s+=i
    i+=1
print(s)

#2 cube of n number
while i<=n:
    s+=i**3
    i+=1
print(s)
#3 square of n odd numbers
i=1
while i<2*n+1:
    s+=i**2
    i+=2
print(s)"""
#4 print square of sum of even numbers
"""
i=0
s=0
while i<=2*n:
    s+=i**2
    i+=2
print(s)
"""
#5 count the digit in a number
"""n=input("Enter the number")
s=len(n)
print(s)
"""
#6
"""n=int(input("enter the number whoes factorial is needed\n"))
i=1
f=1
while(i<=n):
    f*=i
    i+=1
print("The factorial of %d is %d"%(n,f)) """
#7 ##   TO PRINT SUM OF NUMBER OF DIGITS OF A GIVEN NUMBER
n=input("Enter the number\n")
a= sum([int(i) for i in n])  #list comprehension
print(a)
#sum=0
'''for i in n:
    if(ord('i')>=49 and ord('i')<=57):
        sum+=i
        print(sum)'''