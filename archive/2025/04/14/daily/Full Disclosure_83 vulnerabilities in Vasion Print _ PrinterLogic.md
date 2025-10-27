---
title: 83 vulnerabilities in Vasion Print / PrinterLogic
url: https://seclists.org/fulldisclosure/2025/Apr/18
source: Full Disclosure
date: 2025-04-14
fetch_date: 2025-10-06T22:04:44.975436
---

# 83 vulnerabilities in Vasion Print / PrinterLogic

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# 83 vulnerabilities in Vasion Print / PrinterLogic

---

*From*: Pierre Kim <pierre.kim.sec () gmail com>
*Date*: Tue, 8 Apr 2025 13:48:18 -0400

---

```
Hello,

Please find a text-only version below sent to security mailing lists.

The complete version on "83 vulnerabilities in Vasion Print / PrinterLogic"
is posted here:

https://pierrekim.github.io/blog/2025-04-08-vasion-printerlogic-83-vulnerabilities.html

The text version is also posted here:
  https://pierrekim.github.io/advisories/2025-vasion-printerlogic.txt

=== text-version of the advisory  ===

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

## Advisory Information

Title: 83 vulnerabilities in Vasion Print / PrinterLogic
Advisory URL: https://pierrekim.github.io/advisories/2025-vasion-printerlogic.txt
Blog URL: https://pierrekim.github.io/blog/2025-04-08-vasion-printerlogic-83-vulnerabilities.html
Date published: 2025-04-08
Vendors contacted: Vasion
Release mode: Released
CVE: CVE-2025-27637, CVE-2025-27638, CVE-2025-27639, CVE-2025-27641,
CVE-2025-27642, CVE-2025-27643, CVE-2025-27644, CVE-2025-27645,
CVE-2025-27646, CVE-2025-27647, CVE-2025-27648, CVE-2025-27649,
CVE-2025-27650, CVE-2025-27651, CVE-2025-27652, CVE-2025-27653,
CVE-2025-27654, CVE-2025-27655, CVE-2025-27656, CVE-2025-27657,
CVE-2025-27674, CVE-2025-27675, CVE-2025-27676, CVE-2025-27677,
CVE-2025-27678, CVE-2025-27679, CVE-2025-27680, CVE-2025-27681,
CVE-2025-27682, CVE-2025-27683, CVE-2025-27684, CVE-2025-27685

## Product description
```

> ```
> Secure. Scalable. Print Automation That Just Works.
> Eliminate print servers to secure your environment. Leverage the power of AI and automation to streamline print
> processes through one central location. Say goodbye to the frustrations of a traditional print environment and
> welcome a new era of print automation.
>
> Serverless Print Automation with Built-In Flexibility
> Print servers are prone to failure, expensive to maintain, and pose major security risks. Vasion Print's
> cloud-native, centrally-managed direct IP printing architecture eliminates the need for legacy systems, simplifying
> your IT infrastructure and reducing operational costs. By eliminating print servers, your print environment is highly
> available with low maintenance, allowing your business to scale and transform with automation and AI.
> ```

```

```

> ```
> From https://vasion.com/print/
> ```

```
## Vulnerabilities Summary

Vulnerable versions for patched vulnerabilities: Vason Print Virtual
Appliance Host < 25.1.102, Application < 25.1.1413.

Vulnerable versions for unpatched vulnerabilities: all versions.

__I. The summary of the vulnerabilities found in 2021:__

__11 vulnerabilities affecting the MacOS/Linux client__

1. CVE-2025-27685 - Hardcoded Private key for the PrinterLogic CA and
Hardcoded password
2. CVE-2025-27682 - Incorrect permissions in /opt/PrinterInstallerClient/log
3. non-assigned CVE vulnerability - Leak of secrets inside the logs
4. non-assigned CVE vulnerability - Lack of authentication of the
communication between services
5. CVE-2025-27681 - Bypass of admin commands using IPC
6. non-assigned CVE vulnerability - Authentication bypass on the
PrinterInstallerClientService program
7. CVE-2025-27683 - Potential upload of new drivers
8. CVE-2025-27684 - Insecure generation of debug archive
9. CVE-2025-27677 - Arbitrary File Read as root
10. non-assigned CVE vulnerability - Arbitrary File Write as root
11. non-assigned CVE vulnerability - Outdated OpenSSL version

__5 vulnerabilities affecting the Windows client__

12. non-assigned CVE vulnerability - Insecure
PrinterInstallerClientInterface.exe, PrinterInstallerClient.exe and
PrinterInstallClientLauncher.exe
13. CVE-2025-27678 - Local Privilege Escalation with insecure use of
C:\Windows\Temp\PPP\Log
14. non-assigned CVE vulnerability - Local Privilege Escalation with
insecure use of C:\Users\%USER%\AppData\Local\Temp
15. non-assigned CVE vulnerability - Remote Code Execution (Execution
of C:\Program.exe during the installation of a driver)
16. non-assigned CVE vulnerability - Hardcoded Private key for the
PrinterLogic CA and Hardcoded password

__II. The summary of the vulnerabilities found in 2022:__

__33 vulnerabilities affecting the VA and SaaS versions__

17. non-assigned CVE vulnerability - Hardcoded password for the ubuntu user
18. non-assigned CVE vulnerability - Hardcoded SSH server keys
19. non-assigned CVE vulnerability - Insecure communications to
printers and insecure communications to micro-services by disabling
all SSL verifications
20. non-assigned CVE vulnerability - Password for `network` stored in
clear-text inside `/etc/issue`, world-readable
21. CVE-2025-27650 - Hardcoded SSH keys + private SSH keys for
[redacted]@printerlogic.com
22. CVE-2025-27643 - Hardcoded AWS secret key and Presence of CI/CD scripts
23. CVE-2025-27638 - Hardcoded Mailgun credentials
24. CVE-2025-27674 - Hardcoded OKTA Private key
25. non-assigned CVE vulnerability - Lack of firewall between Docker instances
26. non-assigned CVE vulnerability - Insecure access to Docker
instances from the WAN
27. non-assigned CVE vulnerability - Incorrect security architecture
and wrong permissions in /var/www/efs_storage allowing allowing to
compromise the solution
28. non-assigned CVE vulnerability - Outdated, End-Of-Life,
unsupported and vulnerable components (Nginx, libraries, Laravel,
operating systems)
29. non-assigned CVE vulnerability - Processes running as root in
Docker instances
30. CVE-2025-27639 - Creation of administrator cookies using the
credentials of regular users
31. CVE-2025-27637 - XSS in the license generator and weak encryption algorithm
32. CVE-2025-27649 - Incorrect Access Control to PHP webpages allowing
to reach printers
33. CVE-2025-27651 - Pre-authentication Elatec password disclosure,
Change to a malicious Elatec server and Blind-SSRF
34. CVE-2025-27652 - Pre-authenticated SSRF and Change of RFIDeas
35. CVE-2025-27653 - Pre-authenticated Stored XSS in
/var/www/app/console_release/fast_release/register_badge.php
36. CVE-2025-27655 - SSRF everywhere in /var/www/app and compromise of
the SaaS infrastructure
37. CVE-2025-27679 - XSS in /var/www/app/console_release/fast_release/
register_badge_new.php
38. CVE-2025-27676 - XSS in
/www/app/admin/design/reports/overview_popup.php and Incorrect Access
Control
39. CVE-2025-27654 - XSS everywhere in /www/app/admin/*
40. CVE-2025-27657 - Remote Code Executions using eval() - requires
administrator privileges
41. non-assigned CVE vulnerability - Dangerous PHP dead code
42. non-assigned CVE vulnerability - Insecure SSH configuration
43. non-assigned CVE vulnerability - Incorrect encryption algorithms
used to store passwords
44. non-assigned CVE vulnerability - GPG Private key stored in the solution
45. non-assigned CVE vulnerability - Passwords readable and stored in clear-text
46. non-assigned CVE vulnerability - Hardcoded SSL certificate / Private keys
47. CVE-2025-27656 - Samba password available in the process list
48. non-assigned CVE vulnerability - Supply Chain attack against the
PrinterLogic build system
49. CVE-2025-27675 - Vulnerable OpenID implementation

__ 1 vulnerability affecting only the VA version__

50. CVE-2...