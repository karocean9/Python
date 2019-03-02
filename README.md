# Python
Python Reference 

# if-else
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Constraints 
1<=n<=100

```
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])
```    

# Arithmetic_Operation
Task:
Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Input Format:
The first line contains the first integer,a . The second line contains the second integer,b.

Constraints:
1<=a<=10power(10)
1<=b<=10power(10)

```
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)
```

# Loops

Read an integer,N . For all non-negative integers i<N, print i square

Constraints:

1<=N<=20

```
n = int(input())
for x in range(n):
    print(x**2)
    if x==n:
        break
```
# Function

You are given the year, and you have to write a function to check if the year is leap or not.

1900<=year<=10power(5)

```
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    leap = True
year = int(input())
print(is_leap(year))
```

# Valid Phone number using regular expressions

Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a7,8 or 9.

Constraints
1<=n<=10
2<=len(number)<=15
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

```
import re 
for i in range(int(input())) : 
    if re.match(r'[789]\d{9}$',input()): 
        print('YES') 
    else: 
        print('NO')
```
        
here import re is importing regular expressions


