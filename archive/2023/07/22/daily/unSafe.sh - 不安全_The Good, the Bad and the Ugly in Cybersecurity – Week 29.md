---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 29
url: https://buaq.net/go-172675.html
source: unSafe.sh - 不安全
date: 2023-07-22
fetch_date: 2025-10-04T11:52:26.964463
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 29

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

![](https://8aqnet.cdn.bcebos.com/f482afde97b4a73e6306516b67f71f7d.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 29

The Good | The White House Unveils Cybersecure Labeling Program for IoT DevicesA U.S.-wide cyberse
*2023-7-21 21:0:25
Author: [www.sentinelone.com(查看原文)](/jump-172675.htm)
阅读量:22
收藏*

---

## The Good | The White House Unveils Cybersecure Labeling Program for IoT Devices

A U.S.-wide cybersecurity certification and labeling program [launched](https://www.whitehouse.gov/briefing-room/statements-releases/2023/07/18/biden-harris-administration-announces-cybersecurity-labeling-program-for-smart-devices-to-protect-american-consumers/) this week to guide consumers in choosing tech products that are less vulnerable to attack. The latest from the Biden-Harris administration, the “U.S. Cyber Trust Mark” is expected to enhance cybersecurity measures across popular [smart devices](https://www.sentinelone.com/blog/bringing-iot-out-of-the-shadows/) used in homes, [schools](https://www.sentinelone.com/blog/cyber-risks-in-the-education-sector-why-cybersecurity-needs-to-be-top-of-the-class/), offices, and more. The program is a collaborative one involving voluntary industry participation, oversight from the FCC, and stringent cyber standards set by NIST.

> Today, the Biden-Harris Administration is launching the U.S. Cyber Trust Mark – a cybersecurity certification and labeling program that will help Americans more easily choose smart devices that are safer and less vulnerable to cyberattacks. [pic.twitter.com/sBzUImz5TK](https://t.co/sBzUImz5TK)
>
> — The White House (@WhiteHouse) [July 18, 2023](https://twitter.com/WhiteHouse/status/1681296022201352193?ref_src=twsrc%5Etfw)

The U.S. Cyber Trust Mark enables consumers to identify which internet and Bluetooth-connected devices are [cybersecure](https://www.sentinelone.com/blog/hiding-in-plain-sight-the-iot-security-headache-and-how-to-fix-it/), including common items like fitness trackers, baby monitors, home security systems, and smart appliances. Suppliers that meet the program’s security requirements will bear a “Cyber Trust” label as early as next year. So far, participants include Amazon, Best Buy, Google, LG Electronics USA, Logitech, and Samsung.

Use of Internet of Things (IoT) devices has soared within the past decade. In 2023, there are an [estimated](https://www.statista.com/statistics/1183457/iot-connected-devices-worldwide/) 15 billion internet-connected devices in use globally, with that number expected to explode up to 29 billion by 2030. This widespread adoption makes IoT devices a lucrative target for cyberattackers. Seen as vulnerable entry points into private networks, IoT devices entice attackers to exploit, disrupt, or compromise systems and privacy.

FCC officials say that the mark will give consumers peace of mind and help them make more informed purchases. Additionally, program-approved devices will include QR codes allowing users to easily access any updates in applicable security information. The new program from the White House follows similar cybersafety labeling initiatives such as Singapore’s [SG Cyber Safe Programme](https://www.csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme#:~:text=The%20SG%20Cyber%20Safe%20Programme,and%20risk%2Dlevel%20will%20vary.) and the [Cyber Essentials](https://www.ncsc.gov.uk/cyberessentials/overview) certification and trademark program from the U.K.’s National Cyber Security Center.

## The Bad | Design Flaw In Google Cloud Increases Chances of Supply Chain Attacks

Security researchers this week [discovered](https://orca.security/resources/blog/bad-build-google-cloud-build-potential-supply-chain-attack-vulnerability/) a critical design flaw in the Google Cloud Build service that could allow attackers to escalate privileges and tamper with production environments. Dubbed ‘Bad.Build’, the flaw gives attackers nearly full, unauthorized access to Google’s Artifact Registry code repositories.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/bad-build-2.jpg)

With this kind of access, attackers would be able to impersonate the account’s continuous integration and delivery (CI/CD) service and run API calls. After [taking control](https://www.sentinelone.com/cybersecurity-101/the-ultimate-guide-to-preventing-account-takeover-attacks/) over the application images, attackers could then inject malicious code, poisoning customer’s environments with malicious applications and opening them up for potential [supply chain attacks](https://www.sentinelone.com/cybersecurity-101/what-is-supply-chain-attack/).

In their report, researchers warned that the impact of this flaw could be diverse as it applies to any organization using the registry as their main or secondary image repository. Disruption of this could, in turn, spread malware to a wider pool of users or lead to [DoS attacks](https://www.sentinelone.com/cybersecurity-101/what-is-denial-of-service-dos/) and [data theft](https://www.sentinelone.com/cybersecurity-101/what-is-a-data-breach/).

The Google Security Team has since [revoked](https://cloud.google.com/build/docs/security-bulletins#gcp-2023-013) the `logging.privateLogEntries.list` permission from the default Cloud Build Service Account. However, the researchers claim that is a partial fix that does not address the flaw in the Artifact Registry and continues to leave users at risk of privilege escalation abuse and possible supply chain attacks. They recommend that users apply the principle of least privilege (PoLP) and implement [cloud-centric security measures](https://www.sentinelone.com/blog/are-you-making-one-of-these-8-cloud-security-mistakes/) capable of [detecting and responding](https://www.sentinelone.com/resources/sentinelone-cloud-workload-security-autonomous-runtime-detection/) to any identified anomalies in the behavior of the default Google Cloud Build service account.

## The Ugly | Security Researchers Link JumpCloud Attack to North Korean State-Backed Threat Actor

Following a state-backed breach of Colorado-based software firm, JumpCloud, SentinelLabs researchers [published](https://www.sentinelone.com/labs/jumpcloud-intrusion-attacker-infrastructure-links-compromise-to-north-korean-apt-activity/) findings linking the attack to a North Korean APT. The incident was first [discovered](https://jumpcloud.com/blog/security-update-incident-details) earlier this month, after the company’s systems were targeted in a spear phishing attack. After discovery, JumpCloud forced a rotation of all admin API keys and notified customers to generate new keys. The company has since rebuilt the compromised infrastructure and shared [IoCs](https://jumpcloud.com/support/july-2023-iocs) with the community.

Review of the IoCs led SentinelLabs to associate the cluster of threat activity to a DPRK-sponsored APT who have been observed leveraging a supply chain targeting approach in [previous campaigns](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/). SentinelLabs mapped out the threat actor’s infrastructure to show the links between details of the intrusion to the underlying patterns, comprising domains and IP addresses, noted in similar campaigns. After correlating specific domains recently [shared](https://github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/) by GitHub to forensic analysis from JumpCloud’s ongoing investigation, SentinelLabs found clear links to NPM and ‘package’ themed infrastructure characteristic of other DPRK...