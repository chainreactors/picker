---
title: Warning Hackers could take over your email account by stealing cookies, even if you have MFA
url: https://www.malwarebytes.com/blog/news/2024/11/warning-hackers-could-take-over-your-email-account-by-stealing-cookies-even-if-you-have-mfa
source: Instapaper: Unread
date: 2024-12-01
fetch_date: 2025-10-06T19:38:44.727872
---

# Warning Hackers could take over your email account by stealing cookies, even if you have MFA

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

![stealing from cookie jar](https://www.malwarebytes.com/wp-content/uploads/sites/2/2024/04/stealing-cookies.jpg?w=1200)

[News](https://www.malwarebytes.com/blog/category/news)
| [Threats](https://www.malwarebytes.com/blog/category/threats)

# Warning: Hackers could take over your email account by stealing cookies, even if you have MFA

Posted: November 5, 2024
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

The Federal Bureau of Investigation (FBI) has [issued a warning](https://www.fbi.gov/contact-us/field-offices/atlanta/news/cybercriminals-are-stealing-cookies-to-bypass-multifactor-authentication) that cybercriminals are taking over email accounts via stolen session [cookies](https://www.malwarebytes.com/cybersecurity/computer/what-are-tracking-cookies), allowing them to bypass the multi-factor [authentication](https://www.malwarebytes.com/cybersecurity/basics/what-is-authentication) (MFA) a user has set up.

Here’s how it works.

Most of us don’t think twice about checking the “Remember me” box when we log in. When you log in and the server has verified your authentication—straight away or after using MFA–the server creates a session and generates a unique session ID. This session ID is stored in a session cookie (or a “Remember-Me cookie” as the FBI calls it) on your browser, which is typically valid for 30 days.

Every time you return to that website within the time frame, you don’t need to log in. That’s really convenient… unless someone manages to steal that cookie from your system.

If someone steals the session cookie, they can log in as you—even if you have MFA enabled.

This is particularly relevant for email handlers that have an online—webmail—component. This includes major players like Gmail, Outlook, Yahoo, and AOL.

With access to your email account, a cybercriminal can find a lot of useful information about you, such as where you bank, your account numbers, your favorite shops, and more. This information could then be used for targeted cyberattacks that mention information that’s relevant to you only, leaving you more likely to fall for them.

Cybercriminals could use your account to spread [spam](https://www.malwarebytes.com/spam) and [phishing emails](https://www.malwarebytes.com/phishing) to your contacts. And perhaps most worrying of all, once an attacker is in your email account they can reset your passwords to your other accounts and login as you there too.

How do these criminals get their hands on your session cookies? There are several ways.

On very rare occasions, session cookies can be stolen by you visiting a malicious website, or via a Machine-in-the-Middle (MitM) attack where a cybercriminal can intercept traffic and steal cookies if they’re not protected by [HTTPS](https://www.malwarebytes.com/blog/news/2018/05/https-why-the-green-padlock-is-not-enough) on an unsecured network.

However, session cookies are usually stolen by [malware](https://www.malwarebytes.com/malware) on the your device. Modern information-stealing malware is capable of, and even focuses on, stealing session cookies as part of its activity.

## How to keep your email account safe

There are a few things you can do to stay safe from the cookie thieves:

* Use [security software](https://www.malwarebytes.com/premium) on every device you use.
* Keep your devices and the software on them up to date, so there aren’t any known vulnerabilities on them.
* Decide whether you think it’s worth using the Remember me option. Is convenience worth the risk in this situation?
* Delete cookies, or—even better—log out when you are done. That should also remove or invalidate the session ID from the server, so nobody can use...