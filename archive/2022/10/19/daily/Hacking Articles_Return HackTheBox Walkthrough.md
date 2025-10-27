---
title: Return HackTheBox Walkthrough
url: https://www.hackingarticles.in/return-hackthebox-walkthrough/
source: Hacking Articles
date: 2022-10-19
fetch_date: 2025-10-03T20:12:27.058890
---

# Return HackTheBox Walkthrough

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
»* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/)
»* [Return HackTheBox Walkthrough](https://www.hackingarticles.in/return-hackthebox-walkthrough/)
»

[CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/), [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/)

# Return HackTheBox Walkthrough

[October 18, 2022June 19, 2025](https://www.hackingarticles.in/return-hackthebox-walkthrough/) by [Raj](https://www.hackingarticles.in/author/raj/)

Return is a Windows machine on HTB and is rated as easy, this box is designed over windows that have **[Weak Service Permission](https://www.hackingarticles.in/windows-privilege-escalation-weak-services-permission/)**. If summarized, we will abuse a printer admin portal to get hardcoded credentials through netcat and use them for WinRM login. The printer service account is a member of the Server Operators group which allows one to stop and start some services. Thus, we exploited weak configured services to execute our malicious exe file by abusing the Server Operators’ permission.

### Table of content

**Initial Access**

* Enumeration
* Credential Dumping
* WinRM Valid Account
* User Flag

**Privilege Escalation**

* Abusing weak service permission
* Root lag

Let’s deep dive into this.

### Initial Access

First, we do a Nmap scan of the machine’s IP address to find the open ports and observed some ports are open, from Microsoft Services we understood its Windows Operating System.

```
nmap -sV -sC 10.129.31.219
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGjvTOshLo6CMe_t2gZa7W9HCpv4WV6_-iahD_VQBOFxsWjvoEoNoNLavU51c5g4yq5nFlW38sYYa0QvT5b6bqMMT1JLN0GzeVRm5GinHo2wAMTQ3OGRWrya0VzdwYlTMNIPVdAFNsjowwvzEBn8zzkHHBD309svFynqNc9PdqwSHNELwIcH6GLJCFZQ/s16000/1.png)

### Enumeration

Since port 80 is open, let’s try to access the IP address via a browser.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwOIWykpghBfzPAhdRPJpU34X0rmyZA6vsFTK5_A4ih1cMip2ORQbAZaAY1HOfQ5nhGmfSM5kIj-zx4mOaXbzKSlBsUztdHT-Z3sZ5FsaVMJuBGXAOWsUWNvUuVbTb7Vj6IEAwh6IsWHhrHNnrrM5jnftlX1Bjzti12URUYEVt_uNBB0CVZvr6ESajrw/s16000/2.png)

As you can see, we have access to a printer admin panel. The pages are running PHP. Let’s navigate to the setting tab.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNyliMp2_RLQZrkSQud_5EISnalHjdZuImW3YB0iPIbP0JNVXxpgKTv6dkO53k3LimLSdMNLntt9GsBmc1QK-9IYKTsV3GFQlQp6RNV3wtuBJgzzkQ_yO37eszWL124DWNZwr5_aCrzM6hp5zjSSN3PqJm3UW2nz2R7Jm_ih4194eLL3G00YruRejxlA/s16000/3.png)

The above setting shows us the username which is **svc-printer** and the hardcoded password which has been masked. The server address field is the only field that works as a parameter then the update button is pressed. So the printer is communicating with the local address on port 389.

What if we replace the server address with the attacking machine IP address using port 389?

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8UY23M9GeHQ5R7291nmXeLQO3Poyw6LAqrec00JDbOZo9XjIyFgDfwHn_Z1Q49DmhGG1-HJzDQxkLDIPTHd0gJYwcMEXZzX1elAPXxbeKanEoYYCy-VCdFqhoSJ6YLMHpUjFzxKRLXUrXhhU9Gz4QYyCvLkWNNlb24PhyYPaC8XMWaXNzwYYZnn7Y7g/s16000/4.png)

### Credential Dumping

Once we have replaced the server address from the attacker’s IP (Kali Linux), we launched Netcat listener on port 389 on our kali machine.

```
nc -lvp 389
```

Once we hit the update button, we obtained the password “1edFg43012!!”

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisphyQLOOcHWZSf5Z6TkgKIHa1pmwjZKenVF2N3AtypKlWisoWak8WHIlwjtg4zM7P2lM9LwCbtH_cbsWJXw0OUeAOq5pStK-990zdtTKw1Wf2tpfjQBqLQixr2i6OHZt0Umne_sMVsPtvWgn8CpidQP55nqm53SMt0M1MJxFuzwSYDi8nKJpTA-s_2w/s16000/5.png)

#### WinRM Valid Account

Let’s use evil-winrm to establish a remote connection. This can be done by issuing the command below:

```
evil-winrm -i 10.129.31.219 -u svc-printer -p "1edFg43012!!"
```

We have access to the server. Let’s browser to the desktop directory and see if we can find any flags. Indeed, as shown in the above screenshot, we can find the user.txt flag.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgahb42P7LaJVrxOh3rTOnuBGMfpmPsAnuqfGlDyJb0ZZ_7yhc1E36Fr-rqTAhqaKT3fC9XfmzjCV9Hsw34KsHMvug0jVkkQxooDoChXL7d4nibfem1sKCKp-rvAUfo4Qhq-0ivbny40ONFge-w6WnjCQjC1wVRyKTXYo6vmTpDcZq6IIAEp_DyrFVz5Q/s16000/8.png)

### Privilege Escalation

Now that we have access to the machine, let’s verify which user permission or group we have.

To verify this, we issue the command **net user svc-printer**

From the screenshot below, we can see that the actual user is a member of the **server operators** group.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6JuVX4J26K252iLBwUQM4mxNQPUbEVLUtO6Q1jkti5cQykkMTyl1FFYDoMAJuV4hm8_ssGPwI9i1IjgPbO46PpU-ciSumMTu9WIkFHeg0Ye_Qm6IhAzL9zWzKx5JjhonVHfmOjWroE7ZA3KFt_K-yDfJhraxYDb5w6gGTAP5K-EUzPpRUbocZQzUpsg/s16000/9.png)

What can a user with a Server Operators group membership do?

The server operators can start and stop services.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEia8YhLQAD-ZjWNCGdw5YtcBFCrCBZru3K-yrBiUpFC6TGMUT7PaHg4SrmS1ToGcqNyziw7oSOtbXKtR7In00e1VPde9fMH9JAkTX2VuPDL_2xUfmlPcuO7aS2mqgs-FnT-qbtrmlzMLyx_zN2Manld6H-ukxzGr49e4Pe7E1Fooo2vQGNK6PyzZxP7dA/s16000/10.png)

The server Operator group is considered a service administrator and can change binaries that are installed on the domain controller, read more from **[here](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#server-operators)**.

```
upload /usr/share/windows-binaries/nc.exe
```

Thus, we first uploaded the nc.exe windows binaries file and then enumerate for installed services for further exploitation.

```
services
```

we found a list of installed services and their path along with true/false flags for privileges.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXs...