---
title: Credential Dumping: GMSA
url: https://www.hackingarticles.in/credential-dumping-gmsa/
source: Hacking Articles
date: 2025-04-07
fetch_date: 2025-10-06T22:02:46.986172
---

# Credential Dumping: GMSA

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
»* [Credential Dumping](https://www.hackingarticles.in/category/credential-dumping/)
»* [Credential Dumping: GMSA](https://www.hackingarticles.in/readgmsapassword-attack/)
»

[Credential Dumping](https://www.hackingarticles.in/category/credential-dumping/), [Domain Credential](https://www.hackingarticles.in/category/red-teaming/domain-credential/)

# Credential Dumping: GMSA

[April 6, 2025June 24, 2025](https://www.hackingarticles.in/readgmsapassword-attack/) by [Raj](https://www.hackingarticles.in/author/raj/)

**ReadGMSAPassword Attack** is a technique where attackers abuse misconfigured **Group Managed Service Accounts (gMSA)** to retrieve their passwords. In **Active Directory**, **ReadGMSAPassword** should only be granted to specific systems.. However, if these permissions are misconfigured, an attacker with access to a machine that can query the gMSA password can extract it and use it to authenticate as that service account. Once obtained, the **gMSA credentials** can be used for lateral movement, privilege escalation, and persistence within the domain. This method is widely known as the ReadGMSAPassword attack and is part of a broader category of credential abuse techniques. Moreover, attackers can also perform **Pass-the-Hash (PtH) or Overpass-the-Hash attacks** using the extracted **NT hash** of the gMSA password, allowing them to impersonate the account and access other network resources. Therefore, properly securing gMSA permissions and monitoring account access is crucial to preventing this attack.

This guide will provide an in-depth explanation of the ReadGMSAPassword attack, including its working mechanism, the key attributes involved, and how attackers exploit it. Additionally, we will demonstrate an attack scenario where an attacker manipulates delegation settings to gain control over a privileged account.

### Table of Contents

* Understanding Group of GMSA
* Prerequisites
* Lab Setup
* Exploitation Phase
* Bloodhound – Hunting for Weak Permission

**Method for Exploitation – Use Alternate Authentication Material: Pass the Hash (T1550.002)**

* gMSADumper
* nxc
* ntlmrelayx
* ldap\_shell
* GMSAPasswordReader

Post Exploitation

Detection & Mitigation

### Understanding Group Managed Service Account (gMSA)

A Group Managed Service Account (gMSA) is a special type of Active Directory (AD) account that administrators use to run automated services securely. Microsoft introduced it in Windows Server 2012 to solve the common problem of managing service account passwords. Unlike traditional service accounts, where administrators often set passwords manually and rarely update them, gMSAs allow Active Directory to manage passwords automatically.

#### Why Do We Need gMSAs?

Before gMSAs, administrators often used regular user accounts for services, but this led to major security risks:

* **Weak or Unchanged Passwords**: Service account passwords were rarely rotated, making them vulnerable to brute-force and credential theft attacks.
* **Manual Management:** Admins had to manually change service account passwords, which was error-prone and difficult to scale.
* **Kerberoasting Attacks:** Service account passwords could be cracked if an attacker obtained a Kerberos ticket.

#### How gMSAs Improve Security

* **Automatic Password Rotation:** AD generates and updates a complex password every 30 days (default setting).
* **No Manual Password Management:** Administrators never need to know or manage the password.
* **Multiple Machines Can Use a gMSA:** Unlike normal service accounts, multiple computers can use the same gMSA securely.

#### How gMSAs Work – Key Concepts

* **Automatic Password Generation:** The Key Distribution Service (KDS) root key in AD is responsible for generating gMSA passwords.
* **Password Storage:** The password is stored in an attribute called **msDS-ManagedPassword**, which only authorized users and machines can retrieve.
* **Access Control:** The **msDS-GroupMSAMembership** attribute defines which accounts can retrieve the password.

#### Key Attributes of gMSA

A gMSA has special Active Directory attributes that store its information:

* **msDS-ManagedPassword** – Stores the current and previous gMSA passwords in encrypted form.
* **msDS-ManagedPasswordID** – Stores the key ID used to generate the current password.
* **msDS-ManagedPasswordPreviousID** – Stores the key ID used to generate the previous password.
* **msDS-GroupMSAMembership** – Defines which users/computers can request the password.
* **msDS-ManagedPasswordInterval** – Defines how often (in days) the password changes (default: 30 days).

#### How Attackers Can Abuse gMSAs – ReadGMSAPassword

This privilege allows you to read the password for a Group Managed Service Account (GMSA).

The intended use of a GMSA is to allow certain computer accounts to retrieve the password for the GMSA, then run local services as the GMSA. However, an attacker with control of an authorized principal may abuse that privilege to impersonate the GMSA.

While gMSAs improve security, attackers can still abuse **ReadGMSAPassword attack** if misconfigurations are present.

* **Stealing the gMSA Password**: If an attacker has access to a machine that can retrieve the gMSA password, they can extract it using PowerShell or LDAP queries. The extracted password can then be used to authenticate as the gMSA.
* **Pass-the-Hash (PtH) Attacks**: Once an attacker gets the NT hash of the gMSA password, they can perform a Pass-the-Hash attack to gain access to systems.
* **Overpass-the-Hash (Pass-the-Ticket) Attacks**: Attackers can convert the extracted NT hash into a Kerberos ticket and use it to impersonate the gMSA.
* **Running Malicious Services**: If an attacker has control over a computer that can use a gMSA, they can create a malicious service or scheduled task that runs as the gMSA, gaining elevated access.

As a result, this misuse of the **ReadGMSAPassword** **attack**...