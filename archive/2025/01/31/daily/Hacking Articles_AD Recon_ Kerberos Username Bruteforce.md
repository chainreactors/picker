---
title: AD Recon: Kerberos Username Bruteforce
url: https://www.hackingarticles.in/ad-recon-kerberos-username-bruteforce/
source: Hacking Articles
date: 2025-01-31
fetch_date: 2025-10-06T20:07:23.096957
---

# AD Recon: Kerberos Username Bruteforce

[Skip to content](#content)

Hacking Articles

## Recent Posts

* [AWS: IAM CreateLoginProfile Abuse](https://www.hackingarticles.in/aws-iam-createloginprofile-abuse/)
* [Privacy Protection: Encrypted DNS](https://www.hackingarticles.in/privacy-protection-encrypted-dns/)
* [Privacy Protection: Windows Privacy](https://www.hackingarticles.in/privacy-protection-windows-privacy/)
* [Privacy Protection: Browsers](https://www.hackingarticles.in/privacy-protection-browsers/)
* [Privacy Protection: Password Manager](https://www.hackingarticles.in/privacy-protection-password-manager/)

## Most Used Categories

* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/) (504)
  + [VulnHub](https://www.hackingarticles.in/category/ctf-challenges/vulnhub/) (311)
  + [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/) (164)
* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/) (408)
* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/) (126)
* [Website Hacking](https://www.hackingarticles.in/category/website-hacking/) (64)
* [Cyber Forensics](https://www.hackingarticles.in/category/cyber-forensics-tricks/) (68)
* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/) (59)
* [Hacking Tools](https://www.hackingarticles.in/category/collection-of-hacking-tools/) (33)
* [Pentest Lab Setup](https://www.hackingarticles.in/category/pentest-lab-setup/) (29)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Search for:

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/)
»* [AD Recon: Kerberos Username Bruteforce](https://www.hackingarticles.in/ad-recon-kerberos-username-bruteforce/)
»

[Domain Enumeration](https://www.hackingarticles.in/category/red-teaming/domain-enumeration/), [Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# AD Recon: Kerberos Username Bruteforce

[January 30, 2025May 23, 2025](https://www.hackingarticles.in/ad-recon-kerberos-username-bruteforce/) by [Raj](https://www.hackingarticles.in/author/raj/)

In this post, we explore the exploitation technique known as the **Kerberos Username Bruteforce** or **Kerberos pre-authentication brute-force attack**. This attack takes advantage of Kerberos authentication responses to determine valid usernames and perform password bruteforcing.

The post outlines exploitation methods, and mitigation techniques, mapped to the MITRE ATT&CK framework for clarity. Detection mechanisms and actionable recommendations are also provided to help security professionals identify and defend against this prevalent threat.

### Table of Contents

* Kerberos Authentication
* Pre-auth Bruteforce
* Metasploit
* Nmap
* Kerbrute
* Rubeus

Detection & Mitigation

### Kerberos Authentication

Kerberos is a widely used authentication protocol in Active Directory (AD) environments. It enables secure authentication using tickets instead of transmitting passwords in plaintext. The protocol consists of three key components:

**Key Distribution Center (KDC)** – Located on the Domain Controller (DC), responsible for issuing tickets.

**Authentication Server (AS)** – Handles initial authentication requests.

**Ticket Granting Server (TGS)** – Issues service tickets for access to specific resources.

The authentication process follows these steps:

1. A user requests authentication from the AS by sending an encrypted timestamp with their password.
2. If valid, the AS returns a **Ticket Granting Ticket (TGT)**.
3. The user presents the TGT to the TGS when accessing resources.
4. The TGS issues a **Service Ticket**, allowing access to the requested service.

Despite its security features, Kerberos can be exploited using brute-force techniques to obtain credentials and access sensitive information.

### Pre-auth Bruteforce

Brute-forcing Kerberos is possible due to distinct server responses during authentication attempts. Attackers exploit these responses to enumerate valid usernames and crack passwords. Since Kerberos operates on **port 88**, attackers specifically target this port when performing brute-force attacks.

**Username Enumeration via AS-REQ Responses**

When a TGT request is made via an **AS-REQ message**, the Kerberos server responds in different ways:

* **Invalid Username:** The server returns **KRB5KDC\_ERR\_C\_PRINCIPAL\_UNKNOWN**, indicating that the username does not exist.
* **Valid Username without Pre-Authentication:** The server may issue a TGT immediately in a AS-REP response, leading to [AS-REP Roasting](https://www.hackingarticles.in/as-rep-roasting/)
* **Valid Username with Pre-Authentication Required:** The server returns **KRB5KDC\_ERR\_PREAUTH\_REQUIRED**, indicating that the client must provide additional authentication data.

Brute-force techniques like **Kerberos Username Bruteforce** are especially dangerous in environments with misconfigured or weak security settings, enabling attackers to systematically identify valid usernames and gain unauthorized access.

### Metasploit

The auxiliary/scanner/kerberos/kerberos\_login module can verify Kerberos credentials against a range of machines and report successful logins.

This module can identify the following information from the KDC:

* Valid/Invalid accounts
* Locked/Disabled accounts
* Accounts with expired passwords, when the password matches
* AS-REP Roastable accounts

**USER\_FILE** option is used to specify the file containing a list of user names to query the Domain Controller to identify if they exist in the target domain or not.

```
use auxiliary/scanner/kerberos/kerberos_login
set rhosts 192.168.1.48
set domain ignite.local
set user_file users.txt
run
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOLsYcrIfjx573KqKwXwqF-QALQz_367Sxj_5iNIw_dBmQKFCnp_zkXQrN4RoiDvDI-ALW0AlS2BonP58f3oyLmz_ACI5eC3gYVmER-RvSkNyHjjWDXh2zv9tXQOgXIzN30StSXTe6Nc91OyzRSKZWm-D6MtIcd3x7LD-JYvcLSSLJBIyeHAPkzTRdxEXo/s16000/1.png)

The **gather/kerberos\_enumusers** module uses a custom wordlist to query a single Domain Controller and identify valid domain user accounts.

```
use auxiliary/gather/kerberos_enumusers
set rhosts 192.168.1.48
set domain ignite.local
set user_file users.txt
run
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbZkKlwWazt1E9sJo8aLEaNmk-B5pdXjrL-V0ymEcuUW6XmkJYf_xsIiPu-kVyFTD3KvWsTYXANGfiozbfasEqvCfNfQy69dKLOGPfux9y_K065zkNpwtk0GD41q9QAz3_rrajJDUja0qhrYQ8rJKcas8Yhx9XD8m2b5yQKLASEtjaRJfICOYRhSyH7bh6/s16000/2.png)

### Nmap

Nmap krb5-enum-users script Discovers valid usernames by brute force querying likely usernames against a Kerberos service.

**krb5-enum-users.realm:** this argument is required as it supplies the script with the Kerberos REALM against which to guess the user names.

```
nmap -p 88 --script krb5-enum-users --script-args krb5-enum-users.realm='ignite.local',userdb=users.txt 192.168.1.48
```

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5H6QBCdQfI-370APMWrFNf9ulvVZDXiLQt9btdqy2z64s3T8Bsn9Sm64jWNtDAqY8ax8AtDvgq3X7_tiry2vRbohBOKXblU4TSDBqK4l2WgMmSJdEiC3-1oOx11bb7vSf2p1ArQD-F7WIlTsFDbBm3v5v5kC2dXVEn-ndshsQw9jH3Z4j6c5NPqjUUTO3/s16000/3.png)**

### Kerbrute

**[Kerbrute](https://www.hackingarticles.in/a-detailed-guide-on-kerbrute/)** is a tool used to enumerate valid Active directory user accounts that use Kerberos pre-authentication.

```
./kerbrute_linux_amd64 userenum --dc 192.168.1.48 -d ignite.local users.txt
```

![](https://blog...