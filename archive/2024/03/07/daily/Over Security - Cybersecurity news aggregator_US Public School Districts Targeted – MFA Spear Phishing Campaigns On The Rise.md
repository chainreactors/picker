---
title: US Public School Districts Targeted – MFA Spear Phishing Campaigns On The Rise
url: https://pixmsecurity.com/blog/uncategorized/us-public-school-districts-targeted-mfa-spear-phishing-campaigns-on-the-rise/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-07
fetch_date: 2025-10-06T17:10:55.254742
---

# US Public School Districts Targeted – MFA Spear Phishing Campaigns On The Rise

[![Pixm Security Logo](https://pixmsecurity.com/wp-content/themes/Divi-Child/images/pixm-logo-header-white.png)](https://pixmsecurity.com)

* [About](https://pixmsecurity.com/about/)
* [About Us](https://pixmsecurity.com/about-us/)
* [Partners](https://pixmsecurity.com/partners/)
* Resources
  + [Blog](https://pixmsecurity.com/blog/)
  + [News](/news)
* [Login](https://app.pixm.net)
* [Book a Demo](https://pixmsecurity.com/request-demo/)
* [Free Install](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en)
* [Free Install](https://apps.apple.com/app/pixm-phishing-protection/id1622871362)
* [Free Install](https://addons.mozilla.org/en-US/firefox/addon/pixm-web/)

Have a question for us?

Contact support at support@pixm.net

[Book a Demo](/request-free-trial/)

Open Menu

## Request Your Demo

"\*" indicates required fields

### Contact Information

First Name\*

Last Name\*

Company\*

Email\*

Work Phone

CAPTCHA

Request Demo

# US Public School Districts Targeted – MFA Spear Phishing Campaigns On The Rise

### Overview

Multi-Factor Authentication (MFA) phishing campaigns targeting teachers, staff, and executive administrators in large school districts throughout the United States have continued to be on the rise since December 2023. The attacks use **dadsec** and **phishingkit** Phishing-as-a-Service (PhaaS) platforms, which include a number of stealthy features, with the purpose of compromising key administrator email accounts and ultimately delivering ransomware.

### Introduction

This report focuses on ongoing phishing activity beginning in November 2023 that is linked to two prominent threat groups: Tycoon and Storm-1575. [Prior](https://cyberwarzone.com/the-tycoon-phishing-group/) [reports](https://www.bridewell.com/insights/blogs/detail/analysing-widespread-microsoft365-credential-harvesting-campaign) identified these groups waging aggressive phishing campaigns across diverse sectors like financial services, manufacturing, local government and energy. Many attacks our research found involved stealthy tactics like MFA phishing, targeted key HR and finance personnel, and were hosted on Russian infrastructure. These Tycoon and Storm-1575 attacks were distinguished by their use of Adversary-in-the-Middle (AiTM) tools, allowing them (had they gone unthwarted) to capture MFA codes and session cookies.

Research found that targeted officials would receive classic phishing emails prompting them via a link to update their passwords for security purposes. They would then be directed to a Cloudflare Captcha, followed by a spoofed Microsoft password page embedded in a background with their distinct logo. Had the attacks gone unthwarted, the attacker would forward the passwords to the actual legitimate login pages upon stealing user passwords. From there, victims were directed to pages requesting the actual two-factor authentication codes, which were then forwarded to the actual servers, thus completely bypassing MFA protections. Common users targeted across districts include the Chief of Human Capital and multiple finance and payroll administrator accounts that send regular communications to staff members.

Some of the attacks would attempt to alter Windows registry keys with the possibility of infecting the target Windows machines with malicious scripts. The attacks concealed their tracks with a number of stealth tactics, such as hiding behind Cloudflare infrastructure and quickly spinning up new domains with domain generation algorithms.

Most security practitioners believe MFA is a silver bullet for protecting users from credential harvesting phishing attacks. While equipping corporate users with MFA remains a key step in securing an organization’s environment, the increased use and lowered cost of AiTM infrastructure highlight the need for additional measures like proactive AI-powered detection in the browser.

### Context: Storm-1575, Tycoon, and Phishing-as-a-Service (PhaaS)

Both the Tycoon and the Storm-1575 groups orchestrate robust and dangerous PhaaS platforms to target victims across diverse sectors of business and government. PhaaS is a malicious model where cybercriminals or threat actors offer ready-made phishing tools and services. Storm-1575 and Tycoon make use of **dadsec** and **phishingkit** PhaaS services, respectively. Some research indicates that the two platforms are linked. While any threat actor with sufficient intent and funds can purchase **dadsec** and **phishingkit** tools, the specific tactics, techniques and procedures our research identified closely match the cluster of activity associated with Storm-1575 and Tycoon.

**Tycoon**

The Tycoon Phishing Group is a notorious cybercrime organization that targets a wide range of victims. Their website (below) boasts “the best 2fa bypass phishing platform”. They have an active Telegram that offers professional grade customer service and tiered product packaging akin to a typical B2B SaaS business.

![](https://pixmsecurity.com/wp-content/uploads/2024/03/tycoon-1.png)

The group has created a PhaaS platform called **phishingkit** that allows the use of different types of branded templates. They are known for highly targeted delivery mechanisms to infiltrate small to medium sized companies. [Recent reports](https://www.techrepublic.com/article/sekoia-financial-sector-evolutions-threats/) of the group involved targeting investment firms using 2FA phishing links delivered through QR codes in XLS and PDF attachments.

**Storm-1575**

Storm-1575 provides a PhaaS platform named **dadsec** (recently rebranded as “Phoenix Panel”). Their platform offers AiTM capabilities. This means the attackers are proxying all the requests between the victim and a legitimate site (for example, Microsoft). A successful attack results in a complete take over of the victim’s account, even if MFA is enabled. The group recently deleted their store websites, Telegram channels and YouTube videos, but they are still very active.

![](https://pixmsecurity.com/wp-content/uploads/2024/03/phoenix-dadsec.png)

Microsoft has issued a warning against Storm-1575 in their [monthly news](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/monthly-news-november-2023/ba-p/3970796).

![](https://pixmsecurity.com/wp-content/uploads/2024/03/microsoft.png)

###

### Tactics, Techniques and Procedures

Analysis of Tycoon and Storm-1575 phishing attacks targeting district officials revealed a common attack pattern. Here are the key elements:

**Social Engineering**. Typical across most phishing attacks, Tycoon and Storm-1575 attacks rely heavily on social engineering techniques, spoofing their emails to appear to come from legitimate sources and using fear-inducing language to create a sense of urgency.

**Adversary-in-the-Middle (AiTM)**. The attacks targeting k12 officials were distinguished by the use of AiTM phishing. Unlike traditional credential harvesting attacks, these attacks complete the authentication process by proxying stolen credentials into their legitimate server. This enables the attacker to further steal MFA tokens and altogether bypass MFA safeguards. The below diagram illustrates this for a 2FA Microsoft phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2024/03/AiTM.png)

The phishing attacks also steal session cookies, which allow attackers to maintain unauthorized access without requiring re-authentication.

**Customized Login Experiences**. The attacks targeting school districts incorporated not only official email addresses but also cloned district logos in the background (illustrated below with a fictitious school district).

![](https://pixmsecurity.com/wp-content/uploads/2024/03/custom-login-page.png)

Indeed, the dadsec and phisingkit PhaaS services allow operators to point at legitimate sites and produce custom login experiences to match their target’s typical workflow (illustrated below). Such automation further...