---
title: Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database
url: https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html
source: The Hacker News
date: 2026-07-30
fetch_date: 2026-07-31T05:31:17.229143
---

# Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Azure Cosmos DB Flaw Exposed Platform-Wide Key That Could Access Any Database](https://thehackernews.com/2026/07/azure-cosmos-db-flaw-exposed-platform.html)

**Swati Khandelwal**Jul 30, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_dFT-y76kGOf4rFOAu6NYNsE2s57G-7dl0a03tULY-f2ZGTbpPeEvu-NUCLVh-bgEdBvecIt28BJLQXUHclBc_IfGP9tBSZyMIm971Myrp2_zhSPyXhCJkhYmSfvLWNRewSsCip2YJfBEWocEEKdXPUL-y_mK8ZcHbBAaTWt8SzXmDJeQoYc6r5ceC6A/s1700-e365/wiz-cosmodb.jpg)

A now-patched vulnerability in **Azure Cosmos DB** could have let an attacker escape the service's Gremlin query sandbox and obtain full read and write access to databases across customer tenants, according to Wiz.

**Wiz**, which codenamed the chain **CosmosEscape**, said the exploit chain began with a crafted query against a Gremlin database controlled by the attacker. From there, code execution on a multi-tenant gateway exposed a platform-wide signing secret and a regional account directory, allowing the researchers to locate a target and retrieve its primary account key.

Microsoft blocked the vulnerable Gremlin entry point within 48 hours of the November 2025 report. Wiz said Microsoft completed the longer-term fix across all regions in July 2026 and eliminated the platform-wide key.

"We appreciate Wiz's work in identifying and reporting this issue through coordinated vulnerability disclosure," a Microsoft spokesperson told The Hacker News. "We have fully addressed the issue and found no evidence of customer impact based on our investigations. We continue to invest in additional security enhancements across the platform."

Microsoft said its review found no unauthorized activity outside the researchers' testing. It said no customer data was accessed and no customer action is required.

The Hacker News has also reached out to Wiz for clarification of the exploit prerequisites and tested scope. This story will be updated with any response.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The published chain starts with a Gremlin database controlled by the attacker and credentials for that account, not access to a victim database.

[Microsoft's current connection guide](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/quickstart-dotnet) requires an account host, database, and graph path, and primary key before a client can submit Gremlin queries. Wiz has not published whether the exploit required anything beyond that starting point.

According to [Wiz's technical write-up](https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db), Cosmos DB's custom Gremlin engine translates Gremlin queries into .NET code and runs them inside a restricted environment. Wiz said the restrictions failed to account for .NET reflection, allowing the researchers to build file-read and file-write primitives before reaching arbitrary code execution.

The public disclosure shows the output of a crafted query that executed the hostname command on the Cosmos DB backend, but not the query itself. The researchers said they will present the complete chain at a [Black Hat USA briefing](https://www.wiz.io/events/wiz-at-black-hat) on August 6.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1gUFaU0x12X7qouUnKeipEsQ6eeLubLEhgq411KNb8FuEsLXJ7MLR5FiGiH8S9SGg6oZfB-Z2m4k3iA8pLGejDAO0R-Ruiytl-tT8NLvOVxCjV8D33dG4n6B0Rbad6VgIo1I49vgqExln4Z4b38L0VPQukryBbgNIp3YhkDOEzS3VSB4ZcqySuPYvbw0/s1700-e365/attack-chain.png)

The code execution landed on a component Wiz calls the DB Gateway, which executes customer queries on multi-tenant Azure Service Fabric clusters. Customer databases were not stored on those clusters, but the gateway could retrieve the primary key for a requested Cosmos DB account. [Microsoft documentation](https://learn.microsoft.com/en-us/rest/api/cosmos-db/access-control-on-cosmosdb-resources) says a Cosmos DB account primary key grants full control over all resources in that account.

Credentials available to the gateway also provided access to a signing key that Wiz dubbed the Cosmos Master Key. Wiz said the gateway's signing key could retrieve the primary key for any account across tenants, regions, and the SQL, MongoDB, Cassandra, and Gremlin APIs.

The same secret opened a regional database called the Config Store, described by Wiz as a directory containing Cosmos DB account names, subscription and tenant identifiers, network settings, and tags. An attacker could use it to find a specific organization's accounts and then request their primary keys.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyoBGaLXGZpkSo8tDirSz-9LmmoOs31tQTlvJWBMLiWJKqMFFaiMmNLV3l-p8zXaFm1VmGG/s728-e100/sygnia-d-2.png)](https://thn.news/sygnia-webinar)

Wiz said the chain could also reach private and network-isolated accounts because the compromised gateway enforced those network boundaries from inside the service. The researchers' write access to the Config Store suggested network settings could also be changed, although the report does not say they demonstrated that against another customer's account.

[Microsoft documentation](https://learn.microsoft.com/en-us/purview/edisc-search-teams) says Teams message data remains in Cosmos DB, while a [Microsoft engineering post](https://devblogs.microsoft.com/cosmosdb/how-microsoft-copilot-scales-to-millions-of-users-with-azure-cosmos-db/) says Copilot stores users' queries and conversation histories there. Wiz said databases supporting those products were potentially accessible, but it did not report accessing their data.

The public record does not say when the vulnerable engine and signing-key path entered production or what period Microsoft's log review covered. The duration of potential exposure therefore...