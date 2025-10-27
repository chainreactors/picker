---
title: Information stealer compromises legitimate sites to attack other sites
url: https://buaq.net/go-167401.html
source: unSafe.sh - 不安全
date: 2023-06-06
fetch_date: 2025-10-04T11:46:23.930277
---

# Information stealer compromises legitimate sites to attack other sites

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d7d95b39d4bfd2fdba86ede986e71e06.jpg)

Information stealer compromises legitimate sites to attack other sites

Security researchers at Akamai have published a blog about a new Mageca
*2023-6-5 22:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-167401.htm)
阅读量:17
收藏*

---

Security researchers at Akamai have [published a blog](https://www.akamai.com/blog/security-research/new-magecart-hides-behind-legit-domains) about a new [Magecart](https://www.malwarebytes.com/blog/threat-intelligence/2023/04/kritec-art)-alike web skimming campaign that uses compromised legitimate sites as command and control (C2) servers.

A web skimmer is a piece of malicious code embedded in web payment pages to steal personally identifiable information (PII) and credit card details from customers of the site.

Since the code is executed on the client's side, the malicious behavior is hard to detect by the website’s owner since it will not be picked up by web application firewalls (WAFs) and other measures to keep the server safe.

This campaign is different since it relies on legitimate but compromised sites to make the traffic look genuine. Since these sites normally operate as legitimate businesses, they are less likely to raise suspicion when connecting to a victim. The target sites are running digital content management systems like Magento, WooCommerce, WordPress, and Shopify, but contain a variety of [vulnerabilities](https://www.malwarebytes.com/blog/news/2023/01/update-your-wordpress-plugins-now-mass-backdoor-campaign-underway).

The Akamai researchers uncovered numerous digital commerce websites that have fallen victim, and say that it is reasonable to assume that there are additional legitimate websites that have been exploited as part of this extensive campaign.

Some of the victim organizations see hundreds of thousands of visitors per month which could potentially result in thousands of victims that have their credit card data and PII stolen. Especially since the campaign has been going unnoticed for close to a month for many of the victims.

In this campaign there were two kinds of victim sites:

* **Host victims**: Legitimate websites that are hijacked for the purpose of hosting the malicious code used in the attack. They are compromised to behave as an attacker-controlled server.
* **Web skimming victims**: Instead of directly injecting the attack code into the website's resources, the attackers employ small JavaScript code snippets as loaders to fetch the full attack code from the host victim website.

In some cases, the exploited host websites appear to have been abused in both ways.

The code used on the web skimming victims is designed to look like popular third-party services such as Google Tag Manager or Facebook Pixel. This method is popular among web skimmers because it helps the malicious code blend in seamlessly, disguising its true intentions.

## CMS security in a nutshell

Spilling your customers' PII and credit card details can be very damaging for your reputation, so it’s important to make sure they can visit and use your website safely.

There are a few obvious and easy-to-remember rules to keep in mind if you want to use a CMS without compromising your security:

* Choose your CMS with both functionality and security in mind
* Choose your plug-ins wisely
* Update as soon as you can
* Keep track of the changes to your site and their source code
* Use [2FA](https://www.malwarebytes.com/blog/news/2023/05/the-one-and-only-password-tip-you-need)
* Give user permissions (and their levels of access) a lot of thought
* Be wary of [SQL injection](https://www.malwarebytes.com/blog/news/2018/03/explained-sql-injection)
* If you allow uploads, limit the type of files to non-executables and monitor them closely.

For websites that require even more security, there are specialized vulnerability scanners and application firewalls that you may want to look into. This is especially true if you are a popular target for people that would love to deface or abuse your website.

If the CMS is hosted on your own servers, be aware of the dangers that this setup comes with some additional risks. Use network segmentation to keep the website server separated from other work servers.

## IOCs

Malwarebytes Browser Guard blocks the receiving domains of the stolen data:

byvlsa.com

chatwareopenalgroup.net

![Malwarebytes blocks chatwareopenalgroup.net](https://www.malwarebytes.com/blog/news/2023/06/easset_upload_file79639_267751_e.png)

---

文章来源: https://www.malwarebytes.com/blog/news/2023/06/information-stealer-compromises-legitimate-sites-to-attack-other-sites
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)