from itertools import chain
with open("Level3crosses.txt") as a:
    lines = a.readlines()
new_list = [s.replace("\n", "") for s in lines]
sorted_new_list = sorted(new_list)
print(sorted_new_list)

first = [i.split(' ')[0] for i in sorted_new_list] 
second = [i.split(' ')[1] for i in sorted_new_list] 
third = [i.split(' ')[2] for i in sorted_new_list]


test = list(chain.from_iterable(zip(first, second, third)))
chunks = [test[x:x+3] for x in range(0, len(test), 3)]
print(chunks[2][2])

def Sort(chunks):
 
    chunks.sort(key = lambda x: x[2])
    return chunks

print(Sort(chunks))
order = 0
boer = 0 
ww1 = 0 
ww2 = 0

listing = list(map(' '.join, chunks))
print(listing)

for x in listing:
    if "BOER" in x:
        boer += 1      
    if "WWI" in x:
        ww1 += 1 
    if "WWII" in x:
        ww2 += 1

war_boer = listing 
        
