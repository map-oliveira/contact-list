
def add_contact (contact_list, name_contact, phone_number):
    contact = {"contact" : name_contact, "number": phone_number, "favorite" : False }
    contact_list.append (contact)
    print(f"Contact {name_contact} was sucessfully add to your contact list!")
    return 

def list_contact (contact_list): 
    print ("\n Mariana's contact list ")
    for index, contact in enumerate(contact_list, start=1):
        name_contact = contact["contact"]
        phone_number = contact["number"]
        favorite = "★" if contact["favorite"] else " "
        print(f'{index}. [{favorite}] {name_contact} - {phone_number}') 
    return 

def update_contact (contact_list, index_contact, new_contact, new_number):
    index_contact_adjusted = int(index_contact) - 1 
    if index_contact_adjusted >= 0 and index_contact_adjusted < len (contact_list):
        contact_list [index_contact_adjusted] ["contact"] = new_contact 
        contact_list [index_contact_adjusted] ["number"] = new_number 
        return
    else:
        print ('Invalid')

def favorite_contact(contact_list, index_contact):
    if not index_contact.isdigit():
        print("Type a valid number.")
        return

    index = int(index_contact) - 1
    if 0 <= index < len(contact_list):
        contact_list[index]["favorite"] = True
        print("Contact marked as favorite.")
    else:
        print("Invalid index.")

def delete_contact(contact_list, index_contact):
    index = int(index_contact) - 1
    deleted = contact_list.pop(index)
    print("Deleted contact:", deleted["contact"])
    return 

contact_list = []

while True:
    print ("\n  ~ Mariana's contact list ~")
    print ("add contact")
    print ("list contact")
    print ("update contact")
    print ("favorite contact")
    print ("delete contact")
    print ("close contact list")

    selection = input("select a option ")

    if selection == "add contact":
        name_contact = input ("Type name contact ")
        phone_number = input ("Type phone number ")
        add_contact (contact_list, name_contact, phone_number)

    elif selection == "list contact": 
        list_contact(contact_list)
    
    elif selection == "update contact":
        list_contact(contact_list)
        index_contact = input ("Type contact index to update")
        new_name = input ("Type new name ")
        new_number = input ("Type new number ")
        update_contact (contact_list, index_contact, new_name, new_number)
    
    elif selection == "favorite contact":
        list_contact(contact_list)
        index_contact = input ("Type contact to favorite")
        favorite_contact(contact_list, index_contact)
    
    elif selection == "delete contact":
        list_contact(contact_list)
        index_contact = input("Type contact index to delete: ")
        delete_contact(contact_list, index_contact)

    elif selection == "close contact list":
        break 
