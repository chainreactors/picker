---
title: ClickFix tactic: The Phantom Meet
url: https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-18
fetch_date: 2025-10-06T18:55:55.228644
---

# ClickFix tactic: The Phantom Meet

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# ClickFix tactic: The Phantom Meet

This blog post provides a chronological overview of the observed ClickFix campaigns. We further share technical details about a ClickFix cluster that uses fake Google Meet video conference pages to distribute infostealers.

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue and Sekoia TDR](#molongui-disabled-link)
October 17 2024

0

13 minutes reading

## Table of contents

* [Context](#h-context)
* [ClickFix in the wild](#h-clickfix-in-the-wild)
  + [Chronological overview of ClickFix campaigns](#h-chronological-overview-of-clickfix-campaigns)
  + [Victimology of ClickFix clusters](#h-victimology-of-clickfix-clusters)
* [Investigation of ClickFix clusters](#h-investigation-of-clickfix-clusters)
* [Fake Google Meet pages and technical issues](#h-fake-google-meet-pages-and-technical-issues)
  + [Windows users targeted with Stealc and Rhadamanthys](#h-windows-users-targeted-with-stealc-and-rhadamanthys)
  + [MacOS users targeted by AMOS Stealer](#h-macos-users-targeted-by-amos-stealer)
  + [Traffers teams operating this ClickFix cluster](#h-traffers-teams-operating-this-clickfix-cluster)
* [Conclusion](#h-conclusion)
* [Cluster ClickFix IoCs & Technical details](#h-cluster-clickfix-iocs-amp-technical-details)
* [Fake Google Meet pages and associated infection chain](#h-fake-google-meet-pages-and-associated-infection-chain)
* [Additional clusters allegedly associated to the same traffers teams](#h-additional-clusters-allegedly-associated-to-the-same-traffers-teams)
* [External references](#h-external-references)

## Context

In May 2024, a new social engineering tactic called ClickFix emerged, featuring a ClearFake cluster that the Sekoia Threat Detection & Research (TDR) team closely monitored and analysed in a private report entitled *FLINT 2024-027 – New widespread ClearFake variant abuses PowerShell and clipboard*. This tactic involves displaying fake error messages in web browsers to deceive users into copying and executing a given malicious PowerShell code, finally infecting their systems.

Proofpoint researchers, who named this tactic ClickFix, reported[1](#0be63006-3353-4f2d-a64d-cf84af0757e6) that the initial access broker TA571 leveraged it in email phishing campaigns since March 2024. These campaigns primarily used HTML files disguised as Word documents, displaying a fake error window that prompts users to install malware such as Matanbuchus, DarkGate, or NetSupport RAT via a PowerShell script.

In recent months, multiple malware distribution campaigns have leveraged the ClickFix lure to spread Windows and macOS infostealers, botnets, and remote access tools. This is in line with the growing, ongoing trend of distributing malware through the drive-by download technique. Sekoia analysts assess that several intrusion sets recently adopted this tactic, presumably to evade antivirus software scanning and browser security features, aiming to improve attackers’ infection rates.

In this blog post, we provide a **chronological overview of the observed ClickFix campaigns**. We further share technical details about a **ClickFix cluster that uses fake Google Meet video conference pages to distribute infostealers**, targeting both Windows and macOS systems. Sekoia analysts successfully associated this cluster impersonating Google Meet with two **cybercrime groups: “*Slavic Nation Empire (SNE)”* and “*Scamquerteo*“**. These groups are sub-teams of the cryptocurrency scam teams “*Marko Polo*” and “*CryptoLove*“, respectively.

## ClickFix in the wild

### Chronological overview of ClickFix campaigns

Since June 2024, various open source reports and Sekoia investigations have revealed malware distribution campaigns using the emerging ClickFix tactic. The following figure provides a chronological overview of these campaigns. It highlights the malware families involved and the distribution techniques used, which include phishing emails, compromised websites, and distribution infrastructures.

![Overview of malware distribution campaigns using the ClickFix tactic. Source: Sekoia Blog](data:image/svg+xml...)![Overview of malware distribution campaigns using the ClickFix tactic. Source: Sekoia Blog](https://lh7-qw.googleusercontent.com/docsz/AD_4nXd5vRDdqz6MmPQIgPKV54Dd5u0HmjubJ6s4imGSY-woncRMWS97ajzstgeqGLIHRp43Hg66BMJBn6ILJIsVB4FrkjqQXFeWzDXg2yvD_gqnicZTzJJ7wgYMQt5v3ocb23AxuycXdnAfuEzmLqUJJkePS_YG?key=7qDKNHLl6Eh5y3NwaL0TdQ)

*Figure 1. Overview of malware distribution campaigns using the ClickFix tactic*

Here are some examples of malicious websites that impersonate Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix social engineering tactic.

![Examples of malicious websites impersonating Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix tactic](data:image/svg+xml...)![Examples of malicious websites impersonating Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix tactic](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/10/flint_2024_036_fig1_2-1024x750.png)

*Figure 2. Examples of malicious websites impersonating Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix tactic*

### Victimology of ClickFix clusters

While many of these campaigns reportedly aim to broadly target multiple sectors – using websites compromised by ClearFake or through extensive phishing efforts – some are designed to target specific verticals.

For instance, Proofpoint identified[2](#d26f72ab-8a63-443f-bb05-9595e527e828) a ClickFix cluster targeting transport and logistics companies in North America from at least May to August 2024. This campaign uses websites that impersonate transport and fleet operations management softwa...