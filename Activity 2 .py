def book():
    book = {}
    l = int(input("Enter how many contacts: "))

    for x in range (1, l+1):
        name = input("Enter your name: ")
        num = int(input("Enter your number: "))
        book[name] = num

    

    search= input("Find: ")
    if search in book:
        print(f"\nNumber: {book[search]}")
    else:
        print("Not found")
        
    print(f"Address book:{book}")

book()