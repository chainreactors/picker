---
title: Critical Docker Engine Flaw Allows Attackers to Bypass Authorization Plugins
url: https://thehackernews.com/2024/07/critical-docker-engine-flaw-allows.html
source: The Hacker News
date: 2024-07-26
fetch_date: 2025-10-06T17:52:05.595440
---

# Critical Docker Engine Flaw Allows Attackers to Bypass Authorization Plugins

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

# [Critical Docker Engine Flaw Allows Attackers to Bypass Authorization Plugins](https://thehackernews.com/2024/07/critical-docker-engine-flaw-allows.html)

**Jul 25, 2024**Ravie LakshmananContainer Security / Vulnerability

[![Critical Docker Engine Flaw](data:image/png;base64... "Critical Docker Engine Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwlnZVFYjopuxKbFc07dCazoDwkhl54bva_olPKxfsX8g972NfAyU0R6SXIbcAO7R4IolGtcWbHm_QTDkB10uVSGFQII2fO-bZydd2dMCcBKc1LebLgeuLhwIoFf6tQK7M9qKl4jQ8-1ganVP4Xcd4MTnHcgTNlRpnanGY7-SRAVuXh-pZpc_1emR1SXU9/s790-rw-e365/docker.png)

Docker is warning of a critical flaw impacting certain versions of Docker Engine that could allow an attacker to sidestep authorization plugins (AuthZ) under specific circumstances.

Tracked as **[CVE-2024-41110](https://github.com/moby/moby/security/advisories/GHSA-v23v-6jw2-98fq)**, the bypass and privilege escalation vulnerability carries a CVSS score of 10.0, indicating maximum severity.

"An attacker could exploit a bypass using an API request with Content-Length set to 0, causing the Docker daemon to forward the request without the body to the AuthZ plugin, which might approve the request incorrectly," the Moby Project maintainers said in an advisory.

Docker said the issue is a regression in that the issue was originally discovered in 2018 and addressed in Docker Engine v18.09.1 in January 2019, but never got carried over to subsequent versions (19.03 and later).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The issue has been resolved in versions 23.0.14 and 27.1.0 as of July 23, 2024, after the problem was identified in April 2024. The following versions of Docker Engine are impacted assuming AuthZ is used to make access control decisions -

* <= v19.03.15
* <= v20.10.27
* <= v23.0.14
* <= v24.0.9
* <= v25.0.5
* <= v26.0.2
* <= v26.1.4
* <= v27.0.3, and
* <= v27.1.0

"Users of Docker Engine v19.03.x and later versions who do not rely on authorization plugins to make access control decisions and users of all versions of Mirantis Container Runtime are not vulnerable," Docker's Gabriela Georgieva [said](https://www.docker.com/blog/docker-security-advisory-docker-engine-authz-plugin/).

"Users of Docker commercial products and internal infrastructure who do not rely on AuthZ plugins are unaffected."

It also affects Docker Desktop up to versions 4.32.0, although the company said the likelihood of exploitation is limited and it requires access to the Docker API, necessitating that an attacker already has local access to the host. A fix is expected to be included in a forthcoming release (version 4.33).

"Default Docker Desktop configuration does not include AuthZ plugins," Georgieva noted. "Privilege escalation is limited to the Docker Desktop [virtual machine], not the underlying host."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Although Docker makes no mention of CVE-2024-41110 being exploited in the wild, it's essential that users apply their installations to the latest version to mitigate potential threats.

Earlier this year, Docker moved to patch a set of flaws dubbed [Leaky Vessels](https://thehackernews.com/2024/02/runc-flaws-enable-container-escapes.html) that could enable an attacker to gain unauthorized access to the host filesystem and break out of the container.

"As cloud services rise in popularity, so does the use of containers, which have become an integrated part of cloud infrastructure," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/container-escape-techniques/) in a report published last week. "Although containers provide many advantages, they are also susceptible to attack techniques like container escapes."

"Sharing the same kernel and often lacking complete isolation from the host's user-mode, containers are susceptible to various techniques employed by attackers seeking to escape the confines of a container environment."

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

[Cloud computing](https://thehackernews.com/search/label/Cloud%20computing)[Container Security](https://thehackernews.com/search/label/Container%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DevOps](https://thehackernews.com/search/label/DevOps)[Docker](https://thehackernews.com/search/label/Docker)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[IT security](https://thehackernews.com/search/label/IT%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise ...