print("This is a program written by Elijah to convert between Fahrenheit and Celsius")
print(" ")

def celsiusfunc():
    print("What is value in Celsius?")
    print(" ")
    initialc = float(input(">"))
    def c_to_f(initialc):
        f_temp = float(initialc) * (9/5) + 32
        return f_temp
    print(" ")
    print("Value in Fahrenheit is " + str(c_to_f(initialc)))
    print(" ")
    
def fahrenheitfunc():
    print("What is value in Fahrenheit?")
    print(" ")
    initialf = float(input(">"))
    def f_to_c(initialf):
        c_temp = (float(initialf)-32) * (5/9)
        return c_temp
    print(" ")
    print("Value in Celsius is " + str(f_to_c(initialf)))
    print(" ")

x = 1
while True:
    print("Is temperature in Fahrenheit or Celsius? (answer with 'f' or 'c'). If you wish to end this program, type 'end'.")
    print(" ")
    f_or_c = input("\n> ").lower()
    print(" ")
    if f_or_c == "c":
        celsiusfunc()
    if f_or_c == "f":
        fahrenheitfunc()
    if f_or_c == "end":
        break
    if f_or_c != "f" or "c":
        print("\nPlease input a value of 'f' or 'c'.")
        print(" ")
