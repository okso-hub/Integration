from scipy.integrate import quad
from os import system, name


clear = lambda: system("clear") if name == "posix" else system("cls")


borders = [int(input("Enter lower border: ")), int(input("Enter upper border: "))]

a = float(input("Factor of x^5 = "))
b = float(input("Factor of x^4 = "))
c = float(input("Factor of x^3 = "))
d = float(input("Factor of x^2 = "))
e = float(input("Factor of x^1 = "))
f = float(input("Factor of x^0 = "))


def function(x):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f


i = quad(function, borders[0], borders[1])


def main():
    print(i[0])


if __name__ == "__main__":
    main()
