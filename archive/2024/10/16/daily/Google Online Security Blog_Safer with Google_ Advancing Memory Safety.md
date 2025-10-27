---
title: Safer with Google: Advancing Memory Safety
url: http://security.googleblog.com/2024/10/safer-with-google-advancing-memory.html
source: Google Online Security Blog
date: 2024-10-16
fetch_date: 2025-10-06T18:50:43.499986
---

# Safer with Google: Advancing Memory Safety

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Safer with Google: Advancing Memory Safety](https://security.googleblog.com/2024/10/safer-with-google-advancing-memory.html "Safer with Google: Advancing Memory Safety")

October 15, 2024

Posted by Alex Rebert, Security Foundations, and Chandler Carruth, Jen Engel, Andy Qin, Core Developers

Error-prone interactions between software and memory[1](#fn1) are [widely understood](http://phrack.org/archives/issues/49/14.txt) to create safety issues in software. It is estimated that about 70% of severe vulnerabilities[2](#fn2) in memory-unsafe codebases are due to memory safety bugs. Malicious actors exploit these vulnerabilities and continue to create real-world harm. In 2023, Google’s threat intelligence teams conducted an industry-wide study and observed a [close to all-time high number of vulnerabilities exploited in the wild](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Year_in_Review_of_ZeroDays.pdf). Our internal analysis estimates that 75% of CVEs used in [zero-day exploits](https://googleprojectzero.blogspot.com/p/0day.html) are memory safety vulnerabilities.

At Google, we have been mindful of these issues for over two decades, and are on a journey to continue advancing the state of memory safety in the software we consume and produce. Our [Secure by Design](https://blog.google/technology/safety-security/tackling-cybersecurity-vulnerabilities-through-secure-by-design/) commitment emphasizes integrating security considerations, including robust memory safety practices, throughout the entire software development lifecycle. This proactive approach fosters a safer and more trustworthy digital environment for everyone.

This post builds upon our previously reported [Perspective on Memory Safety](https://research.google/pubs/secure-by-design-googles-perspective-on-memory-safety/), and introduces our strategic approach to memory safety.

**Our journey so far**

Google's journey with memory safety is deeply intertwined with the evolution of the software industry itself. In our early days, we recognized the importance of balancing performance with safety. This led to the early adoption of memory-safe languages like Java and Python, and the creation of Go. Today these languages comprise a large portion of our code, providing memory safety among other benefits. Meanwhile, the rest of our code is predominantly written in C++, previously the optimal choice for high-performance demands.

We recognized the inherent risks associated with memory-unsafe languages and developed tools like [sanitizers](https://en.wikipedia.org/wiki/Code_sanitizer), which detect memory safety bugs dynamically, and fuzzers like [AFL](https://github.com/google/AFL) and [libfuzzer](https://releases.llvm.org/8.0.0/docs/LibFuzzer.html), which proactively test the robustness and security of a software application by repeatedly feeding unexpected inputs. By open-sourcing these tools, we've empowered developers worldwide to reduce the likelihood of memory safety vulnerabilities in C and C++ codebases. Taking this commitment a step further, we provide continuous fuzzing to open-source projects through [OSS-Fuzz](https://security.googleblog.com/2016/12/announcing-oss-fuzz-continuous-fuzzing.html), which helped get over [8800 vulnerabilities identified and subsequently fixed across 850 projects](https://security.googleblog.com/2023/02/taking-next-step-oss-fuzz-in-2023.html).

Today, with the emergence of high-performance memory-safe languages like Rust, coupled with a deeper understanding of the limitations of purely detection-based approaches, we are focused primarily on preventing the introduction of security vulnerabilities at scale.

**Going forward: Google's two-pronged approach**

Google's long-term strategy for tackling memory safety challenges is multifaceted, recognizing the need to address both existing codebases and future development, while maintaining the pace of business.

Our long-term objective is to progressively and consistently integrate memory-safe languages into Google's codebases while phasing out memory-unsafe code in new development. Given the amount of C++ code we use, we anticipate a residual amount of mature and stable memory-unsafe code will remain for the foreseeable future.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSRbsz3UFa32nAEek2cEOIN-IM5XN6df3vibnuP7nmzJoYLMAfkHgjlAcbCbjGmV0THU_CMtP9vgs3EHHe7zwRqeuXbQoxA_EGrqDMLDRJShnakXuMxesVqDJaq2xPWcpyqCcRpvW3-ZWJiZu2LXtyEs23CvI4jOBkw89T1iSVWHl-j4OYMsC0EN0E4dFh/s600/memory%20safety%20graphic.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSRbsz3UFa32nAEek2cEOIN-IM5XN6df3vibnuP7nmzJoYLMAfkHgjlAcbCbjGmV0THU_CMtP9vgs3EHHe7zwRqeuXbQoxA_EGrqDMLDRJShnakXuMxesVqDJaq2xPWcpyqCcRpvW3-ZWJiZu2LXtyEs23CvI4jOBkw89T1iSVWHl-j4OYMsC0EN0E4dFh/s3355/memory%20safety%20graphic.png)

*Graphic of memory-safe language growth as memory-unsafe code is hardened and gradually decreased over time.*

**Migration to Memory-Safe Languages (MSLs)**

The first pillar of our strategy is centered on further increasing the adoption of memory-safe languages. These languages drastically drive down the risk of memory-related errors through features like garbage collection and borrow checking, embodying the same Safe Coding[3](#fn3) principles that successfully eliminated other vulnerability classes like cross-site scripting (XSS) at scale. Google has already embraced MSLs like Java, Kotlin, Go, and Python for a large portion of our code.

Our next target is to ramp up memory-safe languages with the necessary capabilities to address the needs of even more of our low-level environments where C++ has remained dominant. For example, we are investing to expand Rust usage at Google beyond Android and other mobile use cases and into our server, application, and embedded ecosystems. This will unlock the use of MSLs in low-level code environments where C and C++ have typically been the language of choice. In addition, we are exploring more seamless interoperability with C++ through [Carbon](https://github.com/carbon-language/carbon-lang), as a means to accelerate even more of our transition to MSLs.

In Android, which runs on billions of devices and is one of our most critical platforms, we've already made strides in adopting MSLs, including Rust, in sections of our network, firmware and graphics stacks. We specifically focused on adopting memory safety in *new code* instead of rewriting mature and stable memory-unsafe C or C++ codebases. As we've previously [discussed](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html), this strategy is driven by vulnerability trends as memory safety vulnerabilities were typically introduced shortly before being discovered.

As a result, the number of memory safety vulnerabilities reported in Android has decreased dramatically and quickly, dropping from more than 220 in 2019 to a projected 36 by the end of this year, demonstrating the effectiveness of this strategic shift. Given that memory-safety vulnerabilities are particularly severe, the reduction in memory safety vulnerabilities is leading to a [corresponding drop in vulnerability severity](https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html#:~:text=With%20the%20drop%20in%20memory%20safety%20vulnerabilities%2C%20we%E2%80%99re%20seeing%20a%20corresponding%20drop%20in%20vulnerability%20severity.), representing a reduction in security risk.

**Risk Reduction for Memory-Unsafe Code**

While transitioning to memory-safe languages is the long-term strategy, and one that requires investment now, we recognize the immediate responsibility ...