---
title: Threat Assessment: Luna Moth Callback Phishing Campaign
url: https://buaq.net/go-136619.html
source: unSafe.sh - 不安全
date: 2022-11-22
fetch_date: 2025-10-03T23:22:55.664910
---

# Threat Assessment: Luna Moth Callback Phishing Campaign

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

![](https://8aqnet.cdn.bcebos.com/2d1eae7d662b2981e3a9a88e57316f6b.jpg)

Threat Assessment: Luna Moth Callback Phishing Campaign

This post is also available i
*2022-11-21 19:0:27
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-136619.htm)
阅读量:43
收藏*

---

![Cybercrime conceptual image, covering activity such as the Luna Moth callback phishing campaign](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/Unit42-blog-2by1-characters-r4d1-2020_crime-orange.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/luna-moth-callback-phishing/)

## Executive Summary

Unit 42 investigated several incidents related to the Luna Moth/Silent Ransom Group callback phishing extortion campaign targeting businesses in multiple sectors including legal and retail. This campaign leverages extortion without encryption, has cost victims hundreds of thousands of dollars and is expanding in scope.

By design, this style of social engineering attack leaves very few artifacts because of the use of legitimate trusted technology tools to carry out attacks. However, Unit 42 has identified several common indicators implying that these attacks are the product of a single highly organized campaign. This threat actor has significantly invested in call centers and infrastructure that’s unique to each victim.

Cybersecurity awareness training is the most effective defense against these stealthy and discreet attacks. However, Palo Alto Networks customers receive protection from the attacks discussed in this blog through the Next-Generation Firewall and Cortex XDR detecting data exfiltration or connections to suspicious networks.

## Table of Contents

[What Is Callback Phishing?](#post-125832-_gr0hbrkqr2av)

## What Is Callback Phishing?

Callback phishing, also referred to as telephone-oriented attack delivery (TOAD), is a social engineering attack that requires a threat actor to interact with the target to accomplish their objectives. This attack style is more resource intensive, but less complex than script-based attacks, and it tends to have a much higher success rate.

In the past, threat actors associated with the [Conti group](https://unit42.paloaltonetworks.com/conti-ransomware-gang/) have had great success with this attack style in the BazarCall campaign. [Unit 42 has been tracking these types of attacks since 2021](https://unit42.paloaltonetworks.com/bazarloader-malware/). Early iterations of this attack focused on tricking the victim into downloading the BazarLoader malware using documents with malicious macros.

This new campaign, which [Sygnia has attributed to a threat actor dubbed "Luna Moth](https://blog.sygnia.co/luna-moth-false-subscription-scams)," does away with the malware portion of the attack. In this campaign, attackers use legitimate and trusted systems management tools to interact directly with a victim’s computer, to manually exfiltrate data to be used for extortion. As these tools are not malicious, they’re not likely to be flagged by traditional antivirus products.

Please note that the tools named in this post are legitimate. Threat actors often abuse, take advantage of or subvert legitimate products for malicious purposes. This does not imply a flaw or malicious quality to the legitimate product being abused.

## The Typical Callback Phishing Attack Chain

The initial lure of this campaign is a phishing email to a corporate email address with an attached invoice indicating the recipient’s credit card has been charged for a service, usually for an amount under $1,000. People are less likely to question strange invoices when they are for relatively small amounts. However, if people targeted by these types of attacks reported these invoices to their organization’s purchasing department, the organization might be better able to spot the attack, particularly if a number of individuals report similar messages.

The phishing email is personalized to the recipient, contains no malware and is sent using a legitimate email service. These phishing emails also have an invoice attached as a PDF file. These features make a phishing email less likely to be intercepted by most email protection platforms.

The attached invoice includes a unique ID and phone number, often written with extra characters or formatting to prevent data loss prevention (DLP) platforms from recognizing it. When the recipient calls the number, they are routed to a threat actor-controlled call center and connected to a live agent.

Under the guise of canceling the subscription, the threat actor agent guides the caller through downloading and running a remote support tool to allow the attacker to manage the victim’s computer. This step usually generates another email from the tool’s vendor to the victim with a link to start the support session.

The attacker then downloads and installs a remote administration tool that allows them to achieve persistence. If the victim does not have administrative rights on their computer, the attacker will skip this step and move directly to finding files for exfiltration.

The attacker will then seek to identify valuable information on the victim’s computer and connected file shares, and they will quietly exfiltrate it to a server they control using a file transfer tool.

In this way, the threat actor is able to compromise organizational assets through a social engineering attack on an individual.

After the data is stolen, the attacker sends an extortion email demanding victims pay a fee or else the attacker will release the stolen information. If the victim does not establish contact with the attackers, they will follow up with more aggressive demands. Ultimately, attackers will threaten to contact victims’ customers and clients identified through the stolen data, to increase the pressure to comply.

## Luna Moth Campaign Analysis

Unit 42 has responded to multiple cases related to a single campaign that occurred from mid-May to late October 2022. [ADVIntel attributes this campaign to a threat actor dubbed Silent Ransom](https://www.advintel.io/post/bazarcall-advisory-the-essential-guide-to-call-back-phishing-attacks-that-revolutionized-the-data) with ties to Conti. While Unit 42 cannot confirm Silent Ransom’s tie to Conti at this time, we are monitoring this closely for attribution.

These cases show a clear evolution of tactics that suggests the threat actor is continuing to improve the efficiency of their attack. Cases analyzed at the beginning of the campaign targeted individuals at small- and medium-sized businesses in the legal industry. In contrast, cases later in the campaign indicate a shift in victimology to include individuals at larger targets in the retail sector.

During the initial campaign, the phishing email frequently originated from an address using the format FirstName.LastName.[SpoofedBusiness]@gmail[.]com as seen in Figure 1. The attacker often spoofs the names of obscure athletes for these email addresses.

Unit 42 has also observed emails with the format [RandomWords]@outlook[.]co.th.

![Phishing image, with subject line including "thank you for subscribing". Body of the email indicates that the subscription will be activated and paid in 24 hours. It also instructs the target to look at the attached invoice if they have any problems, and directs them to call their "customer support" number. The scheme, used by Luna Moth, is known as callback phishing.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-56.png)

Figure 1. Redacted phishing email.

The wording in the body of the phishing email has changed throughout the cam...