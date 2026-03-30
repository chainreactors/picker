---
title: Dovecot Security Advisory OXDC-2026-0001
url: https://seclists.org/fulldisclosure/2026/Mar/13
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:47:00.313135
---

# Dovecot Security Advisory OXDC-2026-0001

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# Dovecot Security Advisory OXDC-2026-0001

---

*From*: Aki Tuomi <aki.tuomi () dovecot fi>
*Date*: Fri, 27 Mar 2026 10:06:15 +0200 (EET)

---

```
Dear subscribers,

we're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. This advisory is also published at
https://documentation.open-xchange.com/dovecot/security/advisories/html/2026/oxdc-adv-2026-0001.html

---

Classification: TLP:GREEN

Internal reference: DOV-7830
Type: CWE-1250 (Improper Preservation of Consistency Between Independent Representations of Shared State)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.1.0, OX Dovecot CE core 2.4.0
First fixed revision: OX Dovecot CE core 2.4.1
Discovery date: 2025-07-24
Solution date: 2026-03-27
Disclosure date: 2026-03-27
Researcher credits: Erik  <erik () broadlux com>
CVE: CVE-2025-30189
CVSS: 7.4 (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N)

Details:
v2.4 regression: auth cache broken with several passdb / userdb. When cache is enabled, some passdb/userdb drivers
incorrectly cache all users with same cache key, causing wrong cached information to be used for these users.

Risk:
After cached login, all subsequent logins are for same user. No publicly available exploits are known.

Solution:
Install fixed version or disable caching either globally or for the impacted passdb/userdb drivers.

---

Internal reference: DOV-8349
Type: CWE-20 (Improper Input Validation)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.1.0, OX Dovecot CE core 2.4.0
First fixed revision: OX Dovecot Pro core 3.1.2, OX Dovecot CE core 2.4.3
Discovery date: 2025-11-04
Solution date: 2026-03-27
Disclosure date: 2026-03-27
CVE: CVE-2025-59028
CVSS: 5.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L)

Details:
Invalid base64 authentication can cause DoS for other logins. When sending invalid base64 SASL data, login process is
disconnected from the auth server, causing all active authentication sessions to fail.

Risk:
Invalid BASE64 data can be used to DoS a vulnerable server to break concurrent logins. No publicly available exploits
are known.

Solution:
Install fixed version or disable concurrency in login processes (heavy perfomance penalty on large deployments).

---

Internal reference: DOV-8508
Type: CWE-20 (Improper Input Validation)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.1.0, OX Dovecot CE core 2.4.0
First fixed revision: OX Dovecot CE core 2.4.3, OX Dovecot Pro core 3.1.3
Discovery date: 2025-11-29
Solution date: 2026-03-27
Disclosure date: 2026-03-27
CVE: CVE-2025-59032
CVSS: 7.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)

Details:
v2.4/v3.1 regression: Pigeonhole: ManageSieve panic occurs with sieve-connect as a client. ManageSieve AUTHENTICATE
command crashes when using literal as SASL initial response.

Risk:
This can be used to crash ManageSieve service repeatedly, making it unavailable for other users. No publicly available
exploits are known.

Solution:
Control access to ManageSieve port, or disable the service if it's not needed. Alternatively upgrade to a fixed version.

---

Internal reference: DOV-8584
Type: CWE-200 (Exposure of Sensitive Information to an Unauthorized Actor)
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 2.3.0
First fixed revision: OX Dovecot CE core 2.4.3, OX Dovecot Pro core 3.1.3, OX Dovecot Pro core 2.3.22.1
Discovery date: 2025-12-29
Solution date: 2026-03-27
Disclosure date: 2026-03-27
Researcher credits: cavid@yeswehack
CVE: CVE-2025-59031
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

Details:
decode2text.sh OOXML extraction may follow symlinks and read unintended files during indexing. Dovecot has provided a
script to use for attachment to text conversion. This script unsafely handles zip-style attachments.

Risk:
Attacker can use specially crafted OOXML documents to cause unintended files on the system to be indexed and
subsequently ending up in FTS indexes. No publicly available exploits are known.

Solution:
Do not use the provided script, instead, use something else like FTS tika.

---

Internal reference: DOV-8591
Type: CWE-22 (Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'))
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 2.3.0
First fixed revision: OX Dovecot Pro core 3.1.0, OX Dovecot CE core 2.4.0
Discovery date: 2026-01-07
Solution date: 2026-03-27
Disclosure date: 2026-03-27
Researcher credits: strokep@yeswehack
CVE: CVE-2026-0394
CVSS: 5.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)

Details:
auth: Path traversal in passwd-file passdb using `%d` (domain) escapes base directory and opens `/etc/passwd`Pre-auth
path traversal in passwd-file passdb using `%d` (domain) escapes base directory and opens `/etc/passwd`. When dovecot
has been configured to use per-domain passwd files, and they are placed one path component above /etc, or slash has
been added to allowed characters, path traversal can happen if the domain component is directory partial.

Risk:
This allows inadvertently reading /etc/passwd (or some other path which ends with passwd). If this file contains
passwords, it can be used to authenticate wrongly, or if this is userdb, it can unexpectly make system users appear
valid users.  No publicly available exploits are known.

Solution:
Upgrade to fixed version, or use different authentication scheme that does not rely on paths. Alternatively you can
also ensure that the per-domain passwd files are in some other location, such as /etc/dovecot/auth/%d.

---

Internal reference: DOV-8775
Type: CWE-90 (Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection'))
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.1.0, OX Dovecot CE core 2.4.0
First fixed revision: OX Dovecot CE core 2.4.3, OX Dovecot Pro core 3.1.4
Discovery date: 2026-02-20
Solution date: 2026-03-27
Disclosure date: 2026-03-27
Researcher credits: cookiejack15@yeswehack
CVE: CVE-2026-27860
CVSS: 3.7 (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N)

Details:
v2.4/v3.1 regression: auth-ldap is not escaping usernames. If auth_username_chars is empty, it is possible to inject
arbitrary LDAP filter to Dovecot's LDAP authentication.

Risk:
This leads to potentially bypassing restrictions and allows probing of LDAP structure. No publicly available exploits
are known.

Solution:
Do not clear out auth_username_chars, or install fixed version.

---

Internal reference: DOV-8781
Type: CWE-89 (Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'))
Component: core
Report confidence: Confirmed
Solution status: Fixed by vendor
Last affected revision: OX Dovecot Pro core 3.1.0, OX Dovecot CE core 2.4.0
First fixed revision: OX Dovecot CE core 2.4.3, OX Dovecot Pro core 3.1.4
Discovery date:...