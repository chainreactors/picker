---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 28
url: https://buaq.net/go-172085.html
source: unSafe.sh - 不安全
date: 2023-07-15
fetch_date: 2025-10-04T11:51:23.196950
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 28

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

![](https://8aqnet.cdn.bcebos.com/8b166bfee23b1ce2a0804ae496c54998.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 28

The Good | Tougher Times Ahead for Play Store MalwareWith so many personal devices now hopping on
*2023-7-14 21:0:20
Author: [www.sentinelone.com(查看原文)](/jump-172085.htm)
阅读量:19
收藏*

---

## The Good | Tougher Times Ahead for Play Store Malware

With so many personal devices now hopping on and off company networks, the risks from [mobile malware](https://www.sentinelone.com/resources/defending-against-the-mobile-threat-landscape/) are always a concern. Google has had more than its fair share of problems with malicious apps on its Play store, but this week new rules for developer accounts aim to curb the problem.

Although new app submissions are vetted before being allowed on the app store, crafty developers typically circumvent these checks by initially uploading a benign version of the app. After approval, they issue an update containing the malicious code. If users are lucky, the malicious app is [discovered](https://www.sentinelone.com/blog/feature-spotlight-integrated-mobile-threat-detection-with-singularity-mobile-and-microsoft-intune/), reported, and the developer banned from the store. Up till now, that has never presented much of a problem, as the malicious developers return by creating a new account and repeating the cycle.

In an effort to combat this, Google will begin requiring all new developer accounts to provide a valid [D-U-N-S](https://www.dnb.co.uk/duns-number.html) number,  a unique nine-digit identifier for businesses, from August 31st. Acquiring a valid D-U-N-S number requires passing various proof-of-identity and business checks and that will make it difficult, expensive and time-consuming for fraudsters to complete.

![DUNS required for Google play store](https://www.sentinelone.com/wp-content/uploads/2023/07/unhappy-1.jpg)

Additionally, the Play store will require apps to display the developer’s business address, website URL and phone number in an effort to improve transparency and limit fraud.

It remains to be seen how effective these moves will be, or whether the extra identification requirements will serve to discourage legitimate independent developers from distributing on Google Play, but if it helps to reduce [malware](https://www.sentinelone.com/cybersecurity-101/what-is-malware-everything-you-need-to-know/) on Android devices, it will certainly be welcomed by IT and security teams.

## The Bad | Cloud Credentials Stealer Targets Azure and Google

A malicious actor previously targeting AWS accounts for compromise has now turned to stealing credentials for Azure and Google Cloud Platform (GCP) services, it was [revealed](https://s1.ai/cloudcreds) this week.

Updated versions of known malware scripts now gather credentials from AWS, Azure, Google Cloud Platform, Censys, Docker, Filezilla, Git, Grafana, Kubernetes, Linux, Ngrok, PostgreSQL, Redis, S3QL, and SMB. Successfully harvested credentials are then exfiltrated to a remote server under the threat actor’s control.

![Newly implemented get_azure function in g.aws.sh](https://www.sentinelone.com/wp-content/uploads/2023/07/Cloud_Credentials_Stealer_1.jpg)

New functionality targets Azure and Google

The campaign has been linked to notorious crime group TeamTNT, a threat group known to primarily target cloud and containerized environments with cryptocurrency miners. However, as researchers at [SentinelLabs](https://s1.ai/cloudcreds) pointed out, attribution remains challenging with script-based tools as they can be readily adapted by anyone for their own use.

The attack scripts target public-facing Docker instances and aim to deploy a worm-like propagation module. They also contain functionality for extensive system and environmental profiling. Post-exploitation activity involves collecting details from the infected host and using Bash to download the curl binary from the attacker’s server. This is notable because attacks against minimal systems like containers are often limited by the absence of common [living off the land](https://www.sentinelone.com/blog/how-do-attackers-use-lolbins-in-fileless-attacks/) tools like curl.

Up to eight incremental versions of the credential harvesting scripts have been observed in the last two months, indicating an actively evolving threat. Based on this activity, researchers believe that the actor is likely preparing for larger scale campaigns.

## The Ugly | Office 365 Intrusions Compounded by Lack of Visibility

A China-based threat actor has breached email accounts of dozens of organizations worldwide, including U.S. and Western European government agencies, it was revealed this week.

The campaign, which is thought to have begun in mid-May, was reported to Microsoft by the U.S. government after the discovery of unauthorized access to Microsoft cloud-based email services. According to [reports](https://edition.cnn.com/2023/07/12/politics/china-based-hackers-us-government-email-intl-hnk/index.html), the State Department was the first of a number of government agencies to detect a compromise of its Microsoft Office 365 system. The Department of Commerce and the House of Representatives were also among those targeted.

> A sophisticated China-based hacking campaign has targeted U.S. government agencies and organizations, compromising email accounts via Microsoft Outlook Web Access in Exchange Online (OWA) & Outlook.
>
> Read: <https://t.co/390mnDokqJ>[#cybersecurity](https://twitter.com/hashtag/cybersecurity?src=hash&ref_src=twsrc%5Etfw) [#hacking](https://twitter.com/hashtag/hacking?src=hash&ref_src=twsrc%5Etfw) [#malware](https://twitter.com/hashtag/malware?src=hash&ref_src=twsrc%5Etfw)
>
> — The Hacker News (@TheHackersNews) [July 13, 2023](https://twitter.com/TheHackersNews/status/1679376402469072896?ref_src=twsrc%5Etfw)

Microsoft’s own investigation revealed that a China-based [threat actor](https://www.sentinelone.com/resources/threat-actor-basics-understanding-the-5-main-threat-types/) used forged authentication tokens and an acquired Microsoft account (MSA) consumer signing key to access user email. It is unclear how the threat actor acquired the Microsoft key or whether there is an exploitable flaw in Microsoft’s token validation system.

The company says it has blocked all tokens signed with the stolen key and worked to improve its “key management systems” since the theft occurred. Microsoft says it has contacted all targeted or compromised organizations directly with information to help them investigate and respond.

However, the company is facing criticism because access to forensic logs for users of its Office 365 services requires extra licensing. U.S. Senator Ron Wyden [reportedly](https://english.alarabiya.net/business/technology/2023/07/14/Microsoft-faces-criticism-over-email-hack-experts-call-for-free-forensic-data-access) said that Microsoft should offer all its customers full forensic capabilities, saying that “charging people for premium features necessary to not get hacked is like selling a car and then charging extra for seatbelts and airbags”.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-28-5/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)