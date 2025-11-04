---
title: A Model-Based Approach for Software Acquisition
url: https://www.sei.cmu.edu/blog/a-model-based-approach-for-software-acquisition/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2025-11-03
fetch_date: 2025-11-04T03:11:30.303992
---

# A Model-Based Approach for Software Acquisition

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

About

Our Work

Publications

News and Events

Education and Outreach

Careers

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. A Model-Based Approach for Software Acquisition

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Dempsey, C., 2025: A Model-Based Approach for Software Acquisition. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed November 3, 2025, https://doi.org/10.58012/vk1p-w413.

Copy

APA Citation

Dempsey, C. (2025, November 3). A Model-Based Approach for Software Acquisition. Retrieved November 3, 2025, from https://doi.org/10.58012/vk1p-w413.

Copy

Chicago Citation

Dempsey, Colin. "A Model-Based Approach for Software Acquisition." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, November 3, 2025. https://doi.org/10.58012/vk1p-w413.

Copy

IEEE Citation

C. Dempsey, "A Model-Based Approach for Software Acquisition," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 3-Nov-2025 [Online]. Available: https://doi.org/10.58012/vk1p-w413. [Accessed: 3-Nov-2025].

Copy

BibTeX Code

@misc{dempsey\_2025,
author={Dempsey, Colin},
title={A Model-Based Approach for Software Acquisition},
month={{Nov},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/vk1p-w413},
note={Accessed: 2025-Nov-3}
}

Copy

# A Model-Based Approach for Software Acquisition

###### [Colin Dempsey](/authors/colin-dempsey)

###### November 3, 2025

##### PUBLISHED IN

[Model-Based Systems Engineering](/blog/topics/model-based-systems-engineering/)

##### CITE

<https://doi.org/10.58012/vk1p-w413>

Get Citation

##### SHARE

The Department of War (DoW) is undergoing a significant transformation in how it acquires and develops software systems. Central to this evolution is [the shift from traditional document-based processes to model-centric methodologies](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500097p.PDF?ver=bePIqKXaLUTK_Iu5iTNREw%3D%3D). In this context, researchers at Carnegie Mellon University Software Engineering Institute (SEI) recently analyzed the alignment of the DoW’s [Software Acquisition Pathway (SWP)](https://www.sei.cmu.edu/library/dod-software-acquisition-pathway-modernizing-and-speeding-software-acquisition/) with the [Unified Architecture Framework (UAF)](https://www.omg.org/uaf/). The aim of the study, as detailed in this blog post, is to operationalize [model-based systems engineering (MBSE)](https://www.sei.cmu.edu/blog/introduction-model-based-systems-engineering-mbse/) within the SWP using UAF, which would enhance traceability, decision-making, and compliance across the lifecycle.

## **The Need for a Model-Centric Acquisition Strategy**

The federal government’s digital engineering strategy, [initiated in 2018](https://ac.cto.mil/wp-content/uploads/2019/06/2018-Digital-Engineering-Strategy_Approved_PrintVersion.pdf) and reinforced by subsequent directives across military branches, emphasizes the use of digital models as the primary means of communication in engineering activities. The [2023 release of DoDI 5000.97](https://www.dau.edu/blogs/new-digital-engineering-policy-published) formalized this shift, requiring programs initiated thereafter to incorporate digital engineering capabilities.

Despite this policy momentum, implementing MBSE across diverse acquisition programs remains challenging. These challenges present valuable opportunities within the SWP. While the policy is designed to streamline software acquisition, there is exciting potential to enhance it further by incorporating clearer guidance on model-based systems engineering (MBSE), especially for embedded software systems that require high levels of certification and assurance.

As part of ongoing work to address these challenges, SEI researchers contributed as panelists at the [22nd Annual Acquisition Research Symposium](https://nps.edu/web/ddm/-/22nd-annual-acquisition-research-symposium) hosted by the Naval Postgraduate School. We also presented the paper [*Synergizing the Software Acquisition Pathway (SWP) With the Unified Architecture Framework (UAF) For Operationalization*](https://dair.nps.edu/handle/123456789/5362). In this post, we’ll introduce the concepts presented in the paper including an overview of the SWP, UAF, the SEI MBSynergy project, and walk through an example related to developing a Capability Needs Statement for the SWP program using UAF.

## **A Focus on the Software Acquisition Pathway**

The SWP provides a tailored acquisition route for software-intensive systems. More specifically, the SWP provides software-intensive development programs with a streamlined path for developing and delivering software capability, emphasizing the use of modern software development methods and tools for delivering capability rapidly.

The SWP lifecycle is separated into two primary phases:

* The **Planning Phase** focuses on defining capability needs, developing strategies and roadmaps, establishing infrastructure, and designing system architecture.
* The **Execution Phase** involves software development, testing, delivery, and value assessment, with continuous user engagement.

The pathway supports various software types, including embedded software, which was the focus of our study. Embedded software, often integrated into weapon systems, requires heightened scrutiny for safety, cybersecurity, and operational effectiveness, making it an ideal candidate for MBSE application.

As of the time of this post, there are [programs utilizing the Software Acquisition Pathway](https://aaf.dau.edu/aaf/software/swp-programs/) across all major departments of the DoW and associated services and the utilization of this pathway is increasing in importance. A March 6, 2025, memo, [*Directing Modern Software Acquisition to Maximize Lethality*](https://media.defense.gov/2025/Mar/07/2003662943/-1/-1/1/DIRECTING-MODERN-SOFTWARE-ACQUISITION-TO-MAXIMIZE-LETHALITY.PDF) directs the DoW to adopt the Software Acquisition Pathway as the preferred pathway for all software development programs.

## **Benefits of an UAF-Based MBSE Approach**

The UAF, developed by the [Object Management Group (OMG)](https://www.omg.org/), is a standardized modeling language that evolved from frameworks like [DoDAF](https://dodcio.defense.gov/Library/DoD-Architecture-Framework/), MoDAF, and NATO’s NAF. It provides a comprehensive set of 89 model views organized by stakeholder viewpoints (e.g., operational, security) and modeling aspects (e.g., processes, parameters).

UAF’s structured semantics and extensibility make it well-suited for MBSE in complex defense environments. However, its breadth can be overwhelming for new users. To address this, the SEI study leverages the [UAF Domain Meta Model (DMM) version 1.2](https://www.omg.org/spec/UAF/1.2/DMM/PDF) and the [Enterprise Architecture Guide for UAF](https://www.omg.org/cgi-bin/doc?formal/22-07-10.pdf) to create a targeted, scenario-based approach tailored to the SWP.

The integration of UAF into the SWP offers several strategic advantages:

* **enhanced traceability and digital threading.** By structuring information in models, programs can establish robust digital threads that link requirements, design decisions, and verification artifacts across the lifecycle.
* **improved decision-making.** Models enable early analysis of tradeoffs, risks, and quality attributes, supporting more informed and timely decisions.
* **reduced documentation burden.** Model-based artifacts can replac...