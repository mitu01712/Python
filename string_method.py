a = "rahim"
print(a.title())#title() method er kaj hosche 1st ta boro hater baki gula choto hater thakbe
print(a)#ekhane output: rahim asbe it's means a variable ekbar amra jei string likhe felchi eta change korte parbo na but ami chaile string function use kore a variable er string ke modify korte parbo but amder main string er kono rokom change hobe na // etai python er immutable string

b = a.title() # ekhane a ke notun kore reassing kora hoyeche 
print(b) 
print(a)

d = "joy"
print(d.upper())
e = "TANmOY"
print(e.lower())
print(e.swapcase())# choto hater ta boro hat er kore dey abar boro hater ta choto hater kore dey
txt = " I Like bananas"
x = txt.replace("bananas", "apples")
# replace("konta ke change korbo", "oitar jaygay ki bosabo")
print(x)
print(txt) # main string e kono change hobe na
print(txt.count('a')) #variable txt er vitore jei string ache sei string tar moddhe koy ta a litter ache seta count kore

txt = "hello, and welcome to my world."

x = txt.capitalize()# capitalize() method er kaj hosche sentence er first letter ke capital kore deoya

print (x)

txt = "Hello, And Welcome To My World!"

x = txt.casefold()# casefold() method er kaj holo sentence er 1st letter ke small letter baniye deoya
#This method is similar to the lower() method

print(x)

txt = "banana"

x = txt.center(20)

print(x)

txt = "banana"

x = txt.center(20, "O")# center() method er kaj holo 20 index er jayga memoryte store hobe first last seven character defualt thakbe center e banana bosbe // ekhane jehetu "o" deoya hoyeche tar mane 1st and last 7 ta index o dara fillup thakbe

print(x)



