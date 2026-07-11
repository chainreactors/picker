---
title: Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws
url: https://thehackernews.com/2026/07/researcher-details-whatsapp-to-host.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:37.041611
---

# Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws

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

# [Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws](https://thehackernews.com/2026/07/researcher-details-whatsapp-to-host.html)

**Ravie Lakshmanan**Jul 10, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs80_SEcGa8Q18LOUd4Y3fWiWZRh6MOX6U3LhAyAVVewqJVSd1cq2bgepE_2vS0eg9qvr0iM1JOYnYd9GPDQ-LZiTP4-J8oEpZjAMc2ivQ9QiNTMbf1BYONSvBOvZaVat_1PUWjM9O72K_pdF74UKhHm-dd-wXKLp8BDoV4dQZTi1HWOUCWbozpd4muH0i/s1700-e365/openclaw-whatsapp.jpg)

Details have emerged about three now-patched [security flaws](https://github.com/jgamblin/OpenClawCVEs/) in the OpenClaw personal artificial intelligence (AI) assistant that, if successfully exploited, could enable credential theft, privilege escalation, and arbitrary code execution on the host.

A brief description of the high-severity vulnerabilities is as follows -

* **[GHSA-hjr6-g723-hmfm](https://github.com/openclaw/openclaw/security/advisories/GHSA-hjr6-g723-hmfm)** (CVSS score: 8.8) - An operating system command injection and an incomplete list of disallowed inputs vulnerability impacting the host execution environment filtering mechanism that could allow for executing or persist actions beyond the caller's intended authorization.
* **[GHSA-9969-8g9h-rxwm](https://github.com/openclaw/openclaw/security/advisories/GHSA-9969-8g9h-rxwm)** (CVSS score: 8.8) - An operating system command injection and an incomplete list of disallowed inputs vulnerability impacting the host execution environment filtering mechanism that could allow for executing or persist actions beyond the caller's intended authorization.
* **[GHSA-575v-8hfq-m3mc](https://github.com/openclaw/openclaw/security/advisories/GHSA-575v-8hfq-m3mc)** (CVSS score: 8.4) - A path traversal and link following vulnerability that could allow [sandbox bind mounts](https://arxiv.org/abs/2603.27517) to bypass parent-directory denylist checks and perform actions that should have been secured with stronger authorization or policy checks.

All three shortcomings have been addressed in OpenClaw version 2026.6.6.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7pp31YSx7YW04s7vxzEYFYsk_y-4ncrMNOtkTw28tuuYW4vjWPb7P9mAe1Ubpa1OPfMIe-nIE6QxtkBjL4J4gvNFanwEZhtdtDuOApElzQf863NGWbHs6CKe6elnjDZXDKA0jiWQfjDoPYamSHzrfpcy11qEMoIbR6iDsq4hAf2REYGHRZYIiZQ1TgF39/s1700-e365/open.jpg)

In a series of advisories released last week, OpenClaw maintainers said "practical impact depends on the operator's configuration and whether lower-trust input can reach that path."

However, security researcher Chinmohan Nayak, who is credited with discovering and reporting the issues, said in a [report](https://medium.com/%40chinmohannayak/i-sent-a-whatsapp-message-to-an-ai-agent-it-ran-my-code-on-the-host-adbbcbb0e0ad) shared with The Hacker News that they can be used to trigger host code execution from an external message sent via WhatsApp.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEju3jGYADeL_1dA8qwtLpzzGKgBpklCfIGmjeMoJlxtlSMdez1q7uss-H9gaBSiqYtSHQjOCbKLifZxOe6GCWnueNFLZKR6pyYKfkc7kZWWQQXm_E7Wi9IH2E-SfActpcfBBZm_-aX4pVUmKslXQIZ1z4hwq8WX0JFdMxcFVRNAll_-n6Fj0a1Fi9MKMkK5/s1700-e365/whatsapp-ai.jpg)

Unlike the [Claw Chain](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html) vulnerabilities disclosed by Cyera back in May, the newly identified bugs do not require an attacker to establish a prior foothold in order to extract sensitive data, drop a persistent backdoor, obtain arbitrary remote code execution, and facilitate an escape to the host.

"`getBlockedReasonForSourcePath()` checks if the source path is under a blocked path," the researcher explained about GHSA-575v-8hfq-m3mc. "But [it] never checks the reverse — whether a blocked path is under the source (parent directory bypass)."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Specifically, the bind mount denylist blocks directories like "~/.ssh," "~/.aws," and "~/.gnupg,” but allows mounting the parent directory "/home" or "/var," effectively undermining the individual blocks.

"Mount /home into your container, and you can read every user's SSH keys, AWS credentials, and GPG secrets," Nayak said. "Mount /var and you get the Docker socket – which means full host escape from inside the 'sandbox.'"

Besides updating OpenClaw to the latest version, it's advised to enable sandbox mode for all non-main sessions, remove "exec" from the tool allowlist for channel-facing agents, and monitor for git clone commands containing the "ext::" external protocol helper that could be abused to run arbitrary system commands.

"Before upgrading, restrict the affected feature to trusted operators or disable it when it is not needed," OpenClaw said. "As general hardening, keep channel and tool allowlists narrow, avoid sharing one Gateway between mutually untrusted users, and disable the affected feature when it is not needed."

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

[AI Security](https://thehackernews.com/search/label/AI%20Security), [Application Security]...