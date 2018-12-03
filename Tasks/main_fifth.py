"""
with open("test.txt", 'w') as f:
    f.write(input())
f = open("test.txt", 'rb')
for line in f:
    print(line)
f.close()
"""
"""
import json

dict = {1: (1, 2, 3), 2: {"Name": "Vasya", "Surname": "Pupkin"}}
print(json.dumps(dict))

with open("json.html", 'w') as f:
    json.dump(dict, f)
"""
"""
import pickle

dict = {1: (1, 2, 3), 2: {"Name": "Vasya", "Surname": "Pupkin"}}
dict0 = pickle.dumps(dict, protocol=0)
dict1 = pickle.dumps(dict, protocol=1)

with open("pickle0.txt", 'wb') as f:
    f.write(dict0)

with open("pickle1.txt", 'wb') as f:
    f.write(dict1)
"""
import sys
import argparse
import itertools

parse = argparse.ArgumentParser(description='lalala')
parse.add_argument('-n', dest='start', action='store',type=int,required=True,help='Start number of the sequence')
parse.add_argument('-i', dest='step', action='store',type=int,required=True,help='Step of the sequence')
#parse.add_argument('-f', dest='path', action='store',type=str,required=False,help='Step of the sequence')
subparsers = parse.add_subparsers(dest='mode')
savesub = subparsers.add_parser('save')
savesub.add_argument('-f', dest='path', type=str, required=True)

showsub = subparsers.add_parser('show')
#savesub.add_argument('-c', dest='len', type=str, required=True)

args = parse.parse_args(sys.argv[1:])
if args.mode == 'save':
    f = open(args.path, 'w')
    sys.stdout = f
    iter_ = range(10)
elif args.mode == 'show':
    iter_ = itertools.count(1, 1)
else:
    sys.exit(-1)


for i in iter_:
    print(args.start + i * args.step)
if args.mode == "save":
    f.close()
