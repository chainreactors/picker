---
title: Google sponsored ads malvertising targets password manager
url: https://www.malwarebytes.com/blog/threat-intelligence/2023/01/google-sponsored-ads-malvertising-targets-password-manager
source: Over Security - Cybersecurity news aggregator
date: 2023-02-02
fetch_date: 2025-10-04T05:30:55.095477
---

# Google sponsored ads malvertising targets password manager

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

![men in front of billboards](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/asset_upload_file78267_255951.png?w=736)

[News](https://www.malwarebytes.com/blog/category/news)
| [Threat Intel](https://www.malwarebytes.com/blog/category/threat-intel)

# Google sponsored ads malvertising targets password manager

Posted: January 31, 2023
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

We have recently written about [malvertising campaigns that leverage Google paid advertisements](https://www.malwarebytes.com/blog/news/2023/01/rogue-sites-causing-trouble-in-google-advert-results) to try and trick people into downloading [malware](https://www.malwarebytes.com/malware) instead of the software they were looking for. This malware then stole login credentials from the affected system.

Now, our researchers found that the [malvertising](https://www.malwarebytes.com/malvertising) campaigns via Google Ads are not just about software downloads and scams. They also include a  much more direct way to get at your login credentials by [phishing](https://www.malwarebytes.com/phishing) for users of popular [password managers](https://www.malwarebytes.com/what-is-password-manager) such as 1Password.

Below is a screenshot of what we found:

![false and legitimate ads side by side](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/easset_upload_file93968_255951_e.png)

Searching for “1password” we noticed two different sponsored advertisements as the top results. The first one leads to the legitimate domain 1password[.]com, but the second one points to start1password[.]com. Both claim to be for 1Password and both are [https](https://www.malwarebytes.com/blog/news/2018/05/https-why-the-green-padlock-is-not-enough) sites. Which makes it very hard for someone who is unfamiliar with the brand to determine which one to follow.

The following order in the search results is based on a metric called “Ad Rank.”

Google [says](https://support.google.com/google-ads/answer/1722122?hl=en) (emphasis by me):

> “Ad Rank is a value that’s used to determine where ads are shown on a page relative to other ads, and whether your ads will show at all. Your Ad Rank is recalculated each time your ad is eligible to appear. It competes in an auction, which could result in it changing each time depending on your competition, the context of the person’s search, and your ad quality at that moment.”

Just to point out that going for the top result is not always a sure fire way to get to the right one.

## Next phase

So where does the fake URL take us? To a very convincing phishing site. We have posted a comparison between the two login forms below.

![comparison of real login form and phishing site](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/easset_upload_file6286_255951_e.png)

The differences are so subtle, most people will fall for it. The only real difference is that following the legitimate link will keep you in the same domain because it goes to my.1password[.]com and the phishing link will take you to my1password[.]com, where the missing dot is the only real difference in the URLs.

## Secret key

The real difference is that phishing site will always have to ask for your secret key, because, well that’s what they are after. The legitimate 1Password will be able to retrieve it from your browser’s database and only ask for it if it has been deleted or if you are using 1Password on a new device or in a new browser. Deletion of the secret key can happen if you haven’t used the [password manager](https://www.malwarebytes.com/what-is-password-manager) for an extended period or if you have cleaned your brows...