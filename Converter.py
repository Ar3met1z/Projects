

def m_to_km(n):
    a = (1.609 * n)
    print(f"{a} Kilometers")
def km_to_m(n):
    a = (n / 1.609)
    print(f"{a} Miles")
def lbs_to_kg(n):
    a = (n / 2.205)
    print(f"{a} Kilograms")
def kg_to_lbs(n):
    a = (2.205 * n)
    print(f"{a} Pounds")
def in_to_cm(n):
    a = (2.54 * n)
    print(f"{a} Centimeters")
def cm_to_in(n):
    a = (n / 2.54)
    print(f"{a} Inches")

print("""
    Units:
        Miles       ---> Kilometers  [a]
        Kilometers  ---> Miles       [b]
        Pounds      ---> Kilograms   [c]
        Kilograms   ---> Pounds      [d]
        Inches      ---> Centimeters [e]
        Centimeters ---> Inches      [f]
    Commands:
        Quit                         [q]
""")


qui = False

while qui != True:
    unit = input("Enter the Units you would like to convert: ")
    number = float(input("Enter the number you would like to convert: "))
    if unit.upper() == "A":
        print(m_to_km(number))
    elif unit.upper() == "B":
        print(km_to_m(number))
    elif unit.upper() == "C":
        print(lbs_to_kg(number))
    elif unit.upper() == "D":
        print(kg_to_lbs(number))
    elif unit.upper() == "E":
        print(in_to_cm(number))
    elif unit.upper() == "F":
        print(cm_to_in(number))
    elif unit.upper() == "Q":
        qui = True
    else:
        print("Not A Valid Unit")
