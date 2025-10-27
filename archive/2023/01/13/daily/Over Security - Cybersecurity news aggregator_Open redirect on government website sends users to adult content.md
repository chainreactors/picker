---
title: Open redirect on government website sends users to adult content
url: https://www.malwarebytes.com/blog/news/2023/01/open-redirect-on-government-website-sends-users-to-adult-content
source: Over Security - Cybersecurity news aggregator
date: 2023-01-13
fetch_date: 2025-10-04T03:49:23.989984
---

# Open redirect on government website sends users to adult content

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

![street signs pointing the right way and the wrong way](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/asset_upload_file23353_253982.jpg?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Open redirect on government website sends users to adult content

Posted: January 11, 2023
 by [Christopher Boyd](https://www.malwarebytes.com/blog/authors/cboyd)

Fake websites and open redirects have conspired to make things awkward for a UKGOV website. The site in question, riverconditions(dot)environment-agency(dot)gov(dot)uk, was being [abused in search engine results](https://www.bleepingcomputer.com/news/security/fake-onlyfans-dating-sites-abuse-uk-environment-agency-open-redirect/) to redirect to various sites which aren’t associated with UKGOV—most of which were adult sites. Worse, it took a little bit of time to have the site taken down so the appropriate fixes could be made.

How did the scammers achieve this slice of open redirection activity? Let’s take a look.

## What is an open redirect?

An open redirect can be a way for a website to send you to somewhere you weren’t expecting. It works for all manner of scam attempts, and can be particularly convincing in cases of [phishing](https://www.malwarebytes.com/phishing). This was the case back in August 2021 when Microsoft [issued warnings](https://www.malwarebytes.com/blog/news/2021/08/microsoft-warns-about-phishing-campaign-using-open-redirects) about such a campaign.

Open redirects can also be involved in everything from token theft to dropping you onto a [malware](https://www.malwarebytes.com/malware) page. It’s a very versatile tool in the hands of a skilled attacker. Someone who is unfamiliar with the redirect process could well end up accusing your site of performing the malware install or phishing theft directly. In reality, your site was dragged along for the ride as a result of not sanitising or validating what’s taking place where open redirects are concerned.

A list of suggestions and recommendations for preventing unwanted redirects can be seen on the ever popular [OWASP cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) for this topic.

## What sites were the final destination for the redirects?

The primary aim for these redirects was to send visitors to pornography sites. Some of them made use of OnlyFans branding to presumably add a sense of legitimacy to the fake portals. Eventually, those sites would send visitors even further to dating sites with some sort of cheating or scandal theme.

Elsewhere, others found [various assorted redirects](https://twitter.com/WilliamNB/status/1611069975032389632) with additional folks claiming to have seen yet more cam site redirects on “environment agency” portals. It sounds like someone over at UKGOV is going to be spending a bit of overtime on this one.

## A difficult fix

In theory this should have been fairly easy to report, and have fixed. Unfortunately several issues conspired to make it all sound a bit tricky. As Bleeping Computer notes, this particular UKGOV site is [not part of the HackerOne bug bounty platform](https://www.bleepingcomputer.com/news/security/fake-onlyfans-dating-sites-abuse-uk-environment-agency-open-redirect/). As a result it took 24 hours to notify the right people at the Department for Environment, Food, and Rural Affairs (DEFRA) and an additional 48 hours for the site to be pulled. At time of writing, the site is still offline and has been since at least Monday.

As mentioned by the [researchers who found this issue](https://www.pentestpartners.com/security-blog/uk-gov-website-being-used-to-redirect-to-porn-sites/...