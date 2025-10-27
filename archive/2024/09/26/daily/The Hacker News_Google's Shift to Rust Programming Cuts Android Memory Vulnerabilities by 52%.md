---
title: Google's Shift to Rust Programming Cuts Android Memory Vulnerabilities by 52%
url: https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html
source: The Hacker News
date: 2024-09-26
fetch_date: 2025-10-06T18:30:41.049556
---

# Google's Shift to Rust Programming Cuts Android Memory Vulnerabilities by 52%

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Google's Shift to Rust Programming Cuts Android Memory Vulnerabilities by 68%](https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html)

**Sep 25, 2024**Ravie LakshmananSecure Coding / Mobile Security

[![Android Memory Vulnerabilities](data:image/png;base64... "Android Memory Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwLU9AeRqOyAMbiXlTr6kiMSQT5ZcTTJGf1DBMaqFxB_7AD-mcTbIp-eTihwUrCAKIaPfAQNx9BfNhU70oPzvlFsy1Ck1B4qJMfWW7IVrNyCCGY6QmfaJP6DyDFXaO4aLbLxBwkLPz-zinHlY0WhooRwV2cTpoIVWoNlr-BYh1qJwh3ksnXlvbJGuMDaOv/s790-rw-e365/android-rust.png)

Google has revealed that its transition to memory-safe languages such as Rust as part of its secure-by-design approach has led to the percentage of memory-safe vulnerabilities discovered in Android dropping from 76% to 24% over a period of six years.

The tech giant said focusing on [Safe Coding](https://blog.google/technology/safety-security/tackling-cybersecurity-vulnerabilities-through-secure-by-design/) for new features not only reduces the overall security risk of a codebase, but also makes the switch more "scalable and cost-effective."

Eventually, this leads to a drop in memory safety vulnerabilities as new memory unsafe development slows down after a certain period of time, and new memory safe development takes over, Google's Jeff Vander Stoep and Alex Rebert [said](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html) in a post shared with The Hacker News.

Perhaps even more interestingly, the number of memory safety vulnerabilities tends to register a drop notwithstanding an increase in the quantity of new memory unsafe code.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The paradox is explained by the fact that vulnerabilities decay exponentially, with a study finding that a high number of vulnerabilities often reside in new or recently modified code.

"The problem is overwhelmingly with new code, necessitating a fundamental change in how we develop code," Vander Stoep and Rebert noted. "Code matures and gets safer with time, exponentially, making the returns on investments like rewrites diminish over time as code gets older."

Google, which [formally announced](https://thehackernews.com/2021/04/android-to-support-rust-programming.html) its plans to support the Rust programming language in Android way back in April 2021, said it began prioritizing transitioning new development to memory-safe languages around 2019.

As a result, the number of memory safety vulnerabilities discovered in the operating system has declined from [223 in 2019](https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html) to less than 50 in 2024.

[![Rust Programming](data:image/png;base64... "Rust Programming")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLLibKDXpz8xiDGfAT_CHM0JEFukwW0E4mBV1FbS1WBh-ySzWYqjDK3mocOaly9voiWpXe_-o5AGgphtma0wHE3UMz7tIHksGmPopqwGuNZxLAypRF1LCb7tg5hyphenhyphenH7oy0uNvbZ3yrsaSqyFnjPpzrkAcsOfy61xWGpxjc2IGnTShE5zg1FHz1BLrimjwrn/s790-rw-e365/flaws.png)

It also goes without saying that much of the decrease in such flaws is down to advancements in the ways devised to combat them, moving from reactive patching to proactive mitigating to proactive vulnerability discovery using tools like [Clang sanitizers](https://thehackernews.com/2023/12/google-using-clang-sanitizers-to.html).

The tech giant further noted that memory safety strategies should evolve even more to prioritize "high-assurance prevention" by incorporating [secure-by-design principles](https://dl.acm.org/doi/10.1145/3651621) that enshrine security into the very foundations.

"Instead of focusing on the interventions applied (mitigations, fuzzing), or attempting to use past performance to predict future security, Safe Coding allows us to make strong assertions about the code's properties and what can or cannot happen based on those properties," Vander Stoep and Rebert said.

That's not all. Google said it is also focusing on offering interoperability between Rust, C++, and Kotlin, instead of code rewrites, as a "practical and incremental approach" to embracing memory-safe languages and ultimately eliminating entire vulnerability classes.

"Adopting Safe Coding in new code offers a paradigm shift, allowing us to leverage the inherent decay of vulnerabilities to our advantage, even in large existing systems," it said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The concept is simple: once we turn off the tap of new vulnerabilities, they decrease exponentially, making all of our code safer, increasing the effectiveness of security design, and alleviating the scalability challenges associated with existing memory safety strategies such that they can be applied more effectively in a targeted manner."

The development comes as Google touted increased collaboration with Arm's product security and graphics processing unit (GPU) engineering teams to flag multiple shortcomings and elevate the overall security of the GPU software/firmware stack across the Android ecosystem.

This includes the discovery of two memory issues in Pixel's customization of driver code ([CVE-2023-48409 and CVE-2023-48421](https://source.android.com/docs/security/bulletin/pixel/2023-12-01)) and another in Arm Valhall GPU firmware and 5th Gen GPU architecture firmware ([CVE-2024-0153](https://developer.arm.com/Arm%20Security%20Center/Mali%20GPU%20Driver%20Vulnerabilities)).

"Proactive testing is good hygiene as it can lead to the detection and resolution of new vulnerabilities before they're exploited," Google and Arm [said](https://security.googleblog.com/2024/09/google-arm-raising-bar-on-gpu-security.html).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [Lin...