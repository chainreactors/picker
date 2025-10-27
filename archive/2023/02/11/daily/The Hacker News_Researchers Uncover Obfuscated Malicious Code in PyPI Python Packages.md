---
title: Researchers Uncover Obfuscated Malicious Code in PyPI Python Packages
url: https://thehackernews.com/2023/02/researchers-uncover-obfuscated.html
source: The Hacker News
date: 2023-02-11
fetch_date: 2025-10-04T06:23:39.586268
---

# Researchers Uncover Obfuscated Malicious Code in PyPI Python Packages

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

# [Researchers Uncover Obfuscated Malicious Code in PyPI Python Packages](https://thehackernews.com/2023/02/researchers-uncover-obfuscated.html)

**Feb 10, 2023**Ravie LakshmananSupply Chain / Software Security

[![PyPI Python Packages](data:image/png;base64... "PyPI Python Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKlBMLQviBS_AqU4IbZxjofkcfjKNRFAv3KDCQF0flRAUcMPHsy1Y0MmC-nIh2zunu8fq9f28BemYMjkqrB4yH6kzIyHbe6w66d3W_SyTCYATJovrUKC8xG3qp20zqgaM81jnGua8m21kg4K9TTrclbLhVzYf59mRj6osJ4FL9Hp_4UMCvYB_YDMyT/s790-rw-e365/malware.png)

Four different rogue packages in the Python Package Index (**PyPI**) have been found to carry out a number of malicious actions, including dropping malware, deleting the netstat utility, and manipulating the SSH authorized\_keys file.

The packages in question are [aptx](https://pepy.tech/project/aptx), [bingchilling2](https://pepy.tech/project/bingchilling2), [httops](https://pepy.tech/project/httops), and [tkint3rs](https://pepy.tech/project/tkint3rs), all of which were collectively downloaded about 450 times before they were taken down. While aptx is an attempt to impersonate Qualcomm's [highly popular audio codec](https://en.wikipedia.org/wiki/AptX) of the same name, httops and tkint3rs are typosquats of https and tkinter, respectively.

"Most of these packages had well thought out names, to purposely confuse people," security researcher and journalist Ax Sharma [said](https://blog.sonatype.com/malicious-aptx-python-package-drops-meterpreter-shell-deletes-netstat).

An analysis of the malicious code injected in the setup script reveals the presence of an obfuscated [Meterpreter payload](https://www.sentinelone.com/blog/meterpreter-advanced-powerful-metasploit-payload/) that's disguised as "[pip](https://pypi.org/project/pip/)," a legitimate package installer for Python, and which can be leveraged to gain shell access to the infected host.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Also undertaken are steps to remove the [netstat](https://en.wikipedia.org/wiki/Netstat) command-line utility that's used for monitoring network configuration and activity as well as modifying the [.ssh/authorized\_keys file](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server) to set up an SSH backdoor for remote access.

"Now this is a sleek but real world example of damaging malware that successfully made its way into the open source ecosystem," Sharma noted.

[![Python Package Index](data:image/png;base64... "Python Package Index")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTiJ7MZLu9urA5RmyDruEmTAs5bn7yknjLgRNL9Yh2MK3c7tyIPtC5mnrOOW2Apv5iDhQHJdbXf3HdC9E717n41Y0CW6PL4Eoo8C5Rku8XbpTg7DLTyvEGDp8fw7KwSPB0uPExG2o0eXeViU33Scmf3xRz6ri6qBBQImVaAi2N-qe42wv7SKEtXxNj/s790-rw-e365/python.png)

But in a sign that malware sneaking into the software repositories are a recurring threat, Fortinet FortiGuard Labs uncovered five different Python packages – [web3-essential](https://pepy.tech/project/web3-essential), [3m-promo-gen-api](https://pepy.tech/project/3m-promo-gen-api), [ai-solver-gen](https://pepy.tech/project/ai-solver-gen), [hypixel-coins](https://pepy.tech/project/hypixel-coins), [httpxrequesterv2](https://pepy.tech/project/httpxrequesterv2), and [httpxrequester](https://pepy.tech/project/httpxrequester) – that are [engineered](https://www.fortinet.com/blog/threat-research/supply-chain-attack-by-new-malicious-python-package-web3-essential) to [harvest and exfiltrate](https://www.fortinet.com/blog/threat-research/supply-chain-attack-via-new-malicious-python-packages-by-malware-author-core1337) sensitive information.

The disclosures come as ReversingLabs shed light on a malicious npm module dubbed aabquerys that masquerades as the legitimate abquery package in an attempt to trick developers into downloading it.

The obfuscated JavaScript code, for its part, comes with capabilities to retrieve a second-stage executable from a remote server, which, in turn, contains an Avast proxy binary ([wsc\_proxy.exe](https://decoded.avast.io/threatintel/apt-treasure-trove-avast-suspects-chinese-apt-group-mustang-panda-is-collecting-data-from-burmese-government-agencies-and-opposition-groups/)) that's known to vulnerable to [DLL side-loading](https://attack.mitre.org/techniques/T1574/002/) attacks.

[![Python Package Index](data:image/png;base64... "Python Package Index")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipJKhhVU3yNjXIkNJUjD1rpObkK4qVy1RzDjEpJd5l4N-v_bxSDJ6dK8kHoxUoJG4Nz85JxmTsc8HIdQcnsxOHosu99aQhSrnizvbrRMVjOdYFBk-ISbOCJJrj4ZKo9k-z7xkrAgKGv5WYGSEk-gQj5jJ_OfWRVvOQ49wB9XWZalGNdwf9y9iMk3Zk/s790-rw-e365/avast.png)

This enables the threat actor to invoke a malicious library that's engineered to fetch a third-stage component, Demon.bin, from a command-and-control (C2) server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Demon.bin is a malicious agent with typical RAT (remote access trojan) functionalities that was generated using an open source, post-exploitation, command-and-control framework named [Havoc](https://github.com/HavocFramework/Havoc)," ReversingLabs researcher Lucija Valentić [said](https://www.reversinglabs.com/blog/open-source-malware-sows-havoc-on-supply-chain).

Furthermore, the author of aabquerys is said to have published multiple versions of two other packages named aabquery and nvm\_jquery that are suspected to be early iterations of aabquerys.

Havoc is far from the only C2 exploitation framework detected in the wild, what with criminal actors leveraging custom suites such as Manjusaka, Covenant, Merlin, and Empire in malware campaigns.

The findings also underscore the [growing](https://thehackernews.com/2023/01/researchers-uncover-3-pypi-packages.html) [risk](https://blog.phylum.io/phylum-identifies-98-malicious-npm-packages) of [nefarious packages](https://blog.sonatype.com/malware-monthly...