# Decorators notes
These notes accompany decorators.py

# jim smith will print to the screen
  emp_1.fullname = 'jim smith'


# More concise that listing three seperate print statements verticaly
print(f"{emp_1.first}\n{emp_1.email}\n{emp_1.fullname}")

# The print(f"") above gives the same results as the
#individualy stacked ones below

#print(emp_1.first)
#print(emp_1.email)
#print(emp_1.fullname)

# This code enables the user to change the employee's name, without rewriting the code
# Because emp_1 = Employee('the', 'dude')
# acts as aa place holder & anything you write in..
# emp_1.fullname = ' '
# that will go in the template and be coded-in printed to the screen

#-----------------End of Notes------------------------------------
