---
title: Woo Skimmer Uses Style Tags and Image Extension to Steal Card Details
url: https://blog.sucuri.net/2024/09/woo-skimmer-uses-style-tags-and-image-extension-to-steal-card-details.html
source: Sucuri Blog
date: 2024-09-13
fetch_date: 2025-10-06T18:26:14.855850
---

# Woo Skimmer Uses Style Tags and Image Extension to Steal Card Details

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
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Woo Skimmer Uses Style Tags and Image Extension to Steal Card Details

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* September 12, 2024

![Woo Skimmer Uses Style Tags and Image Extension to Steal Card Details](https://blog.sucuri.net/wp-content/uploads/2024/09/Blog-Post-Woo-Skimmer-Uses-Style-Tags-and-Image-Extension-to-Steal-Card-Details-820x385.png)

This post starts the same way many others do on this blog, and it will be familiar to those who keep up with website security: A client came to us having been notified by their payment processor that credit cards were being stolen from the checkout page of their eCommerce website. The question of course was *how*? During this investigation we uncovered a very interesting (and in fact, creative) way that threat actors were pilfering credit card details from this compromised website.

In this post we’ll reveal how we uncovered the malicious injection, perform some analysis on the unorthodox (although not entirely unique) ways the attackers concealed their injection and payload, how exactly it worked, and – as always – go over some ways in which eCommerce website administrators can protect themselves from becoming victims from such an attack.

Let’s get started!

## Inspecting Checkout

One of the very first things that is to be done while performing a [MageCart](https://sucuri.net/guides/what-is-magecart/) investigation is to inspect the checkout page. This usually involves simulating a transaction on the website by adding an item to the cart, navigating to the checkout page, and inspecting the code. Although, it should be mentioned that this method only works for JavaScript (rather than PHP) based skimmers.

Ensuring that we’re inspecting the checkout page is important because most carding malware attempts to stay hidden by *only appearing on urls which contain the string “checkout”*. This way the malware doesn’t load on every page (it doesn’t need to in order to accomplish what it wants to do) and is more easily concealed from the website owner and from external scanners. After all, it’s not often that an eCommerce store administrator is going to be purchasing products from themselves.

Now we have an item in our cart and have navigated to the page which asks us to enter in the payment details:

![Infected checkout page](https://blog.sucuri.net/wp-content/uploads/2024/09/checkout-page.png)

At this point we need to do 2-3 things to check if anything is amiss:

1. Check for any strange JavaScript loading on the page
2. Analyse the web traffic for any suspicious requests
3. Inspect the source code of the checkout page

For those of you who aren’t familiar, by right-clicking a webpage and selecting *view-source*, you can peek “behind the scenes” at some of the attributes and formatting which make up the web page that displays within your browser.

In this case, that was the first step in revealing how the client’s customers’ cards were being stolen. We came across this questionable item while scrolling through the source:

![Infected checkout source code](https://blog.sucuri.net/wp-content/uploads/2024/09/checkout-source-code.png)

This is some very peculiar looking code, and at first glance it’s not immediately apparent what it’s even doing. Note the **<style** (rather than **<script**) tags – more on that later.

The way that the malware was injected into the checkout page was actually pretty straightforward: All the attackers did was simply edit the checkout page source, either from **wp-admin** (using a compromised administrator user) or directly through the database:

![Checkout page wp-admin settings](https://blog.sucuri.net/wp-content/uploads/2024/09/checkout-wp-admin.png)

Which is a great reminder of why [securing your wp-admin panel](https://blog.sucuri.net/2021/07/basic-wordpress-hardening.html) is of the utmost importance!

## Reverse Engineering the Malware

So, now we must ask: How exactly was this gibberish code stealing credit card details? It doesn’t seem to reference anything obviously related to credit cards (such as numbers, expiry dates, or anything else you might expect).

Of particular note is this string right here lodged in the centre of the sample:

```
%/spuenlmrt-rbpotepw.ao-eoo-ee1dukc/tc/cd-ci%leeitilntonpwpxgls-do%
```

This, of course, looks like absolute rubbish. But in f...