---
title: New Wave of SocGholish cid=27x Injections
url: https://blog.sucuri.net/2022/11/new-wave-of-socgholish-cid27x-injections.html
source: Sucuri Blog
date: 2022-11-24
fetch_date: 2025-10-03T23:39:07.879927
---

# New Wave of SocGholish cid=27x Injections

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

# New Wave of SocGholish cid=27x Injections

[![](https://secure.gravatar.com/avatar/292c42da0d9f929a9405e6ce269f101cc888f5c5cbcf8006e131c9bed042c80d?s=60&d=mm&r=g)](https://blog.sucuri.net/author/denis)

[Denis Sinegubko](https://blog.sucuri.net/author/denis)

* November 23, 2022

![New Wave of SocGholish cid=27x Injections](https://blog.sucuri.net/wp-content/uploads/2022/11/BlogPost_Feature-Image_1490x700_New-Obfuscation-Techniques-in-SocGholish-cid-272-820x386.png)

On November 15th, Ben Martin reported [a new type of WordPress infection](https://blog.sucuri.net/2022/11/new-socgholish-malware-variant-uses-zip-compression-evasive-techniques.html) resulting in the injection of [SocGholish scripts](https://blog.sucuri.net/2022/08/socgholish-5-years-of-massive-website-infections.html) into web pages. The attack loads zipped malicious templates from WordPress theme and fake plugins files before extracting the SocGholish script, which is saved as an encrypted value inside the **wp\_option** table of the WordPress database. One of its distinguishing features is the **cid=272** parameter included in the SocGholish URLs.

During the past two weeks, **cid=272** has quickly become the second most prevalent variation of SocGholish infection (after [NDSW/NDSX](https://blog.sucuri.net/2022/06/analysis-massive-ndsw-ndsx-malware-campaign.html)) with **100+** detections per day on average.

Ben noted that the approach used by the **cid=272** actor was quite clever: it minimizes the malware footprint in server files and requires an update of only a single database option when the attacker wants to update their injected scripts. But on the other hand, it still contained many moving parts making reinfections and SocGholish script updates more difficult.

One of these moving parts is the tell-tale **siteurl comment** which hackers append to the top of their SocGholish script. This comment contains the domain name of the compromised site — and in order to update the malware, attackers needed to generate a new value for the database option individually for every hacked domain.

![SocGholish script containing prepended siteurl comment](https://blog.sucuri.net/wp-content/uploads/2022/11/socgholish_script_prepended_siteurl_comment.png)

SocGholish script containing prepended siteurl comment

But in recent variants, this siteurl comment has since been removed. And subsequently, attackers have applied new changes to the **cid=272** operation. Let’s review some of these recent modifications.

**Contents:**

* **[Siteurl comment removed](#siteurl)**
* **[New obfuscation techniques](#obfuscation)**
* **[Domain shadowing and script variations](#domain-shadowing)**
* **[Malware footprint](#footprint)**
* **[Simplied script tags](#script-tags)**
* **[Mitigation](#mitigation)**

## Siteurl comment removed

Our forecast from our last article was accurate: we speculated that attackers would eventually simplify their operation. And one of the most obvious changes in this latest evolution of **cid=272** is that attackers got rid of the siteurl comment entirely.

When you decode the payload stored in **wp\_options.<theme-name>-template-plugin** database option, the **code** variable now contains only the malicious script.

![Decoded wp_options.<theme-name>-template-plugin database option with no siteurl comment](https://blog.sucuri.net/wp-content/uploads/2022/11/decoded_wp_options_template_plugin.png)

Decoded wp\_options.-template-plugin database option with no siteurl comment

No unnecessary comments are present in the code and the compromised domain name is no longer referenced within the malware.

## New SocGholish obfuscation

Another noticeable change is the new obfuscation for the SocGholish script itself.

![New SocGholish obfuscation](https://blog.sucuri.net/wp-content/uploads/2022/11/new_socgholish_obfuscation-1.png)

New SocGholish obfuscation

This time, the obfuscation seems to be generated by the popular **javascript-obfuscator** library. It’s not typical for SocGholish — during the past 5 years, attackers have only used [pretty simple obfuscation techniques](https://blog.sucuri.net/2022/08/socgholish-5-years-of-massive-website-infections.html#evolution-socgholish-obfuscation-techniques) thus far to evade detection.

![Decoded SocGholish script](https://blog.sucuri.net/wp-content/uploads/2022/11/decoded_socgholish_script.png)

Decoded SocGholish script

Nonetheless, when we deobfuscate this script we end up with the recognizable SocGholish code. It loads the stage 2 script from **hxxps://mini.ptipexcel[.]com/report?r**=**dj1...