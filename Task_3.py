# Your solution comes here
four_digit = int(input("Enter a four digit: "))
palindrome = False
one = four_digit // 1000
two = (four_digit // 100) % 10
three = (four_digit %100) // 10
four = (four_digit % 100) %10

if one == four and two == three:
    palindrome = True
