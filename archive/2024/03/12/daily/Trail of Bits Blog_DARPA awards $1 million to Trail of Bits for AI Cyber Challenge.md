---
title: DARPA awards $1 million to Trail of Bits for AI Cyber Challenge
url: https://blog.trailofbits.com/2024/03/11/darpa-awards-1-million-to-trail-of-bits-for-ai-cyber-challenge/
source: Trail of Bits Blog
date: 2024-03-12
fetch_date: 2025-10-04T12:12:17.805469
---

# DARPA awards $1 million to Trail of Bits for AI Cyber Challenge

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# DARPA awards $1 million to Trail of Bits for AI Cyber Challenge

Michael D. Brown

March 11, 2024

[aixcc](/categories/aixcc/)

We’re excited to share that [Trail of Bits has been selected](https://www.darpa.mil/news-events/2024-03-11b) as one of the seven exclusive teams to participate in the small business track for DARPA’s AI Cyber Challenge (AIxCC). Our team will receive a $1 million award to create a Cyber Reasoning System (CRS) and compete in the [AIxCC](https://aicyberchallenge.com/) Semifinal Competition later this summer. This recognition not only highlights our dedication to advancing cybersecurity but also marks a significant milestone in our journey in pioneering solutions that could shape the future of AI-driven security. Our involvement in the AIxCC represents a step forward in our commitment to pushing the boundaries of what’s possible, envisioning a future where cybersecurity challenges are met with innovative, AI-powered solutions.

![](/img/wpdump/2e2d6fb6c4632067df1ce00e0f9ecec5.jpg)

It’s official: Trail of Bits was selected as one of the seven exclusive teams for the AIxCC small business track.

As we move beyond the initial phase of the competition, we’re eager to offer a sneak peek into the driving forces behind our approach, without spilling all of our secrets, of course. In a field where competitors often hold their cards close to their chests, we at Trail of Bits believe in the value of openness and sharing. Our motivation stems from more than just the desire to compete; it’s about contributing to a broader understanding and development within the cybersecurity community. While we navigate through this challenge with an eye on victory, our aim is also to foster a culture of transparency and collaboration, aligning with our deep-rooted open-source ethos.

For background on the challenge, see our two previous posts on the AIxCC:

* [DARPA’s AI Cyber Challenge: We’re In!](https://blog.trailofbits.com/2023/12/14/darpas-ai-cyber-challenge-were-in/)
* [Our thoughts on AIxCC’s competition format](https://blog.trailofbits.com/2024/01/18/our-thoughts-on-aixccs-competition-format/)

*\*\*\* **Disclaimer:** Information about AIxCC’s rules, structure, and events referenced in this document are subject to change. This post is **NOT** an authoritative document. Please refer to DARPA’s website and official documents for first-hand information. \*\*\**

> Congrats to the 7 companies that will receive $1 million each to develop AI-enabled cyber reasoning systems that automatically find and fix software vulnerabilities as part of the [#AIxCC](https://twitter.com/hashtag/AIxCC?src=hash&ref_src=twsrc%5Etfw) Small Business Track! Full announcement: <https://t.co/SC6yEFsooy>. [pic.twitter.com/MRt3eoNuJd](https://t.co/MRt3eoNuJd)
>
> — DARPA (@DARPA) [March 11, 2024](https://twitter.com/DARPA/status/1767233220414779464?ref_src=twsrc%5Etfw)

## The guiding principles for building our CRS

In addition to competing in the AIxCC’s spiritual predecessor, the [Cyber Grand Challenge (CGC)](https://blog.trailofbits.com/category/cyber-grand-challenge/), our team at Trail of Bits has been working to apply AI/ML techniques to critical cybersecurity problems for many years. These experiences have heavily influenced our approach to the AIxCC. While we’ll be waiting until later in the competition to share specific details, we would like to share the guiding principles for building our AI/ML-driven CRS that have come from this work:

### CRS architecture is key to achieving scalability, resiliency, and versatility

DARPA’s CGC, like the AIxCC, tasked competitors with developing CRSs that find vulnerabilities at scale (i.e., that scan many challenge programs in a limited period of time) without any human intervention. The CRS Trail of Bits created to compete in the CGC, [Cyberdyne](https://github.com/trailofbits/publications/blob/master/papers/cyberdyne.pdf), addressed these problems with a distributed system architecture. Cyberdyne provisioned many independent nodes, each capable of performing key tasks such as fuzzing and symbolic execution. Each node was tasked with one or more challenge problems, and could even cooperate with other nodes on the same challenge.

This design had several advantages. First, the CRS maximized coverage of the 131 challenges via parallel processing. This allowed the CRS to both achieve the scale needed to succeed in the competition and avoid being bogged down with particularly challenging problems. Second, the CRS was resilient to localized failures. If nodes experienced a catastrophic error while analyzing a challenge problem, the operation of other independent nodes was not affected, limiting the damage to the CRS’s overall score. The care taken in this design paid off in the competition: Cyberdyne ranked second among all CRSs in terms of the total number of verified bugs found!

The format of the AIxCC bears a strong resemblance to that of the CGC, so the CRS we build for the AIxCC will also need to be scalable and resilient to failures. However, the AIxCC has an additional wrinkle—challenge diversity. The AIxCC’s challenge problem set will include programs written in languages other than C/C++, including many interpreted languages such as Java and Python. This will require a successful CRS to be highly versatile. Fortunately, the distributed architecture used in Cyberdyne can be adapted for the AIxCC to address versatility in a manner similar to scalability and resiliency. The key difference is that problem-solving nodes used for AIxCC challenges will need to be specialized for different types of challenge problems.

### AI/ML is best for complementing conventional techniques, not replacing them

I, along with my co-authors from Georgia Tech, recently presented work at the USENIX Security Symposium on an ML-based static analysis tool we built called [VulChecker](https://www.usenix.org/conference/usenixsecurity23/presentation/mirsky). VulChecker uses graph-based ML algorithms to locate and classify vulnerabilities in program source code. We evaluated VulChecker against a commercial static analysis tool and found that VulChecker outperformed the commercial tool at detecting certain vulnerability types that rule-based tools typically struggle with, such as integer overflow/underflow vulnerabilities. However, for vulnerabilities that are amenable to rule-based checks (e.g., stack buffer overflow vulnerabilities), VulChecker was effective but did not outperform conventional static analysis.

Considering that rule-based checks are generally less costly to implement than ML models, it doesn’t make sense to replace conventional analysis entirely with AI/ML. Rather, AI/ML is best suited to complement conventional approaches by addressing the problem instances that they struggle with. In the context of the AIxCC, our experience suggests that an AI/ML-only approach is a losing proposition due to high compute costs and the effect of compounding false positives, inaccuracies, and/or confabulations at each step. With that in mind, we plan to use AI/ML in our CRS only where it is best suited or where no conventional options exist. For now, we are planning to use AI/ML approaches primarily for vulnerability detection/classification, patch generation, and input generation tasks in our CRS.

### Use the right AI/ML models for the job!

LLMs have been demonstrated to have many emergent capabilities due to the sheer size of their training sets. Among the tasks a CRS must complete in the AIxCC that are suitable for AI/ML, several are tailor-made for LLMs, such as generating code snippets and seed inputs for fuzzing. However, based on our past research, we’ve found that LLMs may not actually be the best option for such tasks.

Last fall, our team supported the [United Kingdom’s Frontier AI Taskforce](https://www.go...