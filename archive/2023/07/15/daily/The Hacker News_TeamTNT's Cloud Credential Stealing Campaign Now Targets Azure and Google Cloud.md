---
title: TeamTNT's Cloud Credential Stealing Campaign Now Targets Azure and Google Cloud
url: https://thehackernews.com/2023/07/teamtnts-cloud-credential-stealing.html
source: The Hacker News
date: 2023-07-15
fetch_date: 2025-10-04T11:55:44.487277
---

# TeamTNT's Cloud Credential Stealing Campaign Now Targets Azure and Google Cloud

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

# [TeamTNT's Cloud Credential Stealing Campaign Now Targets Azure and Google Cloud](https://thehackernews.com/2023/07/teamtnts-cloud-credential-stealing.html)

**Jul 14, 2023**Ravie LakshmananCyber Threat / Cloud Security

[![Azure and Google Cloud](data:image/png;base64... "Azure and Google Cloud")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlXGJwY-63sxWhUgOou8l_435yOGAXEKLaTOYOpS9hYcyok65fHZmpQIMhThJzm384JoD3L-Qn8qYVpwaWXK4CJoSSjdKx6FSNT3-vRzA1OOZxoJINNQHfXi_4LgAD28xQosqIous6FLrCsUnc_gxnYr68NFpJfnidRjuZhQkOSRk1FioW7fiKfRZnaig5/s790-rw-e365/azure.jpg)

A malicious actor has been linked to a cloud credential stealing campaign in June 2023 that's focused on Azure and Google Cloud Platform (GCP) services, marking the adversary's expansion in targeting beyond Amazon Web Services (AWS).

The findings come from [SentinelOne](https://www.sentinelone.com/labs/cloudy-with-a-chance-of-credentials-aws-targeting-cred-stealer-expands-to-azure-gcp/) and [Permiso](https://permiso.io/blog/s/agile-approach-to-mass-cloud-cred-harvesting-and-cryptomining/), which said the "campaigns share similarity with tools attributed to the notorious TeamTNT cryptojacking crew," although it emphasized that "attribution remains challenging with script-based tools."

They also overlap with an ongoing TeamTNT campaign [disclosed](https://thehackernews.com/2023/07/teamtnts-silentbob-botnet-infecting-196.html) by Aqua called Silentbob that leverages misconfigured cloud services to drop malware as part of what's said to be a testing effort, while also linking [SCARLETEEL](https://thehackernews.com/2023/07/scarleteel-cryptojacking-campaign.html) attacks to the threat actor, citing infrastructure commonalities.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"TeamTNT is scanning for credentials across multiple cloud environments, including AWS, Azure, and GCP," Aqua noted.

The attacks, which single out public-facing Docker instances to deploy a worm-like propagation module, are a continuation of an intrusion set that [previously targeted](https://permiso.io/blog/s/christmas-cloud-cred-harvesting-campaign/) Jupyter Notebooks in December 2022.

[![Azure and Google Cloud](data:image/png;base64... "Azure and Google Cloud")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1cWbyABCNsWeY5BTZFwQzqMuZvLLkvaIUopq7VRTf0bYRKkxaD5d-6yKQFF6ypdgHadwoBwezDS0c2DmRV1hk33fEo0eKFpp3QvBNpmdffjEJorjWJMzhvlUfVF6nZe-WekGt9iKzsDaCvSYwjwsKHBHfuV6QnaNhr1oP4d7agwx0XuTFE2WcZi3cO0S7/s790-rw-e365/cloud.jpg)

As many as eight incremental versions of the credential harvesting script have been discovered between June 15, 2023, and July 11, 2023, indicating an actively evolving campaign.

The newer versions of the malware are designed to gather credentials from AWS, Azure, Google Cloud Platform, Censys, Docker, Filezilla, Git, Grafana, Kubernetes, Linux, Ngrok, PostgreSQL, Redis, S3QL, and SMB. The harvested credentials are then exfiltrated to a remote server under the threat actor's control.

SentinelOne said the credentials collection logic and the files targeted bears similarities to a [Kubelet-targeting campaign](https://sysdig.com/blog/teamtnt-kubelet-credentials/) undertaken by TeamTNT in September 2022.

Alongside the shell script malware, the threat actor has also been observed distributing a Golang-based ELF binary that acts as a scanner to propagate the malware to vulnerable targets. The binary further drops a Golang network scanning utility called Zgrab.

"This campaign demonstrates the evolution of a seasoned cloud actor with familiarity across many technologies," security researchers Alex Delamotte, Ian Ahl, and Daniel Bohannon said. "The meticulous attention to detail indicates the actor has clearly experienced plenty of trial and error."

"This actor is actively tuning and improving their tools. Based on the tweaks observed across the past several weeks, the actor is likely preparing for larger scale campaigns."

## More connections between SCARLETEEL and TeamTNT emerge

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"From what we know about SCARLETEEL, there is demonstrable overlap in techniques between these TeamTNT-like campaigns," Delamotte told The Hacker News. "The SilentBob campaign regularly achieves access, steals credentials, conducts reconnaissance on connected services and systems. SCARLETEEL obtained credentials from a Terraform configuration file, which is similar to the SilentBob activity."

"The most reliable link is the callout from Avigayil Mechtinger at Sysdig: Avi [noted](https://twitter.com/abbymch/status/1679509312132005888) the SCARLETEEL 2.0 campaign used a crypto miner with the same Monero wallet address. This is fairly conclusive evidence the campaigns are related." The wallet address in question is 43Lfq18TycJHVR3AMews5C9f6SEfenZoQMcrsEeFXZTWcFW9jW7VeCySDm1L9n4d2JEoHjcDpWZFq6QzqN4QGHYZVaALj3U.

Sysdig however said that the use of a common infrastructure notwithstanding, a clear-cut attribution to TeamTNT is difficult due to certain differences in tactics, techniques, and procedures (TTPs).

"There definitely is overlap with some of the infrastructure used by threats such as SCARLETEEL and TeamTNT," Michael Clark, director of threat research at Sysdig, told the publication. "However, there are also differences with the rest of the TTPs observed (i.e., using a custom AWS endpoint) which makes it difficult to do accurate attribution to a single threat actor."

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
[**Share on Fa...