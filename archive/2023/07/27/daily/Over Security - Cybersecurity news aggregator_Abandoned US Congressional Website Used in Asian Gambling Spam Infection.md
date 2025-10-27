---
title: Abandoned US Congressional Website Used in Asian Gambling Spam Infection
url: https://blog.sucuri.net/2023/07/abandoned-us-congressional-website-used-in-asian-gambling-spam-infection.html
source: Over Security - Cybersecurity news aggregator
date: 2023-07-27
fetch_date: 2025-10-04T11:55:56.565843
---

# Abandoned US Congressional Website Used in Asian Gambling Spam Infection

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Security Education](https://blog.sucuri.net/category/security-education)
* [Website Security](https://blog.sucuri.net/category/website-security)

# Abandoned US Congressional Website Used in Asian Gambling Spam Infection

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* July 26, 2023

![Abandoned US Congressional Website Used in Asian Gambling Spam Infection](https://blog.sucuri.net/wp-content/uploads/2023/07/Asian-Gambling-Spam-820x385.png)

Website owners and developers tend to buy a lot of domains. With different projects on the go and working with multiple different clients at any given time it can be a challenge to keep track of all your inventory. Sadly, when old websites and domains get forgotten about they can be preyed upon by attackers and misused for their own ends.

We’ve recently observed a campaign of blackhat SEO infections peddling Asian gambling spam that have been abusing one such domain that appears to have been forgotten about. It also just so happens to be an old campaign website of a former sitting US congressperson.

## Running for Congress

The website appears to be an old campaign website for a former representative of the US Congress. He’s no longer a sitting representative and has moved onto another prominent official position in his state, which might help explain why one of their old campaign-trail domains was forgotten about and abandoned.

We can see an archived version of the campaign website here below:

[![Archived version of the Congress now-spam site](https://blog.sucuri.net/wp-content/uploads/2023/07/congress-site-with-spam-650x308.png)](https://blog.sucuri.net/wp-content/uploads/2023/07/congress-site-with-spam.png)

Archived version of the now-spam site

It appears that in late 2022 one of their old, no-longer-used congressional campaign domains expired and was put up for sale:

[![The domain name 4congress.com is for sale.](https://blog.sucuri.net/wp-content/uploads/2023/07/congress-domain-sale-650x383.png)](https://blog.sucuri.net/wp-content/uploads/2023/07/congress-domain-sale.png)

Spammers appear to have swooped in several months after that, bought up the domain and changed it to their own hosting:

![Registry database reveals purchase of expired domain](https://blog.sucuri.net/wp-content/uploads/2023/07/registry-database.png)

We can confirm this by checking the historical A-record data when it got switched over to NameCheap hosting (where the domain was re-registered). The hosting IP change is reflected here when the spammers first registered and later moved the domain that was sitting vacant:

![Historical a-record data](https://blog.sucuri.net/wp-content/uploads/2023/07/historical-a-record-data.png)

## A simple spam infection

The malware which gets injected into hacked websites is pretty simple and so far has been found lodged at the bottom of the active theme’s **footer.php** file:

![Simple spam infection found in footer.php file](https://blog.sucuri.net/wp-content/uploads/2023/07/spam-infection.png)

All it does is use **file\_get\_contents** to grab the content of the spammy text file sitting on the compromised domain and echos out the contents:

[![Display none used to conceal spam on hacked site](https://blog.sucuri.net/wp-content/uploads/2023/07/display-style-spam-650x302.png)](https://blog.sucuri.net/wp-content/uploads/2023/07/display-style-spam.png)

When we view the source of the infected websites we can see it appear, using **display:none** to hide from view from regular website visitors (but search engines will still see it) which is standard practice for [black hat SEO](https://blog.sucuri.net/2023/02/what-is-black-hat-seo.html) spammers:

[![List of spam domains hidden with display:none on a spam site](https://blog.sucuri.net/wp-content/uploads/2023/07/spam-websites-650x397.png)](https://blog.sucuri.net/wp-content/uploads/2023/07/spam-websites.png)

But what is it that this spam injection is promoting? The gambling websites themselves are about what you would expect:

[![Casino spam landing page associated with domain shadowing](https://blog.sucuri.net/wp-content/uploads/2023/07/asian-casino-spam-650x519.png)](https://blog.sucuri.net/wp-content/uploads/2023/07/asian-casino-spam.png)

Not exactly a reputable-looking online casino, if there ever was such a thing.

As you can see in the above screenshots they all contain the string “**slot-server**” and all appear to be subdomains of websites completely unrelated to online casinos and gambling, indicating that these victim websites had their DNS records compromised (either through a...