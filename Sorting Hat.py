
print("""Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
    """)

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

answer = int(input("Options 1-2  "))
if answer == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

print("""Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

    """)

answer = int(input("Options 1- 4   "))
if answer == 1:
    Hufflepuff += 2
elif answer == 2:
    Slytherin += 2
elif answer == 3:
    Ravenclaw += 2
elif answer == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

print("""
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
""")

answer = int(input("Options 1- 4   "))
if answer == 1:
    Slytherin += 4
elif answer == 2:
    Hufflepuff += 4
elif answer == 3:
    Ravenclaw += 4
elif answer == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

print("🦁Gryffindor points {}".format(Gryffindor))
print("🦅Ravenclaw points  {}".format(Ravenclaw))
print("🦡Hufflepuff points {}".format(Hufflepuff))
print("🐍Slytherin points {}".format(Slytherin))

print("=="*40)

most_points = max(Gryffindor, Hufflepuff, Slytherin, Ravenclaw)

if Gryffindor == most_points:
    print("🦁Gryffindor House Wins")
elif Hufflepuff == most_points:
    print("🦡Hufflepuff House Wins")
elif Slytherin == most_points:
    print("🐍Slytherin House Wins")
else:
    print("🦅RavenClaw House Wins")
