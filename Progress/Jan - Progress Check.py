
#Converter - currency/temperature
import math
import os

def dollar():
    print("Conversion of Pound to Dollar:")
#shows user selected choice
    while True:
        try:
            choice1 = float(input("Enter amount: £"))
#input amount to convert
        except ValueError:
            print("***************Error*****************")
            dollar()
#if input isn't a number runs prog again
        else:
            choice1a = "{:.2f}".format(int(choice1) * 1.24)
#answer = 2 decimal places
            print("$" + str(choice1a))
#displays answer
            print("----------------Next-----------------")
            afterc()
#run next choice prog

def euro():
    print("Conversion of Pound to Euro:")
#shows user selected choice
    while True:
        try:
            choice2 = float(input("Enter amount: £"))
#input amount to convert
        except ValueError:
            print("***************Error*****************")
            euro()
#if input isn't a number runs prog again
        else:
            choice2a = "{:.2f}".format(int(choice2) * 1.16)
#answer = 2 decimal places
            print("€" + str(choice2a))
#displays answer
            print("----------------Next-----------------")
            afterc()
#runs next choice prog

def yen():
    print("Conversion of Pound to Yen:")
#shows user choice
    while True:
        try:
            choice3 = float(input("Enter amount: £"))
#user inputs amount
        except ValueError:
            print("***************Error*****************")
            yen()
#if input isn't a number runs prog again
        else:
            choice3a = "{:.2f}".format(int(choice3) * 138.90)
#answer = 2 decimal places
            print("¥" + str(choice3a))
#displays answer
            print("----------------Next-----------------")
            afterc()
#runs next choice


def afterc():
#after currency program
    print("""Next move:
    1. Currency Conversion
    2. Main Menu""")
#displays choices
    move1 = str(input("Choice: "))
#user input
    if move1 == "1":
        currency ()
#runs currency prog
    elif move1 == "2":
        main()
#runs main prog
    else:
        print("***************Error*****************")
        afterc()
        
def currency():
    print("--------------Currency Converter---------------")
    print("""Convert Pounds to:
    1. Dollars
    2. Euros
    3. Yen""")
    conversion = str(input("Choice: "))
    if conversion == "1":
#input = 1 (dollar)
        dollar()
#run dollar converter
    elif conversion == "2":
#input = 2 (euro)
        euro()
#run euro converter
    elif conversion == "3":
# input = 3 (yen)
        yen()
#run yen converter
    else:
        print("***************Error*****************")
        currency()
        
        print("----------------Next-----------------")
        afterc()
#runs next choice prog
        
def aftert():
#after temperature program
    print("""Next move:
    1. Temperature Conversion
    2. Main Menu""")
#displays choices
    move2 = str(input("Choice: "))
#user input
    if move2 == "1":
        temperature()
#runs temperature prog
    elif move2 == "2":
        main()
#runs main prog
    else:
        print("***************Error*****************")
        afterc()

def temperature():
    print("-------------Temperature Converter--------------")
    print("Conversion from Celsius to Fahrenheit")
#shows user choice
    while True:
        try:
            num = float(input("Enter Celsius: "))
#user inputs
        except ValueError:
            print("***************Error*****************")
            temperature()
#if input isn't number runs prog again
        else:  
            num1 = (int(num) * 9)
            num2 = (int(num1) / 5)
            num3 = (int(num2) + 35)
#converts into fahrenheit
            print(str(num3), ("°F"))
#displays answer
            print("----------------Next-----------------")
            aftert()
#runs next choice prog

def main():
    print("-----------------Converter----------------------")
    print("""Would you like to convert:
    1. Currency
    2. Temperature
    3. or Exit""")
    answer = str(input("Choice: "))
    if answer == "1":
        currency()
#runs currency converter
    elif answer == "2":
        temperature()
#runs temperature converter
    elif answer == "3":
        print("-----------------Exit-----------------------")
        os._exit(99)
    else:
        print(("***************Error*****************"))
        main()

main()
            
