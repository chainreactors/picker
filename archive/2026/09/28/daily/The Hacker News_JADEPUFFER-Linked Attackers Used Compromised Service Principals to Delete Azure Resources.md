---
title: JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources
url: https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
source: The Hacker News
date: 2026-09-28
fetch_date: 2026-09-29T07:41:37.619872
---

# JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources](https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html)

**Ravie Lakshmanan**Sep 28, 2026Cloud Security / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHYvL1hsEQjB3x7u-jNflFT0QK3a9IEFse8ghWqV9SxkawlFerAn8pzjfYgztccVleVlLzZcDlOSvu7gqJhHP_XLWL1lqZkeIVCifya8Ohinriqk_o-kpzzdtv4x7NinDhQgWbE9B7yJliuJPGZ2x0qh9jRgkWfyNyPexujdTWpLTbfe7MKRVQT1Z3BAQ9/s1700-nu-rw-lo-l85-e365/azure-ai.jpg)

The threat actor known as JADEPUFFER has been observed orchestrating destructive actions within a Microsoft Azure environment using compromised service principals.

Microsoft, which is tracking the activity under the name **Storm-3168**, has called it an evolution of the threat actor's tradecraft. The attack took place in early June 2026 over a period of about 18 hours.

"The destructive operations were facilitated by compromising service principals and targeted Azure Storage Accounts, SQL databases, Key Vaults, Function Apps, recovery protection locks, Virtual Machines, and App Services," researchers Yossi Weizman and Tushar Mudi, along with the Microsoft Security Research team, [said](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/).

JADEPUFFER was [first documented](https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html) by Sysdig, describing it as the first-ever ransomware operation run end-to-end with the help of a large language model (LLM). The agentic attack exploited a known security flaw in Langflow (CVE-2025-3248) to break in, harvested credentials, burrowed deeper into the network, encrypted Nacos service configuration files, dropped the original database tables, and left a ransom note demanding a Bitcoin payment.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

While the attack was found to have leveraged MySQL's built-in AES\_ENCRYPT() function to perform the encryption step, the same Langflow instance was subsequently targeted by the threat actor a second time using a compiled Go-based ransomware strain codenamed [ENCFORGE](https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html).

ENCFORGE is specifically built for the artificial intelligence (AI) infrastructure, scanning for nearly 180 file extensions spanning model checkpoints, vector databases, training datasets, and embedding indices, along with macOS-centric files like Keychain stores, Xcode project files, and Apple Pages and Numbers documents.

"An autonomous agent reasoned about its targets, harvested and reused credentials, moved laterally, established persistence, and destroyed a database, narrating its own intent the entire way," Sysdig noted at the time. "None of the individual techniques were novel or sophisticated. What is notable, however, is that an AI model strung them together into a complete ransomware operation against neglected internet-facing infrastructure."

Microsoft, in its analysis, said it observed two compromised service principals linked to the same tenant, with one used for reconnaissance and resource discovery and the second for destructive operations and credential collection.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuOrMrX0PQDEA7pPVIP6lGNJuNBdCF17yDOWt2XSr_95smxq0u_Takg84GDj23w-AiZMRv2PiAA4j6gL8CpXR-atjlF5DiXYKcQo9QQtn-tZrCjwgsbpEPbca1GW5fsOYksk5etBLwFUpHr4k8Ofcj3a-eMq-3iD3GtSrKYSnGOrW1ln7UanvU742v6LGn/s1700-nu-rw-lo-l85-e365/ms-time.jpg)

The enumeration activity targeted Azure Virtual Machines, subscriptions, resource groups, and resources for close to 16 hours, carrying out over 300 read operations during the time period. The second compromised service principal also engaged in some discovery operation of its own 90 minutes later, enumerating virtual machines and resource groups across two subscriptions within five seconds.

After 16 hours, the second service principal also successfully enumerated Azure App Service configuration stores, likely in an attempt to look for exposed credentials. Soon after, the service principal is said to have conducted more than 150 destructive or credential collection-related operations in 35 minutes.

In all, the destructive sequence lasted for about seven minutes and involved over 100 storage account deletion attempts. Also targeted were an Azure Key Vault, Function App, and App Service plan, as well as multiple Azure SQL databases. However, each of the database deletion attempts ended up in failure due to the use of an unsupported API version for the Azure SQL database resource type.

"Most Azure Storage accounts targeted by the threat actor were successfully deleted," Microsoft said. "However, Azure resource locks and storage account-level deletion protection blocked deletion attempts for few of the storage accounts, demonstrating the value of independent safeguards that remain effective even when a compromised identity has broad administrative permissions."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

It's unclear how the service principal was compromised, Microsoft said it observed its client ID, client secret, and tenant ID had been previously exposed in plaintext in a public GitHub issue by an employee of the impacted organization. Although the secret was removed, it remained accessible through the public edit history.

Microsoft said it has also detected repeated probing from Storm-3168 linked infrastructure against several Azure App services for different customers, adding that the attacks are likely automated or scripted given the division of work using multiple service principals and the timing between the different operations.

The end goal of the attack is assessed to be ransomware-aligned, as it led to th...