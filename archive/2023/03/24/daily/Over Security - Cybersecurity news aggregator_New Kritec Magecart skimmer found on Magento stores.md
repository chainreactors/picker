---
title: New Kritec Magecart skimmer found on Magento stores
url: https://www.malwarebytes.com/blog/threat-intelligence/2023/03/new-kritec-skimmer
source: Over Security - Cybersecurity news aggregator
date: 2023-03-24
fetch_date: 2025-10-04T10:31:39.762012
---

# New Kritec Magecart skimmer found on Magento stores

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

![New Kritec Magecart skimmer found on Magento stores](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/asset_upload_file86663_262516.jpg?w=736)

[Threat Intel](https://www.malwarebytes.com/blog/category/threat-intel)

# New Kritec Magecart skimmer found on Magento stores

Posted: March 22, 2023
 by [Jérôme Segura](https://www.malwarebytes.com/blog/authors/jeromesegura)

Threat actors often compete for the same resources, and this couldn’t be further from the truth when it comes to website compromises. After all, if a vulnerability exists one can expect that it will be exploited more than once.

In the past, we have seen such occurrences with Magecart threat actors for example in the [breach of the Umbro website](https://www.malwarebytes.com/blog/news/2018/11/web-skimmers-compete-umbro-brasil-hack). Recently, while reading a blog post from security vendor Akamai, we spotted a similar situation. In the listed indicators of compromise, we noticed domains that we had seen used in a distinct skimming campaign which didn’t seem to be documented yet.

In fact, we saw instances of compromised stores having both skimmers loaded, which means double trouble for victims as their credit card information is stolen not just once but twice. In this blog post, we show how the newly found Kritec skimmer was found along side one of its competitors.

## Original campaign using WebSockets

Researchers at [Akamai reported](https://www.akamai.com/blog/security/magecart-attack-disguised-as-google-tag-manager) on a Magecart skimmer campaign disguised as Google Tag Manager that also made the [news](https://www.bleepingcomputer.com/news/security/canadas-largest-alcohol-retailers-site-hacked-to-steal-credit-cards/) with the compromise of one of Canada’s largest liquor store (LCBO). While details were not shared at the time, we were able to determine thanks to an [archived crawl](https://urlscan.io/result/9b1f4ca6-7a15-4c4a-97f1-c28232f1f3ca/dom/) on urlscan.io that the skimmer was using WebSockets and is the same one as described in Akamai’s blog.

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file73839_262516_e.jpeg)

## Kritec campaign

Akamai notes that they identified multiple compromised websites that had similarities. They also list nebiltech[.]shop in their IOCs which is a domain we sometimes saw injected near the Google Tag Manager script, but not within it.

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file78784_262516_e.png)

We believe this is a different campaign and threat actor altogether. Here are some reasons why:

* No WebSocket being used
* Domains abusing Cloudflare
* Intermediary loader
* Completely different skimming code

To complicate things, we observed some stores that had both skimmers at the same time, which is another reason why we believe they are not related:

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file97655_262516_e.png)

We started calling this new skimmer ‘Kritec’ after one of its domain names. It has an interesting way of loading the malicious JavaScript we had not seen before either. The injected code calls out a first domain (seen above encoded in Base64) and generates a Base64 response:

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file80050_262516_e.png)

Decoding it reveals a URL pointing to the actual skimming code, which is heavily obfuscated (likely via obfuscator.io):

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file47530_262516_e.png)

The data exfiltration is also done differently as seen in the image below. On the lef...