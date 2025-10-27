---
title: New Study Uncovers Text-to-SQL Model Vulnerabilities Allowing Data Theft and DoS Attacks
url: https://thehackernews.com/2023/01/new-study-uncovers-text-to-sql-model.html
source: The Hacker News
date: 2023-01-10
fetch_date: 2025-10-04T03:28:22.436309
---

# New Study Uncovers Text-to-SQL Model Vulnerabilities Allowing Data Theft and DoS Attacks

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

# [New Study Uncovers Text-to-SQL Model Vulnerabilities Allowing Data Theft and DoS Attacks](https://thehackernews.com/2023/01/new-study-uncovers-text-to-sql-model.html)

**Jan 09, 2023**Ravie LakshmananDatabase Security / PLM Framework

[![Text-to-SQL Model Vulnerabilities](data:image/png;base64... "Text-to-SQL Model Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2OimUivszEmv9gsVS2ZhHvKZLguEwHeRIG_L8FdImTssx0NgFW__d-A2Zfe51doLGTZ9ZQPzEMA-6gLcubPxQtJq-G6nzWYRBYOfuXO6soKbeDt-1gb11FTonkZ70f1fnoVOQ1wDw6Y4scT0EMHcGehmF3EBQFJtCnrLmSqLQFiu2jidncrFLyJok/s790-rw-e365/txt-to-sql.png)

A group of academics has demonstrated novel attacks that leverage Text-to-SQL models to produce malicious code that could enable adversaries to glean sensitive information and stage denial-of-service (DoS) attacks.

"To better interact with users, a wide range of database applications employ AI techniques that can translate human questions into SQL queries (namely [Text-to-SQL](https://towardsdatascience.com/text-to-sql-learning-to-query-tables-with-natural-language-7d714e60a70d))," [Xutan Peng](https://twitter.com/Pzoom522/status/1597403840206499840), a researcher at the University of Sheffield, told The Hacker News.

"We found that by asking some specially designed questions, crackers can fool Text-to-SQL models to produce malicious code. As such code is automatically executed on the database, the consequence can be pretty severe (e.g., data breaches and DoS attacks)."

The [findings](https://arxiv.org/abs/2211.15363), which were validated against two commercial solutions [BAIDU-UNIT](https://ai.baidu.com/unit/home) and [AI2sql](https://www.ai2sql.io/), mark the first empirical instance where natural language processing (NLP) models have been exploited as an attack vector in the wild.

The black box attacks are analogous to [SQL injection](https://owasp.org/www-community/attacks/SQL_Injection) faults wherein embedding a rogue payload in the input question gets copied to the constructed SQL query, leading to unexpected results.

The specially crafted payloads, the study discovered, could be weaponized to run malicious SQL queries that, in turn, could permit an attacker to modify backend databases and carry out DoS attacks against the server.

Furthermore, a second category of attacks explored the possibility of corrupting various pre-trained language models ([PLMs](https://dl.acm.org/doi/10.1145/3442442.3451375)) – models that have been trained with a large dataset while remaining agnostic to the use cases they are applied on – to activate the generation of malicious commands based on certain triggers.

"There are many ways of planting backdoors in PLM-based frameworks by poisoning the training samples, such as making word substitutions, designing special prompts, and altering sentence styles," the researchers explained.

The backdoor attacks on four different open source models ([BART-BASE](https://huggingface.co/facebook/bart-base), [BART-LARGE](https://huggingface.co/facebook/bart-large), [T5-BASE](https://huggingface.co/t5-base), and [T5-3B](https://huggingface.co/t5-3b)) using a corpus poisoned with malicious samples achieved a 100% success rate with little discernible impact on performance, making such issues difficult to detect in the real world.

As mitigations, the researchers suggest incorporating classifiers to check for suspicious strings in inputs, assessing off-the-shelf models to prevent supply chain threats, and adhering to good software engineering practices.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[database security](https://thehackernews.com/search/label/database%20security)[SQL Database](https://thehackernews.com/search/label/SQL%20Database)[Text-to-SQL](https://thehackernews.com/search/label/Text-to-SQL)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "C...