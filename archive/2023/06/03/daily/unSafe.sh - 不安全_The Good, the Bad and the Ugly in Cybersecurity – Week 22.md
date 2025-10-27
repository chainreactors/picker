---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 22
url: https://buaq.net/go-166991.html
source: unSafe.sh - 不安全
date: 2023-06-03
fetch_date: 2025-10-04T11:44:49.669098
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 22

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

![](https://8aqnet.cdn.bcebos.com/b3db91246458e59e43bc616ec6e96792.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 22

Breached | Data of 478,000 RaidForum Users Exposed OnlineThe tables turned on cybercriminals this
*2023-6-2 21:0:59
Author: [www.sentinelone.com(查看原文)](/jump-166991.htm)
阅读量:32
收藏*

---

## Breached | Data of 478,000 RaidForum Users Exposed Online

The tables turned on cybercriminals this week when private user information from the notorious RaidForums was leaked online to another hacker forum. This newer forum called “Exposed” was launched just earlier this month, making the news of this data leak their first big splash in the [darknet](https://www.sentinelone.com/cybersecurity-101/what-is-the-dark-web/) ecosystem.

![RAID Forums breach](https://www.sentinelone.com/wp-content/uploads/2023/06/Screenshot-2023-06-02-at-7.57.00-AM-scaled.jpg)

Though RaidForums was infamously frequented by cybercriminals, threat gangs, and other such unsavory parties, it was also accessed by a wide range of [hackers](https://www.sentinelone.com/cybersecurity-101/what-is-a-hacker/) and, of course, law enforcement. The [leaked](https://www.sentinelone.com/cybersecurity-101/what-is-a-data-breach/) database reportedly contained the registration information of just over 478,000 members including signup dates, emails, hashed passwords, and usernames. It is currently unknown why the leaked data, in the form of a single SQL file, was generated in the first place.

Before it was [shut down](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-16-3/) by in an international joint operation across numerous law enforcement agencies in April 2022, RaidForums had built up a reputation as one of the top go-to forums for buying, selling, and dumping stolen data such as bank routing and account numbers, credit card information, login credentials, and social security numbers. The data leak doesn’t provide any new information to law enforcement but can prove useful to security researchers and their investigations.

Though there is a touch of poetic justice in seeing malicious hackers and cybercriminals having their data leaked onto a forum they visit, the existence of new forums like Exposed underscores how prevalent the demands are for trading in illicit and stolen data. After RaidForums was seized, another site called “BreachForums” was on track to become RaidForums’ would-be successor before it shut down in response to the [arrest](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-12-4/) of their founder. As new forums like Exposed continue to quickly fill the void and gain traction, businesses must remain vigilant with protecting their sensitive data.

## Malicious Python Libraries | Novel PyPi Malware Takes Aim at Digital Supply Chains

Observing a spike in malicious submissions to the [PyPi](https://www.sentinelone.com/labs/pypi-phishing-campaign-juiceledger-threat-actor-pivots-from-fake-apps-to-supply-chain-attacks/) (Python Package Index) repository, security researchers this week released a [report](https://securityboulevard.com/2023/06/when-byte-code-bites-who-checks-the-contents-of-compiled-python-files/) on what may be the first [supply chain attack](https://www.sentinelone.com/cybersecurity-101/what-is-supply-chain-attack/) to exploit Python byte code (PYC) files. Since these files can be directly executed, this novel attack method raises yet another concern in digital supply chains.

The package, called `fshec2`, was discovered in April and promptly removed from the repository on the same day, though the PyPi team told researchers that this type of attack was not previously seen before. According to their report, researchers were able to note a suspicious combination of behaviors from the `fshec2` package which contained the following three Python source files:

* `__init__.py` – the entry point of the package with the purpose of importing a function from main.py
* `main.py` – container for the Python source code with the purpose of loading the compiled module in `full.pyc`
* `full.pyc` – the malicious file capable of downloading commands from a remote server.

[![](https://www.sentinelone.com/wp-content/uploads/2023/06/main_py_fshec2.jpg)](https://www.sentinelone.com/?attachment_id=81183)

Loading of the compiled Python module from *main.py* (Source: SecurityBoulevard)

The `fshec2` malware was observed using the import to trigger a novel loading technique instead of using an import directive to load a Python compiled module – a commonly detectable method seen in attacks. Upon analysis, the researchers found a number of mistakes in the malware’s initial configuration suggesting that it was not the work of [advanced persistent threat](https://www.sentinelone.com/cybersecurity-101/advanced-persistent-threat-apt/) (APT) groups nor a state-sponsored actor.

While this malware was spotted early, it’s a reminder that threat actors are [increasingly targeting](https://www.sentinelone.com/labs/cratedepression-rust-supply-chain-attack-infects-cloud-ci-pipelines-with-go-malware/) public code repositories in an effort to breach companies via third-party dependencies. Consequently, supply chain security must continue to be a main priority for enterprises.

## Zero-Day Vulnerability | Flaw In Popular File Transfer Tool Used to Steal Data

MOVEit Transfer, a widely-used file transfer automation solution, [disclosed](https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-31May2023) a vulnerability this week that gives attackers unauthorized access to users’ systems. Designed to securely transfer data and assets between customers and their business partners through SFTP-, SCP-, and HTTP-based uploads, MOVEit is currently used worldwide by thousands of organizations. CISA [warned](https://www.cisa.gov/news-events/alerts/2023/06/01/progress-software-releases-security-advisory-moveit-transfer) this week that mass exploitation of the flaw has already been observed in the wild and data from a number of users’ systems has been stolen.

The [zero-day](https://www.sentinelone.com/cybersecurity-101/zero-day-vulnerabilities-attacks/), not yet assigned a CVE, is a severe SQL-injection vulnerability that allows privilege escalation and potential unauthorized access to the environment. Depending on the database engine being targeted (MySQL, Microsoft SQL Server, or Azure SQL), an attacker can gather valuable intel about the infrastructure and the contents of the database before executing SQL statements to alter or delete the database elements. The developers of MOVEit Transfer have since released patches for the vulnerability and urged customers to patch immediately.

[![](https://www.sentinelone.com/wp-content/uploads/2023/06/moveit_transfer_virustotal.jpg)](https://www.sentinelone.com/?attachment_id=81182)

Webshell code used for hacking the MOVEit has zero detections on VirusTotal (Source: GrindinSoft)

News of the zero-day vulnerability in MOVEit is the latest in a rising trend of attacks on file transfer solutions such as [Accellion’s](https://www.sentinelone.com/blog/to-be-continued-how-end-of-life-products-put-enterprises-at-risk/) File Transfer Appliance , [GoAnywhere’s](https://techcrunch.com/2023/03/22/fortra-goanywhere-ransomware-attack/) file transfer utility (CVE-2023-0669), and [IBM’s](https://therecord.media/ibm-aspera-faspex-bug-cisa-known-vulnerability-list) Aspera Faspex file transfer tool to name a few. As the global managed file transfer market continues to grow in demand from a [reported](https://www.globenewswire.c...