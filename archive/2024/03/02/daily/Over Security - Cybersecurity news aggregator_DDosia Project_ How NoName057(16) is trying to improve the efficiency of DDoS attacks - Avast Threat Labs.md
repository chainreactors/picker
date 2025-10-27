---
title: DDosia Project: How NoName057(16) is trying to improve the efficiency of DDoS attacks - Avast Threat Labs
url: https://decoded.avast.io/martinchlumecky/ddosia-project-how-noname05716-is-trying-to-improve-the-efficiency-of-ddos-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-02
fetch_date: 2025-10-04T12:13:02.961911
---

# DDosia Project: How NoName057(16) is trying to improve the efficiency of DDoS attacks - Avast Threat Labs

Blog

[Home](/blog)[News](/blog/news)[Insights](/blog/insights)[People & Impact](/blog/impact)

[Search](/blog/search)

1. [Blog Home](/blog)
2. [Insights](/blog/insights)
3. [Research](/blog/insights/research)
4. DDosia Project: How NoName057(16) is trying to improve the efficiency of DDoS attacks

Research

# DDosia Project: How NoName057(16) is trying to improve the efficiency of DDoS attacks

Enhanced DDoS Efficiency with Go

![](https://www.gendigital.com/blog/sites/default/files/styles/blogs_author_avatar_small/public/2017-10/author-profile-default.jpg.webp?itok=NuetIy0Z)

Martin a Milánek

Author at Avast Threat Labs

Published

April 18, 2023

Read time

15 Minutes

![DDosia Project: How NoName057(16) is trying to improve the efficiency of DDoS attacks](https://www.gendigital.com/blog/sites/default/files/styles/blogs_hero_tiny/public/2024-08/GettyImages-867421026_edit_1.jpg.webp?itok=jnG-kiPf)

Written by

![](https://www.gendigital.com/blog/sites/default/files/styles/blogs_author_avatar_small/public/2017-10/author-profile-default.jpg.webp?itok=NuetIy0Z)

Martin a Milánek

Author at Avast Threat Labs

Published

April 18, 2023

Read time

15 Minutes

![DDosia Project: How NoName057(16) is trying to improve the efficiency of DDoS attacks](https://www.gendigital.com/blog/sites/default/files/styles/blogs_hero_tiny/public/2024-08/GettyImages-867421026_edit_1.jpg.webp?itok=jnG-kiPf)

Share this article

Through their DDosia project, pro-Russia hacktivist group NoName057(16) is still conducting DDoS attacks, mostly with the goal to take offline websites of institutions and companies in European countries. On its Telegram channels, the group openly communicates the fact that they perform their actions in support of Russia in the war against Ukraine, and it’s apparent that their activities will further continue during the war. The group has been offering payments in cryptocurrencies to people who install their DDosia tool in order to participate in their attacks. We want to create awareness that people who have NoName057(16)’s DDoS tool installed on their computer not only participate in cybercrime, but also support the groups’ warfare activities.

We detect and block DDosia to make the internet a safer place, and we continue to track DDoS victims and configurations of the DDosia botnet because such information helps to mitigate the impact of DDoS attacks.

Since the first Python version needed to be more efficient, the group released a new Go variant of bots in late 2022. [SentinelLabs](https://www.sentinelone.com/labs/noname05716-the-pro-russian-hacktivist-group-targeting-nato) has described the first variant of the Go implementation, including the C2 servers at that time active. A few days later, [Team Cymru](https://www.team-cymru.com/post/a-blog-with-noname) published an investigation about the botnet architecture describing the DDoS attacks as a largely static infrastructure.

Given the above findings, it is apparent that the C2 structure is still evolving. The primary purpose of the following analysis is to explore the C2 architecture and current communication process between the botnet and C2 servers. Therefore, we have been actively monitoring the DDosia botnet and have found several innovations in the bot implementation and the botnet infrastructure. The C2 infrastructure is composed of one central server and two proxies forwarding bot requests. This, combined with an update mechanism, makes the botnet rather resilient to disruptions. The latest versions also include a bot authentication mechanism for all the C2 communication along with IP address blocklisting, presumably to hinder tracking of the project.

## **Implementation Overview**

The first implementation of DDosia came into the world around July 2022. Being authored by the NoName057(16) group, there was interestingly a brief coexistence with the Bobik botnet before the botnet was dismantled, presumably in favor of DDosia. It was written in Python using threads as a means of parallelism; nevertheless, it was still lacking in terms of efficacy. Since the first version, DDosia relied on HTTP protocol for C2 communication, with JSON configs distributed by the servers.

The lack of efficacy presumably motivated changes in DDosia, namely the move from Python to Go that we saw in late 2022, with [SentinelLabs](https://www.sentinelone.com/labs/noname05716-the-pro-russian-hacktivist-group-targeting-nato) describing the first Go variants. The main advantage of Go in comparison to Python is direct compilation into native code along with the absence of Python’s GIL that may severely affect the performance of threaded code in Python. Interestingly, these new versions are also multi-platform, as we’ve seen variants for all major operating systems (Windows, macOS, Linux, Android). Evidently, the bot development is still in progress, as we see new functionalities, such as HTTP authentication, being added to DDosia along with slight changes in the configuration file.

![Console output of the Go-Stresser version 1.0 – variant 1](https://www.gendigital.com/blog/sites/default/files/styles/blogs_paragraph_image_small/public/2024-06/Go-Stresser-v1.png.webp?itok=JfIegNRs)

Console output of the Go-Stresser version 1.0 – variant 1

## **Go Implementation**

Let’s take a closer look at the second variant of DDosia bot from March 6, 2023, that came up with the authentication mechanism, presumably to combat researchers snooping for lists of targets.

![Console output of the Go-Stresser version 1.0 – variant 2](https://www.gendigital.com/blog/sites/default/files/styles/blogs_paragraph_image_small/public/2024-06/Go-Stresser-v2.png.webp?itok=nYje0bsY)

Console output of the Go-Stresser version 1.0 – variant 2

###### **Build Package**

The aforementioned variant has support for multiple architecture as well as multiple platforms; unsurprisingly, it is also written in Go. The builds are distributed via the Telegram channel “Project DDosia” in the form of a zip file with the builds as follows:

* Windows x64 and arm64
* Linux x64 and arm64
* macOS x64 and arm64

The names of the executable are changed sometimes; there is a list of the captured names:

* dosia\_app\_(windows|macos|linux)\_(x64|arm64)
* d\_(win|mac|linux)\_(x64|arm64)
* pd\_(win|mac|linux)\_(x64|arm64)
* dosia\_(win|mac|linux)\_(x64|arm64)

###### **Execution Workflow**

A working dir of the bot executable must contain a text file `client_id.txt` with the `User-Hash` of the registered user. The form of the `User-Hash` is a BCrypt hash with these parameters `$2a$16$`.

The first outcome communication is to use `nordvpn.com` to get detailed information about the bot IP address that is sent to the C2 server. The second outcome is to use C2 as a `POST` method to `/login` URL with data representing information about the bot IP, user ID, and bot identification.

![Login to C2](https://www.gendigital.com/blog/sites/default/files/styles/blogs_paragraph_image_small/public/2024-06/Login-to-C2-1.png.webp?itok=vsZgx2IP)

Login to C2

The `Client-Hash` is the result of a library that returns the OS native machine UUID/GUID. It is an open-source implementation of [Go MachineID](https://github.com/denisbrodbeck/machineid#unique-key-reliability) by Denis Brodbeck. The `Client-hash` has a suffix representing the current PID (5481 in this case).

![Login response from C2 during login](https://www.gendigital.com/blog/sites/default/files/styles/blogs_paragraph_image_small/public/2024-06/Login-response-from-C2-during-login-1.png.webp?itok=_Wmoj58v)

Login response from C2 during login

If the authentication is successful, C2 returns `HTTP/1.1 200 OK` with a token in the form of epoch/Unix timestamp, and the target configuration can then be downloaded via `GET /client/get_targets`. The first variant of the DDosia bot does not implement any authentication mechanism, but the valid token is necessary to get the target configuration successfully in the current C2 architec...