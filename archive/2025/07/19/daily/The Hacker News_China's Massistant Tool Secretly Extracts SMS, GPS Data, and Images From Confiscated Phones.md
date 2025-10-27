---
title: China's Massistant Tool Secretly Extracts SMS, GPS Data, and Images From Confiscated Phones
url: https://thehackernews.com/2025/07/chinas-massistant-tool-secretly.html
source: The Hacker News
date: 2025-07-19
fetch_date: 2025-10-06T23:54:46.180973
---

# China's Massistant Tool Secretly Extracts SMS, GPS Data, and Images From Confiscated Phones

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [China's Massistant Tool Secretly Extracts SMS, GPS Data, and Images From Confiscated Phones](https://thehackernews.com/2025/07/chinas-massistant-tool-secretly.html)

**Jul 18, 2025**Ravie LakshmananSurveillance / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMNrY4KHce1zEXAZWjys6EupGOJ9Kw_WWouGqMxDTpIKdNgKOc607rTnxxG_laaKZJlqTpI6nOLitjQ7IerDikommqFUv3_FrbajPFDOjGYxnZsBOIXLi__Kg194hOjI8SzRxzDOySxAcK4JNrHi7oTs96ikVaso-EkEiC9ZARxnFaLaK3erUN-GzsPhRf/s790-rw-e365/phone-china-hacking.jpg)

Cybersecurity researchers have shed light on a mobile forensics tool called **Massistant** that's used by law enforcement authorities in China to gather information from seized mobile devices.

The hacking tool, believed to be a successor of [MFSocket](https://medium.com/%40fs0c131y/mfsocket-a-chinese-surveillance-tool-58e8850c3de4), is developed by a Chinese company named [SDIC Intelligence Xiamen Information Co., Ltd.](https://www.reuters.com/markets/companies/300188.SZ/), which was formerly known as Meiya Pico. It [specializes](https://web.archive.org/web/20250324193852/https%3A//www.300188.cn/solution/detail/5.html#nav_s) in the research, development, and sale of electronic data forensics and network information security technology products.

According to a report published by Lookout, Massistant works in conjunction with a corresponding desktop software, allowing for access to the device's GPS location data, SMS messages, images, audio, contacts, and phone services.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Meiya Pico maintains partnerships with domestic and international law enforcement partners, both as a surveillance hardware and software provider, as well as through training programs for law enforcement personnel," security researcher Kristina Balaam [said](https://www.lookout.com/threat-intelligence/article/massistant-chinese-mobile-forensics).

Massistant requires physical access to the device in order to install the application, meaning it can be used to collect data from confiscated devices from individuals when stopped at border checkpoints.

Lookout said it obtained Massistant samples between mid-2019 and early 2023 and that they were signed with an Android signing certificate referencing Meiya Pico.

Both Massistant and its predecessor, [MFSocket](https://www.ft.com/content/73aebaaa-98a9-11e9-8cfb-30c211dcd229), work similarly in that they need to be connected to a desktop computer running forensics software to extract the data from the device. Once launched on the phone, the tool prompts the users to grant it permissions to access sensitive data, after which no further interaction is required.

"If the user attempts to exit the application they receive a notice that the application is in 'get data' mode and exiting would result in some error," Balaam explained. "This message is translated to only two languages: Chinese (Simplified characters) and 'US' English."

The application is designed such that it's automatically uninstalled from the device when it is disconnected from a USB. Massistant also expands on MFSocket's features by including the ability to connect to a phone using the Android Debug Bridge (ADB) over Wi-Fi and to download additional files to the device.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfB6wIk3fTYUEIAZ-SUkUOxMH35ILe3QbAQIRV2zNEf9y5H0gNuohPPfzypCX9kFRqxqekpOrza-7FnrGqsNVaMycMxiZtPA2_aeJX_jREUbuzU2sBaCJdr-HuUYH6ZJx73JclA0I44T5J1ng1oA39HeHx9Gpa0SxMaH9SRhxYfumqIjzzzQBn0WjmaNZV/s790-rw-e365/phone.jpg)

Another new functionality incorporated into Massistant is to collect data from third-party messaging apps beyond Telegram to include Signal and Letstalk, a Taiwanese chat application with more than 100,000 downloads on Android.

While Lookout's analysis focuses mainly on the Android version of Massistant, images shared on its website [show](https://web.archive.org/web/20250716124836/https%3A//300188.cn/news/detail/402.html) iPhones connected to its forensic hardware device, suggesting that there is an iOS equivalent to pull data from Apple devices.

The fact that Meiya Pico may also be focused on iOS devices stems from the [various patents](https://patents.google.com/?assignee=Meiya+Pico) filed by the company related to gathering evidence from Android and iOS devices, including voiceprints for internet-related cases.

"Voiceprint features are one of the important biological features of the human body, and can uniquely determine the identity of a user," [according](https://patents.google.com/patent/CN116206611A/en) to one patent. "After the voiceprint library is built, a plurality of police seeds can be directly served, and the efficiency and the capability of detecting and solving a case of a related organization can be effectively improved."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The digital forensics firm's involvement in the [surveillance space](https://www.scmp.com/tech/start-ups/article/3017688/what-you-need-know-about-meiya-pico-chinas-low-profile-forensics) is not new. In December 2017, The Wall Street Journal [reported](https://www.wsj.com/articles/twelve-days-in-xinjiang-how-chinas-surveillance-state-overwhelms-daily-life-1513700355) that the company worked with police officials in Ürümqi, the capital of Xinjiang Uyghur Autonomous Region in Northwestern China, to scan smartphones for terrorism-related content by plugging them into a handheld device.

Four years later, the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC) [sanctioned](https://home.treasury.gov/news/press-releases/jy0538) Meiya Pico for enabling the "biometric surveillance and tracking of ethnic and religious minorities in China, particularly the predominantly Muslim Uyghur minority in Xinjiang."

"Travel to and within mainland China carries with it the potential for tourists, business travelers, ...