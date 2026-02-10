---
title: Bloody Wolf Targets Uzbekistan, Russia Using NetSupport RAT in Spear-Phishing Campaign
url: https://thehackernews.com/2026/02/bloody-wolf-targets-uzbekistan-russia.html
source: The Hacker News
date: 2026-02-09
fetch_date: 2026-02-10T04:27:35.007918
---

# Bloody Wolf Targets Uzbekistan, Russia Using NetSupport RAT in Spear-Phishing Campaign

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Bloody Wolf Targets Uzbekistan, Russia Using NetSupport RAT in Spear-Phishing Campaign](https://thehackernews.com/2026/02/bloody-wolf-targets-uzbekistan-russia.html)

**Ravie Lakshmanan**Feb 09, 2026Threat Intelligence / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiehyphenhyphenizf_EezYiQzf7tUgHJUYqd7k7zumWKSqP1n8K5YoJMRzmHjxJHdnN0GydURXFuwrRJd2qyTQSuH8TWPo_Wfh7SX0_1ljHcMjQGMQrDCtW23OLow6w7rPv4Uemxrd7vnQtGsWBzdUrhnrEtl914RxUcNeqKxVl81xXI9pVOFNaTh6UCLgkKw7QQYqeI/s1700-e365/rat-attack.jpg)

The threat actor known as **Bloody Wolf** has been linked to a campaign targeting Uzbekistan and Russia to infect systems with a remote access trojan known as [NetSupport RAT](https://thehackernews.com/2023/11/netsupport-rat-infections-on-rise.html).

Cybersecurity vendor Kaspersky is tracking the activity under the moniker [Stan Ghouls](https://securelist.com/stan-ghouls-in-uzbekistan/118738/). The threat actor is known to be active since at least 2023, orchestrating spear-phishing attacks against manufacturing, finance, and IT sectors in Russia, Kyrgyzstan, Kazakhstan, and Uzbekistan.

The campaign is estimated to have claimed about 50 victims in Uzbekistan, with 10 devices in Russia also impacted. Other infections have been identified to a lesser degree in Kazakhstan, Turkey, Serbia, and Belarus. Infection attempts have also been recorded on devices within government organizations, logistics companies, medical facilities, and educational institutions.

"Given Stan Ghouls' targeting of financial institutions, we believe their primary motive is financial gain," Kaspersky noted. "That said, their heavy use of RATs may also hint at cyber espionage."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The misuse of NetSupport, a legitimate remote administration tool, is a departure for the threat actor, which previously leveraged STRRAT (aka Strigoi Master) in its attacks. In November 2025, Group-IB [documented](https://thehackernews.com/2025/11/bloody-wolf-expands-java-based.html) phishing attacks aimed at entities in Kyrgyzstan to distribute the tool.

The attack chains are fairly straightforward in that phishing emails loaded with malicious PDF attachments are used as a launchpad to trigger the infection. The PDF documents embed links that, when clicked, lead to the download of a malicious loader that handles multiple tasks -

* Display a fake error message to give the impression to the victim that the application can't run on their machine.
* Check if the number of previous RAT installation attempts is less than three. If the number has reached or exceeded the limit, the loader throws an error message: "Attempt limit reached. Try another computer."
* Download the NetSupport RAT from one of the several external domains and launch it.
* Ensure NetSupport RAT's persistence by configuring an autorun script in the Startup folder, adding a NetSupport launch script ("run.bat") to the Registry's autorun key, and creating a scheduled task to trigger the execution of the same batch script.

Kaspersky said it also identified [Mirai botnet payloads](https://thehackernews.com/2025/01/mirai-botnet-launches-record-56-tbps.html) staged on infrastructure associated with Bloody Wolf, raising the possibility that the threat actor may have expanded its malware arsenal to target IoT devices.

"With over 60 targets hit, this is a remarkably high volume for a sophisticated targeted campaign," the company concluded. "It points to the significant resources these actors are willing to pour into their operations."

The disclosure coincides with a number of cyber campaigns targeting Russian organizations, including those conducted by [ExCobalt](https://thehackernews.com/2024/06/excobalt-cyber-gang-targets-russian.html), which has leveraged known security flaws and credentials stolen from contractors to obtain initial access to target networks. Positive Technologies [described](https://ptsecurity.com/research/pt-esc-threat-intelligence/ex-cobalt-a-review-of-the-group-s-attack-tools-for-2024-2025/#id1) the adversary as one of the "most dangerous groups" attacking Russian entities.

The attacks are characterized by the use of various tools, along with attempts to siphon Telegram credentials and message history from the compromised hosts and Outlook Web Access credentials by [injecting malicious code into the login page](https://thehackernews.com/2024/05/ms-exchange-server-flaws-exploited-to.html) -

* [CobInt](https://thehackernews.com/2024/06/excobalt-cyber-gang-targets-russian.html), a known backdoor used by the group.
* Lockers such as Babuk and LockBit.
* [PUMAKIT](https://thehackernews.com/2024/12/new-linux-rootkit-pumakit-uses-advanced.html), a [kernel rootkit](https://rt-solar.ru/solar-4rays/blog/5400/) to escalate privileges, hide files and directories, and conceal itself from system tools, along with prior iterations known as Facefish (February 2021), Kitsune (February 2022), and Megatsune (November 2023). The use of Kitsune was also linked to a threat cluster known as [Sneaky Wolf](https://bi.zone/expertise/blog/klyuch-ot-vsekh-dverey-kak-rutkit-kitsune-okhotitsya-za-vashimi-dannymi/) (aka Sneaking Leprechaun) by BI.ZONE.
* Octopus, a Rust-based toolkit that's used to elevate privileges in a compromised Linux system.

"The group changed the tactics of initial access, shifting the focus of attention from the exploitation of 1-day vulnerabilities in corporate services available from the internet (e.g., Microsoft Exchange) to the penetration of the infrastructure of the main target through contractors," Positive Technologies said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

State institutions, scientific enterprises, and IT organizations in Russia have also been targeted by a previously unknown threat actor known as [Punishing Owl](https://habr.com/ru/companies/pt/articles/990374) that has resorted to stealing and leaking data o...