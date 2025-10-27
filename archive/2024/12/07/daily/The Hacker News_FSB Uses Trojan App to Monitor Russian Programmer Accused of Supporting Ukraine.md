---
title: FSB Uses Trojan App to Monitor Russian Programmer Accused of Supporting Ukraine
url: https://thehackernews.com/2024/12/fsb-uses-trojan-app-to-monitor-russian.html
source: The Hacker News
date: 2024-12-07
fetch_date: 2025-10-06T19:59:26.124928
---

# FSB Uses Trojan App to Monitor Russian Programmer Accused of Supporting Ukraine

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

# [FSB Uses Trojan App to Monitor Russian Programmer Accused of Supporting Ukraine](https://thehackernews.com/2024/12/fsb-uses-trojan-app-to-monitor-russian.html)

**Dec 06, 2024**Ravie LakshmananSpyware / Mobile Security

[![Russian Programmer](data:image/png;base64... "Russian Programmer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqJ75gjpg8k9dVxTKKsF6qYQzR4IDldFkYCQzUErYTicEA7XHnTiIAFYj-7LQpvnVVRlHUAFwPqOxoe6W4x2dm5h2yRkKNaoNbqu3_Ciei3VitMgxBHQzeNTdBou62tijV1CJmipKBnBiQfIgmEi3J4h3HL9D2grw1IuTTIjyIJrV1t8u0nZ3JuSVZEO8M/s790-rw-e365/programmer.png)

A Russian programmer accused of donating money to Ukraine had his Android device secretly implanted with spyware by the Federal Security Service (FSB) after he was detained earlier this year.

The findings come as part of a collaborative investigation by [First Department](https://dept.one/story/parubets/) and the University of Toronto's [Citizen Lab](https://citizenlab.ca/2024/12/device-confiscated-by-russian-authorities-returned-with-monokle-type-spyware-installed/).

"The spyware placed on his device allows the operator to track a target device's location, record phone calls, keystrokes, and read messages from encrypted messaging apps, among other capabilities," according to the report.

In May 2024, Kirill Parubets was [released](https://cyberscoop.com/russian-surveillance-spyware-threat-citizen-lab/) from custody after a 15-day period in administrative detention by Russian authorities, during which time his phone, an Oukitel WP7 phone running Android 10, was confiscated from him.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

During this period, not only was he beaten to compel him into revealing his device password, he was also subjected to an "intense effort" to recruit him as an informant for the FSB, or else risk facing life imprisonment.

After agreeing to work for the agency, if only to buy some time and get away, the FSB returned his device at its Lubyanka headquarters. It's at this stage that Parubets began noticing that the phone exhibited unusual behavior, including a notification that said "Arm cortex vx3 synchronization."

A further examination of the Android device has since revealed that it was indeed tampered with a trojanized version of the genuine [Cube Call Recorder](https://play.google.com/store/apps/details?id=com.catalinagroup.callrecorder&hl=en_US) application. It's worth noting that the legitimate app has the package name "com.catalinagroup.callrecorder," whereas the [rogue counterpart's](https://www.virustotal.com/gui/file/737f60749c1919ad22102be27d52ba199ec4b707a985c42011b22ce0a4512c90/details) package name is "com.cortex.arm.vx3."

The counterfeit app is designed to request intrusive permissions that allow it to gather a wide range of data, including SMS messages, calendars, install additional packages, and answer phone calls. It can also access fine location, record phone calls, and read contact lists, all functions that are part of the legitimate app.

"Most of the malicious functionality of the application is hidden in an encrypted second stage of the spyware," the Citizen Lab said. "Once the spyware is loaded onto the phone and executed, the second stage is decrypted and loaded into memory."

[![Russian Programmer](data:image/png;base64... "Russian Programmer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxoKBVH9_s5Rp5k09V-R5IOV9zetGOZZ4n5E7Aocet5bLQFN1zLsUYbg727-s9m2lFUWhHb97zIKWtpVQAodhmgpbkWY1pAP28AAvVA6ds4RHXadufQjqKDnd-7nVHVUsftUe1UTWAx0UM_8SYmxDyn6YL1QdCgSkCBUD66Jl4K1XJzoA6OhoCdaez9TFo/s790-rw-e365/malware.png)

The second stage incorporates features to log keystrokes, extract files and stored passwords, read chats from other messaging apps, inject JavaScript, execute shell commands, obtain the device unlock password, and even add a new device administrator.

The spyware also exhibits some level of overlap with another Android spyware called [Monokle](https://thehackernews.com/2019/07/russian-android-spying-apps.html) that was documented by Lookout in 2019, raising the possibility that it's either an updated version or that it's been built by reusing Monokle's codebase. Specifically, some of the command-and-control (C2) instructions between the two strains have been found to be identical.

The Citizen Lab said it also spotted references to iOS in the source code, suggesting that there could be an iOS version of the spyware.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This case illustrates that the loss of physical custody of a device to a hostile security service like the FSB can be a severe risk for compromise that will extend beyond the period where the security services have custody of the device," it said.

The disclosure comes as iVerify said it discovered seven new [Pegasus](https://thehackernews.com/2024/11/nso-group-exploited-whatsapp-to-install.html) spyware infections on iOS and Android devices belonging to journalists, government officials, and corporate executives. The mobile security firm is tracking the spyware developer, NSO Group, as Rainbow Ronin.

"One exploit from late 2023 on iOS 16.6, another potential Pegasus infection in November 2022 on iOS 15, and five older infections dating back to 2021 and 2022 across iOS 14 and 15," security researcher Matthias Frielingsdorf [said](https://iverify.io/blog/iverify-mobile-threat-investigation-uncovers-new-pegasus-samples). "Each of these represented a device that could have been silently monitored, its data compromised without the owner's knowledge."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share...