# list_comprehension er comprehence means sngkocit 
# ba short kora
a = [1, 10, 23, 24, 26, 90]# new ekta list banao a list er jei number gula 2 dara bivagjo tader ke niye 
result = []
#Normal way 
print(10/3)
print(10//3) # // diye amra vagfol pabo output 3 asbe
# 3)10(3 # eta // diye pab0
#    9
# -------
#    1 # vag sesh pabo % eta use kore
print(10%3)

for i in a:
    if i % 2 == 0:
        result.append(i)# append() method list er sesh e item add kore
print(result)   

# ei same kaj amra aro easy way te korte parbo
#List comprehension

new_result = [i for i in a if i%2==0]
print(new_result) 
# etai list comprehension

b = [1, 2, 3, 4, 5] # --> [1, 4, 3, 16, 5]

# for i in b:
#     if i%2 == 0:
#         i**2
#     else:
#         i

b_new = [i**2 if i%2 == 0 else i for i in b]
print(b_new) 

# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# The remove() method removes the specified item.

# ExampleGet your own Python Server
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  #list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".?