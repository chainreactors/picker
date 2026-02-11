---
title: North Korean hackers targeted crypto exec with fake Zoom meeting, ClickFix scam
url: https://therecord.media/north-korean-hackers-targeted-crypto-exec-clickfix
source: Over Security - Cybersecurity news aggregator
date: 2026-02-10
fetch_date: 2026-02-11T04:24:08.539241
---

# North Korean hackers targeted crypto exec with fake Zoom meeting, ClickFix scam

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![cryptocurrency](https://cms.therecord.media/uploads/format_webp/large_cryptocurrency_1_b013f7a9a6.jpg)

Image: Alex Shouper via Unsplash+

[Jonathan Greig](/author/jonathan-greig)February 10th, 2026

# North Korean hackers targeted crypto exec with fake Zoom meeting, ClickFix scam

North Korean hackers targeted an official at a cryptocurrency company with several unique pieces of malware deployed alongside multiple scams, including a fake Zoom meeting, according to a new report from incident responders.

Google-owned Mandiant published a detailed examination of a recent attack involving UNC1069 — a financially-motivated threat actor based in North Korea — that stood out due to how tailored and targeted it was to the victim.

The hackers initially contacted the victim through Telegram using the compromised account of another cryptocurrency executive. The victim was sent a Calendly link for a 30-minute meeting that contained a Zoom meeting link.

“The victim reported that during the call, they were presented with a video of a CEO from another cryptocurrency company that appeared to be a deepfake,” Mandiant [explained](https://cloud.google.com/blog/topics/threat-intelligence/unc1069-targets-cryptocurrency-ai-social-engineering?e=48754805).

“While Mandiant was unable to recover forensic evidence to independently verify the use of AI models in this specific instance, the reported ruse is similar to a previously publicly reported [incident](https://x.com/0xryankim/status/1927630589718573065) with similar characteristics, where deepfakes were also allegedly used.”

When the victim was in the meeting, the hackers claimed there were audio issues — prompting them to ask the victim to take several actions on their device to allegedly resolve them. The issues were a ruse to cover for a [ClickFix attack](https://therecord.media/russian-hackers-europe-hospitality-blue-screen) — a technique where hackers install malware on a device by having the victim try to resolve fictitious technical issues.

In this case, the victim was directed to a web page with troubleshooting directions for both macOS systems and Windows systems. Embedded in the string of commands was one line that kicked off the infection chain.

The victim followed the troubleshooting commands and their macOS device was infected.

The first malicious files, which Mandiant called WAVESHAPER and HYPERCALL, are backdoors that allowed the hackers to install other tools that expanded their foothold on the victim’s device.

Mandiant said it found two different data miners used by the threat actors called DEEPBREATH and CHROMEPUSH. DEEPBREATH enabled the hackers to steal credentials, browser data, user data from Telegram and other data from Apple Notes. The malware compresses all of the information into a ZIP archive and exfiltrates it to a remote server.

CHROMEPUSH is a malicious tool made to look like a harmless browser extension for editing Google Docs offline. But the tool actually records keystrokes, trackers usernames and passwords, steals browser cookies and more.

The incident responders noted that this attack involved an “unusually large amount of tooling dropped onto a single host targeting a single individual” — leading them to believe it was a specified attack designed to steal as much information as possible.

They said it was likely for a dual purpose: “enabling cryptocurrency theft and fueling future social engineering campaigns by leveraging the victim’s identity and data.”

Mandiant said it has been tracking UNC1069 since 2018 and has seen marked evolutions in its tradecraft since then — particularly in its recent targeting of centralized exchanges, software developers at financial institutions, high-technology companies, and individuals at venture capital funds.

“While UNC1069 has had a smaller impact on cryptocurrency heists compared to other groups like UNC4899 in 2025, it remains an active threat targeting centralized exchanges and both entities and individuals for financial gain,” Mandiant explained.

“Mandiant has observed this group active in 2025 targeting the financial services and the cryptocurrency industry in payments, brokerage, staking, and wallet infrastructure verticals.”

UNC1069 has used fake Zoom meetings and a variety of AI tools in its attacks on corporate entities as well as people in the cryptocurrency industry. Mandiant says it has seen the North Korean group use Google’s Gemini AI tool to do operational research, develop tools and more.

At the United Nations last month, U.S. officials [said](https://therecord.media/40-countries-impacted-nk-it-thefts-united-nations) dozens of countries had dealt with crypto thefts perpetrated by North Korean hackers. The country is accused of stealing [more than $2 billion](https://therecord.media/over-3-billion-crypto-stolen-2025-north-korea) in crypto in 2025.

* [Cybercrime](/romania-conpet-oil-pipeline-ransomware-attack)
* [News](/)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

Tags

* [cryptocurrency scam](/tag/cryptocurrency-scam)
* [North Korea](/tag/north-korea)
* [Mandiant](/tag/mandiant)
* [Zoom](/)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/format_webp/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [Cyber Command, NSA nominee Rudd advances to Senate floorFebruary 10th, 2026](/cyber-command-nsa-nominee-rudd-advances-to-senate)
* [Senegal confirms breach of national ID card department after ransomware claimsFebruary 9th, 2026](/senegal-breach-national-id-agency)
* [Payment tech provider for Texas, Florida governments working with FBI to resolve ransomware attackFebruary 9th, 2026](/payment-tech-provider-texas-florida-govs-ransomware-attack)
* [EU, Dutch government announce hacks following Ivanti zero-daysFebruary 9th, 2026](/eu-dutch-government-announce-hacks-ivanti-zero-days)
* [NYC explores using AI cameras to spot subway fare evadersFebruary 6th, 2026](/nyc-explores-ai-cameras-fare-evaders-subway)
* [EU threatens TikTok with massive fine over addictive design featuresFebruary 6th, 2026](/eu-threatens-tiktok-with-fine-over-addictive-features)
* [Romania’s oil pipeline operator confirms cyberattack as hackers claim data theftFebruary 6th, 2026](/romania-conpet-oil-pipeline-ransomware-attack)
* [Substack warns customers of data breach following hacker’s dark web claimsFebruary 5th, 2026](/substack-data-breach-notification)
* [CISA official says CIRCIA cyber reporting update is 'weeks' awayFebruary 3rd, 2026](/cisa-pfficial-says-circia-update-weeks-away)

[## Rublevka Team: Anatomy of a Russian Crypto Drainer Operation

![Rublevka Team: Anatomy of a Russi...