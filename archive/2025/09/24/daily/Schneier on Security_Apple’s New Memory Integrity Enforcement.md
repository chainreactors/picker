---
title: Apple’s New Memory Integrity Enforcement
url: https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html
source: Schneier on Security
date: 2025-09-24
fetch_date: 2025-10-02T20:35:44.747487
---

# Apple’s New Memory Integrity Enforcement

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Apple’s New Memory Integrity Enforcement

Apple has introduced a new hardware/software security feature in the iPhone 17: “[Memory Integrity Enforcement](https://security.apple.com/blog/memory-integrity-enforcement/),” targeting the memory safety vulnerabilities that spyware products like Pegasus tend to use to get unauthorized system access. From [*Wired*](https://www.wired.com/story/apple-iphone-17-memory-integrity-enforcement/):

> In recent years, a movement has been steadily growing across the global tech industry to address a ubiquitous and insidious type of bugs known as memory-safety vulnerabilities. A computer’s memory is a shared resource among all programs, and memory safety issues crop up when software can pull data that should be off limits from a computer’s memory or manipulate data in memory that shouldn’t be accessible to the program. When developers—­even experienced and security-conscious developers—­write software in ubiquitous, historic programming languages, like C and C++, it’s easy to make mistakes that lead to memory safety vulnerabilities. That’s why proactive tools like [special programming languages](https://www.wired.com/story/rust-secure-programming-language-memory-safe/) have been proliferating with the goal of making it structurally impossible for software to contain these vulnerabilities, rather than attempting to avoid introducing them or catch all of them.
>
> […]
>
> With memory-unsafe programming languages underlying so much of the world’s collective code base, Apple’s Security Engineering and Architecture team felt that putting memory safety mechanisms at the heart of Apple’s chips could be a deus ex machina for a seemingly intractable problem. The group built on a specification known as [Memory Tagging Extension](https://www.usenix.org/system/files/login/articles/login_summer19_03_serebryany.pdf) (MTE) released in 2019 by the chipmaker Arm. The idea was to essentially password protect every memory allocation in hardware so that future requests to access that region of memory are only granted by the system if the request includes the right secret.
>
> Arm developed MTE as a tool to help developers find and fix memory corruption bugs. If the system receives a memory access request without passing the secret check, the app will crash and the system will log the sequence of events for developers to review. Apple’s engineers wondered whether MTE could run all the time rather than just being used as a debugging tool, and the group worked with Arm to release a version of the specification for this purpose in 2022 called [Enhanced Memory Tagging Extension](https://developer.arm.com/documentation/109697/0100/Feature-descriptions/The-Armv8-9-architecture-extension?lang=en#md454-the-armv89-architecture-extension__FEAT_MTE4).
>
> To make all of this a constant, real-time defense against exploitation of memory safety vulnerabilities, Apple spent years architecting the protection deeply within its chips so the feature could be on all the time for users without sacrificing overall processor and memory performance. In other words, you can see how generating and attaching secrets to every memory allocation and then demanding that programs manage and produce these secrets for every memory request could dent performance. But Apple says that it has been able to thread the needle.

Tags: [Apple](https://www.schneier.com/tag/apple/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [hardware](https://www.schneier.com/tag/hardware/), [integrity](https://www.schneier.com/tag/integrity/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on September 23, 2025 at 7:07 AM](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html) •
[22 Comments](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html#comments)

### Comments

sle •
[September 23, 2025 7:50 AM](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html/#comment-448158)

Such a progress.

AlexT •
[September 23, 2025 10:49 AM](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html/#comment-448161)

Seems like a significant progress.

Wonder if anyone in the Android space will respond.

ATN •
[September 23, 2025 10:51 AM](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html/#comment-448162)

As if it was simple to isolate tasks inside an operating system…
In general, those tasks are on the same computer because they need to talk to each other, the WEB browser need to talk to the printer, the video game need the graphic card so need support for graphic libraries/compilers that every other task also use, maybe at the exact same time.
Isolation can be a little simpler in between virtual machines on the same computer, but general case is not a solved problem.

KC •
[September 23, 2025 10:54 AM](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html/#comment-448163)

A little OT but hopefully not terribly.

An excerpt from a [linked](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF) June 2025 report on MSL (memory safe languages):

> Prossimo, a project of the [ISRG] and [OpenSSF], states that it plans to transition the Internet’s critical infrastructure to memory safe code and develop memory safe essential software.

I’m reading that Prossimo helped support adding memory safe language to the Linux kernel. (And is contributing to many other projects, still researching.) Seems very important considering the distribution. Happy to see MSLs being implemented so widely. It’s hard to think that mercenary spyware developers or others will fold up shop, but good to make the investments where there are resources or critical needs.

Wayne •
[September 23, 2025 11:18 AM](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html/#comment-448164)

And guaranteed Pegasus et al were first in line to buy new iPhone 17s to figure out ways to corrupt them. It will be interesting to see how this fight goes.

Over the weekend I was reading that the C++ standards people rejected a proposal for SAFE C++ in favor of Profiles to improve memory safety. Unfortunately not enough explanation in the article as to exactly what the difference was. I just know that of all the programming languages that I’ve studied over the years, C/C++ were my least favorite.

wiredog •
[September 23, 2025 11:58 AM](https://www.schneier.com/blog/archives/2025/09/apples-new-memory-integrity-enforcement.html/#comment-448165)

This is a hardware solution. Memory safe hardware! At some point the kernel has to be memory unsafe so handling this at a lower level than the kernel helps. Although you d...