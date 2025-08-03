import math # amra ekhane math ke import korbo math emon ekti module jekhane huge poriman method and function likha ache jeta kono programmer ra likhe rakhche


#ceil
x = 4.5 # ceil mane amra bujhi mathar opor er chad tar mane oporer dike man 4.5 er kacha kachi man 5
#module and packge holo python er kichu build in code je keu likhe rakhche amra just use korbo
y = 4.1 # 4.1 er kacha kachi value holo 5 
print(math.ceil(x))
print(math.ceil(y))



#Floor
a = 4.5 # floor mane niche it's means 4.5 er nicher value holo 4 
b= 0.004
print(math.floor(a))
print(math.floor(b))

#Round
# 3.4
# 3.1 - 3.50 --> Floor hoye jabe 
# 3.51 - 3.99 --> ceil hoye jabe
tax = 420.17
tax1 = 430.56
print(round(tax))
print(round(tax1))

tax2 = input("Enter your tax amount:")# tax2 te amra jehetu string rekhechi tai tax2 ke float e convert kore nite hobe
tax2 = float(tax2)
tax_round = (round(tax2))
print(tax_round)