with open('Level3crosses.txt') as a:
  lines = a.readlines()

print(lines)

new_list = [s.replace("\n", "") for s in lines]

print(new_list)