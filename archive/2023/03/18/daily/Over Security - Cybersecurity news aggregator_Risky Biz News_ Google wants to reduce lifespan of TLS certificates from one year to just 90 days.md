---
title: Risky Biz News: Google wants to reduce lifespan of TLS certificates from one year to just 90 days
url: https://riskybiznews.substack.com/p/risky-biz-news-google-wants-to-reduce
source: Over Security - Cybersecurity news aggregator
date: 2023-03-18
fetch_date: 2025-10-04T09:59:37.167896
---

# Risky Biz News: Google wants to reduce lifespan of TLS certificates from one year to just 90 days

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Google wants to reduce lifespan of TLS certificates from one year to just 90 days

### In other news: Authorities take down ChipMixer service used by ransomware gangs; Magniber ransomware starts targeting Europe; US charges two suspects for DEA portal hack.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Mar 17, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

Google has [announced plans](https://www.chromium.org/Home/chromium-security/root-ca-policy/moving-forward-together/) to reduce the maximum lifespan of a TLS certificate from the current value of 398 days to only 90 in a move that is going to send shockwaves across several IT industries.

There is currently no official date for when this new policy is going to come into effect.

Google says it plans to make a future proposal on this topic at the CA/Browser Forum, an informal group made up of browser vendors and Certificate Authorities (CAs), the companies that issue TLS certificates.

This would mark the fourth time that the maximum lifespan of a TLS certificate would be changed after TLS certs went from 5-year validity periods to three, two, and then one.

Every policy change has been riddled with endless discussions on why a change would be detrimental to both CAs and their customers.

Tim Callan, Chief Experience Officer at certificate authority Sectigo, believes Google is "deliberately telegraphing" the industry about its plan in order to avoid the [public brouhaha](https://www.zdnet.com/article/google-wants-to-reduce-lifespan-for-https-certificates-to-one-year/) we had in previous years.

Google appears to have found the right tone, with the company advocating that reducing certificate lifespans "encourages automation" and moves the CA industry away from "baroque, time-consuming, and error-prone issuance processes" that have failed to detect abuse.

Google specifically mentions that CAs automating their TLS cert issuance procedures will "allow for faster adoption of emerging security capabilities and best practices."

From industry reactions, both [Sectigo](https://sectigo.com/resource-library/google-announces-intentions-to-limit-tls-certificates-to-90-days-why-automated-clm-is-crucial) and [GlobalSign](https://www.globalsign.com/en/blog/google-90-day-certificate-validity-requires-automation) appear to have embraced a migration to automated certificate lifecycle management (CLM) procedures.

Either that or they know that Google can enforce the change in Chrome at any time and without a vote in the CA/Browser Forum, and CAs will have to start issuing 90-day certs or lose customers.

This exact scenario [happened in 2020](https://www.zdnet.com/article/apple-strong-arms-entire-ca-industry-into-one-year-certificate-lifespans/) when Apple unilaterally decided to support one-year TLS certs, and everyone else had to follow its lead—Google, Mozilla, and then the (*grumbling*) CAs.

### **Breaches and hacks**

**Rubrik hack:** Cloud security firm Rubrik [confirms](https://www.rubrik.com/blog/company/23/3/fortra-goanywhere) that it is one of the companies that got hacked using the [GoAnywhere zero-day](https://riskybiznews.substack.com/p/risky-biz-news-zero-day-alert-for) ([CVE-2023-0669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0669)) last month. The company says the intruders only gained access to a non-production IT testing environment and that "there was no lateral movement to other environments." Nevertheless, Rubrik has confirmed the threat actors managed to steal some of its data from the non-production environment, data from its sales department, including data on customers and partner companies.

**Poolz crypto-heist:** The Poolz cryptocurrency platform [lost $665,000](https://archive.ph/Sevxq) worth of assets after an attacker [exploited a bug](https://mp.weixin.qq.com/s/gIpt83U_qd-wMYI_EArv0g) in one of its blockchain contracts.

**ICS incidents:** Kaspersky's ICS team has a [summary](https://ics-cert.kaspersky.com/publications/reports/2023/03/15/h2-2022-brief-overview-of-main-incidents-in-industrial-cybersecurity/) of the cybersecurity incidents that impacted the industrial sector in H2 2022. This includes breaches at Swiss dairy giant Cremo, Luxembourg-based energy provider Encevo, German semiconductor manufacturer Semikron, and others.

### **General tech and privacy**

**Docker to remove free tier:** Virtualization platform Docker plans to remove free Organization accounts from Docker Hub, the company's Docker images repository. The move is expected to impact and effectively boot most open-source projects off the platform unless they pay $420/year. [Tutorials](https://blog.alexellis.io/docker-is-deleting-open-source-images/) are currently being shared online on how to move Docker images from Organization accounts back to free personal accounts.

**Epic Games fined $245 million:** The US FTC has [fined Epic Games](https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-finalizes-order-requiring-fortnite-maker-epic-games-pay-245-million-tricking-users-making), the company behind the Fortnite game, $245 million for using dark patterns to trick players into making unwanted purchases. The FTC says the practice was specifically vile since it allowed children to rack up unauthorized charges without any parental oversight.

### **Government, politics, and policy**

**Federal agency breach:** [CISA says](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-074a) that multiple threat actors, including an APT group, exploited a 2019 vulnerability to gain access to a federal agency's IIS web server. CISA says the attacks took place from November 2022 through early January 2023. The exploited vulnerability is tracked as [CVE-2019-18935](https://nvd.nist.gov/vuln/detail/CVE-2019-18935) and was previously widely exploited for at least two years before the CISA report this week. The vulnerability resides in the UI component of the Progress Telerik framework, a tool commonly used for building user interfaces for ASP.NET applications. In the past, the same bug has been widely used in cryptomining campaigns and for building various botnets.

**New SEC cybersecurity rules:** The US Securities and Exchange Commission has [proposed](https://www.sec.gov/news/press-release/2023-52) new cybersecurity rules for operators on the US securities market, such as broker-dealers, clearing agencies, and national securities exchanges. The new rules require that financial companies report cybersecurity breaches to the SEC within 48 hours of detection. The new rules mandate that financial entities establish "reasonably designed" policies to address cybersecurity risks in their environments and run cybersecurity audits every year to test their defenses. The new rules will enter a 60-day public comment period before they are updated or adopted as is.

**Audit of Chinese drones:** A group of US senator...