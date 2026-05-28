---
title: Expecting the Unexpected: Monitoring for Drift in ML Systems
url: https://www.sei.cmu.edu/blog/expecting-the-unexpected-monitoring-for-drift-in-ml-systems/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-05-27
fetch_date: 2026-05-28T06:03:41.731729
---

# Expecting the Unexpected: Monitoring for Drift in ML Systems

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
4. Expecting the Unexpected: Monitoring for Drift in ML Systems

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Schumock, G., and Walsh, M., 2026: Expecting the Unexpected: Monitoring for Drift in ML Systems. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed May 28, 2026, https://doi.org/10.58012/ds0g-4e06.

Copy

APA Citation

Schumock, G., & Walsh, M. (2026, May 27). Expecting the Unexpected: Monitoring for Drift in ML Systems. Retrieved May 28, 2026, from https://doi.org/10.58012/ds0g-4e06.

Copy

Chicago Citation

Schumock, Grant, and Matt Walsh. "Expecting the Unexpected: Monitoring for Drift in ML Systems." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, May 27, 2026. https://doi.org/10.58012/ds0g-4e06.

Copy

IEEE Citation

G. Schumock, and M. Walsh, "Expecting the Unexpected: Monitoring for Drift in ML Systems," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 27-May-2026 [Online]. Available: https://doi.org/10.58012/ds0g-4e06. [Accessed: 28-May-2026].

Copy

BibTeX Code

@misc{schumock\_2026,
author={Schumock, Grant and Walsh, Matt},
title={Expecting the Unexpected: Monitoring for Drift in ML Systems},
month={{May},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/ds0g-4e06},
note={Accessed: 2026-May-28}
}

Copy

# Expecting the Unexpected: Monitoring for Drift in ML Systems

![Headshot of Grant Schumock.](/media/images/Schumock_Grant_519_240530.max-180x180.format-webp.webp)
![Headshot of Matthew Walsh.](/media/images/Walsh_Matthew_039_240429.360x36.max-180x180.format-webp.webp)

###### [Grant Schumock](/authors/grant-schumock) and [Matt Walsh](/authors/matthew-walsh)

###### May 27, 2026

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/ds0g-4e06>

Get Citation

##### SHARE

Imagine the following scenario: you and a team of cyber experts have been tasked with protecting your organization from cyberattacks. You’ve developed a machine learning (ML) model to screen incoming and outgoing traffic. You feel you can rest easy, as your model achieves near-perfect performance during test and evaluation. One day, you are awakened by a frantic call from your CEO—your customers’ private data have been leaked. *How could this happen?* you think to yourself, as you begin investigating why your model failed to stop this attack.

This situation is not merely hypothetical. Studies have found that models that were once highly effective at detecting malicious activity become significantly less effective as attack patterns evolve (in [Android applications](https://ieeexplore.ieee.org/abstract/document/10935015), [encrypted traffic](https://www.sciencedirect.com/science/article/pii/S1389128623000932), [and](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/jordaney) [malware](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/jordaney)). As ML and other artificial intelligence (AI) models become pervasive, it is increasingly important to ensure these models continue to perform well when deployed. For cybersecurity models, this means they should be able to adapt to counter intelligent adversaries as they evolve their techniques. Continuously monitoring performance for signs of **drift** and retraining, when necessary, can be essential to avoid significant and costly losses.

At the Software Engineering Institute (SEI), we have [a long history of work](https://www.sei.cmu.edu/divisions/cert/#history) at the forefront of cybersecurity and machine learning, from establishing [C/C++ secure coding standards](https://cmu-sei.github.io/secure-coding-standards/sei-cert-cpp-coding-standard/) to founding the first [AI security incident response team](https://www.sei.cmu.edu/history-of-innovation/aisirt/). While ML is a potentially transformative technology for securing information systems, the cyber landscape is ever changing because the behaviors of users, attackers, and information systems evolve over time. If not addressed, these changes can degrade the performance of even the best ML-based defenses. Measures need to be in place to detect and respond to drift before real-world harms are enacted.

In this post, we describe what causes drift, discuss how to detect it, and provide a case study.

## What Is Drift?

Things change over time. Hardware and software systems are updated, humans adopt new behaviors, and environments shift. Adversaries adapt their tactics. Changes that affect data used or predicted by an ML model are called drift. There are three primary types of drift: *data drift, concept drift*, and *label drift*. We illustrate these using an ML-based email classifier as an example:

[![Picture1_05272026](/media/images/Picture1_05272026.max-1280x720.format-webp.webp)](/media/images/Picture1_05272026.original.png)

*Concept drift* is defined by changes in the relationships between features and outcomes. Concept drift can be particularly problematic because the learned relationship between features and outcomes may no longer hold. Concept drift is highly relevant in settings where adversarial actions are common. When adversaries aim to evade detection, they may modify their behaviors, for example to better mimic benign users. For example, adversaries sending phishing emails may discover emails containing hyperlinks are blocked by our phishing classifier model. To circumvent this, adversaries may stop including hyperlinks in phishing emails, altering the relationship between hyperlink-containing text and the probability an email is a phishing attempt (Figure 1, Panel A).

*Data drift*—sometimes called feature or covariate drift—refers to changes in the distributions of one or more features over time. Data drift alone does not affect relationships between features and outcomes. For a classifier, data drift occurs when something affects all classes equally. For our email classifier, benign and phishing emails incorporating text written by large language models (LLMs) could cause data drift by reducing the average number of typos in the text (Figure 1, Panel B).

*Label drift* refers to changes in the distribution of outcomes. For classifier models, label drift indicates the proportion of observations in each class has changed. Label drift can negatively impact classification models that are sensitive to class imbalances. For the phishing email classifier, a change in the proportion of emails that are phishing attempts would be an example of label drift (Figure 1, Panel C).

[![figure1_05272026](/media/images/figure1_05272026.max-1280x720.format-webp.webp)](/media/images/figure1_05272026.original.png)

Figure 1: Three primary types of drift: data drift, concept drift, and label drift illustrated using the example of a phishing email classifier.

These types of drift often co-occur. For example, a change in user behavior could affect the overall distribution of a feature (feature drift) as well as the relationship between that feature and the outcome class (concept drift). Because these different drift types can have varying impacts on production-level ML models, it is important to understand what types of drift are occurring.

## How Can We Detect Drift?

While drift can cause model performance degradation, there are te...