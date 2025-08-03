# Multipul types data niye kaj korte python e list and tuple use kora hoy
a = [1, 2, 3, 'Naim', 'Fahim', 8.9, 3.4]
# # list is mutable // it's means amra chaile list er data update ba modify korte parbo.
# a[0] = 'Mitu'
# print(a)
# print(a[-1])#last index e kon value ache 
# print(len(a))# total index number print korbe

# # s = "Hello" -->('H','e','l','l','o')
# # python e list() and str() nam e build in function ache
# s = "Hello"
# print(list(s))# ekhon e list() function hello ke split kore felbe
# s1 = "he ll o" # ekhane space gula ke string e dhore print korbe
# print(list(s1))

a.append([1,2,3]) # append ()function er maddhome amar list e new number, string or new list add korte parbo seta list er last e giye add hobe
print(a)
print(a.index(3)) # 3 list er koto number index e ache
# print(a.index(300)) # 300 amader index e nei

#perticular index e insert
a.insert(5, "mitu") 
print(a)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")# remove() method use kore amra list er jekono kichu delete korte paarbo
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)# pop(index_number) method use koreo amra je kono index er value delete korte pari
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()# pop() method er vitore jodi index number na bole dei tahole last index er value delete hobe
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()# clear() use kore amra list er sob value remove korte parbo than amder ekta emty [] list show korbe
print(thislist)

b = [1, 2, 3, 4, 'mitu', 'tanmoy', 'joy']
b.reverse()# ulta dik theke list e print korbe
print(b)

# tuple() --> tuple() method holo immutable //it's mean amra chaileo tuple ke update, remove, modify korte parbo na

t = (1, 2, 3)
t_r =tuple(reversed(t))# ulta dik theke ekta new tuple dibe
print(t)
print(t_r)
# t[0] = 100
# print(t) eta amra korte parbo na
# c=(1,)etio tuple 

# range of index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])# age : means ager gula print hobe 0 index theke 4 porjonto

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # pore : means index 2 theke last porjonto print hobe

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#This example returns the items from index -4 (included) to index -1 (excluded)

#update tuple 

tuple1 = ['mitu', 'satu','joy','jibon']
x = list(tuple1)
x[1]= 'Tanmoy'
tuple1 = tuple(x)
print(tuple1)

c = [1, 3, 4, 5, 6, 7]
d = list(c)# ekhane amra list()method use kore immutable tuple ke update korte pari
d[2] = 8
c = tuple(d)
print(c)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


# The del keyword can delete the tuple completely:

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists