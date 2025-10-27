---
title: Mal.Metrica Redirects Users to Scam Sites
url: https://blog.sucuri.net/2024/05/mal-metrica-redirects-users-to-scam-sites.html
source: Over Security - Cybersecurity news aggregator
date: 2024-05-04
fetch_date: 2025-10-06T17:17:06.431813
---

# Mal.Metrica Redirects Users to Scam Sites

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Mal.Metrica Redirects Users to Scam Sites

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* May 2, 2024

![](https://blog.sucuri.net/wp-content/uploads/2024/05/mal-metrica.png)

One of our analysts recently identified a new Mal.Metrica redirect scam on compromised websites, but one that requires a little bit of effort on the part of the victim. It’s another lesson for web users to be careful what they click on, and to be wary of anything suspicious that pops up in their browser — even if it’s coming from a website that they would otherwise trust.

## Please verify that you are a human

When visiting an infected website we are prompted with a (fake) human verification prompt:

![Fake human verification prompt](https://blog.sucuri.net/wp-content/uploads/2024/05/please_verify_you_are_a_human.png)

These prompts are quite common on the web these days, and most users would probably not think twice about clicking on it. After all, many of us have long since forgotten how much time has been spent clicking on fire hydrants, buses, and traffic lights in Google CAPTCHA verification prompts to prove that we are human.

While this prompt seems like a routine human-verification check it is actually completely fake — and is instead trying to trick the user into clicking the button thereby initiating a redirect to malicious and scammy websites.

## Simple image overlay links to malicious domain

Let’s take a quick look at the backend to see what is displaying this “verification prompt”:

![Image overlay code to conceal redirect to tmediacontent](https://blog.sucuri.net/wp-content/uploads/2024/05/image-overlay-650x94.png)

Rather than injecting JavaScript into the website code (which is very common for malware injections), the infection simply creates an image overlay with a link to the malicious domain **rapid.tmediacontent[.]com**.

Here we can see the redirect chain in the browser developer tools:

![Redirect chain from browser developer tools](https://blog.sucuri.net/wp-content/uploads/2024/05/browser-developer-tools.png)
 Lodged within the **footer-copyright** column of the **wp\_options** table, it’s a simple link initiated by clicking on an image loaded from the same domain.

## Mal.Metrica domain names

Judging by the domain names, it looks like this is likely a new campaign by the threat actors behind the Mal.Metrica campaign, which are behind quite a few other malicious domains:

```
content.streamfastcdn[.]com
content.gorapidcdn[.]com
cdn.metricastats[.]com
gll.metricaga[.]com
go.syndcloud[.]com
cloud.edgerapidcdn[.]com
ga.cdzanalytics[.]com
syndication.gcdnanalytics[.]com
cdn.metricastats[.]com
gll.metricaga[.]com
synd.edgecdnc[.]com
host.gsslcloud[.]com
fast.quickcontentnetwork[.]com
static.rapidglobalorbit[.]com
secure.globalultracdn[.]com
metrics.gocloudmaps[.]com
cache.cloudswiftcdn[.]com
host.cloudsonicwave[.]com
secure.gdcstatic[.]com
```

### What is Mal.Metrica?

Mal.Metrica is a massive malware campaign targeting known vulnerabilities in popular WordPress plugins. Similar to [Balada Injector](https://blog.sucuri.net/2023/04/balada-injector-synopsis-of-a-massive-ongoing-wordpress-malware-campaign.html), Mal.Metrica takes advantage of recently disclosed vulnerabilities to inject external scripts that utilize domain names resembling some CDN or web analytics services. The malware is known to inject Yandex.Metrica scripts to track performance of their injections.

This group has been actively exploiting vulnerabilities in [tagDiv Composer](https://blog.sucuri.net/2023/10/balada-injector-targets-unpatched-tagdiv-plugin-newspaper-theme-wordpress-admins.html), [Popup Builder](https://blog.sucuri.net/2024/03/new-malware-campaign-found-exploiting-stored-xss-in-popup-builder-4-2-3.html), [WP Go Maps](https://wpscan.com/vulnerability/f5687d0e-98ca-4449-98d6-7170c97c8f54/) and [Beautiful Cookie Consent Banner](https://wpscan.com/vulnerability/ff83570c-cbd5-4d04-9c4f-28c70dc2b854/) since at least 2023. We’ve detected this malware on a total of **17,449** compromised websites so far in 2024.

Mal.Metrica’s threat actors were recently identified in PatchStack’s latest [State of WordPress security report](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2024/#headline-1368-17052), which we collaborated on to help pinpoint the relationship between vulnerability exploits and massive malware infections.

## Unauthorized inje...