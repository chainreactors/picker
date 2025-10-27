---
title: Abraham's Ax Likely Linked to Moses Staff
url: https://www.secureworks.com/blog/abrahams-ax-likely-linked-to-moses-staff
source: Secureworks Blog
date: 2023-01-27
fetch_date: 2025-10-04T05:00:29.096114
---

# Abraham's Ax Likely Linked to Moses Staff

[Skip to Main Content](#main-content)[Skip to Footer](#cmp-footer-a1fbb96a)

[Sophos completes Secureworks acquisition](https://www.sophos.com/en-us/press/press-releases/2025/02/sophos-completes-secureworks-acquisition)

* [Experiencing a Breach?](https://www.sophos.com/en-us/products/incident-response-services/emergency-response)
* Contact Us
* Support
* [Blog](/blog)
* English

[![logo](/-/media/images/logos/logo_new.svg?iar=0&hash=61254867B6545667A8E17DD1352849AF)](/ "Secureworks")

* Platform
* Services
* Solutions
* About
* Partners
* Resources

[Request Demo](/contact/request-demo-xdr)

Research & Intelligence

# Abraham's Ax Likely Linked to Moses Staff

Both personas are likely operated by the Iranian COBALT SAPLING threat group.

![man and keyboard](/-/media/images/thumbnails/blog/people-man-and-computer-06.jpg?h=722&iar=0&w=1284&hash=4F5BAB56885A7C4364FB3D0D0B9D092E?io=transform:fit,width:4568,height:2568)

[Counter Threat Unit Research Team](/author/Counter-Threat-Unit-Research-Team)

January 26, 2023

Secureworks® Counter Threat Unit™ (CTU) researchers investigated similarities between the Moses Staff hacktivist group persona that emerged in September 2021 and the Abraham's Ax persona that emerged in November 2022. The analysis revealed several commonalities across the iconography, videography, and leak sites used by the groups, suggesting they are likely operated by the same entity. CTU™ analysis indicates that Abraham's Ax is another hacktivist group persona operated by the Iranian [COBALT SAPLING](https://www.secureworks.com/research/threat-profiles/cobalt-sapling) threat group.

Abraham's Ax announced their existence and mission through social media channels such as Twitter posts on November 8, 2022. The group's iconography is reminiscent of Moses Staff (see Figure 1). The Moses Staff logo shows an arm extended from a sleeve holding a staff with a clenched fist. Abraham's Ax shows a clenched fist holding an axe from a different perspective. Both illustrations use a similar style.

![](/-/media/images/insights/blog/2023/abrahams-ax/figure-01.png)

*Figure 1. Comparison of Moses Staff and Abraham's Ax logos. (Source: Secureworks)*

Abraham's Ax and Moses Staff use a WordPress blog as the basis for their leak sites. Although the overall aesthetics are different, there are clear connections in their operations. Both sites offer multiple languages. Moses Staff is available in Hebrew and English, while Abraham's Ax is available in Hebrew, Farsi, and English. Both sites provide versions available via Tor websites, although the Abraham's Ax site appeared to be under construction at the time of analysis. Both use domains registered with EgenSajt . se (see Table 1).

| Domain | Creation Date |
| --- | --- |
| Moses-staff . se | 2021-09-09 |
| abrahams-ax . nu | 2022-10-14 |
| abrahams-ax . se | 2022-11-08 |

*Table 1. Domains registered by Moses Staff and Abraham's Ax.*

Although the threat actors registered .nu and .se domains that use the abrahams-ax name, the group appears to use the .nu version in promotional material (see Figure 2). The abrahams-ax . nu domain was registered approximately three weeks before the group emerged publicly.

![](/-/media/images/insights/blog/2023/abrahams-ax/figure-02.png)

*Figure 2. Screenshot from video segment produced by Abraham's Ax. (Source: Secureworks)*

CTU analysis of the hosting infrastructure for the Moses Staff and Abraham's Ax leak sites revealed that at early points in their lifecycles, both sites were hosted in the same subnet, nearly adjacent to each other (see Figure 3). This is highly unlikely to occur by coincidence and strongly indicates that the same entity chose to host the two sites in near contiguous IP address space.

![](/-/media/images/insights/blog/2023/abrahams-ax/figure-03.png)

*Figure 3. Infrastructure links between Moses Staff and Abraham's Ax. (Source: Secureworks)*

Moses Staff claims to be anti-Israeli and pro-Palestinian and encourages leak site visitors to take part in "exposing the crimes of the Zionists in occupied Palestine." Moses Staff posted 16 "activities" to their site as of December 2. The leaked information is predominantly data sets stolen from Israeli companies but also includes compilations of personal information on individuals affiliated with Israel's signals intelligence [Unit 8200](https://en.wikipedia.org/wiki/Unit_8200). Some of the intrusions have been confirmed, although it is likely that Moses Staff embellished the nature and extent of the compromises. The threat actors have [reportedly](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/) used the custom PyDCrypt loader and DCSrv cryptographic wiper. DCSrv encrypts data using the open-source DiskCryptor library and installs a custom bootloader message. Although the wiper is styled as ransomware, the threat actors do not make a serious attempt to extort a ransom payment. The attacks appear to be politically motivated and focused on disruption and intimidation. The [StrifeWater](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations) remote access trojan (RAT) (also known as brokerhost.exe) has also been linked to the group based on technical overlaps between intrusions, such as the use of the same customized ASPX web shells. An auxiliary tool named DriveGuard has been [deployed](https://www.fortinet.com/blog/threat-research/guard-your-drive-from-driveguard) alongside StrifeWater to monitor its execution. Malware artifacts indicate that COBALT SAPLING has been operating since at least November 2020 (see Figure 4), even though the Moses Staff persona did not emerge until September 2021.

![](/-/media/images/insights/blog/2023/abrahams-ax/figure-04.png)

*Figure 4. Early StrifeWater RAT sample information indicating operations since at least November 2020. (Source: Secureworks)*

Like Moses Staff, Abraham's Ax uses a biblical figure as the basis of their persona and includes religious quotes throughout their site. However, Abraham's Ax states they are operating on behalf of the Hezbollah Ummah. Hezbollah is a Lebanese Shia Islamist political party and militant group that is backed by Iran. Ummah refers to a Muslim community. As of this publication, there is no evidence to suggest that Abraham's Ax is linked to Hezbollah. Rather than attacking Israel directly, Abraham's Ax attacks government ministries in Saudi Arabia. They published sample data allegedly stolen from attacks on the Ministry of the Interior, along with a video that purportedly presents intercepted phone conversations between Saudi Arabian government ministers. The group may be attacking Saudi Arabia in response to Saudi Arabia's leadership role in improving relationships between Israel and Arab nations. In June 2022, [media reports](https://www.theguardian.com/world/2022/jun/27/israel-and-saudi-arabia-in-talks-over-joint-defence-against-iran) described secret talks regarding potential air defense collaborations, which Iran perceived as a significant threat to its interests in the region. Progress on normalization of relations between Saudi Arabia and Israel is fragile, and Iran may see these attacks as a way to discourage those efforts.

Moses Staff and Abraham's Ax have both produced and released videos as part of their operations. The videos often depict Hollywood-style hacking involving satellites, CCTV, 3D building models, and fast scrolling through documents allegedly stolen as part of their operations. Some videos depict multiple mobile phones combined with audio playback to suggest that mobile phone calls of senior government officials were intercepted. The video files released by the two groups show clear repetition and evolution of visual themes. The comparison of video screen captures in Figure 5 shows strong similarities between the groups. The Abraham's Ax videos use several of the same stock video elements used by Moses Staff but incl...