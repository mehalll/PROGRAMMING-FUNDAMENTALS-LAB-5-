def check_palindrome(string):
    string = string.casefold()
    reverse = string[::-1]
    if reverse==string:
        print("\nYes, this string is Palindrome")
    else:
        print("\nNo, this string is not Palindrome")

user = input("Please enter a string to check wether its Palindrome or not : ")
check_palindrome(user)
