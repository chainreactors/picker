---
title: Sharp Multi-Function Printer 18 Vulnerabilities
url: https://cxsecurity.com/issue/WLB-2024070007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-05
fetch_date: 2025-10-06T17:38:32.478530
---

# Sharp Multi-Function Printer 18 Vulnerabilities

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
|  |  | |  | | --- | | **Sharp Multi-Function Printer 18 Vulnerabilities** **2024.07.04**  Credit:  **[Pierre Kim](https://cxsecurity.com/author/Pierre%2BKim/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-29146](https://cxsecurity.com/cveshow/CVE-2024-29146/ "Click to see CVE-2024-29146")** | **[CVE-2024-33610](https://cxsecurity.com/cveshow/CVE-2024-33610/ "Click to see CVE-2024-33610")** | **[CVE-2024-34162](https://cxsecurity.com/cveshow/CVE-2024-34162/ "Click to see CVE-2024-34162")** | **[CVE-2024-36248](https://cxsecurity.com/cveshow/CVE-2024-36248/ "Click to see CVE-2024-36248")** | **[CVE-2024-28038](https://cxsecurity.com/cveshow/CVE-2024-28038/ "Click to see CVE-2024-28038")** | **[CVE-2024-36251](https://cxsecurity.com/cveshow/CVE-2024-36251/ "Click to see CVE-2024-36251")** | **[CVE-2024-32151](https://cxsecurity.com/cveshow/CVE-2024-32151/ "Click to see CVE-2024-32151")** | **[CVE-2024-33605](https://cxsecurity.com/cveshow/CVE-2024-33605/ "Click to see CVE-2024-33605")** | **[CVE-2024-35244](https://cxsecurity.com/cveshow/CVE-2024-35244/ "Click to see CVE-2024-35244")** | **[CVE-2024-33616](https://cxsecurity.com/cveshow/CVE-2024-33616/ "Click to see CVE-2024-33616")** | **[CVE-2022-45796](https://cxsecurity.com/cveshow/CVE-2022-45796/ "Click to see CVE-2022-45796")**  CWE: **N/A** | |

Hello,
Please find a text-only version below sent to security mailing lists.
The complete version on "17 vulnerabilities in Sharp Multi-Function
Printers" is posted here:
https://pierrekim.github.io/blog/2024-06-27-sharp-mfp-17-vulnerabilities.html
The text version is also posted here:
https://pierrekim.github.io/advisories/2024-sharp-mfp.txt
=== text-version of the advisory ===
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
> Multifunction printers offer more than just print. These devices integrate the power of a printer, photocopier and scanner into one single device.
>
> From https://www.sharp.co.uk/printers-photocopiers/explore-sharp-printers/sharp-multifunction-printers
## Vulnerability Summary
Vulnerable versions: 308 different models of Sharp Multi-Function
Printers (MFP) are vulnerable. It is recommended to visit the official
Sharp advisory (https://global.sharp/products/copier/info/info\_security\_2024-05.html)
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
MX-5050V...