---
title: Google to support the use of Rust in Chromium
url: https://www.malwarebytes.com/blog/news/2023/01/google-to-support-the-use-of-rust-in-chromium
source: Over Security - Cybersecurity news aggregator
date: 2023-01-18
fetch_date: 2025-10-04T04:13:57.009511
---

# Google to support the use of Rust in Chromium

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

![programmers working on a project together](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/easset_upload_file1497_254126_e.png?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Google to support the use of Rust in Chromium

Posted: January 16, 2023
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

In a [blog by the Chrome security team](https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html) we learned that the Chromium project is going to support the use of third-party Rust libraries from C++ in Chromium.

This is good news because Rust is a so-called memory-safe programming language. So using it in a widespread program like Chrome and the other members of the Chromium family means that almost everyone can benefit from this step forward.

Besides Google’s own Chrome browser, Microsoft Edge, Opera, and many other browsers are based on Chromium code. Reportedly, there are over [25 million lines of code in 36 programming languages](https://www.openhub.net/p/chrome/analyses/latest/languages_summary) in the Chromium browser codebase.

## Rust

Rust is a community project and the product is a high-level, general-purpose programming language that enforces memory safety. Rust started in 2006 as a personal project by Mozilla Research employee Graydon Hoare as part of the development of the Servo browser engine. Then, in February 2021, the Servo team was disbanded and the Rust Foundation was announced by its five founding companies (AWS, Huawei, Google, Microsoft, and Mozilla).

Rust is designed to be memory safe, because poor memory management has been the root cause for way too many vulnerabilities, for way too long. Only a few months ago, [the NSA urged a shift to memory safe programming languages](https://www.malwarebytes.com/blog/news/2022/11/nsa-guidance-on-how-to-avoid-software-memory-safety-issues).

## Memory vulnerabilities

If you ever read our posts describing security vulnerabilities, you will see a lot of phrases like “buffer overflow”, “failure to release memory”, “use after free”, “memory corruption”, and “memory leak”. These are all memory management issues. And the best way to prevent memory management issues is to use a memory-safe language, which manages memory automatically instead of relying on a programmer to code things correctly.

In an earlier article about the [effects of the introduction of memory safe languages in Android](https://www.malwarebytes.com/blog/news/2022/12/memory-safe-languages-proof-is-in-the-pudding) we showed a steady decline of memory safety vulnerabilities in [Android](https://www.malwarebytes.com/cybersecurity/basics/how-to-clean-your-phone-from-virus). With the introduction of memory-safe languages like Kotlin, Java, and Rust in the development of the Android operating system, the contributions to the software that ties everything together in the background coded in C and C++ have gone down considerably.

## Rule of two

Google’s goals for allowing the use of Rust libraries in Chromium are to provide a simpler and safer way to satisfy the rule of two, in order to speed up development and improve the security of Chrome.

The rule of two is demonstrated in the image below:

![rule of two venn diagram](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/easset_upload_file80971_254126_e.png)

*Image courtesy of Google*

It says not to pick more than two of these possibly unsafe circumstances:

* untrustworthy inputs
* unsafe implementation language
* high privilege

By eliminating the “code written in an unsafe language” factor wherever you can, you lessen the need to run code in a sandbox. So, there is les...