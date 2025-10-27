---
title: Ransomware Hackers Using New Way to Bypass MS Exchange ProxyNotShell Mitigations
url: https://thehackernews.com/2022/12/ransomware-hackers-using-new-way-to.html
source: The Hacker News
date: 2022-12-22
fetch_date: 2025-10-04T02:15:37.035049
---

# Ransomware Hackers Using New Way to Bypass MS Exchange ProxyNotShell Mitigations

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

# [Ransomware Hackers Using New Way to Bypass MS Exchange ProxyNotShell Mitigations](https://thehackernews.com/2022/12/ransomware-hackers-using-new-way-to.html)

**Dec 21, 2022**Ravie LakshmananEmail Security / Data Security

[![MS Exchange ProxyNotShell RCE](data:image/png;base64... "MS Exchange ProxyNotShell RCE")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTLGmaNN3OFFmSILTclxE-UymYSclEFgrwvp76liyrsFGtPk5wpNGVl-AXdppW10UvY5aPmtLoqkxVC3ifpEx9XH3JarmYqPPQtscOXnAMl0K3lHF2nV6pcyicT2bu5U9BbJFd6hbBBVHswmATwzgzQEMc6GEUPcs4-k1yW0cjoEdfsN0LDRvVh5Ty/s790-rw-e365/email-hacking.png)

Threat actors affiliated with a ransomware strain known as Play are leveraging a never-before-seen exploit chain that bypasses blocking rules for ProxyNotShell flaws in Microsoft Exchange Server to achieve remote code execution (RCE) through Outlook Web Access ([OWA](https://en.wikipedia.org/wiki/Outlook_on_the_web)).

"The new exploit method bypasses [URL rewrite mitigations](https://thehackernews.com/2022/10/microsoft-issues-improved-mitigations.html) for the [Autodiscover endpoint](https://learn.microsoft.com/en-us/exchange/architecture/client-access/autodiscover)," CrowdStrike researchers Brian Pitchford, Erik Iker, and Nicolas Zilio [said](https://www.crowdstrike.com/blog/owassrf-exploit-analysis-and-recommendations/) in a technical write-up published Tuesday.

Play ransomware, which first surfaced in June 2022, has been [revealed](https://www.trendmicro.com/en_us/research/22/i/play-ransomware-s-attack-playbook-unmasks-it-as-another-hive-aff.html) to adopt many tactics employed by other ransomware families such as [Hive](https://thehackernews.com/2022/11/hive-ransomware-attackers-extorted-100.html) and [Nokoyawa](https://www.trendmicro.com/en_us/research/22/c/nokoyawa-ransomware-possibly-related-to-hive-.html), the latter of which [upgraded to Rust](https://www.zscaler.com/blogs/security-research/nokoyawa-ransomware-rust-or-bust) in September 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity company's investigations into several Play ransomware intrusions found that initial access to the target environments was not achieved by directly exploiting [CVE-2022-41040](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040), but rather through the OWA endpoint.

Dubbed **OWASSRF**, the technique likely takes advantage of another critical flaw tracked as [CVE-2022-41080](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41080) (CVSS score: 8.8) to achieve privilege escalation, followed by abusing [CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082) for remote code execution.

[![MS Exchange ProxyNotShell RCE](data:image/png;base64... "MS Exchange ProxyNotShell RCE")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh59pwm9Kxv252Uv99amN02oXTHDo8okfVqDQEPqxZy2wZk0tCTHx16xDzABz2QYvABQfBENatlbN2owTSezPh4jYOK-0bGPr_JyWKUPsX1nnLeX5X9za6Rfk5c-juoJI5Q9NT97ANp9X64VSnb_EWUp5s1jYoZJap_uzgruqlI0kYKYqqtMvM5hZQm/s790-rw-e365/email-security.png)

It's worth noting that both CVE-2022-41040 and CVE-2022-41080 stem from a case of server-side request forgery ([SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)), which permits an attacker to access unauthorized internal resources, in this case the [PowerShell remoting](https://learn.microsoft.com/en-us/powershell/exchange/exchange-management-shell) service.

CrowdStrike said the successful initial access enabled the adversary to drop legitimate Plink and AnyDesk executables to maintain persistent access as well as take steps to purge Windows Event Logs on infected servers to conceal the malicious activity.

All three vulnerabilities were addressed by Microsoft as part of its [Patch Tuesday updates](https://thehackernews.com/2022/11/install-latest-windows-update-asap.html) for November 2022. It's, however, unclear if CVE-2022-41080 was actively exploited as a zero-day alongside CVE-2022-41040 and CVE-2022-41082.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Windows maker, for its part, has tagged CVE-2022-41080 with an "Exploitation More Likely" assessment, implying it's possible for an attacker to create exploit code that could be utilized to reliably weaponize the flaw.

CrowdStrike further noted that a proof-of-concept (PoC) Python script [discovered](https://twitter.com/Purp1eW0lf/status/1602989967776808961) and leaked by Huntress Labs researcher Dray Agha last week may have been put to use by the Play ransomware actors for initial access.

This is evidenced by the fact that the execution of the Python script made it possible to "replicate the logs generated in recent Play ransomware attacks."

"Organizations should apply the November 8, 2022 patches for Exchange to prevent exploitation since the URL rewrite mitigations for ProxyNotShell are not effective against this exploit method," the researchers said.

### Update

Cybersecurity company Rapid7, in a related advisory on Wednesday, said it has observed an "increase in the number of Microsoft Exchange Server compromises" through the aforementioned OWASSRF exploit chain to gain remote code execution.

"Patched servers do not appear vulnerable, servers only utilizing Microsoft's mitigations do appear vulnerable," Rapid7 researcher Glenn Thorpe [noted](https://www.rapid7.com/blog/post/2022/12/21/cve-2022-41080-cve-2022-41082-rapid7-observed-exploitation-of-owassrf-in-exchange-for-rce/). "Threat actors are using this to deploy ransomware."

In a statement shared with The Hacker News, a Microsoft spokesperson said "the reported method exploits vulnerable systems that have not applied our latest security updates," adding "customers should prioritize installing the latest updates, specifically our [November 2022 Exchange Server updates](https://techcommunity.microsoft.com/t5/exchange-team-blog/released-november-2022-exchange-server-security-updat...