# Python-101-For-Hackers

## Disclaimer
Scripts developed with the intension of educational purpose only.
  
> Learn - Hack - Secure :upside_down_face:	

## Some python projects for ethical hacking and testing from TCM courses


* Prerequisites for the `ssh_brute_forcing`

- A wordlist to use you can download similar lists from: 

https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

A running SSH service you are authorised to test (such as on your localhost or a VM) is required to test this script.

---
**Note**
    
The default Kali SSH configuration will block authentication attempts after 10 attempts (MaxStartups 10:30:10). If you want to test 100 connections + the valid password using the above wordlist, you will need to edit your sshd_config (for example, by setting MaxStartups 101) and restarting the service. Alternatively to test, use a wordlist with less than 10 invalid passwords, or incrase the delay between each attempt.

---

* Prerequisites for the `SHA256_password_cracking`

- Wordlist like `rockyou.txt`

---
**NOTE**

Create sha256sum for a word: `echo -ne <the_word> | sha256sum`

---