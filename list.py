list= [1,2,"a", 5, 6, 7]
print(list)

list.append(1)
print(list)

list.insert(4,3)
print(list)

list[2]=10
print(list)

list.extend([8,9,10])
print(list)

print(list[7])
list.remove(1)

print(list)

list.pop(6)
print(list)

list.pop()
print(list)

del list[1]
print(list)

print(len(list))

if 2 in list :
    print("element is present")
else:
    print("element is not present")

for i in list:
    print(i)

print(list.count(4))

print(list.index(5))

list.sort()
print(list)

list.sort(reverse = True)
print(list)

new_list = list.copy()
print(new_list)

list.clear()
print(list)

list2 =[1,2,4,5,6]
list3 = list2.copy()
print(list3)