---
title: Veraport: Inside Korea’s dysfunctional application management
url: https://palant.info/2023/03/06/veraport-inside-koreas-dysfunctional-application-management/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-07
fetch_date: 2025-10-04T08:50:46.326767
---

# Veraport: Inside Korea’s dysfunctional application management

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Veraport: Inside Koreaâs dysfunctional application management

2023-03-06
 [Korea](/categories/korea/)/[Security](/categories/security/)/[Privacy](/categories/privacy/)
 21 mins
 [2 comments](/2023/03/06/veraport-inside-koreas-dysfunctional-application-management/#comments)

*Note*: This article is also available in [Korean](https://github.com/alanleedev/KoreaSecurityApps/blob/main/05_wizvera_veraport.md).

As discussed before, South Koreaâs banking websites [demand installation of various so-called security applications](/2023/01/02/south-koreas-online-security-dead-end/). At the same time, weâve seen that these applications like [TouchEn nxKey](/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/) and [IPinside](/2023/01/25/ipinside-koreas-mandatory-spyware/) lack auto-update functionality. So even in case of security issues, it is almost impossible to deliver updates to users timely.

And thatâs only two applications. Koreaâs banking websites typically expect around five applications, and it will be different applications for different websites. Thatâs a lot of applications to install and to keep up-to-date.

Luckily, the Veraport application by Wizvera will take care of that. This application will automatically install everything necessary to use a particular website. And it will also install updates if deemed necessary.

![Laptop with Veraport logo on the left, three web servers on the right. First server is labeled âInitiating server,â the arrow going from it to the laptop says âGet policy from banking.example.â Next web server is labeled âPolicy server,â the arrow pointing from the laptop to it says âInstallation policy?â and the arrow back âInstall app.exe from download.example.â The final web server is labeled âDownload serverâ and an arrow points to it from the laptop saying âGive me app.exe.â](/2023/03/06/veraport-inside-koreas-dysfunctional-application-management/veraport.png)

If this sounds like a lot of power: thatâs because it is. And so Veraport already [made the news as the vehicle of an attack by North Korean hackers](https://threatpost.com/hacked-software-south-korea-supply-chain-attack/161257/).

Back then everybody was quick to shift the blame to the compromised web servers. I now took a deeper dive into how Veraport works and came to the conclusion: its approach is inherently dangerous.

As of Veraport 3.8.6.5 (released on February 28), all the reported security issues seem to be fixed. Getting users to update will take a long time however. Also, the dangerous approach of allowing Veraport customers to distribute arbitrary software remains of course.

#### Contents

* [Summary of the findings](#summary-of-the-findings)
* [How banking websites distribute applications](#how-banking-websites-distribute-applications)
* [How Wizvera Veraport works](#how-wizvera-veraport-works)
* [Protection against malicious policies](#protection-against-malicious-policies)
* [Holes in the protection](#holes-in-the-protection)
  + [Lack of data protection in transit](#lack-of-data-protection-in-transit)
  + [Overly wide allowedDomains settings](#overly-wide-alloweddomains-settings)
  + [Who has the signing keys?](#who-has-the-signing-keys)
  + [The certification authorities](#the-certification-authorities)
* [Combining the holes into an exploit](#combining-the-holes-into-an-exploit)
  + [Using an existing policy file from a malicious website](#using-an-existing-policy-file-from-a-malicious-website)
  + [Running a malicious binary](#running-a-malicious-binary)
  + [Removing visual clues](#removing-visual-clues)
* [Information leak: Local applications](#information-leak-local-applications)
* [Web server vulnerabilities](#web-server-vulnerabilities)
  + [HTTP Response Splitting](#http-response-splitting)
  + [Persistent XSS via a service worker](#persistent-xss-via-a-service-worker)
* [Reporting the issues](#reporting-the-issues)
* [What is fixed](#what-is-fixed)
* [Remaining issues](#remaining-issues)

## Summary of the findings

Veraport signs the policy files determining which applications are to be installed from where. While the cryptography here is mostly sane, the approach suffers from a number of issues:

* One root certificate still used for signature validation is using MD5 hashing and a 1024 bit strong RSA key. Such certificates have been [deprecated for over a decade](https://wiki.mozilla.org/CA%3AMD5and1024).
* HTTPS connection for downloads is not being enforced. Even when HTTPS is used, server certificate is not validated.
* Integrity of downloaded files is not validated correctly. Application signature validation is trivially circumvented, and while hash-based validation is possible this functionality is essentially unused.
* Even if integrity validation werenât easily circumvented, Veraport leaves the choice to the user as to whether to proceed with a compromised binary.
* Download and installation of an application can be triggered without user interaction and without any visible clues.
* Individual websites (e.g. banking) are still responsible for software distribution and will often offer outdated applications, potentially with known security issues.
* Each and every Veraport customer is in possession of a signing certificate that, if compromised, can sign arbitrary malicious policies.
* There is no revocation mechanism to withdraw known leaked signing certificates or malicious policies.

In addition to that, Veraportâs local web server on `https://127.0.0.1:16106` contains vulnerabilities amounting to persistent [Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/) among other things. It will expose the full list of the processes running on the userâs machine to any website asking. For security applications it will also expose the application version.

Finally, Veraport is also built on top of a number of outdated open-source libraries with known vulnerabilities. For example, it uses OpenSSL 1.0.2j (released 2016) for its web server and for signature validation. OpenSSL vulnerabilities are particularly well-documented â itâs [at least 3 known high-severity and 13 known moderate-severity vulnerabilities](https://www.openssl.org/news/vulnerabilities-1.0.2.html) for this version.

The local web server itself is mongoose 5.5 (released in 2014). And parsing of potentially malicious JSON data received from websites is done via JsonCpp 0.5.0 (released 2010). Yes, thatâs almost 13 years old. Yes, current version is JsonCpp 1.9.5 which has seen plenty of security improvements.

## How banking websites distribute applications

Login websites of South Korean banks run JavaScript code from SDKs belonging to various so-called security applications. Each such SDK will first check whether the application is present on the userâs computer. If it isnât, the typical action is redirecting the user to a download page.

![Screenshot of a page titled âInstall Security Program.â Below it the text âTo access and use services on Busan Bank website, please install the security programs. If your installation is completed, please click Home Page to move to the main page. Click [Download Integrated Installation Program] to start automatica installation. In case of an error message, please click 'Save' and run the downloaded the application.â Below that text the page suggests downloading âIntegrated installation (Veraport)â and five individual applications.](/2023/03/06/veraport-inside-koreas-dysfunctional-application-management/applications.png)

This isnât the software vendorâs download page but rather the bankâs page. It lists all the various applications required and expects you to download them. Typically, the bankâs web server doubles as the download server for the application. Some of the software vendors donâ...