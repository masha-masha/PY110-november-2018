import requests
from numpy import floor, sqrt


def next_prime(n):
    assert(isinstance(n, int))
    if n % 2 == 1:
        n += 1
    for x in range(n + 1, 2 * n + 2, 2):
        last = int(floor(sqrt(x)))
        flag = False
        for y in range(3, last + 1, 2):
            if x % y == 0:
                flag = True
                break
        if not flag:
            return x


# requests.get() SAMPLE
param = {"id": "5"}
proxy = {'http': 'http://UserVPN:UserVPN@192.168.17.1:8080/', 'https': 'http://UserVPN:UserVPN@192.168.17.1:8080/'}
a = requests.get("http://192.168.16.114:5000/api/task?id=5")#, proxies=proxy) #, params=param
print(a.text)

# requests.post() SAMPLE
k = next_prime(a.text['number'])
with open('test.txt', 'r') as f:
    r = requests.post('http://192.168.16.114:5000/', data={'number': str(k)}, files={'file': f})
"""
print(next_prime(10))
print(next_prime(100))
print(next_prime(1000))
"""
