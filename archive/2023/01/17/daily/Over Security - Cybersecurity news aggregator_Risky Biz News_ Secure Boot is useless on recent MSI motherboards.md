---
title: Risky Biz News: Secure Boot is useless on recent MSI motherboards
url: https://riskybiznews.substack.com/p/risky-biz-news-secure-boot-is-useless
source: Over Security - Cybersecurity news aggregator
date: 2023-01-17
fetch_date: 2025-10-04T04:04:20.135190
---

# Risky Biz News: Secure Boot is useless on recent MSI motherboards

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Secure Boot not working on recent MSI motherboards

### In other news: Norton Password Manager hit by credential-stuffing attack; hacktivists leak Cellebrite tools; Lexmark printer zero-day disclosed.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jan 16, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

For almost a year, the [Secure Boot](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot) feature on MSI motherboards has been broken and allowing malicious code to run, Dawid Potocki, a Polish IT student studying in New Zealand, has discovered.

Secure Boot is a feature that works at the motherboard chipset level, where it uses cryptographic signatures to verify the authenticity of drivers and operating system files before booting up a computer.

When Secure Boot is enabled inside the BIOS or UEFI firmware of a computer (actually the motherboard firmware), if drivers or the OS bootloader have been tampered with by malware, the boot-up process stops with warnings for IT administrators.

But while this works as intended for many motherboard vendors, Potocki says that since January 2022, MSI appears to have changed the default settings of its Secure Boot section in its UEFI/BIOS with new defaults that effectively make Secure Boot useless.

The new defaults are in the "*Secure Boot*" section, under the "*Image Execution Policy*" menu, where all options are now set to "***Always Execute***."

What this means is that even if malware has modified an OS bootloader, the MSI UEFI/BIOS will still boot the image, even if the cryptographic signature has failed.

[![](https://substackcdn.com/image/fetch/$s_!dE_b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82cf6fa7-1931-4455-a786-2945af4876ce_1024x1247.png)](https://substackcdn.com/image/fetch/%24s_%21dE_b%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/82cf6fa7-1931-4455-a786-2945af4876ce_1024x1247.png)

[Potocki says](https://dawidpotocki.com/en/2023/01/13/msi-insecure-boot/) that since January 2022, MSI has been shipping MSI firmware updates that contain the new insecure Secure Boot defaults.

Tens of MSI motherboard models currently ship with these new settings for both Intel and AMD CPUs, impacting both Windows and Linux distros. A full list of impacted MSI motherboard models is available [here](https://github.com/Foxboron/sbctl/issues/181).

While it may take some time for MSI to ship new firmware versions with fixed settings for its Secure Boot section, Potocki recommends that all MSI motherboard owners who rely on Secure Boot go into their UEFI/BIOS and change away from "***Always Execute***" to another policy.

> "Don't trust that whatever security features you enabled are working, TEST THEM! Somehow I was the first person to document this, even though it has been first introduced somewhere in 2021 Q3."

### **Breaches and hacks**

**CircleCI shares more info:** After [disclosing](https://circleci.com/blog/january-4-2023-security-alert/) a security breach at the start of the year, continuous integration and continuous delivery platform CircleCI has [published more details](https://circleci.com/blog/jan-4-2023-incident-report/) about what really happened behind the scenes. CircleCI says that hackers broke into its internal network after infecting one of its engineers with malware. The hacker used the malware to steal a session cookie for CircleCI's backend network, where they lingered for four days between December 19 and December 22, stealing internal databases and data stores, including from systems that stored customer environment variables, tokens, and keys. CircleCI says that even if this data was normally encrypted, the hacker also dumped and stole the encryption key needed to read the data. CircleCI says it learned of the incident after one of the affected companies notified them about suspicious activity coming via their CircleCI-GitHub integration. CircleCI says that since learning of the hack, it worked with GitHub to rotate all CircleCI OAuth tokens, which should prevent the threat actor from using any of the stolen access tokens to pivot and hack other companies. Regardless, CircleCI still recommends that customers also investigate any irregular activity that took place via its integration between December 19 and January 7.

**Datadog incident:** Cloud security firm [Datadog says](https://docs.datadoghq.com/agent/faq/circleci-incident-impact-on-datadog-agent/) it was impacted by CircleCI's recent incident and that one of its secret access tokens was theoretically exposed. Despite this, Datadog says it saw "no indication that the key was actually leaked or misused."

**SEC sues law firm following APT attack:** The US Securities and Exchange Commission has sued DC-based law firm Covington & Burling in an attempt to reveal the names of customers impacted by a security breach that took place in November 2020. The SEC says the breach was carried out by Hafnium, a suspected Chinese cyber-espionage group, and targeted lawyers that dealt with "policy issues of interest to China in light of the incoming Biden Administration." According to [court documents](https://www.courtlistener.com/docket/66713718/securities-and-exchange-commission-v-covington-burling-llp/), Hafnium accessed internal network drives and email accounts, and the law firm extensively cooperated with the FBI. The SEC is now trying to use the courts to force Covington & Burling to disclose the names of its affected customers and see if the law firm and its customers broke any securities laws by not disclosing the existence or the breadth of their respective breaches. [*Additional coverage in [Reuters](https://www.reuters.com/legal/government/sec-sues-covington-law-firm-names-300-clients-caught-up-hack-2023-01-11/)*]

**NortonLifeLock cred-stuff attack:** NortonLifeLock is sending [data breach notifications](https://ago.vermont.gov/blog/2023/01/09/nortonlifelock-gen-digital-data-breach-notice-to-consumers/) to customers of its Norton Password Manager service, alerting users that hackers have breached their accounts using a credential-stuffing attack. The incident took place in the first half of December last year. NortonLifeLock says that [925,000 accounts](https://www.bleepingcomputer.com/news/security/nortonlifelock-warns-that-hackers-breached-password-manager-accounts/) were targeted but did not disclose how many were compromised. Passwords stored in those accounts should be considered compromised, and users will need to change them as soon as possible.

**24h Le Mans Virtual incident:** This year's edition of the virtual version of the 24 Hours of Le Mans race has been interrupted twice after two servers that were used to host the event have been impacted by w...