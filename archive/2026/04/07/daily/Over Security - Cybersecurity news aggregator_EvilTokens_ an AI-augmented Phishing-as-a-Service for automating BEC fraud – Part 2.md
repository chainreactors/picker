---
title: EvilTokens: an AI-augmented Phishing-as-a-Service for automating BEC fraud – Part 2
url: https://blog.sekoia.io/eviltokens-an-ai-augmented-phishing-as-a-service-for-automating-bec-fraud-part-2/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-07
fetch_date: 2026-04-08T04:38:57.359969
---

# EvilTokens: an AI-augmented Phishing-as-a-Service for automating BEC fraud – Part 2

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# EvilTokens: an AI-augmented Phishing-as-a-Service for automating BEC fraud – Part 2

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue and Sekoia TDR](#molongui-disabled-link)
April 7 2026

0

14 minutes reading

**A TLP:AMBER version of this post was originally distributed as a private FLINT report to our customers on 30 March 2026.**

## Introduction

As detailed in our previous blog post *[New widespread EvilTokens kit: device code phishing as-a-service – Part 1](https://blog.sekoia.io/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1/)*, EvilTokens is a **new turnkey Microsoft device code phishing kit** sold as Phishing-as-a-Service (PhaaS). Since mid-February 2026, these phishing pages have been distributed in the wild and were **rapidly adopted by cybercriminals** specialising in Adversary-in-the-Middle (AiTM) phishing and Business Email Compromise (BEC).

The EvilTokens PhaaS operates through fully featured Telegram bots and continuously improves its phishing kit with new capabilities.

As of March 2026, its features enable attackers to **weaponise harvested tokens to exfiltrate emails**, files and other sensitive data from compromised Microsoft accounts, conduct **reconnaissance** via Microsoft Graph API, and establish **persistence access**.

Beyond pioneering device code phishing as–a-service, EvilTokens provides affiliates with breakthrough **AI-driven features to automate and scale BEC workflows**: analysing harvested emails, identifying finance-related email threads, and drafting BEC emails.

This blog post details the EvilTokens PhaaS operations on Telegram and the administration panel capabilities leveraged by affiliates, including AI-augmented features that significantly facilitate BEC fraud.

## Inside the EvilTokens PhaaS operations

### EvilTokens’ sales on Telegram

On 3 March 2026, Sekoia’s TDR first identified EvilTokens through its PhaaS offering, which was advertised by *eviltokensadmin* in a private Telegram channel, frequented by threat actors specialised in AitM phishing and BEC fraud. The initial announcement included two demonstration videos showing how the EvilTokens device code phishing pages operate and how an attacker can hijack a compromised account to access emails and contacts. The administrator leveraged the following Telegram resources:

* The account for supporting the PhaaS activities.
* The channel for publishing product details, change logs, tutorials, and updates.
* The bot for handling affiliate sales: to add balance to their account, to buy a product and to check their activities.
* The bot, for facilitating the deployment of landing pages to Cloudflare Workers, including EvilTokens phishing pages.
* The bot, for selling the anti-bot pages.
* A private group likely dedicated to the PhaaS customer (around 280 subscribers as of 19 March 2026.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/04/image-2-1024x554.png)

#### PhaaS pricing

Since 17 February 2026, *eviltokensadmin* has offered for sale three different products:

* *EvilTokens B2B sender*, for $600.
* *EvilTokens Office 365 capture link*, for $1500.
* *EvilTokens SMTP sender*, for $1000.

The “Office 365 capture link” corresponds to the device code phishing kit. The one-time fee of $1500 grants affiliates lifetime access to the EvilTokens administration panel for viewing harvested Microsoft tokens. Affiliates must also pay a monthly licence fee of $500 to obtain the phishing page code and an active API key for backend integration and core device code phishing functionality.

Payments are processed using the cryptocurrency payment gateway NOWPayments, which integrates cryptocurrency transactions with traditional payment systems. When an affiliate deposits funds, the bot creates a NOWPayments transaction that accepts multiple cryptocurrencies.

#### Custom browser for BEC operations

In addition, the EvilTokens administrator offers a custom web browser, branded “*Portal Browser*” or “*ET Browser*”, that enables simultaneous access to multiple Microsoft 365 accounts using stolen tokens. It allegedly supports unlimited accounts and Microsoft Admin, Azure, Office, OneDrive, SharePoint and Teams applications, with harvested tokens automatically refreshed. The lifetime license for “*Portal Browser*” is sold for 500$ on the dedicated website *machinemind-market[.]com*.

The development of “*Portal Browser*”, tailored for advanced fraud, demonstrates a strong expertise in Microsoft OAuth token management. It was likely built for the threat actor’s own BEC operations before being commercialised alongside EvilTokens PhaaS. This shift, which is to repurpose advanced tools into revenue streams, mirrors broader cybercriminal trends toward “as-a-service” models such as PhaaS, MaaS, and other offerings (*e.g.* crypters, ransomware, malware distribution).

### Case of an affiliate

A trusted researcher shared two public GitHub repositories that appear to contain the EvilTokens code for hosting and deploying phishing pages on the Railway.app cloud platform.

TDR analysts assess with high confidence that these repositories belong to an EvilTokens affiliate, who obtained the phishing kit’s source code and uploaded it to GitHub to deploy it on Railway.

These repositories mostly include configuration files and an *index.php* file, which includes the server-side phishing pages. This PHP script renders a device code phishing page impersonating either DocuSign or Microsoft Outlook, and displays it to the target. The rendered HTML exactly matches the EvilTokens phishing pages analysed in part 1.

The PHP code defines the domain of the centralised backend server and a token secret, likely serving as a licence key to authenticate affiliates and ve...