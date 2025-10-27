---
title: Fighting Telecom Cyberattacks: Investigating a Campaign Against UK Companies
url: https://any.run/cybersecurity-blog/fighting-telecom-attacks-with-anyrun/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-25
fetch_date: 2025-10-02T20:39:46.526886
---

# Fighting Telecom Cyberattacks: Investigating a Campaign Against UK Companies

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![Fighting Telecom Cyberattacks: Investigating a Campaign Against UK Companies](/cybersecurity-blog/wp-content/uploads/2025/09/telecom_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Fighting Telecom Cyberattacks: Investigating a Campaign Against UK Companies

September 24, 2025

[Add comment](#comments-15944)
4275 views
10 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Fighting Telecom Cyberattacks: Investigating a Campaign Against UK Companies

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  58
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  1620
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  1476
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Fighting Telecom Cyberattacks: Investigating a Campaign Against UK Companies

Telecommunications companies are the digital arteries of modern civilization. Compromise a major telecom operator, and you don’t just steal data — you gain the power to intercept communications, manipulate network traffic, and bring entire regions offline.

Every day, [ANY.RUN’s solutions](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=telecom_attacks&utm_term=240925&utm_content=linktolanding) process thousands of threat samples, and hidden within them are patterns of activity targeting telecom operators. Some are opportunistic, others are advanced and carefully orchestrated.

In this report, we’ll walk through real-world attacks where threat actors weaponized telecom brand trust to launch attacks. We’ll also show how analysts can detect these threats, extract indicators of compromise ([IOCs](https://any.run/cybersecurity-blog/iocs-iobs-ioas-explained/)), and strengthen defenses.

## Key Takeaways

* **Telecommunications under siege:** The telecom sector faced sustained growth in malicious activity from May-July 2025, with 56% of observed APT campaigns targeting telecom and media companies.

* **Brand impersonation is weaponized trust:** Attackers systematically abuse telecom brand recognition, using familiar logos, official-looking domains, and corporate communication styles to bypass human skepticism and technical filters.

* **Pattern recognition defeats mass campaigns**: Simple YARA rules can expose large-scale operations.

* **[Tycoon2FA phishing kit](https://any.run/cybersecurity-blog/tycoon2fa-evasion-analysis/) remains active:** The phishing framework designed to steal Microsoft credentials and bypass two-factor authentication is a critical concern for enterprise telecom environments.

* **Interactive Sandbox reveals multi-stage attack progression**: [ANY.RUN’s Interactive Sandbox](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=telecom_attacks&utm_term=240925&utm_content=linktosandboxlanding) captured the complete attack flow from the initial PDF attachment to the final phishing page. This real-time analysis exposed the redirection chain from legitimate-looking emails to DGA-generated domains (xjrsel.ywnhwmard[.]es), enabling early detection before credentials could be harvested.

* **Proactive hunting scales defense:** Combining YARA Search with [Threat Intelligence Lookup](https://intelligence.any.run/analysis/lookup?utm_source=anyrunblog&utm_medium=article&utm_campaign=telecom_attacks&utm_term=240925&utm_content=linktotilookup) transforms reactive incident response into proactive threat hunting, enabling security teams to build comprehensive defense before attacks succeed.

## Recent Telecom Attack Dynamics

Attacks on communication operators can disrupt critical services, lead to leaks of confidential information, and be used as a springboard for large-scale cyber espionage operations.

According to Cyfirma, telecommunications and media industry were targeted in 9 out of 16 observed [APT](https://any.run/cybersecurity-blog/track-advanced-persistent-threats/) campaigns in May–July 2025, accounting for 56% of all cases. The peak activity occurred in May, followed by a slight decline in June and a renewed increase in July.

We at ANY.RUN have observed a steady increase in telecom-targeting attacks in May–July 2025. The Sandbox data shows a smoother continuous growth, reaching a maximum in July. This reflects the constant pressure of mass attacks.

![](/cybersecurity-blog/wp-content/uploads/2025/09/image3-3.png)

In our [Threat Intelligence Reports](https://intelligence.any.run/reports/) highlighting the activity of top APT groups, we also see an increased targeting of media and telecom campaigns in the recent attacks.

## Analysis of Threats Targeting a Major Telecom Holding

Let’s take the perspective of an information security specialist at a huge Bri...