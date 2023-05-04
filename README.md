# Python-101-For-Hackers

## Disclaimer
Scripts developed with the intension of educational purpose only.

> Learn - Hack - Secure :upside_down_face:	

## Some python projects for ethical hacking and testing from TCM courses

### SSH_Brute_Forcing:

* Prerequisites for the `ssh_brute_forcing`

  * A wordlist to use you can download similar lists from: 

https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

A running SSH service you are authorised to test (such as on your localhost or a VM) is required to test this script.

---
**Note**
    
The default Kali SSH configuration will block authentication attempts after 10 attempts (MaxStartups 10:30:10). If you want to test 100 connections + the valid password using the above wordlist, you will need to edit your sshd_config (for example, by setting MaxStartups 101) and restarting the service. Alternatively to test, use a wordlist with less than 10 invalid passwords, or incrase the delay between each attempt.

---

### SHA256_Password_Cracking


* Prerequisites for the `SHA256_password_cracking`

    * Wordlist like `rockyou.txt`

---
**NOTE**

Create sha256sum for a word: `echo -ne <the_word> | sha256sum`

---



### Web-Login Brute forcing

* Prerequisites for the `Web-Login Brute forcing`

    * Install Docker 
    ```
        #!/bin/bash

        # Update package database
        sudo apt-get update

        # Install Docker dependencies
        sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y

        # Add Docker's official GPG key
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

        # Add Docker repository to system's software sources
        echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

        # Update package database again
        sudo apt-get update

        # Install Docker
        sudo apt-get install docker-ce docker-ce-cli containerd.io -y
    ```
    * Build the docker image in the `Docker_Web_Aapp` folder: `docker build -t web-login .`
    * Run the docker container: `docker run --rm -d -p 5000:5000 web-login`

    * Register test users at ` http://127.0.0.1:5000/register`

### SQL injection

For example, you can test out your knowledge for free, by solving the “The Flag API Key” challenge hosted at https://247CTF.com in the Web category.

Binary search algorithm in nutshell:

Assuming we have a sorted array of numbers `0123456789abcdef`  and we want to find a particular value.

* Queries are limited to 128 queris per api key.

* 32 `character` MD5 password

* 16 `options` per character

* 128/32 =4 request per `charachter`

We know the minimum and the maximum values (0 and f)

Instead of guessing the unknown value, compate with the middle

* If less, compare again with a new minimum and maximum from left

* If more, compare again, with a new minimum and maximum rom the right


* Binary search example for number `6`:

  | Query #  | Charset          | Question| Result |  
  |----------|------------------|---------|--------|  
  |   1      |0123456`7`89abcdef|   >7?   | False  |  
  |   2      |012`3`4567        |   >3?   | True   |  
  |   3      |34`5`67           |   >5?   | True   |  
  |   4      |5`6`7             |   >6?   | False  |  



