---
title: Risky Biz News: Microsoft feels the heat, gives customers access to more cloud security logs
url: https://riskybiznews.substack.com/p/risky-biz-news-microsoft-feels-the
source: Over Security - Cybersecurity news aggregator
date: 2023-07-22
fetch_date: 2025-10-04T11:57:16.393444
---

# Risky Biz News: Microsoft feels the heat, gives customers access to more cloud security logs

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Microsoft feels the heat, gives customers access to more cloud security logs

### In other news: Kevin Mitnick passes; 700,000+ TikTok accounts hacked in Turkey; and Adobe patches a new ColdFusion zero-day.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jul 21, 2023

Share

***This newsletter is brought to you by asset inventory and network visibility company [runZero](https://www.runzero.com). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/). On Spotify:***

Microsoft has expanded the number of security logs that customers of the lower tier of its cloud service can access.

Thirty-one log categories have been moved from the premium tier of the Microsoft Purview Audit service into the standard offering.

The log retention policy for the standard tier has also been changed from 90 to 180 days, Microsoft said in an [announcement](https://www.microsoft.com/en-us/security/blog/2023/07/19/expanding-cloud-logging-to-give-customers-deeper-security-visibility/) on Wednesday.

The company's move comes after increased pressure from the US Cybersecurity and Infrastructure Security Agency, which previously stated that the lack of security logs for many US companies running Azure infrastructure complicated their response and investigations into the SolarWinds and other incidents.

Last week, CISA credited a federal agency that had access to the extended logging capabilities with discovering a stealthy Chinese cyber-espionage campaign that gained access to the Outlook email accounts of several US government agencies, including the State and Commerce Departments.

Through the past few years, Microsoft has been heavily criticized by some of the cybersecurity industry's top figures for placing many crucial security features in the upper and most expensive tiers of its cloud tiers.

This business practice has resulted in companies across the world moving IT infrastructure to Azure cloud services but being unable to pay for the premium tiers, settling for the lower packages, and remaining naked and blind to cybersecurity threats.

As my colleague Tom Uren highlighted in [this week's edition](https://srslyriskybiz.substack.com/p/we-need-cloud-transparency-mandates) of the Seriously Risky Business newsletter (*that incidentally also covered cloud security*), CISA Director Jen Easterly has been [on a campaign](https://www.cisa.gov/cisa-director-easterly-remarks-carnegie-mellon-university) this year to get cloud vendors to stop price gouging security features and provide more logging capabilities to their customers.

Easterly and all others who have been singing this tune are right to push Microsoft on this issue. Providing more security logs doesn't only protect customers but also protects the cloud provider through a secondary effect of crowdsourcing everyone's security detection capabilities. The more eyes on the logs, the more tools scanning those logs, the better for everyone, including Microsoft. If there's one thing the company doesn't need right now, it's more news reports of its cloud service getting rekt for months and crawling with state-sponsored hackers.

In a LinkedIn post, C. Kelly Bissell, CVP for Microsoft's Security Service Line, says there's "much more to come."

*Below is Tom Uren and Patrick Gray discussing needed changes to the security practices of cloud providers in this week's edition of the Seriously Risky Business podcast.*

---

### **Breaches, hacks, and security incidents**

**700k TikTok accounts hacked in Turkey:** An unidentified threat actor gained access to more than 700,000 TikTok accounts from Turkey in April of this year. The hacks took place weeks before the country's presidential election. A TikTok spokesperson confirmed the hacks and said the attacker focused on boosting content from certain accounts. The company told *Forbes*that an internal investigation found no evidence the activity was related to the country's election. Forbes claims the attacker exploited TikTok's use of cheap and insecure SMS-sending capabilities to intercept SMS one-time passwords and hijack accounts. [*Additional coverage in [Forbes](https://www.forbes.com/sites/emilybaker-white/2023/07/18/turkey-tiktok-hack-presidential-election/)/[non-paywall](https://archive.ph/EsCPh)*]

**Estée Lauder incident:** Cosmetics giant Estée Lauder has [disclosed](https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2023/07-19-2023-024305426) a major security breach after a threat actor gained access to its systems. The company says the incident has caused—and is expected to continue to cause—disruption to some parts of its business operations. Estée Lauder is the second-largest cosmetics company in the world by revenue after L'Oreal and owns brands like Tom Ford, MAC, and Clinique. Both the BlackCat and Clop ransomware gangs listed the company on their leak sites. The listings pre-date Estée Lauder's public disclosure, suggesting the company was most likely hit by one or both of the groups.

**MOVEit hacks:** The total number of victims has now surpassed 380, per [Emsisoft](https://www.emsisoft.com/en/blog/44123/unpacking-the-moveit-breach-statistics-and-analysis/).

### **General tech and privacy**

**Google throws support for MLS protocol:** The Internet Engineering Task Force (IETF) has [formally released](https://www.ietf.org/blog/mls-protocol-published/) the Messaging Layer Security ([MLS](https://www.rfc-editor.org/rfc/rfc9420.html)) protocol as an official internet standard. The new MLS protocol was created to allow software to support end-to-end encrypted communications in group or offline scenarios. MLS is [viewed as an upgrade](https://blog.phnx.im/rfc-9420-mls/) to older technologies such as OTR (Off-the-Record) and the Signal protocol. [Google says](https://security.googleblog.com/2023/07/an-important-step-towards-secure-and.html) it plans to integrate the new MLS into its Google Messages client to allow interoperability with other E2EE platforms. Companies like Cisco and RingCentral already have products on the market that support MLS.

**Apple threatens UK exit:** Apple says it will pull FaceTime and iMessage from the UK market if the government uses new proposed powers under the Investigatory Powers Act to force it to weaken its security and encryption features.. Under the [proposed IPA modifications](https://www.gov.uk/government/consultations/revised-investigatory-powers-act-notices-regimes-consultation), companies like Apple would have to clear new security features for their products with the Home Office before releasing them to customers. The new IPA would also let the UK government force tech companies to disable security features for their products without telling the public. Previously, both Signal and WhatsApp threatened they'd leave the UK market if the UK government passed the Online Safety Bill and force them to weaken their encryption to scan for child-abuse material in encrypted messages. [*Additional coverage in the [BBC](https://www.bbc.com/news/technology-66256081)*]

**Ban on private NL domains:** Dutch national domain registrar SIDN has [banned](https://www.sidn.nl/...