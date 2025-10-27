---
title: Chinese authorities are using a new tool to hack seized phones and extract data
url: https://techcrunch.com/2025/07/16/chinese-authorities-are-using-a-new-tool-to-hack-seized-phones-and-extract-data/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-17
fetch_date: 2025-10-06T23:54:45.941429
---

# Chinese authorities are using a new tool to hack seized phones and extract data

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-lockup.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)
* [Disrupt 2025](https://techcrunch.com/events/tc-disrupt-2025/)

* [Events](/events/)
* [Podcasts](/podcasts/)
* [Newsletters](/newsletters/)

Search

Submit

Site Search Toggle

Mega Menu Toggle

### Topics

[Latest](/latest/)

[AI](/category/artificial-intelligence/)

[Amazon](/tag/amazon/)

[Apps](/category/apps/)

[Biotech & Health](/category/biotech-health/)

[Climate](/category/climate/)

[Cloud Computing](/tag/cloud-computing/)

[Commerce](/category/commerce/)

[Crypto](/category/cryptocurrency/)

[Enterprise](/category/enterprise/)

[EVs](/tag/evs/)

[Fintech](/category/fintech/)

[Fundraising](/category/fundraising/)

[Gadgets](/category/gadgets/)

[Gaming](/category/gaming/)

[Google](/tag/google/)

[Government & Policy](/category/government-policy/)

[Hardware](/category/hardware/)

[Instagram](/tag/instagram/)

[Layoffs](/tag/layoffs/)

[Media & Entertainment](/category/media-entertainment/)

[Meta](/tag/meta/)

[Microsoft](/tag/microsoft/)

[Privacy](/category/privacy/)

[Robotics](/category/robotics/)

[Security](/category/security/)

[Social](/category/social/)

[Space](/category/space/)

[Startups](/category/startups/)

[TikTok](/tag/tiktok/)

[Transportation](/category/transportation/)

[Venture](/category/venture/)

### More from TechCrunch

[Staff](/about-techcrunch/)

[Events](/events/)

[Startup Battlefield](/startup-battlefield/)

[StrictlyVC](https://strictlyvc.com/)

[Newsletters](/newsletters/)

[Podcasts](/podcasts/)

[Videos](/video/)

[Partner Content](/sponsored/)

[TechCrunch Brand Studio](/brand-studio/)

[Crunchboard](https://www.crunchboard.com/)

[Contact Us](/contact-us/)

![A border police officer answers questions from inbound passengers at Chongqing Jiangbei International Airport in southwest China's Chongqing, July 8, 2025.](https://techcrunch.com/wp-content/uploads/2025/07/china-border-crossing-check.jpg?w=1024)

**Image Credits:**Huang Wei/Xinhua / Getty Images

[Security](https://techcrunch.com/category/security/)

# Chinese authorities are using a new tool to hack seized phones and extract data

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

3:00 AM PDT · July 16, 2025

Security researchers say Chinese authorities are using a new type of malware to extract data from seized phones, allowing them to obtain text messages — including from chat apps such as Signal — images, location histories, audio recordings, contacts, and more.

[In a report](https://www.lookout.com/threat-intelligence/article/massistant-chinese-mobile-forensics) shared exclusively with TechCrunch, mobile cybersecurity company Lookout detailed the hacking tool called Massistant, which the company said was developed by Chinese tech giant Xiamen Meiya Pico.

Massistant, [according to Lookout](https://www.lookout.com/threat-intelligence/article/massistant-chinese-mobile-forensics), is Android software used for the forensic extraction of data from mobile phones, meaning the authorities using it need to have physical access to those devices. While Lookout doesn’t know for sure which Chinese police agencies are using the tool, its use is assumed widespread, which means Chinese residents, as well as travelers to China, should be aware of the tool’s existence and the risks it poses.

“It’s a big concern. I think anybody who’s traveling in the region needs to be aware that the device that they bring into the country could very well be confiscated and anything that’s on it could be collected,” Kristina Balaam, a researcher at Lookout who analyzed the malware, told TechCrunch ahead of the report’s release. “I think it’s something everybody should be aware of if they’re traveling in the region.”

Balaam found several posts on local Chinese forums where people complained about finding the malware installed on their devices after interactions with the police.

“It seems to be pretty broadly used, especially from what I’ve seen in the rumblings on these Chinese forums,” said Balaam.

The malware must be planted on an unlocked device, and works in tandem with a hardware tower connected to a desktop computer, according to a description and pictures of the system [on Xiamen Meiya Pico’s website](https://300188-cn.translate.goog/news/detail/402.html?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp).

Balaam said Lookout couldn’t analyze the desktop component, nor could the researchers find a version of the malware compatible with Apple devices. In an illustration on its website, Xiamen Meiya Pico shows iPhones connected to its forensic hardware device, suggesting the company may have an iOS version of Massistant designed to extract data from Apple devices.

Police do not need sophisticated techniques to use Massistant, such as using [zero-days](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#zero-day) — flaws in software or hardware that have not yet been disclosed to the vendor — as “people just hand over their phones,” said Balaam, based on what she’s read on those Chinese forums.

Since at least 2024, [China’s state security police](https://www.rfa.org/english/news/china/security-police-check-devices-05082024130107.html) have had legal powers to search through phones and computers without needing a warrant or the existence of an active criminal investigation.

“If somebody is moving through a border checkpoint and their device is confiscated, they have to grant access to it,” said Balaam. “I don’t think we see any real exploits from lawful intercept tooling space just because they don’t need to.”

![An Massistant device showing a tower computer plugged into several iPhones.](https://techcrunch.com/wp-content/uploads/2025/07/whz27x4909.jpeg)

A screenshot of the Massistant mobile forensic tool’s hardware, taken from Xiamen Meiya Pico’s official Chinese website**Image Credits:**Xiamen Meiya Pico

The good news, per Balaam, is that Massistant leaves evidence of its compromise on the seized device, meaning users can potentially identify and delete the malware, either because the hacking tool appears as an app, or can be found and deleted using more sophisticated tools such as the [Android Debug Bridge](http://developer.android.com/tools/adb), a command line tool that lets a user connect to a device through their computer.

The bad news is that at the time of installing Massistant, the damage is done, and authorities already have the person’s data.

According to Lookout, Massistant is the successor of a similar mobile forensic tool, also made by Xiamen Meiya Pico, called [MSSocket](https://www.ft.com/content/73aebaaa-98a9-11e9-8cfb-30c211dcd229), which security researchers [analyzed](https://medium.com/%40fs0c131y/mfsocket-a-chinese-surveillance-tool-58e8850c3de4) in 2019.

Xiamen Meiya Pico reportedly has a 40% share of the digital forensics market in China, and [was sanctioned by the U.S. government in 2021](http://ofac.treasury.gov/recent-actions/20211216) for its role in supplying its technology to the Chinese government.

The company did not respond to TechCrunch’s request for comment.

Balaam said that Massistant is only one of a large number of spyware or malware made by Chinese surveillance tech makers, in what she called “a big ecosystem.” The researcher said that the company tracks at least 15 different malware families in China.

Topics

[Android](https://techcrunch.com/tag/android/), [China](https://techcrunch.com/tag/china/), [cybersecurity](https://techcrunch.com/tag/cybersecurity/), [Exclusive](https://techcru...