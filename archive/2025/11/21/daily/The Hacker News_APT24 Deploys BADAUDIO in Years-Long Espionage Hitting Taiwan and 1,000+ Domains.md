---
title: APT24 Deploys BADAUDIO in Years-Long Espionage Hitting Taiwan and 1,000+ Domains
url: https://thehackernews.com/2025/11/apt24-deploys-badaudio-in-years-long.html
source: The Hacker News
date: 2025-11-21
fetch_date: 2025-11-22T03:08:59.996865
---

# APT24 Deploys BADAUDIO in Years-Long Espionage Hitting Taiwan and 1,000+ Domains

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [APT24 Deploys BADAUDIO in Years-Long Espionage Hitting Taiwan and 1,000+ Domains](https://thehackernews.com/2025/11/apt24-deploys-badaudio-in-years-long.html)

**Nov 21, 2025**Ravie LakshmananMalware / Threat Intelligence

[![Years-Long Espionage Hitting Taiwan](data:image/png;base64... "Years-Long Espionage Hitting Taiwan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5fGdXpR7pCeJpEqPu004ib52NeUwcRAWg8rpaNjFnvLAKcXXAJlHX1A4sgAfLJGc08sUQdEJnmnmtTClxO75Mp2evzyrbHLmQdTx0O3UdCbzZdTJAY71PpCj0gweks8UQDik_IpkCA5Pzxe9p8YA7u2ct5k67kFvIqHs18JF6YHSmZTuYsVbZatTsUKZV/s790-rw-e365/cyberattack.jpg)

A China-nexus threat actor known as **APT24** has been observed using a previously undocumented malware dubbed BADAUDIO to establish persistent remote access to compromised networks as part of a nearly three-year campaign.

"While earlier operations relied on broad strategic web compromises to compromise legitimate websites, APT24 has recently pivoted to using more sophisticated vectors targeting organizations in Taiwan," Google Threat Intelligence Group (GTIG) researchers Harsh Parashar, Tierra Duncan, and Dan Perez [said](https://cloud.google.com/blog/topics/threat-intelligence/apt24-pivot-to-multi-vector-attacks/).

"This includes the repeated compromise of a regional digital marketing firm to execute supply chain attacks and the use of targeted phishing campaigns."

APT24, also called Pitty Tiger, is the moniker [assigned](https://cloud.google.com/security/resources/insights/apt-groups) to a suspected Chinese hacking group that has targeted government, healthcare, construction and engineering, mining, nonprofit, and telecommunications sectors in the U.S. and Taiwan.

According to a July 2014 report from FireEye, the adversary is [believed](https://web.archive.org/web/20220517174055/https%3A//www.fireeye.com/blog/threat-research/2014/07/spy-of-the-tiger.html) to be active as early as 2008, with the attacks leveraging phishing emails to trick recipients into opening Microsoft Office documents that, in turn, exploit known security flaws in the software (e.g., [CVE-2012-0158](https://nvd.nist.gov/vuln/detail/cve-2012-0158) and [CVE-2014-1761](https://nvd.nist.gov/vuln/detail/cve-2014-1761)) to infect systems with malware.

Some of the malware families associated with APT24 include CT RAT, a variant of [Enfal/Lurid Downloader](https://unit42.paloaltonetworks.com/cmstar-downloader-lurid-and-enfals-new-cousin/) called MM RAT (aka Goldsun-B), and variants of Gh0st RAT known as Paladin RAT and Leo RAT. Another notable malware put to use by the threat actor is a backdoor named [Taidoor](https://thehackernews.com/2020/08/chinese-hacking-malware.html) (aka Roudan).

APT24 is assessed to be closely related to another advanced persistent threat (APT) group called Earth Aughisky, which has also deployed Taidoor in its campaigns and has leveraged infrastructure previously attributed to APT24 as part of attacks distributing another backdoor referred to as Specas.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Both the malware strains, per an [October 2022 report](https://thehackernews.com/2022/10/researchers-detail-malicious-tools-used.html) from Trend Micro, are designed to read proxy settings from a specific file "%systemroot%\\system32\\sprxx.dll."

The latest findings from GTIG show that the BADAUDIO campaign has been underway since November 2022, with the attackers using watering holes, supply chain compromises, and spear-phishing as initial access vectors.

A highly obfuscated malware written in C++, BADAUDIO uses [control flow flattening](https://news.sophos.com/en-us/2022/05/04/attacking-emotets-control-flow-flattening/) to resist reverse engineering and acts as a first-stage downloader that's capable of downloading, decrypting, and executing an AES-encrypted payload from a hard-coded command and control (C2) server. It works by gathering and exfiltrating basic system information to the server, which responds with the payload to be run on the host. In one case, it was a Cobalt Strike Beacon.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9jNvTKApMazSZragRJdcYvbYFhwR1_yjW4i1s7uwhycLBYN73IbRTeL5m-6PeLFxw0ClaGSxXolSPqIfRyBFqNH1wEsC0U4irVtpr9-FEUO4xNNCI5jbLuw7WK0eE5b46qCAGgCzKde5Yfc7mvYoG5yAu5Inj_NsVEGg9ywq-psgEVQv8BQlnCGKhyzbG/s2600/flow.jpg) |
| BADAUDIO campaign overview |

"BADAUDIO typically manifests as a malicious Dynamic Link Library (DLL) leveraging DLL Search Order Hijacking (MITRE ATT&CK T1574.001) for execution via legitimate applications," GTIG said. "Recent variants observed indicate a refined execution chain: encrypted archives containing BADAUDIO DLLs along with VBS, BAT, and LNK files."

From November 2022 to at least early September 2025, APT24 is estimated to have compromised more than 20 legitimate websites to inject malicious JavaScript code to specifically exclude visitors coming from macOS, iOS, and Android, generate a unique browser fingerprint using the FingerprintJS library, and serve them a fake pop-up urging them to download BADAUDIO under the guise of a Google Chrome update.

Then, starting in July 2024, the hacking group breached a regional digital marketing firm in Taiwan to orchestrate a supply chain attack by injecting the malicious JavaScript into a widely used JavaScript library that the company distributed, effectively allowing it to hijack more than 1,000 domains.

The modified third-party script is configured to reach out to a typosquatted domain impersonating a legitimate Content Delivery Network (CDN) and fetch the attacker-controlled JavaScript to fingerprint the machine and then serve the pop-up to download BADAUDIO after validation.

"The compromise in June 2025 initially employed conditional script loading based on a unique web ID (the specific domain name) related to the website using the compromised third-party scripts," Google said. "This suggests tailored targeting, limiting the strategic web co...