---
title: Securing tomorrow's software: the need for memory safety standards
url: http://security.googleblog.com/2025/02/securing-tomorrows-software-need-for.html
source: Google Online Security Blog
date: 2025-02-26
fetch_date: 2025-10-06T20:34:07.897780
---

# Securing tomorrow's software: the need for memory safety standards

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Securing tomorrow's software: the need for memory safety standards](https://security.googleblog.com/2025/02/securing-tomorrows-software-need-for.html "Securing tomorrow's software: the need for memory safety standards ")

February 25, 2025

Posted by Alex Rebert, Security Foundations, Ben Laurie, Research, Murali Vijayaraghavan, Research and Alex Richardson, Silicon

For decades, memory safety vulnerabilities have been at the center of various security incidents across the industry, eroding trust in technology and costing [billions](https://en.wikipedia.org/wiki/Petya_%28malware_family%29). Traditional approaches, like code auditing, fuzzing, and exploit mitigations – while helpful – haven't been enough to stem the tide, while incurring an increasingly high cost.

In this blog post, we are calling for a fundamental shift: a collective commitment to finally eliminate this class of vulnerabilities, anchored on [secure-by-design practices](https://blog.google/technology/safety-security/tackling-cybersecurity-vulnerabilities-through-secure-by-design/) – not just for ourselves but for the generations that follow.

The shift we are calling for is reinforced by a recent [ACM article calling to standardize memory safety](https://cacm.acm.org/opinion/it-is-time-to-standardize-principles-and-practices-for-software-memory-safety/) we took part in releasing with academic and industry partners. It's a recognition that the lack of memory safety is no longer a niche technical problem but a societal one, impacting everything from national security to personal privacy.

The standardization opportunity

Over the past decade, a confluence of secure-by-design advancements has matured to the point of practical, widespread deployment. This includes memory-safe languages, now including high-performance ones such as Rust, as well as safer language subsets like [Safe Buffers](https://clang.llvm.org/docs/SafeBuffers.html) for C++.

These tools are already proving effective. In Android for example, the increasing adoption of memory-safe languages like Kotlin and Rust in new code has driven a [significant reduction in vulnerabilities](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html).

Looking forward, we're also seeing exciting and promising developments in hardware. Technologies like ARM's [Memory Tagging Extension](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/enhancing-memory-safety) (MTE) and the [Capability Hardware Enhanced RISC Instructions](https://en.wikipedia.org/wiki/Capability_Hardware_Enhanced_RISC_Instructions) (CHERI) architecture offer a complementary defense, particularly for existing code.

While these advancements are encouraging, achieving comprehensive memory safety across the entire software industry requires more than just individual technological progress:  we need to create the right environment and accountability for their widespread adoption. Standardization is key to this.

To facilitate standardization, we suggest establishing a common framework for specifying and objectively assessing memory safety assurances; doing so will lay the foundation for creating a market in which vendors are incentivized to invest in memory safety. Customers will be empowered to recognize, demand, and reward safety. This framework will provide governments and businesses with the clarity to specify memory safety requirements, driving the procurement of more secure systems.

The framework we are proposing would complement existing efforts by defining specific, measurable criteria for achieving different levels of memory safety assurance across the industry. In this way, policymakers will gain the technical foundation to craft effective policy initiatives and incentives promoting memory safety.

A blueprint for a memory-safe future

We know there's more than one way of solving this problem, and we are ourselves [investing](https://security.googleblog.com/2024/10/safer-with-google-advancing-memory.html) in several. Importantly, our vision for achieving memory safety through standardization focuses on defining the desired outcomes rather than locking ourselves into specific technologies.

To translate this vision into an effective standard, we need a framework that will:

Foster innovation and support diverse approaches: The standard should focus on the security properties we want to achieve (e.g., freedom from spatial and temporal safety violations) rather than mandating specific implementation details. The framework should therefore be technology-neutral, allowing vendors to choose the best approach for their products and requirements. This encourages innovation and allows software and hardware manufacturers to adopt the best solutions as they emerge.

Tailor memory safety requirements based on need: The framework should establish different levels of safety assurance, akin to [SLSA levels](https://slsa.dev/spec/v0.1/levels), recognizing that different applications have different security needs and cost constraints. Similarly, we likely need distinct guidance for developing new systems and improving existing codebases. For instance, we probably do not need every single piece of code to be formally proven. This allows for tailored security, ensuring appropriate levels of memory safety for various contexts.

Enable objective assessment: The framework should define clear criteria and potentially metrics for assessing memory safety and compliance with a given level of assurance. The goal would be to objectively compare the memory safety assurance of different software components or systems, much like we assess energy efficiency today. This will move us beyond subjective claims and towards objective and comparable security properties across products.

Be practical and actionable: Alongside the technology-neutral framework, we need best practices for existing technologies. The framework should provide guidance on how to effectively leverage specific technologies to meet the standards. This includes answering questions such as when and to what extent unsafe code is acceptable within larger software systems, and guidelines on structuring such unsafe dependencies to support compositional reasoning about safety.

Google's commitment

At Google, we're not just advocating for standardization and a memory-safe future, we're actively working to build it.

We are collaborating with industry and academic partners to develop potential standards, and our joint authorship of the recent [CACM call-to-action](https://cacm.acm.org/opinion/it-is-time-to-standardize-principles-and-practices-for-software-memory-safety/) marks an important first step in this process. In addition, as outlined in our [Secure by Design whitepaper](https://blog.google/technology/safety-security/google-secure-by-design-pledge/) and in our [memory safety strategy](https://security.googleblog.com/2024/10/safer-with-google-advancing-memory.html), we are deeply committed to building security into the foundation of our products and services.

This commitment is also reflected in our internal efforts. We are prioritizing memory-safe languages, and have already seen significant reductions in vulnerabilities by adopting languages like Rust in combination with existing, wide-spread usage of Java, Kotlin, and Go where performance constraints permit. We recognize that a complete transition to those languages will take time. That's why we're also investing in techniques to improve the safety of our existing C++ codebase by design, such as [deploying hardened libc++](https://security.googleblog.com/2024/11/retrofitting-spatial-safe...