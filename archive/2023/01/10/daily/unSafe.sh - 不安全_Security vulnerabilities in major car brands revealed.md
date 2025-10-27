---
title: Security vulnerabilities in major car brands revealed
url: https://buaq.net/go-144857.html
source: unSafe.sh - 不安全
date: 2023-01-10
fetch_date: 2025-10-04T03:22:45.968871
---

# Security vulnerabilities in major car brands revealed

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

Security vulnerabilities in major car brands revealed

Your car potentially hasn’t “just” been a car for a long time. With mul
*2023-1-9 23:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-144857.htm)
阅读量:10
收藏*

---

Your car potentially hasn’t “just” been a car for a long time. With multiple digital systems, vehicles are increasingly plugged into web applications and digital processes. These systems tie into everything from passwords and web chat systems for car company employees, to file repositories and other parts of business infrastructure which potentially feed back into the vehicles themselves.

Sounding horns, disabling start up, reporting a vehicle as stolen, even accessing built in cameras are all possible for rogue entities should they manage to break into a manufacturer’s network.

New research has been [revealed in the world of car hacking](https://samcurry.net/web-hackers-vs-the-auto-industry/), which builds and expands upon a way to reveal [car owner details via VIN numbers](https://www.malwarebytes.com/blog/news/2022/12/vehicle-identification-numbers-reveal-driver-data-via-telematics) which we covered last month. These latest revelations come from the same researcher, Sam Curry, and his collective of car technology explorers and investigators.

## Viewing a problem in isolation

Last time around we saw how publicly available data that was visible on a car was being tied back to telematics, and how that data could reveal an awful lot of information about the car owner. It was also possible to send basic instructions to the VIN associated vehicle, such as honking the horn or flashing the lights.

As it turns out, the exploration of how fast moving, incredibly heavy objects are tied to digital systems is a [lot more comprehensive](https://therecord.media/ferrari-bmw-rolls-royce-porsche-and-more-fix-vulnerabilities-giving-car-takeover-capabilities/) than first thought. In fact, many major brands have their digital systems tied to single sign on (SSO) systems, and badly configured endpoints which grant dizzying levels of access to those in the know.

The brands mentioned in the report include:

* **Kia**
* **Honda**
* **Infiniti**
* **Nissan**
* **Acura**
* **Mercedes-Benz**
* **Hyundai**
* **Genesis**
* **BMW**
* **Rolls Royce**
* **Ferrari, Spireon**
* **Ford**
* **Reviver**
* **Porsche**
* **Toyota**
* **Jaguar**
* **Land Rover**
* **SiriusXM**

Where things go wrong is that many of these systems were found to be vulnerable to multiple forms of exploitation. While many of the digital systems in vehicles are isolated from one another, it all goes wrong quickly if an SSO outside of the car owner’s control allows for developer or administrator-level access.

## What access, data, and control was made available to researchers

The complete list is way too long to republish here, but some of the most impressive results from a variety of manufacturers are mentioned below:

* Full admin access to a company-wide admin panel, allowing for the sending of arbitrary commands to roughly 15.5 million vehicles (start engine, disable starter, unlock, read device location, flash and update firmware).
* Update vehicle status to “stolen”, updating both license plate and notifying authorities
* Authenticate into user account and perform actions against vehicles.

These three alone have the potential for sheer chaos, especially in relation to notifying law enforcement. Nothing quite matches the audacity of [killing a jeep on the highway](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/) from way back in 2015, but these vulnerable SSO systems increasingly offer ways to mess with car owners in more and more convoluted ways.

For sheer malicious troll value alone, what could match authorities flagging down your car? It’s entirely possible that an incredibly unlucky individual could end up in a [vehicular based swatting scenario](https://www.malwarebytes.com/swatting%23%3A~%3Atext%3DSwatting%2520is%2520when%2520a%2520bad%2CSWAT%2520team%29%2520to%2520your%2520home.), but with weapon touting officers surrounding your car instead of your home. Elsewhere, instead of malicious individuals spying on your bedrooms with insecure security cameras, we have live views from inside a car.

There is almost no level of privacy invasion, personal risk, or data leak exposure left unturned. I’m a big believer in not overhyping security risks and vulnerabilities but what Curry and team uncovered here is not fantastic by any stretch of the imagination. No matter what your angle of attack, whether your interest is in social engineering, pranking, system tampering, or data collection, there’s potentially something for everyone.

## Are these issues still a problem?

Thankfully, no, as Curry mentions that “all vulnerabilities” were [fixed within a week](https://therecord.media/ferrari-bmw-rolls-royce-porsche-and-more-fix-vulnerabilities-giving-car-takeover-capabilities/), with all of the manufacturers being very responsive to the vulnerability reports. If you own one of the brands listed in the report, you don’t need to do anything as everything mentioned has been addressed.

Given the sheer scale of the finds from this small band of researchers, it may be more concerning should your model of car not be on the list. We simply don’t know what’s out there, and may not unless Sam or other researchers compile fresh lists of findings. For the time being, you may wish to dig into whether or not your non-listed model of car comes with any digital systems or services and if there happens to be any telematics running in the background.

Many systems allow you to set security measures in place related to logins and data collection, but as with any potential situation involving unauthorised access behind the scenes, this may not help where someone has access to the admin account. For now, drive safely and we wish you a non-compromised journey.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/01/security-vulnerabilities-in-major-car-brands-revealed
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)