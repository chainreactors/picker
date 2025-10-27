---
title: New Gafgyt Botnet Variant Targets Weak SSH Passwords for GPU Crypto Mining
url: https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html
source: The Hacker News
date: 2024-08-16
fetch_date: 2025-10-06T18:07:22.172894
---

# New Gafgyt Botnet Variant Targets Weak SSH Passwords for GPU Crypto Mining

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

# [New Gafgyt Botnet Variant Targets Weak SSH Passwords for GPU Crypto Mining](https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html)

**Aug 15, 2024**Ravie LakshmananNetwork Security / Cybercrime

[![Gafgyt Botnet Variant](data:image/png;base64... "Gafgyt Botnet Variant")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj01KpOk9BP4WCswcnjH0Hx3VybKX3HCRux5wlsdWVN446ujuJ86-LoTD9bPx86HyAFUE05hS9CSTJ9AD3aHQIviVN42vX82EohGYEX0v_D7Gw3LQBH4YmqcXMjIxorb_c8ijZWf1ojW9E9eR9T9SiZe81mxIr2O8nOkem1vEYsbjXgUtQ6k3BKJZxCgboG/s790-rw-e365/mining.png)

Cybersecurity researchers have discovered a new variant of the **Gafgyt** botnet that's targeting machines with weak SSH passwords to ultimately mine cryptocurrency on compromised instances using their GPU computational power.

This indicates that the "IoT botnet is targeting more robust servers running on cloud native environments," Aqua Security researcher Assaf Morag [said](https://www.aquasec.com/blog/gafgyt-malware-variant-exploits-gpu-power-and-cloud-native-environments/) in a Wednesday analysis.

Gafgyt (aka BASHLITE, Lizkebab, and Torlus), known to be [active in the wild](https://thehackernews.com/2014/11/bashlite-malware-leverages-shellshock.html) since 2014, has a history of [exploiting](https://unit42.paloaltonetworks.com/unit42-multi-exploit-iotlinux-botnets-mirai-gafgyt-target-apache-struts-sonicwall/) weak or default credentials to gain control of devices such as routers, cameras, and digital video recorders (DVRs). It's also capable of leveraging known security flaws in Dasan, Huawei, Realtek, SonicWall, and Zyxel devices.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The infected devices are corralled into a botnet capable of launching distributed denial-of-service (DDoS) attacks against targets of interest. There is [evidence](https://blog.netlab.360.com/gafgtyt_tor-and-necro-are-on-the-move-again/) to suggest that Gafgyt and Necro are operated by a threat group called [Keksec](https://thehackernews.com/2022/04/new-enemybot-ddos-botnet-borrows.html), which is also tracked as Kek Security and FreakOut.

IoT Botnets like Gafgyt are [constantly](https://nsfocusglobal.com/look-gafgyt-botnet-trends-communication-traffic-log/) [evolving](https://blog.netlab.360.com/the-gafgyt-variant-vbot-and-its-31-campaigns/) to add new features, with [variants](https://www.uptycs.com/blog/threat-research-report-team/mirai-code-re-use-in-gafgyt) detected in 2021 using the TOR network to cloak the malicious activity, as well as borrow some modules from the leaked Mirai source code. It's worth noting that Gafgyt's source code was [leaked online](https://web.archive.org/web/20161003194500/https%3A//blog.level3.com/security/attack-of-things/) in early 2015, further fueling the emergence of new versions and adaptations.

[![Gafgyt Botnet Variant](data:image/png;base64... "Gafgyt Botnet Variant")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgVUwGailnyE-0Q7Pipga2dOUnL92pO5crki9EO68jGif8ebiKMgXz8ajnXhxpGNKDtjS_C86UAMfmROb5sSwKn15uMy2jBjC9cIc9qkTxObUoHJK9GHYKvb_NFhwgwPzVAoftzp7mlLagygcv61I9_dRQLN_ZRqqY0ouEtbXkzSPeARMZpKidIo36UWH8/s790-rw-e365/gg.jpg)

The latest attack chains involve brute-forcing SSH servers with weak passwords to deploy next-stage payloads to facilitate a cryptocurrency mining attack using "systemd-net," but not before terminating competing malware already running on the compromised host.

It also executes a worming module, a Go-based SSH scanner named ld-musl-x86, that's responsible for scanning the internet for poorly secured servers and propagating the malware to other systems, effectively expanding the scale of the botnet. This comprises SSH, Telnet, and credentials related to game servers and cloud environments like AWS, Azure, and Hadoop.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The cryptominer in use is XMRig, a Monero cryptocurrency miner," Morag said. "However, in this case, the threat actor is seeking to run a cryptominer using the --opencl and --cuda flags, which leverage GPU and Nvidia GPU computational power."

"This, combined with the fact that the threat actor's primary impact is crypto-mining rather than DDoS attacks, supports our claim that this variant differs from previous ones. It is aimed at targeting cloud-native environments with strong CPU and GPU capabilities."

Data gathered by querying Shodan shows that there are over 30 million publicly accessible SSH servers, making it essential that users take steps to secure the instances against brute-force attacks and potential exploitation.

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

[botnet](https://thehackernews.com/search/label/botnet)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[iot security](https://thehackernews.com/search/label/iot%20security)[Malware](https://theh...