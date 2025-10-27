---
title: Sapphire Ticket Attack: Abusing Kerberos Trust
url: https://www.hackingarticles.in/sapphire-ticket-attack-abusing-kerberos-trust/
source: Hacking Articles
date: 2025-04-14
fetch_date: 2025-10-06T22:02:47.245988
---

# Sapphire Ticket Attack: Abusing Kerberos Trust

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
»* [Sapphire Ticket Attack: Abusing Kerberos Trust](https://www.hackingarticles.in/sapphire-ticket-attack-abusing-kerberos-trust/)
»

[Persistence](https://www.hackingarticles.in/category/persistence/)

# Sapphire Ticket Attack: Abusing Kerberos Trust

[April 13, 2025June 19, 2025](https://www.hackingarticles.in/sapphire-ticket-attack-abusing-kerberos-trust/) by [Raj](https://www.hackingarticles.in/author/raj/)

Sapphire Ticket attacks are an advanced form of Kerberos exploitation within Active Directory environments**.** As the use of AD continues to grow, attackers are constantly evolving their techniques to bypass authentication systems. For instance**,** recent developments in this space include both Diamond Ticket and Sapphire Ticket attacks, each allowing adversaries to gain unauthorized access to protected resources in an AD domain.

The Diamond Ticket attack has been well explained in the article *“Diamond Ticket Attack: Abusing Kerberos Trust”* by Komal Singh.

In comparison**,** Sapphire Tickets are the evolution of Diamond Tickets, but stealthier. These are legitimate tickets; however, while the Diamond Ticket modifies the PAC, the Sapphire Ticket instead replaces it with the PAC of another privileged user. In this article**,** we are going to deep dive into how Sapphire Ticket attacks work.

### Table of Contents

**Sapphire Ticket**

**Technical Terminology**

**Lab Setup**

**Exploitation Phase – Sapphire Ticket Attack**

**Method for Exploitation**

* impacket
* nxc
* metasploit

   Conclusion

### Introduction – Sapphire Ticket

A Sapphire ticket functions similarly to a Diamond ticket, as it obtains a legitimate TGT and then copies data from its PAC into the forged ticket. However, the key difference lies in an additional step: instead of relying on the PAC from the initial authentication, the attacker performs a separate process to acquire a PAC for another user—typically one with elevated privileges.

This process involves:

* Authenticating with the KDC
* By leveraging the S4U2Self and U2U extensions, the attacker requests a TGS for a high-privilege user. As a result, the system produces a PAC that reflects the real user’s authorization data, even though the resulting ticket cannot be used directly in privileged contexts.
* Decrypting the PAC data
* Modifying the forged PAC to match the attributes of the valid TGT
* Encrypting the forged ticket using the krbtgt hash

As with Golden and Diamond tickets, attackers must possess the domain’s krbtgt hash to create a Sapphire ticket. However, unlike those tickets, they do not need theDOMAIN\_SID andDOMAIN\_RID—they instead extract this information directly from the valid TGT.

#### Important technical terminology

**S4U2Self (Service for User to Self)**

The S4U2Self Kerberos extension allows a service to request a service to act on behalf of a user by requesting a service ticket for itself. This ticket includes the user’s authorization data—namely, the Privilege Attribute Certificate (PAC)—which the system then uses to make access control decisions.

To use S4U2Self, the requesting user must have at least one registered Service Principal Name (SPN). This SPN enables the Domain Controller (DC) to encrypt the generated service ticket with the service’s secret key.

**S4U2Self Ticket Request Flow:**

1. The service constructs the PA\_FOR\_USER data structure, specifying the user it wants to impersonate.
2. It sends a KRB\_TGS\_REQ message to the Ticket Granting Service (TGS).
3. The TGS responds with a service ticket containing the user’s PAC, encrypted for the requesting service.

#### U2U (User-to-User Authentication)

User-to-User (U2U) authentication is a Kerberos mechanism that enables a client to request a ticket encrypted with the session key of another user’s Ticket Granting Ticket (TGT)—typically when the server is a user and does not have a long-term key (like on a desktop machine).

U2U Ticket Request Features:

additional-tickets: Includes the TGT of the user acting as the server.

ENC-TKT-IN-SKEY: Instructs the KDC to encrypt the service ticket using the session key from the additional ticket.

The sname field (service name) can point to a user account instead of a traditional service with an SPN.

This allows one user (User B) to securely authenticate to another user (User A), even when User A doesn’t have a stored secret key.

U2U Flow Example:

User A (acting as a server) provides their TGT to User B.

User B sends a KRB\_TGS\_REQ to the KDC, including both User A’s and their own TGTs.

The KDC generates a new session key, encrypting it twice: once with User A’s session key and once with User B’s.

Both users decrypt their part, and now they share a common session key for secure communication.

This eliminates the need for User A to maintain a long-lived master key, making it safer to run services from less secure endpoints like desktops.

### Technical Details

Sapphire Tickets leverage a combination of S4U2Self and U2U to bypass traditional SPN requirements.

Here’s how it works:

* Normally, S4U2Self requires a valid SPN. But by using U2U in tandem, it becomes possible to request S4U2Self tickets without needing an SPN.
* For example, a service configured for Kerberos Constrained Delegation (KCD) might receive an NTLM-authenticated user session. Without a Kerberos service ticket (ST) for the user, the service can’t delegate further.
* In this case, the service sends a KRB\_TGS\_REQ for an ST for the user—to itself—via S4U2Self.
* The resulting ticket includes the user’s PAC, which the service can decrypt using the krbtgt key.
* Once it has the PAC, the service can inject or modify it in an existing TGT, re-encrypt it, and re-sign it with the krbtgt key.

**In short:**

S4U2Self lets the service obtain a ticket on behalf of a user. U2U allows this process without requiring a service key. C...