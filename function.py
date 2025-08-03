# # 2 types function 
# # 1. user define function--> programmer nijer moto kore function banabe
# # 2. Build in function --> eta already banano ache 
# # jemon: print(), input(), sum()
# print("Hello") #--> ekhane print() function ta box er moddher juice 
# input("Enter your Name: ") # input() function tar vitorer jinis ke amra chaile modify korte parbo 
# user_input = input("Enter your Name: ")# eta glass er juice jeta amke ekta jinis return kore
# print(f"Hello {user_input*2} ")
# mx = max([1, 2, 3, 4])# ekhaneo same input(), and max() function ke amra chaile ekta variable er moddhe store korte pari and chaile print or customise korte pari
# print(f"max value {mx}. {mx*3}")# ekhene output asbe max value 4 // 4*3 = 12
# # ekta function jodi return kore tahole amder print() function ke use kortei hobe r jodi ekta function jodi print kote tahole amra chaile take customise korte pari na or print() function ke konno kono variable e store korte pari na

# user define function 


# type-01 No input, No return

def my_first_function():
    a = 10
    b = 12
    print(a+b)

my_first_function()# ekane function take call kora hoyeche
# ekhane my_first_function() kono input ney and return o nei

#type-02 input thakbe but No return

def add_two_numbers(a,b): # function er vitore amra jei variable dei ei gula holo arguments
    print(a+b)

add_two_numbers(10,5)# function call er madhome amra jei value pass korchi ei value gula ke bole parameters
add_two_numbers(10,5)

# type 3- input thakbe sathe return o thakbe

def multiply_two_nums(a,b):
    return a*b
result = multiply_two_nums(12,2) 
# kono function jodi kichu return kore tahole amder ekta variable er moddhe store korte hobe
print(result)

# No input but return thakbe

def hello():
    return "Hello"
gettings = "Hello"
print(gettings)

# function return korle obossoi ekta variable er vitore function ke store korte hobe
 
