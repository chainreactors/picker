---
title: Fake “Fix It” Pop-Ups Target WordPress Sites via Malicious Plugin to Download Trojan
url: https://blog.sucuri.net/2024/10/fake-fix-it-pop-ups-target-wordpress-sites-via-malicious-plugin-to-download-trojan.html
source: Sucuri Blog
date: 2024-10-19
fetch_date: 2025-10-06T18:51:52.875286
---

# Fake “Fix It” Pop-Ups Target WordPress Sites via Malicious Plugin to Download Trojan

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

# Fake “Fix It” Pop-Ups Target WordPress Sites via Malicious Plugin to Download Trojan

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* October 18, 2024

![Fake “Fix it” Pop-ups Target WordPress Sites via Malicious Plugin to Download Trojan](https://blog.sucuri.net/wp-content/uploads/2024/10/Blog-Post-Fake-Fix-it-Pop-ups-Target-WordPress-Sites-via-Malicious-Plugin-to-Download-Trojan-820x385.png)

In our recent investigation, we discovered a new malware campaign targeting WordPress sites through a fake plugin, **universal-popup-plugin-v133**, which delivers deceptive browser fix pop-ups. This malware leverages social engineering tactics to deceive visitors into downloading malicious files, compromising their systems.

## Type of website impacted and the scope of infection

We reported a similar fake browser update in a recent [June article](https://blog.sucuri.net/2024/06/hundreds-sites-targeted-by-fake-chrome-update-pop-ups.html). The current version of this malware affects WordPress sites, and we saw a similar case in August, 2024 which is now detected by [SiteCheck](https://sitecheck.sucuri.net/) as **malware.fake\_update.7**.

At the moment, [31 sites](https://publicwww.com/websites/%22Right-click%2Bthe%2BStart%2Bbutton%2Band%2Brun%2B%27Windows%2BPower%2BShell%2BAdmin%27%22%2Bdepth%3Aall/) are infected with this malware.

The malware is a [Trojan](https://blog.sucuri.net/2024/02/remote-access-trojan-rat-types-mitigation-removal.html) that downloads from a compromised WordPress site after users are tricked into running it via fake pop-ups, where it then executes potentially harmful software on the user’s system.

## How the malware works

Once installed on a compromised WordPress site, the fake plugin **universal-popup-plugin-vXXX** generates pop-ups that detect the user’s browser and regional language, making the attack appear more personalized and legitimate.

### The Malicious Plugin Code

The plugin’s **index.php** file contains a malicious code that loads the JavaScript responsible for generating the fake pop-up:

![Malicious plugin code](https://blog.sucuri.net/wp-content/uploads/2024/10/malicious-plugin-code.png)

This code includes a JavaScript file named **assets/popup.js** which triggers the malicious pop-up on the frontend of the site.

The file **assets/popup.js** contains obfuscated code:

![](https://blog.sucuri.net/wp-content/uploads/2024/10/assets-obfuscated-code.png)

This obfuscated code decodes to:

![](https://blog.sucuri.net/wp-content/uploads/2024/10/obfuscated-code-decoded.png)

This code appends an iframe to the body of the webpage, loading the **popup.html** file from the plugin’s assets directory, which displays the fake browser update message.

When a user visits an infected site, they are shown an error message pop-up saying:

“**Aw, Snap!** Something went wrong while displaying this webpage.”

This fake error mimics legitimate browser messages, tricking users into believing that something is wrong with their browser.

![Fake Aw snap pop-up](https://blog.sucuri.net/wp-content/uploads/2024/10/aw-snap-popup.png)

The pop-up instructs the user to “install the root certificate” by clicking on a fake button labeled **How to Fix**. Upon clicking this button, a new pop-up appears with detailed instructions for running malicious commands on PowerShell.

![Fake aw snap pop-up copy](https://blog.sucuri.net/wp-content/uploads/2024/10/aw-snap-popup-copy.png)

The second pop-up provides the instructions to run a set of commands on your Windows PowerShell Admin that are copied on the user’s clipboard after they click the **copy** button. When users follow these instructions, the malicious code is executed in PowerShell, downloading an executable file.

Here is the set of instructions that get copied:

![](https://blog.sucuri.net/wp-content/uploads/2024/10/instructions.png)

This script hides the downloaded file from Windows Defender by adding it to an [exclusion list](https://support.microsoft.com/en-us/topic/what-are-exclusions-in-windows-security-8b248399-5e63-4a4b-897f-52ea2dddb962), downloads the malicious Trojan from the specified URL, and then silently executes it on the user’s machine.

The PowerShell script retrieves an executable file named **Setup.exe** from this link:

```
raw[.]githubusercontent[.]com/hohny43/Shell/refs/heads/main/Setup[.]exe
```

### The Setup.exe analysis

The **Se...