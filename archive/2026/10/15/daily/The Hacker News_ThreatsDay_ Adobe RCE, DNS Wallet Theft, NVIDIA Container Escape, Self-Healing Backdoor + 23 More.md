---
title: ThreatsDay: Adobe RCE, DNS Wallet Theft, NVIDIA Container Escape, Self-Healing Backdoor + 23 More
url: https://thehackernews.com/2026/10/threatsday-adobe-rce-dns-wallet-theft.html
source: The Hacker News
date: 2026-10-15
fetch_date: 2026-10-16T06:37:54.399605
---

# ThreatsDay: Adobe RCE, DNS Wallet Theft, NVIDIA Container Escape, Self-Healing Backdoor + 23 More

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [ThreatsDay: Adobe RCE, DNS Wallet Theft, NVIDIA Container Escape, Self-Healing Backdoor + 23 More](https://thehackernews.com/2026/10/threatsday-adobe-rce-dns-wallet-theft.html)

**Ravie Lakshmanan**Oct 15, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8jHVMYXIjddaTrqHbBuPm3mQ6G_g8qlALwitmiIRM9OplZpPxLPDFet7ySOV0OVxPj6cW1oz0K6rydDvGYQGalR1jSt10bz8kti4dWnM0d3NnUBjuymD77_cReujy6AXmFgJgQQvl2qeICur3VHf5vYyOrxz8OFM-bEunzmK9PGDzCzzTVFVEdQyswYho/s1700-nu-rw-lo-l85-e365/threatsday-oct.jpg)

Someone built a tool to steal data, then decided it should scare the victim for fun. Yes, that’s an actual feature. And somehow, it fits right in with this week's security stories.

The rest gets interesting in different ways. A small permission can lead to a big theft. A trusted login can hide the wrong person. Old bugs are finding new victims, familiar tools are being put to strange uses, and some flaws are so simple you wonder how nobody spotted them sooner.

There's a lot more hiding in the details, including a few twists you probably wouldn't expect. Here's what made the list this week.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. Active ransomware exploitation

   [Qilin and Settra Exploit PAN-OS Flaw](https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html)

   Qilin and Settra [ransomware groups](https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html) are actively exploiting [CVE-2026-0257](https://thehackernews.com/2026/05/pan-os-globalprotect-authentication.html), an [authentication bypass vulnerability](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/) in PAN-OS GlobalProtect and Prisma Access. The vulnerability, disclosed in May 2026, has since come under active exploitation. "Because this access originates through an organization’s own VPN, malicious activity can resemble legitimate remote work and may go undetected until credential theft, lateral movement, data theft, or ransomware deployment is underway," ReliaQuest [said](https://x.com/ReliaQuestTR/status/2108647641240465707). "Organizations should immediately upgrade affected deployments, disable authentication override cookies where they are not required, terminate all active GlobalProtect sessions after patching, and investigate unexpected connections, including sessions using hostnames such as 'kali.' Patching alone may not remove access established before remediation."
2. Hybrid warfare escalates across Europe

   [Russia's Hybrid Attacks Across Europe](https://www.recordedfuture.com/blog/russia-new-generation-warfare)

   Russia is assessed to have escalated its use of hybrid, asymmetric warfare across Europe following its full-scale invasion of Ukraine in February 2022. "They do not involve troops moving across a country’s border or a state’s military dropping bombs on an adversary’s capital city," Recorded Future [said](https://www.recordedfuture.com/blog/russia-new-generation-warfare). "Instead, they are a complex kit of psychological, cyber, and physical tactics meant to achieve several key aims: (1) Test the enemy’s defensive capabilities, as Russia evaluates whether to escalate aggression into a formal, kinetic conflict, (2) Degrade the enemy’s critical infrastructure, and (3) Sow an environment of fear in the enemy’s government and population to degrade the enemy’s ability to respond."
3. DNS-powered wallet theft

   [Noir, a Crypto Wallet Drainer Kit](https://www.infoblox.com/blog/threat-intelligence/when-a-wallet-drainer-asks-dns-where-to-go/)

   Infoblox has analyzed a cryptocurrency wallet-drainer kit, self-branded as Noir, that makes use of DNS TXT records to locate its hosted pool, which currently runs on Cloudflare Pages. It's delivered by means of a loader that queries the TXT record through public DoH services to learn which backend pool is active. "The drainer does not need a seed phrase, password, or private key," Infoblox [said](https://www.infoblox.com/blog/threat-intelligence/when-a-wallet-drainer-asks-dns-where-to-go/). "It tailors content to the user after receiving initial read permissions, developing a plan for the specific wallet. Then it obtains spending permissions that can look less alarming than a direct transfer and performs the theft from attacker-controlled infrastructure." It's suspected that the malware was created and maintained with AI assistance.

   [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaGSZY5JqTmW34HInw03BYKUQT78q081NrSDi-G6j98eiKXTl3Afytu-MzaLSWAOb5lr2-GK6QYDz6xQsDIIfD9QQN8Q9aXc32QAPyAYsMEC3RA-qTNCHRxXk_kBxE-FXt4iitg5OA5x1ZVuHG9tW-KmMd6LsDTsQD-_UOAHtsa_xzKGj1v62BfvbfNnoC/s1700-nu-rw-lo-l85-e365/victim.jpg)
4. Discord-based remote access threat

   [CikaBika Bot Uses Discord for C2 Discovered](https://www.darktrace.com/blog/cikabika-bot-inside-a-discord-rat)

   A Rust-based remote access trojan dubbed CikaBika Bot has been observed being delivered via a document-themed lure containing a malicious LNK file and a PDF with an embedded payload. "The malware uses a Nim loader, PowerShell UAC bypass, and DLL search-order hijacking before leveraging Discord for C2, reconnaissance, remote execution, and data exfiltration through ngrok in observed malicious activity," Darktrace [said](https://www.darktrace.com/blog/cikabika-bot-inside-a-discord-rat). The malware also supports screenshot capture and file transfers.
5. RAT combines theft and intimidation

   [New KGB RAT Malware Advertised on Cybercrime Forums](https://www.group-ib.com/blog/kgb-rat-windows-fud-trojan/)

   A Windows remote access trojan (RAT) called KGB RAT is being marketed on underground forums since late 2025 as being fully undetectable. It features a built-in crypter, HVNC, credential theft, ransomware, and an unusual set of psyc...