---
title: 17 vulnerabilities in Sharp Multi-Function Printers
url: https://seclists.org/fulldisclosure/2024/Jul/0
source: Full Disclosure
date: 2024-07-05
fetch_date: 2025-10-06T17:51:43.303685
---

# 17 vulnerabilities in Sharp Multi-Function Printers

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

# 17 vulnerabilities in Sharp Multi-Function Printers

---

*From*: Pierre Kim <pierre.kim.sec () gmail com>
*Date*: Thu, 27 Jun 2024 16:09:17 -0400

---

```
Hello,

Please find a text-only version below sent to security mailing lists.

The complete version on "17 vulnerabilities in Sharp Multi-Function
Printers" is posted here:
  https://pierrekim.github.io/blog/2024-06-27-sharp-mfp-17-vulnerabilities.html

The text version is also posted here:
  https://pierrekim.github.io/advisories/2024-sharp-mfp.txt

=== text-version of the advisory  ===

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

## Advisory Information

Title: 17 vulnerabilities in Sharp Multi-Function Printers
Advisory URL: https://pierrekim.github.io/advisories/2024-sharp-mfp.txt
Blog URL: https://pierrekim.github.io/blog/2024-06-27-sharp-mfp-17-vulnerabilities.html
Date published: 2024-06-27
Vendors contacted: JPCERT
Release mode: Released
CVE: CVE-2024-28038, CVE-2024-36251, CVE-2024-28955, CVE-2024-29146,
CVE-2024-29978, CVE-2024-32151, CVE-2024-33605, CVE-2024-33610,
CVE-2024-33610, CVE-2024-35244, CVE-2024-33616, CVE-2024-34162,
CVE-2024-36248

## Product description
```

> ```
> Multifunction printers offer more than just print. These devices integrate the power of a printer, photocopier and
> scanner into one single device.
>
> From https://www.sharp.co.uk/printers-photocopiers/explore-sharp-printers/sharp-multifunction-printers
> ```

```
## Vulnerability Summary

Vulnerable versions: 308 different models of Sharp Multi-Function
Printers (MFP) are vulnerable. It is recommended to visit the official
Sharp advisory (https://global.sharp/products/copier/info/info_security_2024-05.html)
and apply security patches and replace unsupported Multi-Function
Printers (MFP) models.

The summary of the vulnerabilities is as follows:

1. CVE-2024-28038 - Memory corruption in the main program - Remote
Code Execution against the web server without authentication
2. CVE-2024-36251 - Invalid (0x000000d0) pointer dereference - Remote
DoS without authentication
3. CVE-2024-28955, CVE-2024-29146, CVE-2024-29978, CVE-2024-32151 -
World-readable coredump files and insecure storage of credentials
4. CVE-2024-33605 - Arbitrary Directory Listing without authentication
5. non-assigned CVE vulnerability - Local File Inclusion allowing to
read any file (e.g. Coredump files) without authentication
5.1 Generation of the coredump file on the printer
5.2 Local File Inclusion of the coredump file
5.3 Retrieve of credentials using the coredump files
5.4 Retrieve of credentials using configuration files
6. CVE-2024-33610 - Backdoor webpage - Listing of session cookies
without authentication
7. non-assigned CVE vulnerability - Configuration webpages reachable
without authentication
8. CVE-2024-33610 - Reboot without authentication - Remote DoS
9. CVE-2024-35244 - Backdoor access - Service
10. non-assigned CVE vulnerability - Backdoor access - FSS User
11. non-assigned CVE vulnerability - Insecure default credentials
12. CVE-2024-33616 - Read admin access on telnet
13. non-assigned CVE vulnerability - XSS on all the Sharp printers (login.html)
14. non-assigned CVE vulnerability - XSS on all the Sharp printers
(all other HTML pages)
15. CVE-2024-34162 - Exfiltration of LDAP credentials by downgrading
the security
16. CVE-2024-36248 - Hardcoded Google API Keys
17. non-assigned CVE vulnerability - Hardcoded Amazon API Keys
18. N-day CVE-2022-45796 - Remote Code Execution

TL;DR: An attacker can compromise Sharp Multi-Function Printers using
multiple vulnerabilities.

List of vulnerable models of Sharp Multi-Function Printers (308 models):

    BP-30C25, BP-30C25T, BP-30C25Y, BP-30C25Z, BP-30M35, BP-30M31,
BP-30M28, BP-30M35T, BP-30M31T, BP-30M28T,
    BP-50C36, BP-50C31, BP-50C26, BP-50C65, BP-50C55, BP-50C45,
BP-50M36, BP-50M31, BP-50M26, BP-50M55,
    BP-50M50, BP-50M45, BP-55C26, BP-60C45, BP-60C36, BP-60C31,
BP-70C36, BP-70C31, BP-70C65, BP-70C55,
    BP-70C45, BP-70M36, BP-70M31, BP-70M65, BP-70M55, BP-70M45,
BP-90C70, BP-90C80, BP-B547WD, BP-B537WR,
    BP-B550WD, BP-B540WR, BP-70M90, BP-70M75, MX-M1205, MX-M1055,
DX-2500N, DX-2000U, MX-2010U, MX-1810U,
    MX-2314N, MX-2314NR, MX-2630N, MX-3050N A, MX-3050V A, MX-3100N,
MX-3100G, MX-2600N, MX-2600G, MX-3101N,
    MX-2601N, MX-2301N, MX-3111U, MX-2310U, MX-2310R, MX-3115N,
MX-2615N, MX-2615 A, MX-3116N, MX-2616N,
    MX-3551, MX-3051, MX-2651, MX-3570N, MX-3070N, MX-3570V, MX-3070V,
MX-3571, MX-3071, MX-3571S,
    MX-3071S, MX-3610N, MX-3110N, MX-2610N, MX-3110N A, MX-3610NR,
MX-3640N, MX-3140N, MX-2640N, MX-3140N A,
    MX-3640NR, MX-3140NR, MX-2640NR, MX-4050N, MX-3550N, MX-3050N,
MX-4050V, MX-3550V, MX-3050V, MX-4060N,
    MX-3560N, MX-3060N, MX-4060V, MX-3560V, MX-3060V, MX-4061,
MX-3561, MX-3061, MX-4061S, MX-3561S,
    MX-3061S, MX-5001N, MX-5000N, MX-4101N, MX-4100N, MX-5112N,
MX-5111N, MX-5110N, MX-4112N, MX-4111N,
    MX-4110N, MX-5141N A, MX-4140N A, MX-5141N, MX-5140N, MX-4141N,
MX-4140N, MX-6050N, MX-5050N, MX-6050V,
    MX-5050V, MX-6051, MX-5051, MX-4051, MX-6070N A, MX-4070N A,
MX-3070N A, MX-6070N, MX-5070N, MX-4070N,
    MX-6070V A, MX-4070V A, MX-3070V A, MX-6070V, MX-5070V, MX-4070V,
MX-6071, MX-5071, MX-4071, MX-6071S,
    MX-5071S, MX-4071S, MX-7040N, MX-6240N, MX-7500N, MX-6500N,
MX-7580N, MX-6580N, MX-8081, MX-7081,
    MX-8090N, MX-7090N, MX-B400P, MX-B380P, MX-B401, MX-B381, MX-B402,
MX-B382, MX-B402P, MX-B382P,
    MX-B402SC, MX-B382SC, MX-B455W, MX-B355W, MX-B455WT, MX-B355WT,
MX-B455WZ, MX-B355WZ, MX-B456WH, MX-B356WH,
    MX-B456W, MX-B356W, MX-B476WH, MX-B376WH, MX-B476W, MX-B376W,
MX-C301W, MX-C301, MX-C304, MX-C303,
    MX-C304WH, MX-C303WH, MX-C304W, MX-C303W, MX-C312, MX-C311,
DX-C311, DX-C311J, MX-C310, DX-C310,
    MX-C381, DX-C381, MX-C380, MX-C381B, MX-C400P, MX-C380P, MX-C401,
DX-C401, DX-C401 J, MX-C400,
    DX-C400, MX-C402SC, MX-C382SC, MX-C382SCB, MX-M1204, MX-M1054,
MX-M904, MX-M1206, MX-M1056, MX-M2630,
    MX-M2630 A, MX-M266N, MX-M265N, MX-M265U, MX-M266NV, MX-M265NV,
MX-M265UV, MX-M3050 A, MX-M314NV, MX-M264NV,
    MX-M315NE, MX-M265NE, MX-M315NE, MX-M265NE, MX-M315V, MX-M265V,
MX-M354N, MX-M314N, MX-M264N, MX-M354NR,
    MX-M314NR, MX-M264NR, MX-M354U, MX-M314U, MX-M264U, MX-M3550,
MX-M3050, MX-M3551, MX-M3051, MX-M2651,
    MX-M356N, MX-M316N, MX-M315N, MX-M356U, MX-M315U, MX-M356NV,
MX-M316NV, MX-M315NV, MX-M356UV, MX-M315UV,
    MX-M3570, MX-M3070, MX-M3571, MX-M3071, MX-M3571S, MX-M3071S,
MX-M465N A, MX-M365N A, MX-M503N, MX-M453N,
    MX-M363N, MX-M283N, MX-M503U, MX-M453U, MX-M363U, MX-M564N,
MX-M464N, MX-M364N, MX-M564N A, MX-M565N,
    MX-M465N, MX-M365N, MX-M6050, MX-M5050, MX-M4050, MX-M6051,
MX-M5051, MX-M4051, MX-M6070 A, MX-M4070 A,
    MX-M3070 A, MX-M6070, MX-M5070, MX-M4070, MX-M6071, MX-M5071,
MX-M4071, MX-M6071S, MX-M5071S, MX-M4071S,
    MX-M753N, MX-M753U, MX-M623N, MX-M623U, MX-M754N, MX-M654N,
MX-M754N A, MX-M654N A, MX-M7570, MX-M6570,
    MX-M905.

_Miscellaneous notes_:

This security assessment was entirely done using a blackbox approach
and fully-remote - I only had some IPs of printers (no physical access
and no credentials for admin or normal users). Consequently, the
physical security of the printers was not analyzed and the
vulnerabilities wer...