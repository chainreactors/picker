---
title: Abusing AD-DACL: GenericWrite
url: https://www.hackingarticles.in/abusing-ad-dacl-genericwrite/
source: Hacking Articles
date: 2024-11-28
fetch_date: 2025-10-06T19:15:36.682756
---

# Abusing AD-DACL: GenericWrite

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
»* [Abusing AD-DACL: GenericWrite](https://www.hackingarticles.in/genericwrite-active-directory-abuse/)
»

[DACL Attacks](https://www.hackingarticles.in/category/dacl-attacks/)

# Abusing AD-DACL: GenericWrite

[November 27, 2024June 19, 2025](https://www.hackingarticles.in/genericwrite-active-directory-abuse/) by [Raj](https://www.hackingarticles.in/author/raj/)

In this post, we explore **GenericWrite Active Directory abuse**, focusing on how attackers exploit **Discretionary Access Control Lists (DACLs)** to escalate privileges. By abusing the **GenericWrite** permission, adversaries can modify group memberships, service principal names, or login scripts—leading to lateral movement or domain dominance.

The lab setup necessary to simulate these attacks is outlined, with methods mapped to the **MITRE ATT&CK** **framework** to clarify the associated techniques and tactics. **Detection mechanisms** for identifying **suspicious** activities linked to **GenericWrite** **attacks** are also covered, alongside actionable recommendations for **mitigating these vulnerabilities**. This overview equips security professionals with **critical insights** to recognize and defend against these prevalent threats.

### Table of Contents

**GenericWrite Permission**

**Prerequisites**

**Lab Setup** – User Owns GenericWrite Permission on the Domain Admin Group

**Exploitation Phase I** – User Owns GenericWrite Permission on a Group

**Bloodhound** – Hunting for Weak Permission

Method for Exploitation – Account Manipulation (T1098)

* Linux Net RPC – Samba
* Linux Bloody AD
* Windows Net command
* Windows PowerShell – Powerview

**Lab Setup** – User Owns GenericWrite Permission on Another User

**Exploitation Phase II** – User Owns GenericWrite Permission on Another User

**Bloodhound** – Hunting for Weak Permission

**Method for Exploitation** – Kerberoasting (T1558.003)

* Linux Python Script – TargetedKerberoast
* Windows PowerShell – Powerview

Detection & Mitigation

### GenericWrite Permission

The **GenericWrite** permission in **Active Directory** allows a user to modify all writable attributes of an object, except for properties that require special permissions such as resetting passwords.

**If an attacker gains GenericWrite over a user**, they can write to the **servicePrincipalNames** attribute and immediately initiate a **targeted Kerberoasting** attack.
**Moreover**, having **GenericWrite** over a group enables them to add their account—or one they control—directly to that group, effectively escalating privileges.
**Alternatively**, if the attacker obtains **GenericWrite** over a computer object, they can modify the **msds-KeyCredentialLink** attribute. **As a result**, they create **Shadow Credentials** and authenticate as that computer account using **Kerberos PKINIT**.

### Prerequisites

* Windows Server 2019 as Active Directory
* Kali Linux
* Tools: Bloodhound, Net RPC, Powerview, BloodyAD
* Windows 10/11 – As Client

### Lab Setup – User Owns GenericWrite Permission on the Domain Admin Group

#### Create the Active Directory Environment:

To simulate an **Active Directory** environment, set up a **Windows Server** as a **Domain Controller (DC)** and a client machine (Windows or Linux) to run enumeration and exploitation tools.

#### Domain Controller:

* First, install **Windows Server** (2016 or 2019 recommended).
* Then, promote it to a **Domain Controller** by adding the **Active Directory Domain Services** role.
* Finally, set up the domain (e.g., `ignite.local`).

#### User Accounts:

* Next, create a standard user account named **Anuradha**:

```
net user anuradha Password@1 /add /domain
```

![GenericWrite Active Directory Abuse](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-inD1OxzZZ9671XORPCQQINPV32MU44DH-gmuxsYnpAHwzF_0iakd81dQiFMrhR-id0hI7G1-cxpyP0F7pxgivNJEKo5BUUHquxyD4CfWIQP8QZckHhWkeQf9QjURGVhhYzMO_vbijeS_m12p1jg1-0rKr0DDwK3klriWf5GCwERkGO5vTzyaAPDX13wt/s16000/1.png)

#### Assign the “GenericWrite” Privilege to Anuradha:

Once you configure the **AD environment**, assign the **GenericWrite** privilege to **Anuradha** for the **Domain Admins** group.

**Steps**:

* Open **Active Directory Users and Computers** (ADUC) on the Domain Controller.
* Enable the **Advanced Features** view by clicking on **View** > **Advanced Features**.
* Locate the **Domain Admins** group in the Users container.
* Right-click on **Domain Admins** and go to **Properties**.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfderD1cPvJO0HE6wTWhDoWwMGBsdFokE7xA8vYbbM3tRF9svD9Bb5jVLd9edWZETJFKt_-q2IyM-zkStvMaQhAJjqcJDoa1fEHyDuVVtgVSl8hGHDJY7h4Wy7bXATFP1cJFF1gcSF1TfealOpb5PjdhbAUmUL0Eyat6aQkIfyBwxQepCmPawshW4jJBSF/s16000/2.png)

* Navigate to the **Security** tab, then click on **Add**.

![GenericWrite Active Directory Abuse](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5VD8vPgK6la9mRFjNt7W7miBj91-ytIaYEdnKDReVRL8UCdG6mAz7lkRtVIANA2PDwAoT84_vwmDDsD6sgGduc7OLOCsl2D50f3K3M5C64PPk3yhyphenhyphen8c7rXF4vonnF6dDDUV_VxhyY7QYJzib73avQXSpXSL_HIhYSGhFfw1s_vcLM0WfMB8Jo_9vHUadA/s16000/3.png)

* In the “Enter the object name to select” box, type **Anuradha** and click **Check Names,** and then click on OK.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJ1YPAUW7X_pYJnhqXxdS0ErvJYl_AHB7_uKNBh8yCuKCv4swQ6W8Atks45SzLOSwkeg4eB7NcqOlU0jIU7vSxm4INUHvLIn1y6fJdjqA4TO4-l2yngUZLJCv0-M3-62xJl-HItxpqoe9W2XBvGtUn_HXFMHcOk8g4qXIRbUE09EshKPH8TSZ_BMPjdsL0/s16000/4.png)

* In the **Permissions** section, check the box for **Write** permission.

![GenericWrite Active Directory Abuse](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkkZF9FHnmwnf8_2DcteR9GzXKmNlf8VbCeEYNDsZaxb8Z3uUkm_sjQ4SP6IFg98Z8DePs5zr_HQ3lKmpHJ0pUnwgyE4NKbV6TNT_BjpVU3pkG_KBEkoy1iJxwEgBNFAUi_2dXq02P_lCVqjxA83NbqUAU7j6hcowCa6aQsOlbjnVYiClsc_TY8aP_KY93/s16000/5.png)

* Sele...