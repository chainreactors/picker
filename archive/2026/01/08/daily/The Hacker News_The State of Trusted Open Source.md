---
title: The State of Trusted Open Source
url: https://thehackernews.com/2026/01/the-state-of-trusted-open-source.html
source: The Hacker News
date: 2026-01-08
fetch_date: 2026-01-09T03:32:02.508453
---

# The State of Trusted Open Source

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [The State of Trusted Open Source](https://thehackernews.com/2026/01/the-state-of-trusted-open-source.html)

**Jan 08, 2026**The Hacker NewsDevSecOps / Compliance

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZoKSxRFayxkvrH0IbQJcIVluEGBHP48Adp3NIQ48I_QbNUy3N91tDM6UFfvq-OrbLJkBz91GjwO9Qb_iEtDHgha1j6IYbWqtemdZ19MF0cdUrdtRfZDwf_3QT_gJk1BkqUdxer3wz80NZUw6-hHGdr_hA6LRwSo1zYxa4Q34tGLLCnxiv-xtnSAQYj58/s790-rw-e365/Chainguard.jpg)

Chainguard, the trusted source for open source, has a unique view into how modern organizations actually consume open source software and where they run into risk and operational burdens. Across a growing customer base and an extensive catalog of over 1800 container image projects, 148,000 versions, 290,000 images, and 100,000 language libraries, and almost half a billion builds, they can see what teams pull, deploy, and maintain day-to-day, along with the vulnerabilities and remediation realities that come hand in hand.

That's why they created *The State of Trusted Open Source*, a quarterly pulse on the open source software supply chain. As they analyzed anonymized product usage and CVE data, the Chainguard team noticed common themes around what open source engineering teams are actually building with and the risks associated.

Here's what they found:

* **AI is reshaping the baseline stack:** Python led the way as the most popular open source image among Chainguard's global customer base, powering the modern AI stack.
* **Over half of production happens outside of the most popular projects:** Most teams may standardize on a familiar set of images, but real-world infrastructure is powered by a broad portfolio that extends far beyond the top 20 most popular, which they refer to in this report as longtail images.
* **Popularity doesn't map to risk:** 98% of the vulnerabilities found and remediated in Chainguard images occurred outside of the top 20 most popular projects. That means the biggest security burden accumulates in the less-visible part of the stack, where patching is hardest to operationalize.
* **Compliance can be the catalyst for action:** Compliance takes many forms today: from SBOM and vulnerability requirements to industry frameworks like PCI DSS, SOC 2, and regulations like the EU's Cyber Resilience Act. FIPS is just one example, focused specifically on U.S. federal encryption standards. Even so, 44% of Chainguard customers run a FIPS image in production, underscoring how frequently regulatory needs shape real-world software decisions.
* **Trust is built on remediation speed:** Chainguard eliminated Critical CVEs, on average, in under 20 hours.

Before we dive in, a note on the methodology: This report analyzes 1800+ unique container image projects, 10,100 total vulnerability instances, and 154 unique CVEs tracked from September 1, 2025, through November 30, 2025. When we use terms like "top 20 projects" and "longtail projects" (as defined by images outside of the top 20), we're referring to real usage patterns observed across Chainguard's customer portfolio and in production pulls.

## **Usage: What teams actually run in production**

If you zoom out, today's production container footprint looks exactly like you'd expect: foundational languages, runtimes, and infrastructure components dominate the most popular list.

### **Most popular images: AI is reshaping the baseline stack**

Across all regions, the top images are familiar staples: Python (71.7% of customers), Node (56.5%), nginx (40.1%), go (33.5%), redis (31.4%), followed by JDK, JRE, and a cluster of core observability and platform tooling like Grafana, Prometheus, Istio, cert-manager, argocd, ingress-nginx, and kube-state-metrics.

This indicates that customers operate a portfolio of critical building blocks – including languages, gateways, service mesh, monitoring, and controllers – that collectively form the foundation of their business.

It's not surprising to see Python leading the way globally, as the default glue language for the modern AI stack. Teams typically standardize on Python for model development, data pipelines, and increasingly for production inference services as well.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhR9CByDOdXsz4yy3XK7OMy19LbGvGhmNq9htpH4_6wbi5j3wUvBbel3WM0zMBDkRdt8ndlIsK5jnWOnxzLolXEMsq1InvEUNKUD962ti1WISfAV6bacKbSK_o14CbuR-xNFwmFdd2uOdpbQrwHn_IhcWhJkRr7J9MFXyynZGOAJYUWFF1bIV9PjrpsSyA/s790-rw-e365/Chainguard-1.png)

### **Most popular by region: Similar foundations, different longtail mix**

North America shows a broad and consistent set of default production building blocks: Python (71.7% of customers), Node (56.6%), nginx (39.8%), go (31.9%), redis (31.5%), plus strong penetration of Kubernetes ecosystem components (cert-manager, istio, argocd, prometheus, kube-state-metrics, node-exporter, kubectl). Notably, even utility images like busybox show up meaningfully.

Outside North America, the same core stack appears, but the portfolio spreads differently: Python (72% of customers), Node (55.8%), Go (44.2%), nginx (41.9%), and a noticeable presence of .NET runtimes (aspnet-runtime, dotnet-runtime, dotnet-sdk) and PostgreSQL.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh81p7XS-3IpuaGO_SEH6AyDGaIiuRDXMJxhHuR3ZuKwHOE_1KVFmBYo5UB0HN6cKFMzHzu2bBCpprrFHCNOEcF6hXGg5GYu9-AdopxJSkSxB5MmJ1G-dQ-6a02EMA7jm9JqknW_HcnQzibg1hpUY9ozKDIX-Vf0SR8Z6V9eDcPvQ0hzChyphenhyphenilmGn4sZcjc/s790-rw-e365/Chainguard-2.png)

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmM5OkON-1jZNrCPCNrHJVvAgMZPVGLCviRRvTMoFXtyjbeBJYkmRwiLnR4F-znytA-byFjpd_LQB9PNqOk8y_7jzkTo4_TGgNCXHYLBDcPmbpxvrO1JDO7LOFpIbYDbbYWvalZnwDSBn0Usa72MsxckRyXzZvwJas8yFQAVEZl7jUeS6wrOVgG3UIyYs/s790-rw-e365/Chainguard-3.png)

### **The longtail of images is crucial to production, not edge cases**

Chainguard's most popular images represent only 1.37% of all available images and account f...