from sympy import *
import sys
import webbrowser
from tabulate import tabulate
import tokenize
from collections import deque

def main():
    print("Welcome to Newton Raphson Method!")
    print()
    input("Program will find appoximation of your function.\nPress enter to continue...")
    print()
    function, initial_guess = menu()
    closest_integer = find_interval(function, initial_guess)
    
    last_two = deque(maxlen=2)
    newton_number = newton(function, closest_integer)
    line_break = "-" * 120
    precision = int(input("Set precision for optimization[It will affect the duration of the output process]: "))
    print(line_break)
    while True:
        try:
            approx = next(newton_number)
            input("Press enter to approximate next value...")
            last_two.append(approx)
            print(line_break)
        except KeyboardInterrupt:
            exact_lines = checker_exact_lines (last_two[0],last_two[1],precision)
            digit_exact_lines = len(exact_lines)
            digit_exact_lines = digit_exact_lines - 2
            with open("result.txt", "w") as file:
                file.write(exact_lines)
                file.write(f"\n\n{digit_exact_lines} digits of accuracy")
            sys.exit(f"\nExiting...")



    



def newton(function, closest_integer):
    x = symbols("x")
    while True:         
        closest_integer = closest_integer - (function.subs(x, closest_integer)/ diff(function,x).subs(x, closest_integer))
        yield closest_integer


def checker_exact_lines(first,last,precision):
    matching_digits = ''
    first = N(first, n= precision+1)
    last  = N(last, n= precision+1)
    str_first = str(first)
    str_last  = str(last)
    if '.' in str_first:
        integer_part1 = str_first.split('.')[0]
        decimal_part1 = str_first.split('.')[1]
    else:
        decimal_part1 = ""
    
    if '.' in str_last:
        integer_part2 = str_last.split('.')[0]
        decimal_part2 = str_last.split('.')[1]
    else:
        decimal_part2 = ""
    min_length = min(len(decimal_part1), len(decimal_part2))
    for i in range(min_length):
        if decimal_part1[i] == decimal_part2[i]:
            matching_digits += decimal_part1[i]
        else:
            break
    return f"{integer_part1}.{matching_digits}"
    






def menu():
    while True:    
        table_data = [
        [" ", "Please select one of the following options:"],
        ["1:", " Start typing your function"],
        ["2:", " How to type your function"],
        ["3:", " What is Newton Raphson Method"],
        ["4:", " Exit"],]

        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
        x = input()

        if x == "1":
            function = getter_function()
            initial_guess = checker_initial_guess()
            
            return function, initial_guess

            
        
        elif x == "2":
            sign_data = [
        ["sign", "Its function:"],
        ["x:", "variable"],
        ["*", "multiplication"],
        ["**", "exponent"],
        ["+", "addition"],
        ["-", " subtraction"],
        ["/", "division"],
        ["()", "organizes the function"],
        ]

            print(tabulate(sign_data, headers="firstrow", tablefmt="grid"))
            print()
            input("----Press enter to go back to menu---")
            print()

        elif x == "3":
            webbrowser.open("https://en.wikipedia.org/wiki/Newton%27s_method")
            print()
            input("----Press enter to go back to menu---")
            print()

        elif x == "4":
            sys.exit(tabulate([["exiting..."]], tablefmt="grid"))
        else:
            input("Invalid input. Please try again.")
            print()


def getter_function():
    while True:
        try:
            function = input("Enter your function[must be in x]: ")
            if "x" not in function:
                raise SyntaxError
            function = parse_expr(function, evaluate=False)
            return function
        except  (SyntaxError, SympifyError, tokenize.TokenError):
            input("Invalid input. Please try again.")
            print()

def checker_initial_guess():
    while True:
        try:
            initial_guess = int(input("Enter initial guess[A number may be close to root of the function]: "))
            if initial_guess < 0:
                raise ValueError
            return initial_guess
        except ValueError:
            input("Input must be a integer.")
            print()


def find_interval(function, initial_guess):
    x = symbols("x")
    while True:
        if  abs(function.subs(x, initial_guess)/ diff(function).subs(x, initial_guess)) > 1:
            initial_guess = initial_guess - N(function.subs(x, initial_guess)/ diff(function).subs(x, initial_guess), n= 1)
            print(initial_guess)        
        else:
            return (int(initial_guess))

        
        
        
        




if __name__ == "__main__":
    main()
