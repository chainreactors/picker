---
title: A Detailed Guide on Kerbrute
url: https://www.hackingarticles.in/a-detailed-guide-on-kerbrute/
source: Hacking Articles
date: 2023-01-09
fetch_date: 2025-10-04T03:20:32.540416
---

# A Detailed Guide on Kerbrute

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
»* [A Detailed Guide on Kerbrute](https://www.hackingarticles.in/a-detailed-guide-on-kerbrute/)
»

[Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# A Detailed Guide on Kerbrute

[January 8, 2023May 16, 2025](https://www.hackingarticles.in/a-detailed-guide-on-kerbrute/) by [Raj](https://www.hackingarticles.in/author/raj/)

Kerbrute is a tool used to enumerate valid Active directory user accounts that use Kerberos pre-authentication. Also, this tool can be used for password attacks such as password bruteforce, username enumeration, password spray etc. This tool is being used for many years by penetration testers during internal penetration testing engagements. This tool is originally written by Ronnie Flathers (ropnop) with contributor Alex Flores.

### Table of Content

* **Introduction to Kerberos Authentication**
* **Download Kerbrute**
* **Kerbrute help – List available features**
* **Find valid users / User enumeration**
* **Kerbrute Password Spray**
* **Password Bruteforce**
* **Bruteforce username:password combos**
* **Saving Output**
* **Verbose mode**
* **Mitigation**
* **Conclusion**

### Introduction to Kerberos Authentication

The Kerberos service runs on its default port which is 88 in a domain controller system. This service comes in windows and the Linux system as well where it is used to implement authentication processes more securely in an Active Directory environment. For more information about Kerberos authentication process and service principal name (SPN) please consider visiting the below link:

**<https://www.hackingarticles.in/deep-dive-into-kerberoasting-attack/>**

### Download Kerbrute

Kerbrute can be downloaded from its official github repository release page. It was last modified in December 2019. The source code of the tool is also available, and it is also available for windows systems and other Linux architecture. For simplicity, we will download compiled **kerbrute\_linux\_amd64** for the kali Linux which will be going to be an attacking system for the demonstration. The tool can be downloaded from the link given below.

Download link:

**<https://github.com/ropnop/kerbrute/releases/tag/v1.0.3>**

### ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJoZSkfpQlra-lfqgS6RUnYLAhKZircXoSmKuNNcxI4K9aOo4TEbLjDLY5IJ69qSOLPFQVgZQuCgmFD0rDj0x7EsHXuv8QBRrSXcFcSXNqmO6lLTyfD_-XYSWL_86hnW0z_Sing_YI9k3rpCXqjCJVZZ0GJa8ofEAGKhaf_J87pOIaahWvzgDnpb_naQ/s16000/1.png)

### Kerbrute help – List available features

Once we download the tool in the kali machine, we can list the available options and features by executing the following command:

```
./kerbrute_linux_amd64
```

In the picture below, we can see that tools can perform various tasks such as bruteforce, bruteuser, password spray, userenum and version detection. Moreover, there are some flags available too which can be very handy during penetration testing.  During the internal assessment, many times we encounter security features and the password policy so increasing and decreasing threads can help us to make password attacks stealthier. We highly recommend using all available flags come with kerbrute to get practical experience and analyse the results.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgor0nJy66lHYOaBBmIDHhssfVxQ9IJtdE5t78k0RDouL1UCtUIe5bJzAjrghuBqnr6EHl5hCwNnGvUdkrWRS1KcCLo6COnh9jtaq8_BkSX-6a4fKQPC5Uk_IMSyO1cHzJCD1BH3Xwf1b2OJmiFAUs3X9G-H15_1ZAZEPaalz08zGDMq8Zspg9H72pQTw/s16000/2.png)

### Find valid users / User enumeration

During the internal penetration testing engagements especially in the Active Directory environment, our initial goal is to find valid users. Once we find potential users from the company website or any other sort of misconfiguration then we can verify those users if they have valid accounts or not using kerbrute.  To do that, we will make a list of potential users that we obtained from OSINT or any other way. For the demonstration, we have created a user’s list and saved it as users.txt.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2xONhKJhsjlnKrrdpe9uSkgvaqDGpgqhSnqLxJr7JgIJsmm5RqqSmvA2QfOp4WSiaTmrlHEL-Ce56Acxhc-biMRjHjh4UWQTqMZtZBjJ6_Iidc53OhWWDJjTXC5KuqZCYDn-hZ1vlNKq97QB-7b27-h2Wzi3wyhamASP1ETBlVIHbZc0YLLqQ9hxbZA/s16000/3.png)

Then we provided users list and selected the userenum option. Next, we provided the domain controller IP address and domain name which is **ignite.local** in our case. The tool will test against each user account and verify if those users exist in the domain and using Kerberos pre-authentication.  In the picture below we can see that kapil, aarti, shreya, raj and pawan appeared as valid users using Kerberos authentication. Here we in the position where we can think about various Kerberos attack such as SPN and Kerberos bruteforce etc. To reproduce the proof of concept, feel free to use the below command.

```
./kerbrute_linux_amd64 userenum --dc 192.168.1.19 -d ignite.local users.txt
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWIeARP6j9o46YNN1siF9A_lpyfcw1RTrNp2tiVBlxgPM68QpWa1wag2eQkAuUBZ7HjWwptspLbeMaRJ7vwkygwU4sAYRv8NPXovgQMOhuoXOcnByVrSUp85uM2k_a4YZSgE-xn_q8KtXOPRL7jGrZ6ZVSsGEzkobKFLYf3X9ey0cu43ceeHLAoRlMVg/s16000/4.png)

### Kerbrute Password Spray

Suppose we have obtained a password (**Password@1**) during the enumeration phase that can be anything such as OSNIT leaked password, service misconfiguration, smb share, ftp etc but we do not know the real owner of the obtained password. In the username enumeration phase, we found five valid users now we can test obtained passwords with their accounts. Password spray is like password bruteforce where we test each password against single users but in the password spray, we use a single password and test it against all valid accounts.

To do that, we created a new users list and saved it as ...