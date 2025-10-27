---
title: Amazon EC2 SSM Agent Flaw Patched After Privilege Escalation via Path Traversal
url: https://thehackernews.com/2025/04/amazon-ec2-ssm-agent-flaw-patched-after.html
source: The Hacker News
date: 2025-04-09
fetch_date: 2025-10-06T22:10:00.989129
---

# Amazon EC2 SSM Agent Flaw Patched After Privilege Escalation via Path Traversal

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

# [Amazon EC2 SSM Agent Flaw Patched After Privilege Escalation via Path Traversal](https://thehackernews.com/2025/04/amazon-ec2-ssm-agent-flaw-patched-after.html)

**Apr 08, 2025**Ravie LakshmananCloud Security / Vulnerability

[![Amazon EC2 SSM Agent Flaw](data:image/png;base64... "Amazon EC2 SSM Agent Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicJ51N-8mak9Dqpg_5We99GEnJHykiwpr3DFTa7TlIoKwynAdFD2ialbbgLkLflExXUiinYLlEnkeiNfM9p8tWHxzwU2jyYOm88vpeM2peCgdX1O58X175mw0I1sc6Dm0iLl5bcldvlQT_QWsUcIQ1YHm2Wa-iZr0E-7T0deTh50iavk92R-HswhnDORba/s790-rw-e365/exploit.jpg)

Cybersecurity researchers have disclosed details of a now-patched security flaw in the Amazon EC2 Simple Systems Manager (SSM) Agent that, if successfully exploited, could permit an attacker to achieve privilege escalation and code execution.

The vulnerability could permit an attacker to create directories in unintended locations on the filesystem, execute arbitrary scripts with root privileges, and likely escalate privileges or perform malicious activities by writing files to sensitive areas of the system, Cymulate [said](https://cymulate.com/blog/aws-ssm-agent-plugin-id-path-traversal/) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Amazon SSM Agent](https://github.com/aws/amazon-ssm-agent/) is a component of Amazon Web Services (AWS) that enables administrators to remotely manage, configure, and execute commands on EC2 instances and on-premises servers.

The software processes commands and tasks defined in [SSM Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html), which can include one or more plugins, each of which is responsible for carrying out specific tasks, such as running shell scripts or automating deployment or configuration-related activities.

What's more, the SSM Agent dynamically creates directories and files based on the plugin specifications, typically relying on plugin IDs as part of the directory structure. This also introduces a security risk in that improper validation of these plugin IDs can lead to potential vulnerabilities.

The discovery by Cymulate is a path traversal flaw arising as a result of improper validation of plugin IDs, which could allow attackers to manipulate the filesystem and execute arbitrary code with elevated privileges. The issue is rooted in a function named "ValidatePluginId" within pluginutil.go.

"This function fails to properly sanitize input, allowing attackers to supply malicious plugin IDs containing path traversal sequences (e.g., ../)," security researcher Elad Beber said.

As a result of this flaw, an attacker could essentially furnish a specially crafted plugin ID when creating an SSM document (e.g., ../../../../../../malicious\_directory) to execute arbitrary commands or scripts on the underlying file system, paving the way for privilege escalation and other post-exploitation actions.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Following responsible disclosure on February 12, 2025, the vulnerability was addressed on March 5, 2025, with the release of Amazon SSM Agent [version 3.3.1957.0](https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.1957.0).

"Add and use BuildSafePath method to prevent path traversal in the orchestration directory," according to release notes shared by the project maintainers on GitHub.

### Update

Following the publication of the story, Amazon shared the below statement with The Hacker News -

*On March 4, 2025, we released a fix for this reported bug, which was not a privilege escalation because it did not grant any new user permissions. The behavior described relied on the existing privileges of a user to run an SSM document in their own account. There is no action required for customers running 3.3.1802.0 or higher of amazon-ssm-agent. Customers running lower than 3.3.1802.0 can update to at least 3.3.1802.0 to resolve this matter.*

*(The story was updated after publication to include a response from Amazon Web Services.)*

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

[Amazon Web Services](https://thehackernews.com/search/label/Amazon%20Web%20Services)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Path Traversal](https://thehackernews.com/search/label/Path%20Traversal)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

...