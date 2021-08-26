#!/usr/bin/env python3

'''Functions'''
def greet():
    print("Hello")


def greet_user(user):
    print(f"Yo, {user.title()}")


def car(make, model):
    print(f"I drive a {make} {model}")


def calc(n1, n2):
    return n1, n2


def division(first, second):
    value=first / second
    return value


# Keyword Args
def div_2(first, second):
    value=first / second
    return value


# Keyword ars
def fun(p1, p2, p3):
    print("lowest number: " + p3)


# Arbitrary keyword args
def arbitrary(**dude):
    print("first name: " + dude["fname"])


# pass a list
def list_func(things):
    for x in things:
        print(x)


stuff=['apple', 'car', 'house']


# tip calculator
def tip_calc(bill, tip_perc=10):
    total=bill * (1 + 0.01 * tip_perc)
    total=round(total, 2)
    print(f"Total due: ${total}")


#Passing user input with a while loop
def pretty_desc(opsys, distro):
    full=f"{opsys} {distro}"
    return full.title()


while True:
    c_opsys=input("Operating System: ")
    c_distro=input("Distro: ")

    clean_output=pretty_desc(c_opsys, c_distro)
    print(f"{clean_output}")
    break


# *args **kwargs
def argkwargs(a, b, *args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Lambda function
x=lambda a: a + 10
print(x(5))


def myfunc(n):
    return lambda a: a * n


mydoubler=myfunc(2)


# There are many situations in programming, in which the exact number of necessary parameters cannot be determined a-prior
# Therefore just use an astrix *
def arithmatic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
            arbitrary number of numerical values """

    return (first + sum(values)) / (1 + len(values))


# Call all functions
greet()
greet_user('dude')

a, b=calc(5, 10)
print(f"returned from calc: {a},{b}")
output=division(12, 3)
print("output is: ", output)
output=division(first=40, second=20)
print("output is: ", output)
fun(p1="a", p2="b", p3="c")
arbitrary(fname="The", lname="dude")
list_func(stuff)
tip_calc(15)
car('Toyota', 'Camry')
argkwargs('Python', 'for', 'OOP', first="Python", mid="for", last="OOP")
# lambdas
print(x(5))
print(mydoubler(11))

# arithmatic mean
print(arithmatic_mean(45, 32, 89, 78))
print(arithmatic_mean(8989.8, 78787.78, 3453, 78778.73))
print(arithmatic_mean(45, 32))
print(arithmatic_mean(45))
