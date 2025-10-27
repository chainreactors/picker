---
title: Risky Biz News: Tor network hit with DDoS attacks over past seven months
url: https://riskybiznews.substack.com/p/risky-biz-news-tor-network-hit-with
source: Over Security - Cybersecurity news aggregator
date: 2023-02-09
fetch_date: 2025-10-04T06:09:02.356144
---

# Risky Biz News: Tor network hit with DDoS attacks over past seven months

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Tor network hit with DDoS attacks over past seven months

### In other news: BSI has a new chief; Operation Magicflame disrupts major Asian cybercrime gang; Cl0p gang's Linux ransomware decrypted.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Feb 08, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

The Tor Project says that over the past seven months, the availability of the Tor network has been disrupted by a series of [massive DDoS attacks](https://blog.torproject.org/tor-network-ddos-attack/).

The organization says that during some moments, "the attacks impacted the network severely enough that users could not load pages or access onion services."

The Tor Project says the methods and targets of these attacks have changed over time, and its engineers currently can't determine with certainty who was behind the attacks or their intentions.

After speaking to several Tor relay operators, *RiskyBizNews*understands the attacks are not taking place at the same time against the entire Tor network. Instead, the attackers target a small number of relays and rotate to new relays after a few days.

The Tor community has been well aware of the issue. No Tor server operators have reported receiving ransom demands following the attacks.

Some members successfully developed some basic DDoS mitigations, but as the Tor Project explains in the blog post, attackers also updated the way they carry out attacks.

[![](https://substackcdn.com/image/fetch/$s_!Ud-E!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86b5f069-beee-40f1-820c-6686d8e05d94_1500x707.png)](https://substackcdn.com/image/fetch/%24s_%21Ud-E%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/86b5f069-beee-40f1-820c-6686d8e05d94_1500x707.png)

### **Breaches and hacks**

**SperaxUSD crypto-heist:** A threat actor exploited a bug in the protocols of the SperaxUSD cryptocurrency service and [stole roughly $300,000](https://archive.ph/5nwpW) from the company.

**Vesuvius incident:** UK engineering company Vesuvius [says](https://tools.euroland.com/tools/Pressreleases/GetPressRelease/?ID=4236627&lang=en-GB&companycode=uk-cksn&v=) it suffered a cybersecurity breach. The company says it shut down affected systems and is working to investigate the incident and restore systems. The company has more than 10,000 employees across the world and is known for its metal and ceramics work and molten metal flow engineering.

**RSAWeb ransomware attack:** A ransomware attack has been identified as the source of a days-long outage that has impacted the services of South African telco and cloud hosting provider RSAWeb. The incident took place on February 1, and the company took days to fully recover, according to a notification the company sent to its customers. The company says the attack affected its website, internet fiber, mobile, hosting, VoIP, and PBX services. [*Press coverage in [MyBroadband](https://mybroadband.co.za/news/security/479051-rsaweb-hit-by-ransomware-attack.html)*]

### **General tech and privacy**

**Tutanota's new whistleblower system:** Secure email provider Tutanota has [launched](https://tutanota.com/blog/posts/whistleblower-system) [Secure Connect](https://tutanota.com/hinweisgebersystem), a new whistleblower system that lets companies add a secure and anonymous reporting channel. The project is similar to the Guardian's [SecureDrop](https://securedrop.org/). The difference is that it's not open-source, and it requires a Tutanota Pro account.

**Dashlane apps go open-source:** Password manager Dashlane has [open-sourced](https://blog.dashlane.com/mobile-code-now-publicly-available/) its [Android](https://github.com/Dashlane/android-apps) and [iOS](https://github.com/Dashlane/dashlane-apple-sources) apps. This includes all their apps, not just the password manager ones.

**Prototype pollution protection:** Google security engineers are working on a proposal to mitigate prototype pollution vulnerabilities by introducing a secure opt-in mode in JavaScript processing environments, such as web browsers. [*More in the [Daily Swig](https://portswigger.net/daily-swig/google-engineers-plot-to-mitigate-prototype-pollution)*]

> "Pollution vulnerabilities exist because JS properties can be changed by default by anyone who has a reference to them. [...] Pollution bugs are a type of data-only attacks that lie outside of the threat model of many existing mitigations, like the Content Security Policy."

**NIST cryptography updates:** US NIST has [updated](https://www.nist.gov/news-events/news/2023/02/nist-revises-digital-signature-standard-dss-and-publishes-guideline) the Federal Information Processing Standard known as FIPS 186-5, which recommends which cryptographic algorithms and techniques should be used for the generation and verification of digital signatures. Currently, [the standard](https://www.federalregister.gov/documents/2023/02/03/2023-02273/announcing-issuance-of-federal-information-processing-standard-fips-186-5-digital-signature-standard) recommends algorithms such as RSA, ECDSA, and EdDSA. This update introduces two new Edwards curves recommended for use with the EdDSA algorithm. These are Ed25519 and Ed448.

### **Government, politics, and policy**

**New BSI lead:** Claudia Plattner, Director General of Information Systems at the European Central Bank (ECB), has been [appointed](https://www.ecb.europa.eu/press/pr/date/2023/html/ecb.pr230207_1~cf7b469560.ro.html) as the new chief of Germany's cybersecurity agency, the Federal Office for Information Security, also known as the BSI. Plattner will formally take up her new role in July this year. Plattner replaces Arne Schoenbohm, who was [dismissed](https://www.linkedin.com/posts/arne-sch%C3%B6nbohm-4069b27_liebe-kollegen-heute-r%C3%A4ume-ich-meine-pers%C3%B6nlichen-activity-7004070967308075008-02ID/) last October after [German media](https://www.focus.de/digital/internet/nach-bahn-sabotage-bundeswehr-warnt-vor-infrastruktur-angriffen-boehmermann-deckt-cyber-luecke-auf_id_162047933.html) found ties to Russia's intelligence services in one of his past private-sector endeavors.

**India bans more Chinese apps:** The Indian government has blocked 138 betting apps and 94 loan lending apps, [citing](https://twitter.com/PBNS_India/status/1622125330638192640) alleged "Chinese links." The ban was pushed through as an "emergency" to protect the integrity of its citizens' personal data. India has also blocked more than 300 Chinese apps in recent years. [*Additional coverage in [TechCrunch](https://techcrunch.com/2023/02/05/india-is-blocking-over-230-betting-and-loan-apps-many-with-ties-to-china/)*]

**Cybersecurity execs join NSTAC:** The White House has [added](https://www.whitehouse.gov/briefing-room/statements-releases/20...