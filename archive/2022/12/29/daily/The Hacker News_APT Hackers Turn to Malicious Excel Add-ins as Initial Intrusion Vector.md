---
title: APT Hackers Turn to Malicious Excel Add-ins as Initial Intrusion Vector
url: https://thehackernews.com/2022/12/apt-hackers-turn-to-malicious-excel-add.html
source: The Hacker News
date: 2022-12-29
fetch_date: 2025-10-04T02:42:12.735856
---

# APT Hackers Turn to Malicious Excel Add-ins as Initial Intrusion Vector

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

# [APT Hackers Turn to Malicious Excel Add-ins as Initial Intrusion Vector](https://thehackernews.com/2022/12/apt-hackers-turn-to-malicious-excel-add.html)

**Dec 28, 2022**Ravie LakshmananMalware / Windows Security

[![Malicious Excel Add-ins](data:image/png;base64... "Malicious Excel Add-ins")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdwpNONhOXqfIJMC7x-JbFNWf2lqEvq0BTe-YvdoR_3jCNmbjF9HaPh8i1ML8TqMUoHbWVp9rNYQrZZs4dhBbtvPfmz5WKUgN6MDk9985ZFCUTGCbycYRmwguthyH76aDZPGB298TTmZZidMm7Jm8jyfvV8dukqB1FJasUbEuyLjITtvY5_Swvidr3/s790-rw-e365/VBA.png)

Microsoft's decision to [block](https://thehackernews.com/2022/07/microsoft-resumes-blocking-office-vba.html) Visual Basic for Applications (VBA) macros by default for Office files downloaded from the internet has led many threat actors to improvise their attack chains in recent months.

Now according to [Cisco Talos](https://blog.talosintelligence.com/xlling-in-excel-malicious-add-ins/), advanced persistent threat (APT) actors and commodity malware families alike are increasingly using Excel add-in (.XLL) files as an initial intrusion vector.

Weaponized Office documents delivered via spear-phishing emails and other social engineering attacks have remained one of the widely used entry points for criminal groups looking to execute malicious code.

These documents traditionally prompt the victims to enable macros to view seemingly innocuous content, only to activate the execution of malware stealthily in the background.

To counter this misuse, the Windows maker [enacted a crucial change](https://thehackernews.com/2022/07/microsoft-resumes-blocking-office-vba.html) starting in July 2022 that [blocks macros](https://learn.microsoft.com/en-gb/DeployOffice/security/internet-macros-blocked) in Office files attached to email messages, effectively severing a crucial attack vector.

While this blockade only applies to new versions of Access, Excel, PowerPoint, Visio, and Word, bad actors have been [experimenting](https://thehackernews.com/2022/04/emotet-testing-new-delivery-ideas-after.html) with [alternative infection routes](https://thehackernews.com/2022/07/hackers-opting-new-attack-methods-after.html) to deploy malware.

One such method turns out to be [XLL files](https://learn.microsoft.com/en-us/office/dev/add-ins/excel/make-custom-functions-compatible-with-xll-udf), which is described by Microsoft as a "type of dynamic link library (DLL) file that can only be opened by Excel."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"XLL files can be sent by email, and even with the usual anti-malware scanning measures, users may be able to open them not knowing that they may contain malicious code," Cisco Talos researcher Vanja Svajcer said in an analysis published last week.

The cybersecurity firm said threat actors are employing a mix of native add-ins written in C++ as well as those developed using a free tool called Excel-DNA, a phenomenon that has witnessed a significant spike since mid-2021 and continued to this year.

That said, the first publicly documented malicious use of XLL is said to have occurred in 2017 when the China-linked [APT10](https://thehackernews.com/2022/11/chinese-hackers-using-new-stealthy.html) (aka Stone Panda) actor utilized the technique to inject its backdoor payload into memory via [process hollowing](https://attack.mitre.org/techniques/T1055/012/).

[![Initial Intrusion Vector](data:image/png;base64... "Initial Intrusion Vector")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLoMBM0rPpYyVLK3Yjs__NCqfKlF3nZTYpiKHG5jGP-bHd1JoAZ61nVx5yoNTxTRptEzcGUx8OBc9xQ_bSBHJz9aOnLV4IMdedHq9IFCpTCfM5cXcM9HPRO6izC7SXwhocl9W7Mdwjf-8gFv-NBDUhn0zp33FC0k5rKxBK6r-e7Wx7Xuj2sczeZfF_/s790-rw-e365/VBA.png)

Since then, a number of other adversarial collectives have followed its footsteps, including [TA410](https://thehackernews.com/2022/09/cyber-attacks-against-middle-east.html) (an actor with links to APT10), [DoNot Team](https://thehackernews.com/2022/08/donot-team-hackers-updated-its-malware.html), [FIN7](https://thehackernews.com/2022/12/fin7-cybercrime-syndicate-emerges-as.html), as well as commodity malware families such as [Agent Tesla](https://thehackernews.com/2022/09/researchers-detail-originlogger-rat.html), [Arkei](https://thehackernews.com/2022/12/privateloader-ppi-service-found.html), [Buer](https://thehackernews.com/2021/05/a-new-buer-malware-variant-has-been.html), [Dridex](https://thehackernews.com/2022/06/rig-exploit-kit-now-infects-victims-pcs.html), [Ducktail](https://thehackernews.com/2022/11/ducktail-malware-operation-evolves-with.html), [Ekipa RAT](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/malicious-macros-adapt-to-use-microsoft-publisher-to-push-ekipa-rat/), [FormBook](https://thehackernews.com/2022/06/new-xloader-botnet-version-using.html), [IcedID](https://thehackernews.com/2022/11/notorious-emotet-malware-returns-with.html), [Vidar Stealer](https://thehackernews.com/2022/05/hackers-trick-users-with-fake-windows.html), and [Warzone RAT](https://thehackernews.com/2022/09/russian-sandworm-hackers-impersonate.html).

The abuse of the XLL file format to distribute [Agent Tesla](https://unit42.paloaltonetworks.com/excel-add-ins-malicious-xll-files-agent-tesla/) and [Dridex](https://unit42.paloaltonetworks.com/excel-add-ins-dridex-infection-chain/) was previously highlighted by Palo Alto Networks Unit 42, noting that it "may indicate a new trend in the threat landscape."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"As more and more users adopt new versions of Microsoft Office, it is likely that threat actors will turn away from VBA-based malicious documents to other formats such as XLLs or rely on exploiting newly discovered vulnerabilities to launch malicious code in the process space of Office applications," Svajcer said.

## Malicious Microsoft Publisher macros push Ekipa RAT

[Ekipa RAT](https://cloudsek.com/threatint...