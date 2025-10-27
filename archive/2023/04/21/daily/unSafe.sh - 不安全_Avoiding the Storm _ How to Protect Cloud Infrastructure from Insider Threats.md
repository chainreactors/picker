---
title: Avoiding the Storm | How to Protect Cloud Infrastructure from Insider Threats
url: https://buaq.net/go-159691.html
source: unSafe.sh - 不安全
date: 2023-04-21
fetch_date: 2025-10-04T11:32:28.136150
---

# Avoiding the Storm | How to Protect Cloud Infrastructure from Insider Threats

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

![](https://8aqnet.cdn.bcebos.com/214601885bbc527628108518b879db49.jpg)

Avoiding the Storm | How to Protect Cloud Infrastructure from Insider Threats

One of the most significant security threats to cloud infrastructure is insider threats. As more bu
*2023-4-20 22:58:36
Author: [www.sentinelone.com(查看原文)](/jump-159691.htm)
阅读量:30
收藏*

---

One of the most significant security threats to cloud infrastructure is insider threats. As more businesses move to cloud and hybrid environments, employees sending sensitive data to unsecured or [misconfigured](https://www.sentinelone.com/blog/surviving-the-storm-defending-against-cloud-misconfigurations-vulnerabilities-and-insider-threats/) clouds risk exposing their organization to advanced cyber threats and opportunistic attackers.

The importance of cloud infrastructure to businesses of all sizes along with the privileged access that insiders often have mean that mitigating the risk of insider threats is now high on the list of priorities for mature security teams. In this post, we describe and explore best practices that security teams can implement to safeguard cloud infrastructures from insider threats.

![](https://www.sentinelone.com/wp-content/uploads/2023/04/Avoiding-the-Storm-How-to-Protect-Cloud-Infrastructure-from-Insider-Threats-8.jpg)

## Why Are Insiders Considered a Main Risk to Cloud?

Whether out of negligence or presenting malicious intent, insider threats pose a serious [risk](https://www.sentinelone.com/blog/all-eyes-on-cloud-why-the-cloud-surface-attracts-attacks/) to cloud security as they are harder to detect and respond to. Since they are already part of the organization, they are considered ‘trusted’. Unlike an external intruder, insiders do not have to breach external security measures to access sensitive assets.

Insider risks can stem from a great many reasons. Malicious insiders, for example, may be motivated to do harm to a system in return for a bribe or in retaliation for a perceived slight. Their goals can range from intentional data theft, data destruction, espionage, or personal benefit.  Since malicious insiders have the benefit of time, they are able to study the system and craft a serious attack based on specific weak points in the infrastructure they are privy to.

In Ponemon’s most recent [research](https://protectera.com.au/wp-content/uploads/2022/03/The-Cost-of-Insider-Threats-2022-Global-Report.pdf) on Insider Threats, the findings reveal that both negligent and malicious insider risks as well as credential theft have grown 44% in the last two years alone. Incidents involving compromised users have since racked up costs amounting to over $15 million dollars globally.

In many of these incidents, cloud infrastructures have been the main target with Ponemon’s report indicating that 52% of enterprises name [cloud security](https://www.sentinelone.com/cybersecurity-101/cloud-security/) as one of their greatest risks.

The following best practices can help security teams to mitigate these risks.

## 1. Implement Least Privilege Access Control

Defending against insider threats is a persistent challenge that requires continuous monitoring. One of the key ways to defend sensitive data and systems is to limit the number of users who have access to it as well as the permissions they have whilst exercising that access. To minimize the access of potential insider risk, enterprises can implement the principle of least privilege (PoLP).

The principle of least privilege is a security concept that states that every user, program, or system component should only have access to the resources they need to perform their function and no more. This works to minimize the potential damage that can happen as a result of a security breach or a misconfiguration.

The idea behind the principle of least privilege is that by limiting access to resources, the attack surface is [reduced](https://www.sentinelone.com/blog/ciso-wins-reducing-risk-across-endpoint-identity-and-cloud-surfaces/). By limiting the resources that a user or program can access, it makes it more difficult for attackers to gain access to sensitive information. For example, a user who only needs to read files in a specific directory should not have write access to that directory. Similarly, a program that only needs to access certain system files should not have access to other parts of the system.

## 2. Conduct Regular Security Awareness Training

An uncomfortable fact is that sometimes, insider behavior is carried out unknowingly by a negligent or untrained legitimate user. The Ponemon report cited 56% of incidents related to negligence in comparison to the 26% related to criminal insiders. This makes negligence a root cause in most cybersecurity incidents and varies anywhere from unsecured devices, unprotected passwords, not following their organization’s security policies, or forgetting to patch or upgrade their software.

Unintentional insider threats can arise from the smallest of actions, such as clicking on malicious links or sharing sensitive information with unauthorized individuals. Enterprise leaders can combat this type of insider threat by implementing regular and accessible security awareness training and fostering a culture of good cyber hygiene. Employees who are trained on how to recognize the signs and consequences of insider risks can help prevent them from occurring in the first place. Security awareness training programs often cover a wide range of topics including phishing, password hygiene, social engineering recognition, and how to correctly report anomalous behavior they see.

## 3. Use Behavioral Analytics

Behavioral analytics can be a powerful tool for security teams working to mitigate insider risks in their cloud environments. By measuring real-time behaviors against a predetermined state of normalcy, analytics can help raise a red flag on any anomalies that may indicate potential malicious activity.

For instance, behavioral analytics can monitor user activities such as login times, locations, and access patterns to detect any suspicious changes or deviations from their normal behavior. It can also detect attempts to access unauthorized resources, perform unauthorized actions, or exfiltrate data.

Behavioral analytics is instrumental to how security teams streamline their hunt for potential insider threats. The more time is saved during that crucial hunting stage, the more effective the response can be in stopping incidents from becoming full-blown security crises. Even in post-event processes, behavioral analytics provides valuable insights into the motivations and patterns of insider threats, helping teams to develop or improve their existing security policies and procedures. Learning from the analytic is often a strong foundation upon which training programs can be created.

## 4. Implement DSPM (Data Security Posture Management)

Planning the security of business-critical data requires a comprehensive approach to data security and privacy. Implementing data security posture management (DSPM) can help enterprises manage their data access and prevent data leakage by implementing policies and controls to protect sensitive data from unauthorized access, sharing, and exfiltration.

In cloud infrastructures, DSPM is designed to help prevent insider threats by detecting and blocking attempts to transmit sensitive data outside the infrastructure. It works by:

* Controlling Access – DSPM can help enforce access control policies, ensuring that only authorized users have access to sensitive data. This can include implementing role-based access controls, m...