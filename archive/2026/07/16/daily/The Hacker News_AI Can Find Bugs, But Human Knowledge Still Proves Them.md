---
title: AI Can Find Bugs, But Human Knowledge Still Proves Them
url: https://thehackernews.com/2026/07/ai-can-find-bugs-but-human-knowledge.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:24.671557
---

# AI Can Find Bugs, But Human Knowledge Still Proves Them

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [AI Can Find Bugs, But Human Knowledge Still Proves Them](https://thehackernews.com/2026/07/ai-can-find-bugs-but-human-knowledge.html)

**The Hacker News**Jul 16, 2026Artificial Intelligence / Offensive Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfFHlEVhBtz6htSsevgYmwuQZHGlEXKK9eqiOqgiXJ587449tNZfWR9y74kC9MfZ6CDSPx6IBloYogs0PBSeynORkAZsD6825INUqoJaIMwtAbBVkve-A8xBNmz6fNpxsuwjsF_jfXHqBumqTT9VY7Jn5gEP3C0fVLOtuVFZ2krUvHSagGvupLXQSH-YI/s1700-e365/cvss.jpg)

Artificial intelligence (AI) is changing offensive security, but it has not changed the standard that matters most: a finding has to be proven before it becomes useful. AI-assisted tools can read code quickly, generate payloads, summarize attack surfaces, explain unfamiliar APIs, and run repetitive testing workflows at impressive speed. That is a real advantage for security teams. It also creates a new kind of pressure, because the industry can now produce more vulnerability-looking output than ever before.

The problem is that output is not the same as evidence. A generated report can sound polished, include a severity rating, and even contain a proof-of-concept that looks reasonable at first glance. None of that proves the bug exists in the deployed environment. None of it proves exploitability, impact, or risk. In offensive testing, the hard part has never been writing something that sounds like a vulnerability report. The hard part is demonstrating what is actually true.

That distinction is becoming more important as AI becomes more common in security workflows. AI can accelerate discovery, but validation still depends on knowledge: knowledge of systems, protocols, application behavior, identity boundaries, memory corruption, business logic, and all the implementation details that separate a plausible theory from a real exploit. The future of offensive security will not belong to people who merely produce the largest number of findings. It will belong to people and teams that can prove what matters.

## The Industry Is Already Seeing the Cost of Shallow AI Output

The warning signs are already visible. Bug bounty programs and maintainers have been dealing with a surge of low-quality AI-generated reports, often submitted with thin evidence, templated language, and little meaningful validation. Bugcrowd [publicly addressed this pattern](https://www.bugcrowd.com/blog/bugcrowd-policy-changes-to-address-ai-slop-submissions/) in its policy changes around AI-generated submissions, describing a class of reports that looked polished but created unnecessary triage burden rather than a useful security signal.

This is not just a bug bounty problem. It is a preview of what happens anywhere AI is used to create security findings without enough human judgment behind them. If a tool can generate a convincing write-up in seconds, organizations will receive more reports, more alerts, and more claims. Unless those claims are validated, the result is not better security. It is a larger queue.

Security teams are already overloaded with scanner output, dependency alerts, cloud configuration issues, and compliance findings. Adding AI-generated speculation on top of that does not help unless the quality bar goes up at the same time. A finding should answer basic questions clearly: what happened, how it was reproduced, what the attacker controls, which boundary was crossed, and what the demonstrated impact is. Without that, the report may be interesting, but it is not ready to drive engineering action.

## “Looks Vulnerable” Is Not the Same as Vulnerable

One of the most dangerous habits in offensive testing is confusing a suspicious pattern with a validated vulnerability. AI can make that habit worse because it is good at explaining why something might be bad. A model may see user input near a database query and describe SQL injection. It may see a URL fetch and suggest SSRF. It may see a dangerous API in a code path and describe remote code execution. Sometimes the model is pointing at a real issue. Other times, it is missing the conditions that decide whether the issue matters.

A tester still has to prove reachability. Does the attacker-controlled input actually reach the dangerous operation? Is authentication required? Is authorization enforced somewhere else? Is the vulnerable feature enabled? Does the production configuration expose the code path? Does the application normalize, encode, sanitize, or reject the payload before it matters? Does the issue cross a trust boundary or merely affect an internal-only path with no practical security impact?

These questions are where real offensive security begins. They are also where shallow automation often breaks down. AI can generate hypotheses quickly, but hypotheses are not findings. A good tester treats AI output as a lead to investigate, not a conclusion to forward.

## Why Knowledge Still Matters

The best offensive security practitioners are valuable because they understand systems, not because they can run tools. Tools have always been part of the job, but tool output has never been enough. A web scanner may identify a parameter that reflects input. A static analyzer may flag a dangerous function. A fuzzer may produce a crash. A language model may describe a plausible attack path. In every case, someone still needs to understand what the signal means.

That understanding is usually earned through repetition. Senior researchers spent years doing the work manually: tracing requests, reading source, reverse engineering binaries, debugging crashes, writing exploit code, breaking authentication flows, and learning how real systems fail. That process builds memory and instinct. It teaches a practitioner when a finding is probably real, when a tool is being misled, and when a small bug may become serious if chained with something else.

This kind of knowledge is hard to fake. It shows up in the questions a tester asks. It shows up in the way a report is wr...