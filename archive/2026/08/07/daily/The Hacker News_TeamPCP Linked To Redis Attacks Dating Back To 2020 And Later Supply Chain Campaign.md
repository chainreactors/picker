---
title: TeamPCP Linked To Redis Attacks Dating Back To 2020 And Later Supply Chain Campaign
url: https://thehackernews.com/2026/08/teampcp-linked-to-redis-attacks-dating.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:02.110540
---

# TeamPCP Linked To Redis Attacks Dating Back To 2020 And Later Supply Chain Campaign

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

![cybersecurity](data:image/svg+xml;base64...)

# [TeamPCP Linked To Redis Attacks Dating Back To 2020 And Later Supply Chain Campaign](https://thehackernews.com/2026/08/teampcp-linked-to-redis-attacks-dating.html)

**Ravie Lakshmanan**Aug 07, 2026Cybercrime / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicYXbdZUBG2jW8962nmphGWa0sWoq3jKe6HAT9wa6qlZdPPYBZRdw-uWjUbUv15BxaRgugcEAPXPZ2rMYx3RzM_vLVH18F6oTwwAklstzIRehnPJXwBs9b-d6NKjJZVhO5n1SRnBTlweRonaWCFogLrbJkyzs-F9K3lffy0tfqf2Vownwe9lj06rEe8Nn2/s1700-e365/TeamPCP.jpg)

A new analysis has uncovered that the threat actor tracked as **TeamPCP** has been active on the cybercrime scene as far back as 2020, indicating the group has been compromising internet-facing infrastructure for years before training their sights on the software supply chain.

"The connection is supported by overlapping domains, malware deployment paths, staging techniques, backend infrastructure, and operational tradecraft," Oligo Security researchers Avi Lumelsky and Gal Elbaz [said](https://www.oligo.security/blog/new-intelligence-links-teampcp-to-shadowray-2-0-and-traces-activity-back-to-2020).

This includes two campaigns observed in the second half of 2025: [ShadowRay 2.0](https://thehackernews.com/2025/11/shadowray-20-exploits-unpatched-ray.html) (aka IronErn), which involved hijacking artificial intelligence (AI) infrastructure into a self-propagating botnet, and [TA-NATALSTATUS](https://thehackernews.com/2025/08/geoserver-exploits-polaredge-and.html), which targeted exposed Redis servers to deliver cryptocurrency miners.

TA-NATALSTATUS is assessed to be an evolution of a prior campaign that was detailed by Trend Micro in April 2020 that involved targeting Redis servers to deploy malware. This suggests that the threat actor has been actively targeting internet-accessible infrastructure across Ray, Docker, Redis, and React much before it branded itself as TeamPCP.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Details of the attackers first emerged towards the end of last year when they were linked to the exploitation of security flaws in React Server Components (RSC) and Next.js to facilitate the extraction of credentials and sensitive data from compromised environments. The activity was codenamed [Operation PCPcat](https://thehackernews.com/2025/12/react2shell-vulnerability-actively.html).

Then, earlier this year, Flare detailed a massive campaign undertaken by the threat actor to systematically target cloud native environments as part of efforts to set up malicious infrastructure for follow-on exploitation.

"The operation's goals were to build a distributed proxy and scanning infrastructure at scale, then compromise servers to exfiltrate data, deploy ransomware, conduct extortion, and mine cryptocurrency," Flare security researcher Assaf Morag [noted](https://thehackernews.com/2026/02/teampcp-worm-exploits-cloud.html) at the time.

The group has since branched into [high-profile supply chain compromises](https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html), weaponizing the interconnected nature of modern software to infect developer systems en masse by poisoning popular open-source libraries through a combination of GitHub Actions and token theft abuse.

"One of the strongest operational links is the overlap between the IronErn GitHub and GitLab identities observed during ShadowRay 2.0 and TeamPCP's later infrastructure," Oligo said. "Correlating GitLab authentication logs, command-and-control infrastructure, reverse-shell activity, and malware staging establishes a direct operational bridge between the ShadowRay 2.0 campaign and the actor later operating publicly as TeamPCP."

The latest findings show that not only are these efforts linked, but also that the threat actor repeatedly abused known security flaws impacting React, Docker, Redis, and Ray to gain access and rely on automated and wormable exploitation techniques for self-propagation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The expansion into cascading software supply chain attacks, therefore, represents a natural evolution of this trend, allowing the threat actors to take advantage of legitimate cloud infrastructure and repurpose tried and tested methods in their efforts.

These shifts have been complemented by continuous updates to its malware arsenal, including a Python script ("kube.py") that's specifically used after breaching Kubernetes environments. While earlier versions of the script focused on propagation and setting up persistence, new variants observed as recently as March 2026 began to incorporate wiper-like functionality.

This [destructive code path](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html) checked whether the victim system was configured for the Iran timezone and, if that's the case, fired a DaemonSet that wiped every node in the cluster via a wiper not-so-subtly named Kamikaze. On Kubernetes nodes located outside of Iran, it deployed the CanisterWorm backdoor. For non-Kubernetes Iranian systems, the malware executed a "poison\_pill()" routine to erase the entire file system.

"Whether this continuity reflects a direct rebrand, a shared operator set, or close collaboration between historically related actors cannot be determined with 100% certainty," Oligo said. "What the evidence does demonstrate is that TeamPCP represents the continuation of an existing operational ecosystem rather than an entirely new threat actor that appeared in late 2025."

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
[**Share o...