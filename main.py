from scipy.integrate import quad
from numpy import poly1d
from os import system, name


clear = lambda: system("clear") if name == "posix" else system("cls")


borders = [int(input("Enter lower border: ")), int(input("Enter upper border: "))]

a = float(input("Factor of x^5 = "))
b = float(input("Factor of x^4 = "))
c = float(input("Factor of x^3 = "))
d = float(input("Factor of x^2 = "))
e = float(input("Factor of x^1 = "))
f = float(input("Factor of x^0 = "))

func = poly1d([a, b, c, d, e, f])

def function(x):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f


i = quad(function, borders[0], borders[1])


def main():
    print(f"Your function: \n{func} \nYour interval: {borders}")
    print(f"The integral value is {round(i[0], 2)}.")


if __name__ == "__main__":
    clear()
    main()
