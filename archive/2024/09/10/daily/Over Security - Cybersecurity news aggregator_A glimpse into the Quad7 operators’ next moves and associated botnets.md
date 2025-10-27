---
title: A glimpse into the Quad7 operators’ next moves and associated botnets
url: https://blog.sekoia.io/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-10
fetch_date: 2025-10-06T18:30:10.505678
---

# A glimpse into the Quad7 operators’ next moves and associated botnets

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

# A glimpse into the Quad7 operators’ next moves and associated botnets

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR, Felix Aimé, Pierre-Antoine D. and Charles M.](#molongui-disabled-link)
September 9 2024

0

15 minutes reading

#### Authors’ Note

This blog post is the second in a series of two on the Quad7 botnet. It presents the botnets operated by the Quad7 operators and deduce their possible next moves. However, if you are new on this topic, you can read the first blog post here: **[Solving the 7777 Botnet enigma: A cybersecurity quest](https://blog.sekoia.io/solving-the-7777-botnet-enigma-a-cybersecurity-quest/ "Solving the 7777 Botnet enigma: A cybersecurity quest")**

## Key Takeaways

* The Sekoia TDR team has recently identified new staging servers, leading to the discovery of additional targets, implants, and botnet clusters tied to the Quad7 operators.

* The Quad7 botnet operators seem to be compromising several brands of SOHO routers and VPN appliances, including TP-LINK, Zyxel, Asus, Axentra, D-Link, and Netgear, using multiple vulnerabilities—some of which are previously unknown.

* The Quad7 botnet operators appear to be evolving their toolset, introducing a new backdoor and exploring new protocols, with the aim of enhancing stealth and evading the tracking capabilities of their operational relay boxes (ORBs).

* Given these developments, it is possible that without interception capabilities, tracking the evolution of Quad7 botnets could become nearly impossible in the near future.

## Table of contents

* [Introduction](#h-introduction)
* [The wildcard login galaxy](#h-the-wildcard-login-galaxy)
* [When the Quad7 shells start calling home…](#h-when-the-quad7-shells-start-calling-home)
* [… and possibly abandon open socks proxies](#h-and-possibly-abandon-open-socks-proxies)
* [Conclusion](#h-conclusion)
* [Quad7 Botnet Indicators of compromise](#h-quad7-botnet-indicators-of-compromise)

## **Introduction**

Previously, we detailed [our investigation on the Quad7 botnet](https://blog.sekoia.io/solving-the-7777-botnet-enigma-a-cybersecurity-quest) and our live forensic methodology against a TP-LINK router to get related implants on it. Following this first publication, we continued to track this botnet activity and new clusters related to the Quad7 botnet operators.

Before our blogpost on the Quad7 botnet, we started to monitor another botnet, the alogin botnet (aka 63256 botnet) and attributed this botnet to the Quad7 botnet operators with medium confidence. On 7 August 2024, Team Cymru published a [blogpost](https://www.team-cymru.com/post/botnet-7777-are-you-betting-on-a-compromised-router) confirming the two botnets were operated by the same group as they shared some common administration servers.

Recently, we came across several staging servers, leading us to discover **new targets**, **implants** and **botnet clusters** associated with this threat actor. This new discovery allows us to have a glimpse of the Quad7 next moves as it seems that the operators are developing **HTTP reverse shells** and test **new projects** to relay their attacks instead of using simple **open socks proxies** to be more stealthy and prevent tracking.

## **The wildcard login galaxy**

As of this writing, we are aware of five different \*login clusters linked to this threat actor (**alogin**, **xlogin**, **axlogin**, **rlogin** and **zylogin**), which we are temporarily referring to internally as the **Quad7 Botnet Operators**.

The Quad7 botnet (aka 7777 botnet, **xlogin** botnet) is a botnet composed of compromised **TP-Link routers** which have both TCP ports TELNET/7777 and 11288 opened. The 7777 port is the administration port hosting a bind shell with root privileges (xlogin). This bind shell is password protected. The 11288 port is the Socks5 proxy port, mostly password protected, and this proxy is used to relay **M365 accounts brute force attacks**.

The **alogin** botnet is a botnet composed of compromised **Asus routers** which have both TCP ports 63256 and 63260 opened. The TELNET/63256 port is the administration port hosting a bind shell with root privileges (alogin). This bind shell is also password protected. The SOCKS/63260 port is hosting a password protected Socks5 proxy.

According to our telemetry the alogin botnet is used to relay **brute force attempts on internet exposed services such as VPN, telnet and SSH**. However, we took these observations with a grain of salt as different threat actors can relay attacks from the same compromised assets.

While looking for alogin samples, we found one on VirusTotal, which was hosted on a staging server controlled by the Quad7 operators. This led us to discover another \*login sample, named **rlogin** and used to target [**Ruckus Wireless**](https://www.ruckusnetworks.com) devices.

The bind shell of rlogin is listening on TCP port TELNET/63210. The bind shell is password protected and sometimes includes a challenge as well after the password prompt. The rlogin botnet does not seem to open a proxy port on compromised Ruckus devices. Another notable difference with the other \*login botnets is the botnet size, on one hand, there is the alogin and xlogin botnets with several thousand compromised devices. On the other hand, there is the rlogin botnet, which is **composed of 213 devices as of 26 August 2024 according to Censys**. The first infections for this botnet seem relatively new, with most of the devices compromised on 16 June 2024.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/FsynetProtocol-2.png)

The others \*logins are **axlogin**, which appears to be deployed on **[Axentra NAS](https://www.crunchbase.com/organization/axentra)**. Although we have a sample of this shell, we have not ...