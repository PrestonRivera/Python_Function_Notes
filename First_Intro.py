def create_introduction(name, age, height, weight):
    first_part= "My name is " + name + " and I am " + age + " years old."
    second_part= " I am " + height + ", and my weight " + weight + " pounds."
    full_intro= first_part + second_part
    return full_intro

def short_intro(name, height, weight):
    print(f"My name is {name}. I am {height} and i weight {weight} pounds. I have dedicated months to learn how to code. Ive been in the telecom industry for around 8 years.
          Ive spent alot of time away from family and learned I dont want to live my life like that anymore. Learning to program has given me the oppurtunity to change that.
          I am a fast learner and a hard worker dedicated to getting the task at hand done.")

intro = create_introduction("Preston", "28", "5'10", "140")
print(intro)



name = "Preston Rivera"
height = "5'10"
weight = 140

short_intro(name, height, weight)











