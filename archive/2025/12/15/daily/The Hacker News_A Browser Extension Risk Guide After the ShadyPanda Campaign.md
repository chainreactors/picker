---
title: A Browser Extension Risk Guide After the ShadyPanda Campaign
url: https://thehackernews.com/2025/12/a-browser-extension-risk-guide-after.html
source: The Hacker News
date: 2025-12-15
fetch_date: 2025-12-16T03:24:40.415446
---

# A Browser Extension Risk Guide After the ShadyPanda Campaign

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [A Browser Extension Risk Guide After the ShadyPanda Campaign](https://thehackernews.com/2025/12/a-browser-extension-risk-guide-after.html)

**Dec 15, 2025**The Hacker NewsBrowser Security / SaaS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAAYMfLInHfns5nX7hk3SOBwCvMca-7usfovrOLFewfHgZtx0972jWlVx8u1MVE0_WqJCnczK6ZFXTZ-ir-grtXiWZcXJw6eGWzTX7supbbmuFOPY2fxfgdqcRAP_dpIW4fGawNEFOdY1wfUVlhaL4lx3_HjP20Ql7NEsL3oVu6s2xceDq0DHz_JyQU2Y/s790-rw-e365/reco.jpg)

In early December 2025, security researchers exposed a cybercrime [campaign](https://www.koi.ai/blog/4-million-browsers-infected-inside-shadypanda-7-year-malware-campaign) that had quietly hijacked popular Chrome and Edge browser extensions on a massive scale.

A threat group dubbed ShadyPanda spent seven years playing the long game, publishing or acquiring harmless extensions, letting them run clean for years to build trust and gain millions of installs, then suddenly flipping them into malware via silent updates. In total, about 4.3 million users installed these once-legitimate add-ons, which suddenly went rogue with spyware and backdoor capabilities.

This tactic was essentially a browser extension supply-chain attack.

The ShadyPanda operators even earned featured and verified badges in the official Chrome Web Store and Microsoft Edge Add-ons site for some extensions, reinforcing user confidence. Because extension updates happen automatically in the background, the attackers were able to push out malicious code without users noticing a thing.

Once activated in mid-2024, the compromised extensions became a fully fledged remote code execution (RCE) framework inside the browser. They could download and run arbitrary JavaScript with full access to the browser's data and capabilities. This gave the attackers a range of spyware powers, from monitoring every URL and keystroke, to injecting malicious scripts into web pages, to exfiltrating browsing data and credentials.

One of the worst capabilities was session cookie and token theft, stealing the authentication tokens that websites use to keep users logged in. The extensions could even impersonate entire SaaS accounts (like Microsoft 365 or Google Workspace) by hijacking those session tokens.

## **Why Browser Extensions Are a SaaS Security Nightmare**

For SaaS security teams, ShadyPanda's campaign shows us a lot. It proved that a malicious browser extension can effectively become an intruder with keys to your company's SaaS kingdom. If an extension grabs a user's session cookie or token, it can unlock that user's accounts in Slack, Salesforce, or any other web service they're logged into.

In this case, millions of stolen session tokens could have led to unauthorized access to enterprise emails, files, chat messages, and more, all without triggering the usual security alarms. Traditional identity defenses like MFA were bypassed, because the browser session was already authenticated and the extension was piggybacking on it.

The risk extends beyond just the individual user. Many organizations allow employees to install browser extensions freely, without the scrutiny applied to other software. Browser extensions often slip through without oversight, yet they can access cookies, local storage, cloud auth sessions, active web content, and file downloads.

This blurs the line between endpoint security and cloud security. A malicious extension can be run on the user's device (an endpoint issue), but it directly compromises cloud accounts and data (an identity/SaaS issue). ShadyPanda vividly shows the need to bridge endpoint and SaaS identity defense: security teams should think about treating the browser as an extension of the SaaS attack surface.

## **Steps to Reduce Browser Extension Risk**

So based on all of this, what can organizations do to reduce the risk of another ShadyPanda situation? Below is a practical guide with steps to tighten your defenses against malicious browser extensions.

### **1. Enforce Extension Allow Lists and Governance**

Start by regaining control over which extensions can run in your environment. Conduct an audit of all extensions installed across the company's browsers (both corporate-managed and BYOD if possible) and remove any that are unnecessary, unvetted, or high risk.

It's wise to require business justification for extensions that need broad permissions (for example, any addon that can read all website data). Use enterprise browser management tools to implement an allow list so that only approved extensions can be installed. This policy ensures new or unknown extensions are blocked by default, cutting off the long tail of random installs.

Remember that popular extensions aren't automatically safe, ShadyPanda's malware hid in popular, trusted extensions that people had used for years. Treat all extensions as guilty until proven innocent by vetting them through your security team's approval process.

### **2. Treat Extension Access Like OAuth Access**

Shift your mindset to treat browser extensions similarly to third-party cloud apps in terms of the access they grant. In practice, this means integrating extension oversight into your identity and access management processes.

Just as you might keep a catalog of authorized OAuth integrations, do the same for extensions. Map out what SaaS data or actions an extension could touch - for example, if an extension can read all web traffic, it effectively can read your SaaS application data in transit; if it can read cookies, it can impersonate the user on any service.

Because malicious extensions can steal session tokens, your identity security tools should watch for signs of session hijacking: configure alerts for bizarre login patterns, like an OAuth token being used from two different locations, or an access attempt that bypasses MFA checks.

The key point is to manage extensions with the same caution as any app that has been granted access to your data. Limit extension permissions where possible, and if an employee...