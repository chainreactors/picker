---
title: Shadow Credentials Attack
url: https://www.hackingarticles.in/shadow-credentials-attack/
source: Hacking Articles
date: 2025-02-13
fetch_date: 2025-10-06T20:33:36.655013
---

# Shadow Credentials Attack

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
»* [Shadow Credentials Attack](https://www.hackingarticles.in/shadow-credentials-attack/)
»

[Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# Shadow Credentials Attack

[February 12, 2025June 19, 2025](https://www.hackingarticles.in/shadow-credentials-attack/) by [Raj](https://www.hackingarticles.in/author/raj/)

To begin with, this post explores the exploitation technique known as the Shadow Credentials attack. This attack leverages the mismanagement or exploitation of Active Directory Certificate Services (AD CS) to inject custom certificates into a user account, granting attackers persistent access. As a result of modifying the msDS-KeyCredentialLink attribute, adversaries can effectively create “shadow credentials” that allow them to authenticate as the target user without needing their password or NTLM hash.

The post outlines lab setup, exploitation methods, and mitigation techniques, mapped to the MITRE ATT&CK framework for clarity. In addition, detection mechanisms and actionable recommendations are provided to help security professionals identify and defend against this prevalent threat.

Specifically, this article focuses on the Shadow Credentials attack, a stealthy method that enables persistence in Active Directory by exploiting misconfigurations in certificate-based authentication.

### Table of Contents

* Shadow Credentials
* Prerequisites
* Lab Setup

**Exploitation**

* Bloodhound – Hunting for Weak Permission

**Method for Exploitation – AS-REP Roasting Attack (T1558.004)**

* PyWhisker
* PKINITtools
* Certipy-ad
* NTLMRelayx
* BloodyAD
* Metasploit
* ldap\_shell tool

**Post Explotation**

* Impacket -psexec
* Evil-winrm

**Detection & Mitigation**

### Introduction to Kerberos Authentication

Active Directory uses Kerberos, a trusted authentication protocol, to securely verify the identity of users and services. It issues tickets to avoid transmitting passwords over the network.

#### Symmetric Encryption in Kerberos

In traditional Kerberos authentication, symmetric encryption is used. Here’s how it works:

1. **AS-REQ (Authentication Service Request):** The client sends a request to the Key Distribution Center (KDC), including a timestamp encrypted with a key derived from the user’s password.
2. **AS-REP (Authentication Service Response):** The KDC validates the timestamp using the user’s stored hash and returns a Ticket Granting Ticket (TGT) encrypted with the KDC’s secret key.
3. **TGS-REQ and TGS-REP:** The client uses the TGT to request access to a service, and the KDC issues a service ticket.

However, while symmetric encryption is effective, it relies on shared secrets (passwords) and is not suitable for scenarios requiring public key infrastructure (PKI), such as smart card authentication.

#### Asymmetric Encryption with PKINIT

**PKINIT (Public Key Cryptography for Initial Authentication)**: To address this limitation, PKINIT (Public Key Cryptography for Initial Authentication) is an extension of Kerberos that uses asymmetric encryption. Instead of relying on passwords, it uses public-private key pairs for authentication.

**PKINIT Certificate Authentication**: Uses a traditional X.509 certificate and private key pair to authenticate a Kerberos client. The KDC directly validates the certificate.

**PKINIT Key Trust**: Relies on a public key stored in the **msDS-KeyCredentialLink** attribute of an AD object. The KDC authenticates the client by verifying that the public key used in the authentication request matches the one stored in the AD object, without needing a traditional certificate.

Here’s how it works:

1. **AS-REQ with PKINIT:** The client sends a request to the KDC, including a timestamp signed with the client’s private key and the corresponding public key.
2. **Public Key Validation:** The KDC checks the client’s public key against the **msDS-KeyCredentialLink** attribute in Active Directory. Means, instead of directly using the certificate for authentication, the KDC is validating if any of the public keys in the **msDS-KeyCredentialLink** attribute of the user matches the one used in the AS-REQ. If the key is valid, the KDC decrypts the timestamp and verifies the signature.
3. **AS-REP:** If validation is successful, the KDC issues a TGT to the client.

Consequently*,* Among various lateral movement and persistence techniques, the **Shadow Credentials attack** has become a significant concern for AD security analysts due to its covert nature and minimal visibility on traditional SIEM tools.

#### The msDS-KeyCredentialLink Attribute

In simple terms, PKINIT introduces the **msDS-KeyCredentialLink** attribute in Windows Server 2016 to store public keys for authentication. This attribute is crucial for certificate-based authentication, and here are its key details:

1. The **msDS-KeyCredentialLink** is a multi-value attribute, meaning multiple public keys can be stored for a single account, often representing different devices linked to that account.
2. Each value in this attribute contains serialized objects called Key Credentials. These objects include:

* + Creation date
  + Distinguished name of the owner
  + A GUID representing a Device ID
  + The public key itself

3. During PKINIT authentication, the client’s public key is verified against the values stored in this attribute. If a match is found, the KDC proceeds with authentication.
4. *Therefore*, managing and modifying the **msDS-KeyCredentialLink** attribute is an action that requires specific permissions, typically held by accounts that are members of highly privileged groups.

##### **These groups include:**

**Key Admins:**

Members of this group can perform administrative actions on key objects within the domain. The Key Admins group applies to the Windows Server operating system in Default Active Directory security groups.

**Enterprise Key...