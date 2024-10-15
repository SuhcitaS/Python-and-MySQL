from db_operations import create_table, creat_user, get_users, update_user, delete_user

def menu():
    print("===Usre Management System===")
    print("1. Create usre")
    print("2. View Usres")
    print("3. Update Usre")
    print("4. Delete Usre")
    print("5. Exit")

create_table() # Ensure the table exists

while True:
    menu()
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            name = input('Enter name: ')
            email = input("Enter email: ")
            creat_user(name, email)

        case '2':
            print("Usre List: ")
            get_users()

        case '3':
            user_id = int(input("Enter usre ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            update_user(user_id, new_name, new_email)

        case '4':
            user_id = int(input("Enter user ID to Delete: "))
            delete_user(user_id)

        case '5':
            print("Project Terminated ")
            break

        case _:
            print("INVALID choice. Please try again.")
