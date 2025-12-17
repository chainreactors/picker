---
title: Photo booth flaw exposes people&#8217;s private pictures online
url: https://www.malwarebytes.com/blog/news/2025/12/photo-booth-flaw-exposes-peoples-private-pictures-online
source: Malwarebytes
date: 2025-12-16
fetch_date: 2025-12-17T03:18:46.831189
---

# Photo booth flaw exposes people&#8217;s private pictures online

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
  **Sign up >**](https://my.malwarebytes.com/registration)

  Sign In

[Malwarebytes logo](https://www.malwarebytes.com)

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

[News](https://www.malwarebytes.com/blog/category/news)

# Photo booth flaw exposes people’s private pictures online

by [Danny Bradbury](https://www.malwarebytes.com/blog/authors/dbradbury) |
December 16, 2025

![photo booth](https://www.malwarebytes.com/wp-content/uploads/sites/2/2025/12/photo-booth.jpg?w=1200)

Photo booths are great. You press a button and get instant results. The same can’t be said, allegedly, for the security practices of at least one company operating them.

A security researcher spent weeks trying to warn a photo booth operator about a vulnerability in its system. The flaw reportedly exposed hundreds of customers’ private photos to anyone who knew where to look.

The researcher, who goes by the name Zeacer, said that a website operated by photo kiosk company Hama Film allowed anyone to download customer photos and videos without logging in. The Australian company provides photo kiosks for festivals, concerts, and commercial events. People take a snap and can both print it locally and also upload it to a website for retrieval later.

You would expect that such a site would be properly protected, so only you get to see yourself wearing nothing but a feather boa and guzzling from a bottle of Jack Daniels at your mate’s stag do. But reportedly, that wasn’t the case.

## You get a photo! You get a photo! Everyone gets a photo!

According to [TechCrunch](https://techcrunch.com/2025/12/12/flaw-in-photo-booth-makers-website-exposes-customers-pictures/), which has reviewed the researcher’s analysis, the website suffered from a well-known and extremely basic security flaw. TechCrunch stopped short of naming it, but mentioned sites with similar flaws where people could easily guess where files were held.

When files are stored at easily guessable locations and are not password protected, anyone can access them. Because those locations are predictable, attackers can write scripts that automatically visit them and download the files. When these files belong to users (such as photos and videos), that becomes a serious privacy risk.

At first glance, random photo theft might not sound that dangerous. But consider the possibilities. Facial recognition technology is widespread. People at events often wear lanyards with corporate affiliations or name badges. And while you might shrug off an embarrassing photos, it’s a different story if it’s a family shot and your children are in the frame. Those pictures could end up on someone’s hard drive somewhere, with no way to get them back or even know that they’ve been taken.

## Companies have an ethical responsibility to respond

That’s why it’s so important for organizations to prevent the kind of basic vulnerability that Zeacer appears to have identified. They can do that by properly password-protecting files, limiting how quickly one user can access large numbers of files, and making the locations impossible to guess.

They should also acknowledge researchers and fix vulnerabilities quickly when they’re reported. According to public reports, Hama Film didn’t reply to Zeacer’s messages, but instead shortened its file retention period from roughly two to three weeks down to about 24 hours. That might narrow the attack surface, but doesn’t stop someone from scraping all images daily.

So what can you do if you used one of these booths? Sadly, little more than assume that your photos have been accessed.

Organizations that hire photo booth providers have more leverage. They can ask how long images are retained, what data protection policies are in place, whether download links are password protected and rate limited, and whether the company has undergone third-party security audits.

Hama Film isn’t t...