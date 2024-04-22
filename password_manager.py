# password manager

from cryptography.fernet import Fernet

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt

'''
# funtion to create the key.key file using fernet from cryptography lib
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) # write in the key that was generated in "key"
# create and open file key.key in wb mode (write in bytes)

write_key() # call the function to generate the key.key file with the encryption key
'''


def load_key():
    file = open("key.key", "rb") # 'rb' - reading bytes
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode() # key in bytes. convert 'master_pws' into bytes
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split()
            print("User:", user, + "Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + " " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input ("Would you like to view an existing password or add a new one?(v/a) or quit(q)? ")

    if mode == "v":
        view()
    elif mode == "a":
        add()
    elif mode == "q":
        quit()
    else:
        print("Invalid option.")
        continue
