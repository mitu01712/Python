a = "this is a string"
# 0123456789101112131415 array index number
print(a[0])
print(a[15])
print(a[4])

# string er length janar jonno 
print(len(a))#len machine, len method 

# maximum index = total length -1

# print(a[16])
# string index out of range
# ekta string er choto part ke amra bolbo character

# last character print
print(a[len(a) - 1])# ekhane 
print(a[-3])# python e negative index kaj kore
# last character printing (short method)
print(a[-5])
b = "Rahim"
#-5-4-3-2-1
print(b[-2])
print(b[-5])

# string is By default Immutable data type means, 
print(b[1])# output dekhabe a 
#  ekhon ami a er joygay o dite chaschi mane rohim print korte chaschi sei khetre 
b[1] = 'o'
# ekhon jodi amra b ke print kori
print (b)# tahole dekhabe  'str' object does not support item assignment
# etar mane hosche ekbar amra ekta string ke define kore felle next time amra sei string ke r modify or update korte parbo na

# update korte chaile amder python er method use korte hobe

