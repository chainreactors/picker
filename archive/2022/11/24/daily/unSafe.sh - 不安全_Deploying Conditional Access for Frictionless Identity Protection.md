---
title: Deploying Conditional Access for Frictionless Identity Protection
url: https://buaq.net/go-136942.html
source: unSafe.sh - 不安全
date: 2022-11-24
fetch_date: 2025-10-03T23:36:54.469236
---

# Deploying Conditional Access for Frictionless Identity Protection

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

![](https://8aqnet.cdn.bcebos.com/6faa5ab06d105aa719d6be827356da12.jpg)

Deploying Conditional Access for Frictionless Identity Protection

With the rapid change in modern technologies, workforces are increasingly mobile and require direct
*2022-11-23 22:36:57
Author: [www.sentinelone.com(查看原文)](/jump-136942.htm)
阅读量:26
收藏*

---

With the rapid change in modern technologies, workforces are increasingly mobile and require direct access to applications across hybrid IT environments. They often access both on-premises and cloud applications from various devices and locations, some of which could be using public or unencrypted networks. At the same time, security teams have realized that the directory service widely used to manage the required identity-related services, [Active Directory](https://www.sentinelone.com/blog/active-directory-security/), is vulnerable, and identifying its loopholes to protect it from various attacks is a considerable challenge.

How can organizations detect and block identity-related attacks before adversaries or malicious insiders establish complete Active Directory Domain Controller (DC) dominance? How can they most effectively protect critical assets against advanced identity-based attacks?

The best approach is conditional access, which enables administrators to allow or deny access to resources based on the detection of suspicious or malicious activity. In this post, we’ll discuss conditional access solutions, why they are important, and how they can strengthen the overall security posture of an organization.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Deploying-Conditional-Access-for-Frictionless-Identity-Protection-2.jpg)

## The Growing Risk of Identity-related Breaches

Identity-related breaches remain the most significant threat of compromise, lost data, or malicious operations. According to the Identity Defined Security Alliance ([IDSA](https://www.idsalliance.org/white-paper/2022-trends-in-securing-digital-identities/)) report, 84% of organizations experienced an identity-related breach in the past year, 2021. The most common attacks are phishing attacks (59%), inadequately managed privileges (36%), and stolen credentials (33%).

![phishing attempts in 2021](https://www.sentinelone.com/wp-content/uploads/2022/11/Conditional_Access_5.jpg)

[Research](https://www.businesswire.com/news/home/20210930005642/en/Research-Finds-Attackers-Targeting-Active-Directory-50-of-Businesses-Experienced-an-Attack-with-40-Success) conducted by Enterprise Management Associates also reported that 50% of organizations experienced an attack on Active Directory (AD), with more than 40% indicating the attack was successful.

Microsoft AD is the [prime target](https://www.sentinelone.com/blog/microsoft-active-directory-as-a-prime-target-for-ransomware-operators/) for malicious operations. When attackers gain access to a compromised network, they attempt to discover domain identities and expand access to applications and data with stolen credentials. They can establish persistence, escalate privileges, and move laterally. Attackers attempt to take complete domain dominance through various means, such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003/), stealing, or forging Kerberos tickets to perform a [Pass-the-ticket Attack](https://www.sentinelone.com/blog/sentinelone-debuts-at-the-top-of-mitre-engenuity-attck-deception-evaluation-see-why/).

## What Is Conditional Access and Why Is It Important?

Conditional access refers to the policy-driven concept of allowing access to corporate resources only when certain criteria are met. The solution is traditionally used in authentication systems to grant access to applications only if users go through Multi-Factor Authentication (MFA) while accessing a trusted resource from a new location or when attempting to access applications or data of a sensitive nature.

The same approach has been adopted for threat protection as well. Conditional access provides an extended layer of security by allowing secure access to on-premises and cloud applications only from trusted users or devices.

Conditional access is a mechanism to enforce access control policies based on suspicious or malicious activity. It is a risk-driven approach calculated based on risk factors such as severity and type of attack, among others.

Perimeter-based security is the traditional and obsolete solution for protecting external attackers from accessing the corporate network and applications. An identity security solution which offers conditional access capabilities allows security administrators to respond to the identified suspicious activities. It can help to quickly detect anomalous user or device behavior, restricting or allowing access to sensitive corporate resources. Conditional access enables administrators to set allow/deny conditions based on the severity of the threat detected.

Every organization can benefit from the following key features of conditional access solutions to improve their defense against threats and provide secure services to their users.

* Frictionless Identity Protection – Allow seamless user access without causing friction by quickly identifying threats and isolating systems before exfiltrating the data.
* Risk Driven Protection – Enforce access policy to Allow/Block using MFA based on the risk level of threats detected.
* Reduced Attack Surface – Significantly reduce the attack surface available for malicious activity against both on-premises and cloud applications.

## What Can SentinelOne Singularity Identity’s Conditional Access Offer?

The [Singularity™ Identity](https://www.sentinelone.com/platform/singularity-identity/) solution offers deep packet inspection, identifies abnormal behavior, and detects suspicious activities. The solution detects attackers conducting reconnaissance of AD objects based on SAMR (Security Account Manager Remote), LSARPC (Local Security Authority Remote Procedure Call), and LDAP (Lightweight Directory Access) protocols.

An attacker with discovered AD objects can perform the following domain dominance attacks. The solution can detect these attacks in real-time and apply the conditional access protection policy configured for each type of attack.

* [Golden Ticket](https://www.sentinelone.com/blog/how-kerberos-golden-ticket-attacks-are-signaling-a-greater-need-for-identity-based-security/)
* [Silver Ticket Attack](https://www.attivonetworks.com/kerberos-silver-ticket-attack/)
* [Skeleton Key Attack](https://www.attivonetworks.com/blogs/skeleton-key-vulnerability-assessment/)
* [Pass-the-ticket Attack](https://www.sentinelone.com/blog/sentinelone-debuts-at-the-top-of-mitre-engenuity-attck-deception-evaluation-see-why/)
* Forged PAC Attack
* [DCSync Attack](https://www.sentinelone.com/blog/active-directory-dcsync-attacks/)
* [DCShadow Attack](https://www.sentinelone.com/blog/detecting-a-rogue-domain-controller-dcshadow-attack/)
* Pass-the-hash
* Overpass-the-hash Attack
* AS-REP Roasting Attack

![identity-based attacks](https://www.sentinelone.com/wp-content/uploads/2022/11/Conditional_Access_1.jpg)

SentinelOne’s [Singularity™ Identity](https://www.sentinelone.com/platform/singularity-identity/) conditional access solution also offers an extra layer of security for users accessing cloud applications. The solution enforces risk-driven policies at third-party identity providers based on suspicious activities detected. It can trigger a push notification through MFA and only allow access if approved.

For example, a condition can allow the triggering of MFA for the attack severity of the “Hi...