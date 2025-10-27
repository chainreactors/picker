---
title: secuvera-SA-2024-02: Multiple Persistent Cross-Site Scritping (XSS) flaws in Drupal-Wiki
url: https://seclists.org/fulldisclosure/2024/May/4
source: Full Disclosure
date: 2024-05-07
fetch_date: 2025-10-06T17:19:47.619177
---

# secuvera-SA-2024-02: Multiple Persistent Cross-Site Scritping (XSS) flaws in Drupal-Wiki

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# secuvera-SA-2024-02: Multiple Persistent Cross-Site Scritping (XSS) flaws in Drupal-Wiki

---

*From*: Simon Bieber via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 6 May 2024 10:26:42 +0200 (CEST)

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

secuvera-SA-2024-02: Multiple Persistent Cross-Site Scritping (XSS) flaws in Drupal-Wiki

Affected Products
   Drupal Wiki 8.31
   Drupal Wiki 8.30 (older releases have not been tested)

References
   https://www.secuvera.de/advisories/secuvera-SA-2024-02.txt (used for updates)
   CVE-2024-34481
   CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
   CVSS-B: 6.4 ( CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:P/VC:N/VI:N/VA:N/SC:H/SI:H/SA:N )
   https://drupal-wiki.com/drupal-wiki-update-8-31/ (Vendor 1st Fix Release Notes)

Summary:
   According to the Product Website Drupal-Wiki is an enterprise grade Wiki platform.
   The comment function of a Drupal-Wiki-Page is prone to persistent Cross-Site Scritping
   Attacks (persistent XSS).

Effect:
   A remote attacker that is allowed to edit a wiki page or comment to a wiki page is able to
   execute arbitrary (javascript) code within a victims' browser after the victim has opened
   a wiki page with malicous comments or content.

Example:
        1) XSS in comments to a Wiki Page
        The Following steps are needed to exploit the vulnerability on a Wiki-Page assuming
        that no login is needed to comment on a page.
                1. Go to an arbitrary Wiki-Page.
                2. Click on "submit comment" at the lower end of a Wiki Page
                3. Enter the following into the comment form overlay and click on
        the "save" button:
                   "'><img src=x onError=alert('XSS!')>

        The above code creates a harmless JavaScript alert box whenever the Wiki-Page gets
        loaded.
        2) XSS in captions:
        Open a Wiki-Page, insert a caption with the payload from example 1) and save it.

        3) XSS in image titles
        Open a Wiki-Page, insert an image with the payload from example 1) as title and save it.

Solution
        Update to release 8.31.1 or newer.

Disclosure Timeline:
   2024/03/20 vulnerability discovered
   2024/03/21 vendor contacted to get security contact details
   2024/03/21 vendor replied with contact information
   2024/03/21 vulnerability details sent to security contact
   2024/03/21 vendor confirmed vulnerability, proposed fix in next release update
   2024/03/25 vendor release update containing fix.
   2024/03/27 requested CVE-ID, reworked CVSS, tested fix. First fix not fully remediating
              all issues, contacted vendor again to inform about fix test results.
   2024/03/27 vendor replied confirming and proposed second fix with new update.
              planned publication of the SA for 2024/04/14
   2024/04/14 postponed public release as assign request of cve was not answered yet.
   2024/05/06 CVE was assigned. Public release.

Credits:
   Simon Bieber
   sbieber () secuvera de
   secuvera GmbH
   https://www.secuvera.de

Disclaimer:
    All information is provided without warranty. The intent is to
    provide information to secure infrastructure and/or systems, not
    to be able to attack or damage. Therefore secuvera shall
    not be liable for any direct or indirect damages that might be
    caused by using this information.
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEE6mgEBCu3JYBqmGrgDIJc8mYSY6UFAmY4k7YACgkQDIJc8mYS
Y6Xa1A//cTQ41Wp55MJwjE0t7ABw1RSmPskosPycpMxKgU79LH7xwGLpTaRxd1H9
BiNK/Q/4j5Ad4JtM4TDwb0j7XGj07/Cp+hBcomqKohe7hgVflhZOzUcWKvfQUbQt
1yto71AauEpTz32YebZMxrFJLUXtnJU9pPQnAB5iZOyDT5rsXvEBmCnG6OF1kviy
juXiiR15rZEiiWdW+CaAz3qr07Te0WD1i14IPvE55tuKNwp9LOZr9+Fl3CM2atxs
/LSjgZnTIWODnpnuAD3D2XT5XIj1AK5cEGgg+si4UuYFK/v0nTP4Pytlw2HbS0au
WvAqtiI8YwuhQOYvsXoQ5UYHjZzc2BrQ5mn2MujHb17/eMyG2o3bgPnZ9x+PxDSi
Z++4iRnwolip0ha2E0bIwq8dVyHYcCPfwkrAk3vSmvLmzEivz+OyXPPWwB6EVq8q
3/DRa9fcVO985bxOeBHImyqgPLm8je70Z51GBezCPlHltYXZ8AHpBzqc7Jp0DgUB
UYlQ3y3a62E5oQ8Uo0S7YFkM7ZYhFaxBeVZs4gC1QOo2FNyQjVvD11digf9M+uSR
aH3SwpHhYSIremKeWG9xDGCjN2fiSuEJHdhwAzWUHFa1b7PArB3Ypq3ILKgJyIwx
1S/LYqnuiCC00tp48b8AzMUdYqyeXIfhvOiYMEzzBIq2Ft+IW9U=
=hWhw
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **secuvera-SA-2024-02: Multiple Persistent Cross-Site Scritping (XSS) flaws in Drupal-Wiki** *Simon Bieber via Fulldisclosure (May 06)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")