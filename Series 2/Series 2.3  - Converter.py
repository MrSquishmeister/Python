def temp():
    print("""Choices:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsis""")
    tc = input("Enter: ")
    if tc == "1":
        print("Converts Celsius to Fahrenheit")
        c = int(input("Enter Celsius: "))
        c1 = (c*9)
        c2 = (c1/5)
        c3 = (c2 + 32)
        print((c3), ("°F"))
    elif tc == "2":
        print("Converts Fahrenheit to Celsius")
        f = int(input("Enter Fahrenheit: "))
        f1 = (f - 32)
        f2 = (f1 * 5)
        f3 = (f2 / 9)
        print((f3), ("°C"))
    else:
        print("Try Again.")
        temp()
    aftert()

def aftert():
    print("--------------------------------------")
    print("""Choices:
1. Run Temperature Again
2. Different Conversion""")
    atc = int(input("Enter: "))
    if atc == 1:
        temp()
    elif atc == 2:
        main()
    else:
        print("Try Again.")
        aftert()

def currency():
    print("----------Currency Converter----------")
    print("""Convert Pound to:
1. Dollar
2. Euro
3. Yen""")
    print("--------------------------------------")
    cc = input("Enter: ")
    if cc == "1":
        print("Conversion Of Pound To Dollar:")
        pound1 = int(input("£"))
        dollar = (pound1 * 1.25)
        print(("$"), (dollar))
    elif cc == "2":
        print("Conversion Of Pound To Euro:")
        pound2 = int(input("£"))
        euro = (pound2 * 1.17)
        print(("€"), (euro))
    elif cc == "3":
        print("Conversion Of Pound To Yen:")
        pound3 = int(input("£"))
        yen = (pound3 * 140.39)
        print(("¥"), (yen))
    else:
        print("Try Again.")
        currency()
    afterc()

def afterc():
    print("--------------------------------------")
    print("""Choices:
1. Run Currency Again
2. Different Conversion""")
    acc = int(input("Enter: "))
    if acc == 1:
        currency()
    elif acc == 2:
        main()
    else:
        print("Try Again.")
        aftercc()
        
def volume():
    print("----------Volume Converter----------")
    print("""Convert:
1. Litre To Millilitre
2. Millilitre To Litre""")
    print("--------------------------------------")
    vc = input("Enter: ")
    if vc == "1":
        print("Conversion Of Litre To Millilitre")
        l1 = int(input("Litre: "))
        ml1 = (l1 * 1000)
        print(("Millilitre: "), (ml1))
    elif vc == "2":
        print("Conversion Of Millilitre To Litre")
        ml2 = int(input("Millilitre: "))
        l2 = (ml2 / 1000)
        print(("Litre: "), (l2))
    else:
        print("Try Again.")
        volume()
    afterv()

def afterv():
    print("--------------------------------------")
    print("""Choices:
1. Run Volume Again
2. Different Conversion""")
    avc = int(input("Enter: "))
    if avc == 1:
        volume()
    elif avc == 2:
        main()
    else:
        print("Try Again.")
        aftervc()
        
def mass():
    print("----------Mass Converter----------")
    print("""Convert:
1. Kilogram To Gram
2. Gram To Kilogram
3. Stone To Pound
4. Pound To Stone""")
    print("--------------------------------------")
    mc = input("Enter: ")
    if mc == "1":
        print("Conversion Of Kilogram To Gram")
        k1 = int(input("Kilogram: "))
        g1 = (k1 *1000)
        print(("Gram: "), (g1))
    elif mc == "2":
        print("Conversion Of Gram To Kilogram")
        g2 = int(input("Gram: "))
        k2 = (g2 / 1000)
        print(("Kilogram: "), (k2))
    elif mc == "3":
        print("Conversion Of Stone To Pound")
        s1 = int(input("Stone: "))
        p1 = (s1 * 14)
        print(("Pound: "), (p1))
    elif mc == "4":
        print("Conversion Of Pound To Stone")
        p2 = int(input("Pound: "))
        s2 = (p2 / 14)
        print(("Stone: "), (s2))
    else:
        print("Try Again.")
        mass()
    afterm()

def afterm():
    print("--------------------------------------")
    print("""Choices:
1. Run Mass Again
2. Different Conversion""")
    amc = int(input("Enter: "))
    if amc == 1:
        mass()
    elif amc == 2:
        main()
    else:
        print("Try Again.")
        aftermc()

def main():
    print("---------------Converter----------")
    print("""Units:
1. Temperature
2. Currency
3. Volume
4. Mass""")
    uc = int(input("Enter: "))
    if uc == 1:
        temp()
    elif uc == 2:
        currency()
    elif uc == 3:
        volume()
    elif uc == 4:
        mass()
    else:
        print("Try Again.")
        main()
        
main()
    
        
        
    
