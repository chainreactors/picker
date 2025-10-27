---
title: Zero-day spells disaster for Bitcoin ATM
url: https://www.malwarebytes.com/blog/news/2023/03/zero-day-grants-big-payday-for-bitcoin-atm-attackers
source: Over Security - Cybersecurity news aggregator
date: 2023-03-27
fetch_date: 2025-10-04T10:46:52.224456
---

# Zero-day spells disaster for Bitcoin ATM

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

![Person using an ATM](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/asset_upload_file23860_262528.jpg?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Zero-day spells disaster for Bitcoin ATM

Posted: March 23, 2023
 by [Christopher Boyd](https://www.malwarebytes.com/blog/authors/cboyd)

[Bitcoin](https://www.malwarebytes.com/what-is-bitcoin) ATMs have experienced a severe bout of cash drain after a zero-day bug was exploited to [steal a total of $1.5 million in digital currency](https://arstechnica.com/information-technology/2023/03/hackers-drain-bitcoin-atms-of-1-5-million-by-exploiting-0-day-bug/). The ATMs, located in various convenience stores, function along the lines of regular banking ATMs except your dealings are all in the [cryptocurrency](https://www.malwarebytes.com/cryptocurrency) realm.

As Ars Technica notes, a particular feature of the affected ATMs is the ability to upload video. It’s not mentioned what these videos are used for (presumably security cameras), but the master server interface allowing for the video uploads is where things went horribly wrong.

From the General Bytes statement regarding the March 18 incident:

> The GENERAL BYTES [Cloud](https://www.malwarebytes.com/what-is-the-cloud) service and other standalone servers run by operators suffered security breaches. We noticed the first signs of a break-in on Friday night, right after midnight on Saturday, 18 March (UTC+1). We notified customers to shut down their CAS servers as soon as possible. The attacker could upload his java application remotely via the master service interface used by terminals to upload videos and run it using BATM user privileges. As a result, the attacker could send funds from hot wallets, and at least 56 Bitcoins were stolen before we could release the patch. The patch was released within 15 hours.

To make use of the [exploit](https://www.malwarebytes.com/exploits), the attacker uploaded a custom made application to the ATM application server used by the administration interface. In a nod to the evergreen security tip “Don’t allow things to autorun if you don’t need them to”, the application server allowed applications to start by default.

With this in place, the attacker was able to perform the below:

* Ability to access the database.
* Ability to read and decrypt API keys to access funds in hot wallets and exchanges.
* Send funds from hot wallets.
* Download user names and their password hashes, and turn off [2FA](https://www.malwarebytes.com/cybersecurity/basics/2fa).
* Ability to access terminal event logs, which can include private keys at the ATM.

56 bitcoins are currently worth a cool $1.5 million. It is very unlikely all of the stolen coins belonged to one person, but this is scant consolation for anyone affected. For now, General Bytes is collecting information on everyone affected to “validate losses”. It remains to be seen if anyone is able to recover their funds, but losing money in any cryptocurrency scenario is always a very risky business because  they are generally, by design, unable to roll back fraudulent transactions.

Interestingly, the affected company has a call to any security companies and individuals who feel they can assist in making the product safer.

## Keeping your hot wallet safe

Your cryptocurrency wallet type is an article [all to its own](https://www.malwarebytes.com/blog/news/2021/08/cold-wallet-hot-wallet-or-empty-wallet-what-is-the-safest-way-to-store-cryptocurrency), but in most cases you’re going to have a wallet which is hot or cold. A cold wallet is not connected to the Internet and is therefore the safest possible choice. A hot wallet comes with som...