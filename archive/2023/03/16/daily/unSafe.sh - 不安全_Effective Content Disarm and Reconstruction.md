---
title: Effective Content Disarm and Reconstruction
url: https://buaq.net/go-153596.html
source: unSafe.sh - 不安全
date: 2023-03-16
fetch_date: 2025-10-04T09:42:54.243039
---

# Effective Content Disarm and Reconstruction

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

Effective Content Disarm and Reconstruction

The first problem is that not all malware is executable code. Applications are invariably so co
*2023-3-15 19:39:42
Author: [www.forcepoint.com(查看原文)](/jump-153596.htm)
阅读量:16
收藏*

---

The first problem is that not all malware is executable code. Applications are invariably so complex that they contain flaws, mostly in the way they handle unusual or malformed data – anything more obvious tends to get fixed. With carefully crafted data, the applications can be persuaded to execute it, even though it is not code. Simply ripping out embedded code and scripts does nothing to remove this data that should be passive but isn’t, so the CDR fails to block the attack.

**Zero Trust CDR – A modern approach**

The solution to this was a new form of CDR, which Forcepoint pioneered. It’s called Zero Trust CDR because with this no data from outside is trusted and so none is ever allowed in. This sounds strange – how does anything get into the system if all data is blocked? Well, although no data gets in, the useful information carried by the data does. It is extracted from the original data to form a model of what the data is about. This model is brought into the system and then new data is constructed to deliver the information. In this way, an attacker’s data never gets in, but the information people need does, carried by data that has been constructed on the inside by the Zero Trust CDR solution.

But Zero Trust CDR isn’t a magic wand – it only fixes the malware problem if it gets invoked. So another problem emerges. Data needs to be fed into the Zero Trust CDR, which means it needs to be able to interact with potential attackers. That means attackers might be able exploit flaws in the infrastructure to disable or bypass the protection. For example, [EternalBlue is a flaw](https://arstechnica.com/information-technology/2022/12/critical-windows-code-execution-vulnerability-went-undetected-until-now/) in the Windows protocol stack that allows attackers to run their own code on a server. If the CDR software were running on a Windows server vulnerable to this, an attacker could run code that delivered unsafe files into the network.

Keeping servers fully patched and hiding them behind firewalls, to limit the services that are exposed to an attacker, is the obvious answer here, but this can require a lot of expertise to do right. For many organisations, the most effective way of getting this is to leave it to the experts – that is, put the Zero Trust CDR software in the cloud and let the cloud service provider worry about the infrastructure’s security.

But the cloud is not for everyone. Some systems can’t go there (physical plant equipment for example) and for some organisations the public cloud is just not trustworthy enough (military systems and nuclear power stations for example). In these circumstances what’s needed is a way of deploying Zero Trust CDR without needing a complex infrastructure.

**Zero Trust CDR operates in two ways that can be deployed separately**

With the original idea of CDR, there’s no way this can be done. The CDR software needs to run on a server and that server must interact with the outside world to receive the data to be processed. The protocol stack needed for this is complex and so prone to flaws that an attacker can exploit. But [Forcepoint Zero Trust CDR](https://www.forcepoint.com/product/zero-trust-cdr) is different. It operates in two parts that can be deployed separately – the information extraction software must run on a server that interacts with potential attackers, but the data building software can run on a separate server that exposes a much simpler interface – simpler because it need only interact with the information extraction software to receive the model it has built.

That means Zero Trust CDR can be deployed on two physically separate servers. The outer server is exposed to attack and may succumb. But the inner server is the only one that can deliver data into the protected network, and it presents a much simpler interface that is much easier to get right. In terms of the cloud, the two servers can be run in different tenancies, so the cloud infrastructure is responsible for keeping them apart.

Even though the second, data building, server offers a much simpler interface than the first server, sometimes its complexity will still be too great to trust. For example, the firmware of the network interface card in the server might be flawed in such a way that the attacker can use it to get full access to the entire server. Such a flaw would be very hard to find, but anyone knowing about it can bypass the Zero Trust CDR. If a system faces attackers with that level of knowledge and skill, it’s a risk they cannot take.

Because Zero Trust CDR can be implemented in two parts, there’s a way forward. The information extraction software might be taken over by an attacker, and the interface to the data building software might have a flaw, but being a simple interface, it is possible to add an independent check that it is operating correctly. This check would make sure the model passing across the interface is valid, and so be properly handled by the data building software, and the protocol used to transport the model is being followed, and so not exploiting any hidden flaws in the protocol stack.

It's important this check is independent of the Zero Trust CDR software and the infrastructure supporting it, otherwise there’s the risk of a common flaw allowing an attacker to take over each component in turn. This is impossible to do with software, as its complexity means you can never be sure there’s nothing in common, but it can be done with hardware logic. Implementing the check in logic not only ensures independence, but it also means it can be done fast.

**High Speed Verifier and hardware logic**

Forcepoint take this approach with our [High Speed Verifier](https://www.forcepoint.com/product/high-speed-verifier) (HSV). This is a [hardware logic device](https://www.forcepoint.com/blog/x-labs/hardware-logic-protect-critical-infrastructure) that passes a stream of data only if that stream correctly represents a valid information model for the application and the protocol is followed. The device is placed between the servers running the Zero Trust CDR software. The logic implements the protocol stack and checks the data, providing true independence from the Zero Trust CDR software and its infrastructure.

There are two variants of the HSV. One (HSV2) is designed for data centre use. It is a 1U rack mount appliance housing up to four independent verifiers that are managed from a separate network. The other (HSVT), designed for embedding into a system, is a card that fits into a server chassis. This is managed using a USB interface. Between them, these devices cover use cases in defence systems and critical national infrastructure.

Zero Trust Content Disarm and Reconstruction addresses the malware threat, but it needs to be deployed in a way that means it always gets invoked. For most systems, a cloud solution is ideal, and Forcepoint’s public cloud services deliver Zero Trust CDR as [part of Microsoft 365 Mail](https://www.forcepoint.com/product/zero-trust-cdr-mail-m365), [CASB](https://www.forcepoint.com/product/casb-cloud-access-security-broker), and [Remote Browser Isolation](https://www.forcepoint.com/product/remote-browser-isolation) solutions, as well as APIs for custom applications. Otherwise, the HSV can be deployed to protect critical applications that have to connect to other, untrustworthy, systems. For example, HSVT a...