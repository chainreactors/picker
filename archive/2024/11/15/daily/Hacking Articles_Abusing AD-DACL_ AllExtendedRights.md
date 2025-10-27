---
title: Abusing AD-DACL: AllExtendedRights
url: https://www.hackingarticles.in/abusing-ad-dacl-allextendedrights/
source: Hacking Articles
date: 2024-11-15
fetch_date: 2025-10-06T19:17:37.032062
---

# Abusing AD-DACL: AllExtendedRights

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
»* [DACL Attacks](https://www.hackingarticles.in/category/dacl-attacks/)
»* [Abusing AD-DACL: AllExtendedRights](https://www.hackingarticles.in/allextendedrights-active-directory-abuse/)
»

[DACL Attacks](https://www.hackingarticles.in/category/dacl-attacks/)

# Abusing AD-DACL: AllExtendedRights

[November 14, 2024June 19, 2025](https://www.hackingarticles.in/allextendedrights-active-directory-abuse/) by [Raj](https://www.hackingarticles.in/author/raj/)

**AllExtendedRights Active Directory abuse** represents a critical threat vector, as attackers can exploit **Discretionary Access Control Lists (DACL)** in enterprise environments. In this post, we will explore how the **AllExtendedRights permission** enables attackers to escalate privileges, maintain persistence, and potentially seize control of **vital directory resources**—ultimately making it a significant foothold for **domain compromise**.

Moreover, we’ll walk through the required **lab setup** to simulate these attacks, with **exploitation methods** aligned to the **MITRE ATT&CK framework**. Furthermore, we cover **detection strategies** to identify suspicious activity involving **AllExtendedRights**, and offer actionable **mitigation techniques** to reduce the risk. This post aims to help defenders understand and counter one of the stealthiest forms of **Active Directory abuse**. As you will see, **AllExtendedRights Active Directory abuse** can go unnoticed, making timely detection and prevention crucial.

### Table of Contents

**AllExtendedRights Permission**

**Prerequisites**

**Lab Setup** – User Owns AllExtendedRights Permission

**Exploitation** – User Owns AllExtendedRights Permission

**Bloodhound** – Hunting for Weak Permission

**Method for Exploitation** – Change Password (T1110.001)

* Linux Net RPC – Samba
* Linux Net RPC – BloodAD
* Linux Net RPC – Rpcclient
* Windows PowerShell – Powerview

**Detection & Mitigation**

### AllExtendedRights Permission

To elaborate, **extended rights** refer to special privileges that administrators assign to objects, allowing them to read **privileged attributes** and perform specific **administrative actions**.

Specifically, this permission enables attackers to **reset passwords** on **User objects** and to craft a **Resource-Based Constrained Delegation (RBCD)** attack for **Computer objects**.

Consequently, when a domain object possesses **AllExtendedRights permissions** on the domain object itself and becomes compromised, the attacker gains both the **DS-Replication-Get-Changes** and **DS-Replication-Get-Changes-All privileges**. These rights allow the attacker to **replicate directory objects** from the domain using the **DCSync technique**, further demonstrating the dangers posed by **AllExtendedRights Active Directory abuse**.

### Prerequisites

* Windows Server 2019 as Active Directory
* Kali Linux
* Tools: Bloodhound, Net RPC, Powerview, BloodyAD
* Windows 10/11 – As Client

### Lab Setup – User Owns AllExtendedRights Permission

To begin with, in this lab setup, we will create two users — **Kavish** and **Geet** — and assign the **“AllExtendedRights” permission** to **Geet** for the **Kavish** user.

#### Create the AD Environment:

To simulate an Active Directory environment, you will first need a **Windows Server** configured as a **Domain Controller (DC)**. Additionally, you’ll require a client machine (Windows or Linux) where you can run **enumeration** and **exploitation tools**.

##### **Domain Controller**:

* First, install Windows Server (2016 or 2019 recommended).
* Next, promote it to a Domain Controller by adding the **Active Directory Domain Services** role.
* Finally, set up the domain (e.g., **ignite.local**).

##### **User Accounts**:

* Create two AD user accounts named **Kavish** and **Geet**.

```
net user kavish Password@1 /add /domain
net user geet Password@1 /add /domain
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMJXCrxiaK4aBfcwURTTJT_0R3I69dc97DyoYsyzPJkd6KgCGjIeOm7UaVR_jRKMdQ7p9s7Ztid4HZEQA9gebLPb5ikquzrZvBbb58Hf4JXydkjQ_A2X-6xAwNL2_L-tSDtspxa2lyouQ4SkWTsEbT627ImplaVAApRtd_NgyraotO8MzF3oLhVxpJX9gl/s16000/1.png)

#### Assign **the “AllExtendedRights” Privilege to Geet for Kavish User:**

Once your AD environment is set up, you need to assign the **“AllExtendedRights”** privilege to **Geet** for **Kavish** user.

* **Steps**:
  1. Firstly, open **Active Directory Users and Computers** (ADUC) on the Domain Controller.
  2. Then, enable the **Advanced Features** view by clicking on **View** > **Advanced Features**.
  3. Locate User **Kavish** in the **Users** container.
  4. Right-click on **Kavish User** and go to **Properties**.

                 ![AllExtendedRights Active Directory Abuse](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhekYVuiprM0IVF0fDbK5BvfSRuxeQ7GhcJT04_6ddQVYhnzF0i_fXYHNpPQBGY_HdBpwe2OX0PfFVDZ5nnEglTcBMZvEwydt_KYl7_68rcADTlxNChi3-9Kd_cxQqnkoRVAHffgaqwGzuVi4ZWeb6rZV7mUSQAT4hIyifTKeJ0aph8HXxbifVBPc1Ry-k6/s16000/2.png)

               5. Navigate to the **Security** tab, and click on **Add** button

                ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixIfSEqkok5goMywpM6VYZKBfvQTWOG1ocNT6LyTp8PWz-R5uKZ_qx3TNG0Wvp5JmWNRPjWmCTbkhrQA9QFHdzZDRCj1lGZAS8mXUp7__yCRvsYBZnxBeA4usu18Q2OduqeWq0XYsCO1TPKtE3RERhpuk7uDNybduKTaDzUDCar6BgiBnHBHLvbBKLghuK/s16000/3.png)

                6. In the “Enter the object name to select” box, type **Geet** and click **Check Names** and click on OK.

                ![AllExtendedRights Active Directory Abuse](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiupaTS_-WAQRTMksgGqUe6BiLV6WOr6NsBAIJtaDTqfowppVuP5F-WtRcWt_1faX26O2pQnKCk59_f7LEsA_4JApL_SmND8zzFZX6i_-7KMN8PlqfjUYOs8qdvJ8kn5Gi1BrjGHwlXCBw3sQc3-i3v9gmtbQOwWgqqAG-g3MQBta5VUJJKRhAdXWRgu-Zv/s16000/4.png)

                7. Here, select **Geet** user and click on **advanced** option.

                ![](https://blogger.googleu...