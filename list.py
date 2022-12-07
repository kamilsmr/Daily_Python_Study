# Listö
# mylist = [1,2,3]
# mylist = ['stringadgasfd',1,2,3,4,23,True,'asdf',[1,2,3]]

# print(len(mylist))

mylist = ['a','b','c']

print(mylist[0])
print(mylist[-1])

print(mylist[1:])
print(mylist[:3])


#change item
mylist = ['a','b','c','d','e']
print('before reassignment')
print(mylist)
mylist[0]= 'NEW ITEM'
print("after reassignment")
print(mylist)

# append
mylist = ['a','b','c','d','e']
mylist.append("NEW ITEM")
print(mylist)

mylist = ['a','b','c','d','e']
mylist.append(["x","y","z"])
print(mylist)


#extend
mylist = ['a','b','c','d','e',["x","y","z"]]
listtwo = [8,9]
mylist.extend(listtwo)
print(mylist)

mylist = ['a','b','c','d','e']

# pop
mylist = ['a','b','c','d','e']
item = mylist.pop()
item = mylist.pop(0)
print(mylist)
print(item)

# reverse
mylist = ['a','b','c','d','e']
mylist.reverse()
print(mylist)


# sort
mylist = [4,6,1,7,2,9,3]
mylist.sort()
print(mylist)




