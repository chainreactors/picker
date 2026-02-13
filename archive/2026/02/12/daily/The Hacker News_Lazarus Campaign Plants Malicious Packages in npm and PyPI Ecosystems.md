---
title: Lazarus Campaign Plants Malicious Packages in npm and PyPI Ecosystems
url: https://thehackernews.com/2026/02/lazarus-campaign-plants-malicious.html
source: The Hacker News
date: 2026-02-12
fetch_date: 2026-02-13T04:18:41.929814
---

# Lazarus Campaign Plants Malicious Packages in npm and PyPI Ecosystems

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

# [Lazarus Campaign Plants Malicious Packages in npm and PyPI Ecosystems](https://thehackernews.com/2026/02/lazarus-campaign-plants-malicious.html)

**Ravie Lakshmanan**Feb 12, 2026Vulnerability / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg48-Bb1617Je211tmVOc4BKdYLJjIst0IBibAqJyCaHUi1ZpHQd0EW_idmBrAbIlMm8fDx9yciZ0HiC4WdvabpudTHGJsa_5sOEfHf6idS0Lwv86Zk3Bb9tVvyQJrJ5d0PkByBASbHpjWr5hLU5aWWBeUH3pjMyPhEZtE5WxbpQNRbzhWTSUSSCFGwg1mU/s1700-e365/nkorea-hacker-code.jpg)

Cybersecurity researchers have discovered a fresh set of malicious packages across npm and the Python Package Index (PyPI) repository linked to a fake recruitment-themed campaign orchestrated by the North Korea-linked Lazarus Group.

The coordinated campaign has been codenamed graphalgo in reference to the first package published in the npm registry. It's assessed to be active since May 2025.

"Developers are approached via social platforms like LinkedIn and Facebook, or through job offerings on forums like Reddit," ReversingLabs researcher Karlo Zanki [said](https://www.reversinglabs.com/blog/fake-recruiter-campaign-crypto-devs) in a report. "The campaign includes a well-orchestrated story around a company involved in blockchain and cryptocurrency exchanges."

Notably, one of the identified npm packages, bigmathutils, attracted more than 10,000 downloads after the first, non-malicious version was published, and before the second version containing a malicious payload was released. The names of the packages are listed below -

**npm -**

* graphalgo
* graphorithm
* graphstruct
* graphlibcore
* netstruct
* graphnetworkx
* terminalcolor256
* graphkitx
* graphchain
* graphflux
* graphorbit
* graphnet
* graphhub
* terminal-kleur
* graphrix
* bignumx
* bignumberx
* bignumex
* bigmathex
* bigmathlib
* bigmathutils
* graphlink
* bigmathix
* graphflowx

**PyPI -**

* graphalgo
* graphex
* graphlibx
* graphdict
* graphflux
* graphnode
* graphsync
* bigpyx
* bignum
* bigmathex
* bigmathix
* bigmathutils

As with many [job-focused campaigns](https://thehackernews.com/2026/02/dprk-operatives-impersonate.html) conducted by North Korean threat actors, the attack chain begins with establishing a fake company like [Veltrix Capital](https://www.linkedin.com/company/veltrix-capital/) in the blockchain and cryptocurrency trading space, and then setting up the necessary digital real estate to create an illusion of legitimacy.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

This includes registering a domain and creating a related GitHub organization to host several repositories for use in coding assessments. The repositories have been found to contain projects based on Python and JavaScript.

"Examination of these repositories didn't reveal any obvious malicious functionality," Zanki said. "That is because the malicious functionality was not introduced directly via the job interview repositories, but indirectly – through dependencies hosted on the npm and PyPI open-source package repositories."

The idea behind setting up these repositories is to trick candidates who apply to its job listings on Reddit and Facebook Groups into running the projects on their machines, effectively installing the malicious dependency and triggering the infection. In some cases, victims are directly contacted by seemingly legitimate recruiters on LinkedIn.

The packages ultimately act as a conduit to deploy a remote access trojan (RAT) that periodically fetches and executes commands from an external server. It supports various commands to gather system information, enumerate files and directories, list running processes, create folders, rename files, delete files, and upload/download files.

Interestingly, the command-and-control (C2) communication is protected by a token-based mechanism to ensure that only requests with a valid token are accepted. The approach was [previously observed](https://thehackernews.com/2023/08/north-korean-hackers-deploy-new.html) in 2023 campaigns linked to a North Korean hacking group called Jade Sleet, which is also known as TraderTraitor or UNC4899.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcG8RRGvJ18ideLabWD-1IQnUlQp1of6I6dn14ZIdrnNzBAsbhuxz6aSuW3C5OVImtB64Lj6qe48DOKgw-WFHJJJ5y2S_Hn9680a6Vf_QDcPBVAhH_0ITkpTa5abDWzvXa2tNAq_xnrw2oqjGTKh14PbfQchE_XswJGphGHZvVeU2SLbzDd4b7IY6_blrm/s1700-e365/nkorea.jpg)

It essentially works like this: the packages send system data as part of a registration step to the C2 server, which responds with a token. This token is then sent back to the C2 server in subsequent requests to establish that they are originating from an already registered infected system.

"The token-based approach is a similarity [...] in both cases and has not been used by other actors in malware hosted on public package repositories as far as we know," Zanki told The Hacker News at that time.

The findings show that North Korean state-sponsored threat actors [continue to poison](https://thehackernews.com/2024/09/developers-beware-lazarus-group-uses.html) open-source ecosystems with malicious packages in hopes of stealing sensitive data and conducting financial theft, a fact evidenced by the RAT's checks to determine if the MetaMask browser extension is installed in the machine.

"Evidence suggests that this is a highly sophisticated campaign," ReversingLabs said. "Its modularity, long-lived nature, patience in building trust across different campaign elements, and the complexity of the multilayered and encrypted malware point to the work of a state-sponsored threat actor."

### More Malicious npm Packages Found

The disclosure comes as JFrog uncovered a sophisticated, malicious npm package called "duer-js" published by a user named "luizaearlyx." While the library claims to be a utility to "make the console window more visible," it harbors a Windows informati...