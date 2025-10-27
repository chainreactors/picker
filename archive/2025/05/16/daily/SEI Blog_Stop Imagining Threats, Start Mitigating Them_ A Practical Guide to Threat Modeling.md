---
title: Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling
url: https://insights.sei.cmu.edu/blog/stop-imagining-threats-start-mitigating-them-a-practical-guide-to-threat-modeling/
source: SEI Blog
date: 2025-05-16
fetch_date: 2025-10-06T22:28:43.593346
---

# Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Vesey, A., 2025: Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed October 4, 2025, https://doi.org/10.58012/1m18-xb50.

Copy

APA Citation

Vesey, A. (2025, May 15). Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling. Retrieved October 4, 2025, from https://doi.org/10.58012/1m18-xb50.

Copy

Chicago Citation

Vesey, Alex. "Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, May 15, 2025. https://doi.org/10.58012/1m18-xb50.

Copy

IEEE Citation

A. Vesey, "Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 15-May-2025 [Online]. Available: https://doi.org/10.58012/1m18-xb50. [Accessed: 4-Oct-2025].

Copy

BibTeX Code

@misc{vesey\_2025,
author={Vesey, Alex},
title={Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling},
month={{May},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/1m18-xb50},
note={Accessed: 2025-Oct-4}
}

Copy

# Stop Imagining Threats, Start Mitigating Them: A Practical Guide to Threat Modeling

![Headshot of Alex Vesey.](/media/images/Vesey_Alex_008_241113.360x360.max-180x180.format-webp.webp)

###### [Alex Vesey](/authors/alex-vesey)

###### May 15, 2025

##### PUBLISHED IN

[Cybersecurity Engineering](/blog/topics/cybersecurity-engineering/)

##### CITE

<https://doi.org/10.58012/1m18-xb50>

Get Citation

##### SHARE

When building a software-intensive system, [a key part in creating a secure and robust solution is to develop a cyber threat model](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling). This is a model that expresses who might be interested in attacking your system, what effects they might want to achieve, when and where attacks could manifest, and how attackers might go about accessing the system. Threat models are important because they guide requirements, system design, and operational choices. Effects can include, for example, compromise of confidential information, modification of information contained in the system, and disruption of operations. There are diverse purposes for achieving these kinds of effects, ranging from espionage to ransomware.

This blog post focuses on a method threat modelers can use to make credible claims about attacks the system could face and to ground those claims in observations of adversary [tactics, techniques, and procedures](https://csrc.nist.gov/glossary/term/tactics_techniques_and_procedures) (TTPs).

Brainstorming, subject matter expertise, and operational experience can go a long way in developing a list of relevant threat scenarios. During initial threat scenario generation for a hypothetical software system, it would be possible to imagine, *What if attackers steal account credentials and mask their movement by putting false or bad data into the user monitoring system?* The harder task—where the perspective of threat modelers is critical—substantiates that scenario with known patterns of attacks or even specific TTPs. These could be informed by potential threat intentions based on the operational role of the system.

Developing practical and relevant mitigation strategies for the identified TTPs is an important contributor to system requirements formulation, which is one of the goals of threat modeling.

This SEI blog post outlines a method for substantiating threat scenarios and mitigations by linking to industry-recognized attack patterns powered by [model-based systems engineering](https://insights.sei.cmu.edu/blog/introduction-model-based-systems-engineering-mbse/) (MBSE).

In his memo [*Directing Modern Software Acquisition to Maximize Lethality*](https://media.defense.gov/2025/Mar/07/2003662943/-1/-1/1/DIRECTING-MODERN-SOFTWARE-ACQUISITION-TO-MAXIMIZE-LETHALITY.PDF), Secretary of Defense Pete Hegseth wrote, “Software is at the core of every weapon and supporting system we field to remain the strongest, most lethal fighting force in the world.” While understanding cyber threats to these complex software intensive systems is important, identifying threats and mitigations to them early in the design of a system [helps reduce the cost to fix them](https://www.researchgate.net/publication/255965523_Integrating_Software_Assurance_into_the_Software_Development_Life_Cycle_SDLC). In response to Executive Order (EO) 14028, *Improving the Nation’s Cybersecurity*, the National Institute of Standards and Technology (NIST) recommended [11 practices for software verification](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8397.pdf). Threat modeling is at the top of the list.

## Threat Modeling Goals: 4 Key Questions

Threat modeling guides the requirements specification and early design choices to make a system robust against attacks and weaknesses. Threat modeling can help software developers and cybersecurity professionals know what types of defenses, mitigation strategies, and controls to put in place.

Threat modelers can frame the process of threat modeling around answers to four key questions ([adapted from Adam Shostack](https://shostack.org/resources/threat-modeling#4steps)):

1. *What are we building?*
2. *What can go wrong?*
3. *What should we do about those wrongs?*
4. *Was the analysis sufficient?*

## **What Are We Building?**

The foundation of threat modeling is the model of the system focused on its potential interactions with threats. A model [is a graphical, mathematical, logical, or physical representation that abstracts reality to address a particular set of concerns while omitting details not relevant to the concerns](https://sebokwiki.org/wiki/What_is_a_Model%3F) of the model builder. There are many methodologies that provide guidance on how to construct threat models for different types of systems and use cases. For already built systems where the design and implementation are known and where the principal concerns relate to faults and errors (rather than acts by intentioned adversaries), techniques such as *fault tree analysis* may be more appropriate. These techniques generally assume that desired and undesired states are known and can be characterized. Similarly, *kill chain analysis* can be helpful to understand the full end-to-end execution of a cyber attack.

However, existing high-level systems engineering models may not be appropriate to identify specific vulnerabilities used to conduct an attack. These systems engineering models can create useful context, but more modeling is necessary to address threats.

In this post I use the [Unified Architecture Framework](https://www.omg.org/uaf/) (UAF) to guide our modeling of the system. For larger systems employing MBSE, the threat model can build on [DoDAF, UAF](https://www.dau.edu/acquipedia-article/dod-architecture-framework-dodaf), or other architectural framework models. The common thread with all of these models is that threat modeling is enabled by models of information interactions and flows among components. A common model also gives benefits in coordination across large teams. When multiple groups are working on and d...