---
title: ICS/OT/IoT Security: challenges and protection strategies
url: https://www.adainese.it/blog/2024/09/05/ics/ot/iot-security-challenges-and-protection-strategies/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-07
fetch_date: 2025-10-06T18:29:43.232519
---

# ICS/OT/IoT Security: challenges and protection strategies

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# ICS/OT/IoT Security: challenges and protection strategies

#### Table of contents

* [Lifespan vs. Support Duration](#lifespan-vs-support-duration)
* [Component Lifespan](#component-lifespan)
  + [Bluetooth](#bluetooth)
  + [WiFi](#wifi)
  + [HMI](#hmi)
* [Vulnerability Management](#vulnerability-management)
* [Defense Strategies](#defense-strategies)
* [Network Segmentation](#network-segmentation)
* [Network Access](#network-access)
* [Code Security](#code-security)

#### Latest posts

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)

[Creating an interface in Strata Cloud Manager](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)
October 05, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 160 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 124 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## ICS/OT/IoT Security: challenges and protection strategies

Andrea Dainese

September 05, 2024

[CISO](/categories/ciso/ "All posts under CISO")

[![Post cover](/images/categories/ciso.webp)](/images/categories/ciso.webp)

It’s time to revisit the ICS/OT world, as it has unique characteristics that influence its processes and tools.

First, I would categorize this broad field into the following groups:

* Systems localized within a confined area (e.g., a building or campus)
* Systems geographically distributed but accessible through protected/dedicated networks (often SCADA systems fall under this category)
* Systems geographically distributed and connected to the Internet without additional controls (often IoT systems fall under this category).

I’ve chosen this classification because, as we’ll see in the following posts, it dictates our ability to mitigate risks by implementing additional security measures. Clearly, there are other categorizations we should consider (e.g., based on risk), but this is the one I’d like to use as a starting point.

Based on my experience, I want to highlight that most ICS/OT/IoT systems have a longer lifespan than the support period of individual components. This is crucial when planning a realistic strategy. Even though certain regulations require that components be upgradable, we will inevitably face situations where we need to protect components that are no longer sold, supported, or maintained.

## Lifespan vs. Support Duration

As previously mentioned, in my experience, ICS/OT/IoT systems often remain operational for longer than the manufacturers of individual components anticipated. In other words, the components (particularly software, but not exclusively) are no longer supported, yet the integrated system is still in use.

Those familiar with the industrial, medical, maritime, or oil & gas sectors (and I’d add banking as well) encounter this daily: systems are based on components (e.g., Windows) and remain active well beyond the end of their support period. This is unavoidable for three reasons:

1. The aforementioned systems are generally untouchable: no changes or updates are permitted because their effects are unknown. In some cases, I’ve had vendors strongly advise against updating IEC62443-certified products, despite the regulation allowing for it.
2. Many of the above systems have a very high acquisition cost (in terms of millions or tens of millions). Decommissioning or even simple refitting incurs unjustifiable costs for a system that is still functional (in the sense that it performs its intended work).
3. I’ve often encountered operational systems supplied by defunct companies, leaving no support available. Here again, the cost of acquiring a new system is unjustifiable.

The three points above mainly stem from the approach of the companies and individuals designing such systems. These systems are built to perform their tasks safely, even under stress. But… when we began discussing Industry 4.0 and started connecting systems designed to work to an IP network, we introduced a new risk: Cyber risk.

In conversations with suppliers and customers of ICS/OT/IoT systems, I realize that Cyber risk is not even considered. To be honest, as a professional, I find some topological choices rather peculiar.

In this regard, manufacturers and integrators still need to fully grasp the implications of bringing fragile technologies (from a Cyber perspective) onto IP and connecting them to the Internet.

Given the topic, I’d add that the regulatory world is moving in a certain direction (see NIS, machinery regulation, IMO…). Will we finally see concrete results? Personally, I’m not so optimistic.

## Component Lifespan

We’ve discussed regulations and reality. Now, let’s look at some examples demonstrating that component lifespan will inevitably be shorter than system lifespan. As mentioned earlier, systems continue to be used until they fail and repairs become economically unfeasible compared to purchasing a new system.

Let’s examine a few examples.

### Bluetooth

In the ICS world, I’ve noticed a preference for using Bluetooth in recent years to simplify system reconfiguration activities. Specifically, Bluetooth is used to remote some control commands (non-emergency). In this case, we should consider the risks introduced by a wireless protocol, but for now, let’s focus on the various protocol releases. A new Bluetooth protocol standard is released approximately every 2-3 years. This means that in an industrial system with a lifespan of 15 years, we could find very old and potent...