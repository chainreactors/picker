---
title: New Cryptojacking Operation Targeting Kubernetes Clusters for Dero Mining
url: https://thehackernews.com/2023/03/new-cryptojacking-operation-targeting.html
source: The Hacker News
date: 2023-03-16
fetch_date: 2025-10-04T09:46:14.931426
---

# New Cryptojacking Operation Targeting Kubernetes Clusters for Dero Mining

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

# [New Cryptojacking Operation Targeting Kubernetes Clusters for Dero Mining](https://thehackernews.com/2023/03/new-cryptojacking-operation-targeting.html)

**Mar 15, 2023**Ravie LakshmananServer Security / Cryptocurrency

[![Kubernetes](data:image/png;base64... "Kubernetes")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTXu8pHfBXlC_Wg-IuD4v693ILL-Gk0EF_aKdvsy0jzVUUbVnDL1lQ0F8kn2ygluydtV4UVHnqCn2i4DKtiFrMD4G0g0qSMiwLxucpJd78Te3RmLoxsUwGLNx-6d1BCsf82X-lrX79mZhyBQH60yxGbEw5Q7pdzO505D9wxHt_5BM7womxNNm8j1P5/s790-rw-e365/dero.png)

Cybersecurity researchers have discovered the first-ever illicit cryptocurrency mining campaign used to mint Dero since the start of February 2023.

"The novel Dero cryptojacking operation concentrates on locating Kubernetes clusters with anonymous access enabled on a Kubernetes API and listening on non-standard ports accessible from the internet," CrowdStrike [said](https://www.crowdstrike.com/blog/crowdstrike-discovers-first-ever-dero-cryptojacking-campaign-targeting-kubernetes/) in a new report shared with The Hacker News.

The development marks a notable shift from Monero, which is a prevalent cryptocurrency used in such campaigns. It's suspected it may have to do with the fact that [Dero](https://dero.io/about.html) "offers larger rewards and provides the same or better anonymizing features."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attacks, attributed to an unknown financially motivated actor, commence with scanning for Kubernetes clusters with authentication set as [--anonymous-auth=true](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/), which allows anonymous requests to the server, to drop initial payloads from three different U.S.-based IP addresses.

This includes deploying a Kubernetes [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) named "proxy-api," which, in turn, is used to drop a malicious pod on each node of the Kubernetes cluster to kick-start the mining activity.

[![Cryptojacking Operation](data:image/png;base64... "Cryptojacking Operation")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWEATFZNq0wVhCllOlOw8r3vFEmgvOKE-eTnXN7EettfbeDC6p4LDcjHXovl--o3XJNBQ0IMnP5vnuAovO71IMQ_g3aHp16CiVpi0IVb0LY12K3gVN8VyeybiMPUEpYHRTfgqjLVxIOuEw5enRxqkv3AAhfQn6p3huXHn7f_69FVMurxcemFxM8s1R/s790-rw-e365/crowd.png)

To that end, the DaemonSet's YAML file is orchestrated to run a Docker image that contains a "pause" binary, which is actually the [Dero coin miner](https://github.com/deroproject/derohe/releases/tag/Release114).

"In a legitimate Kubernetes deployment, 'pause' containers are used by Kubernetes to bootstrap a pod," the company noted. "Attackers may have used this name to blend in to avoid obvious detection."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The cybersecurity company said it identified a parallel Monero-mining campaign also targeting exposed Kubernetes clusters by attempting to delete the existing "proxy-api" DaemonSets associated with the Dero campaign.

This is an indication of the [ongoing tussle](https://thehackernews.com/2022/07/this-cloud-botnet-has-hijacked-30000.html) between cryptojacking groups that are vying for cloud resources to take and retain control of the machines and consume all of its resources.

"Both campaigns are trying to find undiscovered Kubernetes attack surfaces and are battling it out," CrowdStrike threat researchers Benjamin Grap and Manoj Ahuje said.

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

[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](...