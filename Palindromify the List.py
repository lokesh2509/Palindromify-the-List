lst = input("Enter the list of numbers:- "). split( )
for i in range(len(lst)):
    while True:
        if lst[i] == lst[i][::-1]:
            break
        else:
            lst[i] = int(lst[i])
            lst[i] = lst[i] + 1
            lst[i] = str(lst[i])
            continue

print(lst)
