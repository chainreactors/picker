---
title: Android is slowly mastering memory management vulnerabilities
url: https://www.malwarebytes.com/blog/news/2022/12/memory-safe-languages-proof-is-in-the-pudding
source: Over Security - Cybersecurity news aggregator
date: 2022-12-09
fetch_date: 2025-10-04T01:01:33.471583
---

# Android is slowly mastering memory management vulnerabilities

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

![monitored programming](https://www.malwarebytes.com/wp-content/uploads/sites/2/2022/12/easset_upload_file70656_250521_e.png?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Android is slowly mastering memory management vulnerabilities

Posted: December 4, 2022
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

Recently we wrote about why the [NSA wants you to shift to memory safe programming languages](https://www.malwarebytes.com/blog/news/2022/11/nsa-guidance-on-how-to-avoid-software-memory-safety-issues). The short version is: If you ever read our posts describing security vulnerabilities, you will see a *lot* of phrases like “buffer overflow”, “failure to release memory”, “use after free”, “memory corruption”, and “memory leak”. These are all memory management issues. And the best way to prevent memory management issues is to use a memory-safe language, which manages memory automatically instead of relying on a programmer to code things correctly.

Hot on the heels of the NSA, Google has just published an article on its [security blog](https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html) that provides some numbers to support agency’s point of view. Google reports that it’s seeing a significant drop in memory safety vulnerabilities in the [Android](https://www.malwarebytes.com/cybersecurity/basics/how-to-clean-your-phone-from-virus) operating system as the use of memory safe programming languages increases.

## The numbers

I’ve always been a stickler for statistics, but you have to consider the source, the population, and the boundaries for each category, before you know what they are telling you. And unless the publisher is trying to manipulate you into a conclusion by using pseudoscientific claims not based on the presented data, statistics allow you to demonstrate the correlation between cause and effect.

### Effect

The Google security team looked at the vulnerabilities reported in the Android security bulletin, which includes critical/high severity vulnerabilities reported through its vulnerability rewards program, and vulnerabilities reported internally. It noticed that the number of memory safety vulnerabilities has shown a year-on-year decline each year since 2019. In 2019 there were 223. In 2022 there were 85.

### Cause

This drop in memory safety vulnerabilities coincides with a shift in programming languages. With the introduction of memory-safe languages like Kotlin, Java, and Rust in the development of the Android operating system, the contributions to the software that ties everything together in the background coded in C and C++ have gone down considerably.

### Other possible causes

So, we can see a clear correlation between writing in memory-safe languages and the number of memory related vulnerabilities that were reported. But correlation does not always mean there is an actual causality. There could be other factors at play.

Software bugs are found and fixed over time, so we can expect the number of bugs in mature code that is being maintained but not actively developed to go down over time.

To demonstrate this is not the reason for the correlation, the Google team looked at new low-level components that require a systems language which would previously have been implemented in C++, but were coded in Rust. The result was impressive:

> To date, there have been zero memory safety vulnerabilities discovered in Android’s Rust code.

There are approximately 1.5 million lines of Rust code in the Android Open Source Project (AOSP) across new functionality. According to Google, historically the vulnerability density is greater than one vulnerabi...