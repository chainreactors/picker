---
title: A practical Cisco NDO multi-site use case: modelling
url: https://www.adainese.it/blog/2025/11/02/a-practical-cisco-ndo-multi-site-use-case-modelling/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-03
fetch_date: 2025-11-04T03:11:26.874468
---

# A practical Cisco NDO multi-site use case: modelling

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# A practical Cisco NDO multi-site use case: modelling

#### Latest posts

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/11/02/a-practical-cisco-ndo-multi-site-use-case-modelling/)

[A practical Cisco NDO multi-site use case: modelling](/blog/2025/11/02/a-practical-cisco-ndo-multi-site-use-case-modelling/)
November 02, 2025

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

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 165 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 129 posts

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

## A practical Cisco NDO multi-site use case: modelling

Andrea Dainese

November 02, 2025

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/cisco.webp)](/images/vendors/cisco.webp)

The example presented here covers the deployment of a multi-site fabric managed through NDO. The current setup, based on a legacy environment, must be migrated to a newly implemented multi-site environment. Although this is not a greenfield project, we can treat it as such since the entire configuration will be generated from scratch.

The automation project requirements are to:

* Distribute the production workload across all sites
* Ensure fast deployment
* Provide simple tools for the operations team

In the current infrastructure, most of the L3 routing is handled by firewalls. Some basic L3 routing scenarios within the fabric may be implemented in the future.

Unfortunately, there is no single “correct” approach that guarantees results. Furthermore, what works today may require changes tomorrow, as NDO, the Terraform NDO provider, and NaC are constantly evolving.

In this case, I chose to:

* Focus on the production tenant, managing fabric setup and inter-site communication manually
* Prefer tools in the order: NaC, Terraform, Python
* Store automation code and data structures in Git
* Manage configuration on NDO, configuring only unsupported features directly on APIC
* Use NaC data structures for objects that rarely require modification
* Use a simple CSV-based structure for operations requiring frequent updates (networks, L3Outs)
* Create a parser to convert CSV files into NaC and Terraform data structures

## NDO

All logical configuration, i.e., related to templates, is managed by NDO, with a few exceptions described later. The physical configuration, however, is managed directly on the APIC for two reasons:

* There is currently no complete NaC or Terraform module for managing the physical layer.
* The Terraform provider for NDO has poor performance, so it’s more efficient to perform non-critical tasks directly on the APIC.

NDO therefore contains:

* The production tenant, applied across all sites
* A schema template including six tenant templates:

  + One template per site containing BDs, subnets, Applications, and EPGs (deploy order 2)
  + One shared template for all sites containing BDs, Applications, and EPGs (deploy order 2)
  + One shared template for all sites containing VRFs (deploy order 1)
  + One shared template for all sites containing Contracts (deploy order 1)
  + One shared template for all sites containing External EPGs (deploy order 3)

Continue reading
[the post on Patreon](https://www.patreon.com/posts/140490898)
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

Designed by [BootstrapMade](https://bootstrapmade.com...