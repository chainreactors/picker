---
title: WordPress sites backdoored with ad fraud plugin
url: https://www.malwarebytes.com/blog/threat-intelligence/2023/02/wordpress-sites-backdoored-with-ad-fraud-plugin
source: Over Security - Cybersecurity news aggregator
date: 2023-02-18
fetch_date: 2025-10-04T07:25:35.092404
---

# WordPress sites backdoored with ad fraud plugin

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

![WordPress sites backdoored with ad fraud plugin](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/02/asset_upload_file36223_258912.jpg?w=736)

[Threat Intel](https://www.malwarebytes.com/blog/category/threat-intel)

# WordPress sites backdoored with ad fraud plugin

Posted: February 16, 2023
 by [Jérôme Segura](https://www.malwarebytes.com/blog/authors/jeromesegura)

WordPress is an immensely popular content management system (CMS) powering over 43% of all websites. Many webmasters will monetize their sites by running ads and need to draw particular attention to search engine optimization (SEO) techniques to maximize their revenues.

But some people will take a shortcut to gaining traffic by engaging in legal but sometimes fraudulent practices. In this instance, we identified someone buying popunder traffic to promote their websites. A popunder is a very common occurrence online and consists of launching a secondary page under the current one. In itself, it could be considered simply an annoyance and is not malicious except when the website that is being launched uses various techniques to defraud advertisers.

We discovered a few dozen WordPress blogs using the same plugin that mimics human activity by automatically scrolling a page and following links within it, all the while a number of ads were being loaded and refreshed. The blogs would only exhibit this invalid traffic behavior when launched from a specific URL created by this plugin, otherwise they appeared completely legitimate.

In this post, we share the technical details behind this ad fraud scheme and any clues pointing to the developer of this WordPress plugin.

## Key findings

* About 50 WordPress blogs have been backdoored with a plugin called fuser-master
* One of the blogs performing this ad fraud had 3.8 M visits in January, with an average visit duration of 24:55 minutes and 17.50 pages per visit
* This plugin is being triggered via popunder traffic from a large ad network
* The WordPress sites are being loaded in a separate page underneath and display a number of ads
* The plugin contains JavaScript code that mimics the activity of a real visitor: scrolls the page, clicks on links, etc.
* The code also monitors for real human activity (mouse movement) and will immediately stop the fake scrolling when that happens

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/02/easset_upload_file79993_258912_e.png)

*Figure 1: Diagram summarizing ad fraud case*

## Fuser-master WordPress plugin

Recently we [blogged](https://www.malwarebytes.com/blog/threat-intelligence/2022/12/adult-popunder-campaign-used-in-mainstream-ad-fraud-scheme) about ad fraud involving a popunder as well, except in that case it was using an iframe to hide the ads. Here, there is nothing hidden at all and the ad fraud can only be deduced when the page is being scrolled down, and back up at random intervals. Because it is a popunder, anyone becomes an unwitting accomplice and does not see any of the fraudulent behavior.

In this investigation, we won’t be spending time on the ad network facilitating these popunders but we have a fairly good idea of which one it might be based on anti-debugging code that they used. What makes popunders particularly enticing for ad fraud is the fact they allow content to be loaded and remain until further action. Unlike the main browser window where a user can easily navigate away from the current website they are visiting, the popunder will remain open for several minutes or even hours, until it is closed.

We were able to trigger the popunder several times and noticed that the fraudsters were using several different blogs that all had the same ...