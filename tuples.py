contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
contactName = input()

for x in contacts:
    if contactName in x:
        print("{} is {}".format(x[0], x[1]))
        break
else:
    print("Not Found")
