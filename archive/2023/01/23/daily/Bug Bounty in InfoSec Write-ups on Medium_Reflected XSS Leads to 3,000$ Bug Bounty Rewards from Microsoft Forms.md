---
title: Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms
url: https://infosecwriteups.com/reflected-xss-leads-to-3-000-bug-bounty-rewards-from-microsoft-forms-efe34fc6b261?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-23
fetch_date: 2025-10-04T04:35:32.301435
---

# Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fefe34fc6b261&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-leads-to-3-000-bug-bounty-rewards-from-microsoft-forms-efe34fc6b261&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-leads-to-3-000-bug-bounty-rewards-from-microsoft-forms-efe34fc6b261&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-efe34fc6b261---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-efe34fc6b261---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Reflected XSS Leads to 3,000$ Bug Bounty Rewards from Microsoft Forms

[![Supakiad S. (m3ez)](https://miro.medium.com/v2/resize:fill:64:64/1*X5fh6pruB5p-7uyfDAjZIg.jpeg)](https://m3ez.medium.com/?source=post_page---byline--efe34fc6b261---------------------------------------)

[Supakiad S. (m3ez)](https://m3ez.medium.com/?source=post_page---byline--efe34fc6b261---------------------------------------)

3 min read

·

Jan 22, 2023

--

4

Listen

Share

Microsoft Forms Vulnerability: Reflected Cross-site Scripting (XSS)

## Table of Contents

* [Introduction](#e426)
* [Background](#902a)
* [Details of the Vulnerability](#914c)
* [Proof of Concept](#eaf8)
* [Disclosure Timelines](#da9b)

## Introduction

In this blog post, I will discuss the details of a reflected cross-site scripting (XSS) vulnerability in Microsoft Forms.

Press enter or click to view image in full size

![]()

Additionally, in my last blog post, I disclosed a vulnerability report on **Microsoft Power Apps** and dove into the processes of reporting. You can refer to my previous post on: [**Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)**](https://m3ez.medium.com/microsoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3-2022-c6c9f70e2ccd)for more detailed information on the process of reporting and claiming rewards through MSRC platform.

## Background

> **Microsoft Forms** is a popular web-based tool for creating surveys, quizzes, and other forms. It allows users to create forms and surveys, share them with others, and collect responses in a centralized location. However, we discovered that it is possible to inject malicious JavaScript code into the forms, which can be executed by unsuspecting users.

I followed the MSRC’s guidelines for reporting vulnerabilities and submitted my findings. For more information, please refer to:

* [Example Report Submissions to the MSRC](https://www.microsoft.com/en-us/msrc/bounty-example-report-submission)
* [Microsoft Bounty Programs | MSRC](https://www.microsoft.com/en-us/msrc/bounty?rtc=1)
* [FAQs — Report an issue and submission guidelines (microsoft.com)](https://www.microsoft.com/en-us/msrc/faqs-report-an-issue?rtc=1)

## Details of the Vulnerability:

The vulnerability lies in the way **Microsoft Forms** processes user input. Specifically, it fails to properly validate user input, allowing an attacker to inject malicious JavaScript code into the **id** parameter. An attacker can generate a malicious link with injected XSS Payload, they can take advantage of this vulnerability to take over authenticated accounts or perform state-changing actions with authenticated users’ sessions in the application, or even use a vulnerable domain to make a phishing page and etc.

**Vulnerable product:** `Microsoft Forms`

**Vulnerable URL:** `https://forms.office.com/pages/responsepage.aspx`

**Vulnerable Parameter:** `id`

> **Reflected XSS (Cross-Site Scripting)** is a type of web vulnerability that allows an attacker to inject malicious code into a website, which is then executed by the victim’s browser. This happens when the website includes untrusted user input in its pages without proper validation or encoding. The attacker crafts a special link or form that, when clicked or submitted by the victim, causes the victim’s browser to execute the malicious code. The victim’s browser is tricked into thinking the code is part of the website, allowing the attacker to steal sensitive information or perform other malicious actions

## Exploitation:

To exploit this vulnerability, an attacker would need to craft a specially-crafted link that contains the malicious JavaScript code. The attacker would then need to trick the user into clicking on the link, which would cause the code to be executed. This could be done through social engineering tactics, such as phishing emails or instant messaging.

### Proof of Concept:

Here is an example of a proof of concept that demonstrates the vulnerability:

1. Navigated to URL:

```
https://forms.office.com/Pages/ResponsePage.aspx
```

2. Injected XSS payload into `id` parameter value and added to a vulnerable URL from step 1.

**The payload was used:**

```
d1bvs%3c%2fscript%3e%3cscript%3ealert(`XSS`)%3c%2fscript%3ec579g
```

**Example injected Link:**

```
https://forms.office.com/pages/responsepage.aspx?id=d1bvs%3c%2fscript%3e%3cscript%3ealert(`XSS`)%3c%2fscript%3ec579g
```

3. Open the URL in step 2.

4. When users open the XSS inject link, the XSS payload will be triggered and executed as shown below.

Press enter or click to view image in full size

![]()

https://youtu.be/pjbaZYEYQV8

## Disclosure Timelines

* **Sep 27, 2022** — Vulnerability Discovered and Reported through MSRC portal.
* **Sep 29, 2022** — MSRC team confirmed. MSRC ticket was moved to Review/Repro.
* **Oct 4, 2022** — Bounty awarded and MSRC case status was changed from Review / Repro to Develop
* **Oct 21, 2022** — MSRC status was changed to Pre-Release and Complete.
* **Jan 22, 2023** — Public release of the security advisory.

I appreciate your feedback and would love to hear your thoughts on my blog. If you have any comments or suggestions, please feel free to reach out to me on LinkedIn or Twitter.

> LinkedIn: [Supakiad S.](https://www.linkedin.com/in/supakiad-satuwan/)
>
> Twitter: [(@Supakiad\_Mee)](https://twitter.com/Supakiad_Mee)

*Thank you for your support!*

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----efe34fc6b261---------------------------------------)

[Cross Site Scripting](https://medium.com/tag/cross-site-scripting?source=post_page-----efe34fc6b261---------------------------------------)

[Microsoft Security](https://medium.com/tag/microsoft-security?source=post_page-----efe34fc6b261---------------------------------------)

[Msrc](https://medium.com/tag/msrc?source=post_page-----efe34fc6b261--...