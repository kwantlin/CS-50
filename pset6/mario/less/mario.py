from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break
for r in range(n):
    for c in range(n-r-1):
        print(" ", end = "")
    for c in range(r+1):
        print("#", end = "")
    print("\n", end = "")

