---
title: The Behavior of Coordinated SSH Brute Force Attacks over the last three months &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)
url: https://isc.sans.edu/diary/rss/33086
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-18
fetch_date: 2026-06-19T07:09:08.961393
---

# The Behavior of Coordinated SSH Brute Force Attacks over the last three months &#x5b;Guest Diary&#x5d;, (Wed, Jun 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33084)
* [next](/diary/33090)

Click HERE to learn more about classes Guy is teaching for SANS

# [The Behavior of Coordinated SSH Brute Force Attacks over the last three months [Guest Diary]](/forums/diary/The%2BBehavior%2Bof%2BCoordinated%2BSSH%2BBrute%2BForce%2BAttacks%2Bover%2Bthe%2Blast%2Bthree%2Bmonths%2BGuest%2BDiary/33086/)

**Published**: 2026-06-17. **Last Updated**: 2026-06-18 01:49:29 UTC
**by** [Adam Nason, SANS.edu BACS Student](/handler_list.html#adam-nason,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/The%2BBehavior%2Bof%2BCoordinated%2BSSH%2BBrute%2BForce%2BAttacks%2Bover%2Bthe%2Blast%2Bthree%2Bmonths%2BGuest%2BDiary/33086/#comments)

[This is a Guest Diary by Adam Nason, an ISC intern as part of the [SANS.edu](https://www.sans.edu/cyber-security-programs/bachelors-degree/) BACS program]

Brute force SSH attacks are an ever-present threat on the internet today. We examine probing behavior over the last three months to identify coordinated and opportunistic attacks by threat actors. A DShield Honeypot has quietly collected and logged the behavior of these threat actors to develop a clearer picture of their malicious intentions. During the log collection period, several significant cyber and geopolitical events occurred. We will take a closer look at these behaviors by analyzing their timing and cross-referencing them with external factors that align with their attack patterns. Can an increase or change in SSH brute force botnet activity be observed during these volatile times?

**Infrastructure Setup and Data Collection Framework – Home Lab**

**Infrastructure**
• Raspberry Pi 4 Model B
• Network Equipment – Isolated from personal home network
  o UniFi Security Gateway Pro
  o UniFi 24 Port Switch

**Data Ingestion**
• RaspberryOS running on Raspberry Pi
• DShield Honeypot Software
  o Logs Collected: 17 Feb 2026 through 26 May 2026

**Software Tools**
• Elasticsearch, Logstash, Kabana (ELK)
• Microsoft VS Code (JSON and Python)
• Microsoft Excel

**Data Analysis of Honeypot Logs**

**Scanning Volume and Timeline Overview**

The cowrie honeypot logs recorded over 20 million SSH brute-force attempts over the past 100 days. Investigation into the scanning trends appears to be closely correlated with Chinese botnets, major law enforcement actions, geopolitical events, and critical cybersecurity advisories released in the first half of 2026. As shown in Figure 1: Daily Brute Force Probing Totals, the timeline shows extended periods of high-volume traffic, with abrupt spikes and drops that seem to align with external events.

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic1.png)
Table 1: *Overview of SSH data collected*

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic2.png)
Figure 1: *Daily Brute Force Probing Totals*

**Notable events within the brute force scan timeline**

**February 17 – 24 (Initial Baseline)**

The first week of running the honeypot produced what can be considered a quiet baseline of standard background scanning activity. During this period, between 200 and 400 attempts were captured each day.

**February 25 – 28 (Sudden Surge)**

Following a quiet start, a spike of over 2100% attempts was observed by the honeypot. It was during this period that CISA published Emergency Directive 26-03 (CISA, 2026), related to Cisco’s software-defined wide-area network, which led to opportunistic attacks against unpatched systems. Additional probing was observed during this period, which can also be attributed to the rising conflict between Iran, Israel, and the United States (Al Jazeera, 2026).

**March 1 – 8 (Activity Peaks)**

Scanning observations peaked this week, with over 300,000 events collected on March 8th (Radauskas, 2026). This is as tensions continue to rise between Iran, Israel, and the United States, and both advanced persistent threats and opportunistic botnets are becoming more active (Reuters, 2026).

**March 9 – April 14 (Sustained Attacks)**

The honeypot continues to collect and log a high volume of activity during this period, with daily probes remaining above 50,000, often exceeding 100,000 (Le Poidevin, 2026). The periodic spikes and dips tend to lean towards automated attack campaigns.

**April 15 (Rapid Decline)**

Attack observations plummet to just over 23,000 attempts logged by the honeypot.

**April 16 – May 14 (Attack Rebounds)**

With news of new vulnerabilities (CISA, 2026), and tensions growing with the Iran-United States ceasefire, logged scans start to rise again. A second spike is observed on May 2nd with 244,344 probes in a single day. This comes just after 24 hours following a major Linux vulnerability that was published by CISA (CISA, 2026)

**May 15 – 23 (Extended Decline)**

Daily log observations drop nearly 95%, as the ceasefire extends (Madhani et al., 2026), and opportunistic threat actors lose interest as the Iran, Israel, and United States war continues to drag on with minimal active military engagements.

**Top 10 Identified Probing IPs (Patterns, Clusters, and Campaign Data)**

From February 2026 through May 2026, the top ten observed IP addresses (Table 2) appeared to have strong geographic and Autonomous System Number (ASN) clustering. Both DigitalOcean (ASN – AS14061) and M247 (ASN – AS9009) show activity from multiple countries (Table 3). Furthermore, synchronized scanning bursts can be observed using identical SSH client fingerprints and version strings, occurring within minutes of each other across different countries.

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic3.png)
Table 2: *Top Ten Probing IPs, with Country and ASN*

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic4.png)
Table 3: *Country Clustering of IPs and ASN*

A closer review of the data shows an example of what appears to be synchronized scanning. Over the course of 53 seconds, two attacks are observed from both the United States and Ukraine. Of note, both attacks exhibit the same HASSH fingerprint. HASSH is a fingerprinting standard developed by the Detection Cloud team at Salesforce and is used to detect attacks with higher granularity than a simple IP address can (Reardon, 2022). Seeing the same HASSH, SSH Version, from two different ASNs and countries does point to a high likelihood of a coordinated attack.

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic5.png)
Table 4: *Clustered attack within 53-seconds*

Further review of the collected honeypot logs shows that 702,706 events use the exact same HASSH fingerprint (03a80b21afa810682a776a7d42e5e6fb) and SSH version, indicating the use of a single managed attack toolkit that has been deployed globally (SSHwatch, 2025).

Finally, a detailed review of the logs shows evidence of a botnet quota assignment (Table 5). These are throttled scan rates, which are tell-tale indicators of a botnet-driven SSH campaign. Reviewing the logs over such extended periods shows a low variation and high uniform attack rates, which point to a controller assigning quotas or workloads to the botnet zombies under its control. Automating a scan in this type of organization has been shown to be a characteristic of these types of programmed botnet operations (Sing et al., 2024 p. 1731-1750).

![](https://isc.sans.edu/diaryimages/images/Adam_Nason_pic6.png)
Table 5: *Attack Rate Analysis of IPs showing Automated Campaigns*

**Reduce your Attack Surface**

As we have seen above, networks are under constant attack, which seems to follow the ebb and flow of external events on digital cyberspace. However, there are several steps you can take to reduce your attack surface, most of which require little effort. Strategies like IP blocks, geo-blocking, and changing default values can go a long way in preventin...