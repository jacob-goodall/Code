with open("Level3crosses.txt") as a:
    lines = a.readlines()
new_list = [s.replace("\n", "") for s in lines]
sorted_new_list = sorted(new_list)
print(sorted_new_list)

chunks = [sorted_new_list[x:x+3] for x in range(0, len(sorted_new_list), 3)]
print(chunks)