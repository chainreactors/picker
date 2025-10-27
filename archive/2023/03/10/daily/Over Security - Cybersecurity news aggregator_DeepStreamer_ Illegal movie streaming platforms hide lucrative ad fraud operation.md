---
title: DeepStreamer: Illegal movie streaming platforms hide lucrative ad fraud operation
url: https://www.malwarebytes.com/blog/threat-intelligence/2023/03/deepstreamer-illegal-movie-streaming-platforms-hide-lucrative-ad-fraud-operation
source: Over Security - Cybersecurity news aggregator
date: 2023-03-10
fetch_date: 2025-10-04T09:10:32.040775
---

# DeepStreamer: Illegal movie streaming platforms hide lucrative ad fraud operation

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

![DeepStreamer: Illegal movie streaming platforms hide lucrative ad fraud operation](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/asset_upload_file76935_260840.jpg?w=736)

[Threat Intel](https://www.malwarebytes.com/blog/category/threat-intel)

# DeepStreamer: Illegal movie streaming platforms hide lucrative ad fraud operation

Posted: March 8, 2023
 by [Threat Intelligence Team](https://www.malwarebytes.com/blog/authors/threatintelligence)

*This investigation was a joint effort between Malwarebytes Threat Intelligence’s Jérôme Segura, DeepSee’s Rocky Moss and Antonio Torres.*

## Key findings

* Over a dozen unique domains were found selling ad inventory through Google Ad Manager, even though the pages were embedded invisibly under the content of illegal movie & porn streaming sites
* Streaming sites in the DeepStreamer fraud ring generated an estimated 210,550,928 visits in January 2023, as measured by Similar Web
* There was not a single seller in common between each of the sites used for laundering (the “money sites”), but most offered their inventory for sale through Google Ad Manager
* Using extremely conservative estimates, which factor in a 50% ad-block rate & 70% ad-unit fill rate, we project advertiser spend on this scheme between $120k – $1.2 million in January 2023 alone
* Working with a leading ad buying platform, we were able to confirm there were hundreds of millions of bid requests generated for these domains between January and February 2023

## Introduction

Online video streaming sites have always been some of the most visited destinations on the web. Legitimate ones will typically require a subscription fee or rely on advertising as part of their business model. Unfortunately, at any given point in time, there are thousands of sites that allow users to illegally stream pirated content, and they often manage to devise strategies that allow them to monetize their illegally sourced content with programmatic advertising.

Researchers at [DeepSee](https://deepsee.io/) and [Malwarebytes](https://www.malwarebytes.com/) have identified an invalid traffic scheme that has gone undetected for over one year via a number of illegal video streaming platforms. DeepStreamer used different techniques to evade detection and forge traffic by surreptitiously loading “money sites” (ad-monetized sites used to monetize/launder the human traffic to pirate sites) filled with Google ads completely hidden from view, while internet users were watching movies.

Not only are these streaming sites breaking the law by using copyrighted material, they are also defrauding advertisers to the tune of $1.2million per month, based on conservative estimates.

## A deceptive business model

DeepSee researchers contacted Malwarebytes about a scheme they had observed recently via a video streaming website called moviesjoy[.]to. DeepSee’s crawlers had observed the site mikerin[.]com loading ads deep under the content of moviesjoy, but it wasn’t exactly clear how this was happening.

Interestingly, the site claims to offer free HD movies and TV series with “absolutely zero ads on our site. Once you hit the play button, you can start streaming right away, without any interruptions in the middle.”

On the internet if something is “free”, it usually means you are the product in some shape or form. Hosting and streaming costs money that needs to be recouped so the service can stay online.

What we identified was not entirely surprising but was quite clever. The platform does indeed rely on ads but rather than having them visible on the site, they are embedding and hiding them.

While the site owner could display ads to their visitors, there is no...