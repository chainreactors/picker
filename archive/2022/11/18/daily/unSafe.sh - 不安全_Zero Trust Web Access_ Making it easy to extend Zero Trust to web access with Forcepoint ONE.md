---
title: Zero Trust Web Access: Making it easy to extend Zero Trust to web access with Forcepoint ONE
url: https://buaq.net/go-136122.html
source: unSafe.sh - 不安全
date: 2022-11-18
fetch_date: 2025-10-03T23:05:20.914964
---

# Zero Trust Web Access: Making it easy to extend Zero Trust to web access with Forcepoint ONE

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

![](https://8aqnet.cdn.bcebos.com/b015b8213b3727c9c029ffc94b86a471.jpg)

Zero Trust Web Access: Making it easy to extend Zero Trust to web access with Forcepoint ONE

Web access is critical… so why is it overlooked?One thing that has often been overlooked thou
*2022-11-17 21:44:12
Author: [www.forcepoint.com(查看原文)](/jump-136122.htm)
阅读量:21
收藏*

---

**Web access is critical… so why is it overlooked?**

One thing that has often been overlooked though is the typical user’s dependency on general web access. It’s important since general web use is often the largest threat vector for most organizations.  Clicking on an unsafe link is often the start of an attack. Outside of that, scanning of resources exposed to the public internet is a standard reconnaissance tactic to identify potential victims of a ransomware attack or data breach.  The simple reality is that employees need access to a spectrum of resources to do their jobs. We also have different levels of control over each.

Web access is one of the most widely used resources across departments within organizations and across different types of organizations.  But by far, we have the least control over general web content. If we were to graph private resources, cloud resources, and general web use in terms of control it would probably look something like this:

![Private resource graph - Zero Trust Web Accesss](https://www.forcepoint.com/sites/default/files/ztwa_-_resource_graph.jpg)

For the middle section on Cloud Apps, just consider the common Shared Responsibility Models to see the gradually reducing control an organization has over a resource as it moves from Infrastructure as a Service (IaaS) to Platform as a Service (PaaS) and Software as a Service (SaaS).  IaaS provides organizations with more control than PaaS or SaaS.  When we get to the web, there is no control whatsoever, it drops off.  However, we can’t just cut off access to the internet since it’s critical to so many tasks, so we are opening ourselves up to the associated risks.  And these risks aren’t just from one direction, it is not just inbound malware that we need to stop, it is also outbound data loss.

**Limiting access only to trusted sites doesn’t cut it**

General web filtering has been around for decades and has always proven less than perfect.  [Secure Web Gateways](https://www.forcepoint.com/product/secure-web-gateway) (SWG)s takes things a step further and give organizations a way to implement an inline check to scan web traffic for content like sensitive data and look for malware signatures.  If you are using the data loss prevention (DLP) capabilities fully than you can really stop sensitive data from leaving the organization, but many that don’t have strong DLP capabilities find it hard to do much more than just audit and send alerts.

Even harder is the malware side of things.  We have things like malware signatures, but that requires first detecting the malware.  This means that zero-day threats i.e., those that no one has seen before, can still slip through.  Often downloading files can also provide ways of slipping parts of malware onto a host machine to then compromise later.

The sensible answer is to only allow access to web content that you know you can trust.  However, there are times that organizations may still have requirements to access certain sites or types of sites regardless of the risk present.  This could be a financial institution looking into a newly created website to determine whether to approve a loan, this could be related to an insurance company investigating fraud, or even be something as innocent as sending and downloading images on social media.

The key question remains: How do we implement anything like the Zero Trust controls that we have for private and cloud apps over all the web content we don’t manage? The answer is a concept I am calling [**Zero Trust Web Access**](https://www.forcepoint.com/newsroom/2022/forcepoint-data-first-sase-pioneers-industrys-most-complete-single-vendor-offering).

**Zero Trust Web Access provides protection and access**

Zero Trust Web Access allows you to isolate and secure a browser session with [Remote Browser Isolation](https://www.forcepoint.com/product/remote-browser-isolation) (RBI).  Think of it like using FaceTime on your phone to live stream an interaction with a website.  All the user really gets is a streamed video of what is happening in a remotely isolated browser.  This allows users to access web content—even if it is malicious.  The remote browser may get infected, but it is deleted at the end of the session. In other words, none of it can touch the end user’s machine.

[Content Disarm and Reconstruction](https://www.forcepoint.com/product/zero-trust-cdr) (CDR) within the RBI takes things a step further. It sanitizes documents and images, recreating them from scratch as clean files without any potentially hidden elements like malware or sensitive data hidden within an image.  By combining CDR with RBI as a highly secure control for risky web traffic managed with a secure web gateway (SWG) you can easily route risky traffic through these heightened protections and send safer traffic through normal SWG controls.

This allows you to wrap enough control around web traffic to insulate users to provide true Zero Trust protections. And even better, as a core part of a single-vendor SASE solution, you have an easy and strategic path to adopt a unified security platform providing safe and fast access for your users and branch sites everywhere.  From access to web content, to cloud resources, to private apps and networks-Forcepoint simplifies the path to Zero Trust.

Find out more about Forcepoint ONE SWG here: <https://www.forcepoint.com/product/secure-web-gateway>.

文章来源: https://www.forcepoint.com/blog/insights/zero-trust-web-access-extends-zero-trust-model-to-web-access
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)