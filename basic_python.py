name = "Python Learner"
age = 25
is_learning = True

print("Name:", name)
print("Age:", age)
print("Learning Python:", is_learning)

# Conditional statement
if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")

# Loop example
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Function example
def greet(user_name):
    return f"Hello, {user_name}! Welcome to Python."

print(greet(name))
