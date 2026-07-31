---
title: SilverFox Targets Japanese Manufacturer with 3-Driver BYOVD Chain and ValleyRAT
url: https://thehackernews.com/2026/07/silverfox-targets-japanese-manufacturer.html
source: The Hacker News
date: 2026-07-30
fetch_date: 2026-07-31T05:31:17.795627
---

# SilverFox Targets Japanese Manufacturer with 3-Driver BYOVD Chain and ValleyRAT

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [SilverFox Targets Japanese Manufacturer with 3-Driver BYOVD Chain and ValleyRAT](https://thehackernews.com/2026/07/silverfox-targets-japanese-manufacturer.html)

**Ravie Lakshmanan**Jul 30, 2026Cybercrime / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzKpx1jDG3j0UsS5Ova8qJWV4gmJcez4M7iowp3M10Tvnvl1toUDwWI1igPQ_XK4-7IIuFXf7cTiKZ9QIRFco8PWFC4mRzBwGz81-8Ix95ujv3bVhshhFEAwjCNJR14ezza7kiAIalG3MjMQPPhH6rQP4lcZS4o1Vw9dO7ErrFmCvlrrd0ATiakQ_LeENQ/s1700-e365/drivers.jpg)

The Chinese cybercrime group known as **Silver Fox** has been observed using new drivers as part of bring your own vulnerable driver (BYOVD) attacks targeting a Japanese organization in the industrial manufacturing sector to ultimately deliver ValleyRAT (aka Winos 4.0) for persistent remote access.

"In this campaign, the group combines new vulnerable-driver abuse, newly observed abuse of legitimate applications for DLL sideloading, defense evasion, and layered recovery mechanisms to keep ValleyRAT running," Cato Networks researchers Shani Kurtzberg, Tomer Pugach, Dr. Guy Waizel, Zohar Buber, Idan Tarab, and Shani Kurtzberg [said](https://www.catonetworks.com/blog/cato-ctrl-silverfox-evolves/) in an analysis.

The attack chain begins with an invoice-themed phishing lure that uses attacker-controlled content hosted on legitimate QQ and Tencent Cloud services to trigger a DLL side-loading chain via a ZIP archive that paves the way for the deployment of ValleyRAT, but not before leveraging the BYOVD technique to obtain kernel access and impair security controls on the compromised host to evade detection.

The ZIP archive contains a downloader executable that retrieves the next-stage components necessary for DLL side-loading from an attacker-controlled Tencent Cloud infrastructure.

While Silver Fox has previously leveraged this method using the legitimate-but-vulnerable "[amsdk.sys](https://thehackernews.com/2025/09/silver-fox-exploits-microsoft-signed.html)" and "[wsftprm.sys](https://thehackernews.com/2026/02/weekly-recap-double-tap-skimmers.html#:~:text=Phishing%20Campaigns%20in%20Taiwan%20Deliver%20Winos%204%2E0)" drivers, the latest campaign marks the use of two other drivers: "BootRepair.sys" and "EnPortv.sys," which have not been publicly reported in connection with prior attack waves.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Specifically, the malicious DLL ("PDFCORE8.dll") sideloaded by "ConvertToPDF.exe" or "PDFDirect.exe" embeds "  [BootRepair.sys](https://github.com/redteamfortress/PhantomKiller)  ," "  [EnPortv.sys](https://thehackernews.com/2026/02/threatsday-bulletin-codespaces-rce.html#driver-abuse-escalation)  ," and  [wsftprm.sys](https://thehackernews.com/2026/06/dragonforce-hackers-abuse-microsoft.html)  ," turning the malware into a modular three-driver BYOVD framework for defense evasion. Both legitimate binaries are associated with Zeon Corporation.

The idea behind incorporating three different drivers is to ensure operational resilience across environments and turn the BYOVD implementation into a plug-and-play system that allows the operators to swap out the drivers and replace them with other options while keeping the rest of the workflow intact.

On top of that, the malware uses NTDLL unhooking to remove user-mode inline hooks placed by endpoint security software to keep tabs on native Windows API activity.

"The malware integrates Bring Your Own Vulnerable Driver (BYOVD), DLL side-loading, NTDLL unhooking, process injection, registry-based payload storage, and two independent recovery mechanisms to impair security controls and maintain execution," the researchers said.

The DLL loader, which acts as a self-contained execution framework, is also responsible for unleashing a watchdog batch script that ensures persistence by means of a scheduled task and communicates with an external server ("43.128.26[.]132") to fetch shellcode that's injected into a new "svchost.exe" process using a technique called [thread-context hijacking](https://www.picussecurity.com/resource/blog/t1055-003-thread-execution-hijacking).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXqApM13ZWajhHL61nSUztShRFmwtT_a1yuOtA1ZCha4Tq0X2YALm_amee_JkZZcoY2LjL9p1KcV1xFdrm9E5zh0HMe7EuPBZlWMmXeN5O7mrcaDTdcohGlp6bYRdlvlBdXN-6CFU-X23yNbn5x9ZgfOYpBef1ZPJqvn2MAvley4GSniEDUxqYYJpNlnYm/s1700-e365/loaer.png)

The resulting final-stage implant is ValleyRAT, a variant of Gh0st RAT that offers remote-access functionality, including command-and-control (C2) communication, task execution, and additional post-compromise capabilities.

A defining aspect of the attack sequence is its dual watchdog design that ensures execution recovery. It pairs an internal routine that monitors the injected payload with the aforementioned external watchdog script that monitors the loader behind the creation of that payload.

This two-pronged approach means that terminating one component alone may not completely neutralize the intrusion. If the injected payload exits, it's recreated by the loader. If the loader itself gets terminated, the watchdog script springs into action to relaunch it.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

"This layered design increases resilience because defenders must interrupt both components and prevent either from restoring the other stage," Cato said.

"The recovery architecture also reinforces the modularity observed throughout the sample. Driver deployment, security-process termination, injection, payload monitoring, and loader recovery are implemented as coordinated components rather than isolated techniq...