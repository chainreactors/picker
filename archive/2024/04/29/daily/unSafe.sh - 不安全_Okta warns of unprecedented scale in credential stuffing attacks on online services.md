---
title: Okta warns of unprecedented scale in credential stuffing attacks on online services
url: https://buaq.net/go-236940.html
source: unSafe.sh - 不安全
date: 2024-04-29
fetch_date: 2025-10-04T12:15:01.892790
---

# Okta warns of unprecedented scale in credential stuffing attacks on online services

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Okta warns of unprecedented scale in credential stuffing attacks on online services

Okta warns of unprecedented scale in credential stuffing attacks on online servicesIdentity an
*2024-4-28 22:34:36
Author: [securityaffairs.com(查看原文)](/jump-236940.htm)
阅读量:12
收藏*

---

## Okta warns of unprecedented scale in credential stuffing attacks on online services

![](https://i0.wp.com/securityaffairs.com/wp-content/uploads/2022/12/okta-vector-logo.png?fit=900%2C500&ssl=1)

## Identity and access management services provider Okta warned of a spike in credential stuffing attacks aimed at online services.

In recent weeks, Okta observed a surge in [credential stuffing attacks](https://securityaffairs.com/76527/hacking/credential-stuffing-attacks-report.html) against online services, aided by the widespread availability of residential proxy services, lists of previously compromised credentials (“combo lists”), and automation tools.

*“Over the last month, Okta has observed an increase in the frequency and scale of credential stuffing attacks targeting online services, facilitated by the broad availability of residential proxy services, lists of previously stolen credentials (“combo lists”), and scripting tools.” reads the [**advisory**](https://sec.okta.com/blockanonymizers) published by Okta.*

From March 18, 2024, to April 16, 2024, Duo Security and Cisco Talos [observed](https://securityaffairs.com/161943/hacking/brute-force-attacks.html) large-scale brute-force attacks against a variety of targets, including VPN services, web application authentication interfaces and SSH services.

Below is a list of known affected services:

* Cisco Secure Firewall VPN
* Checkpoint VPN
* Fortinet VPN
* SonicWall VPN
* RD Web Services
* Miktrotik
* Draytek
* Ubiquiti

From April 19, 2024 through to April 26, 2024, the Okta Identity Threat Research team observed a spike in credential stuffing activity against user accounts from what appears to be similar infrastructure.

A credential stuffing attack is a type of cyber attack where hackers use large sets of username and password combinations, typically obtained from previous data breaches, phishing campaigns, or info-stealer infections, to gain unauthorized access to user accounts on various online services. Credential stuffing attacks exploit the widespread practice of using the same login credentials across multiple online accounts. Attackers automate the process of trying these credentials on various websites until they find a match, granting them unauthorized access to compromised accounts. This method poses a risk of exposing sensitive data or enabling fraudulent activities.

The attacks recently observed by Okta route requests through anonymizing services like TOR and residential proxies such as NSOCKS, Luminati, and DataImpulse. The experts noticed that millions of requests have been routed through these services.

Residential proxies (RESIPs) are networks of legitimate user devices used to route traffic for paying subscribers, often without their knowledge. Threat actors use these RESIPs to evade detection. Users may consciously download “proxyware” for payment or other benefits, or their devices may be infected with malware unknowingly, turning them into part of a botnet.

“The net sum of this activity is that most of the traffic in these credential stuffing attacks appear to originate from the mobile devices and browsers of everyday users, rather than from the IP space of VPS providers. For more information on residential proxy services, we recommend this [informative summary](https://www.orangecyberdefense.com/be/blog/unveiling-the-depths-of-residential-proxies-providers) by CERT Orange Cyberdefense and Sekoia.” continues the advisory.

The advisory includes recommendations to mitigate the risk of account takeovers from credential stuffing attacks along with TTPs used in recent campaigns.

[**Pierluigi Paganini**](http://www.linkedin.com/pub/pierluigi-paganini/b/742/559)

Follow me on Twitter: [**@securityaffairs**](https://twitter.com/securityaffairs) and [**Facebook**](https://www.facebook.com/sec.affairs) and [Mastodon](https://infosec.exchange/%40securityaffairs)

**(**[**SecurityAffairs**](http://securityaffairs.co/wordpress/)**–** **hacking, credential stuffing)**

---

文章来源: https://securityaffairs.com/162464/hacking/okta-warned-spike-credential-stuffing-attacks.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)