---
title: Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API
url: https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html
source: The Hacker News
date: 2026-05-20
fetch_date: 2026-05-21T06:04:43.136865
---

# Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Webworm Deploys EchoCreep and GraphWorm Backdoors Using Discord and MS Graph API](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html)

**Ravie Lakshmanan**May 20, 2026Malware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt4cD52DtnzH5FM8ZMrW9KyPrD1ysrJURSmqalrw9f6siP8XxYqClsqV6ofHpM8ir7gBnmmvehj5HB1k0aSHdPmLtKKwtLLvjSi4ELa9eMq12maW7p56a2yBdl7xzdfv6893fvQxLIH0kKGYKnzYM_7-3XysWIGsSNiEYXBjmiWFqe0Pe8uq-TkWlQjjv4/s1700-e365/cyberattack-paki.jpg)

Cybersecurity researchers have flagged fresh activity from a China-aligned threat actor known as **Webworm** in 2025, deploying custom backdoors that employ Discord and Microsoft Graph API for command-and-control (C2 or C&C) communications.

Webworm, first [publicly documented](https://thehackernews.com/2022/09/webworm-hackers-using-modified-rats-in.html) by Broadcom-owned Symantec in September 2022, is assessed to be active since at least 2022, targeting government agencies and enterprises spanning IT services, aerospace, and electric power sectors in Russia, Georgia, Mongolia, and several other Asian nations.

Attacks mounted by the group have leveraged remote access trojans (RATs) like Trochilus RAT, Gh0st RAT, and [9002 RAT](https://thehackernews.com/2024/07/china-linked-apt17-targets-italian.html) (aka Hydraq and McRat). The threat actor is said to overlap with China-nexus clusters tracked as [FishMonger](https://thehackernews.com/2025/03/china-linked-apt-aquatic-panda-10-month.html) (aka Aquatic Panda), [SixLittleMonkeys](https://www.welivesecurity.com/2020/05/14/mikroceen-spying-backdoor-high-profile-networks-central-asia/), and [Space Pirates](https://thehackernews.com/2025/02/space-pirates-targets-russian-it-firms.html). SixLittleMonkeys is best known for deploying Gh0st RAT and a RAT called Mikroceen targeting entities in Central Asia, Russia, Belarus, and Mongolia.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

"In recent years, it has started moving toward both existing and custom proxy tools, which are more stealthy than full-fledged backdoors," ESET researcher Eric Howard [said](https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/). "In 2025, Webworm also added two new backdoors to its toolset: EchoCreep, which uses Discord for C&C communication, and GraphWorm, which uses Microsoft Graph API for the same purpose."

Underlying these efforts is the use of a GitHub repository impersonating a WordPress fork ("github[.]com/anjsdgasdf/WordPress") as a staging ground for malware and tools like SoftEther VPN in an effort to blend in and fly under the radar. The reliance on SoftEther VPN is a [tried-and-tested](https://thehackernews.com/2023/08/china-linked-flax-typhoon-cyber.html) [approach](https://thehackernews.com/2024/11/china-aligned-mirrorface-hackers-target.html) adopted by [several](https://thehackernews.com/2025/08/taiwan-web-servers-breached-by-uat-7237.html) [Chinese hacking groups](https://thehackernews.com/2026/05/china-linked-uat-8302-targets.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiwVfQDc_kP-HsOpPT50FUgKEC4phePFJrLIjvygH6pnpTugpSdljuJbYv3JxpN5kdYx4X7VJlJBQ1-oDloLI6XkoPh2WrptVd_39HkuzQHvzeHqo8wQDhngv5swgmGgP30bhTlqBDwHPmqM0ljE1_LhdU4v40pxG8vuosm1-suck6gMGN3anvKiLbCuti/s1700-e365/time.png)

Over the past two years, the adversary has been observed shifting away from traditional backdoors to (semi-)legitimate utilities such as SOCKS proxies, while also increasingly focusing on European countries, including governmental organizations in Belgium, Italy, Serbia, Poland, and Spain, and a local university in South Africa.

The discovery of EchoCreep and GraphWorm marks an expansion of Webworm's arsenal, even as Trochilus and 9002 RAT appear to have been abandoned by the threat actor. Other tools of note are iox and custom proxy solutions such as WormFrp, ChainWorm, SmuxProxy, and WormSocket. WormFrp has been found to retrieve configurations from a compromised Amazon S3 bucket.

"These custom proxy tools are not only capable of encrypting communications, but also support chaining across multiple hosts both internally and externally to a network," ESET said. "We believe that the operators use these tools in conjunction with SoftEther VPN to better cover their tracks and increase the stealth of their activities."

EchoCreep supports file upload/download and command execution via "cmd.exe" capabilities, while GraphWorm is a more advanced backdoor that can spawn a new "cmd.exe" session, execute a newly created process, upload and download files to and from Microsoft OneDrive, and stop its own execution after receiving a signal from the operators.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-rTXnA1Y9juitOOYVDzBuX44_jMK5RmaMY-UfcLng2EWv6V0RoB1R1owhC7PNu_XGa9woDcq4vnL_-UvR_5A8u7jRvW-FGmjkOiHpGNoG5Ibk5YqOOGNT9LHocAG8Jna_t4R7HkyCxsjibIMm5jfsVNBzrO9pCsrtHv7C2GgvLT8z0esoZYMTE2o-7den/s1700-e365/badiis.jpg)

An analysis of the Discord channel leveraged by EchoCreep as C2 shows that the earliest commands were sent as far back as March 21, 2024. In all, 433 Discord messages have been sent via the C2 server.

Exactly how these backdoors are delivered, and the initial access pathway used by Webworm, is presently unknown. However, it has emerged that the attacker utilizes open-source utilities like dirsearch and nuclei to brute-force victim web server files and directories, and search for vulnerabilities within.

As for tradecraft overlaps, ESET told The Hacker News that Webworm's links to Space Pirates is tenuous at best, citing the use of open-source RATs and a lack of concrete evidence tying the two clusters.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"The relation on which Webworm and Space Pirates is built is on behalf of RATs which are open sourced," H...