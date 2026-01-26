---
title: GitLab as the backbone of IaC
url: https://www.adainese.it/blog/2026/01/25/gitlab-as-the-backbone-of-iac/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-25
fetch_date: 2026-01-26T03:52:44.936113
---

# GitLab as the backbone of IaC

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# GitLab as the backbone of IaC

#### Latest posts

[![Post cover](/images/vendors/git.webp)](/blog/2026/01/25/gitlab-as-the-backbone-of-iac/)

[GitLab as the backbone of IaC](/blog/2026/01/25/gitlab-as-the-backbone-of-iac/)
January 25, 2026

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

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 178 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 142 posts

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

## GitLab as the backbone of IaC

Andrea Dainese

January 25, 2026

[Learning paths](/categories/learning-paths/ "All posts under Learning paths"),
[Automation](/categories/automation/ "All posts under Automation")

[![Post cover](/images/vendors/git.webp)](/images/vendors/git.webp)

GitLab has become the de facto standard for managing the software lifecycle within enterprises. It offers a huge number of features, adapts to almost any requirement, and for this reason it is a broad and complex piece of software. When talking about automation, we will use GitLab as the foundation for provisioning our infrastructure as code (IaC).

In the series of posts related to Cisco NDO and Cisco ACI, we saw how NaC (NetAsCode) allows us to easily configure our fabric in an IaC model. In those articles we also saw how an additional parser helps us implement input data validation and define configurations starting from simplified data structures designed specifically for our infrastructure.

The next step is to move the validation, build, and configuration process into a CI/CD pipeline, where:

* Continuous Integration (CI): change requests are validated before becoming part of the infrastructure configuration
* Continuous Deployment (CD): after approval by an authorized operator, configurations are pushed to production devices

The entire system is not limited to Cisco NDO / ACI environments, but can be extended to any ecosystem that can be configured programmatically, and in particular with Terraform. In this specific case, I implemented a pipeline that configures Cisco NDO, Cisco ACI, Cisco Intersight, and VMware vSphere environments.

## Installing GitLab

In my case, I installed
[GitLab](https://about.gitlab.com/)
Community Edition on an Ubuntu Linux 24.04 VM:

```
curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | bash
```

At the end of the installation, we can log in using the root user and the password contained in the file **/etc/gitlab/initial\_root\_password**.

Before using GitLab, we may need to set the URL in the /etc/gitlab/gitlab.rb file:

```
external_url 'http://172.24.9.183:8060/'
```

At this point we can validate and apply the configuration:

Continue reading
[the post on Patreon](https://www.patreon.com/posts/148295631)
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