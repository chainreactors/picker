---
title: Managing Architectural Risk During Agile Development
url: https://www.sei.cmu.edu/blog/managing-architectural-risk-during-agile-development/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-05-22
fetch_date: 2026-05-23T05:42:50.211825
---

# Managing Architectural Risk During Agile Development

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. Managing Architectural Risk During Agile Development

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Rosso-Llopart, M., 2026: Managing Architectural Risk During Agile Development. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed May 22, 2026, https://doi.org/10.58012/r3gy-t195.

Copy

APA Citation

Rosso-Llopart, M. (2026, May 22). Managing Architectural Risk During Agile Development. Retrieved May 22, 2026, from https://doi.org/10.58012/r3gy-t195.

Copy

Chicago Citation

Rosso-Llopart, Manuel. "Managing Architectural Risk During Agile Development." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, May 22, 2026. https://doi.org/10.58012/r3gy-t195.

Copy

IEEE Citation

M. Rosso-Llopart, "Managing Architectural Risk During Agile Development," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 22-May-2026 [Online]. Available: https://doi.org/10.58012/r3gy-t195. [Accessed: 22-May-2026].

Copy

BibTeX Code

@misc{rosso-llopart\_2026,
author={Rosso-Llopart, Manuel},
title={Managing Architectural Risk During Agile Development},
month={{May},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/r3gy-t195},
note={Accessed: 2026-May-22}
}

Copy

# Managing Architectural Risk During Agile Development

###### [Manuel Rosso-Llopart](/authors/manuel-rosso-llopart)

###### May 22, 2026

##### PUBLISHED IN

[Software Engineering Research and Development](/blog/topics/software-engineering-research-development/)

##### CITE

<https://doi.org/10.58012/r3gy-t195>

Get Citation

##### SHARE

Architecture issues discovered late in a system’s lifecycle and are inherent to its design are more expensive (or may even be impossible) to fix. Often this is because issues discovered later in development stem from early decisions that have far-reaching software consequences and require major modifications. Identifying those issues that are architectural risks early in design can result in significant cost savings over the life of the system. In this blog post, adapted from [a recently published report](https://www.sei.cmu.edu/library/managing-architectural-risk-during-agile-development/), we propose an approach that draws from Agile Architecture Risk Management (AARM) and Continuous Risk Management (CRM) processes to create a practice for evaluating software architecture risks during development. By weighing the tradeoffs between design pattern attributes and quality attributes, the development team can identify architectural risks early and assess the system impacts of design decisions made during software development.

## Meeting the Needs of the Warfighter

Many Department of War (DoW) projects aimed at developing custom software capabilities are now completed using [Agile](https://www.sei.cmu.edu/blog/what-is-agile/) practices. However, [most Agile practices do not specifically mention activities related to software design or software architecture components during development](https://medium.com/moodah-pos/agile-development-95cad3573abf). A key attribute in Agile practices is speed of development. Often, this speed comes at the cost of fully evaluating design decisions with respect to architecture impact on quality attributes in the form of risk.

Proposals exist for how to apply [software architecture practices to Agile software development projects](https://www.sei.cmu.edu/library/howto-agilely-architect-an-agile-architecture/) (i.e., Agile architecture) and how to apply software architecture in Agile software development projects as a design risk mitigation strategy. In this blog post, we propose an approach that involves a continuous review of design decisions during development to better understand their impact on the architecture as risks against the quality attributes.

The process we propose consists of the following activities:

* continuous design risk evaluation with respect to quality attributes
* use of a Minimally Viable Architecture process
* dedication of design decision review early in the agile sprint
* a review of development team concerns as possible impacts to architecture risk

Applying an architecture methodology helps support risk mitigation for software development because it involves making [early, high-level decisions that prevent costly mistakes, security vulnerabilities, and performance issues](https://www.sei.cmu.edu/library/software-architecture-in-dod-acquisition-an-approach-and-language-for-a-software-development-plan/). Being aware of these attributes and how they are impacted by design decisions can later affect the Agile development practices used by development teams. Examples of these types of decisions include identifying user stories that emphasize quality attributes and may require further elaboration and determining how to measure the design decision acceptability of rapidly developed products for the customer. Understanding the clear connection between Agile software design activities and software architecture quality attributes will help architects, designers, program managers, and developers understand where better practices can be applied.

Architecture risk is defined as [the software system’s inherent inability to promote stakeholder goals (i.e., quality attributes)](https://www.linkedin.com/pulse/managing-technical-debt-continuous-architecture-anthony-j-lattanze). In this blog, when we talk about risk, we are speaking of uncertainty of consequences associated with engineering choices and commitments.

Abbie Redmon defines quality attributes this way:

In general, quality attributes are the [system properties that make a solution viable for the environment where the solution developed from the requirements is expected to operate](https://www.informit.com/articles/article.aspx?p=3128836&seqNum=3). These properties are instantiated when software patterns are used to meet the demands of a desired architecture. Understanding the impact of software design on software architecture can be challenging, as most [developers use familiar design patterns to produce a solution with speed as the goal](https://medium.com/%40josueparra2892/the-impact-of-design-patterns-on-software-development-a-deep-exploration-2369b9c17aa4). We are proposing that specific design decisions can impact the architecture by developing risks that impact how the solution meets quality attributes. The process changes identified in this blog will help alleviate this project concern.

## Continuous Risk Management

[Continuous Risk Management (CRM)](https://www.sei.cmu.edu/library/continuous-risk-management-guidebook/) collects concerns (i.e., uncertainties) from individual developers or the development team during Agile ceremonies. As appropriate, the concerns can be added to either the product backlog or sprint (i.e. iteration) backlog as a spike or task. Concerns are normally collected during

* a sprint planning meeting
* a backlog refinement meeting
* sprint reviews

[![figure1_05212026](/media/images/figure1_05212026_RGfr53V.max-1280x720.format-webp.webp)](/media/images/figure1_05212026_RGfr53V.original.png)

Figure 1: CRM’s Risk Process
[Dorofee, A. et al. Continuous Risk Management Guidebook.](https://www.sei.cmu.edu/library/continuous-riskmanagement-guidebook/)

Our approach focuses on the potential for quality attribute issues identified during sprints to evolve into architec...