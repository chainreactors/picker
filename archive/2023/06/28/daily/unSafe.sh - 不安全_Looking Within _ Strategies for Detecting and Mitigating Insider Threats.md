---
title: Looking Within | Strategies for Detecting and Mitigating Insider Threats
url: https://buaq.net/go-170579.html
source: unSafe.sh - 不安全
date: 2023-06-28
fetch_date: 2025-10-04T11:44:21.576227
---

# Looking Within | Strategies for Detecting and Mitigating Insider Threats

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/855d3643933d101dd96c3a06e9deff41.jpg)

Looking Within | Strategies for Detecting and Mitigating Insider Threats

Over the past decade, the digital landscape has undergone a rapid transformation, reshaping the way
*2023-6-27 20:59:6
Author: [www.sentinelone.com(查看原文)](/jump-170579.htm)
阅读量:20
收藏*

---

Over the past decade, the digital landscape has undergone a rapid transformation, reshaping the way businesses operate and interact with data. With this paradigm shift, the nature and scope of [insider threats](https://www.sentinelone.com/cybersecurity-101/insider-threats-what-it-is-why-its-so-important/) have also evolved significantly.

As [cloud adoption](https://www.sentinelone.com/blog/cloud-computing-is-not-new-why-secure-it-now/) rates and reliance on third-party vendors rise, this has widened the [attack surface](https://www.sentinelone.com/cybersecurity-101/what-is-cyber-security-attack-surface/) for malicious insiders. With greater access to internal systems, insiders are able to leverage sophisticated attack techniques, putting sensitive data and critical infrastructure at risk.

The scope of insider threats encompasses intellectual property theft, insider trading, collusion with external actors, and financial fraud. As insiders become more adept at circumventing traditional security measures, security leaders are implementing robust strategies to address these evolving [risks](https://www.sentinelone.com/blog/ciso-wins-reducing-risk-across-endpoint-identity-and-cloud-surfaces/).

This blog post expands on how insider threats have evolved over the past decade, shedding light on the emerging challenges faced by businesses worldwide. It also explores real-world examples, showing the importance of a holistic approach that combines technology, policies, and employee education to mitigate insider threats effectively.

![](https://www.sentinelone.com/wp-content/uploads/2023/06/Looking-Within-Strategies-for-Detecting-and-Mitigating-Insider-Threats-1024x536.jpg)

## Understanding How Insider Threats Have Evolved

Insider threats are not a new concept. In fact, they’ve been around as long as businesses have. What’s changed is the breadth and depth that a successful insider attack can cause. In today’s digital landscape, the stakes are so much higher. Consider the following:

* [60% of all corporate data](https://www.zippia.com/advice/cloud-adoption-statistics/) globally stored in various cloud-based solutions
* An average organization does business with [11 third parties](https://www.darkreading.com/cloud/nearly-all-firms-have-ties-breached-third-parties)
* The number of connected devices is predicted to reach approximately [75 billion by 2025](https://blog.gitnux.com/future-of-internet-connectivity-statistics/)
* More than [24,000](https://www.cvedetails.com/vulnerability-list/year-2022/vulnerabilities.html) common vulnerabilities and exposures (CVEs) were identified in 2022

An insider threat can be anyone within an organization who has access to sensitive information and systems. This includes privileged users and administrators, contractors, third-party vendors, and even business partners.

In their most recent [Cost of Insider Threats Report](https://www.proofpoint.com/us/resources/threat-reports/cost-of-insider-threats), Ponemon Institute confirmed that negligent, malicious, and compromised users are a serious cyber threat, with incidents rising 44% in the last two years and costing enterprise businesses over $15 million. These figures are a stark reminder of the significant risk insider threats pose to organizations of all sizes.

[Other reports](https://techjury.net/blog/insider-threat-statistics/) suggest that more than 34% of businesses are affected by such threats yearly and that 68% of security leaders now consider insider attacks and accidental [breaches](https://www.sentinelone.com/cybersecurity-101/what-is-a-data-breach/) to be more likely than external attacks.

## The Different Faces of the “Insider” Behind the Threat

Insider threats can manifest in various forms and can be placed into one of three categories based on the intent or motive behind the insider themself.

### Malicious Insiders | Yahoo’s Trade Secrets Stolen By Departing Employee

Malicious insiders purposefully act against the best interests of their organization and seek to cause harm. They may steal data to sell or use as leverage for personal gain. They could also stem from disgruntled employees, contractors, partners who wish to cause the organization reputational and financial damage. Malicious insiders, in essence, intentionally misuse their access to the organization’s systems and information.

In May 2022, a research scientist at Yahoo [allegedly](https://www.thedrum.com/news/2022/05/19/yahoo-lawsuit-alleges-employee-stole-trade-secrets-upon-receiving-trade-desk-job) stole proprietary information about the company’s AdLearn product after receiving a job offer from a competitor. The malicious insider downloaded almost 570,000 pages of Yahoo’s intellectual property (IP) to their personal device including source code, ad placement algorithms, and internal strategy documents.

### Negligent Insiders | Microsoft Employee Exposes Login Credentials

Negligent insiders typically describe employees, vendors, or partners who engage in risky behavior due to an overall sense of being disengaged. While they consciously decide to act inappropriately, there is no malicious intent behind their actions. Negligent insiders are users who often misplace or share sensitive credentials, ignore IT policies, use [unsecured devices](https://www.sentinelone.com/cybersecurity-101/what-is-byod/), and neglect their security training.

In August of 2022, a number of Microsoft employees [uploaded](https://www.pcmag.com/news/microsoft-employees-exposed-their-azure-server-logins-on-github) sensitive login credentials to the company’s GitHub infrastructure, giving potential attackers access to Azure servers and other internal systems. It was discovered that all identified credentials were associated with an official Microsoft tenant ID and that some were still active at the time of discovery.

### Accidental Insiders | Twitter Staff Fall Victim to Spear Phishing Campaign

Accidental or compromised insiders exhibit no conscious decision to act inappropriately. These cases are often chalked up to simple mistakes made by an employee in the course of their daily work. This may include falling for a social engineering scam, opening or forwarding [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/) emails and malware, misconfiguring systems, or mishandling sensitive information.

Attackers launched a phone-based [spear phishing](https://www.sentinelone.com/cybersecurity-101/spear-phishing/) scam on Twitter employees in July 2020, calling consumer service and tech support teams and instructing them to reset their passwords. After providing their credentials and [MFA](https://www.sentinelone.com/cybersecurity-101/what-is-multi-factor-authentication-mfa/) codes on an [attacker-controlled site](https://www.sentinelone.com/cybersecurity-101/what-are-scam-websites-and-how-to-avoid-scam-websites/), the attackers gained access to Twitter’s internal network as well as some internal support tools. With such highly privileged access, the attackers were able to [hijack](https://www.sentinelone.com/cybersecurity-101/the-ultimate-guide-to-preventing-account-takeover-attacks/) several well-known accounts and spread their scam campaign.

## Insider Threat Protection Starts with Effective Detection

Unlike external t...