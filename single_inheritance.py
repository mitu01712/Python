#single Inheritance

class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
        

class Father (GrandFather):
    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby = hobby
        print(f"My father's favatite color is {self.color} and his first name is {self.first_name} and his hobby is {self.hobby}")

gf1 = GrandFather("red", "Ghosh")
print("My Grendfather's favarit color",gf1.color, "and his first name was",gf1.first_name)

f1 = Father("Football","Green","Ghosh")

#output:
# My Grendfather's favarit color red and his first name was Ghosh
# My father's favatite color is Green and his first name is Ghosh and his hobby is Football
