---
title: Konami Code Backdoor Concealed in Image
url: https://blog.sucuri.net/2023/02/konami-code-backdoor-concealed-in-image.html
source: Sucuri Blog
date: 2023-02-03
fetch_date: 2025-10-04T05:33:51.891756
---

# Konami Code Backdoor Concealed in Image

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

# Konami Code Backdoor Concealed in Image

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* February 2, 2023

![Konami Code Backdoor Concealed in front.jpeg Image](https://blog.sucuri.net/wp-content/uploads/2023/02/23-BlogPost_Feature-Image_1490x700_Konami-Code-Backdoor-820x385.jpg)

Attackers are always looking for new ways to conceal their malware and evade detection, whether it’s through new forms of [obfuscation](https://blog.sucuri.net/2020/08/string-concatenation-obfuscation-techniques.html), [concatenation](https://blog.sucuri.net/2021/07/magecart-swiper-uses-unorthodox-concatenation.html), or — in this case — unorthodox use of image file extensions. One of the most common backdoors that we have observed over the last few months has been designed to evade detection by placing the payload in an image file and requiring some additional tricks to unlock it.

In this post we’ll explore how this backdoor works, what sorts of malware we’ve seen in conjunction with it, as well as how to prevent your website from becoming infected.

**Contents:**

* **[Backdoor analysis](#backdoor-analysis)**
* **[Malware footprint](#footprint)**
* **[Why jpeg?](#jpeg)**
* **[core-stab](#core-stab)**
* **[task-controller](#task-controller)**
* **[Variants](#variants)**
* [**Mitigation steps**](#mitigation)

## Backdoor analysis

The malware described in this post is not exactly new; we first detected it back in 2019 within a compromised Drupal environment. However, over the last few months it appears to have surged in popularity among attackers.

This backdoor tends to be uploaded into WordPress environments as a bogus/fake plugin with the following names:

```
./wp-content/plugins/core-stab
./wp-content/plugins/task-controller
```

In fact, over the last three months alone these fake plugins account for nearly 15,000 separate detections in our malware logs. It is one of the most commonly identified backdoors that we have seen over the last period — and we presume it’s likely bundled into a popular attack-kit used by threat actors to compromise WordPress websites.

The backdoor consists of two files lodged within the following bogus plugin directories:

* ./wp-content/plugins/**core-stab/index.php**
* ./wp-content/plugins/**core-stab/front/front.jpeg**
* ./wp-content/plugins/**task-controller/index.php**
* ./wp-content/plugins/**task-controller/application/front.jpg**

With the **index.php** file containing nothing but the following code:

![front.jpeg file found in index.php](https://blog.sucuri.net/wp-content/uploads/2023/02/front-jpeg.png)

@include(‘./front/front.jpeg);

### Malware footprint

The footprint of this malware is tiny; all it does is include the **front.jpeg** file — nothing more. To make it appear more legitimate, attackers have also included the typical fake plugin information pretending to be an official WordPress file.

Although many malicious plugins go out of their way to hide themselves from view in the WordPress administrator interface, interestingly this infection makes no such attempt:

[![Fake Core Stab plugin clearly visible in Admin dashboard. ](https://blog.sucuri.net/wp-content/uploads/2023/02/fake_corestab_plugin.png)](https://blog.sucuri.net/wp-content/uploads/2023/02/fake_corestab_plugin.png)

Fake Core Stab plugin clearly visible in Admin dashboard.

The **core-stab** and **task-controller plugins** contain two separate malicious samples which appear to work together to assist attackers in further compromising environments. Before we take a look at each of them and see what we find, let’s briefly explain why they’ve configured their backdoors in this way.

## Why bother with a jpeg?

You might be wondering why the attackers bother with this extra step of including the image, rather than just uploading a good old fashioned malicious PHP script or [web shell](https://blog.sucuri.net/2024/04/web-shells.html). The answer lies in how many security scanners work.

For performance reasons security scans **will often not scan image files by default.** Many WordPress websites (especially ones that have been on the web for many years) contain hundreds — or even thousands — of image files and scanning them all would add a tremendous amount of time to a security scan.

Also, image files by themselves are not executable and (generally speaking) aren’t regarded as a risk. For this reason, most standard security scans will fo...