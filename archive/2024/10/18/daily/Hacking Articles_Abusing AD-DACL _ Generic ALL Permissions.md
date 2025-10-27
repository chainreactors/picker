---
title: Abusing AD-DACL : Generic ALL Permissions
url: https://www.hackingarticles.in/abusing-ad-dacl-generic-all-permissions/
source: Hacking Articles
date: 2024-10-18
fetch_date: 2025-10-06T18:51:00.388984
---

# Abusing AD-DACL : Generic ALL Permissions

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
»* [Abusing AD-DACL : Generic ALL Permissions](https://www.hackingarticles.in/genericall-active-directory-abuse/)
»

[DACL Attacks](https://www.hackingarticles.in/category/dacl-attacks/)

# Abusing AD-DACL : Generic ALL Permissions

[October 17, 2024June 19, 2025](https://www.hackingarticles.in/genericall-active-directory-abuse/) by [Raj](https://www.hackingarticles.in/author/raj/)

In this post, we explore how attackers can exploit the **Generic ALL Active Directory abuse** through **Discretionary Access Control Lists (DACL)**. This powerful permission grants unrestricted access to objects like user accounts, allowing adversaries to perform actions such as Kerberoasting, password resets, and account manipulation.

We will detail the lab setup needed to simulate these attacks and map these methods to the **MITRE ATT&CK framework** to understand the techniques and tactics involved. Additionally, we will discuss detection mechanisms to identify suspicious activities linked to Generic ALL attacks and provide actionable recommendations to mitigate these vulnerabilities. This overview aims to equip security professionals with the knowledge to recognize and defend against these prevalent threats.

### Table of Contents

**Abusing AD-DACL – Generic ALL Permissions**

**Key Concepts of DACL**

**Generic ALL Right**

**Prerequisites**

**Lab Setup** – User Owns Generic ALL Right For Domain Admin Group

**Exploitation Phase I** – User Own Generic All Right for Group

**Bloodhound** -Hunting for Weak Permission

**Method for Exploitation** – Account Manipulation (T1098)

* Linux Net RPC – Samba
* Linux Bloody AD
* Windows Net command

**Exploitation Phase II** – User own generic Right for another user

**Bloodhound** -Hunting for Weak Permission

**Multiple Method for Exploitation**

* Kerberoasting
  + Linux Python Script – TargetedKerberoast
  + Windows PowerShell Script-Powerview
* Change Password
  + Linux Net RPC – Samba
  + Linux Net RPC – BloodAD
  + Linux Net RPC –Rpcclient
  + Windows Net Utility
  + Windows PowerShell -Powerview
  + Windows PowerShell

**Detection & Mitigation**

### Active Directory DACL

In Active Directory (AD), a **DACL** (Discretionary Access Control List) is a component of an object’s security descriptor. It specifies which users or groups are allowed (or denied) access to the object and what actions they are permitted to perform. It essentially controls who can do what to an object. Such as a user account, computer, group, or any other directory object.

### Key Concepts of DACL

Access Control Entries (ACEs):
A DACL is made up of multiple ACEs. Each ACE defines the specific access rights for a user or group and specifies what kind of access (read, write, execute, etc.) is allowed or denied.

Permissions:
Permissions define the specific actions a user or group can perform on an object. These permissions can be basic, like reading or writing to the object, or more complex, like modifying permissions or taking ownership.

Rights:
Rights are a higher-level abstraction of permissions.

##### **In Active Directory, common DACL rights include:**

* **GenericAll**: Grants full control over an object (e.g., modify properties, reset passwords, etc.).
* **GenericWrite**: Allows modification of some object properties.
* **WriteDACL**: Lets the user modify the DACL itself, potentially escalating privileges.
* **WriteOwner**: Grants the ability to take ownership of the object, allowing further privilege modification.
* **ReadProperty**: Allows reading of object properties (e.g., attributes in a user object).
* **AllExtendedRights**: Grants special rights for advanced operations, like resetting passwords or enabling delegation.
* **Delete**: Grants the ability to delete the object.
* **ReadDACL**: Allows reading the object’s access permissions without being able to change them.
* **ForceChangePassword**: Allows forcing a user to change their password without knowing the current one.

Inheritance:
DACLs can be **inherited** from parent objects, meaning permissions on a container (like an Organizational Unit) can be passed down to child objects. This simplifies management but can also lead to unintended permissions if not carefully configured.

Security Descriptor:
The DACL is part of a larger security descriptor that also includes the **Owner** (the entity that has ownership of the object and can change its permissions) and an optional **SACL** (System Access Control List) that controls auditing.

*Weak DACLs can lead to unauthorized access or privilege escalation if not properly configured.*

### Generic ALL Right

In Active Directory, permissions and privileges define what actions an entity (user, group, or computer) can perform on another object. The **“Generic ALL”** privilege is one of the most powerful in AD because it grants **complete control** over the target object. This means that the user or group with this privilege can:

* Modify any attribute of the object
* Reset passwords
* Add or remove members from groups
* Delegate further control to other users
* Delete the object altogether

Because of its extensive reach, an attacker who gains “Generic ALL” privileges on sensitive objects (like privileged groups or service accounts) can essentially gain domain dominance.

#### Exploiting “Generic ALL” Privilege

Here’s how an attacker can leverage the **“Generic ALL”** privilege to compromise Active Directory:

1. **Identifying Targets with “Generic ALL” Privilege**
   The first step is to identify objects where the attacker has this privilege. This can be done using tools like **BloodHound** or **PowerView**, which map out Active Directory and show privilege relationships. Once identified, the attacker can choose their target based on the potential impact (e.g., a Domain Admin account).
2. **Resetting Passwords**
   If the “Generic ALL” privilege is ap...