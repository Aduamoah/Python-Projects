def calc(x):
    area = x ** 2
    perimeter = 4 * x
    return perimeter, area


side = int(input("What is the length of the square: "))
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))
