---
title: Ansible Playbooks and variables
url: https://www.adainese.it/blog/2024/08/15/ansible-playbooks-and-variables/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:29:11.813931
---

# Ansible Playbooks and variables

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Ansible Playbooks and variables

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

## Ansible Playbooks and variables

Andrea Dainese

August 15, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/ansible.webp)](/images/vendors/ansible.webp)

A playbook is a YAML file that sequentially outlines the operations to be performed on devices or groups of devices. Each playbook is composed of one or more **plays**, which can include **pre\_tasks**, **tasks**, and **post\_tasks**.

[![Patreon Image](/blog/2024/08/15/ansible-playbooks-and-variables/4ac0fb0b4db7b265fc275e6c51e061f3.webp)](/blog/2024/08/15/ansible-playbooks-and-variables/4ac0fb0b4db7b265fc275e6c51e061f3.webp)

When planning and writing playbooks, variables play a crucial role. These variables can be defined at different levels, such as configuration, playbook, inventory, environment, files, or **facts**. It’s helpful to have a method for printing the value of all defined variables.

Let’s start by opening the **Cisco Legacy Core-Access topology** lab and ensuring all devices are active and reachable.

## Printing All Variables

As we know, a playbook is a YAML file containing a list of **plays**. Each **play** defines the operations to be performed and where they should be executed:

[![Patreon Image](/blog/2024/08/15/ansible-playbooks-and-variables/72b236fee54d05709507c6c9713bf400.webp)](/blog/2024/08/15/ansible-playbooks-and-variables/72b236fee54d05709507c6c9713bf400.webp)

The example above defines a **play** with a general list of **pre\_tasks**, **tasks**, and **post\_tasks**. This **play** runs on all inventory objects (**all**) and collects **facts** before executing any tasks. Although gathering **facts** can slow down the **play**, it’s essential for our purpose.

The first line, known as the “shebang,” allows the playbook file to be executed directly without specifying the **ansible-playbook** interpreter manually. As the name suggests, **pre\_tasks** and **post\_tasks** group tasks that need to be executed before any other tasks or just before finishing the **play**, respectively. In this example, we’ll focus only on the **tasks**.

The playbook’s goal is defined by the **hosts** key, which can select all hosts in the inventory (**all**), specific groups, or individual hosts. Here are some examples:

* **all**: selects all hosts in the inventory;
* **r1.example.com**: selects only R1;
* **routers,switches**: selects hosts in the **routers** or **switches** groups;
* **routers,!switches**: selects hosts in the **routers** group but not in the **switches** group.

Now, let’s write a playbook to print all environment variables. The variables we want to print are grouped into:

* Module variables (**vars**)
* Environment variables (**environment**)
* Group names variables (**group\_names**)
* Groups variables (**groups**)
* Host variables (**hostvars**)

We’ll define five tasks to print these variables:

[![Patreon Image](/blog/2024/08/15/ansible-playbooks-and-variables/1c93c95dafbffe18aa9c553faaaa0a25.webp)](/blog/2024/08/15/ansible-playbooks-and-variables/1c93c95dafbffe18aa9c553faaaa0a25.webp)

Each task uses the **ansible.builtin.debug** module to define the **msg** variable, which is set to the contents of **vars**, **environment**, **group\_names**, **groups**, and **hostvars**.

Continue reading
[the post on Patreon](https://www.patreon.com/posts/ansible-and-109844619)
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

Inciden...