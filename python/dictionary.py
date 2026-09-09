# Key value pair
# no index
# no duplicat keys allowed
# ordered
# mutable  

# d={}
# d={'name' : 'Manu','class' : 2 , 'age' : 22}
# print(d)

# d['name']= 'sony'   change the name if any or add the new key 
# print(d)

# print(d['name'])       # print name
# print(d.get('name'))

# d.pop('age')    #remove age
# print(d)

# d.popitem()
# print(d)      #delete last key

# print(d.keys())    #to get keys
# print(d.values())  # to get values

# d.clear()
# d.copy()
# d.update({'name' : 'sangeeth'})
# print(d)

'''practice question'''
# dictionary questions:                                                               Create a dictionary to store a student's name, age, and grade.
# Print all the keys in a dictionary.
# Print all the values in a dictionary.
# Access the value of a given key.
# Add a new key-value pair to a dictionary.
# Update the value of an existing key.
# Remove a key using pop().
# Remove the last inserted item using popitem().
# Delete a key using del.
# Check if a key exists in a dictionary


# Create a menu-driven student management system using dictionaries.

# Features:

# Add student
# Update marks
# Delete student
# Search student
# Display topper


# std={}
# std={'name' : 'Manu','class' : 2 , 'age' : 22,'mark' : 78}
# print(std)

# std.update({'mark' : 89})
# print(std)

# st={'name' : 'sonu','class' : 2 , 'age' : 22,'mark' : 78}
# print(st)

# del st
# print()

# sr=input("enter value to search : ")
# if sr in std:
#     print("found",sr)
# else:
#     print("not found",sr)



# Create a mini banking system.

# Features:

# Create account
# Deposit
# Withdraw
# Check balance
# Transfer money

bank = {}

while True:
    print("\n----- MINI BANKING SYSTEM -----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Create account
    if choice == 1:
        acc = input("Enter account number: ")
        name = input("Enter name: ")
        balance = int(input("Enter initial deposit: "))

        bank[acc] = {
            "name": name,
            "balance": balance
        }

        print("Account created successfully!")

    # Deposit
    elif choice == 2:
        acc = input("Enter account number: ")
        amount = int(input("Enter deposit amount: "))

        if acc in bank:
            bank[acc]["balance"] += amount
            print("Amount deposited successfully!")
        else:
            print("Account not found!")

    # Withdraw
    elif choice == 3:
        acc = input("Enter account number: ")
        amount = int(input("Enter withdrawal amount: "))

        if acc in bank:
            if amount <= bank[acc]["balance"]:
                bank[acc]["balance"] -= amount
                print("Amount withdrawn successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    # Check balance
    elif choice == 4:
        acc = input("Enter account number: ")

        if acc in bank:
            print("Name:", bank[acc]["name"])
            print("Balance:", bank[acc]["balance"])
        else:
            print("Account not found!")

    # Transfer money
    elif choice == 5:
        sender = input("Enter your account number: ")
        receiver = input("Enter receiver account number: ")
        amount = int(input("Enter amount to transfer: "))

        if sender in bank and receiver in bank:
            if amount <= bank[sender]["balance"]:
                bank[sender]["balance"] -= amount
                bank[receiver]["balance"] += amount
                print("Money transferred successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("One or both accounts not found!")

    # Exit
    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")