"""
# first: squares of even numbers

# a - map+filter

def f_square(x):
    return x**2


def is_even(x):
    return x % 2 == 0

def convert_square(arr):
    return map(f_square, filter(is_even, arr))

def convert_square_lambda(arr):
    return map(lambda x: x**2, filter(lambda x: x % 2 == 0, arr))

# b - list comprehension

arr = [1,2,3,4,4,5,12,6,67,7,78,78]
new = [i ** 2 for i in arr if i % 2 == 0]

"""
########################################

# second: select some certain letters
"""
def filter1(arr):
    def filter2(dic):
        return dic[0] in arr
    return filter2

def exctract(x):
    return x[1]

strg = "abcdefghijklmnopqrsntuvwxyz"
arr = [1, 5, 8, 2, 7]

# a - map+filter

res = map(exctract, filter(filter1(arr), enumerate(strg)))
for x in res:
    print(x, end='')

"""
"""
dictt = enumerate(strg)
cutted = filter(lambda x: x[0] in arr, dictt)
for x in cutted:
    print(x[1], end='')
"""

# b - list comprehension

# out = [strg[i] for i in arr]

########################################

# third:

# import pyperclip

"""
def f_3_correct(s):
    s1 = s.lower()
    s11 = s[0].upper()
    return s11 + s1[1:]


s = "minimal does NOT mean terse – don't sacrifice communication to brevity. USE consistent naming and indentation, and include comments if needed to explain portions of the code. Most code editors have a shortcut for formatting code – find it, and use it! Also, don't use tabs – they may look good in your editor, but they'll just make a mess on StackOverflow. "
dictionary = s.split(". ")
dictionary.remove('')
dictionary = map(f_3_correct, dictionary)
out = ""
for x in dictionary:
    out += x + ";"

print(out)
"""
