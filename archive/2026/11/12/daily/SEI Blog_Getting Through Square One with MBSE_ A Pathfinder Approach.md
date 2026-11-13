---
title: Getting Through Square One with MBSE: A Pathfinder Approach
url: https://www.sei.cmu.edu/blog/getting-through-square-one-with-mbse-a-pathfinder-approach/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-11-12
fetch_date: 2026-11-13T09:07:14.181404
---

# Getting Through Square One with MBSE: A Pathfinder Approach

[Skip to main content](#main-content)

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
4. Getting Through Square One with MBSE: A Pathfinder Approach

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Nolan, C., and Dempsey, C., 2026: Getting Through Square One with MBSE: A Pathfinder Approach. Software Engineering Institute blog, Accessed November 12, 2026, https://doi.org/10.58012/57xw-3c06.

Copy

APA Citation

Nolan, C., & Dempsey, C. (2026, November 12). Getting Through Square One with MBSE: A Pathfinder Approach. Retrieved November 12, 2026, from https://doi.org/10.58012/57xw-3c06.

Copy

Chicago Citation

Nolan, Crisanne, and Colin Dempsey. "Getting Through Square One with MBSE: A Pathfinder Approach." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, November 12, 2026. https://doi.org/10.58012/57xw-3c06.

Copy

IEEE Citation

C. Nolan, and C. Dempsey, "Getting Through Square One with MBSE: A Pathfinder Approach," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 12-Nov-2026 [Online]. Available: https://doi.org/10.58012/57xw-3c06. [Accessed: 12-Nov-2026].

Copy

BibTeX Code

```
@misc{nolan_2026,
author={Nolan, Crisanne and Dempsey, Colin},
title={Getting Through Square One with MBSE: A Pathfinder Approach},
month={Nov},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/57xw-3c06},
url={https://doi.org/10.58012/57xw-3c06},
note={Accessed: 2026-Nov-12}
}
```

Copy

# Getting Through Square One with MBSE: A Pathfinder Approach

![Headshot of Crisanne Nolan.](/media/images/Nolan_Crisanne_268_240924.max-180x180.format-webp.webp)
![Headshot of Colin Dempsey.](/media/images/Dempsey_Colin_314_240125.max-180x180.format-webp.webp)

###### [Crisanne Nolan](/authors/crisanne-nolan) and [Colin Dempsey](/authors/colin-dempsey)

###### November 12, 2026

##### PUBLISHED IN

[Model-Based Systems Engineering](/blog/topics/model-based-systems-engineering/)

##### CITE

<https://doi.org/10.58012/57xw-3c06>

Get Citation

##### SHARE

As engineering organizations seek to benefit from digital engineering, many consider strengthening how models are used across engineering work under the banner of model-based systems engineering (MBSE). [The International Council on Systems Engineering (INCOSE)](https://sebokwiki.org/wiki/INCOSE_Systems_Engineering_Vision_2020) defines MBSE as the formalized application of modeling to support requirements, design, analysis, verification, and validation throughout the system life cycle. The distinction is not whether an organization uses models, since nearly all engineering activities do, but whether to adopt practices that make selected models authoritative, connected, and governed. This means that models are used as primary support for making and verifying lifecycle decisions and for reducing technical risk. This blog post explains how organizations can [get started with an MBSE strategy](/library/mbse-strategy-workshop-guidebook/) through a pathfinder project that focuses on one team and one target system, relates models to specific decisions, and measures the results before expanding.

The choices of relevant models depend on the decisions being faced or technical risks to be mitigated. Examples include:

* a SysML v2 model that links requirements to system structure, interfaces, behavior, and verification
* an AADL model that represents embedded software and hardware, processor and bus bindings, communication paths, and end-to-end latency
* a requirements model in IBM DOORS that manages requirement decomposition, allocation, baselines, change history, and verification links
* a government reference architecture modeled in SysML v1 in Cameo Systems Modeler that defines reusable mission, system, and interface patterns for programs to tailor
* and a UAF model that connects operational goals, activities, roles, resources, and measures

These models answer different questions and require different expertise, evidence, validation, and governance.

Consequently, adopting MBSE should not be treated as a binary choice, as in, you’re either “doing MBSE” or you’re not. A useful MBSE practice names the model, the decisions it supports, when it is created and updated, how it connects to other engineering information, how it is validated, and how its results are checked with respect to the as-built system. A SysML v2 model may be checked for semantic consistency, design acceptance criteria, and traceability; an AADL model may be instantiated and analyzed against latency or resource limits; an IBM DOORS requirements model may be reviewed for attribute completeness, baseline integrity, and traceability coverage; a government reference architecture in Cameo may be checked for conformance to its SysML v1 profile and for complete mission, system, and interface patterns; and a UAF model may be reviewed for alignment among goals, activities, roles, and resources.

Scaling considerations can be significant, including horizontal (i.e., across elements of integrated systems) and vertical (i.e., in support of systems that must support multiple variants and continue to evolve). Product-line SysML models, for example, must manage variants and traceability; AADL models spanning computing platforms must manage bindings and timing assumptions; DOORS repositories must manage baselines, access, and link integrity; and reference architectures in SysML or UAF reused across programs must manage profile, library, version, and tailoring governance.

## Challenges with Digital Transformation and MBSE

The National Academies' 2025 study [*Digital Transformation in the Department of the Air Force*](https://www.nationalacademies.org/projects/DEPS-AFSB-23-01/publication/29198) describes digital transformation as the advancement of practices supporting MBSE, digital twins, and digital threads across full system life cycles. It also concludes that there is no proven formula for enterprise-wide success. A model does not create value merely by existing. It creates value when people use trustworthy, appropriately validated model information to make and verify decisions.

The evidence base reinforces the need for a measured approach. [Campo and colleagues](https://incose.onlinelibrary.wiley.com/doi/10.1002/sys.21644) reviewed 60 sources and coded more than 2,900 claims about MBSE; 47 percent of the claims rested on author opinion, and 86 percent were not supported by a metric. [Henderson and Salado](https://incose.onlinelibrary.wiley.com/doi/10.1002/sys.21566) similarly found that two-thirds of claimed MBSE benefits were supported only by perceived evidence and that only two papers in their review reported measured evidence. These findings do not show that MBSE lacks value. They show that organizations need explicit, model-specific value hypotheses and measures that connect a defined model and its use in a decision to engineering and mission outcomes.

Adoption studies also identify practical obstacles. [Vogelsang and colleagues](https://link.springer.com/chapter/10.1007/978-3-319-69926-4_14) interviewed 20 experts from 10 German embedded-systems companies and found concerns about immature tooling, uncertain return on investment, and migration of existing data and processes. Their participants often expected MBSE to manage complexity and reduce cost but could not always identify which models, analyses, or decision workflows would produce those benefits. The researchers concluded that poor experiences frequently began with expectations that were too high or insufficiently concrete.

The SEI's [first MBSynergy Workshop...