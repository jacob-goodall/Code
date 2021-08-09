file = open('Level3crosses.txt',"r")
Counter = 0
# Reading from file
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1
print(counter)