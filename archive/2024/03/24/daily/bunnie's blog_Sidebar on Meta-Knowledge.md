---
title: Sidebar on Meta-Knowledge
url: https://www.bunniestudios.com/blog/?p=7025
source: bunnie's blog
date: 2024-03-24
fetch_date: 2025-10-04T12:07:45.027457
---

# Sidebar on Meta-Knowledge

---

[« Name that Ware, March 2024](https://www.bunniestudios.com/blog/2024/name-that-ware-march-2024/)

[Designing The Light Source for IRIS »](https://www.bunniestudios.com/blog/2024/designing-the-light-source-for-iris/)

## Sidebar on Meta-Knowledge

[IRIS (Infra-Red, in-situ)](https://www.bunniestudios.com/blog/?p=6937) is a multidisciplinary project I’m developing to give people a tangible reason to trust their hardware.

[![](https://bunniefoo.com/iris/ir_sample2_sm.jpg)](https://bunniefoo.com/iris/ir_sample2.jpg)

*Above: example of IRIS imaging a chip mounted on a circuit board.*

When I set out to research this technique, there were many unknowns, and many skills I lacked to complete the project. This means I made many mistakes along the way, and had to iterate several times to reach the current solution.

Instead of presenting just the final solution, I thought it might be interesting to share some of the failures and missteps I made along the way. The propensity to show only final results can make technology feel less inclusive: if you aren’t already in the know, it’s easy to feel like everything is magic. Nothing can be farther from the truth.

This short “sidebar” post will wax philosophical and discuss my general methods for learning and exploration; if you have no interest in this topic, you can safely skip this post.

**The Rule of Three**

When I have no way to derive how many iterations it will take to get something right, I use the “rule of three”: generally, you can get somewhere interesting with three iterations of a methodical process. The rule of three has roots in the observation many natural phenomena can be described with relationships based on the [natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm), *e*. In particular, [diffusive processes](https://en.wikipedia.org/wiki/Diffusion) – that is, progress toward a goal that is driven by random walks over a concentration gradient – have shapes and time constants governed by this relationship. As a corollary it matters less the exact nature of the process, and more the magnitude and proximity of the realizable incentives to get it right.

![](https://bunniefoo.com/iris/2024/diffusion_bruceblaus.jpg)

*Image credit: [BruceBlaus](https://en.wikipedia.org/wiki/Diffusion#/media/File:Blausen_0315_Diffusion.png), CC-BY 3.0*

Such processes tend to get “63% of the way there” in the first interval, “86% of the way there” in the second interval, and “95% of the way there” by the third interval (these percentages correspond to inverse powers of *e*, that is: 63% ≈ 1 – *e*-1, 86% ≈ 1 – *e*-2, etc…). You can’t iterate to perfection, but 95% of the way there is usually good enough. So when I can’t find a better analysis to guide a process, I’ll apply the “rule of 3” to everything from project management for a complex system, to how many times I rinse a dish rag before I hang it to dry.

**Meta-knowledge: Knowing what You Know**

When it comes to planning a big project like IRIS, a realistic self-assessment improves my ability to estimate time and resource requirements; the rule of three only works if you’re realistic about what you can achieve with every iteration.

Thus, I have developed a series of criteria to keep myself grounded, and periodically I take some time to reflect and correct my behavior if it is out of line.

Here is my self-assessment criteria, presented as a series of statements I can make about my knowledge, followed by a set of tests I might use to prove the statement.

* **I am ignorant of it**: the concept does not exist in my consciousness; there’s an instinct to reject the possibility of its existence, especially if it is adjacent to something I already know well. The path to knowledge starts with recognizing ignorance; learning the smell of my own ignorance (that is, the instinct to reject or be incredulous) helps me get over this barrier faster.
* **I am aware of it**: I’ve heard enough about it that I can throw the term around in the right context and impress someone who hasn’t heard of it.
* **I know of it**: I’ve seen others do it, read some articles or papers about it, perhaps even played with a toy version of it and/or correctly answered basic questions about it.

Everyone is different, but this is roughly the level of knowledge I felt I had when I finished my basic undergraduate-level courses in university.

* **I have tried it out**: did a small “original” project with it, and it seemed to go OK. This is the point where it’s easy to fall into the trap of knowing enough to be dangerous, but not realizing it.

This is around the point I felt I got to after completing some thesis-level projects in university.

* **I know it**: did at least two projects with it, one of which I struggled to finish, because I hit a limit of the example code, API, or physics

This is roughly where I felt when I was as a junior professional in my first jobs out of college.

* **I know it well**: extended it with a previously unknown aspect, or built a version of it from near first-principles; can teach it to others, but pupils still come away overwhelmed by jargon. Usually requires at least one several-month period of not touching it, and then coming back to it before I can reach the next stage
* **I have mastered it**: knowing what I don’t know about it, and what it might take to figure out the missing bits; can correctly identify which problems it can be used to solve, and effectively solve them; able to use it as a reference to explore other less-known things; can readily extend it to meet other people’s needs; can offer a lucid and compact explanation of the topic to a beginner, without relying on jargon.

This is roughly what I would expect out of a senior professional or professor.

* **I am overfitting it**: using it to solve everything, and everything is solvable with it; learning new things is harder and riskier relative to converting all the problems into something solvable with it – so I stop learning new things and spend more of my time converting all problems into its domain. This is the point at which everything looks like a nail because you’ve got a really nice, fancy hammer and you can swing it like nobody else can.

Overfitting can happen at any stage of learning, but it tends to happen whenever you become the most skilled within a given peer group. It’s avoidable, but is often a terminal state of learning. Overfitting can prevent forward progress in other skills, because it can seem like there is no need to master any other technique since you’re already “the smartest person in the room”.

I find that the final stages of learning are a constant tension between overfitting and asymptotically approaching mastery; there is no clear answer as to when I’m overfitting or when I’m just judiciously applying a well-worn tool to a job. However, as a matter of habit, when I start to feel too comfortable with a tool or technique, I try to force myself out of my comfort zone and try something new, just to make sure I’m not overfitting.

There is a cost to this, however, since it almost always means passing up easy money or fame to make the time to explore. An excellent way to break the overfitting cycle is to create art. Art is a safer space for exploration; even technical failures, if sufficiently spectacular, may have artistic merit. I also learn a lot when I collaborate with artists, because they often see aspects of familiar topics that I’ve been blind to my entire life.

**Working within my Limitations**

Significantly, progress past the “**know it well**” stage often requires me to take a several month break from doing anything with the topic or tool. During this time, all my short-term memory of the subject is lost, so I have to re-acquire the knowledge when I return to the topic. Re-learning from experience is an important step because I get a fresh look on the topic. Because I’m already somewhat familiar with things, I have the surplus cognitive capacity...