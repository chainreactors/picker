---
title: ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More
url: https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html
source: The Hacker News
date: 2026-09-07
fetch_date: 2026-09-08T06:42:26.613322
---

# ⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More

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

# [⚡ Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack and More](https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html)

**Ravie Lakshmanan**Sep 07, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3SJbgfzjY0QMdutDU1Lf8A1ZVh6S-hcQEwATiHIXXKIpYhh1mrojhkxootev2lhFxjehrTS8h3UNmZgHBwgxNUN0ho2r5Tzk2PRLqK_yO-4OetzmlaFE5V5z0G-Yp34y_RWR5ZlWoL51LWMOFh8YTZCKDADDnHFLhYZl5oQkqLFxJ9JHK1j35kxilIkyp/s1700-nu-rw-lo-l85-e365/recaps.jpg)

Turning off email images should at least stop the pictures. This week, attackers had a workaround: a scannable QR code built out of text. It still appears, even with images blocked. A small detail, but an annoying one if that was a precaution you were counting on.

Elsewhere, a trusted software source delivered code that stole credentials, and a protocol designed for secure network management gave outsiders useful clues before login. Add active attacks on browsers, routers, and online stores, and there’s plenty to check—even for teams that have kept up with the patches.

Read the full recap for the week’s major developments, plus more research, attacks, and security news beyond what we covered last week.

## **⚡ Threat of the Week**

**[N-able Patches Critical N-central Flaws](https://thehackernews.com/2026/09/n-able-issues-fourth-n-central-hotfix.html)** — N-able has released hotfixes to address two severe N-central flaws (CVE-2026-86206 and CVE-2026-86207) that could allow an unauthorized party to bypass authentication controls and gain full access to the platform. Also patched is a maximum-severity security flaw (CVE-2026-86218, CVSS score: 10.0) that could allow for pre-authenticated remote code execution on the N-central server. "At this time, we have no confirmation that these vulnerabilities have been exploited in production environments, but unpatched systems remain at risk," N-able said. However, Huntress said it observed signs that attackers are likely leveraging CVE-2026-86206 or/and CVE-2026-86207, after it launched an investigation on September 4 following the compromise of a customer's fully patched N-central production environment. "However, due to limited historical logging available directly on the appliance, we cannot definitively confirm which specific exploit the threat actor used to achieve their compromise, nor can we rule out the use of alternative vulnerabilities," it said.

[![AI Spend Out of Control](data:image/png;base64... "AI Spend Out of Control")

## AI Spend Out of Control? There's a Path Forward

Imagine you’ve received a water bill for 500,000,000 gallons. Now, you have to account for every teaspoon of that water. IT leaders face a similar task when managing AI budgets, and it’s not as simple as token caps or model limits. Learn how your team can optimize your company's AI spend.](https://thehackernews.uk/ai-spend-guide)
[Learn More ➝](https://thehackernews.uk/ai-spend-guide)

## **🔔 Top News**

* **[Google Warns of Chrome 0-Day Under Attack](https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html)** — Google released security updates to patch 12 vulnerabilities, including one that has come under active exploitation in the wild. The high-severity vulnerability, tracked as CVE-2026-85046 (CVSS score: 8.8), has been described as a type confusion bug in V8, Chrome's JavaScript and WebAssembly engine. "Type confusion in V8 in Google Chrome prior to 152.0.7977.82 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page," according to a description of the flaw in CVE.org. Security researcher Salvatore Gulizia (aka Serotav) has been credited with discovering and reporting the flaw on August 4, 2026. As is usual in these cases, Google acknowledged that an "exploit for CVE-2026-85046 exists in the wild," but did not reveal any details about the nature of the attacks or who is behind them. With the latest development, Google has addressed a total of six actively exploited Chrome zero-days since the start of the year.
* **[MikroTik RouterOS Flaws Exploited](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html)** — The CERT Polska Team warned that bad actors are actively exploiting two zero-day flaws in MikroTik RouterOS that could be combined to take full control of the device without authentication if the device supports remote access using the SSH protocol. The exploit chain has been codenamed MikroTrick. A total of fix flaws (CVE-2026-67276, CVE-2026-67277, CVE-2026-67278, CVE-2026-67279, CVE-2026-67281, and CVE-2026-86060) have been identified. The MikroTrick chain involves CVE-2026-67276 and CVE-2026-86060 (CVSS scores: 9.2), which can allow an attacker to bypass authentication and elevate their privileges. The issues have been fixed in versions 6.49.21 (Long-term), 7.23.4 (Long-term), and 7.24.2 (Stable). "The successful attacks observed so far, including the creation of the 'ops' account, originated from the IP address 82.192.72.4 and have been occurring since at least 2 September," CERT Polska said. "In addition, the IP address 103.102.31.18 was used in attempts to exploit the described chain."
* **[Unpatched Magento and Adobe Commerce 0-Day Exploited to Backdoor Online Stores](https://thehackernews.com/2026/09/unpatched-magento-and-adobe-commerce.html)** — E-commerce storefronts are being compromised to inject a backdoor by exploiting an unpatched Magento and Adobe Commerce zero-day dubbed StyleSmuggler, which gives unauthenticated attackers remote code execution. The attacks commenced on September 4, 2026. "StyleSmuggler injects malicious code into Magento's template system," Sansec said. "By using the styles properties, it can evade existing safeguards. It works in two stages: (1) Inject (poison) PHP code, for example by generating a failure report, and (2) Let Magento execute the poisoned code via a failed payment email." The backdoor is a Rust ...