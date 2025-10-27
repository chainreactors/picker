---
title: Network outage
url: https://www.adainese.it/blog/2024/07/31/network-outage/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-01
fetch_date: 2025-10-06T18:07:58.028675
---

# Network outage

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Network outage

#### Table of contents

* [Open Reflections](#open-reflections)
* [The Scenario](#the-scenario)
* [Final Notes](#final-notes)

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

## Network outage

Andrea Dainese

July 31, 2024

[Infrastructure](/categories/infrastructure/ "All posts under Infrastructure")

[![Post cover](/images/categories/infrastructure.webp)](/images/categories/infrastructure.webp)

In 2013, I [presented](https://www.adainese.it/files/slides/20130918-festival-ict-designing-an-hybrid-data-center-infrastructure.pdf "Designing an Hybrid Data Center Infrastructure") a critical case that could cause a complete isolation of a datacenter. Eleven years later, the situation remains the same.

Let’s reflect on a few points.

## Open Reflections

**Complexity:** Complexity has increased, with many more software layers than before. This complexity leads to misunderstandings, design errors, or unforeseen “blind spots” that can be particularly destructive. The term “complexity” has become a mantra, but we have brought it upon ourselves.

**Simplification:** Paradoxically, it is the opposite of the previous mantra and has been the driving force behind the introduction of various technologies to enable “things” previously deemed incorrect. For those who remember, STP was created this way. To simplify processes and make them more agile and faster, a series of software layers were introduced, leading to the previous point.

**Hybrid Devices:** Thanks to the two previous mantras, devices that behave partly like hosts and partly like switches were born. In the slides, I specifically refer to embedded devices in blade chassis. I described a corner case on HP in the slides, but this scenario is still valid for other vendors.

## The Scenario

Let’s discuss the scenario at hand.

The scenario involves a datacenter network that can be implemented in legacy mode or via fabric. Connected to this network are blade chassis with the aforementioned hybrid devices. Virtualization systems are generally running on the blades, but this is not strictly necessary. If, for any reason, a blade creates an L2 loop, in the absence of protections, the loop propagates through the fabric and all connected devices and chassis.

In the three cases I have experienced from 2013 to today, the fabric generally handles the traffic, but the hybrid switches do not. If the hybrid switches transport FCoE, the damage is obviously greater.

Best practices generally require configuring protection mechanisms on the fabric, which introduces the problem.

As explained in the slides, if a blade or VM creates a real or apparent loop, it activates the fabric’s protection mechanism, shutting down the port from which the loop originates. However, the failover mechanism of the virtualizer or hybrid switches moves the loop cause to a different interface, which is also shut down to protect the fabric. In a few minutes or seconds, the entire blade chassis is isolated along with its entire workload.

The problem is that, as network engineers, we tend to protect “the fabric” without realizing that the fabric actually extends to hybrid switches and virtual switches of the virtualizer. Complexity leads to segmenting the infrastructure into different themes: the fabric is the network team’s responsibility, while blades and virtualization belong to the computing team. According to this logic, the network team protects its perimeter from its perspective, which is incomplete.

The solution should involve implementing loop protection mechanisms at the fabric’s edge, considering it as a whole, to isolate the single VM (or server) causing the loop, rather than the entire blade chassis.

## Final Notes

Some final notes:

* The loop prevention mechanism should be handled by the access switch closest to the potential loop source (which can be VMs or servers).
* The loop prevention mechanism should include some sort of probe. Not all loops can be identified via BPDU guard.
* The described scenario can also occur due to virtualizers installed on rack servers, not just blades.
* To date, I have only observed human errors/bugs, but if I were to plan an effective DOS, I would consider it.
* We cannot prevent 100% of problems; we can only improve our ability to identify and respond to them quickly.

## References

* [Designing an Hybrid Data Center Infrastructure](https://www.adainese.it/files/slides/20130918-festival-ict-designing-an-hybrid-data-center-infrastructure.pdf "Designing an Hybrid Data Center Infrastructure")

## Andrea Dainese

For information, collaborations, proposals, requests for help, donations, use one of the following channels; email is preferred.

#### Past events

* - [SDN: Software Defined Now](/files/slides/20240305-cisco-aci-automation.pdf "View slides")
* - [Cybercrime](/files/slides/20231122-cybercrime.pdf "View slides")
* - [BGP attack scenarios](/files/slides/20220901-bgp-attack-scenarios.pdf "View slides")
* - [Approaching OT/ICS Security](/files/slides/20220317-approaching-ot-ics-security.pdf "View slides") (with [Festo Academy](https://www.festocte.it...