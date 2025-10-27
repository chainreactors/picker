---
title: [Phishing kit] Coinbase phishing kit with live admin panel to bypass MFA – an analysis.
url: https://stalkphish.com/2023/01/25/phishing-kit-coinbase-phishing-kit-with-live-admin-panel-to-bypass-mfa-an-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-26
fetch_date: 2025-10-04T04:53:41.779435
---

# [Phishing kit] Coinbase phishing kit with live admin panel to bypass MFA – an analysis.

[![StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/wp-content/uploads/2021/03/stalkphish-incl-200x60-txt-white.png)](https://stalkphish.com/)

[StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/)

StalkPhish – We provide B2B tools, data and knowledge for a better phishing and brand impersonation detection.

* [Home](https://stalkphish.com/)
* [Products](https://stalkphish.com/portfolio/products/)
* [Projects](https://stalkphish.com/products/)
  + [PhishingKit-Yara-Rules](https://stalkphish.com/products/phishingkit-yara-rules/)
  + [PhishingKitHunter](https://stalkphish.com/products/phishingkithunter/)
  + [StalkPhish OSS](https://stalkphish.com/products/stalkphish/)
* [Blog](https://stalkphish.com/blog-feed/)
* [Contact](https://stalkphish.com/contact/)
* [About](https://stalkphish.com/about-2/)
* [Press & Media](https://stalkphish.com/press-media/)

* [Twitter](https://twitter.com/Stalkphish_io)
* [LinkedIn](https://www.linkedin.com/company/stalkphish)
* [GitHub](https://github.com/t4d/StalkPhish)
* [Youtube](https://www.youtube.com/channel/UC5hb1CaRdmbSWpN0wTz6SFw)

Show search form
Menu- Select Page -HomeProductsProjects - PhishingKit-Yara-Rules - PhishingKitHunter - StalkPhish OSSBlogContactAboutPress & Media

Search for:

 Hide search form

![](https://stalkphish.com/wp-content/uploads/2023/01/coinbase-mfa-kit_analysis.png?w=1084)

# [Phishing kit] Coinbase phishing kit with live admin panel to bypass MFA – an analysis.

An analysis of a Coinbase phishing kit designed to steal personal data, login, password and the second factor of authentication (MFA/2FA).

![StalkPhish's avatar](https://2.gravatar.com/avatar/2ecf84df3d23b66e9e3dc59759be2600c71c9cd576b072248f211024b06278a3?s=35&d=identicon&r=G) By [StalkPhish](https://stalkphish.com/author/stalkphish/)

in [investigation](https://stalkphish.com/category/investigation/), [phishing](https://stalkphish.com/category/phishing/), [phishing kit](https://stalkphish.com/category/phishing-kit/), [PhishingKit-Yara-Rules](https://stalkphish.com/category/tool/phishingkit-yara-rules/), [StalkPhish.io](https://stalkphish.com/category/tool/stalkphish-io/), [threat intelligence](https://stalkphish.com/category/threat-intelligence/)

on [01/25/202301/28/2023](https://stalkphish.com/2023/01/25/phishing-kit-coinbase-phishing-kit-with-live-admin-panel-to-bypass-mfa-an-analysis/)

[No comments](https://stalkphish.com/2023/01/25/phishing-kit-coinbase-phishing-kit-with-live-admin-panel-to-bypass-mfa-an-analysis/#respond)

During our regular analysis of our data, collected mainly by our [Stalkphish.io](https://Stalkphish.io) service, we came across a phishing kit targeting Coinbase and its customers.

Coinbase is a ‘place to buy and sell cryptocurrency’. These kinds of platforms used to store, buy and sell cryptocurrencies are increasingly targeted by scammers, just like traditional banks.

![](https://stalkphish.com/wp-content/uploads/2023/01/coinbase.jpg?w=1024)

The legit Coinbase’s portal

The particularity of this kit is that it adds a part of **interactivity between the victim and the scammer**: the scammer can interact with the victim in real time to get information that can be used only in a limited time, this is the case of MFA data.

## About MFA

It is now known among users that the only login and password used as a connection factor are no longer secure enough to secure access to a portal or data, which is why it is now more than recommended to use **multifactor authentication methods (MFA)**.

Multi-factor authentication allows you to add additional data (such as texts, biometrics, FIDO2 security keys and one-time passcodes) to log in.

This technology **prevents an attacker**, a scammer, who might have stolen your login/password pair from being able to log in to your account, since this second authentication factor (we also call it **2FA**) is single-use: even if it is stolen it cannot be re-used.

## The phishing kit – hosting and development

This phishing kit was downloaded on **December 27, 2022** by one of Stalkphish.io’s sensor. One of the purposes of Stalkphish is to retrieve phishing kits sources to extract interesting information about the actors of the campaign: chasing bullet-proof servers will not contribute significantly to the fight against phishing, trying to **stop the actor is the only way to fight efficiently against phishing**.

Retrieving phishing kit sources permit to analyze the kit, in order to improve our knowledge of the techniques used by scammers.

> Stop the actor is the only way to fight efficiently against phishing.

The phishing kit was deployed on the IP address **34.83.148.63**, an IP address belonging to **Google Cloud**. The domain name chosen by the scammer was **booked 2 days before**, on December 25th, it is **cbase-userhelp[.]com**, the choice of ‘*cbase*‘ corresponds to the usurped brand: Coinbase.

Several kits were deployed between December 27 and 28 on this same domain name according to [Stalkphish.io](https://Stalkphish.io), 2 *Coinbase* kits as well as an *Affirm* kit. All these phishing kits are produced by the same developer: **HadySpeed**. However, this does not mean that this is the scammer operating the campaign, as the scammer may have purchased the kits as well as the ***smishing*** tool that HadySpeed sells:

![](https://stalkphish.com/wp-content/uploads/2023/01/hadyspeed-tg.png?w=417)

The pack sold by HadySpeed

We won’t go any further in this study about this kit developer, but don’t hesitate to [ask us](https://stalkphish.com/contact/) if you want to know more.

## The phishing kit – configuration files

Once downloaded and unzipped, this is what the ZIP archive looks like:

![](https://stalkphish.com/wp-content/uploads/2023/01/coinbase-zip.png?w=1024)

HadySpeed’s Coinbase phishing kit

First over all we open the ***READ ME.txt*** file :

![](https://stalkphish.com/wp-content/uploads/2023/01/hadyspeed-readme.png?w=829)

Phishing kit *READ ME.txt* file

This file contains important information about :

* the **author** and version of the kit
* how to install the kit, on a **cPanel** in particular
* the configuration of the database
* the name of the global configuration file (*files/config.php*)
* the default password of the **admin panel**
* the files containing **Telegram bot** configuration
* the directory that will receive the **ID card pictures** (*IDentity\ID\upload\pics*)

This how looks the configuration file (*files/config.php*):

![](https://stalkphish.com/wp-content/uploads/2023/01/hadyspeed-config.png?w=984)

*Configuration file*

The following information can be obtained from the **configuration file**:

* the name of the database and its credentials
* the password of the administration page of the kit
* the link to where the user is redirected and the message displayed when the user has finished filling in the requested information

This information allows us to learn more about the kit:

* it uses a **database** to store the stolen information
* an **administration panel** is available
* …

## The phishing kit – pages

This phishing kit is divided into different pages and phases with the aim of stealing several types of data related to a Coinbase account:

* login and password to connect to the Coinbase account ;
* scan of a driver’s licence ;
* second authentication factor delivered by SMS or another OTP app

Looking at the first *index.php* file – the first page you launch when you connect to the phishing page – we can see that the connections are **logged** (IP address and user-agent) in a **text file** at the root of the kit.
We can also notice the absence of access filters, where usually a multitude of files dedicated to stop the connections of phishing page detection bots.

![](https://stalkphish.com/wp-content/uploads/2023/01/hadyspeed-index.png?w=652)

First *index.php* file

So we access the first page which presents the Coinbase login screen, the *si...