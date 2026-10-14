---
title: A Five-Step Framework to Sufficient Realism in Cyber Simulations
url: https://www.sei.cmu.edu/blog/a-five-step-framework-to-sufficient-realism-in-cyber-simulations/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-10-13
fetch_date: 2026-10-14T06:53:23.467908
---

# A Five-Step Framework to Sufficient Realism in Cyber Simulations

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
4. A Five-Step Framework to Sufficient Realism in Cyber Simulations

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Updyke, D., 2026: A Five-Step Framework to Sufficient Realism in Cyber Simulations. Software Engineering Institute blog, Accessed October 13, 2026, https://doi.org/10.58012/kpm5-2w04.

Copy

APA Citation

Updyke, D. (2026, October 13). A Five-Step Framework to Sufficient Realism in Cyber Simulations. Retrieved October 13, 2026, from https://doi.org/10.58012/kpm5-2w04.

Copy

Chicago Citation

Updyke, Dustin. "A Five-Step Framework to Sufficient Realism in Cyber Simulations." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, October 13, 2026. https://doi.org/10.58012/kpm5-2w04.

Copy

IEEE Citation

D. Updyke, "A Five-Step Framework to Sufficient Realism in Cyber Simulations," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 13-Oct-2026 [Online]. Available: https://doi.org/10.58012/kpm5-2w04. [Accessed: 13-Oct-2026].

Copy

BibTeX Code

```
@misc{updyke_2026,
author={Updyke, Dustin},
title={A Five-Step Framework to Sufficient Realism in Cyber Simulations},
month={Oct},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/kpm5-2w04},
url={https://doi.org/10.58012/kpm5-2w04},
note={Accessed: 2026-Oct-13}
}
```

Copy

# A Five-Step Framework to Sufficient Realism in Cyber Simulations

![](/media/images/thumb_big_d-updyke_blog_authors.max-180x180.format-webp.webp)

###### [Dustin D. Updyke](/authors/dustin-updyke)

###### October 13, 2026

##### PUBLISHED IN

[Cybersecurity Engineering](/blog/topics/cybersecurity-engineering/)

##### CITE

<https://doi.org/10.58012/kpm5-2w04>

Get Citation

##### SHARE

In late August 2026, the Army’s chief of Network Command (NETCOM) [announced](https://breakingdefense.com/2026/08/army-network-needs-digital-twin-for-training-testing-cybersecurity-netcom-chief/) that to take full advantage of artificial intelligence (AI), the Army needed a comprehensive simulation of its networks. While acknowledging the difficulty in building a digital twin, Maj. Gen. Jacqueline Denise McPhail stated in *Breaking Defense* that a simulation would create “[an ultra-realistic training ground for network operators, cyber defenders, and AI algorithms on how the network works and how to keep it working, even when under attack](https://breakingdefense.com/2026/08/army-network-needs-digital-twin-for-training-testing-cybersecurity-netcom-chief/).”

Since 2017, the SEI has been developing and expanding the [GHOSTS framework](https://github.com/cmu-sei/GHOSTS) as a platform for simulating complex human, organizational, and machine behavior for cyber-training simulations. It began with simulated users operating real applications on hosts, producing the traffic, logs, files, browser history, and other artifacts defenders expect to encounter. It has since expanded into social and cognitive simulation, where actors communicate, form relationships, hold knowledge and beliefs, make decisions, and affect one another across a scenario—including through social influence, information propagation, trust, and the ways those interactions can change behavior and decision-making over time.

GHOSTS does not attempt to reproduce an entire operational environment. It models the parts needed to support a particular experiment, exercise, or mission rehearsal. A complete representation is expensive to build, difficult to validate, and often unnecessary. At the same time, omitting the wrong thing can undermine the event even when everything else is modeled well.

Digital twins re-expose an enduring simulation-design problem: How much of the operational environment actually needs to be reproduced? Every added system, behavior, and dependency increases cost and complexity. GHOSTS approaches the problem from the other direction, focusing on the human and organizational activity needed to make mission-relevant parts of the environment behave realistically. The question is not whether a simulation perfectly duplicates reality, but which parts of reality must hold up for the mission at hand. This is analogous, in the context of test and evaluation, to the concept of [*mission assurance*](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/302045p.pdf).

This blog post, adapted from [a recently published report](https://www.sei.cmu.edu/library/a-decade-of-ghosts-in-the-machine-from-cyber-range-realism-to-cognitive-mission-rehearsal/), layers a philosophical perspective onto the engineering problems of sufficient realism in cyber simulations and proposes a five-step framework for determining the needed realism of a simulated environment.

## Defining Realism

A common question we encounter among our mission partners is *How do you know what is realistic?*

More generally, *do we need to accurately model all aspects of the real operating environment?* For years, CERT has operated simulated environments for training, exercise, war gaming, and mission rehearsal, and keeps arriving at the same conclusion: Realism is tied to exercise validity and value. Dobson built that conclusion into the [R-EACTR framework](https://www.sei.cmu.edu/library/r-eactr-a-framework-for-designing-realistic-cyber-warfare-exercises/) where the premise is that an exercise is valuable to the degree it feels real, and so realism belongs within every design decision that brings that exercise to life. The [first GHOSTS technical report](https://doi.org/10.1184/R1/12363029.v1), published in 2018, confirmed that participants who rated the exercise more realistic also rated the training more valuable. GHOSTS grew from there as machinery to simulate a realistic environment inhabited by people performing activities that we would expect, given their role in an organization.

Out of this background and experience came *sufficient realism*. “[Train as you fight](https://www.army.mil/article/189059/train_as_you_fight_fight_as_you_train)” is a common phrase in military operations, and it sets a bar for training, exercise, and simulation. Otherwise, if the terrain, tools, or processes that a team trains with are significantly different from real-world operations, is it really a valid mission rehearsal? At the same time, cost, timing, and other constraints can often put full fidelity out of reach. Sufficient realism is the working answer to that tension—enough of the right factors in the environment, at the right fidelity, for the mission being rehearsed. Sufficient realism overlaps with many of the concerns captured by R-EACTR, and, in an exercise, resembles a reasonable and consistent storyline, realistic tactical maneuvers, defined rules of engagement, and authorization for action.

Military simulation has dealt with a closely related problem before. The [SIMNET](https://www.iitsec.org/-/media/sites/iitsec/link-attachments/iitsec-fellows/2015_fellowpaper_miller.ashx) [Program](https://www.princeton.edu/~ota/disk1/1995/9512/951203.PDF) called its approach *selective fidelity*. Rather than reproduce a tank in complete physical detail, SIMNET began with the tasks soldiers needed to perform and included the controls, cues, and dynamics required to produce those training behaviors. Its designers could omit a functional bilge-pump switch because it contributed nothing to platoon- or company-level tactical training, while seemingly minor cues such as seat rumble and visual movement mattered because crews used them to judge speed and terrain.

Sufficient real...