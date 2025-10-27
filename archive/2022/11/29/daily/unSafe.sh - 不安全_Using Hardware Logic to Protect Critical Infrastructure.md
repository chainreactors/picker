---
title: Using Hardware Logic to Protect Critical Infrastructure
url: https://buaq.net/go-137610.html
source: unSafe.sh - 不安全
date: 2022-11-29
fetch_date: 2025-10-03T23:57:07.852092
---

# Using Hardware Logic to Protect Critical Infrastructure

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

![](https://8aqnet.cdn.bcebos.com/248f75d1ae62b75547a8add488edd3f5.jpg)

Using Hardware Logic to Protect Critical Infrastructure

Welcome to the fourth post from Forcepoint's 2023 Future Insights series, which offers insights
*2022-11-28 20:44:41
Author: [www.forcepoint.com(查看原文)](/jump-137610.htm)
阅读量:18
收藏*

---

Welcome to the fourth post from Forcepoint's [**2023 Future Insights series**](https://www.forcepoint.com/blog/tags/future-insights-2023), which offers insights and predictions on cybersecurity that may become pressing concerns in 2023.

Here's the next post from **[Dr. Simon Wiseman](https://www.forcepoint.com/company/biographies/dr-simon-wiseman),**Chief Technology Officer, G2CI:

More than ever, we need a solid defense against cyberattacks. With everything being connected to everything else, our systems are exposing an ever-greater attack surface, and attack detection is proving to be [a poor strategy](https://www.forcepoint.com/blog/x-labs/future-insights-age-of-prevention)—it’s a case of too little, too late.

Good cyber hygiene — anti-virus scanning and keeping patches up to date – is essential, but these defenses don’t go far enough. Relying on detection of known attacks and stopping them before they cause damage is not working. It leaves organizations vulnerable to unknown “zero-day” exploits, and once a system has been penetrated it is difficult to detect and evict the attackers. That’s why keeping attackers out still matters.

In any system, stopping attacks is important. But just as important, it must allow the communication that’s essential to business to continue. Hiding inside the cyber equivalent of a medieval castle with the drawbridge raised gives great protection, but you can’t trade so you are soon out of business.

Trading with others means exchanging information. And as soon as that is allowed, the applications receiving information from outside expose an attack surface that could be exploited. Those vulnerabilities put personal or sensitive information at risk. These issues must be tackled by deploying a defense that controls what information flows in and out of the system. In Forcepoint terms, this means deploying our [Content Disarm and Reconstruction](https://www.forcepoint.com/product/zero-trust-cdr) (CDR) and [Data Loss Prevention](https://www.forcepoint.com/product/dlp-data-loss-prevention) (DLP) products.

## **Lots of overhead and complexity in traditional defenses**

However good these defenses are, they require a lot of infrastructure to support them – an operating system, networking stack, crypto libraries etc. This level of overhead adds complexity to the equation. Complexity opens the door for flaws or configuration mistakes. Which means the information flow defense ends up built on sand. This is particularly important for Zero Trust CDR which must directly face potential attackers.

For an effective defense, you need a solid foundation where the complexity is controlled and managed. This is best done by using cloud infrastructure. Cloud services are designed to protect themselves from intruders, keep tenants separate and are patched and continuously monitored by teams who are dedicated to the task. Hosting the defenses in the cloud, [like we do](https://www.forcepoint.com/blog/insights/forcepoint-one-zero-trust-foundation) for our [Forcepoint ONE SSE platform](https://www.forcepoint.com/product/forcepoint-one), gives them a solid foundation and provides scalability. All that remains is to make sure the Zero Trust CDR measures are implemented well enough to face the attackers, which is a separate problem I will return to later.

> But if we can’t rely on software for security, what option do we have?
>
> Use hardware logic in place of software to implement the critical security functions we need."

## **Protecting critical infrastructure with hardware logic**

But not everything can be in the cloud. In the case of critical infrastructure—plant equipment in industrial systems or tactical defense systems, for example—there’s usually a need to build out an on-premises infrastructure. Here a more robust security approach is needed. This kind of equipment often times has to survive in a hostile environment, both physically and from a cyber point of view. And it’s not practical to have a dedicated cyber ops teams looking after it continuously. In these cases, the platform must stand alone and defend itself.

Here, rather than manage the complexity of the platform’s software, we must eliminate reliance on it. But if we can’t rely on software for security, what option do we have? Use hardware logic in place of software to implement the critical security functions we need. There’s just one obstacle to overcome with this–logic is less flexible than software, so it can only do simpler fixed tasks. In reality, that’s where its strength lies – once the logic has been proven to be working correctly, it stays working correctly. Software is malleable, it can change itself, so what works today might not work tomorrow. Logic is immutable, a strong defense stays strong.

## **Combining hardware logic with software defenses**

But how can simple logic provide the complex Zero Trust CDR defenses we need? CDR is an inherently complex process that can only be implemented with complex software. The reality is this: Complexity is only a problem when you need to rely on it —we need an implementation that still delivers security even if the complex functions are flawed.

A quick summary of how [Forcepoint’s Zero Trust CDR](https://www.forcepoint.com/product/zero-trust-cdr) handles data: When examining a document, it doesn’t check the data or modify it. It extracts the information carried by the data, discards all the data (even if it happens to be safe), and then builds new data to carry that information to its destination. This approach means no data from a potential attacker is trusted. But the fact it’s split into two parts is crucial. The first part is complex and handles data that might be unsafe, but the second part is simpler and only handles the extracted information.

Our implementation allows the two parts can be separated, joined only by a simple communications path carrying the information in a simple way. This interconnection is simple enough to be implemented in hardware logic. The interconnect’s job is to make sure that the protocol is being followed and that the information carried is structured as expected and so will be safely handled.

![Forcepoint Future Insights 2023 series - What will you need to think about in 2023?](https://www.forcepoint.com/sites/default/files/future_insights_2023-generic-1200x628-28oct2022.jpg)

With this in place, no reliance is placed on the complex first part that extracts information from data – if it behaves in an unsafe way the logic will prevent any damage spreading to the second part. The second part, which builds the new data to carry the information, is shielded from attack by the simple hardware logic. The complexity of CDR has not been eliminated, but it has been pushed into a position where it can do no harm.

In initial deployments, we used this hardware logic model to secure critical government agencies and business organizations. Today, however we’re seeing increased interest in the hardware logic method from the wider critical infrastructure who need to connect field units back to base and to the cloud (see [this whitepaper for more).](https://www.forcepoint.com/resources/whitepapers/connecting-field-base-and-cloud)

In 2023 and beyond, organizations need to step up and use defenses that take on the sophisticated attackers t...