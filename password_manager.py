from cryptography.fernet import Fernet
import os


def write_key():
    key= Fernet.generate_key()
    with open ("key.key","wb") as f:
        f.write(key)

def load_key():
    file= open("key.key","rb")
    key=file.read()
    file.close()
    return key

key=load_key()
fer =Fernet(key)

master_pwd = input('What is the master password?')





def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            try:
                user, passw = line.strip().split("|")
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
            except Exception as e:
                print(f"Skipping invalid line: {line.strip()}")

def add():
    name=input('Account Name:')
    pwd=input('Account Password:')

    with open('passwords.txt','a') as f:
        f.write(name+'|'+ fer.encrypt(pwd.encode()).decode() + "\n")

while True:
  mode = input("Would you like to add a new password or view existing ones(view,add),press q to quit?").lower()
  if mode=='q':
    break

  if mode == 'view':
    view()
  elif mode=="add":
    add()
  else:
    print('Invalid mode.')
    continue