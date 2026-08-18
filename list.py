list=["shreyas",20]
print(list)

list.append(1)
print(list)

list=[1,3,4,5,6,20]
print(list)

list.insert(1,2)
print(list)

list[2]=9
print(list)

list.extend([8,7,6,0])
print(list)

print(list[5])

list.remove(6)
print(list)

list.pop()
print(list)
 
del list[4]
print(list)

print(len(list))

if 6 in list :
    print("element is present")

else:
    print("element is not present")

for i in list:
    print(i)    
   
print(list.count(9))

print(list.index(4))

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list2=[22,33,44,55,66,77,88,99]

list3=list2
print(list3)

list.clear()
print(list)
