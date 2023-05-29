
def add_bonus(x):
    y = x + bonus
    return y


salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input())

res = list(map(add_bonus, salaries))

print(res)
