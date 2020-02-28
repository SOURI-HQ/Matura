import random
# return a valid list of attributes of the object => print(dir(random))
# print(help(random.random))

# Generating random numbers from interval [0,1)
for i in range(3):
    print(random.random())

# Generating random numbers from interval [3,7)
# The random() function can be used to build customized random number generators.
print("\n")
def my_random():
    # Random, scale, shift & return
    return 4*random.random() + 3
for i in range(3):
    print(my_random())
# UNIFORM RANDOM
print("\n")
for i in range(3):
    print(random.uniform(3, 7))
# BELL CURVE NUMBER GENERATION
print("\n")
for i in range(3):
    print(random.normalvariate(5, 0.2))

# RANDINT
print("\n")
for i in range(3):
    print(random.randint(1,6))

# RANDOM ELEMENT FROM A LIST
print("\n")
outcomes = ['rock', 'paper', 'scissors']
for i in range (3):
    print(random.choice(outcomes))