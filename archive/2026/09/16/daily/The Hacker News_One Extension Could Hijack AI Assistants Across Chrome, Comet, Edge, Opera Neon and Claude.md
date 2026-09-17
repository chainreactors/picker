---
title: One Extension Could Hijack AI Assistants Across Chrome, Comet, Edge, Opera Neon and Claude
url: https://thehackernews.com/2026/09/one-extension-could-hijack-ai.html
source: The Hacker News
date: 2026-09-16
fetch_date: 2026-09-17T06:59:40.766595
---

# One Extension Could Hijack AI Assistants Across Chrome, Comet, Edge, Opera Neon and Claude

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [One Extension Could Hijack AI Assistants Across Chrome, Comet, Edge, Opera Neon and Claude](https://thehackernews.com/2026/09/one-extension-could-hijack-ai.html)

**Swati Khandelwal**Sep 16, 2026Vulnerability / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnDFTLauyvgkyhmqrKcQ3QI3yCM1vbu_L8iwQK997zJz25tL7Gkm50y5S_wiSVF7hSJ7sLUMJEwXzxaubfjQc9JTdwttimIg5POxADfGNPLZEWbplFqzlKn2SZPvPuAyN0BhFtsc8PCzV2bZdBtx3z6qnRdRfw9tj-zk3aWL3t4TufGwksVdAjBuhVdO0/s1700-nu-rw-lo-l85-e365/jack.jpg)

Security researchers at Forever Security have shown that one ordinary browser extension could take control of the AI assistants built into five Chromium-based products: Gemini Live in Chrome, Perplexity Comet, Microsoft Edge, Opera Neon and the Claude in Chrome extension.

Once the extension was installed, it could access each product's built-in AI with a single click. On Comet, Edge, Opera Neon, and Claude in Chrome, it could drive the AI agent to act on behalf of the attacker; on Chrome and Comet, it could read files from the user's computer, and on Chrome, it could also switch on the camera and microphone.

The findings are researcher demonstrations, not attacks seen in the wild, and each requires the attacker's extension to be already running in the victim's browser.

These products all work the same way. The AI has a "body" inside the browser that can see the screen, open files, use the camera, and take actions, and a "brain" that runs on the company's servers and tells the body what to do, according to [Forever Security](https://forever.security/blog/bragjack-hijacking-5-browsers-via-built-in-ai-assistants). The body only takes orders from one trusted web page, such as gemini.google.com for Chrome or perplexity.ai for Comet.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

An extension is not supposed to be able to command that body. It can change web pages, not control the browser itself. Forever Security's method was to seize the trusted page the body listens to and, through it, send the body its own commands.

The extension needed only two common permissions, the researchers said: one that changes web pages, which ad blockers use, and one called declarativeNetRequest that changes the browser's network traffic. Together they let the extension slip its own code into the trusted page and speak to the AI as if it were the vendor.

The Chrome case is not new. Forever Security researcher Gal Weizman first detailed it publicly in March as [GlicJack](https://thehackernews.com/2026/03/new-chrome-vulnerability-let-malicious.html), and Google fixed it in early January 2026 in Chrome version 143.0.7499.192. It is tracked as [CVE-2026-0628](https://nvd.nist.gov/vuln/detail/CVE-2026-0628) and rated 8.8 out of 10 by the U.S. cybersecurity agency CISA, which set the score because the National Institute of Standards and Technology has not.

The other four are what Weizman added this year. Using the same idea, Forever Security said it reached the built-in AI in Comet, Edge, Opera Neon, and Claude in Chrome. Only the Edge finding received a CVE, [CVE-2026-55945](https://nvd.nist.gov/vuln/detail/CVE-2026-55945), a lower-severity issue rated 4.2 that Microsoft fixed in Edge version 150.0.4078.48 on July 2.

The Comet, Opera Neon and Claude findings have no CVE and rest on Forever Security's own account. The company said it earned about $20,000 in bug bounties across the five products, though its per-product figures add up to $20,500.

Forever Security listed what each attack could do.

| Capability | Chrome | Comet | Edge | Opera Neon | Claude in Chrome |
| --- | --- | --- | --- | --- | --- |
| Read local files | Yes | Yes | No | No | No |
| Camera and microphone | Yes | No | No | No | No |
| Control the AI agent | No | Yes | Yes | Yes | Yes |
| Leak browser profile | Yes | Yes | No | No | No |
| Leak browsing history | No | Yes | No | No | No |
| Take screenshots | Yes | Yes | No | No | No |
| No clicks needed | Yes | Yes | Yes | Yes | Yes |
| CVE | CVE-2026-0628 | None | CVE-2026-55945 | None | None |
| Bounty paid | $7,000 | $7,000 | $5,000 | $900 | $600 |

Comet was the worst case, the researchers said. Perplexity built Comet as a fully AI-driven browser, so its agent had broad powers: once hijacked, it could read any file on the computer, list the sites the user had visited, take screenshots, and act as the user.

Perplexity had blocked extensions from its main page, so Forever Security used a leftover test address, testing.perplexity.com, that was not locked down the same way.

Claude in Chrome was the mildest case, and Forever Security said so directly. "Claude in Chrome is a browser extension, not a browser," the company wrote, and it called the finding the least serious in the research because one extension was abusing another rather than an extension abusing a browser. Anthropic rated it medium severity and paid a bounty.

Forever Security also said Anthropic named it the first to report the Claude finding. That sits alongside earlier public reports about the same weak spot in the extension.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Security firm LayerX described a related flaw, called **ClaudeBleed**, in April, and Manifold Security [reported in July](https://thehackernews.com/2026/07/claude-for-chrome-flaw-lets-other.html) that a similar gap remained open in a later version. Edge was the hardest to break, the researchers said. Microsoft had tried to block the extension trick, so Forever Security combined two weaknesses. It took over a Microsoft marketing page that was allowed to send prompts to the Edge AI. It then used a timing flaw, called a race condition, to switch the agent between its "think" and "act" modes at the right moment, causing it to carry out a prompt.

Opera Neon was the easiest. Its AI took orders from opera.com, and Opera had not st...