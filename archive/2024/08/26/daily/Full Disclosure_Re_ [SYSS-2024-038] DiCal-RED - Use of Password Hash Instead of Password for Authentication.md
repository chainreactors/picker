---
title: Re: [SYSS-2024-038] DiCal-RED - Use of Password Hash Instead of Password for Authentication
url: https://seclists.org/fulldisclosure/2024/Aug/39
source: Full Disclosure
date: 2024-08-26
fetch_date: 2025-10-06T18:03:43.880270
---

# Re: [SYSS-2024-038] DiCal-RED - Use of Password Hash Instead of Password for Authentication

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

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
[![Next](/images/right-icon-16x16.png)](40)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#39)
[![Next](/images/right-icon-16x16.png)](40)

![](/shared/images/nst-icons.svg#search)

# Re: [SYSS-2024-038] DiCal-RED - Use of Password Hash Instead of Password for Authentication

---

*From*: Jeffrey Walton <noloader () gmail com>
*Date*: Thu, 22 Aug 2024 18:11:49 -0400

---

```
There's no difference between sending the password or Hash(password)
at the client. It is similar to (but weaker than) HTTP digest
authentication.

There's nothing to see here.

Jeff

On Thu, Aug 22, 2024 at 5:13 PM Sebastian Hamann via Fulldisclosure
<fulldisclosure () seclists org> wrote:
```

> ```
> -----BEGIN PGP SIGNED MESSAGE-----
> Hash: SHA512
>
> Advisory ID:               SYSS-2024-038
> Product:                   DiCal-RED
> Manufacturer:              Swissphone Wireless AG
> Affected Version(s):       Unknown
> Tested Version(s):         4009
> Vulnerability Type:        Use of Password Hash Instead of Password for Authentication (CWE-836)
> Risk Level:                Medium
> Solution Status:           Open
> Manufacturer Notification: 2024-04-16
> Solution Date:             None
> Public Disclosure:         2024-08-20
> CVE Reference:             CVE-2024-36439
> Author of Advisory:        Sebastian Hamann, SySS GmbH
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Overview:
>
> DiCal-RED is a radio module for communication between emergency vehicles and
> control rooms. It provides Ethernet, Wi-Fi and cellular network connectivity
> and runs a Linux- and BusyBox-based operating system.
>
> The manufacturer describes the product as follows (see [1]):
>
> "The DiCal-Red radio data module reliably guides you to your destination. This
> is ensured by the linking of navigation (also for the transmission of position
> data) and various radio modules."
>
> Due to the use of a password hash instead of a password for authentication,
> the device is vulnerable to unauthorized access to administrative
> functionality.
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Vulnerability Details:
>
> The device provides an administrative web interface that requests the
> administrative system password before it can be used. Instead of submitting
> the user-supplied password, its MD5 hash is calculated on the client side
> and submitted.
> An attacker who knows the hash of the correct password but not the password
> itself can simply replace the value of the password URL parameter with the
> correct hash and subsequently gain full access to the administrative web
> interface.
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Proof of Concept (PoC):
>
> 1. Access the device's web interface and log in with an arbitrary password.
> 2. Use a local proxy or browser plug-in to intercept the HTTP requests.
>    One of them looks like this:
> http://192.0.2.1/cgi-bin/fdmcgiwebv2.cgi?action=validatepassword&password=2ab96390c7dbe3439de74d0c9b0b1767
> 3. Replace the value of the password parameter with the hash of the correct
>    device password.
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Solution:
>
> The manufacturer recommends not running the device in an untrusted network.
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Disclosure Timeline:
>
> 2024-02-29: Vulnerability discovered
> 2024-04-16: Vulnerability reported to manufacturer
> 2024-05-10: Manufacturer states that the vulnerability will not be fixed
> 2024-05-14: Vulnerability reported to CERT-Bund
> 2024-08-13: CERT-Bund informs us that the vendor declared the product EOL
> 2024-08-20: Public disclosure of vulnerability
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> References:
>
> [1] Product website for DiCal-RED
>     https://www.swissphone.com/solutions/components/terminals/radio-data-module-dical-red/
> [2] SySS Security Advisory SYSS-2024-038
>     https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-038.txt
> [3] SySS Responsible Disclosure Policy
>     https://www.syss.de/en/responsible-disclosure-policy
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Credits:
>
> This security vulnerability was found by Sebastian Hamann of SySS GmbH.
>
> E-Mail: sebastian.hamann () syss de
> Public Key: https://www.syss.de/fileadmin/dokumente/PGPKeys/Sebastian_Hamann.asc
> Key ID: 0x9CE0E440429D8B96
> Key Fingerprint: F643 DF21 62C4 7C53 7DB2 8BA1 9CE0 E440 429D 8B96
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Disclaimer:
>
> The information provided in this security advisory is provided "as is"
> and without warranty of any kind. Details of this security advisory may
> be updated in order to provide as accurate information as possible. The
> latest version of this security advisory is available on the SySS website.
>
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>
> Copyright:
>
> Creative Commons - Attribution (by) - Version 3.0
> URL: http://creativecommons.org/licenses/by/3.0/deed.en
>
> -----BEGIN PGP SIGNATURE-----
>
> iQIzBAEBCgAdFiEE9kPfIWLEfFN9souhnODkQEKdi5YFAmbEQgMACgkQnODkQEKd
> i5bDcg//QqSSeXrwj8+F+lGJBRgcwK8Qf7LWK3IWovj+DSKR0II7n6voq+ZG2LPS
> BpO8EEjhSbWDkGHCBgyuvZ8NoXu3LSX3mAVpAvrK+Rq8rPXE1dTxINAilq9Z8Q0r
> bjwybUrN6T0W7uc/Z9VtQiMH1hY1fbkcRbp0RWtzdo0cIjhKs7aBWf1bNIdDaiX8
> Mnyc/5nM65IXPjUdGSFvgNDcUOxG7IRlrPvHncjeiJge8JVqSJUiD410ZpvcBS8x
> 6SPBwl+OqWxF5mnmP2iOixDVMyiZl9AlzaUMA4BISsTRrkSugJmOJTwZGusCZIlZ
> KjikGfjvtIIjC31pqzBuX9uwWT59YBlA4zoNl2gHBzFy0zwZKVSIX2IxhsmqfHci
> XthTlkjX+sY8u9XiMKZU6hYAwUOGFo9+i6L34X/XykztFmwjUluOdOQDzXVoA0wm
> mZ1OEAYOdccr/BakIhTJQONKGzGErZWEUGBcyHOccw4AYQwn19bR7kGXqXZ6/DQB
> w0od4XFWuWVVO/OC6HPCH+vsrjFCze4pPAuGbzKzuPc3bBxWp/gYS5znKFGMwyTf
> wOGCi3YKfPzqze4yC46wbviDfjStEe7ljbAVkuy4r8XLh5MPMLCb/3YPgbhdiqUk
> X1OuQWRmHGp9WnzB2uYfK/+EKZNPthT3gDqZoyGWlISm+6C22no=
> =Y5jL
> -----END PGP SIGNATURE-----
> _______________________________________________
> Sent through the Full Disclosure mailing list
> https://nmap.org/mailman/listinfo/fulldisclosure
> Web Archives & RSS: https://seclists.org/fulldisclosure/
> ```

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](38)
[By Date](date.html#39)
[![Next](/images/right-icon-16x16.png)](40)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#39)
[![Next](/images/right-icon-16x16.png)](40)

### Current thread:

* [[SYSS-2024-038] DiCal-RED - Use of Password Hash Instead of Password for Authentication](32) *Sebastian Hamann via Fulldisclosure (Aug 22)*
  + **Re: [SYSS-2024-038] DiCal-RED - Use of Password Hash Instead of Password for Authentication** *Jeffrey Walton (Aug 24)*
    - [Re: [SYSS-2024-038] DiCal-RED - Use of Password Hash Instead of Password for Authentication](40) *J. Hellenthal via Fulldisclosure (Aug 27)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Downlo...