#!/usr/bin/python3
i = 96
result = ""
while i < 122:
    i = i+1
    if i == 101 or i == 113:
        continue
    result = result + chr(i)

print('{0}'.format(result), end="")
