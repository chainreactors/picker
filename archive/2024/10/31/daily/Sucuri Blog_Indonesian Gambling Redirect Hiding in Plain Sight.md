---
title: Indonesian Gambling Redirect Hiding in Plain Sight
url: https://blog.sucuri.net/2024/10/indonesian-gambling-redirect-hiding-in-plain-sight.html
source: Sucuri Blog
date: 2024-10-31
fetch_date: 2025-10-06T18:52:33.612850
---

# Indonesian Gambling Redirect Hiding in Plain Sight

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

# Indonesian Gambling Redirect Hiding in Plain Sight

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* October 30, 2024

![Indonesian Gambling Redirect Hiding in Plain Sight](https://blog.sucuri.net/wp-content/uploads/2024/10/Indonesian-Gambling-Redirect-Hiding-in-Plain-Sight-820x385.png)

Many pieces of malware found over the years have been complex and difficult to find. Attackers often obfuscate their code to make it harder to track. Some pieces of malware require extensive reviews to uncover. But in other instances, that is not always the case. Threat actors find new ways to inject malware to avoid detection, and in some situations, they hide their malicious code in plain sight. Recently, I discovered a cleverly disguised malicious redirect, where attackers leveraged a popular redirect plugin in a WordPress site. By routing through an intermediary domain, they initiated the redirect process in a way that evaded detection.

Let’s review this injection more in depth.

## Redirect Symptoms

A client recently came to us concerned that their site was redirecting to an Indonesian gambling website, as seen below:

![Indonesian gambling site](https://blog.sucuri.net/wp-content/uploads/2024/10/indonesian-gambling-site.png)

Upon reviewing the symptoms, the infected website took a handful of seconds to load before the redirect occurred. Additionally, it occurred even with all javascript disabled, indicating it was not a script injection. The gambling domain the victim’s website redirected to was **surfatech-tis**[**.**]**com**. However, I came up empty handed when searching for this domain in the files and database. How could this be? In other samples found in the past, redirects like this that cannot be found by searching the domain via plain text are usually obfuscated in some fashion. More extensive reviews were performed and yet, I still came up short. Another tactic I decided to employ was to look at the recently modified files. That is when I stumbled upon a plugin called 301 redirects, which was added 2 days prior to my search. I decided to look at the redirects added in that plugin which revealed the malicious redirect chain.

## Uncovering the redirect via a popular redirect plugin

The 301 redirect plugin is a popular, verified tool that’s legitimately used in most cases. However, I decided to take a closer look inside to be sure. Inside the 301 redirect plugin was the domain **uad.uinfasbengkulu**[**.**]**ac**[**.**]**id**. Initially, I didn’t think this was the cause of the malicious redirect, until I remembered that the domain extension, **.id**, is an Indonesian based extension. Not only was the client’s site not based in Indonesia, redirects to Indonesian gambling sites are a common tactic attackers use when exploiting vulnerable sites.

Sure enough, after loading the domain uad.uinfasbengkulu[.]ac[.]id through <https://urlscan.io>, a sandbox testing site, it landed on surfatech-tis[.]com, which was the domain our client’s website was redirecting to. The attackers likely accessed the victim’s site through a vulnerability or compromised WordPress admin account, then proceeded to insert the intermediary domain in the redirect plugin after installing it.

## Moral of the story

To wrap up this case, we can conclude that not all malware relies on heavy obfuscation. Threat actors are constantly evolving, and developing new waves of infections. Some of these tactics include hiding malicious content in plain sight, through a popular verified plugin as seen above. This means that even seemingly harmless elements on a site can carry hidden risks. It is crucial that WordPress site owners take every possible step to protect their sites and stay vigilant against potential threats. Mitigation steps to better protect a WordPress site can be found below.

## Mitigation steps

To mitigate risk, there are a number of steps you can take to protect your website from serving malware to your clients:

1. **Keep your plugins, themes, and website software up-to-date:** Always patch to the latest version to help mitigate risk known [software vulnerabilities](https://blog.sucuri.net/category/vulnerability-disclosure). Website visitors should be sure to keep their browser and operating system up to date as well.
2. **Enforce [unique passwords](https://blog.sucuri.net/2022/08/how-to-create-secure-passwords-for-your-website.html) for all of you...