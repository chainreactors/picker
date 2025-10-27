---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 6
url: https://buaq.net/go-148879.html
source: unSafe.sh - 不安全
date: 2023-02-11
fetch_date: 2025-10-04T06:19:06.348151
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 6

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

![](https://8aqnet.cdn.bcebos.com/672d1d016e3cebed4716341984ef84d7.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 6

The GoodSeven individuals were sanctioned this week for their involvement with the notorious Trick
*2023-2-10 22:0:6
Author: [www.sentinelone.com(查看原文)](/jump-148879.htm)
阅读量:30
收藏*

---

## The Good

Seven individuals were sanctioned this week for their involvement with the notorious [TrickBot](https://www.sentinelone.com/labs/inside-a-trickbot-cobalt-strike-attack-server/) cyber gang. Authorities have [sanctioned](https://home.treasury.gov/news/press-releases/jy1256) a formal block on all U.S.-based property and funds belonging to Vitaly Kovalev, Maksim Mikhailov, Valentin Karyagin, Mikhail Iskritskiy, Dmitry Pleshevskiy, Ivan Vakhromeyev, and Valery Sedletski. Of the seven, one has been identified as a senior figure within the gang while others were involved in ransomware development, money-laundering, and day-to-day administration.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/23-02-10-00-00-21-516_deco-scaled.jpg)

TrickBot malware transitioned from [banking trojan](https://www.sentinelone.com/blog/trickbot-technical-analysis-banking-trojan-malware/) to a full-blown malware designed to break into corporate networks in advanced [ransomware operations](https://www.sentinelone.com/labs/deep-dive-into-trickbot-executor-module-mexec-hidden-anchor-bot-nexus-operations/). The Russian-based cybercrime gang is also tied to the development of multiple malware strains such as BumbleBee, [BazarBackdoor, and Anchor](https://www.sentinelone.com/labs/anchor-project-for-trickbot-adds-icmp/). TrickBot is no stranger to news headlines – in just the last three years, the malware was leveraged in a major attack on the [Costa Rican government](https://www.sentinelone.com/blog/endpoint-identity-and-cloud-top-cyber-attacks-of-2022-so-far/) and [targeted](https://www.cisa.gov/uscert/ncas/alerts/aa20-302a) large hospitals and healthcare services across Ireland and the U.S., particularly during the COVID-19 pandemic.

The joint sanction effort by authorities in the U.S. and United Kingdom follows a significant leak last year of Conti and TrickBot internal conversations, source code, and personally identifiable information. The [‘ContiLeaks’](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-10-3/) resulted in a rare look into the operational infrastructures and identities of key members across both groups, with Conti having acquired TrickBot earlier last year.

Though Conti has disbanded after the leaking of their source code, individuals from the group have likely all transferred to other ransomware gangs, or started new operations. This fact alone makes collaborative efforts to impose sanctions on cybercriminals that much more necessary. Deployment of sanctions make it much harder for threat actors to launder their money, cutting them off from their financial gains and leaving less room for them to operate in.

## The Bad

This week, SentinelLabs researchers [reported](https://www.sentinelone.com/labs/cl0p-ransomware-targets-linux-systems-with-flawed-encryption-decryptor-available/) on a new variant of Cl0p ransomware targeting Linux devices, noting its appearance as part of a larger trend amongst ransomware groups creating new variants of their respective strains.

Cl0p ransomware may have only just branched out into targeting Linux devices, widely used by enterprises as servers and cloud workload hosts, but the group itself has been around since 2019. They have been known to target critical infrastructure around the world but focus especially on large enterprises, financial institutions, and [schools](https://www.sentinelone.com/blog/cyber-risks-in-the-education-sector-why-cybersecurity-needs-to-be-top-of-the-class/). So far, the Linux variant has been seen targeting educational institutions, including a university in Columbia late December.

Despite the concerns this development raises, the report highlights a small silver lining. SentinelLabs researchers found a flaw in the Linux variant, enabling them to create a [decryptor tool](https://github.com/SentineLabs/Cl0p-ELF-Decryptor). Victims of the Linux variant can decrypt any encrypted data without having to pay the ransom. The report explains that unlike the Cl0p Windows ransomware variant, which uses asymmetric encryption and a private key only known to the attackers, the Linux variant uses a symmetric encryption algorithm with the key needed for decryption hardcoded into the malware itself. This makes it possible for analysts to reverse the encryption based on code found in the sample.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/GitHub_-_SentineLabs_Cl0p-ELF-Decryptor__Python3_script_which_decrypts_files_encrypted_by_flawed_Cl0p_ELF_variant_.png)

The discovery of a Linux variant of Cl0p ransomware demonstrates once again that ransomware groups will continue to seek new targets and methods to maximize their profits.  [Linux](https://www.sentinelone.com/blog/cybersecurity-weakest-link-linux-iot/), which is widely used in many enterprise environments, offers up a rich pool of potential victims in the eyes of threat actors. With more operations shifting towards cloud computing and virtual environments, there’s no doubt that Linux has become increasingly attractive to actors in search of easier targets and higher rewards. It is likely that the malware authors will fix the flaw in future iterations and organizations should take steps to protect themselves from ransomware.

## The Ugly

A wave of new ESXiArgs ransomware attacks was reported this week, encrypting extensive amounts of data on various servers across the US, Canada, and Central Europe. While ongoing investigations indicate that the servers were compromised by way of a two-year-old VMware Service Location Protocol (SLP) vulnerability tracked as [CVE-2021-21974](https://www.vmware.com/security/advisories/VMSA-2021-0002.html?irclickid=WCoWJ2WFTxyNWADxqgX86XkiUkA3o0Ww4XSQyE0&utm_source=affiliate&utm_medium=ONLINE_TRACKING_LINK_&utm_campaign=Online%20Tracking%20Link&utm_term=engine%3Aimpact%7Cpublisherid%3A123201%7Ccampaignid%3A11461&irpid=123201&irgwc=1), some victims are reporting that they still experienced breach and encryption even though SLP was disabled in their environments.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/23-02-10-00-00-08-909_deco-scaled.jpg)

Since the first wave of the ransomware campaign earlier this week, the ESXiArgs attacks have targeted over 3800 victims by encrypting the configuration files on vulnerable, unpatched VMware ESXi servers and rendering the virtual machines potentially unusable. Investigative findings so far show the ransomware encrypting *.vmdk, .vmx, .vmxf, .vmsd, .vmsn, .vswp, .vmss, .nvram*, and *.vmem* files on compromised servers. To date, CISA and the FBI have jointly released an advisory and recovery script for victims available on [GitHub](https://github.com/cisagov/ESXiArgs-Recover). The advisory encourages enterprises with affected servers to update to the latest version of ESXi, disable the SLP service, and remove any exposure of the ESXi hypervisor to the public internet.

Security [researchers](https://www.wiz.io/blog/ransomware-attacks-targeting-vmware-esxi-servers-everything-you-need-to-know) believe these attacks have been so rampant due to the sheer volume of vulnerable targets: At least 12% of all existing VMware ESXi servers remain unpatched against CVE-2021-21974, making them a vulnerable target to ESXiArgs ransomware. Highly-focused ransomwar...