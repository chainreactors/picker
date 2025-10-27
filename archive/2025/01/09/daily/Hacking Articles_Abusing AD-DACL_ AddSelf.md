---
title: Abusing AD-DACL: AddSelf
url: https://www.hackingarticles.in/abusing-ad-dacl-addself/
source: Hacking Articles
date: 2025-01-09
fetch_date: 2025-10-06T20:05:58.836358
---

# Abusing AD-DACL: AddSelf

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
»* [Abusing AD-DACL: AddSelf](https://www.hackingarticles.in/addself-active-directory-abuse/)
»

[DACL Attacks](https://www.hackingarticles.in/category/dacl-attacks/)

# Abusing AD-DACL: AddSelf

[January 8, 2025June 19, 2025](https://www.hackingarticles.in/addself-active-directory-abuse/) by [Raj](https://www.hackingarticles.in/author/raj/)

This post explores **AddSelf Active Directory abuse**, a common misconfiguration involving **Discretionary Access Control Lists (DACL)**. Specifically, by exploiting the **AddSelf permission**, attackers can escalate privileges by adding themselves to privileged groups like Domain Admins or Backup Operators. As a result, they gain administrative control, move laterally within the network, access sensitive systems, and maintain persistence.

Moreover, attackers can perform **Kerberoasting attacks** to steal **credentials** or gain control over backup data, potentially leading to a full domain takeover if the abuse goes undetected and unremediated.

The **lab setup** required to simulate these attacks includes methods mapped to the **MITRE ATT&CK framework**, which helps clarify the associated techniques and tactics. This post also covers detection mechanisms to identify suspicious activities linked to **AddSelf attacks and** actionable recommendations to mitigate these vulnerabilities. Ultimately, this overview equips security professionals with critical insights to recognize and defend against these prevalent threats.

### Table of Contents

**AddSelf Permission**

**Prerequisites**

**Lab Setup** – User Owns AddSelf Permission on the Domain Admins Group

**Exploitation Phase I** – AddSelf Abuse on Domain Admins Group

**Bloodhound** – Hunting for Weak Permissions

**Method for Exploitation** – Account Manipulation (T1098)

* + Linux Bloody AD
  + Net RPC
  + Linux Ldap\_shell
  + Windows PowerShell – Powerview
  + Windows PowerShell – Active Directory module

**Post Exploitation** – Dumping hashes with Impacket

**Lab Setup** – User Owns AddSelf Permission on the Backup Operators Group

**Exploitation Phase II** – User Owns AddSelf Permission on the Backup Operators Group

**Bloodhound** – Hunting for Weak Permissions

**Method for Exploitation** – Account Manipulation (T1098)

* + Linux adduserstogroup tool

**Post Exploitation** – Dumping hashes with Impacket

**Alternate method of dumping hashes with Impacket**

**Detection & Mitigation**

### AddSelf Permission

The **AddSelf** permission in Active Directory allows users to add themselves to the target security group. Because of security group delegation, the members of a security group have the same privileges as that group.

By adding yourself to a group and refreshing your token, you gain all the same privileges that the group has.

The impact of **AddSelf DACL abuse** can vary based on the group that is abused. Below is a breakdown of the potential impact from an attacker’s perspective:

### Prerequisites

* Windows Server 2019 as Active Directory
* Kali Linux
* Tools: Bloodhound, Net RPC, Powerview, BloodyAD, Ldap\_Shell, Impacket
* Windows 10/11 – As Client

### Lab Setup – User Owns AddSelf Permission on the Domain Admin Group

**Create the AD Environment:**

To simulate an Active Directory environment, you will need a Windows Server as a Domain Controller (DC) and a client machine (Windows or Linux) where you can run enumeration and exploitation tools.

**Domain Controller**:

* Install Windows Server (2016 or 2019 recommended).
* Promote it to a Domain Controller by adding the **Active Directory Domain Services.**
* Set up the domain (e.g., **local**).

**User Accounts**:

* Create a standard user account named **Shreya**.

```
net user shreya Password@1 /add /domain
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_k5WLJ0lO1ElZEoPO97uqPhMgIYpbeLuN9MsUnScZl-RIst_tErOpqHrbxJUAGaV6IoM-LdFNRxaRuCmzieaY4Lzpa82BV8n1IJlN18UJrAIs3dBaXTC5aJhMhkMHrwDzCua_kyQf3pnkkluJd4SjF6QXMqt1QWlnSHMTyAKGN9VBe73GX39Ey8xMMNgX/s16000/1.png)

* **Assign the “AddSelf” Privilege to Shreya:**
* Firstly, once your **AD environment** is set up, you need to assign the **“AddSelf” privilege** to **Shreya** for the **Domain Admins group**.
* To begin, open **Active Directory Users and Computers (ADUC)** on the **Domain Controller**.
* Next, enable the **Advanced Features view** by clicking on **View > Advanced Features**.
* Afterward, locate the **Domain Admins group** within the **Users container**.
* Finally, right-click on **Domain Admins** and select **Properties**.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNRzzOPePQYTOOy0mzWcE9NwnawJnyUof4av7mf-HlhgrMTyvXRyxgJqZYRYNaLjFRAl6fuL2MJi1fypQA9ag0mvEiNcIOzuPMcaJspqTVvsvPBjcB9HZXcTsuScwWKq1IgVRj4MfPO2jf9-y5O8h5Oql7C4STrsfd7aeXm-aziCbXZrLJvn710EoWEasu/s16000/2.png)

* Go to the **Security** tab, and click on the **Add** button.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNReCSr23BzvneY1S1TYsjHeujSTP-NfLHi3pQwP05URiCMnYPsDHiYz7CBkxsXgOFvFinetrHmwEwduwkaanCE50TrM1JOOb7HaVRX__eB80OXUgINOLEJESjPSLDgqzJxtuWKhLryFfTHngQeiZ2pI-xgMjvnA_okLwcrjilKeNDqcYJvlvn9kJsTE-0/s16000/3.png)

* In the “Enter the object name to select” box, type **Shreya** and click **Check Names,** and click OK.
* Select the **Shreya** user and in the **Permissions** section, click on the **Advanced** option.
* In the **Advanced security settings** box, double-click on **Shreya** user’s permission entry.
* In the **Permissions** section, check the box for **Add/remove self as member permission** rights.
* Apply the settings.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt7YEq25BhHURA2z_LUnuceG7mxOY1K1MPv_NW4DiEjpgPGd7FyW1m8zC27iCs-l57uZ4nP5gRVvPQ-aVCTBKdbgwxjCUvZwEHeuFkFq5136zZdHLljgYRb8besgLV4Kj3CK2AUi-m_vjzXDRmKaL6UfpSanhN8LWCEEDTg-Xe2DLgj7zca3ElmUiU9dnL/s16000/5.png)

At this point, **Shreya** now has **Ad...