# brute_forcer.py
def brute_force_login(username, password_list, correct_password):
    print(f"🔐 Brute-forcing password for user '{username}'...\n")
    for password in password_list:
        if password == correct_password:
            print(f"✅ Password found: {password}")
            return True
        else:
            print(f"❌ Tried: {password}")
    print("❗ Password not found.")
    return False
