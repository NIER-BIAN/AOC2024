#==============================================================
# Pt1

list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        numbers = line.strip().split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

list1.sort()
list2.sort()

differences = [
    abs(list1[i] - list2[i]) for i in range(len(list1))
                                            ]
print(sum(differences))

#==============================================================
# Pt2

list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        numbers = line.strip().split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

occurCount = [list2.count(i) for i in list1]

products=[]
for i in range(len(occurCount)):
    products.append(list1[i] * occurCount[i])

print(sum(products))
