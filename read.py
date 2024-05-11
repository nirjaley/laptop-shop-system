
def username_phone():
    name = input("Please enter your name: ")
    phone = input("Please enter your phone number: ")       
    return name,phone

def display_file():
    file = open("laptop.txt","r")
    items = file.read()
    return items

def replace():
    file = open("Laptop.txt", "r")
    a = 1
    for line in file:
        print(a, "\t\t" + line.replace("," ,"\t\t"))
        a = a + 1
    file.close