---
title: Claude Opus 4.6 Finds 500+ High-Severity Flaws Across Major Open-Source Libraries
url: https://thehackernews.com/2026/02/claude-opus-46-finds-500-high-severity.html
source: The Hacker News
date: 2026-02-06
fetch_date: 2026-02-07T04:09:35.667784
---

# Claude Opus 4.6 Finds 500+ High-Severity Flaws Across Major Open-Source Libraries

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Claude Opus 4.6 Finds 500+ High-Severity Flaws Across Major Open-Source Libraries](https://thehackernews.com/2026/02/claude-opus-46-finds-500-high-severity.html)

**Ravie Lakshmanan**Feb 06, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3INhSQ0eqV1r5O9Q_JGSGDCw6r657lTF_JXgvwnA7iHLRer8FgbUzV37ALPlKD0MNHNUltUI8BjJNLOb2iL8FRZ3xlBO74k2HCxEsTcY8z0wN6xfNacnOK7eRHDmrw0mEbBvYINLHTQs7AEDhffz2DRXd2uOJgPh7tJg-xVZFx070Lo36hdfu7HpEEeRO/s1700-e365/claude-opus-4.6.jpg)

Artificial intelligence (AI) company Anthropic [revealed](https://red.anthropic.com/2026/zero-days/) that its latest large language model (LLM), Claude Opus 4.6, has found more than 500 previously unknown high-severity security flaws in open-source libraries, including [Ghostscript](https://ghostscript.com/), [OpenSC](https://github.com/OpenSC/OpenSC), and [CGIF](https://github.com/dloebl/cgif).

Claude Opus 4.6, which was [launched](https://www.anthropic.com/news/claude-opus-4-6) Thursday, comes with improved coding skills, including code review and debugging capabilities, along with enhancements to tasks like financial analyses, research, and document creation.

Stating that the model is "notably better" at discovering high-severity vulnerabilities without requiring any task-specific tooling, custom scaffolding, or specialized prompting, Anthropic said it is putting it to use to find and help fix vulnerabilities in open-source software.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"Opus 4.6 reads and reasons about code the way a human researcher would—looking at past fixes to find similar bugs that weren't addressed, spotting patterns that tend to cause problems, or understanding a piece of logic well enough to know exactly what input would break it," it added.

Prior to its debut, Anthropic's Frontier Red Team put the model to test inside a virtualized environment and gave it the necessary tools, such as debuggers and fuzzers, to find flaws in open-source projects. The idea, it said, was to assess the model's out-of-the-box capabilities without providing any instructions on how to use these tools or providing information that could help it better flag the vulnerabilities.

The company also said it validated every discovered flaw to make sure that it was not made up (i.e., hallucinated), and that the LLM was used as a tool to prioritize the most severe memory corruption vulnerabilities that were identified.

Some of the security defects that were flagged by Claude Opus 4.6 are listed below. They have since been patched by the respective maintainers.

* Parsing the Git commit history to identify a vulnerability in Ghostscript that could result in a crash by taking advantage of a missing bounds check
* Searching for function calls like strrchr() and strcat() to identify a buffer overflow vulnerability in OpenSC
* A heap buffer overflow vulnerability in CGIF (Fixed in [version 0.5.1](https://github.com/dloebl/cgif/releases/tag/v0.5.1))

"This vulnerability is particularly interesting because triggering it requires a conceptual understanding of the LZW algorithm and how it relates to the GIF file format," Anthropic said of the CGIF bug. "Traditional fuzzers (and even coverage-guided fuzzers) struggle to trigger vulnerabilities of this nature because they require making a particular choice of branches."

"In fact, even if CGIF had 100% line- and branch-coverage, this vulnerability could still remain undetected: it requires a very specific sequence of operations."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The company has pitched AI models like Claude as a critical tool for defenders to "level the playing field." But it also emphasized that it will adjust and update its safeguards as potential threats are discovered and put in place additional guardrails to prevent misuse.

The disclosure comes weeks after Anthropic said its current Claude models can succeed at multi-stage attacks on networks with dozens of hosts using only standard, open-source tools by finding and exploiting known security flaws.

"This illustrates how barriers to the use of AI in relatively autonomous cyber workflows are rapidly coming down, and highlights the importance of security fundamentals like promptly patching known vulnerabilities," it [said](https://red.anthropic.com/2026/cyber-toolkits-update/).

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Application Security](https://thehackernews.com/search/label/Application%20Security), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Open Source](https://thehackernews.com/search/label/Open%20Source), [secure coding](https://thehackernews.com/search/label/secure%20coding), [software development](https://thehackernews.com/search/label/software%20development), [threat detection](https://thehackernews.com/search/label/threat%20detection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Critical Grist-Core Vulnerability Allows RCE Attacks vi...