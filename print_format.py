# 1. F-strings (Formatted String Literals)
name = "Alice"
age = 30
height = 1.75

print("F-String format printing : ")
print(f"My name is {name}, I am {age} years old, and I am {height:.2f} meters tall.")


# 2. str.format() Method
name = "Bob"
score = 85

print("std.format() printing : ")
print("Player: {}, Score: {}".format(name, score))
print("Player: {0}, Score: {1}".format(name, score)) # Positional arguments
print("Player: {p_name}, Score: {p_score}".format(p_name=name, p_score=score)) # Keyword arguments