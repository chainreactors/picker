---
title: Shedding Light on PoisonSeed’s Phishing Kit
url: https://blog.nviso.eu/2025/08/12/shedding-light-on-poisonseeds-phishing-kit/
source: NVISO Labs
date: 2025-08-13
fetch_date: 2025-10-07T00:16:37.974269
---

# Shedding Light on PoisonSeed’s Phishing Kit

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Shedding Light on PoisonSeed’s Phishing Kit

[Efstratios Lontzetidis](https://blog.nviso.eu/author/efstratios-lontzetidis/ "Posts by Efstratios Lontzetidis")

[Blue Team](https://blog.nviso.eu/category/blue-team/)

August 12, 2025August 12, 2025
28 Minutes

# Key Findings:

* NVISO identified and analyzed the MFA-resistant phishing kit employed by the threat actor PoisonSeed, which is loosely aligned with Scattered Spider and CryptoChameleon. This kit is still active as of the time of reporting.
* PoisonSeed uses this phishing kit to acquire credentials from individuals and organizations, leveraging them for email infrastructure purposes such as sending emails and acquiring email lists to expand the scope of cryptocurrency-related spam.
* The domains hosting this phishing kit impersonate login services from prominent CRM and bulk email companies like Google, SendGrid, Mailchimp, and likely others, targeting individuals’ credentials.
* PoisonSeed employs spear-phishing emails embedding malicious links, which redirect victims to their phishing kit.
* The victim’s email is appended in the phishing kit’s URL and also stored as a cookie in an encrypted format that is verified server-side, a technique known as “Precision-Validated Phishing.”
* The phishing kit includes a fake Cloudflare Turnstile challenge to verify the victim’s encrypted email.
* It supports multiple 2FA methods such as Authenticator Codes, SMS Codes, Email Codes and API Keys.
* The phishing kit acts as an Adversary-in-the-Middle (AitM), forwarding login and two-factor authentication (2FA) details to the legitimate service and capturing all authentication information.
* PoisonSeed registered all their domains through the NICENIC registrar. For hosting, they utilized Cloudflare, DE-First Colo, and SWISSNETWORK02, and for name servers, they utilized Cloudflare and Bunny.net.
* This blog provides hunting opportunities, prevention measures related to strong authentication, user awareness, and anomaly detection, as well as indicators of compromise.

# Introduction

As first reported by [SilentPush](https://www.silentpush.com/blog/poisonseed/), PoisonSeed is a threat actor whose TTPs closely align with Scattered Spider and CryptoChameleon, groups that are part of “The Com,” a young, English-speaking threat actor community. They engage in phishing attacks to obtain login information from CRM and bulk email service providers, allowing them to export contact lists and distribute larger volumes of spam using these accounts. The primary aim of targeting email providers appears to be establishing infrastructure for conducting cryptocurrency-related spam activities. Recipients of these spam operations are subjected to a cryptocurrency seed phrase manipulation attack. In this tactic, PoisonSeed offers security seed phrases, encouraging victims to use them in new cryptocurrency wallets, which they can later exploit. PoisonSeed is responsible for the campaign that targeted Troy Hunt where the actors [stole his Mailchimp mailing list](https://www.troyhunt.com/a-sneaky-phish-just-grabbed-my-mailchimp-mailing-list/), and the [Coinbase phishing emails](https://www.bleepingcomputer.com/news/security/coinbase-phishing-email-tricks-users-with-fake-wallet-migration/) tricking users with fake wallet migration.

In this blog, NVISO builds on SilentPush’s report and analyzes PoisonSeed’s MFA-resistant phishing kit, which continues to be active in the wild since April 2025.

# PoisonSeed Phishing Activity

PoisonSeed’s phishing kit utilizes email infrastructure to send spear-phishing emails containing marketing-related links. These links redirect to domains hosting the phishing kit, appending the victim’s email in an encrypted format in the URL. From there, a fake Cloudflare Turnstile challenge page appears that performs victim verification server-side, in the background. This verification checks the presence and validity of the encrypted email in the URL, ensuring it is not banned by the legitimate service. Upon passing these checks, a login form mimicking the legitimate service appears, capturing submitted credentials and relaying them to the legitimate service. If the credentials are valid, the victim is presented with a page corresponding to the registered 2FA method (Authenticator, SMS, Email, API Key). The phishing kit relays the 2FA method submitted by the victim, resulting in capturing the authentication cookies before providing them also to the victim. Thus, the threat actor bypasses MFA protections to gain account access. Once authentication details are captured, PoisonSeed [automates](https://www.silentpush.com/blog/poisonseed/) the bulk downloading of email lists.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-36.png)

PoisonSeed Phishing Attack Chain

## Initial Access

PoisonSeed initiates its attack by delivering phishing emails to targeted individuals. Email lures feature subjects mimicking the impersonated email provider, such as “Sending Privileges Restricted”. The emails contain a malicious link prompting the recipient to take action.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-37.png)

Example of phishing email sent to Troy Hunt

Email marketing and CRM-related links were observed redirecting to PoisonSeed’s phishing domains (source: URLScan). Links such as \*.ct.sendgrid.net redirected to URLs hosting the phishing kit, with the target’s email appended as an encrypted parameter. An example of a public URLScan task is [this one](http://urlscan.io/result/0197d055-e8e6-7475-88d5-462a6ed50c80).

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-38-1024x304.png)

SendGrid URL redirecting to PoisonSeed’s Phishing Domain

## Phishing Kit Technical Analysis

The phishing kit is developed using React and features the following structure:

* A fake Cloudflare Turnstile challenge verifies the victim’s email address presence in the phishing URL in the background.
* A login form captures usernames and passwords, relaying them to the impersonated legitimate service.
* A form captures 2FA details—SMS/Authenticator/Email code or API key—based on the registered method, and relays them to the impersonated service, ultimately capturing authentication cookies.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-39-1024x341.png)

PoisonSeed’s Phishing Kit Overview

The features of each component ar...