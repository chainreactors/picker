---
title: Blind Eagle Uses Fake Court Notices to Deliver Remote Access Trojan Across Latin America
url: https://thehackernews.com/2026/11/blind-eagle-uses-fake-court-notices-to.html
source: The Hacker News
date: 2026-11-10
fetch_date: 2026-11-11T08:35:39.792569
---

# Blind Eagle Uses Fake Court Notices to Deliver Remote Access Trojan Across Latin America

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Blind Eagle Uses Fake Court Notices to Deliver Remote Access Trojan Across Latin America](https://thehackernews.com/2026/11/blind-eagle-uses-fake-court-notices-to.html)

**Ravie Lakshmanan**Nov 10, 2026Threat Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs4UHnKTj_NJCPa7Jqdntj8tEvZ2PgaY7s9kKK8_X2bxehTUcJeZPFfguJzvW_D0H9XD_q-qLZV2Qq6hqRYDQRYMXpyAzw-6T2yDjFjIY7zhGRLPDPjOalASUgX_Z-M2cEsNqiuys_4QjQ8vY_xl0fnWi2Y_9tT9aAH0WQOAB3D6uDf8yZY8VuphL4TRFG/s1700-nu-rw-lo-l85-e365/court-phish.jpg)

The threat actor known as **Blind Eagle** has resurfaced with a new campaign targeting organizations in Latin America through judicial and administrative-themed phishing lures to deliver a remote access trojan (RAT) that shares its lineage with AsyncRAT and DCRat.

"The campaign uses Portuguese and Spanish lures that resemble court notifications, fiscalía notices, [tutela proceedings](https://www.lcg-colombia.com/tutela-actions-in-colombia), and administrative documents," Zenox [said](https://zenox.ai/en/last-heist-new-apt-c-36-infection-wave-in-latam/) in a report shared with The Hacker News.

Assessed to be a Spanish-speaking group and active since 2018, Blind Eagle (aka APT-C-36) has a [track record](https://thehackernews.com/2023/02/apt-c-36-strikes-again-blind-eagle.html) of using [spear-phishing lures](https://thehackernews.com/2024/08/blind-eagle-hackers-exploit-spear.html) to distribute [commodity RATs](https://thehackernews.com/2025/08/blind-eagles-five-clusters-target.html) like AsyncRAT, BitRAT, Lime RAT, NjRAT, Quasar RAT, and Remcos RAT.

Attack chains begin with phishing emails targeting individuals who handle cases, contracts, judicial, or institutional service requests to trick them into opening a malware-laced attachment.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

One email containing a Colombian judicial-themed XHTML file has been identified as a [weaponized](https://www.cloudflare.com/en-in/cloudforce-one/research/svgs-the-hackers-canvas/) Scalable Vector Graphics ([SVG](https://www.sophos.com/en-us/blog/svg-phishing)) [image](https://www.ibm.com/think/x-force/weaponized-svgs-inside-a-global-phishing-campaign-targeting-financial-institutions) that renders a bogus web page impersonating Colombia's Fiscalía General de la Nación, also referred to as the Office of the Attorney General.

The web page, for its part, employs a technique known as [HTML smuggling](https://thehackernews.com/2022/12/hacking-using-svg-files-to-smuggle-qbot.html) to assemble the next-stage ZIP archive payload locally in the web browser using ZipCrypto, thereby circumventing email security controls.

Present within the ZIP archive is a JavaScript dropper that masquerades as Network Configuration Auditor version 2.7.298. The JavaScript code conducts environment reconnaissance, and collects details such as system version, network profile, installation date, memory size, computer name, environment variables, and directories localized in Portuguese and Spanish.

Upon execution, it launches a Visual Basic Script that performs Windows Antimalware Scan Interface ([AMSI](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal)) and Event Tracing for Windows ([ETW](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/event-tracing-for-windows)) bypass, while displaying a fake criminal-citation page as a distraction mechanism.

In parallel, the malware also takes steps to delete the original XHTML artifact, clears Mark of the Web (MotW) metadata, and [sets up persistence](https://cofense.com/blog/windows-persistence-explained-techniques%2C-risks%2C-and-what-defenders-should-know) on the host under the Windows Startup folder so that it's automatically executed on system startup.

The attack culminates with the use of PowerShell to decode and launch the final RAT payload in memory. The trojan is an AsyncRAT fork with DCRat lineage based on code structure, configuration, build characteristics, and observed behavior.

"The targeting of judicial, fiscal, administrative and educational organizations gives the operation access to highly sensitive legal, financial and institutional information," Zenox said.

"Combined with the Portuguese and Spanish lures, Brazilian infrastructure, operational timezone and regional victimology, these elements establish the campaign as an APT-C-36 operation conducted through a Brazilian operational cluster."

Zenox told The Hacker News that it could not confirm whether any of these attacks had succeeded against real-world targets. However, during the campaign period between late October and early November 2026, it observed a large-scale wave of targeted phishing involving nearly 3,300 malicious emails.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

While not all of these messages targeted organizations in Colombia, the country continues to remain a priority target for Blind Eagle for a combination of reasons.

"The repeated targeting of Colombia likely reflects multiple factors, with one of the main enabling factors being the structural vulnerabilities and uneven security maturity across parts of the country's critical, public, financial, and private-sector infrastructure," Zenox security researcher Gabriel Alves said.

"These conditions may increase the likelihood of successful compromises and offer greater opportunities to monetize access, steal sensitive data or funds, or reuse compromised credentials against critical systems. This is further supported by regional actors' familiarity with the Colombian context and is consistent with patterns observed among Latin American threat actors."

*(The story was updated after publication to include additional insights from Zenox.)*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTV...