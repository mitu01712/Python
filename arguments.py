#function define time e amra jei value pass kortechi function er moddhe setai arguments jeta asole ekta variable
# r jokhon function call kortechi tokhon take botechi parameter
# def addition(a,b):
#     result = a+b
#     return result
# r = addition(12,10)
# print(r)

def addition(*args):# *args it means ekhane multiple arguments thakte parbe
    print(args)# ekhane amra function er parameter e jei value gula diyechi segulo ke *args by default tuples akare print korbe
    return sum(args)

r = addition(12,10, 2, 18, 10)
print(r)