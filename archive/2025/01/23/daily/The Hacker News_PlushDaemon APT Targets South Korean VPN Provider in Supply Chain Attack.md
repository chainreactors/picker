---
title: PlushDaemon APT Targets South Korean VPN Provider in Supply Chain Attack
url: https://thehackernews.com/2025/01/plushdaemon-apt-targets-south-korean.html
source: The Hacker News
date: 2025-01-23
fetch_date: 2025-10-06T20:26:59.166107
---

# PlushDaemon APT Targets South Korean VPN Provider in Supply Chain Attack

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

# [PlushDaemon APT Targets South Korean VPN Provider in Supply Chain Attack](https://thehackernews.com/2025/01/plushdaemon-apt-targets-south-korean.html)

**Jan 22, 2025**Ravie LakshmananSupply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8feUMfpw4kkPZ2agFg7JExErk2NI5rUCbpCqdoPeKgGLCQkl-jAaoRKPTl-Lu6ybuuxjqsnlCdcbsSGrzPqz24pVhT9cPsZ9iI6KXOaZgpdSO-mbPICG2PP-T_OhDJLKKe8OG18icf05z0-qb8JUd8ioyp-vc1GoMZTkMOCkd07fkwyP_p4e1144oh4pf/s790-rw-e365/eset.png)

A previously undocumented China-aligned advanced persistent threat (APT) group named **PlushDaemon** has been linked to a supply chain attack targeting a South Korean virtual private network (VPN) provider in 2023, according to new findings from ESET.

"The attackers replaced the legitimate installer with one that also deployed the group's signature implant that we have named SlowStepper – a feature-rich backdoor with a toolkit of more than 30 components," ESET researcher Facundo Muñoz [said](https://www.welivesecurity.com/en/eset-research/plushdaemon-compromises-supply-chain-korean-vpn-service/) in a technical report shared with The Hacker News.

PlushDaemon is assessed to be a China-nexus group that has been operational since at least 2019, targeting individuals and entities in China, Taiwan, Hong Kong, South Korea, the United States, and New Zealand.

Central to its operations is a bespoke backdoor called SlowStepper, which is described as a large toolkit consisting of around 30 modules, programmed in C++, Python, and Go.

Another crucial aspect of its attacks is the hijacking of legitimate software update channels and exploitation of vulnerabilities in web servers to gain initial access to the target network. Muñoz told The Hacker News that PlushDaemon abused an unknown vulnerability in Apache HTTP server from an unidentified organization in Hong Kong last year.

The Slovakian cybersecurity company said it noticed in May 2024 malicious code embedded within the NSIS installer for Windows downloaded from the website of a VPN software provider named IPany ("ipany[.]kr/download/IPanyVPNsetup.zip").

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The rogue version of the installer, which has since been removed from the website, is designed to drop the legitimate software as well as the SlowStepper backdoor. It's currently not clear who the exact targets of the supply chain attack are, although any individual or entity downloading the booby-trapped ZIP archive could have been at risk.

Telemetry data gathered by ESET shows that several users attempted to install the trojanized software in the networks associated with a semiconductor company and an unidentified software development company in South Korea. The oldest victims were recorded from Japan and China in November and December 2023, respectively.

The attack chain starts with the execution of the installer ("IPanyVPNsetup.exe"), which proceeds to establish persistence on the host between reboots and launches a loader ("AutoMsg.dll") that, in turn, is responsible for running shellcode that loads another DLL ("EncMgr.pkg").

The DLL subsequently extracts two more files ("NetNative.pkg" and "FeatureFlag.pkg") that are utilized to sideload a malicious DLL file ("lregdll.dll") using "PerfWatson.exe," which is a renamed version of a legitimate command-line utility named regcap.exe that's part of Microsoft Visual Studio.

The end goal of the DLL is to load the SlowStepper implant from the winlogin.gif file present within FeatureFlag.pkg. SlowStepper is believed to be in the works since January 2019 (version 0.1.7), with the latest iteration (0.2.12) compiled in June 2024.

"Although the code contains hundreds of functions, the particular variant used in the supply-chain compromise of the IPany VPN software appears to be version 0.2.10 Lite, according to the backdoor's code," Muñoz said. "The so-called 'Lite' version indeed contains fewer features than other previous and newer versions."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilLN2bP4s3UL5v7v3NWjCJ1Wze7cx9AgnK-7mH6H6e_qudc1dQmyG81L4d1YDSuEZCRmDZO6LYWcx0X1F8ciL8I4B1_iVJg-v-le010W62GqGmkheMoKjGy4sxaP4857nWUadZiGBdTBYv_y_FEpt6b2XEXjgB7hwTRpxZHRiBKwGzjX6YS0VK8rFPK1bG/s790-rw-e365/malware.png)

Both the full and Lite versions make use of an extensive suite of tools written in Python and Go that allows for the gathering of data and clandestine surveillance through the recording of audio and videos. The tools are said to have been hosted in the Chinese code repository platform [GitCode](https://gitcode.net/LetMeGo22/).

The Hacker News also identified a [Gitee account](https://gitee.com/letmego22/) with the same username as that of the GitCode repository, although it's not known if they are related at this stage. "Regarding the LetMeGo22 account, even though its 'caffee' repository hosts various tools that were used by SlowStepper we don't know whether these tools are the work of PlushDaemon or the work of some third-party," Muñoz said.

As for command-and-control (C&C), SlowStepper constructs a DNS query to obtain a TXT record for the domain 7051.gsm.360safe[.]company to one of the three public DNS servers (114DNS, Google, and Alibaba Public DNS) in order to fetch an array of 10 IP addresses, from which one is chosen for use as a C&C server to process operator-issued commands.

"If, after a number of attempts, it fails to establish a connection to the server, it uses the [gethostbyname API](https://learn.microsoft.com/en-us/windows/win32/winsock/gethostbyname-function-in-the-api-2) on the domain st.360safe[.]company to obtain the IP address mapped to that domain and uses the obtained IP as its fallback C&C server," Muñoz explained.

The commands run a wide gamut, permitting it to capture exhaustive system information; execute a Python module; delete specific files; run commands via cmd.exe; enumerate the file system; downl...