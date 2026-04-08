---
title: Over 1,000 Exposed ComfyUI Instances Targeted in Cryptomining Botnet Campaign
url: https://thehackernews.com/2026/04/over-1000-exposed-comfyui-instances.html
source: The Hacker News
date: 2026-04-07
fetch_date: 2026-04-08T04:39:11.911538
---

# Over 1,000 Exposed ComfyUI Instances Targeted in Cryptomining Botnet Campaign

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Over 1,000 Exposed ComfyUI Instances Targeted in Cryptomining Botnet Campaign](https://thehackernews.com/2026/04/over-1000-exposed-comfyui-instances.html)

**Ravie Lakshmanan**Apr 07, 2026Cloud Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNAquH2CuNdKvNbKqIsmTqg2Rpb5SRn8zxBKdQliREzpq_Byd0ye0aD8IFVa1JUj09QnQVJVnAVET30DX0jRBK1LBXJ-16QC_GoiYDH2ibCfoYcttx3McOurmn9e4cSugeNgEQa-oVqR13I9K1h6ktgggudmT3u88I_iN_ksHQvuS2N0u0uGlUNTW_Tv9l/s1700-e365/compfyui.jpg)

An active campaign has been observed targeting internet-exposed instances running ComfyUI, a popular stable diffusion platform, to enlist them into a cryptocurrency mining and proxy botnet.

"A purpose-built Python scanner continuously sweeps major cloud IP ranges for vulnerable targets, automatically installing malicious nodes via [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) if no exploitable node is already present," Censys security researcher Mark Ellzey [said](https://censys.com/blog/comfyui-servers-cryptomining-proxy-botnet/) in a report published Monday.

The attack activity, at its core, systemically scans for exposed ComfyUI instances and exploits a misconfiguration that allows remote code execution on unauthenticated deployments through [custom nodes](https://docs.comfy.org/development/core-concepts/nodes).

Upon successful exploitation, the compromised hosts are added to a cryptomining operation that mines Monero via XMRig and Conflux via lolMiner, as well as to a Hysteria V2 botnet. Both of them are centrally managed through a Flask-based command-and-control (C2) dashboard.

Data from the attack surface management platforms shows that there are more than [1,000 publicly-accessible ComfyUI instances](https://platform.censys.io/search?q=%28host.services.endpoints.http.html_tags+%3D+%22%3Ctitle%3EComfyUI%3C%2Ftitle%3E%22%29+and+not+host.services.labels.value+%3D+%22HONEYPOT%22). While not a huge number, it's sufficient for a threat actor to run opportunistic campaigns to reap financial gains.

Censys said it discovered the campaign last month after identifying an open directory on [77.110.96[.]200](https://platform.censys.io/hosts/77.110.96.200), an IP address associated with a bulletproofing hosting services provider, [Aeza Group](https://thehackernews.com/2025/07/us-sanctions-russian-bulletproof.html). The directory is said to have contained a previously undocumented set of tools to pull off the attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

This includes two reconnaissance tools to enumerate exposed ComfyUI instances across cloud infrastructure, identify those that have ComfyUI-Manager installed, and shortlist those that are susceptible to the code execution exploit.

One of the two scanner Python scripts also functions as an exploitation framework that weaponizes ComfyUI's custom nodes to achieve code execution. This technique, some aspects of which were [documented](https://labs.snyk.io/resources/hacking-comfyui-through-custom-nodes/) by Snyk in December 2024, takes advantage of the fact that some custom nodes accept raw Python code as input and run it directly without requiring any authentication.

As a result, an attacker can scan exposed ComfyUI instances for specific custom node families that support arbitrary code execution, effectively turning the service into a channel for delivering attacker-controlled Python payloads. Some of the custom node families that the attack particularly looks for are listed below -

* Vova75Rus/ComfyUI-Shell-Executor
* filliptm/ComfyUI\_Fill-Nodes
* seanlynch/srl-nodes
* ruiqutech/ComfyUI-RuiquNodes

"If none of the target nodes are present, the scanner checks whether ComfyUI-Manager is installed," Censys said. "If available, it installs a vulnerable node package itself, then retries exploitation."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikaVhRPaXUbrhU-MsUlf2VqYKxmkD2cdWgOQWGit4H0bQJs5cgpHvy4QP-R8NNC2BGbAotVgtU6ZS_xf7LOAaAVweLeqb64fdwB-AHQv_nUPxhE1Gq3GShLWWfuTWkEEXvjXKAN2aczToCWLsoNlfM1axgUGJXPHNB0VMgujHwfZgwGr5ZeJcX4FPSEfVV/s1700-e365/kry.png)

It's worth noting that "ComfyUI-Shell-Executor" is a malicious package created by the attacker to fetch a next-stage shell script ("ghost.sh") from the aforementioned IP address. Once code execution is obtained, the scanner removes evidence of the exploit by clearing the ComfyUI prompt history.

A newer version of the scanner also incorporates persistence mechanisms that cause the shell script to be downloaded every six hours and the exploit workflow to be re-executed every time ComfyUI is started.

The shell script, for its part, disables shell history, kills competing miners, launches the miner process, anduses the [LD\_PRELOAD](https://thehackernews.com/2023/03/cryptojacking-group-teamtnt-suspected.html) hook to hide a watchdog process that ensures the miner process is revived in the event it gets terminated.

In addition, the miner program is copied to multiple locations so that even if the primary install directory gets wiped, it can be launched from one of the fallback locations. A third mechanism the malware uses to ensure persistence is the use of the "[chattr +i](https://man7.org/linux/man-pages/man1/chattr.1.html)" command to lock the miner binaries and prevent them from being deleted, modified, or renamed, even by the root user.

"There is also dedicated code targeting a specific competitor, 'Hisana' (which is referenced throughout the code), which appears to be another mining botnet," Censys explained. "Rather than just killing it, ghost.sh overwrites its configuration to redirect Hisana's mining output to its own wallet address, then occupies Hisana’s C2 port (10808) with a dummy Python listener so Hisana can't restart."

The infected hosts are commandeered by means of a Flask-based C2 panel, which allows the operator to push instru...