---
title: Diamond Ticket Attack: Abusing kerberos Trust
url: https://www.hackingarticles.in/diamond-ticket-attack-abusing-kerberos-trust/
source: Hacking Articles
date: 2025-01-28
fetch_date: 2025-10-06T20:07:28.279130
---

# Diamond Ticket Attack: Abusing kerberos Trust

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
»* [Persistence](https://www.hackingarticles.in/category/persistence/)
»* [Diamond Ticket Attack: Abusing kerberos Trust](https://www.hackingarticles.in/diamond-ticket-attack-abusing-kerberos-trust/)
»

[Persistence](https://www.hackingarticles.in/category/persistence/)

# Diamond Ticket Attack: Abusing kerberos Trust

[January 27, 2025June 19, 2025](https://www.hackingarticles.in/diamond-ticket-attack-abusing-kerberos-trust/) by [Raj](https://www.hackingarticles.in/author/raj/)

**The Diamond Ticket Attack** represents a sophisticated escalation in **Active Directory (AD) exploitation** methods, leveraging intricate flaws in **Kerberos authentication** and **authorization mechanisms**. In this article, we explore the technical nuances of the Diamond Ticket attack, delving deeply into the **underlying mechanisms**, the role of **Privilege Attribute Certificates (PACs)**, and the root causes that make AD environments susceptible. Finally, we conclude with detailed detection and mitigation strategies to protect against such threats.

### Table of Contents

* **Introduction- Diamond Ticket**
* **Attack Machnism**
* **Ticket Structure**
* **PAC Validation**
* **PAC Validation Limitation**
* **Prerequisites for Attack**
* **Remotely Diamond Attack -Linux**
* **Locally Diamond Attack-Windows**
* **Detection Techniques**
* **Mitigation Strategies**

### Introduction – Diamond Ticket

To build a solid foundation, you must first understand that in a **Domain PAC (Privilege Attribute Certificate)** attack, an attacker forges or manipulates the **PAC within a Kerberos ticket**. As a result, the attacker gains **unauthorized access or escalates privileges** within a **domain environment**. This technique proves effective because many services **trust the PAC** by default, often without validating its authenticity or verifying it against the **Key Distribution Center (KDC)**.

Following this, attackers take things further with the **Diamond Ticket attack**, which represents a more advanced form of the previously mentioned exploitation. In this scenario, the attacker directly manipulates **Kerberos tickets**—specifically **Ticket Granting Tickets (TGTs)** and **PACs**. Consequently, they use the forged tickets to escalate privileges within an **Active Directory (AD) domain**.

### Attack Mechanism

To begin the attack, the attacker manipulates or forges the PAC to include elevated privileges or fake group memberships (e.g., “Domain Admins”).

Subsequently, A forged ticket with the modified PAC is then sent to the target service.

During a typical **Diamond Attack**, the attacker leverages the **KRBTGT AES hash** to **decrypt a valid TGT (Ticket Granting Ticket)**. Then, they **modify the PAC (Privilege Attribute Certificate)** inside the TGT before **re-encrypting** the modified TGT with the **KRBTGT AES hash** again to make it appear **legitimate**.

Essentially, This attack is essentially a **TGT modification attack**. The attacker doesn’t need to steal the original TGT or create a completely new one; instead, they simply manipulate the PAC within an existing TGT.

#### Steps Involved in the Diamond Attack:

* **Obtain the AES hash of the KRBTGT account**: The attacker first compromises the **KRBTGT account** (often by dumping hashes from the domain controller or gaining access to sensitive domain controller information).
* **Decrypt the TGT using the KRBTGT AES hash**: The attacker then uses the AES hash of the KRBTGT account to **decrypt a valid TGT**. The TGT, when decrypted, contains the **PAC** which includes user privileges, group memberships, and other critical information.
* **Modify the PAC**: After decrypting the TGT, the attacker can modify the **PAC** to reflect unauthorized attributes or privileges. This could include adding themselves to privileged groups like **Domain Admins** or changing their group memberships to escalate privileges.
* **Re-encrypt the modified TGT using the KRBTGT AES hash**: Once the attacker has modified the PAC as desired, they re-encrypt the TGT using the **KRBTGT AES hash** to create a new valid TGT. This re-encryption makes the modified TGT appear legitimate to the Kerberos infrastructure.
* **Use the modified TGT**: The attacker can now present the modified TGT to access resources as if they were a privileged user, bypassing normal access control mechanisms.
* **TGS (Service Ticket)**: The **TGS tickets** are issued based on the TGT. They do not directly store the PAC; instead, they rely on the TGT’s PAC to validate the user’s identity and permissions.
* In this attack, the manipulation occurs before the TGS is involved because the tampered TGT is used to request a service ticket with elevated privileges.

### Ticket Structure

**TGT (Ticket Granting Ticket) Structure**

The **TGT** is issued by the **Authentication Server (AS)** and is used to request service tickets from the **Ticket Granting Server (TGS)**. Its structure typically contains:

**Header Information**:Ticket version and type.

**Client Information**:Username and realm (e.g., user@DOMAIN.LOCAL).

**Session Key**: A key shared between the client and the KDC, used for encryption.

**PAC (Privilege Attribute Certificate)**:Contains details about the user:

* Group memberships.
* Privileges (e.g., admin rights).
* Account SID (Security Identifier).

**Timestamp and Lifetime**:Validity period of the ticket (start time, expiration time).

**KRBTGT Encryption**:The TGT is encrypted and signed using the **KRBTGT hash** (AES or RC4), ensuring only the KDC can read or validate it.

**TGS (Service Ticket) Structure**

The **TGS** ticket is issued by the **Ticket Granting Server** based on the TGT and is used to access specific services. Its structure includes:

**Header Information**:Ticket version and type.

**Client Information**:Username and realm.

**Session Key**:A unique key for secure communication between the client and the target service.

**Serv...