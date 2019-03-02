import re
n = int(input())
pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for i in range(n):
    x,y = input().split(" ")
    if re.match(pattern,y):
        print(x,y)
