---
title: Advanced Git commands
url: https://www.adainese.it/blog/2024/09/19/advanced-git-commands/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:29:18.956187
---

# Advanced Git commands

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Advanced Git commands

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

## Advanced Git commands

Andrea Dainese

September 19, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/git.webp)](/images/vendors/git.webp)

In the last two posts, we covered most of the essential Git features. Now, let’s dive into some additional functionalities that might come i

In the last two posts, we covered most of the essential Git features. Now, let’s dive into some additional functionalities that might come in handy.

## .gitignore

The **.gitignore** file is used to specify which files or directories should never be included in your Git repository. This file is tailored to each repository and typically excludes:

* Cache files
* Compiled files
* Temporary files
* Password files

You can either start with
[GitHub’s suggested templates](https://github.com/github/gitignore)
 or create your own using the
[correct format](https://git-scm.com/docs/gitignore)
.

## Stashing your work

Sometimes you need to put aside your current work to focus on something more urgent. If you’ve made changes but aren’t ready to commit, switching branches won’t work because Git doesn’t know how to handle uncommitted changes.

[![Patreon Image](/blog/2024/09/19/advanced-git-commands/212bbcae8876c1b2329db282fc19072e.webp)](/blog/2024/09/19/advanced-git-commands/212bbcae8876c1b2329db282fc19072e.webp)

This is where **stash** comes in. It saves all your changes, including those staged for commit, and allows you to retrieve them later:

[![Patreon Image](/blog/2024/09/19/advanced-git-commands/3aefc5d612be8792c2722da91a7e563e.webp)](/blog/2024/09/19/advanced-git-commands/3aefc5d612be8792c2722da91a7e563e.webp)

Now you can safely switch branches. To retrieve the stashed changes later:

[![Patreon Image](/blog/2024/09/19/advanced-git-commands/a33e755e8636d2534dbe34d4914a1dcb.webp)](/blog/2024/09/19/advanced-git-commands/a33e755e8636d2534dbe34d4914a1dcb.webp)

You can also list all stashed changes with:

[![Patreon Image](/blog/2024/09/19/advanced-git-commands/d4e807d21314ab41cdbe1866685d753b.webp)](/blog/2024/09/19/advanced-git-commands/d4e807d21314ab41cdbe1866685d753b.webp)

## Deleting Remote Branches

While local branches can be deleted with the **branch** command, deleting a remote branch involves a **push**:

[![Patreon Image](/blog/2024/09/19/advanced-git-commands/e2b6f8ecb821fbdf2554e199310d3944.webp)](/blog/2024/09/19/advanced-git-commands/e2b6f8ecb821fbdf2554e199310d3944.webp)

## Rebase

**Rebase** lets you integrate changes in a way similar to **merge**, but it reapplies a series of commits starting from a different base, effectively rewriting the history of the repository. Be cautious, this can cause inconsistencies, especially in public repos where multiple people collaborate.

For example, in a repo with **main** and branches **fix3** and **fix4** waiting to be merged:

[![Patreon Image](/blog/2024/09/19/advanced-git-commands/4d5df19cbad8c8b35cd945d1d5a8a080.webp)](/blog/2024/09/19/advanced-git-commands/4d5df19cbad8c8b35cd945d1d5a8a080.webp)

If we merge the **fix3** branch, we notice that the commit IDs have been preserved:

Continue reading
[the post on Patreon](https://www.patreon.com/posts/advanced-git-112035451)
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

Open Sour...