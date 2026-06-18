---
title: Junior Hacker Used Tailscale and OpenSSH to Keep Access After His C2 Went Offline
url: https://thehackernews.com/2026/06/junior-hacker-used-tailscale-and.html
source: The Hacker News
date: 2026-06-17
fetch_date: 2026-06-18T06:51:58.917349
---

# Junior Hacker Used Tailscale and OpenSSH to Keep Access After His C2 Went Offline

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Junior Hacker Used Tailscale and OpenSSH to Keep Access After His C2 Went Offline](https://thehackernews.com/2026/06/junior-hacker-used-tailscale-and.html)

**Swati Khandelwal**Jun 17, 2026Malware / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhN4ptzzF7u-dzNyOc4F1HsCUbEszvkkeD1ZVl7MHQNXXcUtgqb40Wgodu3aj61QDzaNsX0eJjRDGK1eNJLCbud-4iWHJjnpHPuCfTak2m9UydSW4DEJErr5L2V_KwD39P__6iVxgaOhH8mYtY2LhPFnyCavP8eJ_1N3QpGo4NkZaFJYVRc-LX0droem8Q/s1700-e365/cyber.jpg)

A French-speaking attacker broke into a small French automotive business, planted a keylogger, and stole banking and email credentials.

Ordinary stuff, until one move near the end.

Before his command-and-control server went dark, he installed OpenSSH and Tailscale on a victim's machine, building a way back in that did not run through the C2 at all. When the Havoc server went offline the next day, his access did not. Eighteen days later, the C2 came back, his agents reconnected on their own, and he carried on.

Cato Networks captured the whole operation command by command, 339 of them over 33 days, after the operator left his SSH keys and a step-by-step playbook in an open storage bucket. The write-up, published Tuesday by Cato CTRL researcher Vitaly Simonovich, is a rare view of an intrusion from the operator's keyboard rather than the forensic leftovers.

Researchers' lesson is blunt: pulling a C2 server offline is not remediation if the attacker has already built a separate door.

The actor, handle "Poisson," is not an APT. Researchers [describe](https://www.catonetworks.com/blog/cato-ctrl-operation-poisson-analyzing-a-cybercriminals-entire-operation/) a junior operator on what looks like a school schedule, active after 3 p.m. CET with a long midday gap, all of it running on free-tier kit: DuckDNS, Backblaze B2, and a cheap IONOS VPS in Berlin. His tradecraft was thin.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

He leaked his home directory five times, named his storage buckets after his own handle, and left a test file of his own keystrokes typed over and over inside the keylogger package. He failed at roughly half of what he tried. He compromised four machines anyway.

## The chain

The malware ran almost entirely in memory. A VBScript stager with a sandbox-evasion delay decrypted a PowerShell loader, which pulled down a .NET loader that ran [Havoc's Demon agent](https://thehackernews.com/2023/02/threat-actors-adopt-havoc-framework-for.html) without dropping the implant to disk. For elevation, he used Start-Process -Verb RunAs, which is not a silent UAC bypass. It pops the Windows consent prompt and waits for someone to click Yes. On one victim, it took a dozen tries across two days.

After that came the nailing-down: a scheduled task running at every logon with highest privileges, shellcode injected into Explorer.exe, and a custom-built RustDesk as a backup channel. The credential grabber was a 70-line Python keylogger that wrote keystrokes to a local file, with no beacon and no exfil server. Poisson just logged in, grabbed the file by hand, and ran powercfg to keep the machines from sleeping, so harvesting never paused.

## The move that matters

On April 7, in a five-hour overnight session, he installed OpenSSH Server and Tailscale, joined the victim's machine to his private Tailscale network, and set up key-based SSH and a reverse tunnel. Now he could reach the machine over Tailscale's encrypted mesh with no C2 and no exposed ports.

The next day, the Havoc infrastructure went offline. Cato does not say why, and it barely matters: the Tailscale path sat on a separate network, so the access lived.

When the C2 returned on April 26, the agents reconnected automatically, no re-compromise required. Over the final five days, he ran 145 more commands, probed smart-card and certificate stores (a sign he was eyeing certificate-based logins), ran two unexplained executables from a file named Thales.zip for about 32 minutes total, then deleted 17 files and went quiet on May 1.

What he wanted was narrow. No Mimikatz, no lateral movement, no ransomware, and no sign he took the documents he browsed, from tax records to insurance. Just what people type: banking logins, email passwords, government portals. For a small business owner, that is direct financial exposure.

None of the tools is new, which is the point. China's [APT31](https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html) used Tailscale through 2024 and 2025 to tunnel quietly out of Russian IT firms, [Scattered Spider](https://thehackernews.com/2023/11/us-cybersecurity-agencies-warn-of.html) has leaned on legitimate remote-access tools like Ngrok and Fleetdeck, and RustDesk, Poisson's backup channel, turns up in recent [Akira ransomware](https://thehackernews.com/2025/09/sonicwall-ssl-vpn-flaw-and.html) intrusions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The binaries are signed and legitimate, so detection that stops at bad files, not bad behavior, misses them. What Poisson adds is command-level proof that the trick outlives a takedown, run by someone clearly still learning.

## What to watch

Cato's hunting list is concrete:

* Alert when OpenSSH Server installs on a Windows workstation, which is rarely legitimate.
* Watch for tailscale.exe on machines that have no reason to run a VPN.
* Look for ssh -R reverse tunnels heading to outside hosts.
* Check for wscript.exe running .vbs files out of user staging folders.
* Flag scheduled tasks set to the highest privileges that launch script interpreters.
* Watch for powercfg standby-timeout changes that keep machines awake.
* Block DuckDNS.

The bigger one: when you find a C2, assume it is not the only way in, and go hunting for the quiet persistence layer behind it.

What was in Thales.zip, and what those two programs did in their 32 minutes on the machine, is the questio...