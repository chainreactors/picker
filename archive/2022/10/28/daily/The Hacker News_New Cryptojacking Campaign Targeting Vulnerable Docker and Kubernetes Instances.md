---
title: New Cryptojacking Campaign Targeting Vulnerable Docker and Kubernetes Instances
url: https://thehackernews.com/2022/10/new-cryptojacking-campaign-targeting.html
source: The Hacker News
date: 2022-10-28
fetch_date: 2025-10-03T21:10:25.784442
---

# New Cryptojacking Campaign Targeting Vulnerable Docker and Kubernetes Instances

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

# [New Cryptojacking Campaign Targeting Vulnerable Docker and Kubernetes Instances](https://thehackernews.com/2022/10/new-cryptojacking-campaign-targeting.html)

**Oct 27, 2022**Ravie Lakshmanan

[![Cryptojacking](data:image/png;base64... "Cryptojacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEUnXpWUCT8hVKM-OsrQb2899AzYZzT5F7Sw-vKUR99Vqp0-TlJa14KyMOHCNKVOjxvCweZkL5wklXnKaLpe5lJjoEcqmbRBjqTP7WzR-vLjHYE46TNzTuYSHY35TFs5wogU6PY3tmXwqvOU8nbE4vZ0Ph6lU_KZFHA5yKHCK9iODfEiHBIW5-7P5E/s790-rw-e365/crypto-malware.jpg)

A new cryptojacking campaign has been uncovered targeting vulnerable Docker and Kubernetes infrastructures as part of opportunistic attacks designed to illicitly mine cryptocurrency.

Cybersecurity company CrowdStrike dubbed the activity **Kiss-a-dog**, with its command-and-control infrastructure overlapping with those associated with other groups like [TeamTNT](https://thehackernews.com/2022/09/hackers-targeting-weblogic-servers-and.html), which are known to [strike](https://thehackernews.com/2022/04/watch-out-cryptocurrency-miners.html) [misconfigured](https://www.trendmicro.com/en_us/research/22/i/how-malicious-actors-abuse-native-linux-tools-in-their-attacks.html) Docker and Kubernetes instances.

The intrusions, spotted in September 2022, get their name from a domain named "kiss.a-dog[.]top" that's used to trigger a shell script payload on the compromised container using a Base64-encoded Python command.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The URL used in the payload is obscured with backslashes to defeat automated decoding and regex matching to retrieve the malicious domain," CrowdStrike researcher Manoj Ahuje [said](https://www.crowdstrike.com/blog/new-kiss-a-dog-cryptojacking-campaign-targets-docker-and-kubernetes/) in a technical analysis.

The attack chain subsequently attempts to escape the container and move laterally into the breached network, while simultaneously taking steps to terminate and remove cloud monitoring services.

[![Cryptojacking](data:image/png;base64... "Cryptojacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmi5rQWlcjd7WO_WAapuE6nnf9axamV6Csa4g8C_E17qInP7dBrfylqu7n56h2Ah2rLtNNo31lijFzQTkUB5MLR__j7ERa5uz_Ofbz1PlXyB4xMeM9PVYzo4ELNADA8xw0-l2w5_w69yvM7B9n_uvNLlskkEc7ToU5D0cO20Bdq1VxM6GC3BjO1-m4ng/s790-rw-e365/malware-code.jpg)

As additional methods to evade detection, the campaign makes use of the [Diamorphine](https://github.com/m0nad/Diamorphine) and [libprocesshider](https://github.com/gianlucaborello/libprocesshider) rootkits to hide malicious processes from the user, the latter of which is compiled as a shared library and its [path](https://en.wikipedia.org/wiki/Path_%28computing%29) is set as the value for the [LD\_PRELOAD](https://www.cadosecurity.com/linux-attack-techniques-dynamic-linker-hijacking-with-ld-preload/) environment variable.

"This allows the attackers to inject malicious shared libraries into every process spawned on a compromised container," Ahuje said.

The ultimate goal of the campaign is to stealthily mine cryptocurrency using the XMRig mining software as well as to backdoor Redis and Docker instances for mining and other follow-on attacks.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"As cryptocurrency prices have dropped, these campaigns have been muffled in the past couple of months until multiple campaigns were launched in October to take advantage of a low competitive environment," Ahuje noted.

The findings also come as researchers from Sysdig took the wraps off another sophisticated crypto mining operation dubbed PURPLEURCHIN, which leverages the compute allocated for free trial accounts across GitHub, Heroku, and Buddy[.]Works to scale the attacks.

As many as 30 GitHub accounts, 2,000 Heroku accounts, and 900 Buddy accounts are said to have been utilized in the automated freejacking campaign.

The attack entails the creation of an actor-controlled GitHub account, each containing a repository that, in turn, has a [GitHub Action](https://thehackernews.com/2022/07/cloud-based-cryptocurrency-miners.html) to run mining operations by launching a Docker Hub image.

"Using free accounts shifts the cost of running the cryptominers to the service provider," the researchers [said](https://sysdig.com/blog/massive-cryptomining-operation-github-actions/). "However, like many fraud-use cases, the abuse of free accounts can affect others. Higher expenses for the provider will lead to higher prices for its legitimate customers."

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[Docker Container](https://thehackernews.com/search/label/Docker%20Container)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote...