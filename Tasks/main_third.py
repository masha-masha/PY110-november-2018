"""
def fib():
    yield 0
    a = 0
    b = 1
    while b < 100:
        yield b
        a, b = b, a + b


for i in fib():
    print(i)
"""
"""
import itertools

def prime():
    prime_set = set()
    prime_set.add(2)
    yield 2
    for i in itertools.count(3, 2):
        if all(i % pr_nm for pr_nm in prime_set):
            prime_set.add(i)
            yield i

for i in prime():
    print(i)
"""
"""
#######################################
# first task: all words in text generator
def tear_into_words(s):
    n1, n2 = 0, 0
    while n1 >= 0:
        try:
            n2 = s.index(' ', n2)
        except ValueError: # if index() can't find substring, the exception will be raised, not return -1
            yield s[n1:len(s)]
            break
        yield s[n1:n2]
        n2 += 1
        n1 = n2


text = "If you use any(lst) you see that lst is the iterable, which is a list of some items. If it contained [0, False, '', 0.0, [], {}, None] (which all have boolean values of False) then any(lst) would be False. If lst also contained any of the following [-1, True, "X", 0.00001] (all of which evaluate to True) then any(lst) would be True. In the code you posted, x > 0 for x in lst, this is a different kind of iterable, called a generator expression. Before generator expressions were added to Python, you would have created a list comprehension, which looks very similar, but with surrounding []'s: [x > 0 for x in lst]. From the lst containing [-1, -2, 10, -4, 20], you would get this comprehended list: [False, False, True, False, True]. This internal value would then get passed to the any function, which would return True, since there is at least one True value. But with generator expressions, Python no longer has to create that internal list of True(s) and False(s), the values will be generated as the any function iterates through the values generated one at a time by the generator expression. And, since any short-circuits, it will stop iterating as soon as it sees the first True value. This would be especially handy if you created lst using something like lst = range(-1,int(1e9)) (or xrange if you are using Python2.x). Even though this expression will generate over a billion entries, any only has to go as far as the third entry when it gets to 1, which evaluates True for x>0, and so any can return True. If you had created a list comprehension, Python would first have had to create the billion-element list in memory, and then pass that to any. But by using a generator expression, you can have Python's builtin functions like any and all break out early, as soon as a True or False value is seen."

for x in tear_into_words(text):
    print(x)
"""
#######################################
# second task
"""
def random_numbers(seed):
    n = seed
    while True:
        yield n
        n = n >> 1 | n << 1

c = 10
gen = random_numbers(c)
gen1 = random_numbers(c)
for i in range(10):
    print(next(gen))
    print(next(gen1), end='\n\n')
"""
#######################################
# third task:
"""

def arifm_prog(start):
    n = start
    while True:
        n_new = yield n
        if n_new == None:
            n += 1
        else:
            n = n_new
"""
