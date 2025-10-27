---
title: Risky Biz News: SugarCRM zero-day used to compromise roughly 10% of all internet-accessible servers
url: https://riskybiznews.substack.com/p/risky-biz-news-sugarcrm-zero-day
source: Over Security - Cybersecurity news aggregator
date: 2023-01-12
fetch_date: 2025-10-04T03:41:31.670479
---

# Risky Biz News: SugarCRM zero-day used to compromise roughly 10% of all internet-accessible servers

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: SugarCRM zero-day used to compromise roughly 10% of all internet-accessible servers

### In other news: Windows 7 reaches end-of-support; smart ship management platform taken down after hack; Raspberry Robin botnet loses 30% of C2 servers in partial takedown.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jan 11, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

Almost 10% of all internet-accessible SugarCRM servers (*representing 291 of 3,066 servers, based on [Censys data](https://censys.io/tracking-a-sugarcrm-zero-day/)*) were hacked and compromised using a [zero-day exploit](https://seclists.org/fulldisclosure/2022/Dec/31) published online in late December.

SugarCRM describes the zero-day as an authentication bypass that allows threat actors to upload encoded images containing malicious PHP code on SugarCRM platforms.

Censys researchers say the final payload in many attacks appears to be a simple web shell that could be used to control compromised systems. According to an [open-source report](https://mastodon.social/%40ll%40infosec.exchange/109630615387494049), the zero-day appears to have been used to drop crypto-mining malware as well.

[![](https://substackcdn.com/image/fetch/$s_!vjoI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd92c4070-3801-40b5-bafa-9a26cad0988e_591x485.png)](https://substackcdn.com/image/fetch/%24s_%21vjoI%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/d92c4070-3801-40b5-bafa-9a26cad0988e_591x485.png)

SugarCRM released an [official patch](https://sugarclub.sugarcrm.com/explore/product-updates/b/sugar-sell-updates/posts/january-4-2023-critical-security-hotfix) a week after public disclosure. The company said that all users who run on-premise servers of its SugarCRM Sell, Serve, Enterprise, Professional, and Ultimate services should apply the update to avoid future attacks.

The company says it has [hired a forensics firm](https://sugarclub.sugarcrm.com/engage/b/sugar-news/posts/jan-5-2023-security-vulnerability-update) to investigate the one-week time window during which its cloud platform was exposed to possible attacks.

No CVE has been assigned to this issue yet.

### **Breaches and hacks**

**SF BART ransomware:** The San Francisco Bay Area Rapid Transit (BART) is investigating an intrusion of its IT network after the Vice Society ransomware gang claimed to have compromised the agency via a blog post on their dark web leak site. The agency's spokesperson told *[The Record](https://therecord.media/san-francisco-bart-investigating-ransomware-attack/)* that "no BART services or internal business systems have been impacted," but they are still looking into claims that data was stolen.

**OxShag leak:** A dating website named OxShag, which was created by Oxford University students for their fellows, has caused an accidental data leak by exposing everyone's names and university email addresses. According to *[The Times](https://www.thetimes.co.uk/article/oxford-dating-website-posts-staff-and-students-contact-details-f5zgznrxv)*, OxShag appears to have listed the university's entire email directory for both students and administrators alike. The website was shut down following student complaints.

**DNV ShipManager attack:** Norweigian company DNV says it [had to shut down](https://www.dnv.com/news/cyber-attack-on-shipmanager-a-dnv-software-237552) its ShipManager smart ship management platform in the aftermath of a cyberattack that took place last Saturday. DNV said ShipManager would work in offline mode while they investigate the incident together with the Norwegian police. The [ShipManager platform](https://www.dnv.com/services/marine-fleet-management-software-and-ship-management-systems-shipmanager-114260), which allows maritime companies to manage ship fleets, their crew, maintenance, procurement, cargo, and other analytics, is currently used by more than 300 maritime companies and installed on more than 7,000 vessels.

### **General tech and privacy**

**Cryptome suspension:**Twitter has [permanently suspended](https://mastodon.social/%40Cryptome/109659473692136429) the account of Cryptome.org, a leak site known for publishing leaks of sensitive documents from across the world. The last files published on the site before the suspension are documents claiming to contain Donald and Melania Trump's tax returns.

**Windows 7 end of extended support:** As of [January 10, 2023](https://support.microsoft.com/en-us/office/windows-7-end-of-support-and-office-78f20fab-b57b-44d7-8368-06a8493f3cb9), the Microsoft Windows 7 and Windows 8.1 operating systems have formally reached their end of extended support. Both operating systems previously reached their end of life for home users in January 2020, after which point only selected corporate customers were eligible for additional security updates under a commercial plan. These updates will stop this week. Other Microsoft products that also reached their end of support this Tuesday also include Visual Studio 2012 and the Windows RT and Windows Server 2008 operating systems, among [many others](https://learn.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2023).

[![](https://substackcdn.com/image/fetch/$s_!ZPue!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a7ca639-e939-432e-8a38-cbf58f9f99b5_879x473.png)](https://substackcdn.com/image/fetch/%24s_%21ZPue%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/0a7ca639-e939-432e-8a38-cbf58f9f99b5_879x473.png)

### **Government, politics, and policy**

**DDoS attacks on Serbian govt:** The Serbian government says it mitigated a [two-day-long DDOS attack](https://www.srbija.gov.rs/vest/676312/masovni-sajber-napadi-na-sajt-i-it-infrastrukturu-mup-a.php) that hit several of its official websites and IT infrastructure. No group has yet to claim the attacks.

**Malta drops Huawei CCTV project:** The Maltese government [will abandon](https://www.maltatoday.com.mt/news/national/120627/state_ditches_controversial_huawei_cctv#.Y71ly8TMK8Z) its joint project with Huawei to implement a facial recognition-based CCTV system across some of its urban areas. Named Safe City Malta, the project was [announced in 2018](https://timesofmalta.com/articles/view/budget-facial-recognition-cctv-in-paceville-and-then-marsa.692306) and was initially deployed in 2019 in two cities—Paceville and Marsa. After years of criticism from privacy advocates, earlier this week, the Maltese government chose not to extend Huawei's contract and let the project lapse.

**DNS4EU:** Czech cybersecurity company [Whalebone](https://www.whalebone.io/post/press-release-dns4eu) has been selected to b...