---
title: Software-Defined Warfare: Crossing the Chasm in Two Software Areas
url: https://www.sei.cmu.edu/blog/software-defined-warfare-crossing-the-chasm-in-two-software-areas/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-06-23
fetch_date: 2026-06-24T06:06:21.960477
---

# Software-Defined Warfare: Crossing the Chasm in Two Software Areas

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
4. Software-Defined Warfare: Crossing the Chasm in Two Software Areas

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Nielsen, P., 2026: Software-Defined Warfare: Crossing the Chasm in Two Software Areas. Software Engineering Institute blog, Accessed June 23, 2026, https://doi.org/10.58012/9wg2-8778.

Copy

APA Citation

Nielsen, P. (2026, June 23). Software-Defined Warfare: Crossing the Chasm in Two Software Areas. Retrieved June 23, 2026, from https://doi.org/10.58012/9wg2-8778.

Copy

Chicago Citation

Nielsen, Paul. "Software-Defined Warfare: Crossing the Chasm in Two Software Areas." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, June 23, 2026. https://doi.org/10.58012/9wg2-8778.

Copy

IEEE Citation

P. Nielsen, "Software-Defined Warfare: Crossing the Chasm in Two Software Areas," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 23-Jun-2026 [Online]. Available: https://doi.org/10.58012/9wg2-8778. [Accessed: 23-Jun-2026].

Copy

BibTeX Code

```
@misc{nielsen_2026,
author={Nielsen, Paul},
title={Software-Defined Warfare: Crossing the Chasm in Two Software Areas},
month={Jun},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/9wg2-8778},
url={https://doi.org/10.58012/9wg2-8778},
note={Accessed: 2026-Jun-23}
}
```

Copy

# Software-Defined Warfare: Crossing the Chasm in Two Software Areas

![Headshot of Paul Neilsen.](/media/images/Paul_Nielsen_194_230206.360x360.max-180x180.format-webp.webp)

###### [Paul Nielsen](/authors/paul-nielsen)

###### June 23, 2026

##### PUBLISHED IN

[Software Engineering Research and Development](/blog/topics/software-engineering-research-development/)

##### CITE

<https://doi.org/10.58012/9wg2-8778>

Get Citation

##### SHARE

[Software-defined warfare is today’s reality](https://media.defense.gov/2025/Mar/07/2003662943/-1/-1/1/DIRECTING-MODERN-SOFTWARE-ACQUISITION-TO-MAXIMIZE-LETHALITY.PDF) for national security, shifting the emphasis in military operations from hardware to software, “[the core of every weapon and supporting system](https://media.defense.gov/2025/Mar/07/2003662943/-1/-1/1/DIRECTING-MODERN-SOFTWARE-ACQUISITION-TO-MAXIMIZE-LETHALITY.PDF)” fielded for defense. The Atlantic Council’s 2025 [*Commission on Software-Defined Warfare: Final Report*](https://www.atlanticcouncil.org/in-depth-research-reports/report/atlantic-council-commission-on-software-defined-warfare/) defines software-defined warfare as the “continuous integration and delivery of cutting-edge technology and leading interoperable software into legacy and future defense systems.” The report emphasizes the need for speed through artificial intelligence (AI) by calling on national security organizations to “acquire and sustain unified, shared platforms that support and accelerate the end-to-end development, deployment, and governance of AI solutions.”

This blog post examines how software engineering practices can meaningfully address two enterprise challenges for software-defined warfare identified in the Atlantic Council’s report. The first is a shortfall of software pipelines, talent, and resources, and the second is impediments to the use of DevSecOps. Software engineering is the “[application of a systematic, disciplined, quantifiable approach](https://www.computer.org/education/bodies-of-knowledge/software-engineering)” across the lifecycle of software-enabled systems. Over the past four decades, the advances noted in successive versions of the Software Engineering Body of Knowledge (SWEBoK) suggest that [software is never done](https://media.defense.gov/2019/May/01/2002126690/-1/-1/0/SWAP%20EXECUTIVE%20SUMMARY.PDF). As software continues to improve, its challenges and opportunities do as well.

Software engineering recognizes the importance of both software code (functional instructions) and architecture (system quality attributes). Although the machine learning (ML) software algorithms for AI systems are different—model-based, able to learn new patterns, and producing output based on statistical modeling—[the development and sustainment of those systems is analogous to designing, building, deploying, and improving software-reliant systems](https://www.sei.cmu.edu/documents/1308/2021_014_001_741195.pdf).

## Software-Defined Warfare, an Evolving Concept

The Department of War (DoW) has long worked toward software-defined control. In the late 1970s, for instance, programs to develop software-defined radios (SDRs) sought to [replace incompatible legacy radios](https://www.mitre.org/sites/default/files/pdf/nguyen.pdf) with ones that could be configured—and reconfigured—with software. When I served as Commander of the Air Force Research Lab at Griffiss Air Force Base in Rome, New York, our teams developed the first open architecture SDR in the SPEAKeasy (Software Programmable Embedded Architecture) project. SPEAKeasy technology allowed troops to use a single device to communicate with Army, Navy, and Air Force radios, and it was foundational to the later, larger Joint Tactical Radio System (JTRS) programs.

Alberts, Garstka, and Stein described software-defined networking in a 1999 report [*Network-Centric Warfare: Developing and Leveraging Information Superiority*](https://apps.dtic.mil/sti/tr/pdf/ADA406255.pdf). More recently, DoW’s [Project Maven](https://defensetalks.com/united-states-project-maven-and-the-rise-of-ai-assisted-warfare/) boosted software-defined warfare by applying ML to analyze the tremendous volume of data available. In this decade, the [Combined Joint All-Domain Command and Control (CJADC2)](https://www.ai.mil/Initiatives/CJADC2/) initiative emphasizes a comprehensive approach to act “across all domains, and with partners, to deliver information advantage at the speed of relevance.” Today, the DoW is accelerating software-defined warfare with “[AI-enabled capability development](https://media.defense.gov/2026/Jan/12/2003855671/-1/-1/0/ARTIFICIAL-INTELLIGENCE-STRATEGY-FOR-THE-DEPARTMENT-OF-WAR.PDF).”

While critically needed, software-defined warfare is not guaranteed and relies on network connectivity that is both secure and always available. Denied, disrupted, intermittent, and limited (DDIL) environments, [a feature of the tactical edge](https://www.sei.cmu.edu/blog/networking-at-the-tactical-and-humanitarian-edge/), leave systems vulnerable to cyber-attack and outages. Resilient designs can often overcome this, but there are other impediments, such as a paucity of good training data for AI models, slow procurement processes, a shortage of people with the right skills and expertise, and cultural resistance.

## Software Concerns in the Atlantic Council Report

The Atlantic Council, whose commissioners include former DoW officials and software industry leaders, recommends in its report that the DoW “invest in the pillars of software and AI development . . . to empower end users to efficiently generate and operationalize software and AI . . . .” The report poses seven “as is” enterprise challenges to realizing software-defined warfare. [This blog post addresses two of them](https://www.atlanticcouncil.org/wp-content/uploads/2025/03/Commission-on-Software-Defined-Warfare-Final-Report.pdf%2C):

1. There is a major shortfall of software pipelines, talent, and resources to meet the demand for software-defined warfare within DoD organizations.
2. The absence of a software-centric culture across the DoD impedes the employment of modern DevSecOps, which fosters rapid iterations and recertifications.

Each Atlant...