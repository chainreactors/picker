---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 49
url: https://buaq.net/go-138306.html
source: unSafe.sh - 不安全
date: 2022-12-03
fetch_date: 2025-10-04T00:22:57.931639
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 49

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

![](https://8aqnet.cdn.bcebos.com/705c2fb1e65708e2c753b1bd0f68f8b1.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 49

The GoodScammers who have stolen in excess of $12.8 million were arrested this week in Madrid and
*2022-12-2 22:0:55
Author: [www.sentinelone.com(查看原文)](/jump-138306.htm)
阅读量:52
收藏*

---

## The Good

Scammers who have stolen in excess of $12.8 million were arrested this week in Madrid and Barcelona. Part of a larger cybercrime organization, the scammers had used bogus investment sites to defraud hundreds of victims across Europe. Spanish law enforcement have since charged six members of the organization with suspected fraud and money laundering.

![](https://www.sentinelone.com/wp-content/uploads/2022/12/22-12-01-15-22-13-615_deco-scaled.jpg)

Victims of the cybercrime group spanned across various European countries including France, Spain, Portugal, and Poland. In hopes of avoiding tracing efforts, scammers had bounced the funds through several off-shore financial institutions, and then moved the money back to the crime group’s native bank accounts in Spain.

Authorities [reported](https://www.policia.es/_es/comunicacion_prensa_detalle.php?ID=14662) that the cybercrime group relied on phishing emails to drive traffic to fake websites. Posing as banks and [cryptocurrency](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/) vendors, the scammers tricked investors into making deposits using a malicious technique known as [typosquatting](https://www.sentinelone.com/cybersecurity-101/phishing-scams/). Typosquatting entails the registration of fraudulent domains that are very similar to the official websites of legitimate banks. In comparison to a real domain, the difference is only a few characters or a small typo. This technique takes advantage of unsuspecting users who overlook these minor differences and begin interacting with the scammer-owned site.

[Researchers](https://www.proofpoint.com/sites/default/files/threat-reports/Proofpoint_Threat_Research_Social_Engineering_Report_2022.pdf) warn that social engineering techniques including [phishing](https://www.sentinelone.com/blog/phishing-revealing-vulnerable-targets/) and typosquatting remain effective and that scammers will likely continue to prey on human behaviors and instincts for financial gain.

## The Bad

A breach on cloud storage services this week has hit both GoTo (formerly LogMeIn) and its affiliate company, popular password management giant, LastPass. Threat actors behind the breach were able to gain access to GoTo’s development environment and third-party cloud storage service. Since the incident, GoTo has [announced](https://www.goto.com/blog/our-response-to-a-recent-security-incident) that they are working with industry partners and law enforcement to launch a full-scale security investigation.

GoTo provides cloud-based remote work solutions for IT management and collaboration. The company reported that they first learned of the incident after detecting abnormal activity in both their development workspace and cloud storage. LastPass, which shares the same cloud service with its affiliate, [disclosed](https://blog.lastpass.com/2022/11/notice-of-recent-security-incident/) that “certain elements” of customer information were accessed by the threat actors.

> We recently detected unusual activity within a third-party cloud storage service, which is currently shared by both LastPass and its affiliate GoTo. Customer passwords remain safely encrypted due to LastPass’s Zero Knowledge architecture. More info: <https://t.co/xk2vKa7icq> [pic.twitter.com/ynuGVwiZcK](https://t.co/ynuGVwiZcK)
>
> — LastPass (@LastPass) [November 30, 2022](https://twitter.com/LastPass/status/1598047380305104896?ref_src=twsrc%5Etfw)

LastPass is no stranger to cyberattack, having revealed just last quarter that threat actors accessed their internal networks and made off with source code and proprietary technical information. The company confirmed that information stolen in the August 2022 intrusion was subsequently used to pave the way for this week’s breach. Customer passwords, however, were not compromised due to their [zero trust architecture](https://www.sentinelone.com/cybersecurity-101/zero-trust-architecture/).

Services for both affected companies remain fully operational, but data breaches like this are reflective of the [alarming rise](https://www.sentinelone.com/blog/all-eyes-on-cloud-why-the-cloud-surface-attracts-attacks/) in cloud-based cyberattacks on large enterprises. As threat actors capitalize on the high volumes of sensitive data flowing between the organizations and the cloud, more [attacks](https://www.sentinelone.com/blog/threat-landscape-the-most-dangerous-cloud-attack-methods-in-the-wild-today/) of the same nature will keep occurring. Large companies like LastPass, who claim to service 33 million global users currently, must prioritize implementing robust [cloud-based security](https://www.sentinelone.com/blog/cloud-computing-is-not-new-why-secure-it-now/) to protect themselves and their customers’ data.

## The Ugly

Google researchers this week [unveiled](https://blog.google/threat-analysis-group/new-details-on-commercial-spyware-vendor-variston/) their discovery of a Spain-based IT company trading in commercial spyware. Variston IT is described as an “information security solution provider” focusing on [IoT](https://www.sentinelone.com/blog/bringing-iot-out-of-the-shadows/) surveillance software, SCADA (supervisory control and data acquisition) technology, custom security patches, data discovery, and protocol development for embedded devices.

![](https://www.sentinelone.com/wp-content/uploads/2022/12/22-12-01-15-21-52-251_deco-scaled.jpg)

Researchers have found that Variston also sells advanced software frameworks that exploit [known vulnerabilities](https://www.sentinelone.com/blog/enterprise-security-essentials-top-15-most-routinely-exploited-vulnerabilities-2022/) in Windows Defender, Chrome, and Firefox. In the hands of a threat actor, such frameworks provide everything one would need to inconspicuously install malware and spy on targeted devices. Google’s Threat Analysis Group (TAG) explained that the malicious frameworks are built to exploit n-day vulnerabilities – flaws that have only been recently patched – allowing attackers to target those who have yet to update to the new versions.

After receiving the frameworks through an anonymous source, the researchers identified them as “Heliconia Noise”, “Heliconia Soft”, and “Files”. Heliconia Noise is capable of exploiting the Chrome renderer and escaping the Chrome security sandbox that usually isolates untrusted code from the rest of the system. Heliconia Soft is designed to exploit [CVE-2021-42298](https://nvd.nist.gov/vuln/detail/CVE-2021-42298), a JavaScript engine flaw within the Microsoft Defender Malware Protection product that grants high-level system privileges on Windows. Exploiting the use-after-free flaw [CVE-2022-26458](https://nvd.nist.gov/vuln/detail/CVE-2022-26458), the Files framework included a full-fledged exploit chain for Firefox running on Windows and Linux machines.

While Google TAG’s report on these frameworks noted that they had not detected evidence of active exploitation, they said it was likely the frameworks had been utilized as zero-days in the wild. This discovery highlights the issue of the commercial [surveillance](https://www.sentinelone.com/labs/modifiedelephant-apt-and-a-decade-of-fabricating-evidence/) industry, which is rapidly expanding globally. Exploit sellers contribute to an accelerated rise of dig...