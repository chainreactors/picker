---
title: Retrofitting spatial safety to hundreds of millions of lines of C++
url: http://security.googleblog.com/2024/11/retrofitting-spatial-safety-to-hundreds.html
source: Google Online Security Blog
date: 2024-11-16
fetch_date: 2025-10-06T19:15:27.434658
---

# Retrofitting spatial safety to hundreds of millions of lines of C++

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Retrofitting spatial safety to hundreds of millions of lines of C++](https://security.googleblog.com/2024/11/retrofitting-spatial-safety-to-hundreds.html "Retrofitting spatial safety to hundreds of millions of lines of C++")

November 15, 2024

Posted by Alex Rebert and Max Shavrick, Security Foundations, and Kinuko Yasuda, Core Developer

Attackers regularly exploit [spatial memory safety vulnerabilities](https://research.google/pubs/secure-by-design-googles-perspective-on-memory-safety/), which occur when code accesses a memory allocation outside of its intended bounds, to compromise systems and sensitive data. These vulnerabilities represent a major security risk to users.

Based on an analysis of [in-the-wild exploits tracked by Google's Project Zero](https://googleprojectzero.blogspot.com/p/0day.html), spatial safety vulnerabilities represent 40% of in-the-wild memory safety exploits over the past decade:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQt1XoSwUrAiUmN6tbntYLZ-IsBBV-e2aAKIKJJcavncM9t6IwD4LVlse0OSiA5ecs52_wkiaUml_9MoncUNOU8wxajv3dPonrtVlV31TJW6bKBs6mPNec7jb12rX18VRI0VwhETljd2QEp0kQ4oFQZBNq0pwoH-EedxhThqfwD73s0dqZALf_nGPkPMdK/s1600/graph.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQt1XoSwUrAiUmN6tbntYLZ-IsBBV-e2aAKIKJJcavncM9t6IwD4LVlse0OSiA5ecs52_wkiaUml_9MoncUNOU8wxajv3dPonrtVlV31TJW6bKBs6mPNec7jb12rX18VRI0VwhETljd2QEp0kQ4oFQZBNq0pwoH-EedxhThqfwD73s0dqZALf_nGPkPMdK/s1600/graph.png)

Breakdown of memory safety CVEs [exploited in the wild](https://googleprojectzero.blogspot.com/p/0day.html) by vulnerability class.[1](#fn1)

Google is taking a [comprehensive approach to memory safety](https://security.googleblog.com/2024/10/safer-with-google-advancing-memory.html). A key element of our strategy focuses on [Safe Coding](https://blog.google/technology/safety-security/tackling-cybersecurity-vulnerabilities-through-secure-by-design/) and using memory-safe languages in new code. This leads to an exponential decline in memory safety vulnerabilities and quickly improves the overall security posture of a codebase, as demonstrated by our [post about Android's journey to memory safety](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html).

However, this transition will take multiple years as we adapt our development practices and infrastructure. Ensuring the safety of our billions of users therefore requires us to go further: we're also retrofitting secure-by-design principles to our existing C++ codebase wherever possible.

To that end, we're working towards bringing spatial memory safety into as many of our C++ codebases as possible, including Chrome and the monolithic codebase powering our services.

We’ve begun by enabling hardened libc++, which adds bounds checking to standard C++ data structures, eliminating a significant class of spatial safety bugs. While C++ will not become fully memory-safe, these improvements reduce risk as discussed in more detail in our [perspective on memory safety](https://security.googleblog.com/2024/03/secure-by-design-googles-perspective-on.html), leading to more reliable and secure software.

This post explains how we're retrofitting hardened libc++ across our codebases and  showcases the positive impact it's already having, including preventing exploits, reducing crashes, and improving code correctness.

# Bounds-checked data structures: The foundation for spatial safety

One of our primary strategies for improving spatial safety in C++ is to implement bounds checking for common data structures, starting with hardening the C++ standard library (in our case, LLVM’s libc++). [Hardened libc++](https://libcxx.llvm.org/Hardening.html), recently added by open source contributors, introduces a set of security checks designed to catch vulnerabilities such as out-of-bounds accesses in production.

For example, hardened libc++ ensures that every access to an element of a std::vector stays within its allocated bounds, preventing attempts to read or write beyond the valid memory region. Similarly, hardened libc++ checks that a std::optional isn't empty before allowing access, preventing access to uninitialized memory.

This approach mirrors what's already standard practice in many modern programming languages like Java, Python, Go, and Rust. They all incorporate bounds checking by default, recognizing its crucial role in preventing memory errors. C++ has been a notable exception, but efforts like hardened libc++ aim to close this gap in our infrastructure. It’s also worth noting that similar hardening is available in other C++ standard libraries, such as [libstdc++](https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C%2B%2B.html#precondition-checks-for-c-standard-library-calls).

# Raising the security baseline across the board

Building on the successful deployment of hardened libc++ [in Chrome](https://crbug.com/40228527) in 2022, we've now made it default across our server-side production systems. This improves spatial memory safety across our services, including key performance-critical components of products like Search, Gmail, Drive, YouTube, and Maps. While a very small number of components remain opted out, we're actively working to reduce this and [raise the bar for security across the board](https://www.philvenables.com/post/raise-the-baseline-by-reducing-the-cost-of-control), even in applications with lower exploitation risk.

The performance impact of these changes was surprisingly low, despite Google's modern C++ codebase making heavy use of libc++. Hardening libc++ resulted in an average 0.30% performance impact across our services (yes, only a third of a percent).

This is due to both the compiler's ability to eliminate redundant checks during optimization, and the efficient design of hardened libc++. While a handful of performance-critical code paths still require targeted use of explicitly unsafe accesses, these instances are carefully reviewed for safety. Techniques like [profile-guided optimizations](https://en.wikipedia.org/wiki/Profile-guided_optimization) further improved performance, but even without those advanced techniques, the overhead of bounds checking remains minimal.

We actively monitor the performance impact of these checks and work to minimize any unnecessary overhead. For instance, we identified and fixed an unnecessary check, which led to a 15% reduction in overhead (reduced from 0.35% to 0.3%), and contributed the [fix back to the LLVM project](https://github.com/llvm/llvm-project/pull/105863) to share the benefits with the broader C++ community.

While hardened libc++'s overhead is minimal for individual applications in most cases, deploying it at Google's scale required a substantial commitment of computing resources. This investment underscores our dedication to enhancing the safety and security of our products.

# From tests to production

Enabling libc++ hardening wasn't a simple flip of a switch. Rather, it required a multi-stage rollout to avoid accidentally disrupting users or creating an outage:

1. **Testing:** We first enabled hardened libc++ in our tests over a year ago. This allowed us to identify and fix hundreds of previously undetected bugs in our code and tests.
2. **Baking:** We let the hardened runtime "bake" in our testing and pre-production environments, giving developers time to adapt and address any new issues that surfaced. We also conducted extensive performance evaluations, ensuring minimal impact to our users' experience.
3. **Gradual Production Rollout:** We then rolled out hardened libc++ to production over severa...