---
title: UAT-10027 Targets U.S. Education and Healthcare with Dohdoor Backdoor
url: https://thehackernews.com/2026/02/uat-10027-targets-us-education-and.html
source: The Hacker News
date: 2026-02-26
fetch_date: 2026-02-27T04:08:49.122900
---

# UAT-10027 Targets U.S. Education and Healthcare with Dohdoor Backdoor

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [UAT-10027 Targets U.S. Education and Healthcare with Dohdoor Backdoor](https://thehackernews.com/2026/02/uat-10027-targets-us-education-and.html)

**Ravie Lakshmanan**Feb 26, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJAVofZLLo1DEzVLXd9ahr2wbZLNqwM8K5eVDE8pDM5ossDzBi_U34YB81lu7LBProqz1SirGb7brANr4AQ83_k9Y0RhlcrsKKpl0IBovDLdy1awHNR_dxEV0umYpWUWLWkx7vQqCbunXZ7WnnJooiCvhchGXFwLAdT0LljMY_4MVRGfv2gM8uofci2J7E/s1700-e365/healthcare-cyberattack.jpg)

A previously undocumented threat activity cluster has been attributed to an ongoing malicious campaign targeting education and healthcare sectors in the U.S. since at least December 2025.

The campaign is being tracked by Cisco Talos under the moniker **UAT-10027**. The end goal of the attacks is to deliver a never-before-seen backdoor codenamed Dohdoor.

"Dohdoor utilizes the DNS-over-HTTPS (DoH) technique for command-and-control (C2) communications and has the ability to download and execute other payload binaries reflectively," security researchers Alex Karkins and Chetan Raghuprasad [said](https://blog.talosintelligence.com/new-dohdoor-malware-campaign/) in a technical report shared with The Hacker News.

Although the initial access vector used in the campaign is currently not known, it's suspected to involve the use of social engineering phishing techniques, leading to the execution of a PowerShell script.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The script then proceeds to download and run a Windows batch script from a remote staging server, which, for its part, facilitates the download of a malicious Windows dynamic-link library (DLL) that's named "propsys.dll" or "batmeter.dll."

The DLL payload – i.e., Dohdoor – is launched by means of a legitimate Windows executable (e.g., "Fondue.exe," "mblctr.exe," and "ScreenClippingHost.exe") using a technique referred to as [DLL side-loading](https://attack.mitre.org/techniques/T1574/001/). The backdoored access created by the implant is used to retrieve a next-stage payload directly into the victim's memory and execute it. The payload is assessed to be a Cobalt Strike Beacon.

"The threat actor hides the C2 servers behind the Cloudflare infrastructure, ensuring that all outbound communication from the victim machine appears as legitimate HTTPS traffic to a trusted global IP address," Talos said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglWVTZH6ZI5o1mqkH_UtqjisYIyJ1thdjxBT8x-QsS32B2ibUFlo4And5uZynTOrYBhmqZcQs7zFyziZemjlRKRV_oCR0xL4IK1-ZU9Sy1g9_uv8g1O800e9sQma9FLDOcZrAgK9ZhDQqLHAUIb_fL5fkKXWz32y2l0Z4MM5d0IpJKcBOgXn0oqnrEzmpF/s1700-e365/chain.jpg)

"This technique bypasses DNS-based detection systems, DNS sinkholes, and network traffic analysis tools that monitor suspicious domain lookups, ensuring that the malware's C2 communications remain stealth by traditional network security infrastructure."

Dohdoor has also been found to unhook system calls to bypass endpoint detection and response (EDR) solutions that monitor Windows API calls through [user-mode hooks in NTDLL.dll](https://www.mdsec.co.uk/2020/12/bypassing-user-mode-hooks-and-direct-invocation-of-system-calls-for-red-teams/).

Raghuprasad told The Hacker News that, "the attacker had infected several educational institutions, including a university that is connected to several other institutions, indicating a potential wider attack surface. Additionally, one of the affected entities was a healthcare facility, specifically for elderly care."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

Analysis of the campaign has revealed no evidence of data exfiltration to date. Although no final payloads have been observed other than what appears to be the Cobalt Strike Beacon to backdoor into the victim's environment, it's believed that UAT-10027's actions are likely driven by financial giants based on the victimology pattern, the researcher added.

There is currently no clarity on who is behind UAT-10027, but Cisco Talos said it found some tactical similarities between Dohdoor and [LazarLoader](https://thehackernews.com/2025/03/thn-weekly-recap-router-hacks-pypi.html#:~:text=Lazarus%20Group%20Drops%20LazarLoader%20Malware), a [downloader](https://s2w.inc/en/resource/detail/941) previously identified as used by the North Korean hacking group Lazarus in attacks aimed at South Korea.

"While UAT-10027's malware shares technical overlaps with the Lazarus Group, the campaign’s focus on the education and health care sectors deviates from Lazarus' typical profile of cryptocurrency and defense targeting," Talos concluded.

"However, [...] North Korean APT actors have targeted the healthcare sector using [Maui ransomware](https://thehackernews.com/2022/07/north-korean-maui-ransomware-actively.html), and another North Korean APT group, [Kimsuky](https://thehackernews.com/2021/11/north-korean-hackers-found-behind-range.html), has targeted the [education sector](https://globalcyberalliance.org/aide-data-kimsuky/), highlighting the overlaps in the victimology of UAT-10027 with that of other North Korean APTs."

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
[![...