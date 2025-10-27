---
title: SEC Consult SA-20250127-0 :: Weak Password Hashing Algorithms in Wind River Software VxWorks RTOS
url: https://seclists.org/fulldisclosure/2025/Jan/10
source: Full Disclosure
date: 2025-01-29
fetch_date: 2025-10-06T20:11:58.254733
---

# SEC Consult SA-20250127-0 :: Weak Password Hashing Algorithms in Wind River Software VxWorks RTOS

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250127-0 :: Weak Password Hashing Algorithms in Wind River Software VxWorks RTOS

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 27 Jan 2025 10:20:43 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20250127-0 >
=======================================================================
               title: Weak Password Hashing Algorithms
             product: Wind River Software VxWorks RTOS
  vulnerable version: >= VxWorks 6.9
       fixed version: not available
          CVE number: no CVE assigned by Wind River
              impact: High
            homepage: https://www.windriver.com/
               found: 2024-03-21
                  by: Steffen Robertz (Office Vienna)
                      Constantin Schieber-Knoebl (Office Vienna)
                      Stefan Viehboeck (Office Vienna)
                      SEC Consult Vulnerability Lab

                      An integrated part of SEC Consult, an Eviden business
                      Europe | Asia

                      https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"VxWorks is a real-time operating system (or RTOS) developed as proprietary
software by Wind River Systems, a subsidiary of Aptiv. First released in 1987,
VxWorks is designed for use in embedded systems requiring real-time,
deterministic performance and in many cases, safety and security certification
for industries such as aerospace, defense, medical devices, industrial equipment,
robotics, energy, transportation, network infrastructure, automotive, and
consumer electronics."

Source: https://www.windriver.com/

Business recommendation:
------------------------
SEC Consult advises affected Wind River VxWorks customers to perform thorough
security reviews of their products to assess whether and how they are impacted
by these vulnerabilities. As a mitigation measure, customers should avoid using
the built-in authentication mechanisms of the VxWorks operating system and
instead implement and use modern password hashing algorithms with a sufficiently
high cost factor.

Vulnerability overview/description:
-----------------------------------
1) VxWorks 6.9 Weak Password Hashing Algorithm (no CVE assigned by Wind River)
The password hashing algorithm introduced in VxWorks 6.9 is considered insecure.
This algorithm employs a single iteration of SHA-256 combined with a salt to hash
user passwords.

This method was intended to replace a previous proprietary hashing algorithm
that was susceptible to collision attacks (CVE-2010-2965). However, even at
the time of its release in 2011, the use of a single iteration for password
hashing was deemed inadequate. For comparison, md5crypt (introduced in 1994)
uses 1,000 iterations, and sha256crypt (introduced in 2008) uses 5,000 iterations.

This hashing algorithm is approximately 600,000 times weaker than current standards
(https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2).

An attacker who extracts user password hashes from a VxWorks-based device can
efficiently crack the passwords using a GPU cracking setup (e.g., hashcat on
RTX 4090). Potential vectors for extracting user hashes include:
- Physical access to the device memory via hardware hacking (e.g. bootloader
  access via UART, dumping of memory chips, JTAG, etc.)
- Remote access to device debug interfaces
- Access to firmware update files containing hard-coded users accounts
  (e.g. vendor backdoors added via the loginUserAdd() function)

2) VxWorks 7 Weak Password Hashing Algorithm (no CVE assigned by Wind River)
The password hashing algorithm used in VxWorks 7 (24.04) is also considered
insecure. This algorithm uses 5,000 iterations of SHA-256 combined with a salt
to hash user passwords.

The specific version in which this hashing algorithm was introduced remains
unknown to the authors. Nonetheless, this algorithm is still 5,000 times weaker
than current standards
(https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2).

The same attack vectors mentioned in issue #1 apply here.

Modern embedded systems possess the computational power necessary to perform
secure password hashing. Introducing a new password hashing scheme with a
default cost factor that provides robust defense against GPU cracking is
essential. Additionally, developers should have the flexibility to set a
lower, albeit less secure, cost factor for devices with limited computational
resources.

Proof of concept:
-----------------
1) VxWorks 6.9 Weak Password Hashing Algorithm (no CVE assigned by Wind River)
The password hashes can be cracked using the hashcat hash type 1420 "sha256($salt.$pass)"
and the --hex-salt option.

The following Python script re-implements the hashing algorithm in Python
and demonstrates how hashes can be prepared for cracking with hashcat.

```python
from hashlib import sha256
from base64 import b64decode, b64encode

def format_pw_vx69_hashcat(pw_hash_base64,salt_base64):
    # formats hash for cracking with hashcat hash type 1420 "sha256($salt.$pass)" and the --hex-salt option
    hash = b64decode(pw_hash_base64)
    salt = b64decode(salt_base64)
    print('%s:%s'%(hash.hex(),salt.hex()))

def hash_pw_vx69(password, salt_base64):
    salt = b64decode(salt_base64)

    hash_input = salt + password.encode()

    digest = sha256(hash_input).digest()
    digest_base64 = b64encode(digest).decode()

    return digest_base64

salt = 'BFqADK/VLEk='
pw_hash = 'm4qJ/O/Iam+2AdBmwD7+cav+W6HABSdMF2yQyK+rIQA='

format_pw_vx69_hashcat(pw_hash,salt)

if hash_pw_vx69('password', salt) == pw_hash:
    print('Hashes match!')
```

2) VxWorks 7 Weak Password Hashing Algorithm (no CVE assigned by Wind River)
Cracking these hashes requires the implementation of a hashcat
"sha256($salt.$pass)" variant that uses 5,000 rounds.

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
- VxWorks 6.9 Weak Password Hashing Algorithm was verified on a device
  based on VxWorks 6.9
- VxWorks 7 Weak Password Hashing Algorithm was verified on a device
  based on VxWorks 7 (24.04)

Vendor contact timeline:
------------------------
2024-07-10: Contacting vendor through psirt () windriver com, attaching encrypted
            security advisory. Vendor confirms receipt and is working on it.
2024-07-22: Requesting a status update. Vendor asks for exact version number
            of 6.9 to determine next steps.
2024-07-24: The analyzed device used 6.9.4.12, but stating that all 6.9.x
            versions are affected.
2024-07-25: Vendor wants to discuss further details and requests a meeting.
2024-07-29: Asking for brief summary of initial analysis and timezones.
2024-08-09: Vendor provides a write-up of their current position on these issues.
2024-09-02: Delayed response from our side due to vacation, providing remarks on the
            vendor's statement and proposing a few dates.
2024-09-10: Conference call with vendor, discussing positions and next steps.
2024-09-10: Ven...