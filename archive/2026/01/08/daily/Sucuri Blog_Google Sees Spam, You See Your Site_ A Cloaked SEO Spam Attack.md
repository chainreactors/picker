---
title: Google Sees Spam, You See Your Site: A Cloaked SEO Spam Attack
url: https://blog.sucuri.net/2026/01/google-sees-spam-you-see-your-site-a-cloaked-seo-spam-attack.html
source: Sucuri Blog
date: 2026-01-08
fetch_date: 2026-01-09T03:30:33.434395
---

# Google Sees Spam, You See Your Site: A Cloaked SEO Spam Attack

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

* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [Website Security](https://blog.sucuri.net/category/website-security)

# Google Sees Spam, You See Your Site: A Cloaked SEO Spam Attack

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* January 8, 2026

![A Cloaked SEO Spam Attack on Google](https://blog.sucuri.net/wp-content/uploads/2026/01/A-Cloaked-SEO-Spam-Attack-on-google-820x385.png)

We recently handled a case where a customer reported strange SEO behavior on their website. Regular visitors saw a normal site. No popups. No redirects. No visible spam.

However, when they checked their site on Google, the search results were flooded with eBay-type-looking websites and “Situs Toto” gambling spam.

This is a professional-grade SEO cloaking attack. The malware turns the application into a double agent: it serves your genuine website content to real people but swaps it for a massive list of gambling ads the second a search engine bot crawls the page. By the time you notice the spam in your search results, the damage to your brand is often already done.

![Fake eBay casino spam page](https://blog.sucuri.net/wp-content/uploads/2026/01/fake-ebay-casino-spam-page.png)

This campaign is part of a larger trend of [rising online casino spam](https://blog.sucuri.net/2025/11/slot-gacor-the-rise-of-online-casino-spam.html). In this case, the attackers used a specific domain, **fugthatshit**[**.**]**baby**, to feed the spam content directly into the compromised server.

## What did we find?

The malware was embedded inside a legitimate file **pages/index/IndexHandler.php**. The file appeared normal at first glance and contained real application logic.

However, at the bottom of the file, additional PHP code was appended. This code silently fetched spam content from a remote domain and displayed it only to search engine crawlers.

The malicious domain involved was: **fugthatshit**[**.**]**baby**

The payload was hosted at: **hxxps://fugthatshit**[**.**]**baby/desktop/kindipublisher.txt**

This remote file contained large amounts of spam and gambling keywords, clearly designed for SEO manipulation.

We have [blocklisted this domain](https://www.virustotal.com/gui/url/22f6754b755602a93a15eab148cfc061ce78203480d08013a8819b0ef0f59b3e?nocache=1) and its IP address **104.21.50.131**.

[SiteCheck](https://sitecheck.sucuri.net/) currently detects it as **Spam**.

![Recognized as spam by SiteCheck](https://blog.sucuri.net/wp-content/uploads/2026/01/recognized-as-spam-by-SiteCheck.jpg)

## How the attack works

This malware uses user-agent cloaking. It checks who is visiting the site. If the visitor is Googlebot or another crawler, it injects spam content into the page output.

If the visitor is a real user, nothing happens.

This allows attackers to poison search engine results while staying invisible to site owners.

![How the attack works](https://blog.sucuri.net/wp-content/uploads/2026/01/how-the-attack-works.png)

## Indicators of Compromise (IoCs)

The most important indicators we observed include the malicious domain:

* **fugthatshit**[**.**]**baby**
* **hxxps://fugthatshit**[**.**]**baby/desktop/kindipublisher.txt**
* IP address: **104.21.50.131**

## Analysis of the malware

The file we analyzed was designed to look like a professional academic handler, meant to trick developers into thinking it was a necessary dependency.

### 1. Sniffing for search engine bots

The core of the cloaking logic begins with a “bot sniffer.” The script checks the visitor’s User-Agent string against a list of known search engine crawlers, including Googlebot, Bingbot, and Baiduspider.

If the visitor is a human using a browser like Chrome or Safari, the script does nothing and your website loads normally. But if it’s a bot, the malicious payload takes over.

### 2. Remote content retrieval via cURL

The malware doesn’t store the spam keywords on your server. Instead, it uses a function called fetchContentCurl to grab the latest “Situs Toto” links from an attacker-controlled server at **fugthatshit**[**.**]**baby**.

![Remote Content Retrieval via cURL](https://blog.sucuri.net/wp-content/uploads/2026/01/Remote-Content-Retrieval-via-cURL.png)

### 3. The content swap and exit

The final stage of the attack occurs when a bot is identified. The script pauses for a random interval to mimic natural server behavior, “echoes” the malicious spam content, then terminates the execution of the application.

By calling `exit;`, the malware ensures that the real application never ...