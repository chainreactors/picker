---
title: Kimwolf v7 Android Botnet Makes HTTP/2 DDoS Traffic Look Like Legitimate Browsing
url: https://thehackernews.com/2026/08/kimwolf-v7-android-botnet-makes-http2.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:48.876532
---

# Kimwolf v7 Android Botnet Makes HTTP/2 DDoS Traffic Look Like Legitimate Browsing

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

![cybersecurity](data:image/svg+xml;base64...)

# [Kimwolf v7 Android Botnet Makes HTTP/2 DDoS Traffic Look Like Legitimate Browsing](https://thehackernews.com/2026/08/kimwolf-v7-android-botnet-makes-http2.html)

**Ravie Lakshmanan**Aug 11, 2026Botnet / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieGDZmdQhY70KqvppH4w5wMVhbs804WeageCN1UXtRK4KpFkYWNk-wkTeTv9CUSNGYQMsaZ04XYWimXsIQmfl0uYSFgNJe7uBbXsg1xPw-cukXwJY3O3TAHUpWiiYmleWgDpu4PLMRfjgIQtOxb6Wq2yFjvqyb6lpoCOcOyWOpZoURLpddzyGkmc8soRHe/s1700-e365/android-botnet.jpg)

Cybersecurity researchers have discovered a new version of the **[Kimwolf/AISURU](https://thehackernews.com/2026/05/kimwolf-ddos-botnet-operator-arrested.html)** Android and Internet of Things (IoT) botnet that comes with significant improvements to improve its operational resilience and conduct distributed denial-of-service (DDoS) attacks.

The new version, tracked as Kimwolf v7, was [discovered](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/) by Palo Alto Networks Unit 42 in February 2026.

"Kimwolf v7 adds an HTTP/2-based DDoS flood that constructs complete browser fingerprints," researchers Asher Davila, Chris Navarrete, and Doel Santos said. "This makes attack traffic more difficult to distinguish from legitimate browsing."

The botnet also aims to make its command-and-control (C2) infrastructure more resistant to takedown efforts by using a tiered mechanism that employs Ethereum Name Service (ENS) to obtain the C2 address, a hard-coded Tor .onion hidden service, and a local proxy for routing between clearnet and Tor, while removing all scanning, exploitation, and brute-force functionality.

The removal of the scanner and exploit modules is an indication that the threat actors behind the operation have split the propagation pipeline from the core payload, offloading the task to an external loader for initial access, while the Kimwolf binary handles DDoS attacks and proxy relay.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Kimwolf is known to target Android TV boxes since August 2025, while its Linux counterpart, AISURU, primarily focuses on Linux IoT devices. The botnet has been active since at least mid-2024.

The botnet typically abuses residential proxy services to reach Android TVs that ship with Android Debug Bridge (ADB) enabled on port 5555 on local networks and install malware capable of conducting DDoS attacks and acting as a relay to ferry malicious traffic.

Once launched, the malware attempts to mask itself as seemingly legitimate Android system processes (e.g., "netd\_service") to fly under the radar. Some of the newly observed features in the new version are as follows -

* Carry out HTTP/2 flood attacks powered by the nghttp2 library along with constructing complete browser fingerprints that mirror legitimate browser behavior at the protocol and header level
* Using legitimate public Ethereum RPC services to query ENS domain records and resolve C2 addresses
* A backup C2 mechanism that uses a Tor .onion hidden service ("edctgwib2n5l34t525zkxqzk5bqb6e5il2yiq5r6zu7gtlxa4uosn3qd[.]onion") that's hard-coded into the binary
* A local proxy architecture that routes all C2 traffic through 127.0.0[.]1:23075, irrespective of whether it's headed to clearnet or Tor
* A high-performance UDP flood function that specifically targets ARM processors found in Android TV boxes
* Consolidate all DDoS attack commands to 15 numbered methods, down from 43 text-named methods found in prior versions

The Kimwolf operators have also been found to distribute Android APK packages that masquerade as a system service called SystemService, probe for root access, and execute a bundled ELF kernel payload inside. Eight such APK artifacts have been identified between October and December 2025.

"The earliest dropped sample, targeting the x86 architecture with a [Dirty COW](https://thehackernews.com/2017/09/dirty-cow-android-malware.html) exploit, suggests the family evolved from traditional Linux exploitation toward the current ADB-based Android propagation model," Unit 42 said. "The transition from libn[redacted]kernel.so to the less conspicuous libdevice.so filename in November 2025, followed by a revert in December, indicates active operational security adjustments."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The disclosure comes as a number of [new botnet malware families](https://thehackernews.com/2025/07/rondodox-botnet-exploits-flaws-in-tbk.html) have been detected in recent months -

* [AryStinger](https://thehackernews.com/2026/06/arystinger-malware-infects-4300-legacy.html), which enlists older, vulnerable home routers into a network for distributed reconnaissance and proxying
* [RustDuck](https://thehackernews.com/2026/06/rustduck-botnet-rebuilds-in-rust-to.html), which hijacks home routers, IP cameras, Android boxes, and poorly secured servers to rope them into a network for conducting DDoS attacks
* [NadMesh](https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html), which combines scanning, exploitation, and credential/AI-service intelligence harvesting into a single autonomous platform that's designed to scan for Redis, Docker, MCP, Kubernetes, ComfyUI, Ollama, n8n, Open WebUI, Langflow, and Gradio instances, drop an SSH backdoor, and harvest credentials, environment variables, account tokens, and AWS and Docker configurations
* [Tengu](https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html), a Mirai-derived IoT malware that employs Telnet brute-force to hijack IoT devices and run instructions that allow it to launch DoS attacks, gather network configuration information, set up persistence, exfiltrate system metadata, execute commands, download additional payloads, and turn the infected node into a proxy.

"Kimwolf v7 is a focused evolution of an already large-scale botnet," Unit 42 said. "Organizations should treat Android TV boxes as untrusted and segment them from enterprise networks. Disabling ADB or restricting it to USB-only access removes the primary propagation vector for this botnet."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtF...