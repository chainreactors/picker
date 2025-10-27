---
title: Ansible statements
url: https://www.adainese.it/blog/2024/09/16/ansible-statements/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:29:18.388594
---

# Ansible statements

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Ansible statements

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

## Ansible statements

Andrea Dainese

September 16, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/ansible.webp)](/images/vendors/ansible.webp)

If you’ve got some experience with programming languages, you might find Ansible’s constructs a bit clunky. But no worries, let’s break them

If you’ve got some experience with programming languages, you might find Ansible’s constructs a bit clunky. But no worries, let’s break them down with some practical examples to make things clearer.

## Conditionals (if, then, else)

In Ansible, the **if-then-else** construct is simplified to a single word: **when**.

[![Patreon Image](/blog/2024/09/16/ansible-statements/222f50ae73824db1a76630ebaa9c6747.webp)](/blog/2024/09/16/ansible-statements/222f50ae73824db1a76630ebaa9c6747.webp)

Unlike traditional languages, there’s no direct **else** or **elif**. You’ll handle them all with separate **when** statements and the right expressions.

If you’ve got a bunch of conditions that all need to be true at the same time (logical **AND**), you can list them out:

[![Patreon Image](/blog/2024/09/16/ansible-statements/dff8d365b59559395a290aacb5b5a0a5.webp)](/blog/2024/09/16/ansible-statements/dff8d365b59559395a290aacb5b5a0a5.webp)

Each variable in Ansible can be one of the following types:

* List
* Dictionary
* Boolean (True/true/yes/on or False/false/no/off)
* Integer
* Float
* String (if it’s wrapped in quotes or doesn’t fit the above types)

Ansible heavily relies on
[Jinja](https://jinja.palletsprojects.com/)
, which adds a bit more complexity to the mix. Any variable created using Jinja is treated as a string, and you’ll often need to convert it before use. But sometimes Ansible takes care of this for you, like when it automatically converts a string containing JSON into a list or dictionary when used in a loop.

Here’s a quick breakdown to help you navigate this:

* Variables can be either **defined** or **undefined**.
* A defined variable might be empty (**None**) or have some data.
* The variable’s type depends on the data it holds (Ansible uses weak typing).
* Ansible often creates strings using Jinja, which may require conversion.
* Ansible will automatically convert strings into lists or dictionaries when needed.
* Before performing mathematical operations, it’s a good habit to explicitly convert variables using Jinja filters like **| int** or **| float**.

Continue reading
[the post on Patreon](https://www.patreon.com/posts/ansible-111918170)
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