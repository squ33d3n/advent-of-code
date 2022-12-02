#get data from input
with open('Day1\Day1.in') as file:
    data =[i for i in file.read().strip().split("\n")]


#parse data
calhigh = 0
calhigh2 = 0
calhigh3 = 0
calcount = 0
for item in data:
    if item == '': 
        calcount = 0 
    else: 
        num = int(item)
        calcount += num 

    if calcount > calhigh:
         calhigh = calcount
    elif calcount > calhigh2:
        calhigh2 = calcount
    elif calcount > calhigh3:
        calhigh3 = calcount


print("Elf that has the most calories has", calhigh)
print("Elf with the second most has", calhigh2)
print("Elf with the third most has", calhigh3)
print("Together the three elves that have the most calories equals", calhigh+calhigh2+calhigh3)