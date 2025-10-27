---
title: We need a new way to measure AI security
url: https://blog.trailofbits.com/2023/03/14/ai-security-safety-audit-assurance-heidy-khlaaf-odd/
source: Trail of Bits Blog
date: 2023-03-15
fetch_date: 2025-10-04T09:34:43.947453
---

# We need a new way to measure AI security

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# We need a new way to measure AI security

Trail of Bits

March 14, 2023

[audits](/categories/audits/), [engineering-practice](/categories/engineering-practice/), [machine-learning](/categories/machine-learning/), [press-release](/categories/press-release/)

***Tl;dr:*** *Trail of Bits has launched a practice focused on machine learning and artificial intelligence, bringing together safety and security methodologies to create a new risk assessment and assurance program. This program evaluates potential bespoke risks and determines the necessary safety and security measures for AI-based systems.*

If you’ve read any news over the past six months, you’re aware of the unbridled enthusiasm for artificial intelligence. The public has flocked to tools built on systems like [GPT-3](https://openai.com/blog/gpt-3-apps) and [Stable Diffusion](https://stablediffusionweb.com/), captivated by how they alter our capacity to create and interact with each other. While these systems have amassed headlines, they constitute a small fraction of AI-based systems that are currently in use, powering technology that is influencing outcomes in all aspects of life, such as [finance](https://www.ciodive.com/news/financial-services-AI-appetite-grows/643869/), [healthcare](https://www.forbes.com/sites/amyfeldman/2022/01/03/next-billion-dollar-startups-how-vizai-helps-hospitals-treat-stroke-patients-earlier-video/?sh=3460d9805e1c), [transportation](https://www.nbcnews.com/mach/science/elon-musk-says-tesla-s-ai-will-let-cars-predict-ncna813211) and more. People are also attempting to shoehorn models like GPT-3 into their own applications, even though these models may introduce unintended risks or not be adequate for their desired results. Those risks will compound as the industry moves to [multimodal models](https://venturebeat.com/ai/multimodal-models-are-fast-becoming-a-reality-consequences-be-damned/).

With people in many fields trying to hop on the AI bandwagon, we are dealing with security and safety issues that have plagued the waves of innovation that have swept through society in the last 50 years. This includes issues such as proper risk identification and quantification, responsible and coordinated vulnerability disclosures, and safe deployment strategies. In the rush to embrace AI, the public is at a loss as to the full scope of its impact, and whether these systems are truly safe. Furthermore, the work seeking to map, measure, and mitigate against newfound risks has fallen short, due to the limitations and nuances that come with applying traditional measures to AI-based systems.

The new ML/AI assurance practice at Trail of Bits aims to address these issues. With our forthcoming work, we not only want to ensure that AI systems have been accurately evaluated for potential risk and safety concerns, but we also want to establish a framework that auditors, developers and other stakeholders can use to better assess potential risks and required safety mitigations for AI-based systems. Further work will build evaluation benchmarks, particularly focused on cybersecurity, for future machine-learning models. We will approach the AI ecosystem with the same rigor that we are known to apply to other technological areas, and hope the services transform the way practitioners in this field work on a daily basis.

[In a paper released](https://github.com/trailofbits/publications/blob/master/papers/toward_comprehensive_risk_assessments.pdf) by our ML assurance team, we propose a novel, end-to-end AI risk framework that incorporates the concept of an Operational Design Domain (ODD), which can better outline the hazards and harms a system can potentially have. ODDs are a concept that has been used in the autonomous vehicle space, but we want to take it further: By having a framework that can be applied to all AI-based systems, we can better assess potential risks and required safety mitigations, no matter the application.

We also discuss in the paper:

* **When “safety” doesn’t mean safety:** The AI community has conflated “requirements engineering” with “safety measures,” which is not the same thing. In fact, it’s often contradictory!
* **The need for new measures:** Risk assessment practices taken from other fields, i.e. hardware safety, don’t translate well to AI. There needs to be more done to uncover design issues that directly lead to systematic failures.
* **When “safety” doesn’t mean “security”:** The two terms are not interchangeable, and need to be assessed differently when applied to AI and ML systems.
* **It hasn’t been all bad:** The absence of well-defined operational boundaries for general AI and ML models has made it difficult to accurately assess the associated risks and safety, given the vast number of applications and potential hazards. We discuss what models can be adapted, specifically those that can ensure security and reliability.

The AI community, and the general public, will suffer the same or worse consequences we’ve seen in the past if we cannot safeguard the systems the world is rushing to adopt. In order to do so, it’s essential to get on the same page when it comes to terminology and techniques for safety objectives and risk assessments. However, we don’t need to reinvent the wheel. Applicable techniques already exist; they just need to be adapted to the AI and machine-learning space. With both this paper and our practice’s forthcoming work, we hope to bring clarity and cohesion to AI assurance and safety, in the hope that it can counter the marketing hype and exaggerated commercial messaging in the current marketplace that deemphasizes the security of this burgeoning technology.

This approach builds on [our previous](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) [machine-learning work](https://blog.trailofbits.com/2021/11/09/privacyraven-implementing-a-proof-of-concept-for-model-inversion/), and is just the beginning of our efforts in this domain. Any organizations interested in working with this team can [contact Trail of Bits](https://www.trailofbits.com/contact) to inquire about future projects.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.