---
title: Wind River Software VxWorks 6.9 Weak Password Hashing Algorithms
url: https://cxsecurity.com/issue/WLB-2025010028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-29
fetch_date: 2025-10-06T20:05:02.431393
---

# Wind River Software VxWorks 6.9 Weak Password Hashing Algorithms

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Wind River Software VxWorks 6.9 Weak Password Hashing Algorithms** **2025.01.28**  Credit:  **[Steffen Robertz](https://cxsecurity.com/author/Steffen%2BRobertz/1/)**  Risk: **Low**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Wind River Software VxWorks 6.9 Weak Password Hashing Algorithms
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
(https://cheatsheetseries.owasp.org/cheatsheets/Password\_Storage\_Cheat\_Sheet.html#pbkdf2).
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
(https://cheatsheetseries.owasp.org/cheatsheets/Password\_Storage\_Cheat\_Sheet.html#pbkdf2).
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
def format\_pw\_vx69\_hashcat(pw\_hash\_base64,salt\_base64):
# formats hash for cracking with hashcat hash type 1420 "sha256($salt.$pass)" and the --hex-salt option
hash = b64decode(pw\_hash\_base64)
salt = b64decode(salt\_base64)
print('%s:%s'%(hash.hex(),salt.hex()))
def hash\_pw\_vx69(password, salt\_base64):
salt = b64decode(salt\_base64)
hash\_input = salt + password.encode()
digest = sha256(hash\_input).digest()
digest\_base64 = b64encode(digest).decode()
return digest\_base64
salt = 'BFqADK/VLEk='
pw\_hash = 'm4qJ/O/Iam+2AdBmwD7+cav+W6HABSdMF2yQyK+rIQA='
format\_pw\_vx69\_hashcat(pw\_hash,salt)
if hash\_pw\_vx69('password', salt) == pw\_hash:
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
based o...