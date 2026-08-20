---
title: Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second
url: https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html
source: The Hacker News
date: 2026-08-19
fetch_date: 2026-08-20T02:56:55.960259
---

# Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Cloudflare Workers Spectre Attack Leaks JWT From Co-Located Worker at 12 Bits/Second](https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html)

**Swati Khandelwal**Aug 19, 2026Cloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi50HcHSWt796lc8zQ8Anp_fHUqgV-BM0xiS1NxJW8zRDgBRJ9ovZOECiIhdQt0aVTUdhduJYP1o5wTa5RpDoCwhihq8rKqWmh73E9E8UzafyDcq1n1khCEIDCikK2L6NEt1mbIuMRm6F36bap74JtZawFqqCPvWF72SAm25BzREVerWYaRIDEo1O89V4k/s1700-e365/jwt.jpg)

Cybersecurity researchers have disclosed details of a [remote Spectre attack](https://thehackernews.com/2018/07/netspectre-remote-spectre-attack.html) against Cloudflare Workers that leaked a JSON Web Token (JWT) from a co-located Worker in the production environment at up to 12 bits per second, 360 times the rate of an earlier attack demonstrated in 2021.

The end-to-end experiment used an attacker Worker and a victim Worker controlled by the researchers, with the JWT intentionally placed in the victim's memory. The research paper stated that no customer data was accessed.

Cloudflare said the attack has already been mitigated in production after it improved Dynamic Process Isolation (DyPrIs), integrated the [V8 Sandbox](https://thehackernews.com/2024/04/google-chrome-adds-v8-sandbox-new.html), and deployed Memory Protection Keys (MPK)-based in-process isolation, adding that it found no indicators of active exploitation over the last three years.

"We demonstrate that the production implementation of DyPrIs was insufficient," the researchers said in [the paper](https://arxiv.org/abs/2608.17043).

Cloudflare Workers runs code from multiple tenants in separate V8 isolates within the same operating-system process, relying on language-level isolation instead of strict process isolation to reduce startup latency.

A memory read within a shared Worker process can lead to cross-tenant leakage, according to [Cloudflare](https://blog.cloudflare.com/spectre-research-with-tu-graz/). The attack requires the attacker and victim Workers to be co-located in separate V8 isolates within the same Worker process.

The attacker controls valid code in its own isolate. Native code execution is outside the threat model, and the attack does not depend on a V8 software exploit or sandbox escape.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Cloudflare said Workers restrict local timing sources by freezing or coarsening timers during CPU execution, and do not expose shared memory or multithreading to Worker scripts.

The researchers found that WebSocket communications could provide a remote timing source, while Durable Objects could keep a single Worker isolate alive for five to more than 20 hours.

DyPrIs isolates suspicious scripts into a separate process after an invocation finishes, and the researchers found that a long-lived Durable Object invocation could continue running before the isolation took place.

The researchers also found that WebSocket-heavy input/output (I/O) activity increased instruction translation lookaside buffer (iTLB) activity, reducing the normalized branch-misprediction signal used by DyPrIs below its detection threshold.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2P9lsQIBYYrENmRPWkTLD70K_DP2RD451qVz4X602ySb-t2mhKt_YFvK8LirDVL0iXDsl-RlRfrQY-mtWdgHVUnYkK9ahAVsCsgUjNKJDHHv_jMRTxMyOCqumq24KhI2O7WbHEXdoqXmCvv4Z4N8ZMzP82uNEK3NwQtXV34p8YRnOotyvqXOnxKEOxO0/s1700-e365/cf.jpg)

Cloudflare described the issue as a limitation in its DyPrIs implementation, while the paper said the two weaknesses reflected fundamental limitations of the detection approach rather than implementation oversights. The researchers said robust detection should take place during execution and use a signal that cannot be suppressed by I/O activity.

The paper said the production tests were conducted on Linux servers using AMD EPYC Zen 2 and Zen 3 processors, with the researchers intentionally running measurements at night, when CPU utilization was between 10% and 25%, to observe the best possible results.

The researchers said higher system load reduced the leakage rate, although slower attacks remained feasible under high load.

The paper reported leakage of up to 12 bits per second at 99.16% accuracy, compared with 2 bits per minute in the earlier attack.

The disclosure comes nearly five years after Cloudflare and TU Graz [published research](https://arxiv.org/abs/2110.04751) demonstrating a remote Spectre attack against Workers at 120 bits per hour and introducing DyPrIs as a defense.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The earlier paper reported a 0.61% false-positive rate and concluded that DyPrIs statistically provided the same security guarantees as strict process isolation against the Spectre attacks evaluated at the time.

Cloudflare published additional [Workers hardening measures](https://blog.cloudflare.com/safe-in-the-sandbox-security-hardening-for-cloudflare-workers/) in September 2025. The mitigations deployed by Cloudflare are listed below -

* **Improved DyPrIs** improves the detection capabilities of the existing isolation mechanism.
* **V8 Sandbox** limits transient access to 64-bit pointers.
* **MPK-based in-process isolation** places Worker heaps behind hardware-enforced protection keys. Cloudflare said modern x64 systems leave about 12 keys available for this purpose, and its design combines the keys with the V8 Sandbox and a rotating memory layout to prevent nearby sandboxes from sharing a key.

Cloudflare's September 2025 description said that random MPK assignment alone would trap about 92% of cross-isolate accesses because two isolates can receive the same key, and that the stricter rotating layout is used to remove that gap for the covered in-sandbox threat model.

Found this article interesting? Follow us on [Google News](https://news.goo...