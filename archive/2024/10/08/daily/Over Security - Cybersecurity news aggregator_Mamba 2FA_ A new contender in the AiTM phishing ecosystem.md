---
title: Mamba 2FA: A new contender in the AiTM phishing ecosystem
url: https://blog.sekoia.io/mamba-2fa-a-new-contender-in-the-aitm-phishing-ecosystem/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-08
fetch_date: 2025-10-06T18:53:11.800427
---

# Mamba 2FA: A new contender in the AiTM phishing ecosystem

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

# Mamba 2FA: A new contender in the AiTM phishing ecosystem

Discover Mamba 2FA, a previously unknown adversary-in-the-middle (AiTM) phishing kit, sold as phishing-as-a-service (PhaaS).

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Grégoire Clermont and Sekoia TDR](#molongui-disabled-link)
October 7 2024

0

11 minutes reading

## Table of contents

* [Introduction](#h-introduction)
* [Characteristics of Mamba 2FA phishing pages](#h-characteristics-of-mamba-2fa-phishing-pages)
  + [URL structure and domain names](#h-url-structure-and-domain-names)
  + [Base64-encoded parameter](#h-base64-encoded-parameter)
* [Capabilities of the Mamba 2FA phishing platform](#h-capabilities-of-the-mamba-2fa-phishing-platform)
* [Commercialisation of Mamba 2FA phishing pages](#h-commercialisation-of-mamba-2fa-phishing-pages)
* [HTML attachments](#h-html-attachments)
* [Mamba 2FA Architecture](#h-mamba-2fa-architecture)
  + [Link domains](#h-link-domains)
  + [Socket.IO protocol](#h-socket-io-protocol)
  + [Relay servers](#h-relay-servers)
  + [Domain names lifetime](#h-domain-names-lifetime)
  + [Proxy servers](#h-proxy-servers)
* [Mamba 2FA Indicators of compromise](#h-mamba-2fa-indicators-of-compromise)
  + [Relay server IP addresses](#h-relay-server-ip-addresses)
  + [Relay server domain names](#h-relay-server-domain-names)

## Introduction

In late May 2024, Sekoia’s Threat Detection & Research (TDR) team received an insight from a partner about an ongoing phishing campaign leveraging HTML attachments that mimicked Microsoft 365 login pages. The phishing pages were able to relay some methods of multi-factor authentication (MFA), and made use of the Socket.IO JavaScript library to communicate via websockets with a backend server. At first, these characteristics look like [the *Tycoon 2FA* phishing-as-a-service platform](https://blog.sekoia.io/tycoon-2fa-an-in-depth-analysis-of-the-latest-version-of-the-aitm-phishing-kit), but further inspection found that the campaign leveraged **a previously unknown adversary-in-the-middle (AiTM) phishing kit**, that Sekoia track as ***Mamba 2FA***.

TDR illuminated the infrastructure hosting the phishing pages and developed detection rules to identify Entra ID accounts compromised via this kit. Retro-hunting uncovered that several Sekoia XDR customers have been targeted by campaigns leveraging *Mamba 2FA* in the previous months, suggesting a **widespread threat**. Finally, during this investigation we identified that the kit was **sold as phishing-as-a-service (PhaaS)**.

On 26 June 2024, [ANY.RUN published an analysis of a phishing campaign](https://any.run/cybersecurity-blog/analysis-of-the-phishing-campaign/) that matched the characteristics and infrastructure of *Mamba 2FA*. Since then, and likely in reaction to this publication, the phishing kit and associated infrastructure have undergone several significant changes.

## Characteristics of *Mamba 2FA* phishing pages

### URL structure and domain names

As of October 2024, the URLs of *Mamba 2FA* phishing pages have the following structure:

```
https://{domain}/{m,n,o}/?{Base64 string}
```

For example:

```
https://tubope[.]com/n/?c3Y9bzM2NV8xX25vbSZyYW5kPVZFUnhiR1k9JnVpZD1VU0VSMjUwOTIwMjRVMDgwOTI1NTk=
```

The phishing page is displayed only if a valid Base64 parameter is present. If the parameter is absent or invalid, the page is blank.

However, the phishing kit also tries to detect automated web browsers and security sandboxes. In this case, the visitor is redirected to `https://google.com/404/`.

### Base64-encoded parameter

Once decoded, the Base64 parameter follows the structure of a URL query string, with 3 field-value pairs. For example:

```
sv=o365_1_nom&rand=VERxbGY=&uid=USER25092024U08092559
```

* `sv` controls the appearance of the phishing page
* `rand` is a Base64-encoded pseudo-random string, whose function is unknown
* `uid` is presumed to be a unique identifier for each customer of the PhaaS platform

#### Targeted email address

The email address targeted by the phishing attempt can be added at the end of the URL, separated from the Base64 parameter by the string `N0123N`, or by a `#` (URL fragment). If present, this address will be automatically pre-filled in the login form. This email address is optionally Base64-encoded. The four examples below are equivalent:

```
https://tubope[.]com/n/?c3Y9bz...TI1NTk=N0123Nsatyan@microsoft.com
https://tubope[.]com/n/?c3Y9bz...TI1NTk=N0123Nc2F0eWFuQG1pY3Jvc29mdC5jb20=
https://tubope[.]com/n/?c3Y9bz...TI1NTk=#satyan@microsoft.com
https://tubope[.]com/n/?c3Y9bz...TI1NTk=#c2F0eWFuQG1pY3Jvc29mdC5jb20=
```

#### Appearance of the phishing pages

The appearance of the phishing page can be one of four types, depending on the `sv` parameter:

* `sv=o365_#_one` imitates OneDrive
* `sv=o365_#_nom` is a generic Microsoft sign-in page
* `sv=o365_#_sp` mimics a SharePoint Online secure link
* `sv=o365_#_voice` purports to be a voice mail, then displays a generic Microsoft sign-in page after a click

(where `#` is a number, usually `1` in recent weeks, whose function is unknown)

![Mamba 2FA OneDrive phishing page](data:image/svg+xml... "OneDrive template")![Mamba 2FA OneDrive phishing page](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/flint_2024_034_fig1_3-1024x768.png "OneDrive template")
![Mamba 2FA SharePoint Online phishing page](data:image/svg+xml... "SharePoint Online secure link template")![Mamba 2FA SharePoint Online phishing page](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/flint_2024_034_fig1_1-1024x768.png "SharePoint Online secure link template")
![Mamba 2FA generic Microsoft 365 phishing page](data:image/svg+xml... "generic Microsoft sign-in page template")![Mamba 2FA generic Microsoft 365 phishing page](https://t7f4e9n3....