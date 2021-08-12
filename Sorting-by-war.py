from itertools import chain

with open("Level3crosses.txt") as a:
    lines = a.readlines()
new_list = [s.replace("\n", "") for s in lines]
sorted_new_list = sorted(new_list)


first = [i.split(" ")[0] for i in sorted_new_list]
second = [i.split(" ")[1] for i in sorted_new_list]
third = [i.split(" ")[2] for i in sorted_new_list]


test = list(chain.from_iterable(zip(first, second, third)))
chunks = [test[x : x + 3] for x in range(0, len(test), 3)]


def Sort(chunks):

    chunks.sort(key=lambda x: x[2])
    return chunks


Sort(chunks)
order = 0
boer = 0
ww1 = 0
ww2 = 0

listing = list(map(" ".join, chunks))


for x in listing:
    if "BOER" in x:
        boer += 1
    if "WWI" and not "WWII" in x:
        ww1 += 1
    if "WWII" in x:
        ww2 += 1
ww1 = ww2 - ww1
war_boer = listing[:boer]
war_1 = listing[boer : boer + ww1]
war_2 = listing[boer + ww1 :]


sorted_war_boer = sorted(war_boer)
sorted_war_1 = sorted(war_1)
sorted_war_2 = sorted(war_2)
