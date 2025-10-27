---
title: New TeamTNT Cryptojacking Campaign Targets CentOS Servers with Rootkit
url: https://thehackernews.com/2024/09/new-teamtnt-cryptojacking-campaign.html
source: The Hacker News
date: 2024-09-20
fetch_date: 2025-10-06T18:31:15.118542
---

# New TeamTNT Cryptojacking Campaign Targets CentOS Servers with Rootkit

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

# [New TeamTNT Cryptojacking Campaign Targets CentOS Servers with Rootkit](https://thehackernews.com/2024/09/new-teamtnt-cryptojacking-campaign.html)

**Sep 19, 2024**Ravie LakshmananCryptojacking / Cloud Security

[![CentOS Servers with Rootkit](data:image/png;base64... "CentOS Servers with Rootkit")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDQJdANNLf6jZ3svP-n1iRIY6amvjG4FFO6IkcI0CXXXNgyGKbAVQQfFFhC7zVwFaFBRcBDgLKFVqFmi0_MUyN3RUTcGy_fPxzz-diwOSHHZXaddIg72oh72RYbLDTxiNU5WksFs8a253IbKeLM64Du0RBLs16MzwdJKWFrnH77InBXvlV4_Buz4sFVoRs/s790-rw-e365/servers.png)

The cryptojacking operation known as **TeamTNT** has likely resurfaced as part of a new campaign targeting Virtual Private Server (VPS) infrastructures based on the CentOS operating system.

"The initial access was accomplished via a Secure Shell (SSH) brute force attack on the victim's assets, during which the threat actor uploaded a malicious script," Group-IB researchers Vito Alfano and Nam Le Phuong [said](https://www.group-ib.com/blog/teamtnt/) in a Wednesday report.

The malicious script, the Singaporean cybersecurity company noted, is responsible for disabling security features, deleting logs, terminating cryptocurrency mining processes, and inhibiting recovery efforts.

The attack chains ultimately pave the way for the deployment of the [Diamorphine rootkit](https://thehackernews.com/2022/10/new-cryptojacking-campaign-targeting.html) to conceal malicious processes, while also setting up persistent remote access to the compromised host.

The campaign has been attributed to TeamTNT with moderate confidence, citing similarities in the tactics, techniques, and procedures (TTPs) observed.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

TeamTNT was first discovered in the wild in 2019, undertaking illicit cryptocurrency mining activities by infiltrating cloud and container environments. While the threat actor bid farewell in November 2021 by announcing a "clean quit," public reporting has uncovered [several](https://thehackernews.com/2023/03/cryptojacking-group-teamtnt-suspected.html) [campaigns](https://thehackernews.com/2023/07/teamtnts-cloud-credential-stealing.html) undertaken by the hacking crew since [September 2022](https://thehackernews.com/2022/09/hackers-targeting-weblogic-servers-and.html).

The latest activity linked to the group manifests in the form of a shell script that first checks if it was previously infected by other cryptojacking operations, after which it precedes to impair device security by disabling [SELinux](https://github.blog/2023-07-05-introduction-to-selinux/), AppArmor, and the firewall.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwrRQk19A5rvaEhxO00KQe8qRyNQCwkCI7AnkCL5LtJn4aUe_dOfoJA2I8-iAOS7ap4wdglpPm-VT37M4GSWKy54-xEcquvdERAwbp2f7PqrUf9ArkhPPHALfJerXpYzVvn7sKoftM7bAELaVAxVUMVcRLwaMPnjBMffuuRJDteu7FUrC6LlL8x9Zzj3ag/s790-rw-e365/ssh.png) |
| Changes implemented on ssh service |

"The script searches for a daemon related to the cloud provider Alibaba, named aliyun.service," the researchers said. "If it detects this daemon, it downloads a bash script from update.aegis.aliyun.com to uninstall the service."

Besides killing all competing cryptocurrency mining processes, the script takes steps to execute a series of commands to remove traces left by other miners, terminate containerized processes, and remove images deployed in connection with any coin miners.

Furthermore, it establishes persistence by configuring cron jobs that download the shell script every 30 minutes from a remote server (65.108.48[.]150) and modifying the "/root/.ssh/authorized\_keys" file to add a backdoor account.

"It locks down the system by modifying file attributes, creating a backdoor user with root access, and erasing command history to hide its activities," the researchers noted. "The threat actor leaves nothing to chance; indeed, the script implements various changes within the SSH and firewall service configuration."

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

[CentOS](https://thehackernews.com/search/label/CentOS)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hacking](https://thehackernews.com/search/label/hacking)[rootkit](https://thehackernews.com/search/label/rootkit)[SSH](https://thehackernews.com/search/label/SSH)[VPS Security](https://thehackernews.com/search/label/VPS%20Security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise De...