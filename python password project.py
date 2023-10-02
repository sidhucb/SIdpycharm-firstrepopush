from cryptography.fernet import Fernet

var = ('def write_key():\n'
       '  key=Fernet.generate_key()\n'
       '  with open(\'key.key\',\'wb\') as key_file:\n'
       '    key_file.write(key)')
def load_key():
  file=open('key.key','rb')
  key: bytes=file.read()
  file.close()
  return key
master_pwd=input("What is your master password? : ")
key=load_key() + master_pwd.encode()
fer=Fernet(key)
def view():
  with open("passwords.txt", "r") as f:
    for j in f.readlines():
      data=j.strip()
      ukr,pikr=data.split('|')
      print(f'Account Name : {ukr}  Password : {fer.decrypt(pikr.encode()).decode()}')
def add():
  name=input("Account name : ")
  pwd=input("Password : ")
  with open("passwords.txt","a") as f:
    f.write(name + "|" +fer.encrypt(pwd.encode()).decode() +"\n")
while True:
  mode=input("Would you like to add a new password or view existing ones? (view, add,or q for quit) : ").lower()
  if mode=='q':
    break
  if mode=='view':
    view()
    quit()
  elif mode=='add':
    add()
    quit()
  else:
    print('Invalid mode')
    continue
