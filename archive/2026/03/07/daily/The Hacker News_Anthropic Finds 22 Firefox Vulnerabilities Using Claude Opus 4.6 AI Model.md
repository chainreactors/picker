---
title: Anthropic Finds 22 Firefox Vulnerabilities Using Claude Opus 4.6 AI Model
url: https://thehackernews.com/2026/03/anthropic-finds-22-firefox.html
source: The Hacker News
date: 2026-03-07
fetch_date: 2026-03-08T04:07:58.452548
---

# Anthropic Finds 22 Firefox Vulnerabilities Using Claude Opus 4.6 AI Model

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

# [Anthropic Finds 22 Firefox Vulnerabilities Using Claude Opus 4.6 AI Model](https://thehackernews.com/2026/03/anthropic-finds-22-firefox.html)

**Ravie Lakshmanan**Mar 07, 2026Browser Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2DaQuy20IkM7M8iL7NBmzJhI9m5KDEpf6CBgxcI9rAhiVLO1VyfdAeQKaInOY3dlIiwy1FWtusinpu8Yyj1fChemLiVCTLnMLRtKaKNvDbOOa0ZjVFt5zoT7yON1ljb2DAlgki_aVmVuWSmAPn2jFszCpJdjzN7DGGRzeEzD5OYcSn2oeLzcaBARYzmOS/s1700-e365/firefox-claude.jpg)

Anthropic on Friday said it [discovered](https://www.anthropic.com/news/mozilla-firefox-security) 22 new security vulnerabilities in the Firefox web browser as part of a security partnership with Mozilla.

Of these, 14 have been classified as high, seven have been classified as moderate, and one has been rated low in severity. The issues were addressed in [Firefox 148](https://www.firefox.com/en-US/firefox/148.0/releasenotes/), released late last month. The [vulnerabilities](https://www.mozilla.org/en-US/security/advisories/mfsa2026-13/) were identified over a two-week period in January 2026.

The artificial intelligence (AI) company said the number of high-severity bugs identified by its Claude Opus 4.6 large language model (LLM) represents "almost a fifth" of all high-severity vulnerabilities that were patched in Firefox in 2025.

Anthropic said the LLM detected a use-after-free bug in the browser's JavaScript after "just" 20 minutes of exploration, which was then validated by a human researcher in a virtualized environment to rule out the possibility of a false positive.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"By the end of this effort, we had scanned nearly 6,000 C++ files and submitted a total of 112 unique reports, including the high- and moderate-severity vulnerabilities mentioned above," the company said. "Most issues have been fixed in Firefox 148, with the remainder to be fixed in upcoming releases."

The AI upstart said it also fed its Claude model access to the entire list of vulnerabilities submitted to Mozilla and tasked the AI tool with developing a practical exploit for them.

Despite carrying out the test several hundred times and spending about $4,000 in API credits, the company said Claude Opus 4.6 was able to turn the security defect into an exploit only in two cases.

This behavior, the company added, signaled two important aspects: the cost of identifying vulnerabilities is cheaper than creating an exploit for them, and the model is better at finding issues than at exploiting them.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiR7S27TSUj8zO6SfTKVyaaZU_d2fqSjR6LwvQB3LL616Df2gFbzN92rJite4Bgyz-rX8A5YN-CydNBhLytbNq7DkZx4rMuhElnME6aDBTDPWHGEzUsY1cu8V8twKOFYXKfon62a_8nyaIuJnidHE5iS_SE5qigtSmFkeHBCMmLKOXe3gSzDFPKhF7rheHA/s1700-e365/firefox-ai.jpg)

"However, the fact that Claude could succeed at automatically developing a crude browser exploit, even if only in a few cases, is concerning," Anthropic emphasized, adding the exploits only worked within the confines of its testing environment, which has had some security features like sandboxing intentionally stripped off.

A crucial component incorporated into the process is a task verifier to determine if the exploit actually works, giving the tool real-time feedback as it explores the codebase in question and allowing it to iterate its results until a successful exploit is devised.

One such exploit Claude wrote was for [CVE-2026-2796](https://nvd.nist.gov/vuln/detail/CVE-2026-2796) (CVSS score: 9.8), which has been [described](https://red.anthropic.com/2026/exploit/) as a just-in-time (JIT) miscompilation in the JavaScript WebAssembly component.

The disclosure comes weeks after the company [released](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html) Claude Code Security in a limited research preview as a way to fix vulnerabilities using an AI agent.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

"We can't guarantee that all agent-generated patches that pass these tests are good enough to merge immediately," Anthropic said. "But task verifiers give us increased confidence that the produced patch will fix the specific vulnerability while preserving program functionality—and therefore achieve what's considered to be the minimum requirement for a plausible patch."

Mozilla, in a coordinated announcement, said the AI-assisted approach has discovered 90 other bugs, most of which have been fixed. These consisted of assertion failures that overlapped with issues traditionally found through fuzzing and distinct classes of logic errors that the fuzzers failed to catch.

"The scale of findings reflects the power of combining rigorous engineering with new analysis tools for continuous improvement," the browser maker [said](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/). "We view this as clear evidence that large-scale, AI-assisted analysis is a powerful new addition to security engineers' toolbox."

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
[**Share on ...