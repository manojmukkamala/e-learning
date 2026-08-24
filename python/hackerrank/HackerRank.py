#!/usr/bin/env python
# coding: utf-8

# ## Python

# ### Introduction

# Say "Hello, World!" With Python




print("Hello, World!")


# Python If-Else




#!/bin/python3

N = int(input())

if((N%2 != 0) or (N >=6 and N <= 20)): print("Weird")
else: print("Not Weird")


# Arithmetic Operators




if __name__ == '__main__':
    a = int(input())
    b = int(input())

print("{0} \n{1} \n{2}". format((a + b), max(a - b, b - a), (a * b)))


# Python: Division




if __name__ == '__main__':
    a = int(input())
    b = int(input())

print("{0} \n{1}". format(a//b, a/b))


# Loops




if __name__ == '__main__':
    n = int(input())

[print(i**2) for i in range(n)]


# Write a function




def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4 == 0 and (year%100 != 0 or year%400 == 0)): leap = True
    
    return leap

year = int(input())
print(is_leap(year))


# Print Function




if __name__ == '__main__':
    n = int(input())

print(*range(1, n+1), sep = "")


# ### Basic Data Types

# List Comprehensions




if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if((i + j + k)!= n)])


# Find the Runner-Up Score! 




if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])


# Nested Lists




if __name__ == '__main__':
    n = int(input())
    arr = [[input(), float(input())] for _ in range(n)]
    c = sorted(set([b for a, b in arr]))[1]
    print('\n'.join(sorted(a for a, b in arr if b == c)))


# Finding the Percentage




if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('%.2f' %(sum(student_marks[query_name])/len(student_marks[query_name])))


# Lists




if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if (cmd != 'print'):
            cmd += "("+",".join(args) +")"
            eval("l."+cmd)
        else:
            print (l)


# Tuples




if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


# ### Strings

# sWAP cASE




def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# String Split and Join




def split_and_join(line):
    # write your code here
    line = line.split()
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# What's Your Name?




def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Mutations




def mutate_string(string, position, character):
    return string[:position]+character+string[(position+1):]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string




def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        if((string[i:(i+len(sub_string))]) == sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# String Validators




if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.isupper() for c in s))
    print(any(c.islower() for c in s))


# Text Alignment




#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# Text Wrap




import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# String Formatting




def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1, number+1): 
        print(str(i).rjust(w, ' '), str(oct(i)[2:]).rjust(w, ' '), str(hex(i)[2:]).rjust(w, ' '), str(bin(i)[2:]).rjust(w, ' '), sep = ' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


























# ### Sets

# No Idea!




n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(sum([(i in A)-(i in B) for i in arr]))


# Set .add()




n = int(input())
print(len(set(input() for _ in range(n))))


# Set .discard(), .remove() & .pop()




n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    c = input()
    if c == 'pop':
        s.pop()
    else:
        cmd, val = c.split()
        cmd = 's.'+cmd+'('+str(val)+')'
        eval(cmd)
print(sum(s))


# Set .Union() Operation




m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e|f))


# Set .intersection() Operation




m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e&f))


# Set .difference() Operation




m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e-f))


# Set .symmetric_difference() Operation




m = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
print(len(e^f))


# Set Mutations






























