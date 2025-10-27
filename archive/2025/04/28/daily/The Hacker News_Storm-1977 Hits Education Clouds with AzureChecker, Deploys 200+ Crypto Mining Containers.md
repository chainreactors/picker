---
title: Storm-1977 Hits Education Clouds with AzureChecker, Deploys 200+ Crypto Mining Containers
url: https://thehackernews.com/2025/04/storm-1977-hits-education-clouds-with.html
source: The Hacker News
date: 2025-04-28
fetch_date: 2025-10-06T22:05:21.343865
---

# Storm-1977 Hits Education Clouds with AzureChecker, Deploys 200+ Crypto Mining Containers

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

# [Storm-1977 Hits Education Clouds with AzureChecker, Deploys 200+ Crypto Mining Containers](https://thehackernews.com/2025/04/storm-1977-hits-education-clouds-with.html)

**Apr 27, 2025**Ravie LakshmananKubernetes / Cloud Security

[![Clouds with AzureChecker](data:image/png;base64... "Clouds with AzureChecker")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0ogsOdS8Vlx4Sl7V917OPyw2gqTGjCAN2x_uCJnc_VyW0DnHdaVHdLryBOe4_2iputGorprMa4F_ryWrh6I4uN1PG5o0G7IcKYl5y6a9140sh31QD7NwYOJ3oj0u1gY1Qp44dmw7-6VnfHuhMbQLVSixlZJFaG0c_0hQ_k_U9LfdfWG9pE9hn9y7R-qy5/s790-rw-e365/azure.jpg)

Microsoft has revealed that a threat actor it tracks as Storm-1977 has conducted [password spraying attacks](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/password-spraying/) against cloud tenants in the education sector over the past year.

"The attack involves the use of AzureChecker.exe, a Command Line Interface (CLI) tool that is being used by a wide range of threat actors," the Microsoft Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2025/04/23/understanding-the-threat-landscape-for-kubernetes-and-containerized-assets/) in an analysis.

The tech giant noted that it observed the binary to connect to an external server named "sac-auth.nodefunction[.]vip" to retrieve an AES-encrypted data that contains a list of password spray targets.

The tool also accepts as input a text file called "accounts.txt" that includes the username and password combinations to be used to carry out the password spray attack.

"The threat actor then used the information from both files and posted the credentials to the target tenants for validation," Microsoft said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In one successful instance of account compromise observed by Redmond, the threat actor is said to have taken advantage of a guest account to create a resource group within the compromised subscription.

The attackers then created more than 200 containers within the resource group with the ultimate goal of conducting illicit cryptocurrency mining.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC6ByqrFtSCDIOhz4s0_kagIgT3xx4DVkXlMJQ_h20AlW-5NCzsTTsM8LBzcOXxpv17h-ph6SzGYJjRagPh0a7OJCwNnN3zXWBHxlWuTM3wCYicY2GcUALAQlonTSrPeJKY4PG3_o_wPL1azs2gRz3SYcV4LYjk96Li9pbgNJoqBoYwWpGf5xR49WXm2RD/s790-rw-e365/ms-cloud.jpg)

Microsoft said containerized assets, such as Kubernetes clusters, container registries, and images, are [liable](https://attack.mitre.org/matrices/enterprise/cloud/) to [various kinds of attacks](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/), including using -

* Compromised cloud credentials to facilitate cluster takeover
* Container images with vulnerabilities and misconfigurations to carry out malicious actions
* Misconfigured management interfaces to gain access to the Kubernetes API and deploy malicious containers or hijack the entire cluster
* Nodes that run on vulnerable code or software

To mitigate such malicious activities, organizations are advised to secure container deployment and runtime, monitor unusual Kubernetes API requests, configure policies to prevent containers from being deployed from untrusted registries and ensure that the images being deployed in containers are free from vulnerabilities.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Container Security](https://thehackernews.com/search/label/Container%20Security)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)[Microsoft](https://thehackernews.com/search/label/Microsoft)[Password Attack](https://thehackernews.com/search/label/Password%20Attack)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking:...