---
title: COVID-bit: New COVert Channel to Exfiltrate Data from Air-Gapped Computers
url: https://thehackernews.com/2022/12/covid-bit-new-covert-channel-to.html
source: The Hacker News
date: 2022-12-09
fetch_date: 2025-10-04T01:02:25.019700
---

# COVID-bit: New COVert Channel to Exfiltrate Data from Air-Gapped Computers

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

# [COVID-bit: New COVert Channel to Exfiltrate Data from Air-Gapped Computers](https://thehackernews.com/2022/12/covid-bit-new-covert-channel-to.html)

**Dec 08, 2022**Ravie LakshmananData Protection / Computer Security

[![The Hacker News](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikgRzBB_ZcTeEQfWI-Dxw6-XhxMPAi6xp3RumT0D_xkyE9JEi7NvFNi-zF5SKYCIIloz4qnrFUd2bA0q7O6Abo-BkHBJhSkK2bqaKks8SlFSCB183Rm1vlAaiQUPHmE7_S3TH54Qvtv5vNn25f_kuggVKQCidEyebMlYsuj_LTE17de8FgkUgppbBb/s790-rw-e365/daa.png)

An unconventional data exfiltration method leverages a previously undocumented covert channel to leak sensitive information from air-gapped systems.

"The information emanates from the air-gapped computer over the air to a distance of 2 m and more and can be picked up by a nearby insider or spy with a mobile phone or laptop," [Dr. Mordechai Guri](https://www.linkedin.com/in/mordechai-guri-081109100/), the head of R&D in the Cyber Security Research Center in the Ben Gurion University of the Negev in Israel and the head of Offensive-Defensive Cyber Research Lab, said in a [new paper](https://arxiv.org/abs/2212.03520) shared with The Hacker News.

The mechanism, dubbed **COVID-bit**, leverages malware planted on the machine to generate electromagnetic radiation in the 0-60 kHz frequency band that's subsequently transmitted and picked up by a stealthy receiving device in close physical proximity.

This, in turn, is made possible by exploiting the dynamic power consumption of modern computers and manipulating the momentary loads on CPU cores.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

COVID-bit is the [latest technique](https://cyber.bgu.ac.il/advanced-cyber/airgap) devised by Dr. Guri this year after [SATAn](https://thehackernews.com/2022/07/new-air-gap-attack-uses-sata-cable-as.html), [GAIROSCOPE](https://thehackernews.com/2022/08/new-air-gap-attack-uses-mems-gyroscope.html), and [ETHERLED](https://thehackernews.com/2022/08/air-gapped-devices-can-send-covert.html), which are designed to jump over air-gaps and harvest confidential data.

Air-gapped networks, despite their high level of isolation, can be [compromised](https://thehackernews.com/2021/12/researches-detail-17-malicious.html) by various strategies such as [infected USB drives](https://unit42.paloaltonetworks.com/unit42-tick-group-weaponized-secure-usb-drives-target-air-gapped-critical-systems/), supply chain attacks, and even rogue insiders.

Exfiltrating the data after breaching the network, however, is a challenge due to the lack of internet connectivity, necessitating that attackers concoct special methods to deliver the information.

The COVID-bit is one such covert channel that's used by the malware to transmit information by taking advantage of the electromagnetic emissions from a component called switched-mode power supply ([SMPS](https://en.wikipedia.org/wiki/Switched-mode_power_supply)) and using a mechanism called frequency-shift keying ([FSK](https://en.wikipedia.org/wiki/Frequency_modulation)) to encode the binary data.

[![The Hacker News](data:image/png;base64... "Air-Gapped Computers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAaGr5HllfFUM-w0XxTGv8wJC0raePRoFZ8fj_3vnFyGUwNdKOHz8w2mzfFlfc-zgK8Yih-oBTIWxVv-8XE-FOBqngV4E0GtQ0Eym-DWzZM5_Xuv2oSmufmKtsuTV3IyOWWKgnX408Q_yWW_CoEJnru1ZqpjedNJoJzDfPxfY8NsNhB6sAThb-Hd2B1Q/s790-rw-e365/1.png)

"By regulating the workload of the CPU, it is possible to govern its power consumption and hence control the momentary switching frequency of the SMPS," Dr. Guri explains.

"The electromagnetic radiation generated by this intentional process can be received from a distance using appropriate antennas" that cost as low as $1 and can be connected to a phone's 3.5 mm audio jack to capture the low-frequency signals at a bandwidth of 1,000 bps.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The emanations are then demodulated to extract the data. The attack is also evasive in that the malicious code doesn't require elevated privileges and can be executed from within a virtual machine.

An evaluation of the data transmissions reveals that keystrokes can be exfiltrated in near real-time, with IP and MAC addresses taking anywhere between less than 0.1 seconds to 16 seconds, depending on the bitrate.

Countermeasures against the proposed covert channel include carrying out dynamic opcode analysis to flag threats, initiating random workloads on the CPU processors when anomalous activity is detected, and monitoring or jamming signals in the 0-60 kHz spectrum.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Air Gap Hacking](https://thehackernews.com/search/label/Air%20Gap%20Hacking)[computer security](https://thehackernews.com/search/label/computer%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-2...