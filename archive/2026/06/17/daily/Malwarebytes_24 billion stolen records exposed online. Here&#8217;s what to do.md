---
title: 24 billion stolen records exposed online. Here&#8217;s what to do
url: https://www.malwarebytes.com/blog/news/2026/06/24-billion-stolen-records-found-in-giant-data-dump-check-if-youre-affected
source: Malwarebytes
date: 2026-06-17
fetch_date: 2026-06-18T06:50:08.705214
---

# 24 billion stolen records exposed online. Here&#8217;s what to do

[Skip to content](#primary)

Search

Search Malwarebytes.com

Search for:

* [Sign In](https://my.malwarebytes.com/en/login)

  Sign in

  [Activate subscription >](https://my.malwarebytes.com/landing/activate)

  [Add devices or upgrade >](https://my.malwarebytes.com/landing/upgrade)

  [Renew subscription >](https://my.malwarebytes.com/landing/manual-renewal)

  [Secure Hub >](https://my.malwarebytes.com/secure-hub)

  Don’t have an account?
  **Sign up >**

  Sign In

* Products

  < Products

  **Solutions**

  + [Premium security antivirus](https://www.malwarebytes.com/premium)
  + [Privacy VPN](https://www.malwarebytes.com/vpn)
  + [Identity Theft Protection](https://www.malwarebytes.com/identity-theft-protection)
  + [Personal Data Remover](https://www.malwarebytes.com/personal-data-remover)
  + [Mobile security for iOS and Android](https://www.malwarebytes.com/mobile)

  + [Looking for small business protection? Visit Teams](https://www.malwarebytes.com/teams)

  **Free device cleaners**

  + [Malware and virus remover](https://www.malwarebytes.com/solutions/virus-scanner)
  + [AdwCleaner](https://www.malwarebytes.com/adwcleaner)
  + [Antivirus trial](https://www.malwarebytes.com/solutions/free-antivirus)

  **Free identity and personal data scanners**

  + [Digital footprint scanner](https://www.malwarebytes.com/digital-footprint)
  + [Personal data scanner](https://www.malwarebytes.com/personal-data-remover)

  **Free scam and ad blockers**

  + [Scam Guard](https://www.malwarebytes.com/solutions/scam-guard)
  + [Scam number checker](https://www.malwarebytes.com/scam-check/phone)
  + [Browser Guard](https://www.malwarebytes.com/browserguard)

  **[See all free tools](https://www.malwarebytes.com/free-tools)**
* [Pricing](http://www.malwarebytes.com/pricing)
* [Partners](https://www.malwarebytes.com/partners)
* About

  **Company**

  + [About Malwarebytes](https://www.malwarebytes.com/company)
  + [Why Malwarebytes?](https://www.malwarebytes.com/why-us)
  + [Jobs](https://www.malwarebytes.com/jobs)

  **[Newsroom](https://www.malwarebytes.com/press/)**
* Resources

  < Resources

  **Cybersecurity News**

  + [Malwarebytes Blog](https://www.malwarebytes.com/blog)
  + [Threat Center](https://www.malwarebytes.com/blog/threats)
  + [Lock & Code podcast](https://www.malwarebytes.com/blog/category/podcast)

  **Cybersecurity Basics**

  + [What is Malware?](https://www.malwarebytes.com/malware)
  + [What is Antivirus?](https://www.malwarebytes.com/cybersecurity/basics/antivirus)
  + [What is Phishing?](https://www.malwarebytes.com/phishing)
  + [See all topics](https://www.malwarebytes.com/cybersecurity)

  **Research reports**

  + [Modern Love in the Digital Age](https://www.malwarebytes.com/modernlove)
  + [Mobile Scam Report](https://www.malwarebytes.com/mobile-scams)
  + [How AI is reshaping trust, identity, and scams](https://www.malwarebytes.com/ai-scams)

  **Small Business Learning Hub**

  + [Small business news](https://www.malwarebytes.com/small-business#news)
  + [Upcoming Webinars](https://www.malwarebytes.com/small-business#webinar)

  **[See all resources](https://www.malwarebytes.com/resources)**
* Help

  < Help

  **[Malwarebytes Help Center](https://help.malwarebytes.com/hc)**

  **[Community Forums](https://forums.malwarebytes.com/)**

Free Download

Search
Search

Search Malwarebytes.com

Search for:

[Data breaches](https://www.malwarebytes.com/blog/category/data-breaches), [News](https://www.malwarebytes.com/blog/category/news)

# 24 billion stolen records exposed online. Here’s what to do

by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp) |
June 17, 2026

![databreach](https://www.malwarebytes.com/wp-content/uploads/sites/2/2026/06/databreach.jpg?w=600)

[![Add as a Preferred Source on Google](https://www.malwarebytes.com/wp-content/themes/malwarebytes/assets/src/images/google_preferred_source_badge_dark.png)](https://google.com/preferences/source?q=https://www.malwarebytes.com)

A newly discovered database containing 24 billion stolen records is a reminder that personal information from data breaches, phishing campaigns, and infostealer infections continues to circulate online.

The collection was exposed on the internet before being taken offline. While researchers can’t confirm exactly whose information was included, the discovery is a good opportunity to check whether your email addresses, passwords, or other personal data have already been exposed.

## What happened?

Researchers at [Cybernews](https://cybernews.com/security/24-billion-credentials-data-leak/) found a publicly exposed database holding more than 8.3 TB of data.

The data, consisting of 24 billion credential records, reportedly came from 36 sources, including numerous Telegram channels, prior breach compilations, collections of infostealer logs, and some datasets apparently exported directly from live servers.

Because the data came from different sources there are some differences in what the records contain and how they are organized.

Some records were structured infostealer logs containing usernames, email addresses, and plaintext passwords, and the associated login URL. Infostealers are a type of malware designed to steal sensitive information from infected devices, such as your home computer.

An infostealer log from a single infected device can include passwords stored across all browsers, active session cookies and tokens (including those that bypass multi-factor authentication), autofill data, device fingerprints, and sometimes crypto wallets or messaging accounts. The complete bundle is what ends up in logs such as those seen by the Cybernews researchers.

Roughly 1.7 billion of the records came from hacking-related Telegram channels, mainly English and Russian, including at least one that was focused on stolen credit card data.

The exposed database was hosted on an Elasticsearch cluster. Elasticsearch is a tool used to quickly store and search lots of data. If an Elasticsearch server lacks passwords, [authentication](https://www.malwarebytes.com/cybersecurity/basics/what-is-authentication), or network restrictions, it can be accessed by anyone who finds it online. Without protections such as passwords or a firewall, anyone can read, copy, change, or even delete its data.

Other documents in the dataset contained information about known vulnerabilities, articles about breaches, and social media posts about cyberattacks. This suggests the owner actively monitors security news and vulnerabilities and enriches the credential hoard with fresh breach information, either for a commercial “monitoring” service or for offensive use.

A few years ago, we [wrote about what was called the “mother of all breaches,”](https://www.malwarebytes.com/blog/news/2024/01/the-mother-of-all-breaches-26-billion-records-found-online) where the source of the dataset was later identified as data breach search engine Leak-Lookup.

This newly discovered 24 billion record exposure is in the same league as that previous mega‑dump, but appears more heavily weighted toward fresh infostealer logs, rather than older, static breach data.

Since the data was taken out of public view soon after the discovery, the researchers were unable to fully retrace everything they had found or determine how many duplicate records it contained. That’s reassuring because it reduces the chances of cybercriminals finding the database, but reused passwords may still put accounts at risk. And we still don’t know the purpose for the data collection in the first place.

## What to do now

It’s good to be aware of how much information about you is out there and who’s gathering it, but it’s even more important to know exactly which information they have, since that is what they can use against you.

1. Check if your data has been exposed online using our [Digital Footprint Portal](https://www.malwarebytes.com/digital-footprint).

[Check whether your data is exposed](https://w...