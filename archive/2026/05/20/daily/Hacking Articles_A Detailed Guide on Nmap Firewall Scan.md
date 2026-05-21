---
title: A Detailed Guide on Nmap Firewall Scan
url: https://www.hackingarticles.in/a-detailed-guide-on-nmap-firewall-scan/
source: Hacking Articles
date: 2026-05-20
fetch_date: 2026-05-21T06:02:02.946240
---

# A Detailed Guide on Nmap Firewall Scan

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Nmap](https://www.hackingarticles.in/category/nmap/)
»* [A Detailed Guide on Nmap Firewall Scan](https://www.hackingarticles.in/a-detailed-guide-on-nmap-firewall-scan/)
»

[Nmap](https://www.hackingarticles.in/category/nmap/)

# A Detailed Guide on Nmap Firewall Scan

[May 20, 2026May 20, 2026](https://www.hackingarticles.in/a-detailed-guide-on-nmap-firewall-scan/) by [raj](https://www.hackingarticles.in/author/admin/)

This walkthrough confirms an uncomfortable truth for defenders: flag-based firewall rules age poorly because Nmap supplies enough scan variants to circumvent any single combination. Length-based filtering scales better, but it remains a reactive control that an attacker can defeat through fragmentation or custom payloads. Effective network defence, therefore, demands layered controls — stateful inspection, intrusion detection signatures, rate limiting, and host-based monitoring — rather than reliance on iptables alone. For penetration testers, the lessons are equally clear: vary your scan techniques, observe how the target responds at the packet level, and let the defender’s rule choices guide your next probe.

### **Introduction**

Firewalls remain the first line of defence against network reconnaissance, yet attackers continue to refine techniques that slip past static rule sets. This article walks the reader through the complete arc of a reconnaissance battle between an Nmap-equipped attacker and a defender wielding iptables. Each scan technique exposes a new packet attribute that the defender can match on, and each new firewall rule prompts the attacker to craft probes that evade it. By the end of the walkthrough, virtually every attribute that iptables can inspect — TCP flags, packet length, Time-To-Live, source port, source MAC, source IP, payload bytes, and TCP options — has been challenged and defeated by a one-line Nmap argument.

The exercise serves two communities. For penetration testers, it provides a structured methodology for probing unfamiliar firewalls, reading their behaviour as a fingerprint of the rules they enforce, and selecting the next probe that targets exactly that rule. For defenders, it demonstrates why static rule-by-rule filtering ultimately fails and why robust security must combine stateful inspection, anomaly detection, behavioural analytics, and layered controls rather than rely on iptables alone. Every probe in the walkthrough is captured in Wireshark, allowing the reader to observe the byte-level behaviour that determines whether each scan succeeds or fails.

### **Table of Contents**

* Introduction
* Lab Environment
* Understanding Nmap scan signatures
* The Baseline: TCP Connect Scan (-sT)
* Blocking the SYN Probe at the Firewall
* FIN Scan (-sF)
* NULL Scan (-sN)
* XMAS Scan (-sX)
* Hardening Against FIN Scans
  + Reject Data-length with IPTables
  + Bypassing the Length Filter with a SYN Scan
* Fragment Scan
  + Closing the Common Length Signatures
  + Verifying the Defence: All Standard Scans Blocked
  + Data Length Scan
* TTL Scan
* Strengthening Security: Blocking TTL 64 and Below
* Source Port Spoofing Scan
* Decoy Scan
* Hiding in the Crowd: Decoy Scanning
* Spoof MAC Address Scan
* Spoof IP Address Scan
* Data-String Scan
* Hex String Scan
* IP-Options Scan
* Mitigation Strategies
  + Adopt Stateful Inspection
  + Deploy Intrusion Detection and Prevention Systems
  + Apply Rate Limiting and Connection Throttling
  + Avoid Relying on Spoofable Headers for Authentication
  + Implement Centralised Logging and Correlation
  + Block Fragmentation and Anomalous Packets
  + Practise Network Segmentation and Least Privilege
  + Maintain Patching and Configuration Hygiene
  + Conduct Regular Penetration Testing
* Final Analysis

### **Lab Environment**

The lab consists of two virtual machines on the 192.168.1.0/24 segment. The attacker runs Kali Linux at 192.168.1.17 with Nmap 7.99, while the target runs Ubuntu at 192.168.1.5 and exposes an SSH service on port 22 (and HTTP on port 80 in later sections). The Ubuntu host also acts as the iptables firewall, with rules added or modified throughout the walkthrough as the defender reacts to each new evasion technique. Wireshark captures every probe from the attacker side using the display filter “ip.addr == 192.168.1.5”, which isolates the relevant traffic and exposes the precise packet structure produced by each Nmap scan mode.

### **Understanding Nmap scan signatures**

The following image maps three diagnostic fields—TCP flags, data length, and TTL—across five Nmap scan modes, revealing exactly how each leaks its identity to an IDS.

**-sT (TCP connect)**: Flags follow a textbook handshake (SYN → SYN,ACK → ACK, then RST,ACK teardown). Data length is 60 bytes because the OS kernel attaches full options: MSS, window scale, timestamp, SACK permitted. TTL is the native 64—no Nmap fingerprint, but every connection hits application logs.

**-sS (Stealth SYN**): Flags abort mid-handshake (SYN → SYN,ACK → RST), never completing. Data length drops to 44 bytes since Nmap’s raw socket includes only MSS, omitting the three options a kernel-built SYN always carries. TTL is below 64, often randomized—a non-default outbound TTL alone is suspicious to tuned sensors.

**-sF (FIN)**: Flag is a lone FIN with no prior session, illegal per RFC 793; open ports stay silent, closed ports reply RST. Data length collapses to 40 bytes—20B IP plus 20B TCP, zero options. TTL is sub-64, custom-set. This trio is an immediate IDS hit.

**-sN (Null)**: Flag field is completely empty—zero control bits, something no legitimate stack emits. Data length 40 bytes, identical raw template. TTL sub-64. Length 40 plus no flags plus odd TTL is a signature signed by Nmap.

**-sX (Xmas)**: Flags FIN, PSH, URG illuminated together—impossible on a real opening packet. Data length 40 bytes, TTL sub-64; the most recognizable signature in the wild.

Together, these three fields convert Nmap probes into self-labeling traffic—signature gold for IDS engines worldwide.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjk79MXkl-I4bmww2D20pUsSXqH9HpIsPAgU5F_N-IW0gDVw8YjvG99phUA6jW1MFLV5ISeYM2bNfRSatXxUrnc12hzx7ddF0RHNWVBKigviV_QW7G4HEUUDbHc_4BgjcP6QQ3lnawaAtMqNJhOMLpwBqgqztF6haXjSur0m6GyXVLeJnlfWloOiZbDpwaM/s16000/0.jpg)

## **The Baseline: TCP Connect Scan (-sT)**

A TCP Connect scan completes the full three-way handshake by invoking the operating system’s connect() system call. It produces the most reliable result because it uses the same code path as any normal client application, but it is also the noisiest scan available in Nmap. This scan is activated through the following command:

```
nmap -sT -p 22 192.168.1.5
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjT645AdSk5ueTZo3xQx8V6de2FBru3roWvYhv-cUuiLb0xb5faWrRTVmST-OXp_BKl0-xB0f1XLKwU0d8i-Q59XWAfisTePN2FzGAbcPn18WK-BBD8h_8MjWrEKlE6Yo433oQJFt3c0z2jWNeIqSKVr2zQbXPINpg6KVTvfiUhjrVt-ST7fH3NLTmHNrLi/s16000/1.png)

Nmap reports port 22/tcp as open with the SSH service identified, confirming that no filtering currently exists between the two hosts.

The image below shows the corresponding network traffic of the scan in Wireshark. The exchange contains a SYN, a SYN-ACK, and a final ACK followed by RST-ACK, which proves that the kernel completed a real connection before tearing it down. Two fingerprintable values stand out in the IPv4 header:...