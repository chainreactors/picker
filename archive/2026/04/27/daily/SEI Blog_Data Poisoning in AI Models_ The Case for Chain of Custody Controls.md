---
title: Data Poisoning in AI Models: The Case for Chain of Custody Controls
url: https://www.sei.cmu.edu/blog/data-poisoning-in-ai-models-the-case-for-chain-of-custody-controls/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-04-27
fetch_date: 2026-04-28T05:28:24.058845
---

# Data Poisoning in AI Models: The Case for Chain of Custody Controls

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
4. Data Poisoning in AI Models: The Case for Chain of Custody Controls

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Metcalf, R., and Churilla, M., 2026: Data Poisoning in AI Models: The Case for Chain of Custody Controls. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed April 27, 2026, https://doi.org/10.58012/25yz-9b86.

Copy

APA Citation

Metcalf, R., & Churilla, M. (2026, April 27). Data Poisoning in AI Models: The Case for Chain of Custody Controls. Retrieved April 27, 2026, from https://doi.org/10.58012/25yz-9b86.

Copy

Chicago Citation

Metcalf, Renae, and Matt Churilla. "Data Poisoning in AI Models: The Case for Chain of Custody Controls." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, April 27, 2026. https://doi.org/10.58012/25yz-9b86.

Copy

IEEE Citation

R. Metcalf, and M. Churilla, "Data Poisoning in AI Models: The Case for Chain of Custody Controls," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 27-Apr-2026 [Online]. Available: https://doi.org/10.58012/25yz-9b86. [Accessed: 27-Apr-2026].

Copy

BibTeX Code

@misc{metcalf\_2026,
author={Metcalf, Renae and Churilla, Matt},
title={Data Poisoning in AI Models: The Case for Chain of Custody Controls},
month={{Apr},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/25yz-9b86},
note={Accessed: 2026-Apr-27}
}

Copy

# Data Poisoning in AI Models: The Case for Chain of Custody Controls

![Headshot of Renae Metcalf.](/media/images/kmetcalf.max-180x180.format-webp.webp)
![Headshot of Matthew Churilla.](/media/images/Churilla_Matthew_349_230628.max-180x180.format-webp.webp)

###### [Renae Metcalf](/authors/renae-metcalf) and [Matt Churilla](/authors/matthew-churilla)

###### April 27, 2026

##### PUBLISHED IN

[Securing AI](/blog/topics/securing-ai/)

##### CITE

<https://doi.org/10.58012/25yz-9b86>

Get Citation

##### TAGS

[Machine Learning](/blog/tags/machine-learning)
[AISIRT](/blog/tags/aisirt)

##### SHARE

If a machine learning model is trained on 50,000 images, an attacker need alter only 50 of them, or [0.1 percent of the training data](https://www.usenix.org/system/files/sec21-carlini-poisoning.pdf), to achieve a data poisoning attack. Consider a data curation pipeline involving a drone camera that captures images and stores them on disk, (data generation and storage). These images are labeled and split into datasets (data curation), and a machine learning model is then trained using these datasets (model training). This pipeline involves multiple instances where data is at rest or in transit and presumes the involvement of multiple people (perhaps one person to curate the data and another to train the model). Each instance presents an opportunity to alter the data while each person involved presents a potential insider threat. For example, an [on-path attacker](https://www.cloudflare.com/learning/security/threats/on-path-attack/) could modify the images when they are transferred from the drone to be curated, or after the data is labeled, the attacker could modify some labels, leaving the images themselves unaltered.

Data poisoning occurs when an insider or adversary modifies training data to influence the performance or operation of a model. As artificial intelligence (AI) has proliferated, corresponding security mechanisms have not kept up, leaving vulnerabilities, including in the data used to train the model. However, lessons gained from decades of experience in data protection can be applied to AI.

Organizations without mechanisms to detect or prevent data poisoning are open to an avenue of attack that is difficult to mitigate once it has succeeded. While there is [burgeoning research in machine unlearning](https://arxiv.org/abs/2406.09073), which could be used to recover from a data poisoning attack if you know what was poisoned, it is still more effective to retrain the model, a task itself that is extremely expensive. Since recovery is meager at best, prevention is the optimal approach. Nowadays, as we see threat actors looking to influence models and degrade the trust of users through incorrect behaviors, preventing data poisoning is [more important than ever](https://www.crn.com/news/ai/2024/the-ai-danger-zone-data-poisoning-targets-llms).

We propose being *proactive* with [chain of custody](https://en.wikipedia.org/wiki/Chain_of_custody) controls. This is because probabilistic methods to retroactively check whether data was tampered with are becoming less effective. *Chain of custody*, the documentation of who possesses an object and when, is a concept primarily applied to legal evidence, but it has application to other domains. This post describes data poisoning and proposes cryptographic chain of custody as a mitigating solution.

## Data Poisoning

[Data poisoning is an attack against the machine learning model](https://doi.org/10.58012/jrjp-n210) that powers an AI system. The methodology of this attack is to subtly modify the data or labels used to train the model. An adversary can utilize data poisoning to influence or degrade model performance, leading to [bias](https://www.ibm.com/think/topics/data-bias), overlooked issues, and the introduction of software vulnerabilities

As the size of models and datasets exceeds the capability of people to label data, machine learning has moved from supervised learning to semi-supervised learning. In supervised learning, all training data is labeled whereas in semi-supervised learning, [only some of the training data is labeled. The rest of the data supports the training process](https://www.ibm.com/think/topics/semi-supervised-learning) by enabling the model to encompass patterns in data. LLM training, for example, is generally unsupervised, detecting patterns in the training data that guide the predictive generation process. Regardless, the machine learning training process typically relies on large amounts of data, and only a small fraction of that data need be malicious to achieve a data poisoning attack.

Data curation encompasses “[all the processes needed for principled and controlled data creation, maintenance, and management, together with the capacity to add value to data](https://dl.acm.org/doi/proceedings/10.5555/2726970).” It can be an extremely difficult and time-consuming process when humans must review, verify, and label each data item. Due to the rapid pace of data development and the lack of data journaling software, organizations need to keep accurate logs of data manipulation and access.

## Cryptographic Chain of Custody

Chain of custody is not a new topic; it is used in the legal realm to provide a paper trail for evidence and records. The documentation and control verification processes used in chain of custody management has made its way into other fields, such as [digital forensics](https://par.nsf.gov/servlets/purl/10620995) and supply chain management. Nonetheless, keeping detailed records of data is only part of the solution.

In our previous work, [*AI Hygiene Starts with Models and Data Loaders*](https://www.sei.cmu.edu/library/ai-hygiene-starts-with-models-and-data-loaders/), we explored the value of traditional cybersecurity methods to secure AI systems. As part of that work, we described how cryptographic methods can be leveraged to provide robustness in the presence of an adversary. Use of checksums an...