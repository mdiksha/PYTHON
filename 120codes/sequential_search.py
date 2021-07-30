def sequential_search(list_, n):
    found = False
    print("Number not present")
    for i in list_:
        if i == n:
            print("Number is present")
            found=True
            break
    return found

numbers = list(range(0, 50))
print(sequential_search(numbers, 100))
