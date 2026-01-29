---
title: From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible
url: https://www.sei.cmu.edu/blog/from-concept-to-practice-how-ssvc-has-evolved-to-make-adoption-possible/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-01-28
fetch_date: 2026-01-29T04:06:02.116016
---

# From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Our Work

Publications

News and Events

Education and Outreach

Careers

Search

Mobile Menu

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Metcalf, R., Householder, A., and Sarvepalli, V., 2026: From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed January 28, 2026, https://doi.org/10.58012/mqp8-cx09.

Copy

APA Citation

Metcalf, R., Householder, A., & Sarvepalli, V. (2026, January 28). From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible. Retrieved January 28, 2026, from https://doi.org/10.58012/mqp8-cx09.

Copy

Chicago Citation

Metcalf, Renae, Allen Householder, and Vijay Sarvepalli. "From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, January 28, 2026. https://doi.org/10.58012/mqp8-cx09.

Copy

IEEE Citation

R. Metcalf, A. Householder, and V. Sarvepalli, "From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 28-Jan-2026 [Online]. Available: https://doi.org/10.58012/mqp8-cx09. [Accessed: 28-Jan-2026].

Copy

BibTeX Code

@misc{metcalf\_2026,
author={Metcalf, Renae and Householder, Allen and Sarvepalli, Vijay},
title={From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible},
month={{Jan},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/mqp8-cx09},
note={Accessed: 2026-Jan-28}
}

Copy

# From Concept to Practice: How SSVC Has Evolved to Make Adoption Possible

![Headshot of Renae Metcalf.](/media/images/kmetcalf.max-180x180.format-webp.webp)
![Headshot of Allen Householder.](/media/images/thumb_big_a-householder_blog_au.max-180x180.format-webp.webp)

###### [Renae Metcalf](/authors/renae-metcalf), [Allen D. Householder](/authors/allen-householder), and [Vijay S. Sarvepalli](/authors/vijay-sarvepalli)

###### January 28, 2026

##### PUBLISHED IN

[Security Vulnerabilities](/blog/topics/security-vulnerabilities/)

##### CITE

<https://doi.org/10.58012/mqp8-cx09>

Get Citation

##### SHARE

It’s Patch Tuesday.

Your software scanners light up with almost 70 percent more vulnerabilities than last month, and by Friday you’re expected to explain, clearly and defensibly, which ones matter, which ones wait, and which ones could put the organization at real risk if ignored. Your teams are already stretched, new AI-enabled software is landing faster than it can be inventoried, and every dashboard insists its prioritization should come first.

Even if you manage to get through this week, the question remains: how do you make vulnerability prioritization sustainable when volume keeps growing, software keeps changing, and risk tolerance is not the same for every system considering the diverse stakeholders.

This is not just hypothetical, in October 2025, Microsoft released fixes for 167 vulnerabilities on a single Patch Tuesday. As Tenable noted in a recent [blog](https://www.tenable.com/blog/microsoft-patch-tuesday-2025-year-in-review) post

1. Microsoft alone patched more than 1,100 vulnerabilities for the second consecutive year, nearing 2020’s record.
2. The year 2025 saw two record-breaking monthly Patch Tuesdays (January and October)
3. The "Important" vulnerabilities (over 90 percent) remained the largest category, with "Critical" patches also significant, and a notable rise in actively exploited zero-days (41 in 2025).
4. Elevation of Privilege (EoP) and Remote Code Execution (RCE) flaws were dominant.
5. The increasing scope of Microsoft’s portfolio, including AI and cloud products, contributes to higher patch counts.

This is the problem the [Stakeholder-Specific Vulnerability Categorization (SSVC) framework](https://certcc.github.io/SSVC/) was created to address.

Since its initial publication in 2019, SSVC has evolved from a set of concepts and questionnaires into a practical decision framework with defined models that organizations can adopt, implement, and operationalize. As adoption has increased, barriers to entry have steadily decreased. New tooling, community-driven interfaces, and APIs, combined with CISA’s [Vulnrichment](https://www.cisa.gov/news-events/news/unlocking-vulnrichment-enriching-cve-data) efforts and improved data exchange formats, are making SSVC easier to integrate, automate, and scale.

As a result, more organizations, including smaller teams without dedicated risk engineering staff, can now apply SSVC using data already flowing through their vulnerability management processes. This post traces the milestones that made this shift possible and invites the community to participate, contribute, and benefit from the continued maturation of SSVC.

## Transitioning to SSVC

Introducing a new framework for prioritizing vulnerability response presents two problems: stakeholders must be able to access framework data, and they must be able to consume it in support of decisions. In 2019, they could do neither. For starters, stakeholders had to generate their own data by reading and analyzing vulnerability reports. Moreover, the vulnerability ecosystem was geared to support the more popular Common Vulnerability Scoring System (CVSS) scoring and metric values, so adapting to SSVC was an uphill battle that few were inclined to undertake. Transitioning from CVSS V3.1 to SSVC is a greater challenge than translation—it is more analogous to converting from driving a car with an automatic transmission to a motorcycle with a manual transmission, a challenge of spatial awareness and how you interact with your environment. By mid-2024, [deployers](https://certcc.github.io/CERT-Guide-to-CVD/topics/roles/deployer/) had some global data, but no way to integrate it. Now, at the start of 2026, deployers have the global data and will soon be able to integrate the data.

SSVC is now more broadly accessible, and it continues to gain adoption, particularly by larger, well-resourced organizations. For example, CISA uses the SSVC framework to prioritize vulnerability response and protect federal networks from active cyber threats.

## Increasing Availability of Vulnerability Data Content

SSVC adoption has hinged not just on motivated individuals and organizations integrating it into their own decision-making apparatus, it is also facilitated by the increasing availability of consumable data from trusted and reliable sources:

* CISA KEV and Vulnrichment programs provide SSVC-ready information.
* CVSS V4 and SSVC share semantic compatibility in some attributes by design.
* Both CVE and CSAF data standards are or will soon be incorporating schemas to allow the inclusion of SSVC data.

### KEV (since November 2021)

A key question in SSVC is the state of *Exploitation* for the vulnerability in question. The [Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), established by CISA in November 2021, contains a “[subset of CVEs which have been used to compromise systems in the real world.](https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities)” KEV records are always *Exploitation: Active*, per SSVC, and this data can accordingly be represented in decision models. *Exploitation* is the first decision point in both Supplier and Deployer decision ta...