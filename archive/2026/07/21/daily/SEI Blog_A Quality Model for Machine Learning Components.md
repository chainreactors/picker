---
title: A Quality Model for Machine Learning Components
url: https://www.sei.cmu.edu/blog/a-quality-model-for-machine-learning-components/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-07-21
fetch_date: 2026-07-22T05:04:19.486163
---

# A Quality Model for Machine Learning Components

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
4. A Quality Model for Machine Learning Components

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Lewis, G., Brower-Sinning, R., Derr, A., Ozkaya, I., and Echeverría, S., 2026: A Quality Model for Machine Learning Components. Software Engineering Institute blog, Accessed July 21, 2026, https://doi.org/10.58012/bzpa-f838.

Copy

APA Citation

Lewis, G., Brower-Sinning, R., Derr, A., Ozkaya, I., & Echeverría, S. (2026, July 21). A Quality Model for Machine Learning Components. Retrieved July 21, 2026, from https://doi.org/10.58012/bzpa-f838.

Copy

Chicago Citation

Lewis, Grace, Rachel Brower-Sinning, Alex Derr, Ipek Ozkaya, and Sebastián Echeverría. "A Quality Model for Machine Learning Components." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, July 21, 2026. https://doi.org/10.58012/bzpa-f838.

Copy

IEEE Citation

G. Lewis, R. Brower-Sinning, A. Derr, I. Ozkaya, and S. Echeverría, "A Quality Model for Machine Learning Components," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 21-Jul-2026 [Online]. Available: https://doi.org/10.58012/bzpa-f838. [Accessed: 21-Jul-2026].

Copy

BibTeX Code

```
@misc{lewis_2026,
author={Lewis, Grace and Brower-Sinning, Rachel and Derr, Alex and Ozkaya, Ipek and Echeverría, Sebastián},
title={A Quality Model for Machine Learning Components},
month={Jul},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/bzpa-f838},
url={https://doi.org/10.58012/bzpa-f838},
note={Accessed: 2026-Jul-21}
}
```

Copy

# A Quality Model for Machine Learning Components

![Headshot of Grace Lewis.](/media/images/Lewis_Grace_095_2022.max-180x180.format-webp.webp)
![Headshot of Rachel Brower-Sinning.](/media/images/thumb_big_r-browersinning_blog_.max-180x180.format-webp.webp)

###### [Grace Lewis](/authors/grace-lewis), [Rachel Brower-Sinning](/authors/rachel-brower-sinning), [Alex Derr](/authors/alex-derr), [Ipek Ozkaya](/authors/ipek-ozkaya), and [Sebastián Echeverría](/authors/sebastian-echeverria)

###### July 21, 2026

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/bzpa-f838>

Get Citation

##### SHARE

[![Screenshot 2026-07-21 at 11.11.49 AM](/media/images/Screenshot_2026-07-21_at_11.11.max-1280x720.format-webp.webp)](/media/images/Screenshot_2026-07-21_at_11.11.49AM.original.png)

Despite increased adoption and advances in machine learning (ML), [studies](https://www.rand.org/pubs/research_reports/RRA2680-1.html) show that often [ML projects do not reach the production stage](https://www.forbes.com/sites/andreahill/2025/08/21/why-95-of-ai-pilots-fail-and-what-business-leaders-should-do-instead/) because they do not fit into the overall business workflow and context, or the use case is not well understood. As such, testing ML components is still largely limited to model properties, such as accuracy, with limited consideration of requirements derived from the system or workflow it will be a part of, such as throughput, resource consumption, or robustness. This limited view of testing can lead to failures in model integration, deployment, and operations.

In traditional software development, quality models, such as [ISO 25010](https://www.iso.org/standard/78176.html), provide a widely used structured framework to assess software quality, define quality requirements, and provide a common language for communication with stakeholders. A newer standard, [ISO 25059](https://www.iso.org/standard/80655.html), defines a more specific quality model for AI systems. However, a problem with this standard is that it combines system attributes with ML component attributes, which is not helpful for a model developer or evaluator, as many system attributes cannot be assessed at the component level. In this blog post, adapted from [a recently published paper](https://arxiv.org/pdf/2602.05043), we present a quality model for ML components that serves as a guide for requirements elicitation and negotiation.

[![figure1_07202026](/media/images/figure1_07202026.max-1280x720.format-webp.webp)](/media/images/figure1_07202026.original.png)

Figure 1: Quality Model for ML Components

##

By developing a quality model specifically for ML components, developers, evaluators, acquirers, and stakeholders can draw upon the model’s quality attributes (QAs) and definitions to establish a common vocabulary for defining system- and mission-derived requirements and focus testing efforts accordingly.

* **Behavior Analysis**: QAs related to ease of observing and analyzing ML component behavior at development time and run time.
  + **Analyzability.** Capability of an ML component to expose attributes that enable it to be effectively and efficiently assessed regarding its behavior or the impact of an intended change, to diagnose it for deficiencies or causes of failure, or to identify sub-components to be modified.
  + **Monitorability.** Capability of an ML component to produce data that can be used to measure runtime attributes (e.g., performance degradation, latency) that can effectively be observed and used by the ML-enabled system or operator to take action aligned with requirements.
  + **Testability.** Capability of an ML component to support testing against expected behaviors by offering information relevant to test results or ensuring the visibility of failures.
  + **Understandability.** Ease with which the code, implementation choices, and design choices of an ML component can be understood.

* **Confidence**: QAs related to producing information that increases insight into the model and its outputs.
  + **Explainability.** Capability of an ML component to provide information that can explain model outputs (decisions) in human terms.
  + **Functional Correctness**. Capability of an ML component to meet system-derived correctness or model performance requirements.
  + **Interpretability.** Capability of an ML component to be transparent in its execution and produce information concerning the relationship between inputs and outputs.

* **Consistency**: QAs related to producing consistent results over time.
  + **Repeatability**. Capability of an ML component to produce equivalent results when run on equivalent inputs during inference time.
  + **Reproducibility**. Capability of the training algorithm for the ML model to produce functionally-equivalent ML models when run on similar datasets during training time.

* **Continued Operation**: QAs related to providing continued operation within specified boundaries and constraints.
  + **Deployability**. Capability of an ML component to be deployed into production when needed, without any unanticipated side effects and within specified resource and time constraints.
  + **Resilience** Capability of an ML component to provide and maintain an acceptable level of service in the face of technical challenges to normal operation.
  + **Reliability.** Capability of an ML component to perform specified functions without failure under normal operation.
  + **Resource Utilization.** Capability of an ML component to use no more than the specified amount of resources to perform its function.
  + **Robustness.** Capability of an ML component to preserve its level of functional correctness under specified fault modes or conditions.
  + **Time Behavior.** Capability of an ML component to produce outputs within required response time and throughput rates.

* **Maintenance and Evolution**: QAs related to ease of maintaining a...