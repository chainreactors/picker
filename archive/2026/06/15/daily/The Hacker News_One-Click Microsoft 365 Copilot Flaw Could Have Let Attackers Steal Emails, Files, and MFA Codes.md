---
title: One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes
url: https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html
source: The Hacker News
date: 2026-06-15
fetch_date: 2026-06-16T07:17:03.610788
---

# One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [One-Click Microsoft 365 Copilot Flaw Could Have Let Attackers Steal Emails, Files, and MFA Codes](https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html)

**Swati Khandelwal**Jun 15, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgH3B8zgsVZmHEyLi8McE-eOrGvwf6Uh3zyqWrttvaEddXJCot7sybI1o-Ly5Q1TtuEJx9BzXol3oaXSFdzFif_5fg0TE3bFA7cuuNewVB2QiZC9HuWNsVDLZlpANK_qnbk_DfBgO1fRgpUbYbc_dL60zHQFxxFN4DgYDVI-D1LsA-8dkcVKpNjAStg9b4/s1700-e365/ms365.jpg)

A single click on a trusted Microsoft link could have let an attacker pull emails, calendar details, and indexed files out of Microsoft 365 Copilot Enterprise Search.

Researchers at Varonis Threat Labs chained three bugs into a one-click exfiltration path they call **SearchLeak**. Because the link pointed to a real microsoft.com domain, traditional anti-phishing and URL filtering tools were unlikely to flag it.

No prompt, no password, no second click. Microsoft assigned [CVE-2026-42824](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42824) and marked it critical; the CVSS scores ran lower and disagreed, 6.5 from Microsoft and 7.5 from the [National Vulnerability Database](https://nvd.nist.gov/vuln/detail/CVE-2026-42824). The company mitigated the flaw on its backend, so customers have nothing to worry about, and Varonis presented a proof-of-concept, not observed exploitation.

## Three bugs, one click

Microsoft's advisory describes the flaw as a command injection that can expose information over a network. In practice, SearchLeak stacks one AI-specific weakness on two old web bugs, and each link is needed for the next.

The entry point is the **q** parameter in the Copilot Enterprise Search URL. It is meant for a natural-language query, but Copilot reads whatever sits there as instructions, not just a search string.

[Varonis](https://www.varonis.com/blog/searchleak) calls this **Parameter-to-Prompt injection**. An attacker writes a URL that tells Copilot to search the mailbox, take an email title, and place it inside an image URL. The victim types nothing. They click, and Copilot does the work.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Next is a race condition in how the response renders. Microsoft's guardrail wraps Copilot output in **<code>** blocks so the browser treats markup as text. The catch is timing: the wrapping happens after Copilot finishes generating, but the browser renders the stream as it arrives. The injected **<img>** tag is drawn and fires its request before the sanitizer runs. By the time the output is neutralized, the request has already left.

The last link gets the data past the page's Content Security Policy. The CSP on m365.cloud.microsoft blocks images from arbitrary domains, but it allowlists \*.bing.com. Bing's "Search by Image" endpoint accepts an image URL and fetches it server-side to analyze it. Point that fetch at an attacker's server with the stolen text encoded in the path, and Bing retrieves it. The browser's CSP never applies, because the request comes from Bing's infrastructure. Bing becomes the exfiltration proxy. The CSP allowlist does the hiding.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHil70ZIYTT6xWWda3ydur8oehimc0ctJwEB-VHp-JVL6nwtsEfraD957lLRArQJSWQCNHrlZLMTWxx1wdU2aJsYxHUf_2Jv0-Uz-W3fg6GxitiLXWhlHDf5p84nELVuPOh7qDWd-X9Qx25SR301PT4BktufkFGp0lt_xGc25z5vyl5rCwV0EHGVDCU6Y/s1700-e365/flow.png)

Put together: the victim clicks, Copilot searches their data, the response embeds a value like an email subject in a Bing image URL, the browser calls Bing during streaming, and Bing pulls the attacker's URL. The attacker reads it off their own logs, for example, a request for /Your\_Security\_Code\_847291/img.png.

## What an attacker gets

Copilot Enterprise can reach whatever the signed-in user can, through their Microsoft Graph access, and the attacker inherits that reach without ever logging in.

The most time-sensitive prize sits in the inbox: one-time codes, MFA codes, and password-reset links, often still valid for a few minutes. A script that lifts those off a log while the window is open can take over an account before anyone notices.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The same access also reaches calendar invites, meeting notes, and any SharePoint or OneDrive file Copilot has indexed, where the salary data, earnings figures, and acquisition plans live.

SearchLeak is the second time Varonis has shown this pattern. Varonis researcher Dolev Taler demonstrated the same one-click technique in an [earlier Reprompt attack](https://thehackernews.com/2026/01/researchers-reveal-reprompt-attack.html) against Copilot Personal, and it held up against Enterprise Search despite the extra guardrails that tier is supposed to enforce.

The same pattern showed up in [EchoLeak](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html) (CVE-2025-32711), the zero-click Copilot data-leak bug Aim Security disclosed in 2025. SSRF and sanitizer races are old bug classes; the prompt injection is the new part, and it makes them reachable again.

Microsoft mitigated the flaw on its backend, and because Copilot Enterprise is a managed service, tenant admins cannot patch or reconfigure the parts that failed. What they can do is watch and contain.

Look for Copilot Search URLs carrying encoded payloads or HTML in the q parameter, and for unusual outbound requests to Bing's image endpoints. Tighten data-access governance so Copilot indexes less, which shrinks what any future leak can reach.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) t...