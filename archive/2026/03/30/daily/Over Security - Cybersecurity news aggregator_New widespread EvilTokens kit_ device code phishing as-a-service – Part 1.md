---
title: New widespread EvilTokens kit: device code phishing as-a-service – Part 1
url: https://blog.sekoia.io/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-30
fetch_date: 2026-03-31T04:37:15.610974
---

# New widespread EvilTokens kit: device code phishing as-a-service – Part 1

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

# New widespread EvilTokens kit: device code phishing as-a-service – Part 1

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue and Sekoia TDR](#molongui-disabled-link)
March 30 2026

0

20 minutes reading

***This post was originally distributed as a private FLINT report to our customers on 25 March 2026.***

## Introduction

In March 2026, through our monitoring of phishing-focused cybercrime communities, Sekoia’s Threat Detection & Research (TDR) team uncovered **EvilTokens, a new turnkey Microsoft device code phishing kit** sold as Phishing-as-a-Service (PhaaS). These phishing pages have been circulating since mid-February 2026, and were **rapidly adopted by cybercriminals** specialising in Adversary-in-the-Middle (AitM) phishing and Business Email Compromise (BEC).

Our analysis showed that EvilTokens provides a turnkey Microsoft device code phishing kit and a range of **advanced features to conduct BEC attacks**, including access weaponisation, email harvesting, reconnaissance capabilities, a built-in webmail interface, and **AI-powered automation**.

The EvilTokens PhaaS operates through fully featured bots on Telegram and continuously improves its phishing kit with new capabilities. In the near future, the operator intends to extend support to Gmail and Okta phishing pages.

Given EvilTokens’s rapid adoption, advanced phishing capabilities, and BEC task automation, TDR analysts assess with high confidence that this kit will **become a serious competitor in the phishing and BEC landscape**.

This report explains the Microsoft device code authorisation flow and offers a technical analysis of the EvilTokens device code kit, covering its phishing pages, the weaponisation of harvested Microsoft tokens, and the functionalities available to affiliates. It also highlights the widespread adoption of EvilTokens by analysing delivery campaigns, and the large adversary’s infrastructure.

In a follow-up blog post, we will detail the PhaaS operations on Telegram and the additional services provided by the operator *eviltokensadmin*. It will highlight the advanced features that significantly facilitate BEC fraud by leveraging AI.

## Device code phishing and its impact

To compromise Microsoft 365 accounts, EvilTokens pages rely on device code phishing, a technique that differs from the common AitM tactic of replicating Microsoft authentication pages. In this attack, victims are tricked into entering a device code on the legitimate login page, thereby granting attackers access to their accounts.

### Microsoft device code authentication flow

The OAuth 2.0 Device Authorisation Grant enables authentication for endpoints with limited input capabilities, such as smart TVs, IoT devices, or printers. Rather than requiring a direct local login, the authentication flow delegates sign-in to a secondary host: the endpoint displays a user code, which the user enters in a browser on a separate device, typically a smartphone or computer, to authenticate. Once succeeded, the endpoint receives an access token and refresh token, resulting in a long-lived authenticated session on the device.

Microsoft’s implementation of this flow uses three endpoints:

1. POST */oauth2/v2.0/devicecode*: the device requests a code (*user\_code*), which is alphanumeric characters associated with a session identifier (*device\_code*), for a specified client and a scope.
2. GET */devicelogin* redirecting to */common/oauth2/deviceauth*: the user signs in on a secondary host, by entering the *user\_code* and authenticating using a common method.
3. POST */<TENANT>/oauth2/v2.0/token*: the device polls this endpoint to obtain the access token (*access\_token*) and refresh token (*refresh\_token*) granting a persistent access without re-authentication, once the user has authenticated. The refresh token is obtained when the *offline\_access* scope is included in the authorisation request,

The following diagram illustrates this protocol, as provided by Microsoft[1](#69ddc5c8-150c-4a9b-aacb-fea0789640f4):

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/03/image-7-1024x481.png)

### Device code phishing attack

The device code phishing attack exploits the inherent separation between the device to authenticate and the user sign-in in the OAuth 2.0 Device Authorisation Grant detailed above. Rather than relying on an adversary infrastructure, the attacker initiates a genuine device authorisation request to obtain access to the target’s account. By acting as the device’s client, the attacker tricks the victim into completing the standard authentication, taking advantage of the victim’s lack of knowledge regarding device code authentication, and thereby stealing the access grant.

Main steps of device code phishing attack are:

1. The attacker sends a valid POST request to */oauth2/v2.0/devicecode* using a legitimate client\_id (*e.g.* a Microsoft first-party application, for example Microsoft Office client). The server returns a *device\_code*, *user\_code*, and the *verification\_uri*.
2. The attacker relays the *user\_code* and *verification\_uri* to the target. For this step, a social engineering lure must prompt the target to authenticate to the legitimate Microsoft URL delivered by the attacker by entering the user\_code.
3. The target browses the *verification\_uri* which is a legitimate Microsoft endpoint *hxxps://microsoft[.]com/devicelogin*, redirecting to: *hxxps://login.microsoftonline[.]com/<TENANT>/oauth2/v2.0/devicecode.*
4. The target enters the *user\_code* delivered by the threat actor through the phishing page or another means, and completes authentication on the Microsoft sign-in page.
5. The attacker polls the */<TENANT>/oauth2/v2.0/token* to retrieve a valid *access\_token* and ...