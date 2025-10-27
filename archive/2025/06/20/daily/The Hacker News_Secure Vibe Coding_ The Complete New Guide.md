---
title: Secure Vibe Coding: The Complete New Guide
url: https://thehackernews.com/2025/06/secure-vibe-coding-complete-new-guide.html
source: The Hacker News
date: 2025-06-20
fetch_date: 2025-10-06T22:59:19.687245
---

# Secure Vibe Coding: The Complete New Guide

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

# [Secure Vibe Coding: The Complete New Guide](https://thehackernews.com/2025/06/secure-vibe-coding-complete-new-guide.html)

**Jun 19, 2025**The Hacker NewsApplication Security / LLM Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlBrWxKRxNwPArXdmBDNM285vbutfSIyBBjglGzi1VaqT8dMwA8qMF8otBD4Ododi5o1gZEaoxTFOvdJkVgunpuRusp9vOmkBFIuUvigJSeUIxGz28TQfiiASkgeoQfP5JAReBpp-19EIfPrHpyx6MPkJHg3dm2hZVLcw2zWw6fZZT2JDJS9XevXW0eo0/s790-rw-e365/main-ref.jpg)

DALL-E for coders? That's the promise behind vibe coding, **a term** describing the use of natural language to create software. While this ushers in a new era of AI-generated code, it introduces "silent killer" vulnerabilities: exploitable flaws that evade traditional security tools despite perfect test performance.

A detailed analysis of secure vibe coding practices is available [here](https://www.reflectiz.com/learning-hub/secure-vibe-coding/).

## **TL;DR: Secure Vibe Coding**

Vibe coding, using natural language to generate software with AI, is revolutionizing development in 2025. But while it accelerates prototyping and democratizes coding, it also introduces "silent killer" vulnerabilities: exploitable flaws that pass tests but evade traditional security tools.

This article explores:

* Real-world examples of AI-generated code in production
* Shocking stats: 40% higher secret exposure in AI-assisted repos
* Why LLMs omit security unless explicitly prompted
* Secure prompting techniques and tool comparisons (GPT-4, Claude, Cursor, etc.)
* Regulatory pressure from the EU AI Act
* A practical workflow for secure AI-assisted development

Bottom line: AI can write code, but it won't secure it unless you ask, and even then, you still need to verify. **Speed without security is just fast failure.**

## **Introduction**

Vibe coding has exploded in 2025. Coined by Andrej Karpathy, it's the idea that anyone can describe what they want and get functional code back from large language models. In [Karpathy's words](https://x.com/karpathy/status/1886192184808149383), vibe coding is about "giving in to the vibes, embrace exponentials, and forget that the code even exists."

## **From Prompt to Prototype: A New Development Model**

This model isn't theoretical anymore. Pieter Levels (@levelsio) famously launched a multiplayer flight sim, [Fly.Pieter.com](https://fly.pieter.com), using AI tools like Cursor, Claude, and Grok 3. He created the first prototype in under 3 hours using just one prompt:

"Make a 3D flying game in the browser."

After 10 days, he had made [$38,000 from the game](https://open.spotify.com/episode/0H3krhS9ezT6GMHLdEFdyu) and was earning around $5,000 monthly from ads as the project scaled to 89,000 players by March 2025.

But it's not just games. Vibe coding is being used to build MVPs, internal tools, chatbots, and even early versions of full-stack apps. According to [recent analysis](https://www.ycombinator.com/library/ME-vibe-coding-is-the-future), nearly **25% of Y Combinator startups** are now using AI to build core codebases.

Before you dismiss this as ChatGPT hype, consider the scale: we're not talking about toy projects or weekend prototypes. These are funded startups building production systems that handle real user data, process payments, and integrate with critical infrastructure.

The promise? Faster iteration. More experimentation. Less gatekeeping.

**But there's a hidden cost to this speed.** AI-generated code creates what security researchers call "silent killer" vulnerabilities, code that functions perfectly in testing but contains exploitable flaws that bypass traditional security tools and survive CI/CD pipelines to reach production.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEij8Wvz9S2NwI10L1ZHCXiiFo9QAkdeSihbDfGUBYeBP1eabyd_bBuORspmFOCkz22dvdVQ9WBKG9HVZJmOccLbmLSAe9ZgqHtoURp2KoO5jdbZbiYg8vd4GcP6spxVHiCqUqEPTIogTEF1HBOn3GhACu_NRSyaq3hrlOvGTJU2Z7wCuiWMfaJ5AVJ9oe4/s790-rw-e365/1.jpg) |
| Sources: [Y Combinator research](https://www.ycombinator.com/library/ME-vibe-coding-is-the-future) | [GitGuardian research](https://blog.gitguardian.com/generic-secrets-beyond-github-push-protection/) | [Stanford University research](https://arxiv.org/pdf/2211.03622) |

## **The Problem: Security Doesn't Auto-Generate**

The catch is simple: **AI generates what you ask for, not what you forget to ask.** In many cases, that means critical security features are left out.

The problem isn't just naive prompting, it's systemic:

* LLMs are trained to *complete*, not *protect*. Unless security is explicitly in the prompt, it's usually ignored.
* Tools like GPT-4 may suggest deprecated libraries or verbose patterns that mask subtle vulnerabilities.
* Sensitive data is often hardcoded because the model "saw it that way" in training examples.
* Prompts like "Build a login form" often yield insecure patterns: plaintext password storage, no MFA, and broken auth flows.

According to this new [Secure Vibe Coding](https://www.reflectiz.com/learning-hub/secure-vibe-coding/) guide, this leads to what they call **"security by omission"**, functioning software that quietly ships with exploitable flaws. In one cited case, a developer used AI to fetch stock prices from an API and accidentally committed their hardcoded key to GitHub. A single prompt resulted in a real-world vulnerability.

**Here's another real example:** A developer prompted AI to "create a password reset function that emails a reset link." The AI generated working code that successfully sent emails and validated tokens. But it used a non-constant-time string comparison for token validation, creating a timing-based side-channel attack where attackers could brute-force reset tokens by measuring response times. The function passed all functional tests, worked perfectly for legitimate users, and would have been impossible to detect without specific security testing.

## **Technical Reality: AI Needs Guardrails...