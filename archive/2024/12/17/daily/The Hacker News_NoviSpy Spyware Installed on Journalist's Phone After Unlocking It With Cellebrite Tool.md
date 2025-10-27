---
title: NoviSpy Spyware Installed on Journalist's Phone After Unlocking It With Cellebrite Tool
url: https://thehackernews.com/2024/12/novispy-spyware-installed-on.html
source: The Hacker News
date: 2024-12-17
fetch_date: 2025-10-06T19:42:56.126660
---

# NoviSpy Spyware Installed on Journalist's Phone After Unlocking It With Cellebrite Tool

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

# [NoviSpy Spyware Installed on Journalist's Phone After Unlocking It With Cellebrite Tool](https://thehackernews.com/2024/12/novispy-spyware-installed-on.html)

**Dec 16, 2024**Ravie LakshmananSpyware / Surveillance

[![NoviSpy Spyware](data:image/png;base64... "NoviSpy Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_2TkY3EkWwGy-ZDFhCeo3o3ohyphenhyphenfdPPvRZc-8Oey9ynOCgVjRDcDdp5nTJPabnz5qW5DGuZv-jeRdoTT6WTDFY1W_5eYlDFn24y8v44qr4fh1PG7m5eFJpSx8bpGYkyotmR5lg9fomrr23KrzhCYNo0Pwc0ZwWKZIVHcw96XpC_J32I76ouROQ7NUxGVL4/s790-rw-e365/spyware.png)

A Serbian journalist had his phone first unlocked by a Cellebrite tool and subsequently compromised by a previously undocumented spyware codenamed **NoviSpy**, according to a new report published by Amnesty International.

"NoviSpy allows for capturing sensitive personal data from a target's phone after infection and provides the ability to turn on the phone's microphone or camera remotely," the company [said](https://securitylab.amnesty.org/latest/2024/12/a-digital-prison-surveillance-and-the-suppression-of-civil-society-in-serbia/) in an 87-page technical report.

An analysis of forensic evidence points to the spyware installation occurring when the phone belonging to independent journalist Slaviša Milanov was in the hands of the Serbian police during his detention in early 2024.

Some of the other targets included youth activist Nikola Ristić, environmental activist Ivan Milosavljević Buki, and an unnamed activist from Krokodil, a Belgrade-based organization promoting dialogue and reconciliation in the Western Balkans.

The development marks one of the first known instances where two disparate highly invasive technologies were used in combination to facilitate snooping and the exfiltration of sensitive data.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

NoviSpy, in particular, is engineered to harvest various kinds of information from compromised phones, including screenshots of all actions on the phone, targets' locations, audio and microphone recordings, files, and photos. It's installed using the Android Debug Bridge ([adb](https://developer.android.com/tools/adb)) command-line utility and manifests in the form of two applications -

* **NoviSpyAdmin** (com.serv.services), which requests extensive permissions to collect call logs, SMS messages, contact lists, and record audio through the microphone
* **NoviSpyAccess** (com.accesibilityservice), which abuses Android's [accessibility services](https://thehackernews.com/2024/12/this-3000-android-trojan-targeting.html) to stealthily collect screenshots from email accounts and messaging apps like Signal and WhatsApp, exfiltrate files, track location, and activate camera

Exactly who developed NoviSpy is currently not known, although Amnesty [told](https://www.404media.co/cellebrite-unlocked-this-journalists-phone-cops-then-infected-it-with-malware/) 404 Media that it could have either been built in-house by Serbian authorities or acquired from a third-party. Development of the spyware is said to have been ongoing since at least 2018.

"Together, these tools provide the state with an enormous capability to gather data both covertly, as in the case of spyware, and overtly, through the unlawful and illegitimate use of Cellebrite mobile phone extraction technology," Amnesty International noted.

The non-governmental organization further noted that the Serbian Security Information Agency (BIA) has been publicly linked to the procurement of spyware tools since at least 2014, using various offerings such as FinFisher's [FinSpy](https://thehackernews.com/2020/10/finfisher-spyware-raid.html), Intellexa's [Predator](https://thehackernews.com/2024/09/us-treasury-sanctions-executives-linked.html), and NSO Group's [Pegasus](https://thehackernews.com/2024/11/nso-group-exploited-whatsapp-to-install.html) to covertly spy on protest organizers, journalists and civil society leaders.

In a [statement](https://apnews.com/article/serbia-amnesty-spying-protests-d35744f1fb9282aed8618934748dc93b) shared with the Associated Press, Serbia's police characterized the report as "absolutely incorrect" and that "the forensic tool is used in the same way by other police forces around the world."

Responding to the findings, Israeli company Cellebrite said it's investigating the claims of misuse of its tools and that it would take appropriate measures, including terminating its relationship with relevant agencies, if they are found to be in violation of its end-user agreement.

In tandem, the research also uncovered a zero-day privilege escalation exploit used by Cellebrite's universal forensic extraction device ([UFED](https://cellebrite.com/en/ufed/)) – a software/system that allows law enforcement agencies to [unlock and gain access to data](https://thenextweb.com/news/ice-is-paying-an-israeli-security-company-30m-to-break-into-phones) stored on mobile phones – to gain elevated access to a Serbian activist's device.

The vulnerability, tracked as [CVE-2024-43047](https://thehackernews.com/2024/10/qualcomm-urges-oems-to-patch-critical.html) (CVSS score: 7.8), is a user-after-free bug in Qualcomm's Digital Signal Processor (DSP) Service (adsprpc) that could lead to "memory corruption while maintaining memory maps of HLOS memory." It was patched by the chipmaker in October 2024.

Google, which initiated a "broader code review process" following the receipt of kernel panic logs generated by the in-the-wild (ITW) exploit earlier this year, said it discovered a total of six vulnerabilities in the adsprpc driver, including CVE-2024-43047.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Chipset drivers for Android are a promising target for attackers, and this ITW exploit represents a meaningful real-world example of the negative ramifications that the current third-party vendor driver security posture poses to end-users," Seth Jenkins of Google Project Zero...