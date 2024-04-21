def create_introduction(name, age, height, weight):
    first_part= "My name is " + name + " and I am " + age + " years old."
    second_part= " I am " + height + ", and my weight " + weight + " pounds."
    full_intro= first_part + second_part
    return full_intro

def short_intro(name, height, weight):
    print(f"My name is {name}. I am {height} and i weight {weight} pounds soak and wet")

intro = create_introduction("Preston", "28", "5'10", "140")
print(intro)



name = "Preston"
height = "5'10"
weight = 140

short_intro(name, height, weight)











