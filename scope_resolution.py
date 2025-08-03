# scope --> a region where a variable is accessible// 
x = 10 # eta ekta Global variable ar global variable ke amra je kono jayga theke access korte pari
print(x)

def func():
    y = 19 # ei y ke amra baire theke print korte parbo na karon eta ekta local variable
    x = 200
    print("Y =",y)# ekhane amra y ke print korte parbo local variable
    print("X =",x)# ekhane x er value 200 print hobe karon, ekhane global variable ke local variable e modify kora hoyeche 
func()  
#print(y)# amra ekhane y ke print korte parbo na 

# amra chaile global variable gulo ke local variable er moddhe modify or update kore felte pari

#LEGB 
# L = local
# E = Enclosing
# G = Global
# B = Built in Scope jokhon amra build in function use kori tokhon eta mainly kaj kore jemon(print, sum, max, input)

n ="global_variable" # Global variable

def outer():
    n = "enclosing_variable"# Enclosing variable
    def inner():# nastted function
        #n = "local_variable" # local variable
        #ekhon amra jodi chai global variable ke local variable e print korte 
        # global n # global keyword tar power nai enclosing_variable ke change korar // eta just global variable ke update kore
        # n = "local_variable"
        # print(n)# ekhane print korle amra output pabo local_variable

        # ekhon amra jodi ei scope er moddhe enclosing variable ke change or update korte chaitam sei khetre nonlocal keyword use korbo
        nonlocal n
        n = "Local_variable"
        print(n)

    inner()
    print(n)#ekhane print korle amra output pabo enclosing_variable
outer()
print(n)# ekhane print korle amra output global_variable pabo
# ekhon ekhane output asbe local_variable

# global keyword ---> global variable ke change korte pare, not enclosing ke
# nonlocal keyword ---> enclosing variable ke change korte pare not globale ke