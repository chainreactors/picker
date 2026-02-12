---
title: Exposed Training Open the Door for Crypto-Mining in Fortune 500 Cloud Environments
url: https://thehackernews.com/2026/02/exposed-training-open-door-for-crypto.html
source: The Hacker News
date: 2026-02-11
fetch_date: 2026-02-12T04:23:18.760098
---

# Exposed Training Open the Door for Crypto-Mining in Fortune 500 Cloud Environments

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

# [Exposed Training Open the Door for Crypto-Mining in Fortune 500 Cloud Environments](https://thehackernews.com/2026/02/exposed-training-open-door-for-crypto.html)

**The Hacker News**Feb 11, 2026Identity Security / Threat Exposure

[![](data:image/png;base64...)](https://go.pentera.io/pentera-labs-exposed-cloud-training-apps?utm_source=thn&utm_medium=eblast&utm_campaign=pentera_labs_door)

Intentionally vulnerable training applications are widely used for security education, internal testing, and product demonstrations. Tools such as OWASP Juice Shop, DVWA, Hackazon, and bWAPP are designed to be insecure by default, making them useful for learning how common attack techniques work in controlled environments.

The issue is not the applications themselves, but how they are often deployed and maintained in real-world cloud environments.

Pentera Labs examined how training and demo applications are being used across cloud infrastructures and identified a recurring pattern: applications intended for isolated lab use were frequently found exposed to the public internet, running inside active cloud accounts, and connected to cloud identities with broader access than required.

### **Deployment Patterns Observed in the Research**

[Pentera Labs research](https://go.pentera.io/pentera-labs-exposed-cloud-training-apps?utm_source=thn&utm_medium=eblast&utm_campaign=pentera_labs_door) found that these applications were often deployed with default configurations, minimal isolation, and overly permissive cloud roles. The investigation uncovered that many of these exposed training environments were directly connected to active cloud identities and privileged roles, enabling attackers to move far beyond the vulnerable applications themselves and potentially into the customer’s broader cloud infrastructure.

In these scenarios, a single exposed training application can act as an initial foothold. Once attackers are able to leverage connected cloud identities and privileged roles, they are no longer constrained to the original application or host. Instead, they may gain the ability to interact with other resources within the same cloud environment, significantly increasing the scope and potential impact of the compromise.

As part of the investigation, Pentera Labs verified nearly **2,000 live, exposed training application instances**, with close to **60% hosted on customer-managed infrastructure running on AWS, Azure, or GCP**.

[![](data:image/png;base64...)](https://go.pentera.io/pentera-labs-exposed-cloud-training-apps?utm_source=thn&utm_medium=eblast&utm_campaign=pentera_labs_door)

### **Evidence of Active Exploitation**

The exposed training environments identified during the research were not simply misconfigured. Pentera Labs observed clear evidence that attackers were actively exploiting this exposure in the wild.

Across the broader dataset of exposed training applications, approximately **20% of instances were found to contain artifacts deployed by malicious actors**, including crypto-mining activity, webshells, and persistence mechanisms. These artifacts indicated prior compromise and ongoing abuse of exposed systems.

The presence of active crypto-mining and persistence tooling demonstrates that exposed training applications are not only discoverable but are already being exploited at scale.

### **Scope of Impact**

The exposed and exploited environments identified during the research were not limited to small or isolated test systems. Pentera Labs observed this deployment pattern across cloud environments associated with **Fortune 500 organizations and leading cybersecurity vendors,** including Palo Alto, F5, and Cloudflare.

While individual environments varied, the underlying pattern remained consistent: a training or demo application deployed without sufficient isolation, left publicly accessible, and connected to privileged cloud identities.

### **Why This Matters**

Training and demo environments are frequently treated as low-risk or temporary assets. As a result, they are often excluded from standard security monitoring, access reviews, and lifecycle management processes. Over time, these environments may remain exposed long after their original purpose has passed.

The research shows that exploitation does not require zero-day vulnerabilities or advanced attack techniques. Default credentials, known weaknesses, and public exposure were sufficient to turn training applications into an entry point for broader cloud access.

Labeling an environment as “training” or “test” does not reduce its risk. When exposed to the internet and connected to privileged cloud identities, these systems become part of the organization’s effective attack surface.

Refer to the full **[Pentera Labs research blog](https://go.pentera.io/pentera-labs-exposed-cloud-training-apps?utm_source=thn&utm_medium=eblast&utm_campaign=pentera_labs_door)** & [join a live webinar on Feb 12th](https://go.pentera.io/pentera-labs-exposed-cloud-training-apps-webinar?utm_source=THN&source=THN&utm_medium=article&medium=article&utm_campaign=pentera%20labs%20door&campaign=pentera%20labs%20door) to learn more about the methodology, discovery process, and real-world exploitation observed during this research.

*This article was written by Noam Yaffe, Senior Security Researcher at Pentera Labs. For questions or discussion, contact labs@pentera.io*

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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
[...