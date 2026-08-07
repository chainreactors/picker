---
title: 22 Seconds to Compromise: How Automated SSH Actors Move From Login to Persistence Before You Can Blink &#x5b;Guest Diary&#x5d;, (Thu, Aug 6th)
url: https://isc.sans.edu/diary/rss/33220
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-06
fetch_date: 2026-08-07T04:27:14.015361
---

# 22 Seconds to Compromise: How Automated SSH Actors Move From Login to Persistence Before You Can Blink &#x5b;Guest Diary&#x5d;, (Thu, Aug 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33218)

Click HERE to learn more about classes Guy is teaching for SANS

# [22 Seconds to Compromise: How Automated SSH Actors Move From Login to Persistence Before You Can Blink [Guest Diary]](/forums/diary/22%2BSeconds%2Bto%2BCompromise%2BHow%2BAutomated%2BSSH%2BActors%2BMove%2BFrom%2BLogin%2Bto%2BPersistence%2BBefore%2BYou%2BCan%2BBlink%2BGuest%2BDiary/33220/)

**Published**: 2026-08-06. **Last Updated**: 2026-08-06 00:15:40 UTC
**by** [Daryl Jiminez, SANS.edu BACS Student](/handler_list.html#daryl-jiminez,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/22%2BSeconds%2Bto%2BCompromise%2BHow%2BAutomated%2BSSH%2BActors%2BMove%2BFrom%2BLogin%2Bto%2BPersistence%2BBefore%2BYou%2BCan%2BBlink%2BGuest%2BDiary/33220/#comments)

[This is a Guest Diary by Daryl Jiminez, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Introduction**

On May 23, 2026, a threat actor successfully authenticated to my Cowrie SSH honeypot using compromised credentials and, within 22 seconds, injected a backdoor SSH key, changed the root password, attempted to clear host-based access restrictions, and performed automated system reconnaissance. The speed and consistency of the behavior left no room for doubt: this was not a human attacker manually working through a system. This was automated post-exploitation infrastructure executing a pre-scripted playbook the instant it found an open door.

This post documents that intrusion, the broader campaign it belongs to, and what defenders can do about it. The data comes from a self-managed Raspberry Pi 5 honeypot running Cowrie, operating continuously since April 2026 as part of my SANS Internet Storm Center internship. Over the 30-day monitoring period analyzed here, the sensor captured over 112,000 SSH sessions and 72,000+ authentication attempts from 175+ unique malicious source IPs.

**The Sensor and Setup**

The honeypot runs Cowrie v2.3.0 on a Raspberry Pi 5 with a residential internet connection. Cowrie simulates an SSH server that accepts connections on port 2222 (forwarded from external port 22), logs all attacker activity including commands, file transfers, and credentials, and submits data automatically to ISC DShield. The sensor's logs are archived daily and analyzed for attacker TTPs, campaign patterns, and threat intelligence value.

All data referenced in this post was extracted from raw JSON Cowrie logs using jq queries and cross-referenced against AbuseIPDB, VirusTotal, GreyNoise, ISC DShield, AlienVault OTX, Shodan, and Whois.

**The Intrusion: 22 Seconds From Login to Persistence**

At 01:06:43 UTC on May 23, 2026, source IP 163.7.8.79 initiated an SSH connection to the honeypot. One second later, the actor successfully authenticated using the credentials root / Aa123123123, a weak password consistent with credentials leaked in past data breaches and commonly cycled through automated attack tools.

What happened next is best understood through the session timeline:

**Session Timeline — 163.7.8.79 — May 23, 2026**
![](https://isc.sans.edu/diaryimages/images/Daryl_Jiminez_pic1.png)

The SSH key injected into authorized\_keys was captured by Cowrie with the following hash:
a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2
The actor also removed the existing .ssh directory and recreated it before injecting the key, a technique used to eliminate existing authorized keys and ensure exclusive backdoor access. Changing the root password immediately after key injection further locks out legitimate administrators. Clearing /etc/hosts.deny removes any host-based access restrictions that might block future connections from the actor's infrastructure.

The entire sequence executed in 22 seconds. There was no hesitation, no exploration, no human decision-making visible in the command pattern. This is automation: a pre-scripted playbook executing the moment authentication succeeded.

**The Attacker Kept Coming Back**

After reviewing the full May 23 logs, I found that 163.7.8.79 returned to the sensor multiple times throughout the day, reconnecting approximately every few minutes and executing the same automated command sequence on each successful session. The consistency across sessions, identical command order, identical timing patterns, identical SSH key material, confirms this is not a human operator adapting to findings but an automated tool running a fixed exploitation script.

When I queried the logs for all successful authentications on May 23, I found 21 successful logins from 21 different source IPs within a single 24-hour period. The logins were clustered heavily between 01:00 and 02:30 UTC, suggesting coordinated wave-based scanning rather than independent actors discovering the honeypot randomly. A sample of the credentials used shows the breadth of the wordlists being deployed:

![](https://isc.sans.edu/diaryimages/images/Daryl_Jiminez_pic2.png)

The presence of 'minecraft / 12345' is particularly noteworthy. Someone compiled a wordlist that includes gaming server default credentials, indicating active scanning for Minecraft or similar game server installations, not just generic Linux systems.

**The Campaign Is Not Isolated and Has Not Stopped**

To understand whether this was a one-time event or part of a sustained campaign, I cross-referenced the full list of IPs my sensor had observed over 30+ days of operation against a compiled list of IPs associated with the mdrfckr SSH campaign, a persistent automated SSH scanning operation that has been documented across multiple honeypot operators worldwide.

The result: 93 IPs from the mdrfckr campaign list were still actively hitting my sensor weeks after first being documented. This is not a historical observation. These actors did not stop. The campaign has been running continuously throughout the monitoring period.

Additionally, analysis of the top connecting IPs by session volume revealed a coordinated subnet cluster:

80.94.92.184    — high volume connections
80.94.92.186    — high volume connections
80.94.92.171    — high volume connections

Three IPs from the same /24 subnet hitting the sensor simultaneously is not coincidence. This is coordinated scanning infrastructure, either a botnet or a distributed scanning platform, operating multiple nodes from the same network block to maximize coverage while distributing the load.

**Threat Intelligence on 163.7.8.79**

Cross-referencing the primary actor IP across multiple threat intelligence platforms confirmed its malicious reputation:
AbuseIPDB: 100% confidence of abuse, over 5,700 reported incidents primarily related to SSH brute-force attacks, with recent reports confirming continued active scanning activity.
VirusTotal: Multiple security vendors classify the IP as malicious or suspicious.
GreyNoise: Identified as part of internet-wide SSH brute-force and reconnaissance scanning activity, confirming this is not a targeted attack but systematic exploitation of any reachable vulnerable host.
Whois: The IP is associated with Byteplus infrastructure (AS150436), a cloud hosting provider, consistent with the pattern of actors using cloud resources to scale automated attack campaigns.

**MITRE ATT&CK Mapping**

T1078 — Valid Accounts: Actor authenticated using compromised credentials from a wordlist.
T1098 — Account Manipulation: Malicious SSH key injected into authorized\_keys to establish persistent access.
T1059 — Command Execution: Multiple shell commands executed immediately following authentication.
T1562 — Impair Defenses: /etc/hosts.deny cleared and processes terminated to remove access restrictions.

**Why This Matters**

The 22-second compromise window is the most important takeaway from this obs...