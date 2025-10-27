---
title: Risky Biz News: Iranian state hackers breached US government agency and deployed a cryptominer, out of all things
url: https://riskybiznews.substack.com/p/risky-biz-news-iranian-state-hackers
source: Over Security - Cybersecurity news aggregator
date: 2022-11-19
fetch_date: 2025-10-03T23:14:46.519215
---

# Risky Biz News: Iranian state hackers breached US government agency and deployed a cryptominer, out of all things

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Iranian state hackers breached US government agency and deployed a cryptominer, out of all things

### In other news: Google wins lawsuit against Glupteba botnet operators; Popopret gets suspended sentence; France fines Discord for GDPR violations.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Nov 18, 2022

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

In a [joint security advisory](https://www.cisa.gov/uscert/ncas/alerts/aa22-320a) this week, CISA and the FBI revealed that an Iranian APT group breached the network of a US government organization in an attack that could have turned out much worse than it did.

The breach took place earlier this year, in February, and CISA and FBI incident responders said the threat actor used an [exploit](https://digital.nhs.uk/cyber-alerts/2022/cc-4002) for the Log4Shell vulnerability to take control over a VMWare Horizon server, moved laterally inside the victim's network, compromised the domain controller and local credentials, and deployed reverse proxies on several hosts for future access.

The report doesn't mention anything about sensitive data collection or abuse of the agency's email domain for espionage purposes but instead claims that the intruders deployed a very basic and widely known cryptocurrency mining app known as [XMRig](https://github.com/xmrig/xmrig) to mine the Monero cryptocurrency on the agency's servers, for their own personal gains.

This seems odd, but if you've read enough reporting on Iranian APTs, it's actually not that strange since it's widely known at this point that the Iranian government heavily relies on third-party contractors to carry out offensive cyber operations and espionage activity.

Previous reports have linked several of these groups to both classic espionage activity but also to your run-of-the-mill financially motivated cybercrime, usually carried out from the same infrastructure but for the personal gain of the operator, who would most likely know that because of their Iran citizenship, they would face almost no consequences for their actions.

For example, Iranian threat groups have been linked to internet-wide scans that compromised corporate systems, which were later put on sale on cybercrime forums. They've also been linked to different ransomware strains and subsequent payments, but also to the theft of academic papers that were later resold internally, in Iran, on dedicated web portals.

While the joint alert doesn't mention the victim, the *[Washington Post](https://s2.washingtonpost.com/camp-rw/?trackId=624610cbf03bc02e7d7af4cc&s=637627877e2620469f141094&linknum=4&linktot=45)* cites people familiar with the investigation who claim that the compromised agency was the [Merit Systems Protection Board](https://www.mspb.gov/), a small government agency established to protect government workers against partisan political actions. Obviously, not the high-end US government target you'd expect, which would explain why the intruders chose mining over espionage.

WaPo also identified the Iranian hacking group as **Nemesis Kitten**. This group—also known as [DEV-0270](https://www.microsoft.com/en-us/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/), [Cobalt Mirage](https://www.secureworks.com/blog/opsec-mistakes-reveal-cobalt-mirage-threat-actors), [APT42, and UNC788](https://www.mandiant.com/media/17826)—has been linked in the past to attacks with the Log4Shell vulnerability, but also ransomware.

Some security experts have already suggested that deploying a cryptominer could be a cover to hide their espionage-related operations, but is it, though?

If there's one thing that's known about cryptomining is that it's noisy as hell. Once you deploy a cryptominer, your entire server slows down to a crawl, which often leads to your IT team looking into your active process lists and spotting XMRig, one of the most common signs that you've been hacked. In a government agency, that usually implies calling in the feds and DHS, so this theory doesn't particularly hold up.

It's quite possible that the intruders either didn't have the vision to see how they could abuse MSPB's position in the US government infrastructure, or they just didn't care or know what they compromised.

### Breaches and hacks

**Infosys leak:** Cybersecurity firm Infosys has leaked a FullAdminAccess AWS keys on PyPi for over a year, [according to Tom Forbes](https://tomforb.es/infosys-leaked-fulladminaccess-aws-keys-on-pypi-for-over-a-year/), a Python developer from the UK.

**Hyundai fined:** South Korea's data privacy watchdog has fined automaker Hyundai 3 million won ($2,000) after the company's engineers shipped untested code to one of its servers that exposed the personal data of six customers. According to the [commission's inquiry](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=8325#LINK), the server in question was responsible for an app that broadcasts real-time sales information.

**Dom.ru leak:** Hackers have leaked the alleged database of Dom.ru, a Sankt Petersburgh-based internet service provider. The data [allegedly contains](https://paperpaper.ru/papernews/2022/11/16/v-otkrytyj-dostup-vylozhili-lichnye-dan/) the personal details of 4 million of the company's customers, including full names, dates of birth, phone numbers, customer comments, and service-related information.

### General tech and privacy

**Apple satellite emergency service:** Apple [launched](https://www.apple.com/newsroom/2022/11/emergency-sos-via-satellite-available-today-on-iphone-14-lineup/) this week "Emergency SOS via Satellite," a new feature for its Health app that can allow phone owners to request emergency services via satellite whenever they are outside WiFi or cellular coverage. The service is currently available in the US and Canada and will come to France, Germany, Ireland, and the UK in December. Instructions on how to set up the service are available [here](https://support.apple.com/en-us/HT207021).

**Twitter working on encrypted DMs:** While almost everything else is falling apart at Twitter, the company appears to be working on [adding support](https://twitter.com/wongmjane/status/1592721308479291397) for encrypted DMs. Probably not the trustworthy feature Musk envisions when there are reports of foreign intelligence agents lurking inside your company.

**Fringe groups love Musk's Twitter acquisition:** A [joint report](https://blog.smat-app.com/p/fringe-reaction-to-musk-acquiring) from social media analysis app SMAT and New Zealand NGO Tohatoha found that news of Musk's formal Twitter acquisition has been met with great joy by various fringe and extremist groups in all of the internet's darkest corners.

> "From this initial research we can see that racist, conspiracy-driven, anti-democratic groups are very actively discussing and excited about the ne...