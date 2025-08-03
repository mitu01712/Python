#set python
#{} 
# unordered --> it's means indexing kore value pawa jabe na 
# immutable --> no update ,no delete eta python er string and tuple er moto 
#no duplicates --> it's mean ekta set e same item thaka jabe na
#set()

a = [1, 2, 2, 3, 4, 4, 4, 5]# ekhane 5 ta unic value ache
s = set(a) 
print(a)# ekhane same value print hosche karon immutable bole
print(s)

# union, Intersection
# Intersection hosche tuita set er moddhe jei common value thake oi value gula noye sei set hoy
a = {1, 2, 3}
b = {2, 3, 4}

c = a.intersection(b)
print(c)

d = a.union(b)
print(d)

# union --> it's mean tui ta set duplicate value bade sob value niye new set create kore
