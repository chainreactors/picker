---
title: Out of Distribution Detection: Knowing When AI Doesn’t Know
url: https://insights.sei.cmu.edu/blog/out-of-distribution-detection-knowing-when-ai-doesnt-know/
source: SEI Blog
date: 2025-06-10
fetch_date: 2025-10-06T22:57:34.820744
---

# Out of Distribution Detection: Knowing When AI Doesn’t Know

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
4. Out of Distribution Detection: Knowing When AI Doesn't Know

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Heim, E., and Frank, C., 2025: Out of Distribution Detection: Knowing When AI Doesn't Know. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed October 3, 2025, https://doi.org/10.58012/5e1y-zq76.

Copy

APA Citation

Heim, E., & Frank, C. (2025, June 9). Out of Distribution Detection: Knowing When AI Doesn't Know. Retrieved October 3, 2025, from https://doi.org/10.58012/5e1y-zq76.

Copy

Chicago Citation

Heim, Eric, and Cole Frank. "Out of Distribution Detection: Knowing When AI Doesn't Know." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, June 9, 2025. https://doi.org/10.58012/5e1y-zq76.

Copy

IEEE Citation

E. Heim, and C. Frank, "Out of Distribution Detection: Knowing When AI Doesn't Know," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 9-Jun-2025 [Online]. Available: https://doi.org/10.58012/5e1y-zq76. [Accessed: 3-Oct-2025].

Copy

BibTeX Code

@misc{heim\_2025,
author={Heim, Eric and Frank, Cole},
title={Out of Distribution Detection: Knowing When AI Doesn't Know},
month={{Jun},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/5e1y-zq76},
note={Accessed: 2025-Oct-3}
}

Copy

# Out of Distribution Detection: Knowing When AI Doesn't Know

![Headshot of Eric Heim.](/media/images/Heim_Eric_274_230629.max-180x180.format-webp.webp)
![Headshot of Cole Frank.](/media/images/Frank_Cole_136_240327.max-180x180.format-webp.webp)

###### [Eric Heim](/authors/eric-heim) and [Cole Frank](/authors/cole-frank)

###### June 9, 2025

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/5e1y-zq76>

Get Citation

##### SHARE

Imagine a military surveillance system trained to identify specific vehicles in desert environments. One day, this system is deployed in a snowy mountain region and begins misidentifying civilian vehicles as military targets. Or consider an artificial intelligence (AI) medical diagnosis system for battlefield injuries that encounters a novel type of wound it was never trained on, but it confidently—and incorrectly—recommends a standard treatment protocol.

These scenarios highlight a critical challenge in artificial intelligence: how do we know when an AI system is operating outside its intended knowledge boundaries? This is the critical domain of *out-of-distribution (OoD) detection*—identifying when an AI system is facing situations it wasn't trained to handle. Through our work here in the SEI’s AI Division, particularly in collaborating with the [Office of the Under Secretary of Defense for Research and Engineering (OUSD R&E)](https://www.cto.mil/) to establish the [Center for Calibrated Trust Measurement and Evaluation (CaTE)](https://insights.sei.cmu.edu/library/center-for-calibrated-trust-measurement-and-evaluation-categuidebook-for-the-development-and-tevv-of-laws-to-promote-trustworthiness/), we’ve seen firsthand the critical challenges facing AI deployment in defense applications.

The two scenarios detailed above aren’t hypothetical—they represent the kind of challenges we encounter regularly in our work helping the Department of Defense (DoD) ensure AI systems are safe, reliable, and trustworthy before being fielded in critical situations. As this post details, this is why we’re focusing on OoD detection: the crucial capability that allows AI systems to recognize when they’re operating outside their knowledge boundaries.

### Why Out-of-Distribution Detection Matters

For defense applications, where decisions can have life-or-death consequences, knowing when an AI system might be unreliable is just as important as its accuracy when it is working correctly. Consider these scenarios:

* autonomous systems that need to recognize when environmental conditions have changed significantly from their training data
* intelligence analysis tools that should flag unusual patterns, not force-fit them into known categories
* cyber defense systems that must identify novel attacks, not just those seen previously
* logistics optimization algorithms that should detect when supply chain conditions have fundamentally changed

In each case, failing to detect OoD inputs could lead to silent failures with major consequences. As the DoD continues to incorporate AI into mission-critical systems, OoD detection becomes a cornerstone of building trustworthy AI.

## What Does Out-of-Distribution Really Mean?

Before diving into solutions, let's clarify what we mean by *out-of-distribution*. *Distribution* refers to the distribution of the data that the model was trained on. However, it's not always clear what makes something *out* of a distribution.

In the simplest case, we might say new input data is OoD if it would have zero probability of appearing in our training data. But this definition rarely works in practice because most commonly used statistical distributions, such as the normal distribution, technically allow for any value, however unlikely. In other words, they have infinite [support](https://www.statlect.com/glossary/support-of-a-random-variable).

Out-of-distribution typically means one of two things:

1. The new input comes from a fundamentally different distribution than the training data. Here, fundamentally different means there is a way of measuring the two distributions as not being the same. In practice, though, a more useful definition is that when a model is trained on one distribution, it performs unexpectedly on the other distribution.
2. The probability of seeing this input in the training distribution is extremely low.

For example, a facial recognition system trained on images of adults might consider a child's face to be from a different distribution entirely. Or an anomaly detection system might flag a tank moving at 200 mph as having an extremely low probability in its known distribution of vehicle speeds.

## Three Approaches to OoD Detection

Techniques for OoD detection can be broadly categorized in three ways:

### 1. Data-Only Techniques: Anomaly Detection and Density Estimation

These approaches try to model what *normal* data looks like without necessarily connecting it to a specific prediction task. Typically this task is done using methods from one of two sub-domains:

**1)** **Anomaly detection** aims to identify data points that deviate significantly from what’s considered normal. These techniques can be categorized by their data requirements: supervised approaches that use labeled examples of both normal and anomalous data, semi-supervised methods that primarily learn from normal data with perhaps a few anomalies, and unsupervised techniques that must distinguish anomalies[1] without any explicit labels. Anomalies are defined as data that deviates significantly from the majority of previously observed data. In anomaly detection, deviates significantly is often left up to the assumptions of the technique used.

**2)** **Density estimation** involves learning a probability density function of training data that can then be used to assign a probability to any new instance of data. When a new input receives a very low probability, it's flagged as OoD. Density estimation is a classic problem in statistics.

While these approaches are conceptually straightforward and offer several mature techniques f...