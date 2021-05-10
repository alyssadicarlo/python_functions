print("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
""")

running = True
phonebook = {
    "Alyssa": {
        "phone_number": "123-456-7890"
    },
    "Jessica": {
        "phone_number": "456-678-9963"
    }
}

def lookup(name):
    names_found = []
    if name in phonebook:
        names_found.append(name)
        print("Found entry for %s: %s" % (name, phonebook[name]["phone_number"]))
    if names_found == []:
        print("No entries found.")
        
    
def add(name, phone_number):
    phonebook[name] = {
        "phone_number": phone_number
    }
    print("Entry stored for %s." % (name))

def delete(name):
    if name in phonebook:
        del phonebook[name]
        print("Deleted entry for %s." % (name))
    else:
        print("%s not found." % (name))
    
def print_all():
    if phonebook == {}:
        print("No entries found.")
    else:
        for entry in phonebook:
            print("Found entry for %s: %s" % (entry, phonebook[entry]["phone_number"]))

# Main loop

while running == True:
    
    # Handlie invalid input
    try:
        user_input = int(input("What do you want to do (1-5)? "))
    except:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    # Look up entry in phonebook
    if user_input == 1:
        name = input("Name: ")
        lookup(name)
    
    # Add entry to phonebook
    elif user_input == 2:
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        add(name, phone_number)
    
    # Delete an entry from phonebook
    elif user_input == 3:
        name = input("Name: ")
        delete(name)
    
    # List all entries
    elif user_input == 4:
        print_all()
        
    # Quit
    elif user_input == 5:
        running = False
        
    # Handle invalid input
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
