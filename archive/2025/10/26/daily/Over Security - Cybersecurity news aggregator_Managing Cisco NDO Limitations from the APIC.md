---
title: Managing Cisco NDO Limitations from the APIC
url: https://www.adainese.it/blog/2025/10/26/managing-cisco-ndo-limitations-from-the-apic/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-26
fetch_date: 2025-10-27T16:50:59.747277
---

# Managing Cisco NDO Limitations from the APIC

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Managing Cisco NDO Limitations from the APIC

#### Latest posts

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/10/26/managing-cisco-ndo-limitations-from-the-apic/)

[Managing Cisco NDO Limitations from the APIC](/blog/2025/10/26/managing-cisco-ndo-limitations-from-the-apic/)
October 26, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/19/simplifying-the-data-structure/)

[Simplifying the Data Structure](/blog/2025/10/19/simplifying-the-data-structure/)
October 19, 2025

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/10/12/frameworks-for-projects-with-cisco-aci-and-ndo/)

[Frameworks for Projects with Cisco ACI and NDO](/blog/2025/10/12/frameworks-for-projects-with-cisco-aci-and-ndo/)
October 12, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)

[Creating an interface in Strata Cloud Manager](/blog/2025/10/05/creating-an-interface-in-strata-cloud-manager/)
October 05, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 164 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 128 posts

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

## Managing Cisco NDO Limitations from the APIC

Andrea Dainese

October 26, 2025

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/cisco.webp)](/images/vendors/cisco.webp)

We have observed that NDO currently has some important limitations that must be kept in mind:

* NDO frameworks have limitations, particularly NaC
* NDO itself has limitations
* certain configurations must necessarily be managed directly on the APIC

This consideration is far from trivial, and to fully understand it, we need to analyze how objects are created by NDO on the APIC.

## Objects Created by APIC vs. NDO

When I manually create an object on the APIC, the **annotation** field is empty. If I create it through Terraform or Ansible, the field is populated with the name of the framework used.

However, when the object is created by NDO, it results in:

```
annotation: orchestrator:msc-shadow:no
children -&gt; fvSiteAssociated -&gt; children -&gt; fvRemoteId
```

See files **BD-MANUAL-ON-APIC.json** and **BD-94-FROM-NDO.json** in the
[GitHub repository](https://github.com/dainok/courses/tree/master/Cisco/NDO/objects)
.

## Modifying an Object Created by NDO

Let’s now look at a practical example: we need to add the IGMP Snooping policy since it is not supported by NDO with NaC. The Bridge Domain has **unicastRoute** disabled.

We modify the Bridge Domain using Terraform/NaC. The final result shows the following differences:

Continue reading
[the post on Patreon](https://www.patreon.com/posts/139724658)
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

System Integration / Automation

![Training / Education / Cyber Range](/images/categories/writeup-125x100.webp)

Training / Education / Cyber Range

![Personal Security](/images/categories/personal-security-125x100.webp)

Personal Security

© Copyright **Andrea Dainese**. All Rights Reserved

Designed by [BootstrapMade](https://bootstrapmade.com/ "BootstrapMade")