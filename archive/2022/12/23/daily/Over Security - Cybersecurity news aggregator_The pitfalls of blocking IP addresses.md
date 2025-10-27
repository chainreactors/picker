---
title: The pitfalls of blocking IP addresses
url: https://www.malwarebytes.com/blog/news/2022/12/the-pitfalls-of-blocking-ip-addresses
source: Over Security - Cybersecurity news aggregator
date: 2022-12-23
fetch_date: 2025-10-04T02:21:59.852705
---

# The pitfalls of blocking IP addresses

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

![a man complaining on the phone while looking at his laptop](https://www.malwarebytes.com/wp-content/uploads/sites/2/2022/12/asset_upload_file97903_253735.png?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# The pitfalls of blocking IP addresses

Posted: December 21, 2022
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

In August 2022, the Austrian court ordered the block of 11 IP addresses for copyright violations on 14 websites. Sadly, there was an undesirable side-effect—thousands of websites were rendered inaccessible to internet users in Austria for two days.

There are many possible reasons why governments would order Internet Service Providers (ISPs) to block specific IP addresses—from censorship to several different illegal activities like copyright infringements, fraud, and selling banned substances.

For the sake of the article we will focus on blocking for illegal activities in democratic countries, because censorship in more dictatorial states falls under very different considerations.

## The problem

Blocking an entire [IP address](https://www.malwarebytes.com/cybersecurity/basics/what-is-ip-address) because there are one or a few unwanted sites hosted on that IP address is unfair at one level to those that happen to be on the same IP address but are unaware of the illegal activities. Compare it to issuing a search warrant for an entire block because the owner of one house is suspected of doing something illegal.

But even though courts have an obligation to consider the rights of those not contributing to the illegal activities, blocking by IP address is something that happens too often according to content delivery network [Cloudflare that investigated the matter](https://blog.cloudflare.com/consequences-of-ip-blocking/).

> “Freedom House recently reported that [40 out of the 70](https://freedomhouse.org/report/freedom-net/2022/key-internet-controls) countries that they examined – which vary from countries like Russia, Iran and Egypt to Western democracies like the United Kingdom and Germany –  did some form of website blocking.”

## Sharing your IP

While it is easy to say that you shouldn’t share your IP with illegal, fraudulent, or even compromised sites, this is not how the internet works for the average user. For starters, there is a huge difference between the number of available IP addresses and the number of existing domains, let alone the possible number of domains. Even when you take [IPv6](https://www.malwarebytes.com/blog/news/2017/12/ipv6-its-waiting-for-you) into account, which allows for more unique IP addresses.

A regular website owner registers a domain and hosts the website on the server of a provider which is often the same one that registered the domain for them. They do not have a say over which other sites will be on the same server. The provider will decide this based on availability and load balancing. All a website owner can do is find a provider that is quick to respond in case there is a complaint about a site.

## Cloudflare

The problem in Austria was magnified because the court ordered the ISPs to block the IP addresses owned by Cloudflare that pointed to the websites they wanted to block. This rendered thousands of websites inaccessible.

> “In a network like Cloudflare’s, any single IP address represents thousands of servers, and can have even more websites and services — in some cases numbering into the millions — expressly because the Internet Protocol is designed to enable it.”

## Better blocking

Better blocking should be based on blocking closer to the source. If you have a problem with a domain, you should first try to block that particu...