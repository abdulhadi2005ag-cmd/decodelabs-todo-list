total=0
print("your expense tracker:")
while True:
    entry=input("enter your expense or quit for ending:")
    if entry=="quit":
        break
    try:
        expense=int(entry)
    except ValueError:
        print("invalid input, enter number")
        continue
    total+=expense

print("total:",total)

