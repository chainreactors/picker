---
title: Risky Biz News: Norwegian government hacked with MobileIron zero-day
url: https://riskybiznews.substack.com/p/risky-biz-news-norwegian-government
source: Over Security - Cybersecurity news aggregator
date: 2023-07-27
fetch_date: 2025-10-04T11:56:39.312879
---

# Risky Biz News: Norwegian government hacked with MobileIron zero-day

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Norwegian government hacked with MobileIron zero-day

### In other news: TETRA encrypted radio traffic can be decrypted; Apple patches another Triangulation zero-day; and Zenbleed vulnerability leaks passwords and encryption keys from AMD Zen CPUs.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jul 26, 2023

Share

***This newsletter is brought to you by application allow-listing software maker [Airlock Digital](https://www.airlockdigital.com/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/). On Apple Podcasts:***

A threat actor has exploited a MobileIron zero-day to breach twelve Norwegian government agencies, the country's security service [said](https://www.regjeringen.no/en/aktuelt/ministries-hit-by-cyber-attacks/id2990098/) on Tuesday.

The identity of the attacker, the dates of the intrusions, and the names of the compromised agencies have not been revealed.

Norwegian authorities say the zero-day targeted a piece of software named the [Ivanti Endpoint Manager Mobile](https://www.ivanti.com/resources/v/doc/ivi/2726/88684c72867a) (EPMM), previously known as MobileIron Core. The platform is used to manage mobile devices used by government employees and grant remote access to government systems and applications.

In a [blog post](https://www.ivanti.com/blog/cve-2023-35078-new-ivanti-epmm-vulnerability), Ivanti confirmed the zero-day and said it was aware of "*a very limited number of customers that have been impacted*," which is also what this newsletter heard from a source—that more organizations besides the Norwegian government were breached.

At a technical level, Ivanti described the vulnerability ([CVE-2023-35078](https://forums.ivanti.com/s/article/CVE-2023-35078-Remote-unauthenticated-API-access-vulnerability?language=en_US)) as a bypass of the EPMM API authentication system that can allow an attacker to make remote changes to an EPMM management server, changes that can technically be limited only by an attacker's imagination.

Because of the level of access an MDM platform like the EPMM has, the vulnerability can be used to collect data from user devices or deploy malicious payloads.

The Norwegian National Security Authority ([NSM](https://nsm.no/aktuelt/nulldagssarbarhet-i-ivanti-endpoint-manager-mobileiron-core)) and the Norwegian Government Security and Service Organisation ([DSS](https://www.dss.dep.no/aktuelle-saker/departementer-utsatt-for-dataangrep/)) took credit for discovering the zero-day.

The NSM said it withheld information about the zero-day and the attacks until Ivanti released a patch. The NSM said it was afraid the vulnerability would be exploited in both Norway and abroad if they disclosed details too early.

Judging by the fact the zero-day received a severity rating of 10/10, it is likely easy to exploit and requires little technical know-how to do so.

Several cybersecurity agencies across the EU and US have already released advisories, urging their private and public sector organizations to patch.

More than 500 Ivanti EPMM systems are currently exposed on the internet, according to Shodan.

[![](https://substackcdn.com/image/fetch/$s_!6OIr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2d167e06-6011-43c1-b111-6b32b7501a05_1084x449.png)](https://substackcdn.com/image/fetch/%24s_%216OIr%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/2d167e06-6011-43c1-b111-6b32b7501a05_1084x449.png)

### **Breaches, hacks, and security incidents**

**Yamaha breach (sort of):**Yamaha's Canadian music division has had its [network breached](https://ca.yamaha.com/en/news_events/2023/0720_cyber_security.html) and data stolen. Multiple ransomware gangs are taking credit—with both Akira and BlackByte taking credit. [*Additional coverage in [The Record](https://therecord.media/yamaha-confirms-cyberattack-after-multiple-ransomware-gangs-claim)*]

**AlphaPo hack update:** Losses from the AlphaPo hack have grown from $23 million to $60 million.

**Palmswap crypto-heist:** The Palmswap platform lost [$900,000](https://archive.ph/MAsBF) in crypto-assets after a hacker exploited a vulnerability in its blockchain smart contract.

**Spyhide hack:** A misconfiguration has exposed the development environment and the source code of Iranian spyware maker Spyhide. The exposed systems were [discovered](https://maia.crimew.gay/posts/fuckstalkerware-2/) by Swiss computer hacker [Maia Arson Crimew](https://en.wikipedia.org/wiki/Maia_arson_crimew) (*formerly known as Tillie Kottmann, deletescape, and antiproprietary*), who analyzed the code and later developed an exploit to access the spyware's backend panel and dump its data. The data contained information on Spyhide customers and information collected from infected Android smartphones. *[TechCrunch](https://techcrunch.com/2023/07/24/spyhide-stalkerware-android/)* reviewed the Spyhide data and said it found information on 4,000 customers who deployed the spyware on more than 60,000 devices across the world over the past seven years.

### **General tech and privacy**

**AI at the NYC subway:** The New York City subway administration is using AI to spot people dodging fares. The system has been live since May in seven stations across the city and is scheduled to expand to more than two dozen more stations. [*Additional coverage in [NBC News](https://www.nbcnews.com/tech/tech-news/nyc-subway-using-ai-track-fare-evasion-rcna93045)*]

**Ubisoft to suspend accounts:** Gaming giant Ubisoft plans to suspend and then delete long-inactive accounts, regardless if they own paid-for games or not. Continues the trend of tech companies doing whatever they want regardless of consumer and privacy laws. [*Additional coverage in [Eurogamer](https://www.eurogamer.net/ubisoft-is-suspending-inactive-accounts-disabling-access-to-game-libraries)]*

**Google plea:** A coalition of K-12 professionals, environmentalists, consumer advocates, and more than 10,000 members of the US Public Interest Research Group have asked Google in an [open letter](https://pirg.org/edfund/resources/chromebook-expiration-full-letter/) to extend the life of millions of Chromebooks that are set to reach end-of-life this summer. The signees say that Chromebooks hardware and software expire too quickly and the devices need to be replaced too often, creating [unnecessary e-waste](https://www.theverge.com/2023/4/21/23691840/us-pirg-education-fund-report-investigation-chromebook-churn) and costs to schools and students. They say Google could continue to ship software updates and extend the life of 13 Chromebooks that are set to expire this summer and keep millions of students online and capable of accessing school systems.

> "Chromebooks come with an Automatic Update Expiration date, after which software support ends. The lack of software support can block essential uses such as accessing state testing websites and make devices vulnerable. Google could extend the life of these models, most of which are still available for purchase online."

[![](https:...