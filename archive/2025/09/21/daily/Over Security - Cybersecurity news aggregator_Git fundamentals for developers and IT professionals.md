---
title: Git fundamentals for developers and IT professionals
url: https://www.adainese.it/blog/2024/09/06/git-fundamentals-for-developers-and-it-professionals/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-21
fetch_date: 2025-10-02T20:29:16.334491
---

# Git fundamentals for developers and IT professionals

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Git fundamentals for developers and IT professionals

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

## Git fundamentals for developers and IT professionals

Andrea Dainese

September 06, 2024

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/git.webp)](/images/vendors/git.webp)

Git is a distributed version control software created by Linus Torvalds to manage the
[Linux kernel source code](https://git.kernel.org/)
. Personally, I use Git, along with
[GitHub](https://github.com/)
, to manage:

* [The source code for the software I develop](https://github.com/dainok/)
  ;
* The source code and compiled files for
  [my website](https://www.adainese.it/)
  ;
* The source code for
  [the books I’ve written](https://www.adainese.it/categories/books/)
  ;
* My notes, written with
  [Obsidian](https://obsidian.md/)
  .

Git allows me to track every change and, overall, the evolution of a repository. It’s well-suited to handle any file that can be represented as text. This is why, for the past few years, I’ve been using
[Markdown](https://en.wikipedia.org/wiki/Markdown)
 to write text and have embraced the Documentation as Code approach.

Git is a vital tool that should be mastered by anyone working in IT, but it’s essential for developers.

Before getting started, here are some important considerations:

* **Storage:** Git saves every version of every file. For text files, we know that changes can be represented by just the lines that have been modified, but for binary files, a revision often means saving a full copy of the file. So, keep in mind that a repository may grow in size, and it might require maintenance to reduce the space used, which will improve its performance.
* **Clean Structure:** Especially when working in a team, it’s important to adopt a common workflow. The repository should only contain the files necessary to recreate the environment and avoid cache, compiled, or temporary files.
* **Security:** Since Git saves permanent copies of all files added to the repository, be cautious about including files with sensitive information like passwords. While you can remove references to such files locally, this process isn’t fully effective on third-party platforms like GitHub.

In this series of posts, we’ll explore the fundamentals of Git. For those interested in learning more, I recommend the following resources:

* [Pro Git Book](https://git-scm.com/book/en/v2)
   by Scott Chacon and Ben Straub
* [GIT for Beginners](https://people.irisa.fr/Anthony.Baire/git/git-for-beginners-handout.pdf)
   by Anthony Baire

## Working Locally

Let’s start working with Git by creating a local repository. Any empty or non-empty directory can be initialized as a Git repository:

[![Patreon Image](/blog/2024/09/06/git-fundamentals-for-developers-and-it-professionals/7f069244cc257d7dde86a8256070a1f2.webp)](/blog/2024/09/06/git-fundamentals-for-developers-and-it-professionals/7f069244cc257d7dde86a8256070a1f2.webp)

The commands above create a **.git** directory, which contains all the information for the repository. As long as this directory remains intact, the contents of the repository are safe.

Continue reading
[the post on Patreon](https://www.patreon.com/posts/git-fundamentals-111155980)
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

Open Source Inte...