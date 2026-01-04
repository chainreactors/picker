---
title: First Approach to Cisco ACI APIs
url: https://www.adainese.it/blog/2025/12/21/first-approach-to-cisco-aci-apis/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-03
fetch_date: 2026-01-04T03:37:37.320182
---

# First Approach to Cisco ACI APIs

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# First Approach to Cisco ACI APIs

#### Latest posts

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/12/28/cisco-aci-classes/)

[Cisco ACI Classes](/blog/2025/12/28/cisco-aci-classes/)
December 28, 2025

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/12/21/first-approach-to-cisco-aci-apis/)

[First Approach to Cisco ACI APIs](/blog/2025/12/21/first-approach-to-cisco-aci-apis/)
December 21, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/12/14/automating-user-management-with-n8n-and-ai-agents/)

[Automating user management with n8n and AI Agents](/blog/2025/12/14/automating-user-management-with-n8n-and-ai-agents/)
December 14, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/12/07/an-introduction-to-workflow-and-process-automation-with-n8n-and-camunda/)

[An introduction to workflow and process automation with n8n and Camunda](/blog/2025/12/07/an-introduction-to-workflow-and-process-automation-with-n8n-and-camunda/)
December 07, 2025

[![Post cover](/images/vendors/cisco.webp)](/blog/2025/11/30/a-practical-cisco-ndo-multi-site-use-case-config-deploy/)

[A practical Cisco NDO multi-site use case: config deploy](/blog/2025/11/30/a-practical-cisco-ndo-multi-site-use-case-config-deploy/)
November 30, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 174 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 138 posts

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

## First Approach to Cisco ACI APIs

Andrea Dainese

December 21, 2025

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/cisco.webp)](/images/vendors/cisco.webp)

Let’s now see how to write our first automation for Cisco ACI. As we mentioned, Cisco ACI is designed to be *API-first*, meaning that every operation is performed through APIs.

Cisco made an interesting design choice: to address the challenge of documenting APIs in an effective and long-lasting way, they built a web interface that itself uses only APIs. In other words, by observing what happens while we use the web interface, we can identify the APIs being called and the required parameters. In addition, Cisco added a feature to the web interface: **API Inspector**, which allows us to observe the APIs in use.

We can therefore say that Cisco ACI APIs are self-documenting. Cisco also provides an official
[APIC REST API User Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/1-x/api/rest/b_APIC_RESTful_API_User_Guide/overview_of_the.html)
. This guide will be very useful later on, but to get started, API Inspector is the fastest way to achieve results.

Let’s go through the process step by step.

## API Inspector

First, connect to the APIC and go to **Tools → Show API Inspector**:

[![Patreon Image](/blog/2025/12/21/first-approach-to-cisco-aci-apis/150caea846521025bdd4bd065f6e1eda.webp)](/blog/2025/12/21/first-approach-to-cisco-aci-apis/150caea846521025bdd4bd065f6e1eda.webp)

A new browser window will open, containing the API Inspector. Navigate through the web interface and add a tenant. If we look at the API Inspector window, we’ll see that it contains all the API calls performed during our actions:

[![Patreon Image](/blog/2025/12/21/first-approach-to-cisco-aci-apis/0a6e2f14e546d1aaa42dc894b5329478.webp)](/blog/2025/12/21/first-approach-to-cisco-aci-apis/0a6e2f14e546d1aaa42dc894b5329478.webp)

For example, if we select our tenant in the web interface, we will find a POST call and its payload:

```
method: POST url: https://172.25.82.1/api/node/mo/uni/tn-AD-TEST.json payload: { "fvTenant": { "attributes": { "dn": "uni/tn-AD-TEST", "name": "AD-TEST", "rn": "tn-AD-TEST", "status": "created" }, "children": [] } }
```

Continue reading
[the post on Patreon](https://www.patreon.com/posts/145750820)
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