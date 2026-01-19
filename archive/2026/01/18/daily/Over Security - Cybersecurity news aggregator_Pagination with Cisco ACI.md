---
title: Pagination with Cisco ACI
url: https://www.adainese.it/blog/2026/01/18/pagination-with-cisco-aci/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-18
fetch_date: 2026-01-19T03:44:55.971992
---

# Pagination with Cisco ACI

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Pagination with Cisco ACI

#### Latest posts

[![Post cover](/images/vendors/cisco.webp)](/blog/2026/01/18/pagination-with-cisco-aci/)

[Pagination with Cisco ACI](/blog/2026/01/18/pagination-with-cisco-aci/)
January 18, 2026

[![Post cover](/images/vendors/cisco.webp)](/blog/2026/01/11/filtering-cisco-api-output/)

[Filtering Cisco API Output](/blog/2026/01/11/filtering-cisco-api-output/)
January 11, 2026

[![Post cover](/images/vendors/cisco.webp)](/blog/2026/01/04/finding-cisco-aci-classes-with-visore/)

[Finding Cisco ACI Classes with Visore](/blog/2026/01/04/finding-cisco-aci-classes-with-visore/)
January 04, 2026

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/12/28/cisco-aci-classes/)

[Cisco ACI Classes](/blog/2025/12/28/cisco-aci-classes/)
December 28, 2025

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/12/21/first-approach-to-cisco-aci-apis/)

[First Approach to Cisco ACI APIs](/blog/2025/12/21/first-approach-to-cisco-aci-apis/)
December 21, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 177 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 141 posts

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

## Pagination with Cisco ACI

Andrea Dainese

January 18, 2026

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/cisco.webp)](/images/vendors/cisco.webp)

When dealing with a large number of records, pagination becomes necessary. By default, Cisco ACI pagination allows you to retrieve up to **500 objects**. A maximum value is not explicitly
[documented](https://www.cisco.com/c/en/us/td/docs/dcn/aci/apic/all/apic-rest-api-configuration-guide/cisco-apic-rest-api-configuration-guide-42x-and-later/m_using_the_rest_api.html#concept_ACBD6DDCEDE64FCF9DAE8134123C8F3C)
; however, it is not recommended to go beyond this limit in order to avoid overloading the APIC.

Pagination can be controlled using the following parameters:

* **page-size**, which defines the size of each page
* **page**, which defines which page to retrieve, starting from 0

The response includes the **totalCount** attribute, which indicates the total number of objects available for the specific query.

Continue reading
[the post on Patreon](https://www.patreon.com/posts/145883187)
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