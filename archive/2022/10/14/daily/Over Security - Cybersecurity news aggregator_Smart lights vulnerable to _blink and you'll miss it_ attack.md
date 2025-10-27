---
title: Smart lights vulnerable to "blink and you'll miss it" attack
url: https://www.malwarebytes.com/blog/news/2022/10/smart-lighting-system-suffers-a-blink-and-youll-miss-it-attack
source: Over Security - Cybersecurity news aggregator
date: 2022-10-14
fetch_date: 2025-10-03T19:52:12.850294
---

# Smart lights vulnerable to "blink and you'll miss it" attack

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

![Two people sitting with devices](https://www.malwarebytes.com/wp-content/uploads/sites/2/2022/10/asset_upload_file52574_239784.jpg?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Smart lights vulnerable to “blink and you’ll miss it” attack

Posted: October 11, 2022
 by [Christopher Boyd](https://www.malwarebytes.com/blog/authors/cboyd)

Over the last couple of years, key parts of our daily lives have been sliding into some form of Internet connectivity. Smartphones and other devices have become necessities. Paying bills? Those systems have moved online. Tax? Online. Wage slips and bank statements? It’s paperless time. Welfare assistance? There’s a login portal for that. In short, people need web access.

However, there’s a lot of non-critical systems and services which are making this leap too. And if it’s got a computer in it and it’s connected to the Internet, you know that sooner or later somebody will find a way to compromise it. Internet-connected light bulbs, now is your time to shine.

## Shining a light on vulnerabilities

Back in 2021, researchers [discovered two potential flaws](https://therecord.media/researchers-find-bugs-in-ikea-smart-lighting-system/) in a popular smart lighting system. The vulnerability allowed them to make the light bulbs blink. In a worst case scenario, the system would “forget” its configuration and all bulbs would be set to maximum. These issues are outlined in [CVE-2022-39064](https://www.synopsys.com/blogs/software-security/cyrc-advisory-ikea-tradfri-smart-lighting/) and [CVE-2022-39065](https://www.synopsys.com/blogs/software-security/cyrc-advisory-ikea-tradfri-smart-lighting-gateway/). It’s the old “Blink once for yes, blink twice for no” except in this case it’s “Blink once to assume control, blink a few more times to perform a factory reset”.

Victims of these potential attacks could power cycle their gateway, but the attackers would be free to come back at any time without a fix in place. Now, some folks may wonder what the big deal is as it’s “just” making a light bulb blink. Well, if nothing else, ramping someone’s household to maximum lightbulb brightness over a sustained period of time isn’t great at a time of [spiralling energy bill costs](https://www.bbc.co.uk/news/business-58090533).

But there’s more too it than that. Whether the computer in question is a server or a light bulb, unauthorised users are not supposed to be able to make it do things without your permission. When they do, the only thing you know for sure is that your security has been breached.

The first CVE has been addressed with all software versions from 1.19.26 onward. According to The Record, CVE-2022-39064 “has not been fully dealt with” and there’s no ETA on when a full fix will arrive.

## The winding road of IoT issues

The [Internet of Things (IoT](https://www.malwarebytes.com/iot)) is here to stay, and a lot of folks simply like the idea of managing every aspect of their home life via one app or service. Unfortunately, some services or devices are cheaply made and [insecure by default](https://www.malwarebytes.com/blog/news/2018/04/please-dont-buy-smart-toys).

IoT devices can introduce new risks too. Some devices inadvertently provide abusive people with new ways to harass and abuse their partner or ex-partner, for example.

And making devices “smart” often means making them dependent on an Internet connection or [cloud](https://www.malwarebytes.com/what-is-the-cloud) service—which is fine until they aren’t there. In 2020, an Amazon cloud service outage [managed to knock out](https://www.dailymail.co.uk/sciencetech/article-8994907/Widespread-Amazon-cloud-service-outage-disables-Roombas-Ring-d...