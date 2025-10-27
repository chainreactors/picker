---
title: Sneaky 2FA: exposing a new AiTM Phishing-as-a-Service
url: https://blog.sekoia.io/sneaky-2fa-exposing-a-new-aitm-phishing-as-a-service/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-17
fetch_date: 2025-10-06T20:13:14.155915
---

# Sneaky 2FA: exposing a new AiTM Phishing-as-a-Service

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

# Sneaky 2FA: exposing a new AiTM Phishing-as-a-Service

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue, Grégoire Clermont and Sekoia TDR](#molongui-disabled-link)
January 16 2025

0

20 minutes reading

## Table of contents

* [Introduction](#h-introduction)
* [Characteristics of Sneaky 2FA](#h-characteristics-of-sneaky-2fa)
  + [URL patterns](#h-url-patterns)
  + [Anti-bot and anti-analysis features](#h-anti-bot-and-anti-analysis-features)
  + [Authentication with Microsoft API](#h-authentication-with-microsoft-api)
* [Business and operations of Sneaky Log](#h-business-and-operations-of-sneaky-log)
  + [Phishing kit connections](#h-phishing-kit-connections)
  + [Sneaky Log’s operations on Telegram](#h-sneaky-log-s-operations-on-telegram)
  + [Cryptocurrency transactions](#h-cryptocurrency-transactions)
* [Detection and tracking opportunities](#h-detection-and-tracking-opportunities)
  + [Detecting impossible device shift](#h-detecting-impossible-device-shift)
  + [Unveiling Sneaky 2FA phishing pages](#h-unveiling-sneaky-2fa-phishing-pages)
* [Conclusion](#h-conclusion)
* [Annex](#h-annex)
  + [Annex 1 – Initial email phishing campaign distributing Sneaky 2FA using QR code](#h-annex-1-initial-email-phishing-campaign-distributing-sneaky-2fa-using-qr-code)
* [IoCs & Technical details](#h-iocs-amp-technical-details)
  + [Sneaky 2FA’s phishing pages](#h-sneaky-2fa-s-phishing-pages)
  + [Sneaky 2FA’s operator servers](#h-sneaky-2fa-s-operator-servers)
* [External references](#h-external-references)

## Introduction

In December 2024, during our daily threat hunting routine, we uncovered **a new Adversary-in-the-Middle (AiTM) phishing kit targeting Microsoft 365 accounts**. These phishing pages have been circulating since at least October 2024, and during that period, we identified potential compromises through the Sekoia.io telemetry.

Our analysis showed that this kit is being **sold as Phishing-as-a-Service (PhaaS)** by the cybercrime service “*Sneaky Log”*, which operates through a fully-featured bot on Telegram. Customers reportedly receive access to a licensed obfuscated version of the source code and deploy it independently. Currently, Sneaky 2FA’s phishing pages are hosted on compromised infrastructure, frequently involving WordPress websites, and other domains controlled by the attacker.

[Sekoia’s Threat Detection & Research (TDR) team](https://www.sekoia.io/en/about-threat-detection-research-team/) obtained the leaked source code for further analysis. During our investigation, we discovered that the phishing kit includes some source code from the W3LL Panel OV6, an AiTM phishing kit reported by Group-IB[1](#a2d6110e-d257-468e-98e3-7cf837b86a15) in September 2023.

This blog post provides an overview of the Sneaky 2FA phishing kit, explaining its functionality and the related cybercrime service operating on Telegram. Additionally, it shares detection opportunities, as well as Indicators of Compromise (IoCs) associated with Sneaky 2FA’s phishing campaigns.

## Characteristics of Sneaky 2FA

The following analysis is based on Sneaky 2FA phishing campaigns identified in the wild, as well as its purported source code.

### URL patterns

#### Autograb

Sneaky 2FA implements the *autograb* functionality to automatically prefill the Microsoft phishing page with the victim’s email address. To achieve this, the phishing URL includes the email address as a parameter, either in plain text or encoded in base64. For example:

```
hxxps://mysilverfox.com[.]my/00/#victim[@]example[.]com

hxxps://highnationservices[.]com/n/#victim[@]example[.]com
```

The server then extracts the email address and inserts it into the username field of the fake Microsoft authentication page presented to the victim.

#### Fake Microsoft authentication pages

Sneaky 2FA phishing URLs are generated using 150 alphanumeric characters, followed by the path `/index`, `/verify` and `/validate`. This pattern offers opportunities for tracking.

We observed that most customers of the phishing kit service deploy the server in a dedicated repository, named `/auth/` by default.

Below are examples of Sneak Log phishing URLs identified in December 2024:

```
hxxps://kagumigroup[.]id/wp-content/plugins/well/auth/j9P8KGpfDZyoHplo5XdnHOw79OCkDYo2l7TQcrrnclSz2XGLzmtCghFJwIWR1AaW33Rk36Z0ymZc6DIgMy4EFqTsiiqAKEBIN5jiTbYAUk1BfG4uoVhetLa2XWebUSShQOFq7L8Mpx1vf4Pum0xBVx/verify

hxxps://mysilverfox.com[.]my/00/7N0tV3XAh1yp4NFo9X6YsH3cOam6DYJhmMEXRky24mzGUuTE2RpwIIlI4olBypVCEYqiKFPDTAsRvKrS8bgiKBOZiPOUnxoCSHveA0zk5hcdjQ1UltSxdw7rdgZoo7HDWorfj9CzN8gc0q5PQ19nZe/index

hxxps://highnationservices[.]com/n/uswDOVS70y9sjyPwtLieCJdZiEUGhokxRUvY7JApYlFo35Sb9o66AvhK8oNrHPTgj9aaJDHItTWDnPOo3t4mz8Tfhf7GBem0YE1cqx8O13VoKuWIbN4knGg6fRrvMIZXRQ2xgdEFzj2mVBzwSbpe5c/validate
```

### Anti-bot and anti-analysis features

#### Cloudflare Turnstile page

Sneaky 2FA phishing pages can be protected by Cloudflare Turnstile[2](#d447737d-b446-4ead-bf7d-9267268dba65) or reCAPTCHA pages to determine whether the user behaves like a human rather than a bot. As of December 2024, we only observed the use of Cloudflare Turnstile prior to accessing fake Microsoft authentication pages.

![Sneaky 2FA page embedding a Cloudflare Turnstile challenge](data:image/svg+xml...)![Sneaky 2FA page embedding a Cloudflare Turnstile challenge](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/01/image1-1024x704.png)

Figure 1. Sneaky 2FA page embedding a Cloudflare Turnstile challenge

Cloudflare Turnstile pages have the following characteristics:

* Initially, it returns an HTML page with food-related content, titled “Gourmet Delights and Beverage”. This page uses the JavaScript function `window.location.reload()` to load the C...