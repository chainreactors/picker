---
title: Over 300K Prometheus Instances Exposed: Credentials and API Keys Leaking Online
url: https://thehackernews.com/2024/12/296000-prometheus-instances-exposed.html
source: The Hacker News
date: 2024-12-13
fetch_date: 2025-10-06T19:42:20.258998
---

# Over 300K Prometheus Instances Exposed: Credentials and API Keys Leaking Online

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

# [Over 300K Prometheus Instances Exposed: Credentials and API Keys Leaking Online](https://thehackernews.com/2024/12/296000-prometheus-instances-exposed.html)

**Dec 12, 2024**Ravie LakshmananVulnerability / Cloud Security

[![296,000 Prometheus](data:image/png;base64... "296,000 Prometheus")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilxvzp7qifblFeuL3ZoafBcE1HWFEiK00Lo9dmjf4qlisZ4iKgZRYAZ0UvUt8Juk8AVQvLV5HNsUa3YZdU-O6oyfIYbCsMSP76Ogi3jOabCm-30Ch8EG-OrLyRxkNKqc5pEWjyoYuBFvRMLoT7NaXcKtMcGspZy1Au1ny2cRyI-LDJuG4GcTR7YFbSf2Cj/s790-rw-e365/serves-hacking.png)

Cybersecurity researchers are warning that thousands of servers hosting the Prometheus monitoring and alerting toolkit are at risk of information leakage and exposure to denial-of-service (DoS) as well as remote code execution (RCE) attacks.

"Prometheus servers or [exporters](https://prometheus.io/docs/instrumenting/exporters/), often lacking proper authentication, allowed attackers to easily gather sensitive information, such as credentials and API keys," Aqua security researchers Yakir Kadkoda and Assaf Morag [said](https://www.aquasec.com/blog/300000-prometheus-servers-and-exporters-exposed-to-dos-attacks/) in a new report shared with The Hacker News.

The cloud security firm also said that the exposure of the ["/debug/pprof" endpoints](https://training.promlabs.com/training/monitoring-and-debugging-prometheus/profiling/overview/) used for determining heap memory usage, CPU usage, and others, could serve as a vector for DoS attacks, rendering the servers inoperable.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As many as 296,000 [Prometheus Node Exporter](https://prometheus.io/docs/guides/node-exporter/) instances and 40,300 Prometheus servers have been estimated to be publicly accessible over the internet, making them a huge attack surface that could put data and services at risk.

The fact that sensitive information, such as credentials, passwords, authentication tokens, and API keys, could be leaked through internet-exposed Prometheus servers has been documented previously by [JFrog](https://thehackernews.com/2021/10/experts-warn-of-unprotected-prometheus.html) in 2021 and [Sysdig](https://sysdig.com/blog/exposed-prometheus-exploit-kubernetes-kubeconeu/) in 2022.

"Unauthenticated Prometheus servers enable direct querying of internal data, potentially exposing secrets that attackers can exploit to gain an initial foothold in various organizations," the researchers said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5rlnkl8fitk4HNdKG6Q8W43cQ3qnON-qAk4XGhdN0sdOfJSBjXEOD3kMCLZ6iesum6n-741B6buzasD8c06R5qlMd_yKbViDxf-A8dk16k0KZbO8GwlmuoFoxVtQ1dpZ8s6kyDvCa4ZrgT9adXDhNa9Mxir2hgszegrJyDAToIpybVhV7fDxMoM9GgZm5/s790-rw-e365/server.png)

In addition, it has been found that the "/metrics" endpoint can not only reveal internal API endpoints, but also data about subdomains, Docker registries, and images -- all valuable information for an attacker conducting reconnaissance and looking to expand their reach within the network.

That's not all. An adversary could send multiple simultaneous requests to endpoints like "/debug/pprof/heap" to trigger CPU and memory-intensive heap profiling tasks that can overwhelm the servers and cause them to crash.

Aqua further called out a supply chain threat that involves using repojacking techniques to leverage the name associated with deleted or renamed GitHub repositories and introduce malicious third-party exporters.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Specifically, it discovered that eight exporters listed in Prometheus' [official documentation](https://prometheus.io/docs/instrumenting/exporters/) are vulnerable to [RepoJacking](https://thehackernews.com/2023/12/15000-go-module-repositories-on-github.html), thereby [allowing](https://github.blog/security/supply-chain-security/how-to-stay-safe-from-repo-jacking/) an attacker to recreate an exporter with the same name and host a rogue version. These issues have since been [addressed](https://github.com/prometheus/docs/pull/2505/commits/dab10480a022adb0a15d05bbc1417801910e82c4) by the Prometheus security team as of September 2024.

"Unsuspecting users following the documentation could unknowingly clone and deploy this malicious exporter, leading to remote code execution on their systems," the researchers said.

Organizations are recommended to secure Prometheus servers and exporters with adequate authentication methods, limit public exposure, monitor "/debug/pprof" endpoints for any signs of anomalous activity, and take steps to avoid RepoJacking attacks.

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

[Authentication](https://thehackernews.com/search/label/Authentication)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[monitoring](https://thehackernews.com/search/label/monitoring)[Prometheus](https://thehackernews.com/search/label/Prometheus)[RepoJacking](https://thehackernews.com/search/label/RepoJacking)[Supply Chain](https://thehackern...