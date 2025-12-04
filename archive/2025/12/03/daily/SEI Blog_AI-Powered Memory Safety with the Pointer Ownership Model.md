---
title: AI-Powered Memory Safety with the Pointer Ownership Model
url: https://www.sei.cmu.edu/blog/ai-powered-memory-safety-with-the-pointer-ownership-model/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2025-12-03
fetch_date: 2025-12-04T03:19:36.131253
---

# AI-Powered Memory Safety with the Pointer Ownership Model

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

About

Our Work

Publications

News and Events

Education and Outreach

Careers

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. AI-Powered Memory Safety with the Pointer Ownership Model

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Svoboda, D., and Flynn, L., 2025: AI-Powered Memory Safety with the Pointer Ownership Model. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed December 3, 2025, https://doi.org/10.58012/zpzf-0005.

Copy

APA Citation

Svoboda, D., & Flynn, L. (2025, December 3). AI-Powered Memory Safety with the Pointer Ownership Model. Retrieved December 3, 2025, from https://doi.org/10.58012/zpzf-0005.

Copy

Chicago Citation

Svoboda, David, and Lori Flynn. "AI-Powered Memory Safety with the Pointer Ownership Model." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, December 3, 2025. https://doi.org/10.58012/zpzf-0005.

Copy

IEEE Citation

D. Svoboda, and L. Flynn, "AI-Powered Memory Safety with the Pointer Ownership Model," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 3-Dec-2025 [Online]. Available: https://doi.org/10.58012/zpzf-0005. [Accessed: 3-Dec-2025].

Copy

BibTeX Code

@misc{svoboda\_2025,
author={Svoboda, David and Flynn, Lori},
title={AI-Powered Memory Safety with the Pointer Ownership Model},
month={{Dec},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/zpzf-0005},
note={Accessed: 2025-Dec-3}
}

Copy

# AI-Powered Memory Safety with the Pointer Ownership Model

![Headshot of David Svoboda.](/media/images/Svoboda_David_22_230926.360x360.max-180x180.format-webp.webp)
![Headshot of Lori Flynn.](/media/images/thumb_big_l-flynn_blog_authors_.max-180x180.format-webp.webp)

###### [David Svoboda](/authors/david-svoboda) and [Lori Flynn](/authors/lori-flynn)

###### December 3, 2025

##### PUBLISHED IN

[Secure Development](/blog/topics/secure-development/)

##### CITE

<https://doi.org/10.58012/zpzf-0005>

Get Citation

##### SHARE

In October 2025, CyberPress [reported](https://cyberpress.org/redis-use-after-free-vulnerability/) a critical security vulnerability in the Redis Server, an open-source in-memory database: [CVE-2025-49844](https://nvd.nist.gov/vuln/detail/CVE-2025-49844) allowed authenticated attackers to achieve remote code execution through a [use-after-free](https://cwe.mitre.org/data/definitions/416.html) ([CWE-416](https://cwe.mitre.org/data/definitions/416.html)) flaw in the Lua scripting engine.

In 2024, another prominent temporal memory safety flaw was found in the Netfilter subsystem in the Linux kernel: [CVE-2024-1086](https://nvd.nist.gov/vuln/detail/cve-2024-1086). This issue caused the `nf_hook_slow()` function to free memory twice ([CWE-415: Double Free](https://cwe.mitre.org/data/definitions/415.html)), allowing an attacker to exploit this double-free vulnerability to execute arbitrary code of their own choosing.

As the above examples illustrate, bugs related to temporal memory safety, such as use-after-free and double-free vulnerabilities, are challenging issues in C and C++ code. These bugs are difficult to detect and fix, often resulting in significant security vulnerabilities and system instability. Each year from 2006-2018, [approximately 70 percent](https://www.microsoft.com/en-us/msrc/blog/2019/07/a-proactive-approach-to-more-secure-code/) of vulnerabilities to which Microsoft assigned a CVE have been memory safety issues (temporal or spatial memory safety issues, such as buffer overflows), dropping only to around [50 percent in 2023](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF). In its list of most dangerous software weaknesses, MITRE ranked CWE-416 [seventh in 2022](https://cwe.mitre.org/top25/archive/2022/2022_cwe_top25.html) and [fourth in 2023](https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html). CWE-416 is also the source of [more than a third of the high-severity security bugs in the Chromium codebase](https://www.chromium.org/Home/chromium-security/memory-safety/). ([CVE](https://www.cve.org/) is the MITRE-maintained inventory of identified vulnerabilities in systems; [CWE](https://cwe.mitre.org/) is the MITRE-maintained inventory of patterns of common weakness in systems, such as use-after-free.)

This post, primarily adapted from the recently published technical report [*Design of Enhanced Pointer Ownership Model for C*](https://www.sei.cmu.edu/library/design-of-enhanced-pointer-ownership-model-for-c/), highlights recent updates to the [Pointer Ownership Model](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6759228) (POM). POM is a modeling framework designed to improve the ability of developers to statically analyze C programs for errors involving dynamic memory. To make a program comply with POM, a developer needed to identify the program’s “responsible” pointers, that is, pointers whose objects must be explicitly freed before the pointers themselves may be destroyed. Any program that complies with POM can be statically analyzed to ensure that the design is consistent and secure and that the code correctly respects the principles of pointer ownership.

POM can also be used to diagnose and eliminate many dynamic memory errors from C programs. The main drawback of the original POM (model and tooling) was the extensive manual effort required for developers to extract POM-relevant information from a particular codebase and formalize it into a corresponding pointer model (known as a *p-model*).

There have been two significant developments since that initial 2013 POM was released: First, Rust [has grown significantly in popularity and adoption](https://thenewstack.io/survey-memory-safe-rust-gains-45-of-enterprise-development/), offering the flexibility and safety provided by C and C++ but with guarantees of memory safety. Hence, there is more sensitivity to memory safety in general. Second, LLMs provide novel capabilities in various areas of software engineering, bringing with them significant potential but also significant risks to security and functionality. Hence, LLMs offer the potential to reduce the manual burden of building a p-model, making adoption and application easier. Both developments motivate our work to enhance the original POM, for improved capabilities and for fully automated p-model creation.

Our recent updates to POM include:

* the use of large language models (LLMs) to complete a p-model,
* an improved mechanism to prevent use-after-free errors, inspired by Rust’s borrow checker and object lifetimes,
* improved function argument handling with a new abstraction of diligent or producer arguments, and
* handling structs, unions, or arrays that contain pointers; and correct handling of ambiguity in assignment operations.

This post also details an approach to automatically check whether a program satisfies an associated p-model, as outlined in the technical report. Beyond the report, this post provides highlights of our team’s latest POM work that incorporates SAT solvers for automated p-model creation and/or validation.

## A Two-Stage Approach to Securing Temporal Memory Safety

POM is designed to help developers avoid, identify, and fix temporal memory-safety issues in two stages:

1. The POM builder automates generation of the p-model.
2. The POM verifier identifies all remaining POM compliance errors.

The POM builder and verifier are designed to assume that every pointer...