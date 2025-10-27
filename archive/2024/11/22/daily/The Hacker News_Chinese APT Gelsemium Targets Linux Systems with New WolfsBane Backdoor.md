---
title: Chinese APT Gelsemium Targets Linux Systems with New WolfsBane Backdoor
url: https://thehackernews.com/2024/11/chinese-apt-gelsemium-targets-linux.html
source: The Hacker News
date: 2024-11-22
fetch_date: 2025-10-06T19:20:11.567405
---

# Chinese APT Gelsemium Targets Linux Systems with New WolfsBane Backdoor

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

# [Chinese APT Gelsemium Targets Linux Systems with New WolfsBane Backdoor](https://thehackernews.com/2024/11/chinese-apt-gelsemium-targets-linux.html)

**Nov 21, 2024**Ravie LakshmananCyber Espionage / Malware

[![Chinese APT Gelsemium](data:image/png;base64... "Chinese APT Gelsemium")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilJmAV4lFXTTkecwwaj72BFrkJEvyepdc79cW8gaa6wfH8Hy2FfAAmo-7njWDGjyDbzI-2SEw2MpZzqrSYy3dHTcqWQB4X_OZBTWd8TPveAI2mdaGUsL24vvz5aEvNyefLm7DGhnWoPUVCE-IBxf_zhTs3mNU4icqVM4u399Ib7FfVl54M2Bb_8VHzGeHM/s790-rw-e365/linux.png)

The China-aligned advanced persistent threat (APT) actor known as [Gelsemium](https://thehackernews.com/2023/09/new-report-uncovers-three-distinct.html) has been observed using a new Linux backdoor dubbed WolfsBane as part of cyber attacks likely targeting East and Southeast Asia.

That's according to [findings](https://www.welivesecurity.com/en/eset-research/unveiling-wolfsbane-gelsemiums-linux-counterpart-to-gelsevirine/) from cybersecurity firm ESET based on multiple Linux samples uploaded to the VirusTotal platform from Taiwan, the Philippines, and Singapore in March 2023.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

WolfsBane has been assessed to be a Linux version of the threat actor's [Gelsevirine](https://thehackernews.com/2021/06/noxplayer-supply-chain-attack-is-likely.html) backdoor, a Windows malware put to use as far back as 2014. Also discovered by the company is another previously undocumented implant named FireWood that's connected to a different malware toolset known as [Project Wood](https://thehackernews.com/2024/01/china-backed-hackers-hijack-software.html).

FireWood has been attributed to Gelsemium with low confidence, given the possibility that it could be shared by multiple China-linked hacking crews.

"The goal of the backdoors and tools discovered is cyber espionage targeting sensitive data such as system information, user credentials, and specific files and directories," ESET researcher Viktor Šperka said in a report shared with The Hacker News.

[![Chinese APT Gelsemium](data:image/png;base64... "Chinese APT Gelsemium")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgue57iMsDLN_7V7wESFrNBhK8_BlMFVR_JtyRy49Y47n_AMnsbiZasp6SLEO0IeexVAPzToR5flt38mqidGd-Wn6N0wWPepBFskp8__dd3vHyLf-qnH3jW2VcYJscpuq3mL0BPvCX_w7BrcD5QlM8iKXoOPqiQrJzOEn7MviZuYR3Gl9RAzHYQPPbgbbC0/s790-rw-e365/backdoor.png)

"These tools are designed to maintain persistent access and execute commands stealthily, enabling prolonged intelligence gathering while evading detection."

The exact initial access pathway used by the threat actors is not known, although it's suspected that the threat actors exploited an unknown web application vulnerability to drop web shells for persistent remote access, using it to deliver the WolfsBane backdoor by means of a dropper.

Besides using the modified open-source [BEURK](https://github.com/unix-thrust/beurk/tree/dev) userland rootkit to conceal its activities on the Linux host, it's capable of executing commands received from an attacker-controlled server. In a similar vein, FireWood employs a kernel driver rootkit module called usbdev.ko to hide processes, and run various commands issued by the server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The use of WolfsBane and FireWood is the first documented use of Linux malware by Gelsemium, signaling an expansion of the targeting focus.

"The trend of malware shifting towards Linux systems seems to be on the rise in the APT ecosystem," Šperka said. "From our perspective, this development can be attributed to several advancements in email and endpoint security."

"The ever-increasing adoption of EDR solutions, along with Microsoft's default strategy of disabling VBA macros, are leading to a scenario where adversaries are being forced to look for other potential avenues of attack."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data security](https://thehackernews.com/search/label/data%20security)[ESET](https://thehackernews.com/search/label/ESET)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[rootkit](https://thehackernews.com/search/label/rootkit)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

...