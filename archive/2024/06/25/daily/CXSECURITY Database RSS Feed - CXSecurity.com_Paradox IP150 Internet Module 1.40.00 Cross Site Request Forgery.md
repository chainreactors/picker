---
title: Paradox IP150 Internet Module 1.40.00 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2024060054
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-25
fetch_date: 2025-10-06T16:54:43.089200
---

# Paradox IP150 Internet Module 1.40.00 Cross Site Request Forgery

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
|  |  | |  | | --- | | **Paradox IP150 Internet Module 1.40.00 Cross Site Request Forgery** **2024.06.24**  Credit:  **[Jakob Pachmann](https://cxsecurity.com/author/Jakob%2BPachmann/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-5676](https://cxsecurity.com/cveshow/CVE-2024-5676/ "Click to see CVE-2024-5676")**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256
# Paradox IP150 Internet Module Cross-Site Request Forgery #
Link: https://github.com/sbaresearch/advisories/tree/public/2024/SBA-ADV-20240321-01\_Paradox\_Cross\_Site\_Request\_Forgery
## Vulnerability Overview ##
The Paradox IP150 Internet Module in version 1.40.00 is vulnerable to
Cross-Site Request Forgery (CSRF) attacks due to
a lack of countermeasures and the use of the HTTP method `GET` to introduce
changes in the system.
\* \*\*Identifier\*\* : SBA-ADV-20240321-01
\* \*\*Type of Vulnerability\*\* : Cross-Site Request Forgery (CSRF)
\* \*\*Software/Product Name\*\* : [IP150 Internet Module](https://www.paradox.com/Products/default.asp?CATID=3&SUBCATID=38&PRD=563)
\* \*\*Vendor\*\* : [Paradox Security Systems (Bahamas) Ltd.](https://www.paradox.com/)
\* \*\*Affected Versions\*\* : 1.40.00 (possibly others too)
\* \*\*Fixed in Version\*\* : Not yet
\* \*\*CVE ID\*\* : CVE-2024-5676
\* \*\*CVSS Vector\*\* : CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:H/A:H
\* \*\*CVSS Base Score\*\* : 6.8 (Medium)
## Vendor Description ##
> IP150
> Internet Module
> Supports SWAN Server
>
> Features
>
> \* Controls and monitors a control panel through an IP network (LAN / WAN / Internet)
> \* Reports control panel events via IP to the Paradox IPR512 GPRS / IP Monitoring Receiver and / or IPRS-7 GPRS / IP PC Receiver Software
> \* Two I/Os on board; controlled via the web interface, triggering an email
> \* Sends notification and alarm system events via email
> \* Arm / Disarm individual partitions via Insite GOLD app
> \* Connects to Swan for easy installation (no port forwarding)
> \* Enables Insite GOLD, or BabyWare to access your system through the Internet
> \* Push notification to Insite GOLD app
> \* HTTPS support for improving security (HyperText Transfer Protocol Secure; a widely used communications protocol for secure communication over a computer network)
> \* Very low bandwidth consumption
> \* Easy installation; built-in clip for mounting in a metal box
> \* Supported language: English
> \* Compatible with EVO Series, Spectra SP Series, MG5000, MG5050 and MG5075
Source: <https://www.paradox.com/Products/default.asp?PID=404>
## Impact ##
An attacker can coerce an administrator into clicking a link, which issues
a HTTP request that changes the state of the system.
Depending on the configuration, meaning which downstream component is
controlled by the affected component, the impact will be different.
As an example the \*IP150 Internet Module\* might control an alarm unit.
Thus an attacker can deactivate the alarm by performing a CSRF attack.
## Vulnerability Description ##
The server cannot verify whether a request was sent intentionally. This
makes it possible for an attacker to trick a client into making
unintentional requests to the web server which will be treated as an
authentic request. In combination with a social engineering attack,
this allows an attacker to perform server-side actions as the victim.
In addition, the functionality of activation and deactivation of the alarm
systems, is accessed via a HTTP `GET` request.
Changing the state of the server with `GET` is discouraged in the HTTP
standard, since it is defined to be a \*safe\* method [1].
This makes the exploitation of the vulnerability easier, as an attacker
can craft an URL.
If the victim opens this URL, the CSRF attack is carried out and an action
is performed.
## Proof of Concept ##
For example, the following HTTP request disables the alarm in area `00`:
```http
GET /statuslive.html?area=00&value=d HTTP/1.1
Host: 192.0.2.1
```
It is vulnerable to CSRF, since it does not apply any CSRF countermeasures.
Therefore, it is possible to craft an URL that performs this action:
```text
http://192.0.2.1/statuslive.html?area=00&value=d
```
## Recommended Countermeasures ##
We are not aware of a vendor fix yet. Please contact the vendor.
A generally valid solution against CSRF, which however requires a server-side
state, is the implementation of an unpredictable token that is unique for
each session.
The OWASP project gives further recommendations [2] [3].
## Timeline ##
\* `2024-02-09` Identified the vulnerability in version 1.40.00
\* `2024-02-12` First contact to the system owner to acquire more information about the system configuration and version
\* `2024-03-08` System owner provided all details on the affected system
\* `2024-03-21` First attempt to contact vendor via support email
\* `2024-04-03` Second attempt to contact vendor via web form and support email
\* `2024-06-19` No reaction from vendor to all previous contact attempts
\* `2024-06-19` SBA Research assigned CVE-2024-5676
\* `2024-06-19` Public disclosure
## References ##
1. RFC 7231. HTTP/1.1 Semantics and Content. Safe Methods: <https://datatracker.ietf.org/doc/html/rfc7231#section-4.2.1>
2. OWASP Cheat Sheet Series. Cross-Site Request Forgery Prevention Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html>
3. OWASP Web Security Testing Guide (WSTG) v4.2. Testing for Cross Site Request Forgery: <https://owasp.org/www-project-web-security-testing-guide/v42/4-Web\_Application\_Security\_Testing/06-Session\_Management\_Testing/05-Testing\_for\_Cross\_Site\_Request\_Forgery.html>
## Credits ##
\* Jakob Pachmann ([SBA Research](https://www.sba-research.org/))
\* Fabian Funder ([SBA Research](https://www.sba-research.org/))
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCAAdFiEEL9Wp/yZWFD9OpIt6+7iGL1j3dbIFAmZyq50ACgkQ+7iGL1j3
dbIISw/8CO95qAHA1sNw43g7j202gLt4zyIRHAjowX1btaOb5SwEPKgZCMa+Trnz
fF/Ck5opN/Y8QvKE4C75TJVXVZBja4cTWeNa0bqXXNlvGsUB/9y5N2d7NTAN+CLc
ew61aTFrudgjHL...