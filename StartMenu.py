
admin = {'Admin': "Admin"}
users = {}


def login():
    print("LOGIN")
    user_user = input("Enter Username:")
    user_pass: str = input("Enter Password:")

    if user_user in admin and admin[user_user] == admin[user_user]:
        print("Login Successful.")
        import Admin
        Admin.admin_menu()
    else:
        print("username or password is incorrect.")


login()