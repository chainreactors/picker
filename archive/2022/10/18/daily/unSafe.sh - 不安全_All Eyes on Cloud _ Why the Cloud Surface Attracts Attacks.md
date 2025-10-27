---
title: All Eyes on Cloud | Why the Cloud Surface Attracts Attacks
url: https://buaq.net/go-131321.html
source: unSafe.sh - 不安全
date: 2022-10-18
fetch_date: 2025-10-03T20:04:25.247927
---

# All Eyes on Cloud | Why the Cloud Surface Attracts Attacks

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

![](https://8aqnet.cdn.bcebos.com/20943399ca283488f545961df64c4540.jpg)

All Eyes on Cloud | Why the Cloud Surface Attracts Attacks

Cloud environments have seen a meteoric rise in the past decade. What began as means of data storag
*2022-10-17 21:0:59
Author: [www.sentinelone.com(查看原文)](/jump-131321.htm)
阅读量:29
收藏*

---

Cloud environments have seen a meteoric rise in the past decade. What began as means of data storage has now become a full-scale computing platform, enabling a global shift in how businesses share, store, optimize, and manage information. However, [threat actors](https://www.sentinelone.com/blog/threat-actor-basics-understanding-5-main-threat-types/) have witnessed these changes and taken to targeting the cloud, knowing that more and more businesses continue to make the transition to hybrid workspaces and cloud technologies.

The same features that make cloud services beneficial to organizations are the same that make them attractive to threat actors. In recent years, [attacks on cloud environments](https://www.sentinelone.com/blog/endpoint-identity-and-cloud-top-cyber-attacks-of-2022-so-far/) have surged as threat actors took advantage of the high volumes of sensitive data flowing between organizations and their cloud service providers. Opportunistic by nature, threat actors thrive off of [weak credentials](https://www.sentinelone.com/blog/how-attackers-exploit-security-support-provider-ssp-for-credential-dumping/), misconfiguration, and human errors when it comes to planning their attacks on the cloud surface.

While the related security challenges haven’t slowed cloud adoption, organizations should be aware of their scope, significance, and how to secure against them. This blog post outlines why cloud has emerged as one of the most attacked surfaces and what [security measures](https://www.sentinelone.com/blog/ciso-wins-reducing-risk-across-endpoint-identity-and-cloud-surfaces/) businesses can implement to safeguard their cloud environment and data.

![](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/All-Eyes-on-Cloud-Why-the-Cloud-Surface-Attracts-Attacks-4.jpg?lossy=0&strip=1&webp=0)

## Cloud Attacks Are Rising

The number of reported attacks on clouds has increased dramatically in the last few years, in part spurred on by the [COVID-19](https://www.sentinelone.com/blog/three-key-challenges-for-cloud-security-in-a-world-changed-by-covid-19/) pandemic when businesses of all sizes needed to adapt quickly to alternative means of operation.

[According to Gartner](https://www.gartner.com/en/newsroom/press-releases/2021-11-10-gartner-says-cloud-will-be-the-centerpiece-of-new-digital-experiences), the pandemic along with a surge in digital services have made cloud the “centerpiece of new digital experiences”, and global cloud revenue will total $474 billion this year – a $66 billion dollar increase from 2021. The research firm also predicts that more than 95% of new digital workloads will be deployed on cloud-native platforms resulting in a 30% increase from the year before.

Businesses need to plan beyond traditional security strategies to manage a widening enterprise attack surface as well as the risks associated with cloud services. The following statistics show the rise in cloud adoption and just how much clouds have come under attack in the last few years:

* 69% of organizations have accelerated their cloud migration in the last 12 months. The percentage of organizations with most or all of their IT infrastructure in the cloud is expected to increase from 41% to 63% in the next 18 months [(Foundry, 2022)](https://resources.foundryco.com/download/cloud-computing-executive-summary).
* 49% of IT professionals reported that cloud-based attacks led to unplanned expenses.
* 80% of CISOs surveyed by [PurpleSec](https://purplesec.us/resources/cyber-security-statistics) were unable to identify instances of excessive access to data in their cloud environments.
* 79% of organizations have suffered at least one cloud-based data breach in the last 18 months. Further, 43% have reported 10 or more breaches within that same time frame [(Emertic, 2021)](https://ermetic.com/blog/cloud/state-of-cloud-security-2021-more-aware-yet-very-exposed/).
* 83% of cloud breaches are derived from access-related vulnerabilities [(CyberTalk.org, 2021)](https://www.cybertalk.org/2021/10/20/key-cloud-security-statistics-that-will-reshape-your-cloud-perspectives/).

## Understanding Cloud Risks

Using cloud services inherently exposes organizations to new security challenges, often related to unauthorized access, insider threats, and supply chain risks. To a threat actor, cloud vulnerabilities are means of gaining access to exfiltrate data from the targeted organization’s network whether by [service disruptions](https://www.sentinelone.com/blog/look-whos-back-its-ddos/), [ransomware](https://www.sentinelone.com/blog/the-changing-nature-of-the-ransomware-menace-today/), or unauthorized data transfer. More sophisticated threat actors may employ lateral movement and detection evasion techniques, or account takeovers to establish and maintain a long-term foothold within the targeted network before leveraging existing services and tools found within it.

Common cloud security [risks](https://www.sentinelone.com/blog/surviving-the-storm-defending-against-cloud-misconfigurations-vulnerabilities-and-insider-threats/) include the following:

* User Account Takeovers – Whether credentials are stolen through [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/), brute force, or malware, weak password policies often lead to compromised user accounts.
* Misconfiguration – Cloud service providers offer different tiers depending on the needs of the organization. This allows the cloud to work to scale with the organization. However, many organizations lack the security posture needed to ensure the safety of these services, resulting in security risks in the deployment stage of implementation. Misconfigured servers are a leading cause of compromise when it comes to cloud-based attacks.
* Vulnerable Public APIs – Public APIs allow trusted users to interact and operate within the cloud. If exploited, these APIs become a straightforward method for threat actors to gain access to the platform and exfiltrate sensitive data in the cloud database. Further, if the original configuration of the API harbors any vulnerabilities, this leaves threat actors with a backdoor for future exploits.
* Insider Threats – Even organizations with a healthy cyber ecosystem can fall victim to a legitimate, malicious user with a mind to leak data. Malicious users often already have access to sensitive or critical data, and may also have the permissions to remove certain security protocols. The threat of [malicious insiders](https://www.sentinelone.com/blog/insider-threats-from-malicious-to-unintentional/) is greatly minimized through zero-trust policies and identity and access management solutions.
* Denial-of-Service (DoS) Attacks – Designed to overload a system and bar users from accessing services, DoS attacks are especially devastating to cloud environments. When the [workload](https://www.sentinelone.com/blog/accelerating-your-cloud-security-with-workload-protection/) increases in a cloud environment, it will provide extra computational power to address the extra load. Eventually, the cloud slows down and legitimate users lose their access to any files in the cloud.
* Third-Party Vendors – It is important for organizations to assess third-party risks when using vendor services. Clouds are susceptible to supply chain a...