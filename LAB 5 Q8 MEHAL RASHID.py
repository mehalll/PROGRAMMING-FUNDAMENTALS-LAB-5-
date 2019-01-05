def reverse_name(string):
    string = string.casefold()
    name_r = string[::-1]
    print("Name Reversed          :",name_r)


name = input("Please enter your name : ")

reverse_name(name)
