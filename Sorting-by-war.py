from itertools import chain

i = []
myList = []
with open("Level3crosses.txt") as a:
    lines = a.readlines()
new_list = [s.replace("\n", "") for s in lines]
sorted_new_list = sorted(new_list)
print(sorted_new_list)

first = [i.split(' ')[0] for i in sorted_new_list] 
second = [i.split(' ')[1] for i in sorted_new_list] 
third = [i.split(' ')[2] for i in sorted_new_list]

orders = 0

test = list(chain.from_iterable(zip(first, second, third)))
chunks = [test[x:x+3] for x in range(0, len(test), 3)]
print(chunks[2][2])
