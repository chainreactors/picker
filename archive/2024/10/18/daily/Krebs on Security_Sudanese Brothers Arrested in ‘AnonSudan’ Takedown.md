---
title: Sudanese Brothers Arrested in ‘AnonSudan’ Takedown
url: https://krebsonsecurity.com/2024/10/sudanese-brothers-arrested-in-anonsudan-takedown/
source: Krebs on Security
date: 2024-10-18
fetch_date: 2025-10-06T19:06:08.308915
---

# Sudanese Brothers Arrested in ‘AnonSudan’ Takedown

Advertisement

[![](/b-knowbe4/40.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Sudanese Brothers Arrested in ‘AnonSudan’ Takedown

October 17, 2024

[11 Comments](https://krebsonsecurity.com/2024/10/sudanese-brothers-arrested-in-anonsudan-takedown/#comments)

The U.S. government on Wednesday announced the arrest and charging of two Sudanese brothers accused of running **Anonymous Sudan** (a.k.a. **AnonSudan**), a cybercrime business known for launching powerful distributed denial-of-service (DDoS) attacks against a range of targets, including dozens of hospitals, news websites and cloud providers. The younger brother is facing charges that could land him life in prison for allegedly seeking to kill people with his attacks.

![](https://krebsonsecurity.com/wp-content/uploads/2024/10/as-kenya.png)

Active since at least January 2023, AnonSudan has been described in media reports as a “hacktivist” group motivated by ideological causes. But in [a criminal complaint](https://www.justice.gov/usao-cdca/media/1373586/dl?inline), the FBI said those high-profile cyberattacks were effectively commercials for the hackers’ DDoS-for-hire service, which they sold to paying customers for as little as $150 a day — with up to 100 attacks allowed per day — or $700 for an entire week.

The complaint says despite reports suggesting Anonymous Sudan might be state-sponsored Russian actors pretending to be Sudanese hackers with Islamist motivations, AnonSudan was led by two brothers in Sudan — **Ahmed Salah Yousif** **Omer**, 22, and **Alaa Salah Yusuuf Omer**, 27.

AnonSudan claimed credit for successful DDoS attacks on numerous U.S. companies, causing a [multi-day outage](https://msrc.microsoft.com/blog/2023/06/microsoft-response-to-layer-7-distributed-denial-of-service-ddos-attacks/) for Microsoft’s cloud services in June 2023. The group hit **PayPal** the following month, followed by **Twitter/X** (Aug. 2023), and **OpenAI** (Nov. 2023). An [indictment](https://www.justice.gov/usao-cdca/media/1373581/dl?inline) in the Central District of California notes the duo even swamped the websites of the **FBI** and the **Department of State**.

Prosecutors say Anonymous Sudan offered a “Limited Internet Shutdown Package,” which would enable customers to shut down internet service providers in specified countries for $500 (USD) an hour. The two men also allegedly extorted some of their victims for money in exchange for calling off DDoS attacks.

The government isn’t saying where the Omer brothers are being held, only that they were arrested in March 2024 and have been in custody since. A [statement](https://www.justice.gov/usao-cdca/pr/two-sudanese-nationals-indicted-alleged-role-anonymous-sudan-cyberattacks-hospitals) by the **U.S. Department of Justice** says the government also seized control of AnonSudan’s DDoS infrastructure and servers after the two were arrested in March.

AnonSudan accepted orders over the instant messaging service **Telegram**, and marketed its DDoS service by several names, including “**Skynet**,” “**InfraShutdown**,” and the “**Godzilla botnet**.” However, the DDoS machine the Omer brothers allegedly built was not made up of hacked devices — as is typical with DDoS botnets.

Instead, the government alleges Skynet was more like a “distributed cloud attack tool,” with a command and control (C2) server, and an entire fleet of cloud-based servers that forwards C2 instructions to an array of open proxy resolvers run by unaffiliated third parties, which then transmit the DDoS attack data to the victims.

**Amazon** was among many companies credited with helping the government in the investigation, and said AnonSudan launched its attacks by finding hosting companies that would rent them small armies of servers.

“Where their potential impact becomes really significant is when they then acquire access to thousands of other machines — typically misconfigured web servers — through which almost anyone can funnel attack traffic,” Amazon explained in [a blog post](https://www.aboutamazon.com/news/aws/amazon-US-department-of-justice-cybersecurity). “This extra layer of machines usually hides the true source of an attack from the targets.”

The security firm **CrowdStrike** [said](https://www.crowdstrike.com/en-us/blog/anonymous-sudan-hacktivist-group-ddos-indictment/) the success of AnonSudan’s DDoS attacks stemmed from a combination of factors, including sophisticated techniques for bypassing DDoS mitigation services. Also, AnonSudan typically launched so-called “[Layer 7](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/)” attacks that sought to overwhelm targeted “[API endpoints](https://www.cloudflare.com/learning/security/api/what-is-api-endpoint/)” — the back end systems responsible for handling website requests — with bogus requests for data, leaving the target unable to serve legitimate visitors.

The Omer brothers were both charged with one count of conspiracy to damage protected computers. The younger brother — Ahmed Salah — was also charged with three counts of damaging protected computers.

![](https://krebsonsecurity.com/wp-content/uploads/2024/10/ahmedomer.png)

If extradited to the United States, tried and convicted in a court of law, the older brother Alaa Salah would be facing a maximum of five years in prison. But prosecutors say Ahmed Salah could face life in prison for allegedly launching attacks that sought to kill people.

As Hamas fighters broke through the border fence and attacked Israel on Oct. 7, 2023, a wave of rockets was launched into Israel. At the same time, AnonSudan announced it was attacking the APIs that power Israel’s widely-used “red alert” mobile apps that warn residents about any incoming rocket attacks in their area.

In February 2024, AnonSudan launched a digital assault on the **Cedars-Sinai Hospital** in the Los Angeles area, an attack that caused emergency services and patients to be temporarily redirected to different hospitals.

The complaint alleges that in September 2023, AnonSudan began a week-long DDoS attack against the Internet infrastructure of Kenya, knocking offline government services, banks, universities and at least seven hospitals.

*This entry was posted on Thursday 17th of October 2024 10:17 AM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [DDoS-for-Hire](https://krebsonsecurity.com/category/ddos-for-hire/) [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Ahmed Salah Yousif Omer](https://krebsonsecurity.com/tag/ahmed-salah-yousif-omer/) [Alaa Salah Yusuuf Omer](https://krebsonsecurity.com/tag/alaa-salah-yusuuf-omer/) [Amazon](https://krebsonsecurity.com/tag/amazon/) [AnonSudan](https://krebsonsecurity.com/tag/anonsudan/) [Anonymous Sudan](https://krebsonsecurity.com/tag/anonymous-sudan/) [fbi](https://krebsonsecurity.com/tag/fbi/) [Godzilla botnet](https://krebsonsecurity.com/tag/godzilla-botnet/) [InfraShutdown](https://krebsonsecurity.com/tag/infrashutdown/) [Skynet](https://krebsonsecurity.com/tag/skynet/) [U.S. Department of Justice](https://krebsonsecurity.com/tag/u-s-department-of-justice/)

Post navigation

[← Lamborghini Carjackers Lured by $243M Cyberheist](https://krebsonsecurity.com/2024/10/lamborghini-carjackers-lured-...