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




