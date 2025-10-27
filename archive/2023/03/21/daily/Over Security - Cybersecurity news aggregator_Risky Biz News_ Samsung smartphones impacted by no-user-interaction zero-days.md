---
title: Risky Biz News: Samsung smartphones impacted by no-user-interaction zero-days
url: https://riskybiznews.substack.com/p/risky-biz-news-samsung-smartphones
source: Over Security - Cybersecurity news aggregator
date: 2023-03-21
fetch_date: 2025-10-04T10:11:17.353275
---

# Risky Biz News: Samsung smartphones impacted by no-user-interaction zero-days

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Samsung smartphones impacted by no-user-interaction zero-days

### In other news: FBI investigates TikTok for spying on journalists; BreachForum admin arrested in the US; aCropalypse vulnerability can recover cropped and redacted screenshots.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Mar 20, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

Google's Project Zero research team has [identified 18 vulnerabilities](https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html) in Exynos, a modem chipset manufactured by South Korean company Samsung and used by multiple smartphone vendors and even some vehicles.

Project Zero says that of the 18 vulnerabilities, four are incredibly dangerous as they allow for what the company calls "Internet-to-baseband remote code execution attacks."

Google says that tests carried out by Project Zero researchers have confirmed that attackers can compromise a smartphone with no user interaction and only require that the attacker knows the victim's phone number.

Of the 18 vulnerabilities, Samsung has [patched only six](https://semiconductor.samsung.com/support/quality-support/product-security-updates/) in security updates in January and March this year. Of the four big RCEs, only one has received patches—see CVE-2023-24033.

Google has published its findings after some of the 18 bugs it reported to Samsung hit the 90-day deadline, which it gave Samsung to fix the issues.

Based on publicly available information, none of the 18 vulnerabilities appear to have been exploited in the wild, but Google says that skilled attackers would be able "to quickly create an operational exploit to compromise."

Until Samsung releases patches and until the patches make it to consumers, Google says that users should be safe if they turn off "Wi-Fi calling" and "Voice-over-LTE (VoLTE)" in their device settings.

While a list of affected users who might be using a device with an Exynos modem/chipset may not be complete, the following are known to be vulnerable:

* Mobile devices from Samsung, including those in the S22, M33, M13, M12, A71, A53, A33, A21s, A13, A12 and A04 series;
* Mobile devices from Vivo, including those in the S16, S15, S6, X70, X60 and X30 series;
* The Pixel 6 and Pixel 7 series of devices from Google; and
* any vehicles that use the Exynos Auto T5123 chipset.

### **Breaches and hacks**

**Wawa breach settlement:** Convenience store chain Wawa has [agreed](https://www.law360.com/articles/1585134/wawa-credit-unions-ink-28-5m-settlement-over-card-hack) to pay $28.5 million to settle a class-action lawsuit stemming from a [2019 data breach](https://www.zdnet.com/article/wawa-says-pos-malware-incident-impacts-potentially-all-locations/). Hackers breached the company in 2019 and ran malware on its point-of-sale systems for eight months. The intruders collected more than 30 million credit card details, which they later [sold on the dark web](https://geminiadvisory.io/breached-wawa-payment-card-records-reach-dark-web/). Three major credit unions sued Wawa in 2020 for financial relief after they had to replace cards and reimburse stolen funds.

**NBA breach:** The NBA is [notifying](https://archive.ph/FE74e) users of a data breach that impacted its email service provider. The sports league says that names and email addresses were stolen from the third-party's systems. While the NBA warns of increasing phishing-related risks, it says that now passwords for its website were compromised. The NBA didn't name the email service provider.

**HMIS hack:** Indian cybersecurity firm [CloudSEK says](https://cloudsek.com/threatintelligence/russian-hacktivist-group-phoenix-targets-indias-health-ministry-website) that a pro-Russian hacktivist group named Phoenix has compromised the website of India's Health Ministry and gained access to the ministry's official database system, the Health Management Information System (HMIS). The hackers claimed to have gained access to information on all Indian hospitals, doctors, and other employees. The group claimed they carried out the attack as a consequence of India's agreement to honor oil price caps and sanctions imposed on Russia by fellow G-20 countries.

**ParaSpace avoids hack:** Cryptocurrency platform [ParaSpace](https://archive.ph/FzxAJ) paused transactions and prevented a hacker from stealing $5 million worth of funds from its accounts. The attempted hack was described as an exploit against one of the platform's smart contracts and was spotted before it did any damage by blockchain auditing firm [BlockSec](https://archive.ph/fWdbn). It also helped that the attacker also didn't have enough funds for the necessary "gas price" to run the exploit during their first hack attempt. Ironically, after the attack was spotted the second time, the hacker had the audacity to ask BlockSec to refund the gas price they wasted on the second attack. [*Press coverage in [BitcoinInsider](https://www.bitcoininsider.org/article/209219/blocksec-foils-hackers-attempt-steal-5-million-paraspace)*]

**Fiatusdt leak:** The Fiatusdt cryptocurrency platform left a database with KYC data exposed online. Passports and IDs for [20,000 users](https://www.websiteplanet.com/news/fiatusdt-leak-report/) were exposed.

[![](https://substackcdn.com/image/fetch/$s_!CFDD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8db265ae-69a7-4134-a92b-12853e5cb990_798x536.png)](https://substackcdn.com/image/fetch/%24s_%21CFDD%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/8db265ae-69a7-4134-a92b-12853e5cb990_798x536.png)

### **General tech and privacy**

**GitHub stars black market:** DevOps company Dagster has a [deep dive](https://dagster.io/blog/fake-stars) into how to spot projects that have bought GitHub stars off the black market.

**Safe npm:** DevOps company Socket has released what it calls "[safe npm](https://socket.dev/blog/introducing-safe-npm)," a security wrapper for the npm package manager utility that pauses installations whenever it detects a malicious or risky package.

**NordVPN goes FOSS:** NordVPN has [open-sourced](https://nordvpn.com/blog/nordvpn-linux-open-source/) its Linux VPN client, Libtelio, a networking library used across NordVPN apps, and Libdrop, a library used to share files over Meshnet.

**Meta tracking deemed illegal:** The Austrian Data Protection Authority (DSB) has [ruled](https://noyb.eu/en/austrian-dsb-meta-tracking-tools-illegal) that Facebook's use of its tracking pixel directly violates the GDPR. The ruling comes after consumer protection organization noyb filed more than 100 complaints against the company across Europe.

**Linux project refuses Russian company's patches:** The Linux kernel project has declined to accept a patch s...