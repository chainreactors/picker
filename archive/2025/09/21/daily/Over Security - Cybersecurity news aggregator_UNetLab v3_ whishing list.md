---
title: UNetLab v3: whishing list
url: https://www.adainese.it/blog/2024/07/23/unetlab-v3-whishing-list/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:28:57.690963
---

# UNetLab v3: whishing list

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# UNetLab v3: whishing list

#### Latest posts

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

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

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

## UNetLab v3: whishing list

Andrea Dainese

July 23, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/categories/learning-paths.webp)](/images/categories/learning-paths.webp)

The idea behind UNetLab v2 was partly good, but some choices complicated the implementation and negatively impacted system performance. Specifically, managing UNetLab’s network in user space would have caused serious problems, even though it would have made horizontal scalability easier.

Moreover, I had a significant doubt: does it make sense to implement a virtualization system today when several are maintained by companies far better than I could manage? Initially, I considered
[ESXi](https://www.vmware.com/products/esxi-and-esx.html)
, but after the
[Broadcom acquisition](https://investors.broadcom.com/news-releases/news-release-details/broadcom-completes-acquisition-vmware)
, I leaned towards
[Proxmox](https://www.proxmox.com/)
. While ESXi would have required abandoning physical link simulation, Proxmox allows using the same strategy I used with UNetLab.

Using an existing hypervisor significantly simplifies development at the cost of a substantial sacrifice: unsupported systems like IOL and Dynamips would no longer be supported. While this isn’t a big issue for Dynamips, IOL has always been my preferred system for creating lightweight labs.

## UNetLab v3 Wishlist

I should divide the list into functional and non-functional requirements, but for now, let’s compile a sort of wishlist together.

In my mind, a hypothetical UNetLab v3 wishlist includes:

* Free, open-source, community-driven
* Ability to easily share labs, template repositories, playbooks
* Support for Ansible, Nornir, NAPALM, Netmiko playbooks
* Unified but focus on network and security labs
* Multi-user, multi-tenant, multi-role (e.g., student/teacher)
* Easy scalability
* API-first approach, with CLI and web interface

Lab Features:

* Each lab is isolated by default.
* Labs can be interconnected.
* Labs can be shared between users.
* A management network is deployed per lab.
* Management network is hidden in topology.
* Management network is reachable by all nodes.
* A DHCP server is deployed per lab.
* An Internet gateway can be deployed per lab.
* A fake internet gateway can be deployed.
* Labs are described by a human-readable YAML file.
* Labs could contain an inventory compatible with Ansible.
* Imported labs should allow selecting alternative templates if the existing ones are not available.
* Labs could be signed by users.
* Live changes (jitter, delay, interface up/down) should immediately reflect in the running lab.
* Marketplace: A place where users and teachers can share labs and learning paths.
* Automation: All relevant nodes within a lab should be reachable by automation software by default.
* Packet capture: Users should be able to capture packets from any specific interface.
* Scale-out: Labs could be run on multiple computing nodes.

Continue reading
[the post on Patreon](https://www.patreon.com/posts/unetlab-v3-list-108650525)
.

## Andrea Dainese

For information, collaborations, proposals, requests for help, donations, use one of the following channels; email is preferred.

#### Past events

* - [SDN: Software Defined Now](/files/slides/20240305-cisco-aci-automation.pdf "View slides")
* - [Cybercrime](/files/slides/20231122-cybercrime.pdf "View slides")
* - [BGP attack scenarios](/files/slides/20220901-bgp-attack-scenarios.pdf "View slides")
* - [Approaching OT/ICS Security](/files/slides/20220317-approaching-ot-ics-security.pdf "View slides") (with [Festo Academy](https://www.festocte.it/eventi/industry_4_0/17-03-2022/webinar_la_cybersecurity_nelle_reti_di_fabbrica_P/))
* - [Cyber Range: Analyzing a Cyber Attack](/files/slides/20200922-cyberrange.pdf "View slides")
* - [Securing OT/ICS plants](/files/slides/20200623-clubitfvg-securing-ot-ics-plants.pdf "View slides")
* - [Automation for Cisco NetOps](/files/slides/20190226-automation-for-cisco-netops.pdf "View slides")
* - [SDN, Complexity and TCO](/files/slides/20181107-ciscon-sdn-complexity-and-tco-looking-for-an-easy-way.pdf "View slides")
* - [Protection and visibility for enterprise networks](/files/slides/20181003-nts-protection-and-visibility-for-enterprise-networks.pdf "View slides")
* - [Why WAN AccelerAtors (still) matter?](/files/slides/20141106-festival-ict-why-wan-accelerators-still-matter.pdf "View slides")
* - [Designing an Hybrid Data Center Infrastructure](/files/slides/20130918-festival-ict-designing-an-hybrid-data-center-infrastructure.pdf "View slides")

#### Competencies

![Incident Response](/images/categories/security-125x100.webp)

Incident Response

![Advisor](/images/categories/ciso-125x100.webp)

Advisor

![Open Source Intelligence (OSINT)](/images/categories/osint-125x100.webp)

Open Source Intelligence (OSINT)

![System Integration / Automation](/images/categories/infrastructure-125x100.webp)

System Integrati...