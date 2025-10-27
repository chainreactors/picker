---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 11
url: https://buaq.net/go-153953.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:30.113600
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 11

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

![](https://8aqnet.cdn.bcebos.com/8df5912ab7e4787e174dde7779acc83b.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 11

The GoodGood news this week as “one of the darkweb’s largest cryptocurrency laundromats”, unlicens
*2023-3-17 21:0:10
Author: [www.sentinelone.com(查看原文)](/jump-153953.htm)
阅读量:21
收藏*

---

## The Good

Good news this week as “one of the darkweb’s largest cryptocurrency laundromats”, unlicensed crypto platform ChipMixer, was seized and shuttered in a [joint operation](https://www.justice.gov/opa/pr/justice-department-investigation-leads-takedown-darknet-cryptocurrency-mixer-processed-over-3) involving U.S., Swiss, Polish and German law enforcement agencies.

ChipMixer, which began operating in 2017, specialized in obfuscating blockchain transactions to hide the trail of virtual currency assets. Known as “mixers” or “tumblers”, such sites attempt to disguise the true source and destinations of exchanges by breaking down and mixing cryptocurrency tokens from different transactions.

It is alleged that the service had been used to launder over $3 billion in [Bitcoin](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/), with a large percentage of that being proceeds of ransomware payments, thefts, [darknet](https://www.sentinelone.com/blog/20-years-in-the-dark-the-dark-web-turns-twenty-what-does-this-mean-for-a-ciso/) [marketplace payments](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/) and nation-state criminal activity. Notorious North Korean threat actor and [cryptocurrency thief Lazarus](https://www.sentinelone.com/blog/lazarus-operation-interception-targets-macos-users-dreaming-of-jobs-in-crypto/) is believed to have been among its clients along with Russia’s General Staff Main Intelligence Directorate (GRU), *aka* [APT28](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/), which is said to have used ChipMixer to hide purchases of hacking infrastructure.

![chipmixer.io](https://www.sentinelone.com/wp-content/uploads/2023/03/Screenshot-2023-03-17-at-10.44.27-AM.jpg)

Along with seizing the site, authorities also bagged around $46 million worth of cryptocurrency and charged a 49-year old Vietnamese national, Minh Quoc Nguyen, with operating an unlicensed money transmitting business, money laundering and identity theft.

Nguyen, whose whereabouts remain unknown, openly flouted financial regulations. The DoJ’s indictment says that he publicly derided efforts to curtail money laundering and registered domain names and hosting services using stolen identities, pseudonyms and anonymous email services. If caught and convicted, Nguyen faces up to 40 years jail time.

ChipMixer joins BestMixer, BitcoinFog and Helix in being shut down by U.S. and European law enforcement agencies for money laundering via cryptocurrency.

## The Bad

It was revealed this week that a U.S. Federal Agency had been breached by multiple threat actors, including a nation-state APT, through a software bug that had been known since 2019. The breaches may have begun as early as August 2021 and occurred as late as November 2022.

According to an [advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-074a) from CISA published on Wednesday, threat actors exploited CVE-2019-18935, a .NET deserialization vulnerability in Progress Telerik user interface located in the agency’s Microsoft IIS (Internet Information Services) web server to gain remote code execution.

![Telerik UI](https://www.sentinelone.com/wp-content/uploads/2023/03/Screenshot-2023-03-17-at-11.40.14-AM.jpg)

Source: Telerik

CISA says it observed threat actors including known cybercrime gang XE Group uploading malicious DLLs, some disguised as PNG image files to the `C:\Windows\Temp\` directory. These were then executed via the legitimate `w3wp.exe` process running on the compromised IIS servers. The attackers appear to have used timestomping as part of their evasion tactics, which involves changing the creation and modified dates on files to disguise their origin.

Much of the malware opened up reverse shells and allowed attackers interactive access to the compromised devices. ASPX [webshells](https://www.sentinelone.com/labs/wading-through-muddy-waters-recent-activity-of-an-iranian-state-sponsored-threat-actor/) were also deployed to enumerate drives, send, receive and delete files, and execute commands.

Interestingly, the Federal agency concerned had deployed an appropriate plugin to scan for the CVE-2019-18935 vulnerability but failed to detect it. CISA’s advisory says this is due to the Telerik UI software being installed in a file path that the scanner does not typically scan, a situation that may be common in other organizations as file paths for installed software can vary depending on the organization and installation method.

Organizations are advised to implement patch management solutions to ensure compliance with the latest security patches, and to update any instances of Telerik UI ASP.NET AJAX to the latest version. Security teams should review the detection and mitigations provided in the [advisory](https://www.cisa.gov/news-events/alerts/2023/03/15/threat-actors-exploited-progress-telerik-vulnerability-us-government-iis-server) for further information.

## The Ugly

A threat actor group with interests closely aligned to those of the Russian and Belarussian governments was revealed to have been conducting a wide range of hitherto unknown espionage campaigns against Western governments and institutions this week by [SentinelLabs researchers](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/).

Winter Vivern, *aka* UAC-0114, was first spotted back in 2021 but appeared to have gone dark soon after. New activity was observed by the Polish CBZC and Ukraine CERT at the end of January this year, but research published this week revealed a much wider set of campaigns that have targeted the Vatican, Indian government organizations, the Italian Ministry of Foreign Affairs as well as Polish and Ukrainian government agencies, among others. The campaigns have been ongoing through 2021 and 2022 to present but have remained unreported until now.

Some of the group’s latest tactics involve mimicking government domains, including government email login pages, to phish credentials and distribute malicious downloads.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/Winter_Vivern5.jpg)

Although the group is not thought to be particularly technical, the researchers say that Winter Vivern makes creative use of simple batch scripts using [PowerShell](https://www.sentinelone.com/cybersecurity-101/windows-powershell/). In some incidents, the threat actors utilized batch scripts disguised as virus scanners to download malware in the background while victims believed they were conducting a security scan.

The group also exploits application vulnerabilities to compromise specific targets. The SentinelLabs post says that in one incident, a malicious server hosted a login page for the Acunetix web application vulnerability scanner, which may have served as a supplementary resource to scan target networks and possibly compromise WordPress sites.

More information about the Winter Vivern APT including indicators of compromise can be found in the SentinelLabs report [here](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/).

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-11-4/
 如有侵权请联系:admin#unsafe.sh

© ...