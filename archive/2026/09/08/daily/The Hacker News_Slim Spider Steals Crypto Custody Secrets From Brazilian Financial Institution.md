---
title: Slim Spider Steals Crypto Custody Secrets From Brazilian Financial Institution
url: https://thehackernews.com/2026/09/slim-spider-steals-crypto-custody.html
source: The Hacker News
date: 2026-09-08
fetch_date: 2026-09-09T06:56:58.071480
---

# Slim Spider Steals Crypto Custody Secrets From Brazilian Financial Institution

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

# [Slim Spider Steals Crypto Custody Secrets From Brazilian Financial Institution](https://thehackernews.com/2026/09/slim-spider-steals-crypto-custody.html)

**Ravie Lakshmanan**Sep 08, 2026Cybercrime / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim6TzHNI7Stg7pvo_Pu0vMltU2jmnIr922wxLWIYFfaRpN3G7rVZCy76FgWwyZUCT36dRygtzxVmZPFTPSm1FuRrmqXwuvTjJhxwJE7zl34ZHuwZUEDdlrnunlem-Xo7KS6Buy1xlHYYxf-0u-d3qWer-o64MrNvrsh5V1WC7dVtGVwubINEgB1AtfQBNC/s1700-nu-rw-lo-l85-e365/brazil-hackers.jpg)

A previously undocumented financially motivated threat actor has been linked to attacks targeting Brazilian financial institutions since at least March 2026.

Cybersecurity company CrowdStrike is tracking the Brazil-based activity cluster under the name **Slim Spider**.

"The adversary demonstrates deep operational knowledge of Brazilian financial infrastructure, including the instant payment service Pix, digital asset platforms, and financial entities' cloud environments," CrowdStrike [said](https://go.crowdstrike.com/rs/281-OBQ-266/images/CrowdStrike-2026-Threat-Hunting-Report.pdf).

Slim Spider has been observed orchestrating a multi-stage intrusion at a Brazil-based financial institution in late March 2026, setting its sights on the entity's cryptocurrency assets and instant payment accounts.

As part of the attack, the e-crime group is said to have developed custom Bash scripts that query the cloud instance metadata to steal temporary cloud credentials over socket connections.

Upon establishing access to the organization's cloud environment, the threat actor enumerated all available secrets stored in the cloud credential manager and used the "[sed](https://www.digitalocean.com/community/tutorials/linux-sed-command)" command to clone and modify secret-extracting scripts. The approach specifically focuses on credentials tied to digital financial assets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"Following exfiltration of digital asset custody secrets, Slim Spider invoked cast, a component of the Foundry Ethereum developer toolkit, to derive the Ethereum wallet address associated with a stolen private key," CrowdStrike explained.

"Rather than relying on third-party libraries that could introduce detection risk, the threat actor implemented cloud-native cryptographic signing directly via OpenSSL within their Bash scripts. This deliberate choice reflected sophisticated operational security awareness and a nuanced understanding of cloud environments."

In the observed attack, Slim Spider moved to establish access to nodes running in a cloud container service cluster, while deploying backdoors mimicking infrastructure-related binaries to blend with legitimate tooling and fly under the radar.

The threat actor then pivoted to Azure DevOps, likely using compromised credentials, to run malicious pipelines that deployed additional implants across a managed Kubernetes cluster. One of the implants was named "spi," an attempt to impersonate Sistema de Pagamentos Instantâneos (SPI), which refers to the central digital infrastructure that processes Pix payments in Brazil.

Slim Spider has also been linked to various web-based panels to automate and streamline different aspects of the attack chain -

* NEXUS // Scanner, an API endpoint-scanning panel that uses Ollama to slot endpoints into 16 categories, such as fintech, banking, payment, and cryptocurrency, and rank them based on availability and authentication options
* Painel de Emails Entra ID, an email reconnaissance panel that searches compromised Microsoft 365 mailboxes sorted into finance, admin, and Brazil categories
* Painel Pix, a transaction panel designed to execute bulk unauthorized Pix transfers from compromised accounts

CrowdStrike said it discovered an exposed command-and-control (C2) panel connected to the threat actor that displayed several compromised hosts from several Brazil-based banks and fintech organizations and likely exfiltrated archive files.

According to the cybersecurity vendor's [adversary profile](https://www.crowdstrike.com/en-us/adversaries/slim-spider/), another key tool in Slim Spider's arsenal is MikeDor, a [Go-based backdoor](https://www.virustotal.com/gui/file/54ac4ba45ac5a7bda0a311b97aa4263b94657f612ce73cd4e1407376a6f05d98/details) capable of [harvesting sensitive information](https://www.virusview.net/malware/Trojan/Linux/MikeDor/Backdoor) and monitoring user activities.

"Slim Spider's knowledge of the cloud attack surface allows them to target credentials associated with an organization's valuable digital currency assets, including custody credentials that control cryptocurrency wallets," it said. "Access to such assets can result in devastating financial loss for victims."

"E-crime threat actors are demonstrating increasingly sophisticated cloud awareness, deliberately targeting the infrastructure and credentials that sit closest to high-value financial assets."

The disclosure coincides with the emergence of another cybercrime group dubbed [Breeze Comet](https://thehackernews.com/2026/09/breeze-comet-executes-hundreds-of.html) (aka CL-CRI-1163, Plump Spider, and SHADOW-AETHER-064) that's infiltrating Brazilian financial systems to abuse payment infrastructure and carry out illegal transactions for financial gain.

Google Threat Intelligence Group (GTIG) and Mandiant said the Portuguese-speaking hacking group breaks into systems that Brazilian financial organizations use to perform transactions and initiates payments for itself. The earliest attacks date back to 2024.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

The threat actor has also been spotted using insufficiently secure Brazilian government websites to stage its malware, and leveraged their reputation in follow-on social engineering attacks against its targets. To make matters worse, Breeze Comet ha...