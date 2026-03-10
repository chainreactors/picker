---
title: UNC4899 Breached Crypto Firm After Developer AirDropped Trojanized File to Work Device
url: https://thehackernews.com/2026/03/unc4899-used-airdrop-file-transfer-and.html
source: The Hacker News
date: 2026-03-09
fetch_date: 2026-03-10T04:04:05.188382
---

# UNC4899 Breached Crypto Firm After Developer AirDropped Trojanized File to Work Device

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [UNC4899 Breached Crypto Firm After Developer AirDropped Trojanized File to Work Device](https://thehackernews.com/2026/03/unc4899-used-airdrop-file-transfer-and.html)

**Ravie Lakshmanan**Mar 09, 2026DevOps / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu3lqP8aiEKLJA-l7TChGGULVqWhyphenhyphenMc67vwAHHEK4LkpR5ZlZuFIYWFmmPqdA8VQpGbFPvjwGvDHxkhXmC9xhTWlRCccD9PyU3A08-ahTc87j__u6g7RvgkwNo85LmbffhVRly_r4Sd9iiVdEvjtVvpcw0NiwOM1NfjNFQXx5xquwbd9E1zUUr09SYv_-A/s1700-e365/crypto.jpg)

The North Korean threat actor known as **UNC4899** is suspected to be behind a sophisticated cloud compromise campaign targeting a cryptocurrency organization in 2025 to steal millions of dollars in cryptocurrency.

The activity has been attributed with moderate confidence to the state-sponsored adversary, which is also [tracked](https://thehackernews.com/2025/07/n-korean-hackers-used-job-lures-cloud.html) under the cryptonyms Jade Sleet, PUKCHONG, Slow Pisces, and TraderTraitor.

"This incident is notable for its blend of social engineering, exploitation of personal-to-corporate device peer-to-peer data (P2P) transfer mechanisms, workflows, and eventual pivot to the cloud to employ living-off-the-cloud (LOTC) techniques," the tech giant noted in its [H1 2026 Cloud Threat Horizons Report](https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026) shared with The Hacker News.

Upon gaining access to the cloud environment, the attackers are said to have abused legitimate DevOps workflows to harvest credentials, break out of the confines of containers, and tamper with Cloud SQL databases to facilitate the cryptocurrency theft.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The attack chain, Google Cloud said, represents a progression of what started with the compromise of a developer's personal device to their corporate workstation, before jumping to the cloud to make unauthorized modifications to the financial logic.

It all started with the threat actors using social engineering ploys to deceive the developer into downloading an archive file as part of a supposed open-source project collaboration. The developer then transferred the same file to their company device over AirDrop.

"Using their AI-assisted Integrated Development Environment (IDE), the victim then interacted with the archive's contents, eventually executing the embedded malicious Python code, which spawned and executed a binary that masqueraded as the Kubernetes command-line tool," Google said.

The binary then contacted an attacker-controlled domain and acted as a backdoor to the victim's corporate machine, giving the attackers a way to pivot to the Google Cloud environment by likely using authenticated sessions and available credentials. This step was followed by an initial reconnaissance phase aimed at gathering information about various services and projects.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZO4D4LxxDvQpbsrbs0jqDTmLq0AV9bswK4cf-m70PGtHV-jMrxx7nzGAh4ut7SHVOlJ5jkLsEU5zip6M9Xl_8InIcBbCxWxUVaeVLqtijwt4xETyHti-WfqEfmwNO3Qf7rqBlNq9C-db1BmEwUfwXgpqjWRwN9wy9gLyUrBd-mi8SUVRDPePyPqRPwWai/s1700-e365/g1.jpg)

The attack moved to the next phase with the discovery of a [bastion host](https://en.wikipedia.org/wiki/Bastion_host), with the adversary modifying its multi-factor authentication (MFA) policy attribute to access it and perform additional reconnaissance, including navigating to specific pods within the Kubernetes environment.

Subsequently, UNC4899 adopted a living-off-the-cloud (LotC) approach to configure persistence mechanisms by altering Kubernetes deployment configurations so as to execute a bash command automatically when new pods are created. The command, for its part, downloaded a backdoor.

Some of the other steps carried out by the threat actor are listed below -

* Kubernetes resources tied to the victim's CI/CD platform solution were modified to inject commands that displayed the service account tokens onto the logs.
* The attacker obtained a token for a high-privileged CI/CD service account, permitting them to escalate their privileges and conduct lateral movement, specifically targeting a pod that handled network policies and load balancing.
* The stolen service account token was used to authenticate to the sensitive infrastructure pod running in privileged mode, escape the container, and deploy a backdoor for persistent access.
* Another round of reconnaissance was conducted by the threat actor before shifting their attention to a workload responsible for managing customer information, such as user identities, account security, and cryptocurrency wallet information.
* The attacker used it to extract static database credentials that were stored insecurely in the pod's environment variables.
* The credentials were then abused to access the production database via Cloud SQL Auth Proxy and execute SQL commands to make user account modifications. This included password resets and MFA seed updates for several high-value accounts.
* The attack culminated with the use of the compromised accounts to successfully withdraw several million dollars in digital assets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

The incident "highlights the critical risks posed by the personal-to-corporate P2P data transfer methods and other data bridges, privileged container modes, and the unsecured handling of secrets in a cloud environment," Google said. "Organizations should adopt a defense-in-depth strategy that rigorously validates identity, restricts data transfer on endpoints, and enforces strict isolation within cloud runtime environments to limit the blast radius of an intrusion event."

To counter the threat, organizations are advised to implement context-aware access and phishing-resistant MFA, ensure only truste...