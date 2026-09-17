---
title: AI-Augmented AADL in Visual Studio Code
url: https://www.sei.cmu.edu/blog/ai-augmented-aadl-in-visual-studio-code/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-09-16
fetch_date: 2026-09-17T06:59:33.114284
---

# AI-Augmented AADL in Visual Studio Code

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
4. AI-Augmented AADL in Visual Studio Code

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Dempsey, C., and Wrage, L., 2026: AI-Augmented AADL in Visual Studio Code. Software Engineering Institute blog, Accessed September 17, 2026, https://doi.org/10.58012/4c2e-xd64.

Copy

APA Citation

Dempsey, C., & Wrage, L. (2026, September 16). AI-Augmented AADL in Visual Studio Code. Retrieved September 17, 2026, from https://doi.org/10.58012/4c2e-xd64.

Copy

Chicago Citation

Dempsey, Colin, and Lutz Wrage. "AI-Augmented AADL in Visual Studio Code." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, September 16, 2026. https://doi.org/10.58012/4c2e-xd64.

Copy

IEEE Citation

C. Dempsey, and L. Wrage, "AI-Augmented AADL in Visual Studio Code," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 16-Sep-2026 [Online]. Available: https://doi.org/10.58012/4c2e-xd64. [Accessed: 17-Sep-2026].

Copy

BibTeX Code

```
@misc{dempsey_2026,
author={Dempsey, Colin and Wrage, Lutz},
title={AI-Augmented AADL in Visual Studio Code},
month={Sep},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/4c2e-xd64},
url={https://doi.org/10.58012/4c2e-xd64},
note={Accessed: 2026-Sep-17}
}
```

Copy

# AI-Augmented AADL in Visual Studio Code

![Headshot of Colin Dempsey.](/media/images/Dempsey_Colin_314_240125.max-180x180.format-webp.webp)

###### [Colin Dempsey](/authors/colin-dempsey) and [Lutz Wrage](/authors/lutz-wrage)

###### September 16, 2026

##### PUBLISHED IN

[Model-Based Systems Engineering](/blog/topics/model-based-systems-engineering/)

##### CITE

<https://doi.org/10.58012/4c2e-xd64>

Get Citation

##### SHARE

The challenging part of architecture modeling is not the act of drawing boxes and connecting lines, but capturing sufficient engineering context and data to answer critical questions about system behavior:

* Can a sensor-to-actuator path meet its end-to-end latency requirement?
* Does the deployed communication architecture have enough capacity?
* Which combinations of operational modes can the system attain?
* Are software execution assumptions consistent with the hardware resource allocations?

The [Architecture Analysis and Design Language (AADL)](https://www.sei.cmu.edu/projects/architecture-analysis-and-design-language-aadl/), now an [SAE International standard](https://www.sae.org/standards/as5506d-architecture-analysis-design-language-aadl), is designed to answer questions such as these on the basis of an analyzable architecture model. AADL can describe software threads and processes, processors and memories, physical and virtual buses, typed communications, deployment bindings, operational modes, and the properties needed by engineering analyses. The challenge is that an analysis-ready model must be valid. A model can appear plausible while containing an unresolved component reference, an incorrectly applied property, an incomplete flow, or a timing assumption that does not mean what its author intended.

SEI researchers developed an [AADL open-source suite](https://www.sei.cmu.edu/library/aadl-tooling-and-software/) for working with AADL models outside the traditional desktop environment for AADL, which is the [Open Source AADL Tool Environment (OSATE)](https://github.com/osate). This includes an extension for [Visual Studio Code](https://code.visualstudio.com/) that brings language services and selected architecture analyses from OSATE into the same environment used by many software engineers and AI coding tools.

The extension was developed as open source and is available on the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=osate.aadl2). The source is available through the SEI-managed [OSATE GitHub organization](https://github.com/osate) in the [AADL Tooling repository](https://github.com/osate/aadl-tooling).

For program managers and engineering leaders, the potential value of an accelerated architecture modeling capability is not simply faster model authoring. For example, it can help larger teams apply scarce architecture expertise consistently, shortening the time between design changes and evidence about their consequences, which both reduces design risk and helps keep models, analysis results, and documentation aligned. From the perspective of program management, that means timing, resource, and integration risks can surface earlier, when they are less expensive to address.

AI has a role in this extension to OSATE. The AI capability does not replace engineering judgment or approval authority, but it can reduce routine modeling effort so specialists can focus on assumptions, tradeoffs, and acceptance criteria.

If we are to realize these potential benefits, we must address a critical question: What changes when an AI coding tool can not only author AADL models, but also receive feedback from an AADL language server, instantiate those models, run analyses, and inspect the resulting reports?

As detailed later in this post, we piloted this approach by building a flight-controller system that models both software and hardware. Our prototype system did not prove that AI can design or certify a flight-control system. It did, however, demonstrate something narrower and more useful: when coupled with domain-specific validation and analysis, an AI coding tool can help an engineer create and refine a nontrivial AADL model while producing evidence that reviewers can inspect and trace back to model elements and assumptions.

## Moving AADL into the Engineering Loop

Moving AADL into the engineering loop means treating the architecture model as a version-controlled, analyzable artifact that evolves with the system rather than documentation consulted only at review milestones. Each change can be checked while design decisions are still being made, shortening the distance between an architectural choice and evidence about its consequences. By placing these capabilities in Visual Studio Code, the extension gives engineers and AI coding tools an integrated environment for making, evaluating, and reviewing model changes.

To support this workflow, the extension provides both language-aware editor services and architecture-analysis capabilities:

* syntax validation and diagnostics
* completion, navigation, outline, breadcrumbs, and code comment hover information
* access to bundled AADL packages and property sets
* component instantiation
* end-to-end latency analysis
* bound bus-load analysis
* mode-reachability analysis, including HTML, [DOT](https://graphviz.org/doc/info/lang.html), and [SMV](https://nusmv.fbk.eu/) output

This combination of editor services and expanded capabilities matters because a generative AI model can produce text that resembles AADL, but resemblance is not a useful acceptance criterion. The language server can identify malformed syntax, unresolved names, illegal features, and invalid property use. Instantiation then checks whether the declarative architecture can be elaborated into a concrete system instance. Analyses operate on that instance and expose the consequences of its timing, communication, binding, and modal properties.

Together, these capabilities create a feedback loop:

1. The engineer states an architectural objective and its constraints.
2. The AI coding tool creates or modifies candidate AADL source.
3. The language server returns model-specific diagnostics.
4. The AI and engineer use those diagnostics to revise the source.
5. The AI calls the extension to instantiate the a...