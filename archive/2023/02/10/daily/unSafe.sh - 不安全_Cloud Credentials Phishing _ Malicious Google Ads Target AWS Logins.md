---
title: Cloud Credentials Phishing | Malicious Google Ads Target AWS Logins
url: https://buaq.net/go-148703.html
source: unSafe.sh - 不安全
date: 2023-02-10
fetch_date: 2025-10-04T06:12:34.402850
---

# Cloud Credentials Phishing | Malicious Google Ads Target AWS Logins

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

![](https://8aqnet.cdn.bcebos.com/df82e2da2a52d0c1765a37f7e660935d.jpg)

Cloud Credentials Phishing | Malicious Google Ads Target AWS Logins

Advertising is an integral part of the modern digital economy, providing businesses with the opport
*2023-2-9 19:53:39
Author: [www.sentinelone.com(查看原文)](/jump-148703.htm)
阅读量:41
收藏*

---

Advertising is an integral part of the modern digital economy, providing businesses with the opportunity to reach a large and diverse audience. However, malicious actors are taking advantage of the ubiquity of online advertising to spread malware, phishing scams, and other forms of malicious content. In recent weeks, Google Ads, one of the largest online advertising platforms, [has become a popular target for these types of attacks](https://www.sentinelone.com/blog/breaking-down-the-seo-poisoning-attack-how-attackers-are-hijacking-search-results/).

In this analysis, we examine recent malicious Google Ads targeting Amazon Web Services (AWS) logins through fraudulent credential phishing websites.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/Cloud-Credentials-Phishing-Malicious-Google-Ads-Target-AWS-Logins-10.jpg)

## Overview

From a high level, the workflow of the malvertising campaign followed a unique pattern, providing yet another example of the evolving malvertising campaigns ongoing through Google search results. In the case of AWS credentials targeting discussed here, we perform a normal Google search for “AWS”, which returns the malicious ad among the results.

The ad itself goes to a hop domain, which is an actor-controlled blogger website. This first hop then redirects to the actual credentials phishing page hosted on a second domain. After the victim submits their credentials, a final redirect sends the victim to the legitimate AWS login page. The redirect represents an effort to evade detection by cautious users, but more importantly to evade automated detection of the phishing websites and malicious ad monitors. The various hops and content included in the webpages of each domain add to the complexity of automated detection in such attacks.

![Google Malvertising AWS Phishing Workflow](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish4.jpg)

Google Malvertising AWS Phishing Workflow

## Malicious Ads

The malicious advertisements we observed occurred on January 30th and 31st 2023. These ads were most easily identified by searching “aws” in Google. Initially, the phishing domain was the ad itself; however, the attacker later shifted to a proxy ad through a `blogspot.com` website. As the image below shows, the attacker made use of `us1-eat-a-w-s.blogspot[.]com` as the destination for malicious ads. This is likely an effort to evade automated detection by Google of suspicious ad destination content.

![Google Malvertising AWS Phishing Ad](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish12.jpg)

Google Malvertising AWS Phishing Ad

The content of the `us1-eat-a-w-s.blogspot[.]com` website is a copy of a legitimate vegan food blog. However, the page loads a second domain, `aws1-console-login[.]us/login`, through an HTML `window.location.replace` action. Note, the blogger page was shut down less than a day after its creation.

![Malicious Blogspot Webpage Redirect](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish5.jpg)

Malicious Blogspot Webpage Redirect

Following the automated redirect to the `aws1-console-login[.]us/login` destination, the target is finally presented with a spoofed AWS login prompt. The login process appears legitimate to unsuspecting targets.

![Fake AWS Login Page - Email](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish3.jpg)

Fake AWS Login Page – Email

![Fake AWS Login Page - Password](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish9.jpg)

Fake AWS Login Page – Password

After the user enters their credentials, the final `zconfig01.php` page is loaded. This  contains a single line of code to direct victims to the legitimate AWS login page.

![Redirect to Legitimate AWS Login After Credential Submission](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish6.jpg)

Redirect to Legitimate AWS Login After Credential Submission

Recently, [Permiso’s P0 Labs](https://permiso.io/blog/s/watering-hole-attack-targets-aws-users/) conducted a review of an AWS phishing site related to the same attacker. Based on our analysis, we attributed it to the same attacker continuing their campaign on new ads with a few technical adjustments.

## Phishing Page Characteristics

Several characteristics unique to the phishing pages are noteworthy, including the layout, design, and efforts to hinder analysis as well as the developers’ spoken language.

A JavaScript function disables the right-click context menu and middle mouse button click on the web page. The function sets the `oncontextmenu` event to return false, effectively disabling the right-click context menu. It also sets the `onmousedown` event to call the `clickNS` function for non-IE browsers, which checks for middle mouse button clicks and returns false if either is detected. The `clickIE` function does the same for Internet Explorer. The purpose of this code is likely to prevent users from copying content from the web page using the right-click context menu or middle mouse button.

![Mouse Click Disable](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish1.jpg)

Mouse Click Disable

More JavaScript code adds several keyboard shortcuts that, when pressed, will redirect the user to “#”. This does not correspond to a specific page on the website and in effect serves to disable the keyboard shortcuts while the page is active.

![Shortcut Key Combo Disable](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish7.jpg)

Shortcut Key Combo Disable

All comments, variable names, and other bits of language are written in Portuguese. Additionally, one unused function included `maskaraCPF`. It’s possible that this function could be used to format and display personal information, such as a Brazilian CPF number, in a way that makes it appear legitimate to the user.

![maskaraCPF Function](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish2.jpg)

maskaraCPF Function

Throughout the various web pages the attacker made for this campaign, such as the blogspot and phishing pages, repeated use was made of source code copied from unrelated and legitimate websites. For example, the root page of the blogger domain mimics a legitimate Brazilian dessert business. The `/login` file on this site loads the AWS phishing page.

![Legitimate Website - source of copied code](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish8.jpg)

Legitimate Website – source of copied code

![Home of Malicious Website](https://www.sentinelone.com/wp-content/uploads/2023/02/AWS_Phish10.jpg)

Home of Malicious Website

## Infrastructure Analysis

The phishing domain `aws1-console-login[.]us` was registered through Sav, and then protected under CloudFlare on 2023-01-31, the same day it was being used in malicious ads. `aws1-us-west[.]info` was registered the day prior, and `aws1-ec2-console.com` on January 21, 2023.

For the `aws1-console-login[.]us`, the attacker did not protect the WHOIS details, providing yet another interesting link to Brazil.

* City: sao luis
* State/Province: ma
* Postal Code: 65076170
* Country: BR
* Phone: +55.99991638370
* Email: [email protected][.]com

CloudFlare were quick to confirm and responded by shutting down the account for service abuse. Due to this fast action, in s...