---
title: Magento Credit Card Stealer Disguised in an <img> Tag
url: https://blog.sucuri.net/2025/02/magento-credit-card-stealer-disguised-in-an-tag.html
source: Sucuri Blog
date: 2025-02-13
fetch_date: 2025-10-06T20:34:40.471292
---

# Magento Credit Card Stealer Disguised in an <img> Tag

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

* [Ecommerce Security](https://blog.sucuri.net/category/ecommerce-security)
* [Magento Security](https://blog.sucuri.net/category/magento-security)
* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)

# Magento Credit Card Stealer Disguised in an <img> Tag

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* February 12, 2025

![Magento Credit Card Stealer Disguised in an img Tag](https://blog.sucuri.net/wp-content/uploads/2025/02/Magento-Credit-Card-Stealer-Disguised-in-an-img-Tag-820x385.png)

Recently, we had a client come to us concerned that their website was infected with credit card stealing malware, often referred to as [MageCart](https://sucuri.net/guides/what-is-magecart/). Their website was running on Magento, a popular eCommerce content management system that skilled attackers often target to steal as many credit card numbers as possible. The goal of attackers who are targeting platforms like Magento, WooCommerce, PrestaShop and others is to remain undetected as long as possible, and the malware they inject into sites is often more complex than the more commonly found pieces of malware impacting other sites.

In this case, the malware affecting the client follows the same goal — staying hidden. It does this by disguising malicious content inside an <img> tag, making it easy to overlook. Let’s take a look at this sneaky and well hidden piece of malware.

## Encoded <img> tag code

In order to find this malicious code, we must first go to the infected website, add an item to the cart, and observe the page source at the end of the checkout process, once it is time to submit credit card details. Most MageCart malware only loads on the checkout page in order to try to avoid detection, so it’s important to follow the whole process during investigation.

It is also important to be at the portion of the checkout process that includes the input field for credit card information. After following the steps above, reviewing the page source shows the following code:

![source code](https://blog.sucuri.net/wp-content/uploads/2025/02/source-code.png)*(Note: This is only a partial snapshot of the code.)*

It’s common for <img> tags to contain long strings, especially when referencing image file paths or base64 encoded images, along with additional attributes like height and width. However, upon closer inspection, you’ll notice that following the <img> tag is a large chunk of Base64-encoded content, with no reference to an actual image file or indication that it is actually an image.

Typically, references to images in an <img> tag are file paths or URLs, whereas in this case, the data is embedded directly as Base64-encoded content that doesn’t represent actual image data. While using Base64 in an <img> tag is technically legitimate and commonly used when we’re talking about very small images like icons, it definitely stands out in this context.

What makes this even more suspicious is its location—on the checkout page and nowhere else on the site. The <img> tag is essentially a decoy that has malicious JavaScript hidden inside the base64 encoded data. The location of this code and the utilization of base64 within an <img> tag makes it clear that this code warrants further investigation.

## Activation of the payload within the browser

Before decoding the base64 encoded content, let’s first go over how this code activates in a victim’s browser.

The base64 encoded content is followed by a **onerror** function, which is a function that is triggered if an error occurs when attempting to load a file or image. This can be seen below:

![onerror function](https://blog.sucuri.net/wp-content/uploads/2025/02/onerror-function.png)*(Note: This is only a partial snapshot of the code.)*

If an image fails to load, the **onerror** function will trigger the browser to show a broken image icon instead. However, in this context, the **onerror** event is hijacked to execute JavaScript instead of just handling the error.

This attack is harder to detect because the browser inherently trusts the **onerror** function. Since it’s a standard event handler used for legitimate purposes (like handling image loading errors), security tools may overlook it. Additionally, <img> tags are often overlooked because they’re generally considered harmless, can contain large amounts of content, and are typically used for displaying images. This malware is unique because oftentimes, anyone looking at it would think it is a...