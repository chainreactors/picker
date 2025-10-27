---
title: 32 vulnerabilities in IBM Security Verify Access
url: https://seclists.org/fulldisclosure/2024/Nov/0
source: Full Disclosure
date: 2024-11-04
fetch_date: 2025-10-06T19:15:46.720994
---

# 32 vulnerabilities in IBM Security Verify Access

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# 32 vulnerabilities in IBM Security Verify Access

---

*From*: Pierre Kim <pierre.kim.sec () gmail com>
*Date*: Fri, 1 Nov 2024 15:24:26 -0400

---

```
Hello,

Please find a text-only version below sent to security mailing lists.

The complete version on "32 vulnerabilities in IBM Security Verify
Access" is posted here:
  https://pierrekim.github.io/blog/2024-11-01-ibm-security-verify-access-32-vulnerabilities.html

The text version is also posted here:
  https://pierrekim.github.io/advisories/2024-ibm-security-verify-access.txt

=== text-version of the advisory  ===

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

## Advisory Information

Title: 32 vulnerabilities in IBM Security Verify Access
Advisory URL: https://pierrekim.github.io/advisories/2024-ibm-security-verify-access.txt
Blog URL: https://pierrekim.github.io/blog/2024-11-01-ibm-security-verify-access-32-vulnerabilities.html
Date published: 2024-11-01
Vendors contacted: IBM
Release mode: Released
CVE: CVE-2022-2068, CVE-2023-30997, CVE-2023-30998, CVE-2023-31001,
CVE-2023-31004, CVE-2023-31005, CVE-2023-31006, CVE-2023-32328,
CVE-2023-32329, CVE-2023-32330, CVE-2023-38267, CVE-2023-38267,
CVE-2023-38368, CVE-2023-38369, CVE-2023-38370, CVE-2023-43017,
CVE-2024-25027, CVE-2024-35137, CVE-2024-35139, CVE-2024-35140,
CVE-2024-35141, CVE-2024-35142

## Product description
```

> ```
> IBM Security Verify Access is a complete authorization and network security policy management solution. It provides
> end-to-end protection of resources over geographically dispersed intranets and extranets.
> In addition to state-of-the-art security policy management, IBM Security Verify Access provides authentication,
> authorization, data security, and centralized resource management capabilities.
>
> IBM Security Verify Access offers the following features:
>
> - Authentication
>
> Provides a wide range of built-in authenticators and supports external authenticators.
>
> - Authorization
>
> Provides permit and deny decisions for protected resources requests in the secure domain through the authorization
> API.
>
> - Data security and centralized resource management
>
> Manages secure access to private internal network-based resources by using the public Internet's broad connectivity
> and ease of use with a corporate firewall system.
>
> From https://www.ibm.com/docs/en/sva/10.0.8?topic=overview-introduction-security-verify-access
> ```

```
## Vulnerability Summary

Vulnerable versions: IBM Security Verify Access < 10.0.8.

The summary of the vulnerabilities is as follows:

1. non-assigned CVE vulnerability - Authentication Bypass on IBM
Security Verify Runtime
2. CVE-2024-25027 - Reuse of snapshot private keys
3. CVE-2023-30997 - Local Privilege Escalation using OpenLDAP
4. CVE-2023-30998 - Local Privilege Escalation using rpm
5. CVE-2023-38267, CVE-2024-35141, CVE-2024-35142 - Insecure setuid
binaries and multiple Local Privilege Escalation in IBM codes
5.1. CVE-2023-38267 - Local Privilege Escalation using mesa_config -
import of a new snapshot
5.2. CVE-2024-35141 - Local Privilege Escalation using mesa_config -
command injections
5.3. CVE-2023-38267 - Local Privilege Escalation using mesa_cli -
import of a new snapshot
5.4. CVE-2024-35142 - Local Privilege Escalation using mesa_cli -
telnet escape shell
6. CVE-2022-2068 - Outdated OpenSSL
7. CVE-2023-43017 - PermitRootLogin set to yes
8. CVE-2024-35137 and CVE-2024-35139 - Lack of password for the `cluster` user
9. CVE-2023-38368 - Non-standard way of storing hashes and
world-readable files containing hashes
10. CVE-2023-38369 - Hardcoded PKCS#12 files
11. CVE-2023-31001 - Incorrect permissions in verify-access-dsc (race
condition and leak of private key
12. non-assigned CVE vulnerability - Insecure health_check.sh script
in verify-access (race condition and leak of private key)
13. CVE-2024-35140 - Local Privilege Escalation due to insecure
health_check.sh script in verify-access (insecure SSL, insecure files)
14. CVE-2024-35140 (duplicate?) - Local Privilege Escalation due to
insecure health_check.sh script in verify-access-dsc (insecure SSL,
insecure file)
15. CVE-2023-31004 - Remote Code Execution due to insecure download of
snapshot in verify-access-dsc, verify-access-runtime and
verify-access-wrp
16. CVE-2023-31005 - Lack of authentication in Postgres inside
verify-access-runtime
17. CVE-2023-31006 - Null pointer dereference in dscd - Remote DoS
against DSC instances
18. CVE-2023-32327 - XML External Entity (XXE) in dscd
19. CVE-2023-38370 - Remote Code Execution due to insecure download of
rpm and zip files in verify-access-dsc, verify-access-runtime and
verify-access-wrp (/usr/sbin/install_isva.sh)
20. non-assigned CVE vulnerability - Remote Code Execution due to
insecure download of rpm in verify-access-runtime
(/usr/sbin/install_java_liberty.sh)
21. CVE-2023-32328 - Remote Code Execution due to insecure Repository
configuration
22. CVE-2023-32329 - Additional repository configuration (potential
supply-chain attack)
23. non-assigned CVE vulnerability - Remote Code Execution due to
insecure /usr/sbin/install_system.sh script in verify-access-runtime
24. CVE-2023-32330 - Remote Code Execution due to insecure reload
script in verify-access-runtime
25. CVE-2023-32330 (duplicate?) - Remote Code Execution due to
insecure reload script in verify-access-wrp
26. non-assigned CVE vulnerability - Hardcoded private key for IBM ISS
(ibmcom/verify-access)
27. non-assigned CVE vulnerability - dcatool using an outdated OpenSSL
library (ibmcom/verify-access)
28. non-assigned CVE vulnerability - iss-lum using an outdated OpenSSL
library (ibmcom/verify-access) and hardcoded keys
29. non-assigned CVE vulnerability - Outdated "IBM Crypto for C" library
30. non-assigned CVE vulnerability - Webseald using outdated code with
remotely exploitable vulnerabilities
30.1. Libmodsecurity.so - 1 non-assigned CVE vulnerability
30.2. libtivsec_yamlcpp.so - 4 CVEs
30.3. libtivsec_xml4c.so - outdated Xerces-C library
31. non-assigned CVE vulnerability - Outdated and untrusted CAs used
in the Docker images
32. non-assigned CVE vulnerability - Lack of privilege separation in
Docker instances

TL;DR: An attacker can compromise IBM Security Verify Access using
multiple vulnerabilities (7 RCEs, 1 auth bypass, 8 LPEs and some
additional vulnerabilities).
IBM Security Verify Access is a SSO solution mainly used by banks,
Fortune 500 companies and governmental entities.

_Miscellaneous notes_:

The vulnerabilities were found in October 2022 and were communicated
to IBM at the beginning of 2023. They ultimately were patched at the
end of June 2024 (after 18 months). Requiring 1.5 years to provide
security patches for vulnerabilities found in a SSO solution does not
appear to be in par with current cybersecurity risks and is quite
worrying. Update: Following communications with IBM PSIRT in September
2024 regarding missing CVEs and the publication of this security
advisory, it was confirmed that at least one vulnerability was not yet
patched (a 2017 DoS in libinjection, no CVE).

The vulnerabilities were patched progressively in the 10.0.6, 10.0.7
and 10.0.8 versions. It is unclear if all the non-assigned CVE
vulnerabilities have been patched but ...