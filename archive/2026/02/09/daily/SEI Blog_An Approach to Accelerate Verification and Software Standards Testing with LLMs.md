---
title: An Approach to Accelerate Verification and Software Standards Testing with LLMs
url: https://www.sei.cmu.edu/blog/an-approach-to-accelerate-verification-and-software-standards-testing-with-llms/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-02-09
fetch_date: 2026-02-10T04:27:30.570294
---

# An Approach to Accelerate Verification and Software Standards Testing with LLMs

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
4. An Approach to Accelerate Verification and Software Standards Testing with LLMs

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Karl, R., Hindka, Y., Zhang, S., and Robert, J., 2026: An Approach to Accelerate Verification and Software Standards Testing with LLMs. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed February 9, 2026, https://doi.org/10.58012/rzfv-cx22.

Copy

APA Citation

Karl, R., Hindka, Y., Zhang, S., & Robert, J. (2026, February 9). An Approach to Accelerate Verification and Software Standards Testing with LLMs. Retrieved February 9, 2026, from https://doi.org/10.58012/rzfv-cx22.

Copy

Chicago Citation

Karl, Ryan, Yash Hindka, Shen Zhang, and John Robert. "An Approach to Accelerate Verification and Software Standards Testing with LLMs." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, February 9, 2026. https://doi.org/10.58012/rzfv-cx22.

Copy

IEEE Citation

R. Karl, Y. Hindka, S. Zhang, and J. Robert, "An Approach to Accelerate Verification and Software Standards Testing with LLMs," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 9-Feb-2026 [Online]. Available: https://doi.org/10.58012/rzfv-cx22. [Accessed: 9-Feb-2026].

Copy

BibTeX Code

@misc{karl\_2026,
author={Karl, Ryan and Hindka, Yash and Zhang, Shen and Robert, John},
title={An Approach to Accelerate Verification and Software Standards Testing with LLMs},
month={{Feb},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/rzfv-cx22},
note={Accessed: 2026-Feb-9}
}

Copy

# An Approach to Accelerate Verification and Software Standards Testing with LLMs

![Headshot of Ryan Karl.](/media/images/Karl_Ryan_004_241009.max-180x180.format-webp.webp)
![Headshot of Yash Hindka.](/media/images/Hindka_Yash_007_241009.max-180x180.format-webp.webp)

###### [Ryan Karl](/authors/ryan-karl), [Yash Hindka](/authors/yash-hindka), [Shen Zhang](/authors/shen-zhang), and [John E. Robert](/authors/john-robert)

###### February 9, 2026

##### PUBLISHED IN

[AI-Augmented Software Engineering](/blog/topics/ai-augmented-software-engineering/)

##### CITE

<https://doi.org/10.58012/rzfv-cx22>

Get Citation

##### SHARE

The recent explosion in large language model (LLM) technology has highlighted the challenges of using public generative artificial intelligence (AI) tools in classified environments, especially for software analysis. Currently, software analysis falls on the shoulders of heuristic static analysis (SA) tools and manual code review, which tend to provide limited technical depth and are often time-consuming in practice. As this post details, a group of SEI researchers sought to prove that LLMs can be used in unclassified environments to rapidly develop tools that could then be used to accelerate software analysis in classified environments. The resulting tools were a plugin-based architecture that enables analysts to develop customer checkers (i.e., plugins) and a visualization tool that leverages CodeQL to perform control flow and taint analysis to help analysts perform CSA. The tools created an initial time savings of approximately 40 percent and improved accuracy of approximately 10 percent, based on experiments conducted with a team of software analysts.

In this blog post, adapted from [a recently published paper](https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/ec51f137-8f73-476f-98cd-d8027d6fc745/content), we highlight our approach, which can be used to develop static analysis tools in classified and unclassified environments, as well as the two existing tools. This work is part of ongoing SEI research to apply artificial intelligence (AI) across software engineering activities, including software analysis.

## Issues with Static Analysis Tolls in the Software Development Lifecycle

While LLMs are relatively new, SA tools have long been present in the software development lifecycle. Despite their utility, out-of-the-box heuristic SA tools often fail to provide the quality analysis required for complex systems. These SA tools tend to use pattern matching and other approximate techniques and lack full comprehension of code semantics, leading to gaps in the depth of their analysis. Conversely, manual code review, despite its effectiveness in identifying issues that automated tools might miss, is time consuming, demanding of human attention, and scales poorly with the size of modern software projects. These shortcomings present a significant bottleneck in the SDLC, impacting the speed and quality of software delivery.

To resolve these bottlenecks, we sought to demonstrate how LLMs can be used to develop tools that streamline traditionally manual aspects of software analysis. Unlike existing research on directly applying LLMs to software analysis tasks, our research suggests that leveraging public LLMs (i.e., an internet accessible, commercial/open-source model such as ChatGPT) for SA tool generation offers [increased efficiency and a greater technical depth for software analysis tasks](https://www.sei.cmu.edu/blog/using-chatgpt-to-analyze-your-code-not-so-fast/). Our work focused on improving code verification in classified environments (i.e., any area that handles sensitive information and/or has an air-gapped network).

## Issues with LLMs in Software Analysis

LLM-generated code can be error-prone, which highlights [the need for robust verficiation and testing frameworks](https://doi.org/10.1109/TSE.2024.3392499). LLM reliability issues are particularly concerning when LLMs are applied to critical tasks, such as vulnerability and quality analysis. These sophisticated tasks often require a contextual understanding of software’s logic and execution flow. LLMs, constrained by their training data, often lack the subject matter expertise of trained software professionals and may fail to fully grasp the intricacies of complex systems. For example, [experiments by researchers in the SEI CERT Division's Secure Development initiative demonstrated the limitations of LLMs in identifying and correcting C code that was noncompliant with a coding standard](https://insights.sei.cmu.edu/blog/using-chatgpt-toanalyze-your-code-not-so-fast/).

## A Methodology for Incorporating LLMs in Static Analysis Tool Development

Although there has been a great deal of work on the efficacy of LLMs for direct software analysis, their current limitations prompted us to investigate their utility in developing tools for software analysis. This new research direction leverages natural language prompting to allow LLMs to assist with developing SA tools that can operate in classified environments. In addition, it allows end users with minimal software experience to customize SA tools.

In our methodology, we input public (i.e., openly published) material related to software verification tasks into public LLMs, and used them to assist in the design, implementation, and customization of SA tools. We later reviewed and migrated the resulting tools to a classified environment. Needless to say, software tools developed using our approach must be reviewed as described in software security verification standards before being deployed in classified environments.

The specific policies for reviewing software before deployment on a classified system follow government regulations and are generally proportional to the level of required secu...