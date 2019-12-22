from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars >0:
        break

# convert to cents for accuracy
cents = round(dollars * 100);

# count number of coins in change
coins = 0;

# add quarters
while cents >= 25:
    coins += 1
    cents -= 25

# add dimes
while cents >= 10:
    coins += 1
    cents -= 10

# add nickels
while cents >= 5:
    coins += 1
    cents -= 5

# add pennies
while cents >= 1:
    coins += 1
    cents -= 1

# print number of coins
print(coins)

