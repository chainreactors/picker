---
title: Google dismantles massive botnet hidden in Android TV boxes
url: https://therecord.media/google-dismantles-botnet-hidden-android-tv-boxes
source: Over Security
date: 2026-11-03
fetch_date: 2026-11-04T08:19:10.146779
---

# Google dismantles massive botnet hidden in Android TV boxes

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

![tv](https://cms.therecord.media/uploads/large_tv_1_8b7fd51044.jpg)

Image: Glenn Carstens Peters via Unsplash

[Jonathan Greig](/author/jonathan-greig)November 3rd, 2026

# Google dismantles massive botnet hidden in Android TV boxes

Google along with several cybersecurity companies and Japanese law enforcement dismantled a global botnet called X.CPE that was hidden in more than 1.3 million set-top boxes across more than 200 countries.

Google [said](https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet) it tied the scheme to Videostrong Technology, a Chinese company that was an Android original equipment manufacturer producing a range of screens, speakers and robots.

The overwhelming majority of the infected devices in the X.CPE botnet are Android TV set-top boxes, Google said, adding that they observed a number of other infected Android-based IoT devices, including telehealth devices, karaoke machines and digital signage devices.

In [lengthy reports](https://synthient.com/blog/the-internals-of-a-badbox-operation) about the scheme, Google and [other cyber investigators](https://cdn.plume.com/3d/92/f7c576bd4afabd79df4e7b39ca7f/xcpe-botnet-whitepaper-10-2026.pdf) accused Videostrong of monetizing the backdoor by “selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices.”

“We found this malicious software built directly into many different device models and brands over multiple years, supported by dedicated infrastructure and constantly evolving configurations to evade detection and manage their affiliates,” Google said.

“We believe this campaign wasn’t an isolated rogue insider or a development oversight. As a result, Google has cut ties with Videostrong and banned them from making devices with preloaded Google apps.”

Videostrong did not respond to requests for comment. The company says it has worked as an original equipment manufacturer for more than 14 years and sells a variety of AI-backed devices.

![Screenshot 2026-11-03 at 12.59.27 PM.png](https://cms.therecord.media/uploads/Screenshot_2026_11_03_at_12_59_27_PM_5e1bdeb323.png)

*Image: Google*

## Millions of households

Google said Videostrong was allegedly turning infected devices into a residential proxy network and loading other types of malware onto X.CPE-compromised devices.

The botnet generated revenue from the devices by reselling bandwidth, data exfiltration, delivering video content, ad fraud, loading additional backdoors and installing apps for payment. The software allowed third-party traffic to pass through a person’s internet connection, using their internet address and bandwidth.

X.CPE was embedded in the device’s firmware before it even reached a person’s home and was built to evade security checks. Videostrong allegedly continued to change the malware used, updating it in 2024 and 2026.

Google worked with Japanese police, as well as cybersecurity firms TrendAI, Human and Synthient, to disrupt the domains that underpinned the botnet.

“Our research identified over 1.3 million devices affected by this campaign,” said Robert McArdle, director of cybercrime research at TrendAI. “That's millions of households and businesses completely unaware that their equipment was being used as an accessory in active criminality — whether defrauding advertisers or piggybacking on their connections to carry out other attacks via residential proxies — which would commonly include identity theft impersonating people in their region.”

According to Google, Videostrong used “obfuscation techniques” to pass its security tests and load the malware onto the devices. Google pledged to change its review process to stop future manufacturers from conducting similar campaigns.

Google said it took legal action to take down the domains Videostrong used to control the botnet and install the malware while also suing to destroy the domains used by other malware families loaded onto the devices.

But they noted that even if a user tried to uninstall the malware, it would automatically reinstall, according to cybersecurity researchers. The backdoor was able to silently download other files onto the device and execute them without user consent.

Google did not explain if customers with infected devices will be notified or if there is any effort to forcibly remove malware from compromised devices as U.S. law enforcement agencies [have done](https://therecord.media/us-disrupts-prolific-botnet-controlled-by-russian-military-doj-says) in other [similar botnet cases](https://therecord.media/china-run-botnet-takedown-fbi-doj-routers).

In response to questions about removing the malware, Charley Snyder, head of disruption operations at Google Threat Intelligence Group, told Recorded Future News that their actions severed the domains the botnet was communicating with, “effectively rendering the malware benign."

Google claimed the takedown of command and control domains of Videostrong's criminal affiliates may have also cut off cybercriminal access to an additional 10 million compromised devices — many of which are not Android devices.

Videostrong and any future subsidiaries are now banned from selling Android devices or supplying software to certified vendors, Google said.

“The x.cpe network was built for ongoing profit. By giving malware affiliates backdoor access, the operators conspired to monetize these devices long after purchase,” Google said. “Since at least late 2024, Videostrong has evolved its pre-installed malware from simple single-stage droppers into a modular, three-stage architecture designed for resilience and multi-tenant monetization.”

Tech companies like Google have increasingly turned to court orders to take down malicious tools or services used to target their customers. Microsoft used court orders multiple times this year to destroy [phishing platforms](https://therecord.media/microsoft-takes-down-3-major-chinese-phishing-platforms), [malicious AI tools](https://therecord.media/two-arrested-in-uk-after-microsoft-takedown-eviltokens), and [cybercrime-as-a-service infrastructure](https://therecord.media/stealc-amadey-socgholish-malware-takedown-europol-microsoft).

* [Cybercrime](/news/cybercrime)
* [News](/ukraine-says-starshield-working-again-after-disruption)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [Largest crypto exchange in Brazil confirms cyberattack as millions flow out of platformNovember 2nd, 2026](/mercado-bitcoin-brazil-cryptocurrency-heist)
* [Michigan State cyber incident claimed by ransomware gang behind recent hospital attackNovemb...