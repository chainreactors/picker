---
title: Xenomorph v3: a new variant with ATS targeting more than 400 institutions
url: https://www.threatfabric.com/blogs/xenomorph-v3-new-variant-with-ats.html
source: Over Security - Cybersecurity news aggregator
date: 2023-03-11
fetch_date: 2025-10-04T09:17:17.834534
---

# Xenomorph v3: a new variant with ATS targeting more than 400 institutions

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## Xenomorph v3: a new variant with ATS targeting more than 400 institutions

10 March 2023

![](https://www.threatfabric.com/hubfs/cover-2.png)

### Jump to

## Xenomorph Introduces ATS and hundreds of new Targets

In the last year ThreatFabric saw a radical shift in the approach towards mobile malware from criminals. Criminals have started paying closer attention to the world of Mobile banking, abandoning more rudimental approaches in favor of a more refined and professional philosophy.

The most evident example of this new wave of malware creators is offered by the **Hadoken Security Group**. We have mentioned this actor previously in our blog about [BugDrop](https://www.threatfabric.com/blogs/bugdrop-new-dropper-bypassing-google-security-measures.html): the products developed and distributed by this group have been circulating for the entirety of 2022, while the actors themselves surfaced by claiming the ownership of the malware in May.

![hadoken](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/xenomorph-v3/hadoken.png?width=1920&height=1080&name=hadoken.png)

The main product of this group is [Xenomorph, a Android banking trojan discovered by ThreatFabric in February 2022](https://www.threatfabric.com/blogs/xenomorph-a-newly-hatched-banking-trojan.html). This malware family has been a work in progress for the entirety of 2022, and despite being distributed in small campaigns, it never truly reached the volume of other malware families on the threat landscape, such as Octo or more recently Hook.

Xenomorph campaigns have always been characterized by **short and contained distribution efforts**, first via GymDrop, a dropper operation created and managed by the same group, and later via [**Zombinder**, another distribution vector that we covered on a previous article in December 2022](https://www.threatfabric.com/blogs/zombinder-ermac-and-desktop-stealers.html). In either case, the short bursts of activity were indicative of short test runs opposed to a real large scale distribution with fraudulent intent.

However, things are very likely to change in the near future: ThreatFabric’s analysts have discovered a new variant of this malware family, which we classify as **Xenomorph.C**.

This new version of the malware adds many new capabilities to an already feature rich Android Banker, most notably the introduction of a very extensive **runtime engine powered by Accessibility services**, which is used by actors to implement a complete **ATS framework**. With these new features, Xenomorph is now able to completely automate the whole fraud chain, from infection to funds exfiltration, making it one of the **most advanced and dangerous** Android Malware trojans in circulation.

In addition, the samples identified by ThreatFabric featured configurations with Target lists made of **more than 400 banking and financial institutions**, including several **cryptocurrency wallets**, with an increase of more than 6 times with comparison to its previous variants, including financial institutions from all continents.

In addition, after discovering some samples belonging to this new variant, our researchers also discovered the **website** dedicated to the **advertisement** of this Android banker, indicating clear intentions of entering the **MaaS landscape**, and start large scale distribution.

![ad](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/xenomorph-v3/ad.png?width=1920&height=1080&name=ad.png)

This functionality is typical of more advanced malware families, such as Gustuff and SharkBot, which have caused thousands of euros worth of damage towards their targeted institutions.

In this article we will cover the main new features of this variant, and how these new variations can elevate Xenomorph’s threat level.

## Distribution

### Test Samples

ThreatFabric was able to identify also some samples connected to **test** campaigns: in these cases, the samples seem to be linked with distribution abusing third party hosting services, more specifically **Discord Content Delivery Network (CDN)**. This is not the first time we see malware using this sort of legitimate hosting services: it not uncommon to see malware authors use services such as Discord CDN or GitHub repositories to hide in plain sight their products.

![cdn](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/xenomorph-v3/cdn.png?width=1920&height=1080&name=cdn.png)

The reasons for using this sort of service are quite straight forward: these are very common services, which are very **reliable** and used by millions of people. In addition, it is **free** to open an account and use it to distribute malware and there are no limitation on the number of accounts. Finally, it is **very common** for devices to connect to such services, so it is less likely that a security service might flag connections to these domains as suspicious.

In this specific case it is likely that these samples, which are not really part of any campaign, were simply hosted on Discord CDN for sharing purposes, and not for distribution.

### Zombinder Campaign

The first variants of Xenomorph were distributed by **GymDrop**, in February 2022. Later in the year we saw the Hadoken group switch distribution medium, trying out first **BugDrop**, and finally landing on **Zombinder**. In our case, Xenomorph v3 is deployed by a **Zombinder** app “bound” to a legitimate currency converter, which downloads as an “update” an application posing as Google Protect:

![zombinder](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/xenomorph-v3/zombinder.png?width=1920&height=1080&name=zombinder.png)

This seems to be the method of choice with the third version of Xenomorph, abandoning previous in-house developed techniques. Despite this, actors behind Zombinder have claimed to have stopped providing the service, indicating that there might be once again a switch in distribution in future builds of Xenomorph.

## Targets

Xenomorph, since its first appearance, has revolved around **gathering PII** such as usernames and passwords using **overlay attacks**.

Over the course of 2022, Xenomorph has maintained a relatively stable set of targets in its configuration, with specific interest in **Spain**, **Portugal**, and **Italy**, with the latest campaigns also introducing **Belgian** and **Canadian** institutions, together with some cryptocurrency wallets.

The first sample of this new variant analyzed by ThreatFabric continued this trend, featuring the same list of targets as the previous versions observed. However, another sample, seemingly belonging to the same campaign, but sporting the tag “**xeno3-test**”, contained a much larger list of targets, counting **more than 400 institutions**, more than 6 times the number of targets available ...