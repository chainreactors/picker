---
title: Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials
url: https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
source: The Hacker News
date: 2026-09-05
fetch_date: 2026-09-06T06:40:18.060497
---

# Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials](https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html)

**Ravie Lakshmanan**Sep 05, 2026Data Breach / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH4sbUEhtXF9n1_8s2f6ChnKMmjUv4Ht-DvEtZyLDPuSNhKFoi41aNlu3-u5kJLXUva81rNFwlsprMXE11cnbXc_es968eO-ANvWm0j1Cyi9SaoVUfneQqNINCR7lRs3qkkYdsSoyMu34Mgxs7B4pKclAt4atPw8B-RCFOTChtgeji9NTes_NEdZ2KKu2_/s1700-nu-rw-lo-l85-e365/jet.jpg)

JetBrains is urging Cadence users to revoke and rotate all credentials following a security incident last month in which unidentified threat actors exploited a recently disclosed critical vulnerability in TeamCity to breach its own environment.

"Cadence users should immediately revoke or rotate all credentials and secrets that may have been used to run their Cadence executions," JetBrains [said](https://blog.jetbrains.com/pycharm/2026/08/cadence-security-incident-august-2026/). "They should also treat all executions, including their inputs and outputs in your Cadence project, as potentially untrusted."

"As the threat actors gained access to the Cadence server, any credentials or secrets stored in Cadence, contained in the compromised backup, or made available to executions on the affected server should be considered compromised and must be revoked or rotated."

[Cadence](https://blog.jetbrains.com/pycharm/2025/06/training-your-ml-models-with-cadence/) is a JetBrains-hosted cloud computing service that integrates with PyCharm via an optional plugin to let developers run machine learning and heavy workloads on cloud GPUs directly from their IDE.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The attack, per the software development company, involved the exploitation of [CVE-2026-63077](https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html) (CVSS score: 9.8) to breach the affected Cadence environments. The deserialization of untrusted data vulnerability can permit an unauthenticated attacker with access to a TeamCity server to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process.

The security flaw has since [come under active exploitation](https://thehackernews.com/2026/08/cisa-flags-teamcity-cve-2026-63077-rce.html) in the wild, with the U.S. Cybersecurity and Infrastructure Security Agency (CISA) adding it to the Known Exploited Vulnerabilities (KEV) catalog on August 5, 2026. The exploitation was discovered by JetBrains on August 23, 2026.

In subsequent updates, JetBrains said the threat actor accessed data contained in the Cadence server backup from 2024 and that they obtained unauthorized access that could have allowed them to reach storage containing data associated with current Cadence users, including email addresses, project source code, and credentials.

"This affects the same group of users we previously contacted directly," Daniel Gallo, Solutions Engineering Lead at JetBrains, said. "These findings did not identify any additional affected users. As a precaution, we are treating the data stored there as potentially exposed."

Some of the information the threat actor has been "confirmed" to have accessed or compromised -

* Personal data, including usernames, real names, email addresses, last-login timestamps, and last accessed IP addresses
* A full backup of the Cadence server dating from 2024, which contains credentials, configuration, artifacts, logs, or other data
* Multiple AWS IAM users and associated credentials/secrets used with Cadence extracted from the 20224 backup, including IAM users belonging to JetBrains employees who used the service
* Files stored in S3 buckets within JetBrains AWS accounts used by Cadence

JetBrains also cautioned that the attackers may have accessed source code synchronized from PyCharm projects to the affected server. This covers scenarios where users have relied on PyCharm to upload or synchronize project files for execution in Cadence, meaning the actions could have inadvertently exposed code, credentials, or configurations.

It's not clear who is behind the activity. However, JetBrains said the intrusion took place between August 8 and 24, 2026. The exploited Cadence server ("api.cadence.jetbrains.com") has since been taken offline. The company conceded that the server in question should have been patched as part of its own vulnerability response efforts, but did not share any details as to why this did not happen.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

JetBrains has also invalidated all access tokens used by the JetBrains Cadence plugin in PyCharm to connect to Cadence. It has shared the following indicators of compromise -

* Activity occurring from August 8, 2026, onwards, particularly authentication or activity using credentials previously stored in or accessible through Cadence
* IP addresses associated with observed exploitation activity:
  + 150.109.230.104
  + 43.153.227.206
  + 62.210.127.48
  + 210.247.242.190
  + 15.235.225.205
  + 152.233.30.18
* Authentication or other activity from unexpected IP addresses or locations
* Unexpected repository clones or downloads, and unexpected commits to repositories
* Changes to repository secrets, webhooks, collaborators, or permissions
* New or modified personal access tokens, API tokens, or SSH keys in external services
* New service accounts created in external services
* Unexpected changes to cloud IAM roles, policies, or permissions
* Unexpected access to cloud storage, including S3 buckets and objects, in services such as AWS and Google Cloud
* Unexpected publication or modification of packages or releases

Besides rotating all credentials, users are being asked to review connected systems for suspicious activity, specifically AWS accounts, S3 bu...