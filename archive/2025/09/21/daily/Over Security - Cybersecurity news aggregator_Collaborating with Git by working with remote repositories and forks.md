---
title: Collaborating with Git by working with remote repositories and forks
url: https://www.adainese.it/blog/2024/09/10/collaborating-with-git-by-working-with-remote-repositories-and-forks/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:29:16.967352
---

# Collaborating with Git by working with remote repositories and forks

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Collaborating with Git by working with remote repositories and forks

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

## Collaborating with Git by working with remote repositories and forks

Andrea Dainese

September 10, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/git.webp)](/images/vendors/git.webp)

In the previous post, we covered the basics of using Git locally. Now, let’s dive into real-world scenarios and learn how to collaborate using Git with remote repositories.

When working with remote repositories, we gain access to some new functionalities:

* **clone**: allows us to create a local copy of a remote repository.
* **pull**: lets us update our local branch with changes from the remote.
* **push**: enables us to update the remote branch with our local changes.

Typically, **pull** and **push** actions are not allowed directly on the main branch. This forces us to always create a new branch for our changes, which we’ll then merge into the main branch.

Moreover, we often don’t have permission to create branches on repositories we don’t own. This requires us to create a **fork**, which is a copy of the entire repository we want to work on. We can then create a branch on this new repository, make our changes, and request (via a Pull Request or PR) that the original repository merges our changes.

But let’s take it step by step.

## Origin

First, let’s clone a repository of our choice:

Continue reading
[the post on Patreon](https://www.patreon.com/posts/collaborating-by-111643903)
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