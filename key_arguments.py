#key Arguments
# def my_func(f_name, l_name, age):
#     print(f"My name is {f_name} {l_name}. I am {age} years old.")
    # my_func("Mitu", "Ghosh", 25)
    #ekhon jodi amra kono karone vule jai first name kothay age naki last name age it's mean amra sequence ta haray feli tahole amra ki korbo

    # amra jodi vule jai kon arguments ta kon parameter er sathe jabe sei khetre amra key arguments use korbo
# my_func(age = 25, l_name = "Ghosh", f_name = "Mitu")

# Arbitary Number of key word arguments chole ase 
# it means koto gula arguments thakbe seta amra jani na sei khetre amra ki korbo//Multiple key word arguments thakle kothon amra use kori **kwargs or **data **jhuigh eigula use korlei hobe

def my_func(**kwargs):
    print(kwargs)# eta amrke dictionary formate key arguments gula diye dibe
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old. I got {kwargs['marks']} in programming. I live in {kwargs['address']}")
    
          
my_func(age = 25, l_name = "Ghosh", marks =95, f_name = "Mitu", address = "Dhaka")