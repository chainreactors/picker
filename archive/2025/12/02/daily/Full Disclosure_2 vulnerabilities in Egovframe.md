---
title: 2 vulnerabilities in Egovframe
url: https://seclists.org/fulldisclosure/2025/Dec/2
source: Full Disclosure
date: 2025-12-02
fetch_date: 2025-12-03T03:17:16.821643
---

# 2 vulnerabilities in Egovframe

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# 2 vulnerabilities in Egovframe

---

*From*: Pierre Kim <pierre.kim.sec () gmail com>
*Date*: Thu, 20 Nov 2025 07:02:15 -0500

---

```
Hello,

Please find a text-only version below sent to security mailing lists.

The complete version on "2 vulnerabilities in Egovframe" is posted here:

https://pierrekim.github.io/blog/2025-11-20-egovframe-2-vulnerabilities.html

The text version is also posted here:
  https://pierrekim.github.io/advisories/2025-egovframe.txt

=== text-version of the advisory  ===

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

## Advisory Information

Title: 2 vulnerabilities in Egovframe
Advisory URL: https://pierrekim.github.io/advisories/2025-egovframe.txt
Blog URL: https://pierrekim.github.io/blog/2025-11-20-egovframe-2-vulnerabilities.html
Date published: 2025-11-20
Vendors contacted: KISA/KrCERT
Release mode: Released
CVE: CVE-2025-34336, CVE-2025-34337

## Product description
```

> ```
> eGovFrame, the e-Government Standard Framework, is a platform-specific standardized development framework for public
> sector IT projects in Korea.
> It is developed by the government of the Republic of Korea and can be used by every person all over the world.
>
> From https://www.egovframe.go.kr/eng/sub.do?menuNo=2
> ```

```
Egovframe is a Java-based framework mainly used in the websites of the
Government of South Korea (Korea).

## Vulnerabilities Summary

Vulnerable versions: currently existing all versions.

The summary of the vulnerabilities is:

1. CVE-2025-34336 - Unauthenticated file upload vulnerability
2. CVE-2025-34337 - Pre-authenticated Cryptographic Oracle

_Miscellaneous notes_:

These vulnerabilities were discovered in March 2023 after a brief
security assessment (2-3 hours) on egovframe and were reported to
KrCERT in April 2023 through POC Security, a Korean cybersecurity
company acting as a trusted third party.

Due to previous bad experiences when reporting vulnerabilities
directly to KrCERT, I preferred using a reputable Korean cybersecurity
company - POC Security - who could act as a third party. The initial
advisories were given to POC Security at the Zer0con conference in
April 2023.

In August 2023, KISA confirmed that the vulnerabilities were
exploitable. In October 2023, KISA confirmed that the vulnerabilities
had been patched. In September 2025, I confirmed that the following
vulnerabilities had not been properly patched.

These vulnerabilities allow an unauthenticated remote attacker to
upload any file to websites based on "egovframework", a solution
widely used on Korean government websites.

Furthermore, this program does not appear to be tracked by CVE
identifiers. Instead, KVE identifiers are used:
```

> ```
> KVE stands for Korea Vulnerabilities and Exposures, which is a system used in South Korea for cataloging and tracking
> security vulnerabilities. Contrary to CVEs and CNNVDs, it is unclear if KVE entries  are public.
> ```

```
Analyzing the source code and searching for "KISA" (the agency
managing KrCERT), I could find approximately 260 mentions of
vulnerabilities fixed by KISA. It appears that these vulnerabilities
were not publicly tracked outside of the source code (I found only
three KVE-2025-XXXX entries in a PDF file announcing a new release).

We can list the vulnerabilities detected and fixed by KISA by
searching for comments containing "KISA" and "YYYY-MM-DD".
Unfortunately, the reported vulnerabilities are not found there.

    kali% for i in $(seq 2010 2025);do echo -n "$i - "; rgrep "$i"
|grep -c KISA | grep -v ' - 0$';done
    2012 - 6
    2018 - 161
    2019 - 65
    2020 - 18
    2022 - 1
    2024 - 1
    2025 - 2
    kali%

For example:
https://github.com/eGovFramework/egovframe-common-components/blob/main/src/main/java/egovframework/com/utl/sys/pxy/web/EgovProxySvcController.java#L176.

We also note that all version changelogs indicate that some
vulnerabilities have been fixed without any information:
https://github.com/eGovFramework/egovframe-common-components/releases.

Since vulnerability tracking is quite difficult, using this solution
seems like a questionable choice from a risk management point of view.

On a positive note, these results mean there is plenty of room for improvement.

_Impacts_

An unauthenticated remote attacker can upload any file to any website
based on the egovframework. Since the content type was controlled by
the attacker (up to version 4.1.2), it was possible to host any type
of content on the remote website, such as a phishing webpage or a
webpage with JavaScript to steal cookies. Since version 4.1.2, it is
possible to download any image uploaded with the correct content type.
Any file uploaded other than an image will be served with the
`application/octet-stream` content type (the content type is no longer
controlled by the attacker).

The malicious file will then be available on the targeted website via
a specific API accessible without authentication.

It is possible to exploit a cryptographic Oracle to create valid and
custom encrypted variables. These malicious encrypted strings will be
then fully trusted and can be used to abuse internal services.

_Recommendations_

Do not expose Egovframe-based websites on the Internet.

## Unpatched vulnerabilities

Vulncheck assigned the following CVEs in November 2025:

- - CVE-2025-34336 - eGovFramework <= 4.3.1 Unauthenticated File
Upload via Web Editor Image Upload Endpoints
- - CVE-2025-34337 - eGovFramework <= 4.3.1 Unauthenticated Encryption
Oracle via Web Editor Image Upload Endpoints

These KVEs have been assigned by KISA/KrCERT:

- - KVE-2023-5280 Unauthenticated File upload in egovframework
- - KVE-2023-5281 encryption Oracle to craft custom valid encrypted variables

## Identification of the solution

For this advisory, the latest version as of the date of this security
advisory was obtained via the official git repository at
https://github.com/eGovFramework/egovframe-common-components.

The latest commit is:

    commit 7030600a8d959fbdb09787cd346be9ccf2c2dc1c (HEAD -> main,
origin/main, origin/HEAD)
    Merge: e10475cc b354bbb7
    Author: eGovFrameSupport <egovframesupport () gmail com>
    Date:   Wed Sep 24 14:49:27 2025 +0900

There were some changes in the source codes since March 2023,
including a incorrect attempt to fix one of the vulnerabilities after
I reported it - it is unclear if this was a bug collision (someone
else was credited for this vulnerability in the source codes).

## Details - Unauthenticated file upload vulnerability

An attacker can upload any file without authentication on a website
developed with the egov framework.

The vulnerable component `egovframe-common-components` is used by the
egovframe framework.

The `/utl/wed/insertImage.do` and `/utl/wed/insertImageCk.do` POST
APIs defined in the
`egovframe-common-components/src/main/java/egovframework/com/utl/wed/web/EgovWebEditorImageController.java`
file do not implement authentication as shown below:

[code:java]
 60         private final String extWhiteList =
EgovProperties.getProperty("Globals.fileDownload.Extensions");
[...]
 76         /**
 77          * ??? Upload? ????.
 78          *
 79          * @param model
 80          * @return
 81          * @throws Ex...