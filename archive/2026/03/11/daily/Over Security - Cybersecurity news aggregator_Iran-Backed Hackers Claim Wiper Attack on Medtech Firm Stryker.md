---
title: Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker
url: https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-11
fetch_date: 2026-03-12T04:08:29.389278
---

# Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker

Advertisement

[![](/b-knowbe4/48.jpg)](https://www.knowbe4.com/training-humans-ai-agents?utm_source=krebs&utm_medium=display&utm_campaign=traininghumansandai&utm_content=bannerai)

Advertisement

[![](/b-knowbe4/49.jpg)](https://www.knowbe4.com/training-humans-ai-agents?utm_source=krebs&utm_medium=display&utm_campaign=traininghumansandai&utm_content=bannerai)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker

March 11, 2026

[16 Comments](https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/#comments)

A hacktivist group with links to Iran’s intelligence agencies is claiming responsibility for a data-wiping attack against **Stryker**, a global medical technology company based in Michigan. News reports out of Ireland, Stryker’s largest hub outside of the United States, said the company sent home more than 5,000 workers there today. Meanwhile, a voicemail message at Stryker’s main U.S. headquarters says the company is currently experiencing a building emergency.

Based in Kalamazoo, Michigan, Stryker [NYSE:SYK] is a medical and surgical equipment maker that reported $25 billion in global sales last year. In a lengthy statement posted to Telegram, an Iranian hacktivist group known as **Handala** (a.k.a. Handala Hack Team) claimed that Stryker’s offices in 79 countries have been forced to shut down after the group erased data from more than 200,000 systems, servers and mobile devices.

![A manifesto posted by the Iran-backed hacktivist group Handala, claiming a mass data-wiping attack against medical technology maker Stryker.](https://krebsonsecurity.com/wp-content/uploads/2026/03/handala-stryker.png)

“All the acquired data is now in the hands of the free people of the world, ready to be used for the true advancement of humanity and the exposure of injustice and corruption,” a portion of the Handala statement reads.

The group said the wiper attack was in retaliation for a Feb. 28 missile strike that hit an Iranian school and killed at least 175 people, most of them children. **The New York Times** [reports](https://www.nytimes.com/2026/03/11/us/politics/iran-school-missile-strike.html) today that an ongoing military investigation has determined the United States is responsible for the deadly Tomahawk missile strike.

Handala was one of several Iran-linked hacker groups recently [profiled](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2026/) by **Palo Alto Networks**, which links it to Iran’s **Ministry of Intelligence and Security** (MOIS). Palo Alto says Handala surfaced in late 2023 and is assessed as one of several online personas maintained by [Void Manticore](https://malpedia.caad.fkie.fraunhofer.de/actor/void_manticore), a MOIS-affiliated actor.

Stryker’s website says the company has 56,000 employees in 61 countries. A phone call placed Wednesday morning to the media line at Stryker’s Michigan headquarters sent this author to a voicemail message that stated, “We are currently experiencing a building emergency. Please try your call again later.”

A [report](https://www.irishexaminer.com/news/munster/arid-41808308.html) Wednesday morning from the **Irish Examiner** said Stryker staff are now communicating via WhatsApp for any updates on when they can return to work. The story quoted an unnamed employee saying anything connected to the network is down, and that “anyone with Microsoft Outlook on their personal phones had their devices wiped.”

“Multiple sources have said that systems in the Cork headquarters have been ‘shut down’ and that Stryker devices held by employees have been wiped out,” the Examiner reported. “The login pages coming up on these devices have been defaced with the Handala logo.”

Wiper attacks usually involve malicious software designed to overwrite any existing data on infected devices. But a trusted source with knowledge of the attack who spoke on condition of anonymity told KrebsOnSecurity the perpetrators in this case appear to have used a Microsoft service called **Microsoft Intune** to issue a ‘remote wipe’ command against all connected devices.

Intune is a cloud-based solution built for IT teams to enforce security and data compliance policies, and it provides a single, web-based administrative console to monitor and control devices regardless of location. The Intune connection is supported by [this Reddit discussion](https://www.reddit.com/r/cybersecurity/comments/1rqopq0/stryker_hit_by_handala_intune_managed_devices/) on the Stryker outage, where several users who claimed to be Stryker employees said they were told to uninstall Intune urgently.

Palo Alto says Handala’s hack-and-leak activity is primarily focused on Israel, with occasional targeting outside that scope when it serves a specific agenda. The security firm said Handala also has taken credit for recent attacks against fuel systems in Jordan and an Israeli energy exploration company.

“Recent observed activities are opportunistic and ‘quick and dirty,’ with a noticeable focus on supply-chain footholds (e.g., IT/service providers) to reach downstream victims, followed by ‘proof’ posts to amplify credibility and intimidate targets,” Palo Alto researchers wrote.

The Handala manifesto posted to Telegram referred to Stryker as a “Zionist-rooted corporation,” which may be a reference to the company’s 2019 acquisition of the Israeli company OrthoSpace.

Stryker is a major supplier of medical devices, and the ongoing attack is already affecting healthcare providers. One healthcare professional at a major university medical system in the United States told KrebsOnSecurity they are currently unable to order surgical supplies that they normally source through Stryker.

“This is a real-world supply chain attack,” the expert said, who asked to remain anonymous because they were not authorized to speak to the press. “Pretty much every hospital in the U.S. that performs surgeries uses their supplies.”

**John Riggi**, national advisor for the **American Hospital Association** (AHA), said the AHA is not aware of any supply-chain disruptions as of yet.

“We are aware of reports of the cyber attack against Stryker and are actively exchanging information with the hospital field and the federal government to understand the nature of the threat and assess any impact to hospital operations,” Riggi said in an email. “As of this time, we are not aware of any direct impacts or disruptions to U.S. hospitals as a result of this attack. That may change as hospitals evaluate services, technology and supply chain related to Stryker and if the duration of the attack extends.”

This is a developing story. Updates will be noted with a timestamp.

**Update, 2:54 p.m. ET:** Added comment from Riggi and perspectives on this attack’s potential to turn into a supply-chain problem for the healthcare system.

*This entry was posted on Wednesday 11th of March 2026 12:20 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Ne'er-Do-Well News](https://krebsonsecurity.com/category/neer-do-well-news/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/)

[Handala](https://krebsonsecurity.com/tag/handala/) [Handala Hack](https://krebsonsecurity.com/tag/handala-hack/) [Irish Examiner](https://krebsonsecurity.com/tag/irish-examiner/) [Microsoft Intune](https://krebsonsecurity.com/tag/microsoft-intune/) [Ministry of Intelligence and Security](https://krebsonsecurity.com/tag/ministry-of-intelligence-and-security/) [Palo Alto Networks](https://krebsonsecurity.com/tag/palo-alto-...