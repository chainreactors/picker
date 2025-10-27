---
title: Quantum Computing Needs More Software Engineers
url: https://buaq.net/go-241646.html
source: unSafe.sh - 不安全
date: 2024-05-27
fetch_date: 2025-10-06T16:49:05.123220
---

# Quantum Computing Needs More Software Engineers

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/8768ba8ddedffcf49fb16de0056615eb.jpg)

Quantum Computing Needs More Software Engineers

This article is inspired by the need for more Software Engineers in quantum computing. Not to mentio
*2024-5-26 23:0:12
Author: [hackernoon.com(查看原文)](/jump-241646.htm)
阅读量:5
收藏*

---

This article is inspired by the need for more Software Engineers in quantum computing. Not to mention the other Developers, UX Designers, QA Testers, Product Managers and all the rest of the talent that makes it possible to ship a real product to real customers. Especially products in Deep Tech and Frontier Tech like quantum computing.

These products and the teams attempting to create them are subject to a long and challenging [journey from "Science to Technology to Engineering to Product"](https://medium.com/%40hellodavidryan/how-do-we-think-about-products-in-deep-tech-a-suggested-framework-69e59419a1c6?ref=hackernoon.com). A series of phase shifts that are more about organisational (and community) evolution than just a linear progression through technology readiness.

This evolution doesn't just happen. For those of us working in these teams, we face the challenge of reinventing the organisation as it shifts from academic to technical to something more broadly engaged with the marketplace. Which means sourcing and collaborating with a growing community of talent as well as continually evolving and growing our own skills.

![](https://hackernoon.imgix.net/images/CKaVHZqE7ZR84bJkMLuXNRhCEdB2-fg93es5.jpeg?auto=format&fit=max&w=3840)

This was something I touched on in my "[Open Source Your Way into a Quantum Computing Career](https://www.youtube.com/watch?v=sXDva9Etw5A&ref=hackernoon.com)" talk back in 2022 at the Linux Foundation's Open Source Summit. And it's grown even further in the year or so since, with a noticeable industry shift toward "quantum utility" (a term we use to focus on real-world usefulness rather than [theoretical supremacy](https://www.sciencenews.org/article/google-quantum-supremacy-claim-controversy-top-science-stories-2019-yir?ref=hackernoon.com)) and some massive projects kicking off. Such as the Australian government's [nearly $1B investment in PsiQuantum](https://www.abc.net.au/news/2024-04-30/australia-signs-deal-for-first-useful-quantum-computer/103781352?ref=hackernoon.com) setting up a commercial quantum computer back in my home town of Brisbane (said with a little homesickness from here in Seattle).

So yes, there is a lot going on. Which makes this is a very good time to understand what these quantum systems are actually composed of and where your talent and curiosity fits in. I've included some recommendations at the end for how to get involved. And I should add a quick disclaimer that there's not really one "quantum computer" paradigm. I've abstracted the most common elements of the various systems we work on for educational value, but welcome any challenges or rebuttals as this model evolves over time.

## The quantum stack at a glance

In many ways the quantum computing stack matches the pattern of a modern high-performance computing (HPC) stack. And to a lesser degree will be familiar enough to anyone working in the cloud computing space. We go from a high-level user experience down to some form of platform that takes our workload and converts it to something that will then run on the hardware. Simple enough to get our head around.

The nuance is a lot more complicated. Such as understanding that a quantum computer is only really as good as the quantum algorithm being used. All the fancy stuff you've heard about [superposition](https://scienceexchange.caltech.edu/topics/quantum-science-explained/quantum-superposition?ref=hackernoon.com) and [entanglement](https://scienceexchange.caltech.edu/topics/quantum-science-explained/entanglement?ref=hackernoon.com) really just comes down to a way to reliably run some useful algorithms that, on a hardware level, [uses phase and interference](https://www.wolframcloud.com/objects/summerschool/pages/2017/JacobMarks_TE?ref=hackernoon.com) to perform the "computation" that spits out a probability of the right answer. Doing this a lot creates a greater likelihood of the right answer. Doing this at all requires a useful algorithm and a reliable system implementation.

Simulation also plays a crucial role. You might see this talked about as having to do with "saving from expensive hardware purchases", but this isn't really the case (and often a clue someone is just using AI to write their quantum clickbait). We rely on simulation to not only help develop new and interesting algorithms, but to explore the various ways to set up a workload. It's also a core part of the workflows many of us are building towards, where a truly hybrid system would use classical computing resources to handle the workload and scheduling, along with acceleration via GPUs (or newer chips like [TPUs](https://cloud.google.com/blog/products/ai-machine-learning/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu?ref=hackernoon.com) and [LPUs](https://wow.groq.com/lpu-inference-engine/?ref=hackernoon.com)), and effectively push certain workloads to the quantum processing unit (QPU) where a quantum algorithm may be useful to the task at hand. While some, like myself, are focused on integrating quantum computing with existing infrastructure, others are dedicated to building the most powerful standalone quantum system. Hence the wide range of exploration in the industry.

If all you take away from this is that a quantum computer is a specialised system that includes a QPU in additional to the existing compute stack to run specialised quantum algorithms then that's a win. No cats, slits, or spooky hand-waving required.

![](https://hackernoon.imgix.net/images/CKaVHZqE7ZR84bJkMLuXNRhCEdB2-c2a3er6.jpeg?auto=format&fit=max&w=3840)

## The quantum stack in detail

The following sections move from the top user layer down through the platform, and ultimately into the hardware layer. While the boundaries between these layers can be blurred in practice, we'll follow a model based on a typical workload or workflow for clarity (and sanity).

### 1. Quantum programming languages and developer tools

At the highest level of the quantum system is the human punching away at the keyboard. Quantum programming languages provide the high level of abstraction required for exploring quantum algorithms and creating programs in a manageable form. The experience of working with these languages is expanded by Software Development Kits (SDKs) that offer the libraries and tools required to develop quantum software.

There is some blurring of the distinction between SDKs and frameworks and Integrated Development Environments (IDEs). This is shaped by the diverse approaches of quantum vendors and the integration of platforms and product verticals tailored to specific end-users. A researcher wanting full local access and pulse level control will differ from an enterprise team developing hybrid workloads, which will differ from a fintech startup building on top of a cloud-based quantum platform. This pattern is familiar in enterprise or cloud-based projects, but it will evolve with nuances as the commercial value of quantum systems becomes more apparent and influences product design. Meanwhile, the most prevalent SDKs and their associated programming languages are as follows.

* [IBM Quantum](https://www.ibm.com/quantum?ref=hackernoon.com) and (Python-based) [Qiskit](https://www.ibm.com/quantum/qiskit?ref=hackernoon.com)
* [Microsoft Quantum Development Kit (QDK)](https://learn.microsoft....