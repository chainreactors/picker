---
title: LangChain, LangGraph Flaws Expose Files, Secrets, Databases in Widely Used AI Frameworks
url: https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html
source: The Hacker News
date: 2026-03-27
fetch_date: 2026-03-28T04:20:15.980488
---

# LangChain, LangGraph Flaws Expose Files, Secrets, Databases in Widely Used AI Frameworks

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [LangChain, LangGraph Flaws Expose Files, Secrets, Databases in Widely Used AI Frameworks](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html)

**Ravie Lakshmanan**Mar 27, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkhroYg33geYKogEf838RfX0FRNjBX23ucPFzrxtbtf2CyTxoGZZ4RbTArZX672fygWxhNN2MOX-SXaPzWJPOeRTrnLCzYzQZ2e-7HO98AIbj-wEXbrPWSwzIOW2NbNhpWfayHyPYHyJGTRxZmDCHhR_qk79vyb29q1_p-hBCWvY2GsAPu0296IOlq_uQv/s1700-e365/langchain.jpg)

Cybersecurity researchers have disclosed three security vulnerabilities impacting LangChain and LangGraph that, if successfully exploited, could expose filesystem data, environment secrets, and conversation history.

Both LangChain and LangGraph are open-source frameworks that are used to build applications powered by Large Language Models (LLMs). LangGraph is built on the foundations of LangChain for more sophisticated and non-linear agentic workflows. According to statistics on the Python Package Index (PyPI), LangChain, LangChain-Core, and LangGraph have been downloaded more than [52 million](https://pypistats.org/packages/langchain), [23 million](https://pypistats.org/packages/langchain-core), and [9 million times](https://pypistats.org/packages/langgraph) last week alone.

"Each vulnerability exposes a different class of enterprise data: filesystem files, environment secrets, and conversation history," Cyera security researcher Vladimir Tokarev [said](https://www.cyera.com/research/langdrained-3-paths-to-your-data-through-the-worlds-most-popular-ai-framework) in a report published Thursday.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The issues, in a nutshell, offer three independent paths that an attacker can leverage to drain sensitive data from any enterprise LangChain deployment. Details of the vulnerabilities are as follows -

* **[CVE-2026-34070](https://github.com/langchain-ai/langchain/security/advisories/GHSA-qh6h-p6c9-ff54)** (CVSS score: 7.5) - A path traversal vulnerability in LangChain ("langchain\_core/prompts/loading.py") that allows access to arbitrary files without any validation via its prompt-loading API by supplying a specially crafted [prompt template](https://docs.langchain.com/langsmith/prompt-template-format#few-shot-examples).
* **[CVE-2025-68664](https://github.com/langchain-ai/langchain/security/advisories/GHSA-c67j-w6g6-q2cm)** (CVSS score: 9.3) - A deserialization of untrusted data vulnerability in LangChain that leaks API keys and environment secrets by passing as input a data structure that tricks the application into interpreting it as an already serialized LangChain object rather than regular user data.
* **[CVE-2025-67644](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-9rwj-6rc7-p77c)** (CVSS score: 7.3) - An SQL injection vulnerability in LangGraph SQLite checkpoint implementation that allows an attacker to manipulate SQL queries through metadata filter keys and run arbitrary SQL queries against the database.

Successful exploitation of the aforementioned flaws could allow an attacker to read sensitive files like Docker configurations, siphon sensitive secrets via prompt injection, and access conversation histories associated with sensitive workflows. It's worth noting that details of CVE-2025-68664 were also shared by Cyata in December 2025, giving it the cryptonym [LangGrinch](https://thehackernews.com/2025/12/critical-langchain-core-vulnerability.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVfAGzR6DAF7blHy7zfdizcRIcH6tubz4EB360xew-2PDSi5B4KI-NO_mH1MyDh4WZ12uIiJ_Za5zi2V_w_YOiaENf5u_MUUoRwYd8vNc9oE9M5GvR8KWuYGiXv_ROe-mpgz1tZlC9XbDIqp79XRKy9BXqnZhkq9zZ65nLdg7CUXW781fCguMyimQl_Otm/s1700-e365/flow.png)

The vulnerabilities have been patched in the following versions -

* CVE-2026-34070 - langchain-core >=1.2.22
* CVE-2025-68664 - langchain-core 0.3.81 and 1.2.5
* CVE-2025-67644 - langgraph-checkpoint-sqlite 3.0.1

The findings once again underscore how artificial intelligence (AI) plumbing is not immune to classic security vulnerabilities, potentially putting entire systems at risk.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-stories-xmcyber-d)

The development comes days after a critical security flaw impacting Langflow (CVE-2026-33017, CVSS score: 9.3) has [come under active exploitation](https://thehackernews.com/2026/03/critical-langflow-flaw-cve-2026-33017.html) within 20 hours of public disclosure, enabling attackers to exfiltrate sensitive data from developer environments.

Naveen Sunkavally, chief architect at Horizon3.ai, said the vulnerability shares the same root cause as [CVE-2025-3248](https://thehackernews.com/2025/05/critical-langflow-flaw-added-to-cisa.html), and stems from unauthenticated endpoints executing arbitrary code. With threat actors moving quickly to exploit newly disclosed flaws, it's essential that users apply the patches as soon as possible for optimal protection.

"LangChain doesn't exist in isolation. It sits at the center of a massive dependency web that stretches across the AI stack. Hundreds of libraries wrap LangChain, extend it, or depend on it," Cyera said. "When a vulnerability exists in LangChain’s core, it doesn’t just affect direct users. It ripples outward through every downstream library, every wrapper, every integration that inherits the vulnerable code path."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#...