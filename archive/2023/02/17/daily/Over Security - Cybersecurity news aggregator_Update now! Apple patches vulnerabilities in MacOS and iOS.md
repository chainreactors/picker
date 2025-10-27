---
title: Update now! Apple patches vulnerabilities in MacOS and iOS
url: https://www.malwarebytes.com/blog/news/2023/02/update-now-apple-patches-vulnerabilities-in-macos-and-ios
source: Over Security - Cybersecurity news aggregator
date: 2023-02-17
fetch_date: 2025-10-04T06:54:16.189676
---

# Update now! Apple patches vulnerabilities in MacOS and iOS

[Skip to content](#primary)

Search

Search Malwarebytes.com

Search for:

* [Sign In](https://my.malwarebytes.com/en/login)

  [Sign in](https://my.malwarebytes.com/overview)

  [Activate subscription >](https://my.malwarebytes.com/landing/activate)

  [Add devices or upgrade >](https://my.malwarebytes.com/landing/upgrade)

  [Renew subscription >](https://my.malwarebytes.com/landing/manual-renewal)

  [Secure Hub >](https://my.malwarebytes.com/secure-hub)

  [Don’t have an account?
  **Sign up >**](https://my.malwarebytes.com/overview?flow=signup)

  Sign In

[Malwarebytes logo](https://www.malwarebytes.com/blog)

* Personal

  < Products

  **Device Protection & Antivirus**

  + [Premium Security Antivirus](https://www.malwarebytes.com/premium)
  + [Mobile Security for Android & iOS](https://www.malwarebytes.com/mobile)

  **Identity Protection**

  + [Identity Theft Protection](https://www.malwarebytes.com/identity-theft-protection)
  + [Personal Data Remover](https://www.malwarebytes.com/personal-data-remover)
  + [Digital Footprint Scanner](https://www.malwarebytes.com/digital-footprint)

  **Privacy Protection**

  + [Privacy VPN](https://www.malwarebytes.com/vpn)
  + [Browser Guard](https://www.malwarebytes.com/browserguard)
  + [AdwCleaner](https://www.malwarebytes.com/adwcleaner)

  Have a current computer infection?

  [**Free Virus Scan**](https://www.malwarebytes.com/solutions/virus-scanner)

  Worried it’s a scam?

  [**Free Scam Guard tool**](https://www.malwarebytes.com/solutions/scam-guard)

  Try our antivirus with a free, full-featured 14-day trial

  [**Free Antivirus**](https://www.malwarebytes.com/mwb-download)

  Get your free digital security toolkit

  [**Explore all free tools**](https://www.malwarebytes.com/free-tools)

  Find the right cyberprotection for you

  [**Compare plans and pricing**](https://www.malwarebytes.com/pricing)
* Business

  < Business

  **[Teams](https://www.malwarebytes.com/teams)**

  Protect small & home offices – no IT expertise needed

  **[ThreatDown](https://www.threatdown.com/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cta-mb-nav-threatdown)**

  Award-winning endpoint security for small and medium businesses
* Pricing

  < Pricing

  [Personal pricing](https://www.malwarebytes.com/pricing)

  Protect your personal devices and data

  [Small or home office pricing](https://www.malwarebytes.com/pricing/teams)

  Protect your team’s devices and data – no IT skills needed

  [Corporate pricing](https://www.threatdown.com/pricing/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cat-en-us-navbar-pricing-business-pricing-click)

  Explore award-winning endpoint security for your business
* [Partners](https://www.malwarebytes.com/partners)
* Resources

  < Resources

  [![Malwarebytes Labs](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/07/mwb-labs-159px.svg)](https://www.malwarebytes.com/blog)

  + [Security terms glossary](https://www.malwarebytes.com/glossary)
  + [Threat Center](https://www.malwarebytes.com/blog/threats)
  + [Cybersecurity News](https://www.malwarebytes.com/blog)

  + [About Malwarebytes](https://www.malwarebytes.com/company)
  + [Press](https://www.malwarebytes.com/press/)
  + [Careers](https://www.malwarebytes.com/jobs)

  [Cybersecurity Resource Center](https://www.malwarebytes.com/cybersecurity)

  + [Antivirus](https://www.malwarebytes.com/cybersecurity/basics/antivirus)
  + [Malware](https://www.malwarebytes.com/malware)
  + [Phishing](https://www.malwarebytes.com/phishing)
  + [Ransomware](https://www.malwarebytes.com/ransomware)
  + [Small business hub](https://www.malwarebytes.com/small-business)
  + [See all articles](https://www.malwarebytes.com/cybersecurity)
* Help

  < Support

  [Malwarebytes Help Center](https://help.malwarebytes.com/hc/en-us)

  Malwarebytes and Teams Customers

  [ThreatDown Business Support](https://support.threatdown.com/hc/en-us/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cta-navbar-support-Threatdown-business-click)

  Nebula and Oneview Customers

  [Community Forums](https://forums.malwarebytes.com/)

Free Download

Search
Search

Search Malwarebytes.com

Search for:

![hands in surgeon gloves stitching an apple](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/02/asset_upload_file56374_259098.png?w=736)

[Mobile](https://www.malwarebytes.com/blog/category/mobile)
| [Bugs](https://www.malwarebytes.com/blog/category/bugs)
| [News](https://www.malwarebytes.com/blog/category/news)

# Update now! Apple patches vulnerabilities in MacOS and iOS

Posted: February 15, 2023
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

Apple has released information about the new [security content of macOS Ventura 13.2.1](https://support.apple.com/en-us/HT213633) and of [iOS 16.3.1 and iPadOS 16.3.1](https://support.apple.com/en-us/HT213635).

Most prominent is a vulnerability in WebKit that may have been actively exploited. In December, 2022, we [warned](https://www.malwarebytes.com/blog/news/2022/12/update-now-apple-patches-active-exploit-vulnerability-for-iphones) our readers about another actively exploited vulnerability in Apple’s WebKit.

The currently patched vulnerability was a type confusion issue that Apple says has been addressed with improved checks.

Type confusion vulnerabilities are programming flaws that happen when a piece of code doesn’t verify the type of object that is passed to it before using it. So let’s say you have a program that expects a number as input, but instead it receives a string (i.e. a sequence of characters). If the program doesn’t properly check that the input is actually a number and tries to perform arithmetic operations on it as if it were a number, it may produce unexpected results which could be abused by an attacker.

Type confusion can allow an attacker to feed function pointers or data into the wrong piece of code. In some cases, this could allow attackers to execute arbitrary code on a vulnerable device. So, an attacker would have to trick a victim into visiting a malicious website or open such a page in one of the apps that use WebKit to render their pages.

## Mitigation

Updates are available for macOS Ventura, iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th generation and later, and iPad mini 5th generation and later.

The updates should all have reached you in your regular update routines, but it doesn’t hurt to check if your device is at the [latest update level](https://support.apple.com/en-us/HT201222).

[How to update your iPhone or iPad.](https://support.apple.com/en-us/HT204204)

[How to update macOS on Mac.](https://support.apple.com/en-us/HT201541)

Since the vulnerability we’ll discuss below is already being exploited, it’s important that you update your devices as soon as you can.

There may be one exception to this rule. [Reportedly](https://www.xda-developers.com/google-photos-broken-ios-1631-update/) users of Google Photos on iPhone have noticed that the update causes Google Photos to break. These users may want to wait for Apple to fix this and in the meantime be extra careful when clicking links.

If you fear your Mac has been infected, try out [Malwarebytes for Mac](https://malwarebytes.com/mac). Or [Malwarebytes for iOS](https://support.malwarebytes.com/hc/en-us/categories/360002468273-Malwarebytes-for-iOS) for your Apple devices.

## Vulnerabilities

The Common Vulnerabilities and Exposures (CVE) database lists publicly disclosed computer security flaws. Its goal is to make it easier to share data across separate vulnerability capabilities (tools, databases, and services). The CVEs patched in these updates are:

[CVE-2023-23514](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23514): Apple addressed a use after free issue by implementing improved memory management. Use af...