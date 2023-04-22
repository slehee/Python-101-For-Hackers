# Python-101-For-Hackers

## Some python projects for ethical hacking and testing from TCM courses


* Prerequisites for the ssh brute forcing

 A wordlist to use you can download similar lists from: 

https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

A running SSH service you are authorised to test (such as on your localhost or a VM) is required to test this script.

---
**Note**
    
    The default Kali SSH configuration will block authentication attempts after 10 attempts (MaxStartups 10:30:10).<br>If you want to test 100 connections + the valid password using the above wordlist, you will need to edit your sshd_config (for example, by setting MaxStartups 101) and restarting the service.<br>Alternatively to test, use a wordlist with less than 10 invalid passwords, or incrase the delay between each attempt.

---