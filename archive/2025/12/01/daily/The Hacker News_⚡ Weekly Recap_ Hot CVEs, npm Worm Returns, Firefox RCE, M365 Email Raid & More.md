---
title: ⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid & More
url: https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html
source: The Hacker News
date: 2025-12-01
fetch_date: 2025-12-02T03:19:08.400301
---

# ⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid & More

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid & More](https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html)

**Dec 01, 2025**Ravie LakshmananHacking News / Cybersecurity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcq3E5v51_c0rVzjd3B8VALj_RAmWr8iM2Uy8icWvBKtPm85iW1D9oPIgVyRoNMU51ycVecBo6UBEsmOveLErPzL96cTiC-Av_jllbVpTLKqRHD6zSrim61Buwn50jxqU2I76e-MmqBTWQk9fvUH5n5y635QZ8JA-ZUNCB_O_vYy43CaF8WHgRXdfl7UAW/s790-rw-e365/recap1.jpg)

Hackers aren't kicking down the door anymore. They just use the same tools we use every day — code packages, cloud accounts, email, chat, phones, and "trusted" partners — and turn them against us.

One bad download can leak your keys. One weak vendor can expose many customers at once. One guest invite, one link on a phone, one bug in a common tool, and suddenly your mail, chats, repos, and servers are in play.

Every story below is a reminder that your "safe" tools might be the real weak spot.

## **⚡ Threat of the Week**

**Shai-Hulud Returns with More Aggression** — The npm registry was [targeted](https://entro.security/blog/shai-hulud-2-0-banks-gov-tech-breach/) a [second time](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/) by a self-replicating worm that went by the moniker "Sha1-Hulud: The Second Coming," affecting over 800 packages and 27,000 GitHub repositories. Like in the previous iteration, the [main objective](https://www.trendmicro.com/en_us/research/25/k/shai-hulud-2-0-targets-cloud-and-developer-systems.html) was to steal sensitive data like API keys, cloud credentials, and npm and GitHub authentication information, and facilitate deeper supply chain compromise in a worm-like fashion. The malware also created GitHub Actions workflows that allow for command-and-control (C2) and injected GitHub Actions workflow mechanisms to steal repository secrets. Additionally, the malware [backdoored](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/) every npm package maintained by the victim, republishing them with malicious payloads that run during package installation. "Rather than relying solely on Node.js, which is more heavily monitored, the malware dynamically installs Bun during package installation, benefiting from its high performance and self-contained architecture to execute large payloads with improved stealth," Endor Labs [said](https://www.endorlabs.com/learn/shai-hulud-2-malware-campaign-targets-github-and-cloud-credentials-using-bun-runtime). "This shift likely helps the malware evade traditional defenses tuned specifically to observe Node.js behavior." GitGuardian's analysis [revealed](https://blog.gitguardian.com/shai-hulud-2/) a total of 294,842 secret occurrences, which correspond to 33,185 unique secrets. Of these, 3,760 were valid as of November 27, 2025. These included GitHub access tokens, Slack webhook URLs, GitHub OAuth tokens, AWS IAM keys, OpenAI Project API keys, Slack bot tokens, Claude API keys, Google API Keys, and GitLab tokens. Trigger.dev, which had one of its engineers installing a compromised package on their development machine, [said](https://trigger.dev/blog/shai-hulud-postmortem) the incident led to credential theft and unauthorized access to its GitHub organization. The Python Package Index (PyPI) repository [said](https://blog.pypi.org/posts/2025-11-26-pypi-and-shai-hulud/) it was not impacted by the supply chain incident.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxccbWJ-vDSqI16EW7ZePzdrN3msD8Y3I0OTsvj1um0AaRoYcyvX3eLFo-sBB0eYAJo4eAWSx6sD1CzE5eg8VyNf78Q3VT_rTNZnr4eRvv3yMkwnSzSHiOn2h2qJQ8R8lrBil_sKk2qB13O5gndDatKecuFz_HWw_qneqKBpSGsaEV3A9u84byU_xXgELI/s2600/tm.png)

[![Securing Privileged Access](data:image/png;base64... "Securing Privileged Access")

## [Report] Securing Privileged Access: The Key to Modern Enterprise Defense

On-prem PAM no longer cuts it. 55% of IT leaders say cloud-native PAM is now essential. Modern teams demand secure credential storage, seamless integration and real-time visibility everywhere. Download Keeper's PAM Report for key insights from 4,000 IT and security leaders.](https://thehackernews.uk/modern-pam-insights-ar)
[Download the Report ➝](https://thehackernews.uk/modern-pam-insights-ar)

## **🔔 Top News**

* **[ToddyCat Steals Outlook Emails and Microsoft 365 Access Tokens](https://thehackernews.com/2025/11/toddycats-new-hacking-tools-steal.html)** — Attackers behind the ToddyCat advanced persistent threat (APT) toolkit have evolved to stealing Outlook mail data and Microsoft 365 Access tokens. The APT group has refined its toolkit in late 2024 and early 2025 to capture not only browser credentials, as previously seen, but also victims' actual email archives and access tokens. The activity marks the second major shift in ToddyCat's tooling this year, following an April 2025 campaign where the group abused a vulnerability in ESET's security scanner to deliver a previously undocumented malware codenamed TCESB.
* **[Qilin Attack Breaches MSP to Hack into Dozens of Financial Firms](https://thehackernews.com/2025/11/qilin-ransomware-turns-south-korean-msp.html)** — South Korea's financial sector has been targeted by what has been described as a sophisticated supply chain attack that led to the deployment of Qilin ransomware. "This operation combined the capabilities of a major Ransomware-as-a-Service (RaaS) group, Qilin, with potential involvement from North Korean state-affiliated actors (Moonstone Sleet), leveraging Managed Service Provider (MSP) compromise as the initial access vector," Bitdefender said. Korean Leaks took place over three publication waves, resulting in the theft of over 1 million files and 2 TB of data from 28 victims. To pull off these attacks, the Qilin affiliate is said to have breached a single upstream managed service provider (MSP), leveraging the access to compromise several victims at once.
* **[CISA Warns of Spyware Campaigns Using Spyware and...