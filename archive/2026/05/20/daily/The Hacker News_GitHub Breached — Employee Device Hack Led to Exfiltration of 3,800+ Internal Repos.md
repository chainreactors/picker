---
title: GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos
url: https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html
source: The Hacker News
date: 2026-05-20
fetch_date: 2026-05-21T06:04:43.428564
---

# GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html)

**Ravie Lakshmanan**May 20, 2026Malware / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoDiyeJZY33dxAsa8qElLYXNILLDT4NhloINZiuzcx3La2JvDK_d54kM8qsx_obt8vQ3FpTJr2ZVoMYiEcqHN0sbt-1A_MHlS7mSavlbDiEDg42HN1d4wCffs7ytuZhDvmMjuej5oljVIqIuRezyZCLmafRclN3wNBKcboV-19F0VMMBkVsQZckV5UaiiH/s1700-e365/github.jpg)

GitHub on Tuesday said it's investigating unauthorized access to its internal repositories after the notorious threat actor known as TeamPCP listed the platform's source code and internal organizations for sale on a cybercrime forum.

"While we currently have no evidence of impact to customer information stored outside of GitHub's internal repositories (such as our customers' enterprises, organizations, and repositories), we are closely monitoring our infrastructure for follow-on activity," the Microsoft-owned subsidiary [said](https://x.com/github/status/2056884788179726685).

The company also noted that it will notify customers via established incident response and notification channels if any impact is discovered.

The development comes after TeamPCP, a threat actor behind a string of software supply chain attacks targeting open-source packages, listed GitHub's source code for sale for an asking price of no less than $50,000. The alleged data dump is said to include about 4,000 repositories.

"As always, this is not a ransom," the group said in a post, [according to screenshots](https://x.com/DarkWebInformer/status/2056831051742527507) shared by Dark Web Informer. "We do not care about extorting GitHub, 1 buyer and we shred the data on our end, it looks like our retirement is soon so if no buyer is found, we leak it for free."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

In a follow-up update shared on X, GitHub said it detected and contained a compromise of an employee device involving a poisoned Microsoft Visual Studio Code extension. As a risk mitigation measure, the company has rotated critical secrets, while prioritizing highest-impact credentials.

"Our current assessment is that the activity involved exfiltration of GitHub-internal repositories only," GitHub [said](https://x.com/github/status/2056949168208552080). "The attacker's current claims of ~3,800 repositories are directionally consistent with our investigation so far."

GitHub did not disclose the name of the VS code extension, although it's worth noting that [Nx Console](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html) recently suffered a compromise that allowed threat actors to push a multi-stage credential stealer and a supply chain poisoning tool. The Nx team has since [acknowledged](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w) that "very few users were compromised."

Following the incident, an X account linked to TeamPCP, [xploitrsturtle2](https://www.ox.security/blog/teampcps-telnyx-windows-malware-technical-analysis/), [stated](https://x.com/xploitrsturtle2/status/2056927898771067006): "GitHub knew for hours, they delayed telling you and they won't be honest in the future. What an amazing run, it's been an honor to play around with the cats over the past few months."

### TeamPCP Compromises durabletask PyPI Package

News of the sale comes as TeamPCP's self-replicating malware campaign, known as [Mini Shai-Hulud](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html), continues to expand in reach with the compromise of durabletask, an official Microsoft Python client for the Durable Task workflow execution framework. Three malicious package versions have been identified: 1.4.1, 1.4.2, and 1.4.3.

"The attacker compromised a GitHub account via a previous attack, dumped GitHub secrets from a repository to which the user had access, and from there had access to the PyPi token to publish directly," Google-owned Wiz [said](https://www.wiz.io/blog/durabletask-teampcp-supply-chain-attack).

The payload embedded into the package is a dropper, which is configured to fetch and run a second-stage payload ("rope.pyz") from an external server ("check.git-service[.]com"). The malware is assessed to be an evolution of the payload deployed in connection with the compromise of the [guardrails-ai package](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html) last week.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHBPAvTjqSKkmsWL6htHglfONKxWRlMxkN39FMW8MfDgpUwqCxrp8xTGg_N7xrv212054zvl3OttJwv6xVWcY3intJhnH6VF65yd5qf2od8NCAR97aEoP7M4WAoLflM0JBaucHcMCoHM_5AWG3KNWasGkv85Tp0dAS9gFh2lZtmrTyg7sab6yXcNHKM3uK/s1700-e365/payload.png)

Specifically, it's designed to activate a full-featured infostealer that's capable of harvesting credentials associated with major cloud providers, password managers, and developer tools, and exfiltrating the data to the attacker-controlled domain. It's worth noting that the stealer is configured to execute only on Linux systems.

According to [SafeDep](https://safedep.io/malicious-durabletask-pypi-supply-chain-attack/), the 28KB Python stealer also attempts to read HashiCorp Vault KV secrets, unlock and dump 1Password and Bitwarden password vaults, and access SSH keys, Docker credentials, VPN configurations, and shell history.

"If the machine is running inside AWS, it propagates itself to other EC2 instances using SSM. If it's inside Kubernetes, it propagates through kubectl exec," Aikido Security [said](https://www.aikido.dev/blog/durabletask-package-compromised-mini-shai-hulud). "And if it detects Israeli or Iranian system settings, there's a 1-in-6 chance it plays audio and then runs rm -rf /\*."

"After enumerating SSM-managed instances, it uses SendCommand with the AWS-RunShellScript document to execute the r...