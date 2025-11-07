---
title: Phishing Campaigns “I Paid Twice” Targeting Booking.com Hotels and Customers
url: https://blog.sekoia.io/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-06
fetch_date: 2025-11-07T03:11:41.608665
---

# Phishing Campaigns “I Paid Twice” Targeting Booking.com Hotels and Customers

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

# Phishing Campaigns “I Paid Twice” Targeting Booking.com Hotels and Customers

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/TDR-badge2.png)](#molongui-disabled-link)

[Jeremy Scion, Quentin Bourgue and Sekoia TDR](#molongui-disabled-link)
November 6 2025

0

23 minutes reading

*This article was originally distributed as a private report to our customers.*

## Table of contents

* [Introduction](#h-introduction)
* [From Hotels to Guests: the First Breach](#h-from-hotels-to-guests-the-first-breach)
  + [Malicious emails](#h-malicious-emails)
  + [ClickFix infection chain](#h-clickfix-infection-chain)
    - [Step 1: redirection steps](#h-step-1-redirection-steps)
    - [Step 2: ClickFix tactic](#h-step-2-clickfix-tactic)
    - [Step 3: malware delivery](#h-step-3-malware-delivery)
  + [PureRAT Malware](#h-purerat-malware)
* [Booking Partners’ Data and Customer Funds at Risk](#h-booking-partners-data-and-customer-funds-at-risk)
  + [The fraud scheme targeting hotel customers](#h-the-fraud-scheme-targeting-hotel-customers)
  + [The cybercrime ecosystem targeting Booking.com](#h-the-cybercrime-ecosystem-targeting-booking-com)
    - [Booking-management accounts](#h-booking-management-accounts)
    - [Distributing Booking.com phishing](#h-distributing-booking-com-phishing)
    - [Business of logs](#h-business-of-logs)
    - [Checking harvested Booking accounts](#h-checking-harvested-booking-accounts)
* [Detection Opportunities](#h-detection-opportunities)
  + [ClickFix infection via PowerShell](#h-clickfix-infection-via-powershell)
  + [Loader](#h-loader)
  + [PureRAT](#h-purerat)
* [Conclusion](#h-conclusion)
* [IoCs](#h-iocs)

## Introduction

A Sekoia partner recently reported a **phishing campaign targeting hospitality industry customers** worldwide. The campaign was observed to involve either emails sent from a hotel’s compromised Booking.com account or messages distributed via WhatsApp. This activity proved particularly effective because the threat actor possessed customer data, including personal identifiers and reservation details, which further increased the credibility of the phishing attempts.

Sekoia.io analysts assess that the campaign stemmed from a **broader operation** that began earlier with the deployment of **infostealing malware**. The malware likely infected machines across multiple **hotel establishments**, enabling the theft of professional **credentials granting access to booking platforms** (*e.g.* Booking.com, Expedia). Threat actors then either sold the harvested credentials on cybercrime forums or leveraged them directly to send fraudulent emails to hotel customers, often as part of banking fraud schemes.

TDR uncovered a specific campaign that stood out for its sophisticated tactics and persistence. The intrusion began with a malicious email sent from a compromised address to a hotel reservation or administration email. The subject line referred to a customer request, while the email body reproduced the Booking.com brand identity to convince the recipient of its authenticity. The email included a URL that ultimately led to the **compromise of the victim machine** through the **ClickFix** social engineering tactic.

Once compromised, Booking professional accounts are typically sold and then exploited by other actors to deliver **targeted banking phishing emails to hotel guests**.

Sekoia.io analysts named the report *“I Paid Twice”* after the subject line of an email from a defrauded client. We assess with high confidence that the client who fell victim to this fraudulent scheme paid twice for his reservation: one at the hotel and once to the cybercriminal.

This report provides a detailed overview of the ClickFix campaign leveraged by threat actors to compromise hotel establishments and subsequently target their customers. Furthermore, it examines activities within the related cybercrime ecosystem.

## From Hotels to Guests: the First Breach

The analysed campaign has been active since at least April 2025 and remained in operation as of early October 2025. This campaign is one of several that were observed targeting booking platform accounts. In March 2025, [Microsoft documented](https://www.microsoft.com/en-us/security/blog/2025/03/13/phishing-campaign-impersonates-booking-com-delivers-a-suite-of-credential-stealing-malware/) a comparable operation that pursued similar objectives but distinct TTPs.

### Malicious emails

In the campaign analysed by TDR, the attacker’s modus operandi involved using a compromised email account to send malicious messages to multiple hotel establishments. After reviewing messages linked to this campaign since early September, we are highly confident that the sender’s address was compromised, since most of the emails originated from legitimate corporate accounts. In some instances, the **“From”** **header** was altered to impersonate Booking.com. Below is a list of observed subject lines from Sekoia SOC platform telemetry:

* *New last-minute booking ({REF + DATE})*
* *New guest message in reference to your unit – Tracking code:{ID}*
* *New guest message linked to your listing – Ref.{ID}*
* *New guest message about the guest record Log:{ID}*
* *New guest message about reservation – Tracking code:{ID}*
* *New guest message related to your listing Ref:{ID}*

The same compromised email address was used to target several hotels across multiple countries. This suggests the attacker used a compromised account with no actual reservation to contact the hotels.

In October 2023, the cybersecurity researcher *g0njxa* published a [Medium article](https://g0njxa.medium.com/un-booking-a-scam-8f8058eb7200) describing how threat actors create fraudulent Booking.com accounts to make cancellable reservations solely to contact hotels. While this technique differs from the current campaign, it nonetheless underscores the...