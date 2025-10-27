---
title: Critical Flaws in Tank Gauge Systems Expose Gas Stations to Remote Attacks
url: https://thehackernews.com/2024/09/critical-flaws-in-tank-gauge-systems.html
source: The Hacker News
date: 2024-10-01
fetch_date: 2025-10-06T18:56:05.929789
---

# Critical Flaws in Tank Gauge Systems Expose Gas Stations to Remote Attacks

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

# [Critical Flaws in Tank Gauge Systems Expose Gas Stations to Remote Attacks](https://thehackernews.com/2024/09/critical-flaws-in-tank-gauge-systems.html)

**Sep 30, 2024**Ravie LakshmananOperational Technology / Network Security

[![Gas Stations to Remote Attacks](data:image/png;base64... "Gas Stations to Remote Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxVyghya3tM_vqrVJGzPfmSlRwRhNQHUKooArq1g4GffE_Als5GHPh9loOOEvAzKQOlfQyVkqwW2q4VUQ-IZgJehY6t1-eT5v_GggsdjYWrZcQ34z4KoDDOvgva43VY28VnGke336EHIS3gB1NpkCDa9JI-mwBYSuZKYD2pzNLm1R4bzzNJRNfY1TiCt94/s790-rw-e365/gas.png)

Critical security vulnerabilities have been disclosed in six different Automatic Tank Gauge (ATG) systems from five manufacturers that could expose them to remote attacks.

"These vulnerabilities pose significant real-world risks, as they could be exploited by malicious actors to cause widespread damage, including physical damage, environmental hazards, and economic losses," Bitsight researcher Pedro Umbelino [said](https://www.bitsight.com/blog/critical-vulnerabilities-discovered-automated-tank-gauge-systems) in a report published last week.

Making matters worse, the analysis found that thousands of ATGs are exposed to the internet, making them a lucrative target for malicious actors looking to stage disruptive and destructive attacks against gas stations, hospitals, airports, military bases, and other critical infrastructure facilities.

ATGs are sensor systems designed to monitor the level of a storage tank (e.g., fuel tank) over a period of time with the goal of determining leakage and parameters. Exploitation of security flaws in such systems could therefore have serious consequences, including denial-of-service (DoS) and physical damage.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The newly discovered 11 vulnerabilities [affect](https://www.cisa.gov/news-events/alerts/2024/09/24/cisa-releases-eight-industrial-control-systems-advisories) six ATG models, namely Maglink LX, Maglink LX4, OPW SiteSentinel, Proteus OEL8000, Alisonic Sibylla, and Franklin TS-550. Eight of the 11 flaws are rated critical in severity -

* CVE-2024-45066 (CVSS score: 10.0) - OS command injection in Maglink LX
* CVE-2024-43693 (CVSS score: 10.0) - OS command injection in Maglink LX
* CVE-2024-43423 (CVSS score: 9.8) - Hard-coded credentials in Maglink LX4
* CVE-2024-8310 (CVSS score: 9.8) - Authentication bypass in OPW SiteSentinel
* CVE-2024-6981 (CVSS score: 9.8) - Authentication bypass in Proteus OEL8000
* CVE-2024-43692 (CVSS score: 9.8) - Authentication bypass in Maglink LX
* CVE-2024-8630 (CVSS score: 9.4) - SQL injection in Alisonic Sibylla
* CVE-2023-41256 (CVSS score: 9.1) - Authentication bypass in Maglink LX (a duplicate of a previously disclosed flaw)
* CVE-2024-41725 (CVSS score: 8.8) - Cross-site scripting (XSS) in Maglink LX
* CVE-2024-45373 (CVSS score: 8.8) - Privilege escalation in Maglink LX4
* CVE-2024-8497 (CVSS score: 7.5) - Arbitrary file read in Franklin TS-550

"All these vulnerabilities allow for full administrator privileges of the device application and, some of them, full operating system access," Umbelino said. "The most damaging attack is making the devices run in a way that might cause physical damage to their components or components connected to it."

## Flaws Discovered in OpenPLC, Riello NetMan 204, and AJCloud

Security flaws have also been uncovered in the open-source OpenPLC solution, including a critical stack-based buffer overflow bug (CVE-2024-34026, CVSS score: 9.0) that could be exploited to achieve remote code execution.

"By sending an ENIP request with an unsupported command code, a valid encapsulation header, and at least 500 total bytes, it is possible to write past the boundary of the allocated log\_msg buffer and corrupt the stack," Cisco Talos [said](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2005). "Depending on the security precautions enabled on the host in question, further exploitation could be possible."

Another set of security holes concern the Riello NetMan 204 network communications card used in its Uninterruptible Power Supply (UPS) systems that could enable malicious actors to take over control of the UPS and even tamper with the collected log data.

* CVE-2024-8877 - SQL injection in three API endpoints /cgi-bin/db\_datalog\_w.cgi, /cgi-bin/db\_eventlog\_w.cgi, and /cgi-bin/db\_multimetr\_w.cgi that allows for arbitrary data modification
* CVE-2024-8878 - Unauthenticated password reset via the endpoint /recoverpassword.html that could be abused to obtain the netmanid from the device, from which the recovery code for resetting the password can be calculated

"Inputting the recovery code in '/recoverpassword.html' resets the login credentials to admin:admin," CyberDanube's Thomas Weber [said](https://cyberdanube.com/en/en-multiple-vulnerabilities-in-riello-netman-204/index.html), noting that this could grant the attacker the ability to hijack the device and turn it off.

Both vulnerabilities remain unpatched, necessitating that users limit access to the devices in critical environments until a fix is made available.

Also of note are several critical vulnerabilities in the [AJCloud](https://ajcloud.app) IP camera management platform that, if successfully exploited, could lead to the exposure of sensitive user data and provide attackers with full remote control of any camera connected to the smart home cloud service.

"A built-in P2P command, which intentionally provides arbitrary write access to a key configuration file, can be leveraged to either permanently disable cameras or facilitate remote code execution through triggering a buffer overflow," Elastic Security Labs [said](https://www.elastic.co/security-labs/storm-on-the-horizon), stating its efforts to reach the Chinese company have been unsuccessful to date.

## CISA Warns of Continued Attacks Against OT Networks

The development comes as the U.S. Cybersecurity and In...