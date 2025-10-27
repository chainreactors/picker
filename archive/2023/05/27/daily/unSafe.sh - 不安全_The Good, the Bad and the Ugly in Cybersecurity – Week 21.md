---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 21
url: https://buaq.net/go-165932.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:13.003852
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 21

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

![](https://8aqnet.cdn.bcebos.com/05ec8c3c8bb702fe79ec75c95462b4fa.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 21

Private Sector Offensive Actor | FinFisher Execs Charged for Selling Spyware to TurkeyProsecutors
*2023-5-26 21:0:16
Author: [www.sentinelone.com(查看原文)](/jump-165932.htm)
阅读量:25
收藏*

---

## Private Sector Offensive Actor | FinFisher Execs Charged for Selling Spyware to Turkey

Prosecutors in Germany this week indicted four executives of spyware firm FinFisher for selling the [FinSpy](https://www.sentinelone.com/blog/how-to-catch-a-spy-detecting-finfisher-spyware-on-macos/) hacking tool to Turkey’s intelligence agency.

FinFisher produces cross-platform espionage tools for what it describes as “tactical intelligence gathering”, “strategic intelligence gathering”, and “deployment methods and exploitation”. The company’s marketing material states that it only partners with “Law Enforcement and Intelligence Agencies” and has a “worldwide presence”.

However, in 2020, Amnesty International [warned](https://www.sentinelone.com/blog/how-to-catch-a-spy-detecting-finfisher-spyware-on-macos/) that FinSpy was being used in campaigns targeting human rights activists, journalists and dissidents in Egypt, Ethiopia, and the United Arab Emirates (UAE) among others.

Now, German prosecutors say that FinFisher evaded export controls on its spyware in 2015 and sold it to a Bulgarian company being used as a front for Turkey’s intelligence agency. There are suggestions that the spyware was used to target opponents of President Erdoğan in 2017.

> The public prosecutor charged the German hacking company FinFisher. Directors of four former companies are accused of selling surveillance technology made in Germany to the Turkish MIT without authorization. This is a result of our our criminal complaint. <https://t.co/YILIPIbEPf>
>
> — Andre Meister (@andre\_meister) [May 22, 2023](https://twitter.com/andre_meister/status/1660613463335477250?ref_src=twsrc%5Etfw)

The prosecutors allege that four FinFisher executives, who were only identified by single initials, signed a deal with the Turkish government for the spyware along with technical support and training. The deal was thought to be worth around $5 million.

FinFisher has since ceased trading, but a spokesperson for the European Center for Constitutional and Human Rights [warned](https://netzpolitik.org/2023/unsere-strafanzeige-staatsanwaltschaft-klagt-manager-von-finfisher-an/):

*“So far, companies like FinFisher have been able to export almost unhindered worldwide despite European export regulations. Today’s indictment is long overdue and will hopefully lead to the conviction of the responsible managing directors in the near future. But beyond that, the EU and its member states must take much more decisive action against the massive misuse of surveillance technology.”*

## Ransomware | Insider Threat As Employee Tried to Siphon Off Ransom Payment

The threat of [ransomware](https://www.sentinelone.com/anthology) has loomed large over the last few years, with threat actors aggressively exploiting any weaknesses they can find in organizations’ defenses and constantly innovating in response to detection and prevention strategies. But one attack vector few are looking for is an insider threat that positions themselves between the business and the ransomware gang in an attempt to steal the ransom payment.

A [court](https://serocu.police.uk/man-convicted-of-blackmail-and-other-offences/) in the UK this week found Ashley Liles, formerly an IT security analyst at Oxford Biomedica, guilty of doing just that after his employer was hit with a ransomware attack in February 2018. Liles was among those responsible for investigating the attack, but surreptitiously began hacking a board member’s emails as they negotiated with the attackers.

Liles altered an email from the attackers to insert his own [bitcoin](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/) payment details, then created an email address similar to the attacker’s and began sending pressurizing emails to his employers.

![ashley liles](https://www.sentinelone.com/wp-content/uploads/2023/05/ashley-liles-scaled.jpg)

Had a payment been made, it’s fairly certain that Liles would have been rapidly exposed, as the original attackers would have soon made it clear they had not received the funds. However, as the company chose not to pay the ransom, Liles received no payment and may have thought he had escaped justice.

Unfortunately for him, the unauthorized access to the board member’s emails was noticed and tracked down to Liles’ home address. Police later seized his devices and recovered incriminating evidence despite his attempts to wipe the data. Liles, now aged 28, pleaded guilty in court and will be sentenced in July.

## Volt Typhoon | Chinese-sponsored Threat Actor Targets US Critical Infrastructure

CISA, the FBI and other partners have this week [warned](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF) that a Chinese-backed threat actor has been targeting U.S. critical infrastructure organizations since 2021 in activity that appears designed to aid China in any potential conflict between the two superpowers. Among the targets were organizations on Guam, a vital part of America’s Asia-Pacific defense strategy and home to Anderson Air Base and Naval Base Guam.

![Andersen Air Force Base Guam](https://www.sentinelone.com/wp-content/uploads/2023/05/Screenshot-2023-05-26-at-11.57.48-AM.jpg)

[Source: Andersen Air Force](https://www.andersen.af.mil/Portals/43/36th-Wing-Overview-Infographic-20220413_1.pdf)

The threat actor, labeled “Volt Typhoon”, leverages compromised or vulnerable small office/home office (SOHO) devices to gain initial access to organization’s networks. Observed TTPs include exploiting CVE-2021-40539 and CVE-2021-27860 and attacking devices such as ASUS, Cisco RV, Draytek Vigor, FatPipe IPVPN/MPVPN/WARP, Fortinet Fortigate, Netgear Prosafe, and Zyxel USG.

Having once gained a foothold, the threat actor relies heavily on Windows [LOLBins](https://www.sentinelone.com/blog/how-do-attackers-use-lolbins-in-fileless-attacks/) – legitimate programs already installed on host computers – to conduct its malicious activities and evade discovery.

CISA’s advisory noted that the actor makes use of [WMI/WMIC](https://www.sentinelone.com/labs/labscon-replay-blasting-event-driven-cornucopia-wmi-based-user-space-attacks-blind-siems-and-edrs/) to stealthily gather information about local drives, as WMI logging is not enabled by default. [PowerShell](https://www.sentinelone.com/cybersecurity-101/windows-powershell/) and [certutil](https://www.sentinelone.com/blog/malware-living-off-land-with-certutil/) were among a long list of [living off the land tools](https://www.sentinelone.com/labs/living-off-windows-land-a-new-native-file-downldr/) used for discovery, lateral movement and collection:

* certutil
* dnscmd
* ldifde
* makecab
* net user/group/use
* netsh
* nltest
* ntdsutil
* PowerShell
* req query/save
* systeminfo
* tasklist
* wevtutil
* wmic
* xcopy

In addition, “hacktools” such as FRP (Fast Reverse Proxy), Impacket, and [Mimikatz](https://www.sentinelone.com/cybersecurity-101/mimikatz/) as well as remote administration tools were also characteristic of the attacks.

Researchers believe that the primary objective of Volt Typhoon is to enable China to disrupt critical communications infrastructure during any future crisis, and organizations are on alert that the same stealthy tactics seen in this campaign could be used against organiz...