---
title: PHP2Shell Attack Roots 25 Servers, Breaches U.S. Government-Affiliated Network
url: https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html
source: The Hacker News
date: 2026-10-28
fetch_date: 2026-10-29T07:52:55.154767
---

# PHP2Shell Attack Roots 25 Servers, Breaches U.S. Government-Affiliated Network

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [PHP2Shell Attack Roots 25 Servers, Breaches U.S. Government-Affiliated Network](https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html)

**Ravie Lakshmanan**Oct 28, 2026Vulnerability / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl3PPkqzXf7YyMcnwdBu5XWlOwWtUonf15z0n79qMtIOVTb4LNfKdnl7tUK-45_2boP9r2ZKuHmX6e1BZLmo-LYF-rUwH8gtNrynFuaX4rlNh20UXPvtIfC85BcKcHXK1qei6uOJyImSjTfO537yljJve0Y_zMlfFfhBl0mKPfppWhkfojtGlYgxLjdSO0/s1700-nu-rw-lo-l85-e365/php-united.jpg)

Cybersecurity researchers have disclosed details of what appears to be an artificial intelligence (AI)-assisted attack orchestrated by a suspected China-nexus threat actor that has leveraged the [PHP2Shell](https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html) vulnerabilities to breach exposed systems.

The activity, which was observed on October 25, 2026, involved an attacker combining PHP2Shell with a kernel privilege escalation exploit to root 25 servers, including three systems in a U.S. government-affiliated environment.

"The affected devices run specific versions of a large vendor's firewall software," cybersecurity firm Dream [said](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers). "The attacker then launched attacks against Active Directory. The recovered artifacts confirm credential extraction and directory enumeration."

The name of the affected vendor was not disclosed, but the Israeli company said it notified the entity. The attack chain essentially brings together two sets of vulnerabilities impacting PHP and the Linux kernel -

* **[PHP2Shell](https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html)**, a pair of flaws tracked as CVE-2026-109618 and CVE-2026-109619 (CVSS scores: 9.2) that could result in unauthenticated remote code execution
* **[Fragnesia](https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html)**, a Linux kernel local privilege escalation vulnerability tracked as CVE-2026-46300 (CVSS score: 7.8)

"The implementation we recovered is a custom, non-public build, not a copy of any known public exploit for PHP2Shell," Dream researchers explained. "It follows the same underlying concept but appears to have been independently developed and tailored specifically for the targeted firewall platform."

"The vulnerability targets PHP's session.upload\_progress mechanism on the firewall's appweb management server. The firewall OS uses PHP 8.0.30 with a high memory limit that enables the memory corruption stages of the attack."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

The custom weaponization of the PHP2Shell exploit chain, coupled with CVE-2026-46300, is said to have rooted 25 servers across the U.S., Japan, Taiwan, and South Korea.

Artifacts discovered by Dream indicate that the operation started with exploit development in a lab environment before obtaining persistent access to a U.S. government organization's internal Active Directory domain.

"Once rooted, the attacker zeroed in on three specific servers in a U.S. government-affiliated environment," the company noted.

The links to AI-assisted tooling stem from evidence pointing to the installation of Anthropic's Claude Code in the attack infrastructure, along with the presence of API keys for FOFA and an AI-powered offensive security platform called aiscan configured with large language models (LLMs) from DeepSeek and Kimi.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaxx8wfDKYDFFOw0TNItz_Q8w0NuKcGFhyphenhyphenWDU2OUthlSq_pye7Y413RXqAIEMLodQ8zFM8foL5B2hcXTNEGy0TkpWmlKXlTXyaCGR-gwUXlRxUhErOxrq7arHgnjdDD83y4eUU8Rc4BJRYm0Iq7t8PpyhWQrg6iawTqGIDo7_E36tE2CQE6ohysAiZGFiw/s1700-nu-rw-lo-l85-e365/cncept.png)

What's more, the code structure, commenting style, and consistency across nearly 40 scripts suggest the use of AI to augment the development process. The entire operation, per Dream, unfolds as follows -

* Attacker uses FOFA to identify approximately 19,000 internet-facing firewalls with exposed management interfaces worldwide.
* A custom version scanner is executed to determine which among those devices are online and what operating system version they are running. About 5,000 devices respond with the version information.
* The attacker filters the servers to those located in the U.S., Japan, Taiwan, and South Korea, and then limits the scope to systems that match newer release branches running PHP 8.0.30. This step yields 240 targets.
* The target list is fed as input to an automated batch runner that exploits the PHP2Shell-Fragnesia chain, plants a PHP web shell on a publicly accessible directory on the firewall, verifies root access, and logs the target's hostname and IP to a CSV file. This step allows the attacker to gain root access to 24 servers.
* Two of the successfully compromised systems are identified as belonging to a U.S. government-affiliated organization. One of them crashes shortly after it was rooted on October 23, 2026, at 6:14 p.m. UTC and never comes back online. The attacker carries out a dedicated campaign to successfully root a second system on October 24, 2026, at 10:09 a.m. UTC.
* The attacker exploits the second system to build a persistent channel into the internal network via a reverse SSH tunnel connecting the compromised firewall back to the operator's infrastructure. At 11:35 a.m. UTC, a third government server is compromised using the same method, the only difference being that this was an internal firewall management server only reachable through the tunnel. The total number of rooted servers reaches 25.
* The attacker targets Active Directory to decrypt the LDAP service account password, enumerate users, and spray passwords against every user account using organization-themed passwords in an attempt to extract credentials. The operation also attempts to create backdoo...