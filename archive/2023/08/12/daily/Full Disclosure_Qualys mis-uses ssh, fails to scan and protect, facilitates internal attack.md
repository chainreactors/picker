---
title: Qualys mis-uses ssh, fails to scan and protect, facilitates internal attack
url: https://seclists.org/fulldisclosure/2023/Aug/14
source: Full Disclosure
date: 2023-08-12
fetch_date: 2025-10-04T12:03:30.372007
---

# Qualys mis-uses ssh, fails to scan and protect, facilitates internal attack

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Qualys mis-uses ssh, fails to scan and protect, facilitates internal attack

---

*From*: Paul Szabo via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 10 Aug 2023 06:40:37 +1000

---

```
=== Introduction ===================================================

My institution uses Qualys

  www.qualys.com

to scan for vulnerabilities, including on some Debian Linux machines
that I manage. The scanner does some network scans, and also logs in
to each machine to do "authenticated scans".

=== Discovery ======================================================

When I recently updated my machines from Debian11 to Debian12, the
Qualys scanner was no longer able to SSH login, with syslog lines:

  sshd: userauth_pubkey: signature algorithm ssh-rsa not in PubkeyAcceptedAlgorithms [preauth]

The ssh-rsa algorithm was removed from the default list in Debian12
(has OpenSSH 9.2, up from 8.4 in Debian11), see e.g.

  www.openssh.com/txt/release-8.8
    ... disables RSA signatures using the SHA-1 hash algorithm by
    default. This change has been made as the SHA-1 hash algorithm
    is cryptographically broken ...

I confirmed that Qualys uses (requires) ssh-rsa as public key signing
algorithm: its SSH login to Debian12 suceeds with the SSHD setting
"PubkeyAcceptedAlgorithms +ssh-rsa", and to Debian11 fails with the
opposite "PubkeyAcceptedKeyTypes -ssh-rsa".

=== Issues =========================================================

 - Qualys scanner uses insecure ssh-rsa algorithm for pubkey signing
   in its attempt of SSH login.

 - Modern SSHD servers reject pubkey login with ssh-rsa, so Qualys is
   unable to scan up-to-date Linux e.g. Debian12 or RHEL9.

 - Qualys does not check the list of pubkey signing algorithms
   accepted by SSHD servers, cannot notify about any insecure ones.

=== Vulnerability ==================================================

Any SSHD server that accepts the insecure ssh-rsa algorithm for pubkey
signing is vulnerable. The fact that Qualys had been able to log in to
all Linux machines at my institution, shows that all accept ssh-rsa
and are vulnerable. It is expected that anywhere that Qualys is used,
all Linux machines (except recently updated) are similarly vulnerable.

The vulnerability affects all uses of public key authentication.
Qualys itself facilitates an internal attack, by providing the account
used to do "authenticated scans", forced onto all machines and with
root (sudo) access, with the public key commonly available to any
local admins of any scanned machines. An attack on this account is
both easier and more fruitful; admittedly an attack may be impractical
with currently available computing resources.

=== Fixes needed ===================================================

 - Qualys to reconfigure the scanner to use a secure pubkey signing
   algorithm for its SSH login attempt. This same fix also enables
   Qualys to scan up-to-date Linux e.g. Debian12 or RHEL9.

 - Qualys to check the pubkey signing algorithms accepted by SSHD
   servers, and notify when insecure ones are in use.

 - Administrators of Linux machines to check SSHD settings, ensure
   that ssh-rsa is not accepted. This is needed on all SSHD servers,
   regardless of whether Qualys is used.

=== Comments =======================================================

It is curious how Qualys:
 - uses (requires!) an insecure pubkey signing algorithm, though
   better alternatives have been the norm for decades;
 - did not notice its inability to do authenticated scans on RHEL9
   and similar machines, since over a year ago;
 - checks many similar (similarly impractical) SSHD issues, but does
   not check pubkey signing; and
 - seems to know all about SSH, reporting esoteric issues in its
   internals, but still uses it wrongly.

=== Dedication =====================================================

I dedicate this advisory to Luis Fuentes-Cobas, my one-time professor
of Electromagnetism, who taught me logic, deduction and persistence.
Maybe I missed the class about patience.

=== References =====================================================

www.qualys.com/
www.qualys.com/docs/qualys-authenticated-scanning-unix.pdf
www.openssh.com/txt/release-8.2
www.openssh.com/txt/release-8.8
https://eprint.iacr.org/2020/014.pdf
www.usenix.org/conference/usenixsecurity20/presentation/leurent
https://csrc.nist.gov/news/2006/nist-comments-on-cryptanalytic-attacks-on-sha-1
https://csrc.nist.gov/Projects/hash-functions/nist-policy-on-hash-functions
https://en.wikipedia.org/wiki/SHA-1
www.rfc-editor.org/rfc/rfc4252.html
https://success.qualys.com/support/s/article/000003219
https://success.qualys.com/support/s/article/000006407
https://seclists.org/fulldisclosure/2016/Jan/44
https://seclists.org/oss-sec/2023/q1/75
https://seclists.org/fulldisclosure/2023/Jul/31

=== Timeline =======================================================

24 June 2023  Discovered, notified internally within my institution
 9 July 2023  Qualys contacted via "community" post
16 July 2023  Qualys contacted via security () qualys com
26 July 2023  CVE requested from bugreport () qualys com (a CNA partner)

====================================================================

--
Paul Szabo       psz () maths usyd edu au       www.maths.usyd.edu.au/u/psz
School of Mathematics and Statistics   University of Sydney    Australia
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

### Current thread:

* **Qualys mis-uses ssh, fails to scan and protect, facilitates internal attack** *Paul Szabo via Fulldisclosure (Aug 11)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://ins...