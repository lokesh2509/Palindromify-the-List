"""
The task you have to perform is “Palindromify the List.” This task consists of a total of 10 points to evaluate your performance.

Problem Statement:-
You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is
greater than 10; otherwise, you will print that number.



Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
"""

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