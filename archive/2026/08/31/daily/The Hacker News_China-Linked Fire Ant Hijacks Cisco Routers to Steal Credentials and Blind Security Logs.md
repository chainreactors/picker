---
title: China-Linked Fire Ant Hijacks Cisco Routers to Steal Credentials and Blind Security Logs
url: https://thehackernews.com/2026/08/china-linked-fire-ant-hijacks-cisco.html
source: The Hacker News
date: 2026-08-31
fetch_date: 2026-09-01T07:01:29.040842
---

# China-Linked Fire Ant Hijacks Cisco Routers to Steal Credentials and Blind Security Logs

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [China-Linked Fire Ant Hijacks Cisco Routers to Steal Credentials and Blind Security Logs](https://thehackernews.com/2026/08/china-linked-fire-ant-hijacks-cisco.html)

**Swati Khandelwal**Aug 31, 2026Cyber Espionage / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxYI5Ntk3CPoEGUHNQbd80hij-0QLnz3V_HBU3aXV-mvQq98IE6xsRlbuwZ2PNbbSV7dA-HlNfqRWj0_bd3XpQCOPt9R2gS3PJMm8lfMP_9IoKyhDNbY9NOotNDHO68v2DSUT_R-0UYTqZQc16DJM7OqS8_35iVUMqyy3GrUt7iMaIWz6iW6OSP2ddiDc/s1700-nu-rw-lo-l85-e365/cisco-creds.jpg)

A China-nexus cyber espionage actor tracked as **Fire Ant** has expanded a long-running campaign beyond VMware hypervisors to compromise Cisco IOS XR routers, Terminal Access Controller Access-Control System (TACACS) servers, and Linux management hosts used to route, authenticate, and manage high-value networks.

Sygnia, the incident response firm that investigated the intrusion, said the actor turned the compromised routers into collection platforms, capturing network traffic, harvesting credentials, and suppressing the logging and telemetry that defenders rely on to reconstruct an attack.

The firm assessed that the hacker group used its foothold to explore paths to connected high-value environments, including critical infrastructure. However, activity against those networks was limited to scanning and connection attempts rather than confirmed compromise.

Controlling the routers gave the actor a vantage point over traffic moving through trusted network paths, Sygnia said.

"This activity reinforces one of the core observations from the investigation: when a threat actor controls routers, they do not only gain reach. They gain perspective," the firm said.

The firm assessed that the activity strongly overlaps with [public reporting on UNC3886](https://thehackernews.com/2026/02/china-linked-unc3886-targets-singapore.html), a China-nexus espionage group known for targeting virtualization platforms and network edge devices, though it said in [its report](https://www.sygnia.co/blog/fire-ant-evolves-from-hypervisors-to-trusted-infrastructure/) that it does not make a conclusive attribution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Mandiant, which first documented UNC3886, has said it [found no technical overlap](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers) between the group and the separate Chinese operations tracked as Salt Typhoon and Volt Typhoon.

The 2026 activity follows [Sygnia's July 2025 disclosure](https://thehackernews.com/2025/07/fire-ant-exploits-vmware-flaw-to.html) of Fire Ant, which detailed the group's exploitation of VMware ESXi and vCenter environments before moving into the network and management layers.

The investigation began with an anomaly on a Cisco IOS XR router, where a Generic Routing Encapsulation (GRE) tunnel interface was operating with no running configuration or commit history to explain how it had been created. Sygnia did not identify how the actor first gained access to the router.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuRD9dBO8I1dB7DhtLLjlj-2Dirhi0Ktx0IwvFELrdxuVvW7SwjHIB8prpVAe9D5nUoW5Dj_2wAgZGQ1y9knq7osYyV5XLyFbO-kMPuIiTr0rDSBD0YvQxuxGtaTbETSl44lSq7TCfgLJYTL4Jnl3l3kN3pz_Gx3B709XK45qG6TgtMKRdwmb15PdHnzc/s1700-nu-rw-lo-l85-e365/target.png)

Tracing the tunnel led investigators to a legacy Linux system, from which Fire Ant ran repeated connection attempts and port probing against administrative and service ports on connected networks, including SSH, HTTP, SMB, and RDP.

The router malware was purpose-built for the IOS XR control plane rather than a generic Linux appliance. One component embedded a modified system library that checked each outgoing log message for the string Health and forwarded it only when the string was present.

A separate component altered the router's command-execution path to append an | exclude filter to show commands, hiding the attacker's tunnel configuration from administrators inspecting the device.

Fire Ant then used the routers to capture packet captures (PCAPs) from multiple Cisco devices. The captures were uploaded to external FTP servers, one of which appeared to have been installed the same day the uploads took place.

On the TACACS server, Sygnia identified a credential-collection toolset it tracks as TacTap.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVOxqvxfh_6YAxLk4LeYW4_dtqrv7a44AZj10eKJVZlEm1oNCzxe5zWe_0_8PZfM1ngMvglGbZxorRoVA0EUdd8XnFP4u9ubOBemr7_inOB_3bR-JDZuHoEgzabQpXOkHJYxX5EXF-duODGDEcJtnqBziXYVvyBh8zr3w81KIDu8pBD4NNvlb6uQGIJy4/s1700-nu-rw-lo-l85-e365/TACACS.png)

An injector named acppid loaded a malicious library into the running tac\_plus authentication process. The library hooked the functions that accept new connections. It then passed the live session handles to a second process over a local Unix socket.

The captured credentials were written to /var/log/.tacplus.acct and lightly obfuscated with a single-byte XOR key of 0xEF.

"To our knowledge, this specific tac\_plus library-injection technique has not been publicly described before, making it a notable evolution of Fire Ant's TACACS-focused credential collection tradecraft," Sygnia said.

Credential theft from TACACS servers is established tradecraft for the cluster, as Mandiant has previously documented UNC3886 deploying a [TACACS+ sniffer called LOOKOVER](https://thehackernews.com/2024/06/chinese-cyber-espionage-group-exploits.html) and replacing the tac\_plus daemon with a backdoored version to log credentials.

Sygnia also recovered a second new tool, a Linux backdoor it called **BridgeAgent**, which was deployed on the tunnel-connected host and masqueraded as a Zabbix monitoring agent.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi27a...