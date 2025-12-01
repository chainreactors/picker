---
title: A practical Cisco NDO multi-site use case: additional configuration
url: https://www.adainese.it/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-30
fetch_date: 2025-12-01T03:35:58.985928
---

# A practical Cisco NDO multi-site use case: additional configuration

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# A practical Cisco NDO multi-site use case: additional configuration

#### Latest posts

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/11/30/a-practical-cisco-ndo-multi-site-use-case-config-deploy/)

[A practical Cisco NDO multi-site use case: config deploy](/blog/2025/11/30/a-practical-cisco-ndo-multi-site-use-case-config-deploy/)
November 30, 2025

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/11/23/a-practical-cisco-ndo-multi-site-use-case-building-the-parser/)

[A practical Cisco NDO multi-site use case: building the parser](/blog/2025/11/23/a-practical-cisco-ndo-multi-site-use-case-building-the-parser/)
November 23, 2025

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/11/22/eve-ng-sw-architecture-and-docker-support/)

[EVE-NG (SW architecture and docker support)](/blog/2025/11/22/eve-ng-sw-architecture-and-docker-support/)
November 22, 2025

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/11/16/a-practical-cisco-ndo-multi-site-use-case-data-validation/)

[A practical Cisco NDO multi-site use case: data validation](/blog/2025/11/16/a-practical-cisco-ndo-multi-site-use-case-data-validation/)
November 16, 2025

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/)

[A practical Cisco NDO multi-site use case: additional configuration](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/)
November 09, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 170 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 134 posts

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

## A practical Cisco NDO multi-site use case: additional configuration

Andrea Dainese

November 09, 2025

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/cisco.webp)](/images/vendors/cisco.webp)

In the previous article, we built the data structure that defines our infrastructure and most of its operational logic. However, there are some elements that require a different handling approach.

## Config

I usually work with two main files to store the required variables: **config.yml** and **secrets.yml**.

Specifically, the config.yaml file includes:

* The access references for APIC and NDO

[![Patreon Image](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/c262772601b60dba4f3aa3a5393956ff.webp)](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/c262772601b60dba4f3aa3a5393956ff.webp)

* Template names and deployment order

[![Patreon Image](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/0bd7a074f859013b81bbbc28ec874cb2.webp)](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/0bd7a074f859013b81bbbc28ec874cb2.webp)

* Parameters for optional filters

[![Patreon Image](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/564f23e964c2d5cf91992de6948a5974.webp)](/blog/2025/11/09/a-practical-cisco-ndo-multi-site-use-case-additional-configuration/564f23e964c2d5cf91992de6948a5974.webp)

Continue reading
[the post on Patreon](https://www.patreon.com/posts/140724207)
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