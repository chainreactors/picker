---
title: Abusing AD Weak Permission Pre2K Compatibility
url: https://www.hackingarticles.in/abusing-ad-weak-permission-pre2k-compatibility/
source: Hacking Articles
date: 2025-02-09
fetch_date: 2025-10-06T20:33:42.917990
---

# Abusing AD Weak Permission Pre2K Compatibility

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
»* [Abusing AD Weak Permission Pre2K Compatibility](https://www.hackingarticles.in/pre2k-active-directory-misconfigurations/)
»

[Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# Abusing AD Weak Permission Pre2K Compatibility

[February 8, 2025June 19, 2025](https://www.hackingarticles.in/pre2k-active-directory-misconfigurations/) by [Raj](https://www.hackingarticles.in/author/raj/)

**Pre2K** **Active Directory misconfigurations** **(short for “Pre-Windows 2000”)** often stem from overlooked legacy settings in Windows environments. Common issues include enabling **NTLM** or **SMBv1** for backward compatibility, leaving **Pre-Windows 2000 accounts** active, and neglecting proper account cleanup. These misconfigurations, when combined with weak permissions, can expose domains to privilege escalation and unauthorized access.

In this article, we will show how a misconfiguration can set the password of Computer Accounts to match the hostname in lowercase, allowing an attacker to take over a domain controller.

### **Table of Contents**

* **Prevalence of Pre2K AD Misconfigurations**
* **Prerequisites**
* **Lab Setup**
* **Enumeration**
  + Method #1: Using the tool:- pre2k
  + Method #2: Using the tool:- nxc
* **Exploitation**
* **Mitigation**

### Prevalence of Pre2K AD Misconfigurations

While many organizations have moved to newer technologies, Pre2K (short for “Pre-Windows 2000″) misconfigurations can still found in many environments, especially where legacy applications or systems require continued support. A few prominent surveys across the industry confirm

* **40-60%** of organizations are still using legacy systems that require **Pre2K compatibility**.
* Around **30-40% of Active Directory environments** have lingering **unused Pre2K accounts** that remain improperly configured.
* **57% of businesses** rely on outdated or unsupported operating systems with legacy configurations, which often involve Pre2K AD misconfigurations.
* Approximately **30%** of data breaches stem from **mismanaged Active Directory settings**, including legacy configurations like Pre2K.

**Keynotes:**

* UAC 4128 indicates legacy settings where accounts may be enabled for authentication without the usual security checks (e.g., passwords).
* LogonCount of 0 suggests that the account might not be used for typical logons but could still be exploited for other purposes.
* Post-password change authentication: When a user changes their password, the system normally requires the new password for authentication.

### Prerequisites

* Windows Server 2019 as Active Directory Domain Controller
* Tools: pre2k, nxc, impacket, evil-winrm
* Kali Linux

### Lab Setup

In this lab set up, we will create a Computer Account and provide backward compatibility to interact with legacy systems or services that are particularly prior to Windows 2000.

**Create the AD Environment:**

To simulate an Active Directory environment, you will need a Windows Server 2019 as a Domain Controller (DC) and a client/attacker machine (Kali Linux) where you can run enumeration and exploitation tools.

**Domain Controller:**

* install Windows Server (2016 or 2019 recommended).
* Promote it to a Domain Controller by adding the “**Active Directory Domain Services**” role.
* Set up the domain (e.g., “**local**”).
* Create a domain user with username “**raj**” and password “**Password@1**”.

**Create a Computer (Account) and assign Pre2K Compatibility:**

Once the AD environment is setup, open “**Active Directory Users and Computers** (ADUC)” on the Domain Controller. Then, right-click on “Computers” and add a New Computer.

![Pre2K Active Directory Misconfigurations](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRjeuMbA4KfCA8XaRguG95kUnwt18jPJ7BPqaJJ6DYxkKO4Q0NEJivY760vvnQyZGVUYH0fshLoRjJGII8wre5PfwWQtDLDrfsqNXd78L1N4pYwZKwznGKUNkRwmjW6eU2J1Vuh4kER5UZ4VjWOLoD2BcEXfwLZsLzrwQxoDmkOftTv9znlWsBErt2ltRS/s16000/1.png)

Provide the computer name as “demo”, “DEMO” for “pre-Windows 2000 Computer Name” and ensure to select the checkbox that enables this computer to support/act as a Pre2K computer.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjn6hR8erjYsJBzS1sb8IalIQKvKeXwjkG5T497QuERdhTrl7OdlIxLms55lYFiuvplcdR-hwmRxKO_FDMfwxblLGJhmX4HMcR0PsL_R8VeigijL6YuAgXjYmyQh1jTWIowXj8WZziTWiLm1dqvVaPNoVxIU0hcUdqvBdLh1Q2VRc7d6W4Fqv7Fwnka7_b-/s16000/2.png)

Click on “OK” button and confirm that a computer with name “demo” is created within “ignite.local” domain.

![Pre2K Active Directory Misconfigurations](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLu0hpKIiz92-N1wzv_gjiEFShN8JMSUEVwOz2XRYmn-_TDSu4Tuk2R9FZ1DJh-uHhN-3DXhqqJ6KeYFcTEPQYYM_-mu8sZlZTOXqLOMuNL8Ow7oUX_RMmibyL-tbP87c329YO5lEPimkM_v4HWgzgfzm-bTMF-gUp16dqItTcRS-HMUR6nyA_ILhs0_27/s16000/3.png)

**Note:** Ensure to have SMB & WINRM services enabled on the Domain Controller.

### Enumeration

Tools like pre2k and nxc are commonly used to enumerate **Pre2K Active Directory Misconfigurations and abuse weak AD permissions related to Pre2K compatibility**, which can expose computer accounts with default passwords.

#### pre2k

Use the commands below to download and install pre2k tool in Kali Linux.

```
git clone https://github.com/garrettfoster13/pre2k.git
cd pre2k
ls
pipx install .
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCEYp0LFPYoYveUIgoAJvqBZDtJomMIpgbULWfNFeaQCz6PKBJgqqojP0pWyi2g6vf8TGxevWQXHATFmvZ_uR8r5LARm4uVlhrkezvxl_B7D0E8oJGkgscFxH41_1oB1E4RtvS-bfZb5bFb_yrtZ4Bg1WTsrPWT69tel23xAhyyiM3OvujnPU5uBRk-Wjw/s16000/4.png)

Now, let’s enumerate valid Computer Accounts that act as pre-windows 2000 computers by performing password spraying attack using pre2k tool in an authenticated mode.

```
pre2k auth -u raj -p Password@1 -dc-ip 192.168.1.48 -d ignite.local
```

![Pre2K Active Directory Misconfigurations](h...