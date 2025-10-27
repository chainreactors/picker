---
title: Attackers Abuse Swap File to Steal Credit Cards
url: https://blog.sucuri.net/2024/07/attackers-abuse-swap-file-to-steal-credit-cards.html
source: Over Security - Cybersecurity news aggregator
date: 2024-07-23
fetch_date: 2025-10-06T17:44:23.746982
---

# Attackers Abuse Swap File to Steal Credit Cards

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

# Attackers Abuse Swap File to Steal Credit Cards

[![](https://secure.gravatar.com/avatar/067bd4ee574f53bb79d411d83b5cc84ea794c798f945cb84a001cbe05fee65df?s=60&d=mm&r=g)](https://blog.sucuri.net/author/matt-morrow)

[Matt Morrow](https://blog.sucuri.net/author/matt-morrow)

* July 19, 2024

![Attackers abuse swap file to steal credit cards](https://blog.sucuri.net/wp-content/uploads/2024/07/Blog-Post-Credit-Card-Stealing-Malware-820x385.png)

When it comes to website security, sometimes the most innocuous features can become powerful tools in the hands of attackers. Such was the case in a recent incident we investigated, where bad actors exploited the humble swap file to maintain a persistent credit card skimmer on a Magento e-commerce site. This clever tactic allowed the malware to survive multiple cleanup attempts — that is, until our analysts wrapped up their investigation.

In this post, we’ll peel back the layers of this sophisticated ecommerce attack, offering valuable insights into how you can protect your own online store from similar threats.

Let’s take a look!

## Inspecting the malware

When navigating to the compromised website’s checkout page, we could see an interesting script buried way down in the page source.

![Interesting script buried in checkout page](https://blog.sucuri.net/wp-content/uploads/2024/07/hidden-script.png)

The script had all the usual indicators of malware, like base64 encoded variables and hex encoded strings. But once decoded, we could see some clear indicators that the script was watching for credit card details.

### Malicious checkout page behavior

The following snippet enables a checkout button and adds custom bindings to the normal click function on the compromised checkout page.

![snippet enables a checkout button and adds custom bindings to the normal click function on the compromised checkout page](https://blog.sucuri.net/wp-content/uploads/2024/07/custom-bindings.png)

Once the checkout button is clicked, the script captures data entered into the credit card form via a **querySelectorAll** function as seen here.

![script captures data entered into the credit card form via a querySelectorAll function](https://blog.sucuri.net/wp-content/uploads/2024/07/querySelectorAll.png)

Several other variations of the function elsewhere in the script capture sensitive information such as name, address, card number and other data needed by the attackers to utilize the stolen card details. We can also see a domain, **amazon-analytic[.]com**, used by the attackers to retrieve the stolen credit card details.

![amazon-analytic[.]com used by the attackers to retrieve the stolen credit card details](https://blog.sucuri.net/wp-content/uploads/2024/07/amazon-analytic-domain.png)

This amazon-analytic[.]com domain was registered in February 2024 and has also been seen used in other previous cases of credit card theft. Note the use of the brand name; this tactic of leveraging popular products and services in domain names is often used by bad actors in an attempt to evade detection.

## Tracing the source to bootstrap.php

Once we had the checkout page decoded, it was time to find the source. Further investigation led us to the Magento **app/bootstrap.php** file which had been completely replaced from the official version.

![Replaced Magento app/bootstrap.php file](https://blog.sucuri.net/wp-content/uploads/2024/07/appbootstrap-php.png)

Decoding that base64 content revealed the exact malicious script found in the checkout page source. We also located the **curl** function used by the attackers to exfiltrate the stolen data to their external domain.

The **ob\_filter\_callback** function is used to add the skimmer script to web pages if their URLs contain the keyword “checkout” and the pages were requested using the GET method.

![ob_filter_callback function is used to add the skimmer script to web pages](https://blog.sucuri.net/wp-content/uploads/2024/07/ob_filter_callback.png)

## The malware removal process

We figured that removing the malware should be as simple as replacing **app/bootstrap.php** with the correct version and then clearing caches, since we know the content there is what we are seeing in the checkout, right? Well, not in this case.

Once we replaced the file with the correct contents, we noticed the script was still loading in checkout. It’s not impossible for files to be reinfected pretty quickly, so we took another look at **bootstrap.php** with our malware cleanup tools and noticed that the malware was back.

What was especially strange was that wh...