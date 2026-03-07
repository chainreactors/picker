---
title: China-Linked Hackers Use TernDoor, PeerTime, BruteEntry in South American Telecom Attacks
url: https://thehackernews.com/2026/03/china-linked-hackers-use-terndoor.html
source: The Hacker News
date: 2026-03-06
fetch_date: 2026-03-07T03:57:09.213931
---

# China-Linked Hackers Use TernDoor, PeerTime, BruteEntry in South American Telecom Attacks

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [China-Linked Hackers Use TernDoor, PeerTime, BruteEntry in South American Telecom Attacks](https://thehackernews.com/2026/03/china-linked-hackers-use-terndoor.html)

**Ravie Lakshmanan**Mar 06, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibIdID8bpu83EtYZEGzGQcfnL4Q2mTuhTp95la1d1iDtHqYtujF75TT6TkEmu6C123EIHQNF2P-M-Kj7Z0-3pjvm4CFFqnJ_qOxbgVAGJ7V6rnycpn-O-8v3Mw3dkYcSHSyee7EdPjIEejdoWwUx0YBQXexhtMZ79zQV5rBwbbrvxzoloBcLHoSOY_7Sg-/s1700-e365/telecom.jpg)

A China-linked advanced persistent threat (APT) actor has been targeting critical telecommunications infrastructure in South America since 2024, targeting Windows and Linux systems and edge devices with three different implants.

The activity is being [tracked](https://blog.talosintelligence.com/uat-9244/) by Cisco Talos under the moniker **UAT-9244**, describing it as closely associated with another cluster known as [FamousSparrow](https://thehackernews.com/2025/03/new-sparrowdoor-backdoor-variants-found.html).

It's worth noting that FamousSparrow is assessed to share tactical overlaps with [Salt Typhoon](https://thehackernews.com/2024/11/chinese-hackers-use-ghostspider-malware.html), a China-nexus espionage group known for its targeting of telecommunication service providers. Despite the similar targeting footprint between UAT-9244 and Salt Typhoon, there is no conclusive evidence that ties the two clusters together.

In the campaign analyzed by the cybersecurity company, the attack chains have been found to distribute three previously undocumented implants: TernDoor targeting Windows, PeerTime (aka angrypeer) targeting Linux, and BruteEntry, which is installed on network edge devices.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The exact initial access method used in the attacks is not known, although the adversary has previously targeted systems running outdated versions of Windows Server and Microsoft Exchange Server to drop web shells for follow-on activity.

TernDoor is deployed through DLL side-loading, leveraging the legitimate executable "wsprint.exe" to launch a rogue DLL ("BugSplatRc64.dll") that decrypts and executes the final payload in memory. A variant of [Crowdoor](https://thehackernews.com/2024/09/chinese-speaking-hacker-group-targets.html) (itself a variant of SparrowDoor), the backdoor is said to have been put to use by UAT-9244 since at least November 2024.

It establishes persistence on the host by means of a scheduled task or the Registry Run key. It also exhibits differences with CrowDoor by making use of a disparate set of command codes and embedding a Windows driver to suspend, resume, and terminate processes. Furthermore, it only supports one command-line switch ("-u") to uninstall itself from the host and delete all associated artifacts.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhenZ4kcSPFJFiI9zSta98ann-7-BuELfJThLmSO7B3A97tiiw79koef53dKymIRInkF79PmQm3sgS4kGvJDH-YlzEf-_YKrFcidQv9_MwVCkCGV1SyYGPa7T9Tor0XQh-Hs6j5Qj-ErIpgdu0uTszh19t5zCXLJUKnQPcePNK9yBIKJaaJLn_V475wxdNF/s1700-e365/BruteEntry.jpg)

Once launched, it runs a check to make sure that it has been injected into "msiexec.exe," after which it decodes a configuration to extract the command-and-control (C2) parameters. Subsequently, it establishes communication with the C2 server, allowing it to create processes, run arbitrary commands, read/write files, collect system information, and deploy the driver to hide malicious components and manage processes.

Further analysis of the UAT-9244's infrastructure has led to the discovery of a Linux peer-to-peer (P2P) backdoor dubbed PeerTime, which is compiled for several architectures (i.e., ARM, AARCH, PPC, and MIPS) so as to infect a variety of embedded systems. The ELF backdoor, along with an instrumentor binary, is deployed via a shell script.

"The instrumentor ELF binary will check for the presence of Docker on the compromised host using the commands docker and docker –q," Talos researchers Asheer Malhotra and Brandon White said. "If Docker is found, then the PeerTime loader is executed. The instrumentor consists of debug strings in Simplified Chinese, indicating that it is a custom binary created and deployed by Chinese-speaking threat actors."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

The primary goal of the loader is to decrypt and decompress the final PeerTime payload and execute it directly in memory. PeerTime comes in two flavors: one version written in C/C++ and a newer variant programmed in Rust. Besides having the ability to rename itself as a harmless process to sidestep detection, the backdoor employs the BitTorrent protocol to fetch C2 information, download files from its peers, and execute them on the compromised system.

Also staged in the threat actor's servers are a set of shell scripts and payloads, including a brute-force scanner codenamed BruteEntry that's installed on edge devices to turn them into mass-scanning proxy nodes within an Operational Relay Box (ORB) capable of brute-forcing Postgres, SSH, and Tomcat servers.

This is accomplished by means of a shell script that drops two Golang-based components: an orchestrator that delivers BruteEntry, which then contacts a C2 server to obtain the list of IP addresses to be targeted for performing brute-force attacks. The backdoor ultimately reports successful logins back to the C2 server.

"'Success' indicates if the brute force was successful (true or false), and 'notes' provides specific information on whether the brute force was successful," Talos said. "If the login failed, the note reads 'All credentials tried.'"

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com...