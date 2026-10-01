import prog26
x=18.9
y=20.9

def show():
    z=True
    print('In show fn of program30')
    print('last line of show fn of program30')

show()
print(prog26.a) # it prints the value of a from prog26 module
print(prog26.b) # it prints the value of b from prog26 module
print(prog26.show()) # it prints the show fn of program26 module
print(dir()) # it prints the attributes of show fn of program30 module
print(dir(prog26)) # it prints the attributes of show fn of program26 module

