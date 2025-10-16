print("Task 5: Secure System Login Simulator" )

correct_username = "DocBen"
correct_password = "yohoo123"
correct_2fa = "246810"
username = input("Enter username: ")
password = input("Enter password: ")
is_2fa_enabled = input("Is 2FA enabled? (y/n): ").lower() == "y"
code = input("Enter 2FA code: ")
if username == correct_username and password == correct_password and (not is_2fa_enabled or code == correct_2fa):
    print("Login successful")
else:
    print("Login failed")
    