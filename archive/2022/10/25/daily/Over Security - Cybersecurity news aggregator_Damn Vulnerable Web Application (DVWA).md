---
title: Damn Vulnerable Web Application (DVWA)
url: https://blog.g0tmi1k.com/dvwa/index/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:55.566423
---

# Damn Vulnerable Web Application (DVWA)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Damn Vulnerable Web Application (DVWA)

This is a [SERIES of blog posts](https://blog.g0tmi1k.com/dvwa/), which will all relate to one another, **but will take time**.

I'm publishing as I go, but will come back and edit them in places at a later date - as well as adding in videos.

Best to check back when there is the **"Undocumented" Bugs/Vulnerabilities** post (**that will be the last post**!) ;-).

---

The following posts will demonstrate **various environments, scenarios and setups**. This will cover a mixture of Operating Systems (**Linux & Windows**), range of web servers (**Apache, Nginx & IIS**), different versions of PHP (v5.4 & v5.6), databases (MySQL & MariaDB) as well as user permissions (inside the services and also the ones running services on the OS itself). DVWA also comes with a (outdated) **Web Application Firewall (WAF)** called PHP-IDS, which also has its own issues with! Lastly, there are **"undocumented" vulnerabilities** with DVWA's core which are either hidden bugs and/or unintended issues...

![DVWA Logo](/images/dvwa-logo.png "DVWA Logo")

*Note: This list will be updated with links, over the next few weeks - once they have been published!*

* [Login - *HTTP POST form brute force with CSRF token*](https://blog.g0tmi1k.com/dvwa/login/)
* **Brute Force**
  + [Low - *HTTP GET form brute force*](https://blog.g0tmi1k.com/dvwa/bruteforce-low/)
  + [Medium - *HTTP GET form brute force with time delays*](https://blog.g0tmi1k.com/dvwa/bruteforce-medium/)
  + [High - *HTTP GET form brute force with anti-CSRF token)*](https://blog.g0tmi1k.com/dvwa/bruteforce-high/)
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* **Command Injection** (RCE)
  + [Low - *Remote Code Execution*](https://blog.g0tmi1k.com/dvwa/rce-low/)
  + ~~Medium *(Bypassing blacklist patterns)*~~
  + ~~High *(Bypassing more blacklist filters)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* ~~**Cross-Site Request Forgery** (CSRF)~~
  + ~~Low *(CSRF)*~~
  + ~~Medium *(Referer header check. Links with XSS module)*~~
  + ~~High *(Anti-CSRF token used. Links with XSS module)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* ~~**File Inclusion** (LFI/RFI)~~
  + ~~Low *(LFI & RFI)*~~
  + ~~Medium *(Blacklisting patterns)*~~
  + ~~High *(Whitelisting with wildcards)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* ~~**File Upload** (FU)~~
  + ~~Low *(File Upload)*~~
  + ~~Medium *(Spoofed upload type)*~~
  + ~~High *(Merged image. Links with LFI module)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* ~~**Insecure CAPTCHA**~~
  + ~~Low *(CAPTCHA bypass)*~~
  + ~~Medium *(CAPTCHA bypass by using an extra field)*~~
  + ~~High *(Hardcoded/debug values)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* ~~**SQL Injection** (SQLi)~~
  + ~~Low *(SQLi)*~~
  + ~~Medium *(`mysql_real_escape_string`bypass - unable to use single/double quotes. POST requests in a dropdown menu)*~~
  + ~~High *(SQLi in SESSION carried over from another page)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* ~~**SQL Injection** (SQLi) **Blind**~~
  + ~~Low *(SQLi)*~~
  + ~~Medium *(`mysql_real_escape_string` bypass - unable to use single/double quotes. POST requests in a dropdown menu)*~~
  + ~~High *(SQLi in cookie value)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
* ~~**Cross Site Scripting** (XSS) **Reflected**~~
  + ~~Low *(XSS)*~~
  + ~~Medium *(XSS filter to remove `<script>`)*~~
  + ~~High *(XSS filter to remove `<*s*c*r*i*p*t`)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
  + ~~Phishing~~
* ~~**Cross Site Scripting** (XSS) **Stored**~~
  + ~~Low *(XSS)*~~
  + ~~Medium *(XSS filter to remove `<script>`. Limited input size)*~~
  + ~~High *(XSS filter to remove `<*s*c*r*i*p*t`. Limited input size)*~~
  + ~~Impossible~~
  + ~~PHPIDS (WAF)~~
  + ~~Phishing~~
* ~~**"Undocumented" Vulnerabilities**~~
  + [Login *(HTTP POST form brute force with CSRF token)*](https://blog.g0tmi1k.com/dvwa/login/)
  + ~~Core~~
    - ~~LFI~~
    - ~~XSS~~
  + ~~Brute Force & SQLi~~
  + ~~File Inclusion (LFI/RFI) & XSS~~

---

## Targets

Going to use a mixture of targets:

* 4x Operating Systems (Arch Linux, Raspbian Jessie, Windows Server 2012 & Windows XP)
* 2x Apaches (One Windows & One Linux)
* 2x Windows (One Apache & One IIS)
* 2x Linux (One Apache & One Nginx)
* 2x Raspberry Pis "B" (One v1 & One v2)
* 2x Virtual Machines

---

**`192.168.1.11` (aka: ArchPi)**

* Machine: **Raspberry Pi v1 "B"**
* Web Server: **Nginx v1.8.0** *(as "httpd")*
* Server Side Scripting: **PHP v5.6.14**
* Database: **MariaDB v10.0.21**
* OS: **Arch Linux 2015.10.01** / Linux archpi 4.1.9-1-ARCH #1 PREEMPT Thu Oct 1 19:15:46 MDT 2015 armv6l GNU/Linux

**`192.168.1.22` (Aka: Raspbian)**

* Machine: \*\*Raspberry Pi v2 "B"
* Web Server: **Apache v2.4.10** *(as "www-data")*
* Server Side Scripting: **PHP v5.6.13**
* Database: **MySQL v5.5.44**
* OS: **Raspbian Jessie September 2015** / Linux raspberrypi 4.1.7-v7+ #817 SMP PREEMPT Sat Sep 19 15:32:00 BST 2015 armv7l GNU/Linux

**`192.168.1.33` (aka: XAMPP)**

* Machine: **VM - 512MB / 1 CPU**
* Web Server: **Apache v2.4.10** *(as "SYSTEM")*
* Server Side Scripting: **PHP v5.4.31** *(`display_errors` enabled by default)*
* Database: **MySQL v5.5.39**
* OS: **Windows XP Professional SP3 ENG x86** (Using **XAMPP v1.8.2 package**)

**`192.168.1.44` (aka: IIS)**

* Machine: **VM - 2GB / 1 CPU**
* Web Server: **IIS v8.0** *(as "NT AUTHORITY\IUSR")*
* Server Side Scripting: **PHP v5.6.0**
* Database: **MySQL v5.5.45**
* OS: **Windows Server 2012 ENG x64**

Posted by g0tmi1kOct 20th, 2015 5:00 pm [dvwa](/./dvwa/)

[« Offensive Security Wireless Attacks (WiFu) + Offensive Security Wireless (OSWP)](/2014/01/offensive-security-wireless/ "Previous Post: Offensive Security Wireless Attacks (WiFu) + Offensive Security Wireless (OSWP)") [DVWA - Main Login Page - Brute Force HTTP POST Form with CSRF Tokens »](/dvwa/login/ "Next Post: DVWA - Main Login Page - Brute Force HTTP POST Form with CSRF Tokens")

[![g0tmi1k](/images/logo.png)](/)

# Recent Posts

* [DVWA - Brute Force (High Level) - Anti-CSRF Tokens](/dvwa/bruteforce-high/)
* [DVWA - Brute Force (Medium Level) - Time Delay](/dvwa/bruteforce-medium/)
* [DVWA Brute Force (Low Level) - HTTP GET Form [Hydra, Patator, Burp]](/dvwa/bruteforce-low/)
* [DVWA - Main Login Page - Brute Force HTTP POST Form With CSRF Tokens](/dvwa/login/)
* [Damn Vulnerable Web Application (DVWA)](/dvwa/index/)
* [Offensive Security Wireless Attacks (WiFu) + Offensive Security Wireless (OSWP)](/2014/01/offensive-security-wireless/)
* [Cracking the Perimeter (CTP) + Offensive Security Certified Expert (OSCE)](/2013/08/cracking-perimeter-ctp-offensive/)
* [pWnOS 2 (PHP Web Application)](/2012/09/pwnos-2-php-web-application/)
* [pWnOS 2 (SQL Injection)](/2012/09/pwnos-2-sql-injection/)
* [21LTR - Scene 1](/2012/09/21ltr-scene-1/)
* [Stripe CTF 2.0 (Web Edition)](/2012/09/stripe-ctf-20-web-edition/)
* [Kioptrix - Level 4 (Local File Inclusion)](/2012/02/kioptrix-level-4-local-file/)
* [Kioptrix - Level 4 (SQL Injection)](/2012/02/kioptrix-level-4-sql-injection/)
* [Kioptrix - Level 4 (Limited Shell)](/2012/02/kioptrix-level-4-limited-shell/)
* [Hackademic RTB2](/2012/01/hackademic-rtb2/)

[![RSS Feed](/images/social/rss.png "RSS")](/atom.xml "RSS") [![GitHub Profile](/images/social/github.png "GitHub")](https://github.com/g0tmi1k "GitHub") [![Twitter Profile](/images/social/twitter.png "Twitter")](https://twitter.com/g0tmi1k "Twitter") [![Google Plus Profile](/images/social/google-plus.png "Google Plus")](http://plus.google.com/110108403609022118432 "Google Plus")

Copyright © 2009-2021 g0tmi1k