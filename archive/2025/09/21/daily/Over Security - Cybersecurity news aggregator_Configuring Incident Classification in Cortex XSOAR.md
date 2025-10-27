---
title: Configuring Incident Classification in Cortex XSOAR
url: https://www.adainese.it/blog/2024/08/19/configuring-incident-classification-in-cortex-xsoar/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:29:12.808688
---

# Configuring Incident Classification in Cortex XSOAR

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Configuring Incident Classification in Cortex XSOAR

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

## Configuring Incident Classification in Cortex XSOAR

Andrea Dainese

August 19, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/categories/learning-paths.webp)](/images/categories/learning-paths.webp)

In this post, we’ll set up the
[classification](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Classification-and-Mapping)
 feature, which allows us to transform events into specific incident types. This guide expands on the content covered in the videos
[XSOAR Engineer Training - Part 2: Incident Types & Fields](https://www.youtube.com/watch?v=o92rG4FPc-k&list=PLD6FJ8WNiIqUVEA2e5LZhmqNnwFcFhDTZ&index=2)
 and
[XSOAR Engineer Training - Part 3: Classification and Mapping](https://www.youtube.com/watch?v=TW-q2wmchZk&list=PLD6FJ8WNiIqUVEA2e5LZhmqNnwFcFhDTZ&index=3)
.

## Set Up Incident Classifier

Navigate to **Settings** -> **Objects Setup** -> **Classification & Mapping** -> **New Incident Classifier**. At the top, select the **JSONSampleIncidentGenerator\_url\_events** instance we created in the previous post. This allows us to work with sample events.

[![Patreon Image](/blog/2024/08/19/configuring-incident-classification-in-cortex-xsoar/5e61ebd449ebd5e9081ae2ce6f0caa49.webp)](/blog/2024/08/19/configuring-incident-classification-in-cortex-xsoar/5e61ebd449ebd5e9081ae2ce6f0caa49.webp)

On the right, you’ll see a list of existing incident types in XSOAR:

[![Patreon Image](/blog/2024/08/19/configuring-incident-classification-in-cortex-xsoar/bcf12b7ef44a0b89f802857295b0fcf1.webp)](/blog/2024/08/19/configuring-incident-classification-in-cortex-xsoar/bcf12b7ef44a0b89f802857295b0fcf1.webp)

There’s already a **PAN-OS URL Log Incident** type, but since our events don’t originate from PAN-OS, we’ll create a new incident type specific to the data we’re analyzing.

Go to **Settings** -> **Objects Setup** -> **Incidents** -> **Types** and select **PAN-OS URL Log Incident**. Use the **Detach** button to modify the object and explore its structure. After making your changes, click **Reattach** to restore the original state.

## Create a New Incident Type

Create a new incident type with the following settings:

* Name: URL Alerts
* Run playbook automatically: Set (best practice)
* Post process using: Unset (script executed before closing the incident)

Continue reading
[the post on Patreon](https://www.patreon.com/posts/configuring-in-110023409)
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