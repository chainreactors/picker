---
title: Turla Turns Kazuar Backdoor Into Modular P2P Botnet for Persistent Access
url: https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html
source: The Hacker News
date: 2026-05-15
fetch_date: 2026-05-16T05:15:44.676693
---

# Turla Turns Kazuar Backdoor Into Modular P2P Botnet for Persistent Access

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Turla Turns Kazuar Backdoor Into Modular P2P Botnet for Persistent Access](https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html)

**Ravie Lakshmanan**May 15, 2026Botnet / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8BT1AOScncZQM_A-0WBdCzTDAHGHSey48_Mywhij-TJupCdzP3s3o-MIImRtMZcoV2OqX3RjRV4COpVqkB1mrH3d_zjwvSTwCEXOq_2m80HgDo-xwAZ1KpR1h8eN9dAHGcKN_PpcE0cBsnv67FcthDycHLBJMYs8NkPszWNiQqdbhyL0YIlwVJn4NtgaR/s1700-e365/code.jpg)

The Russian state-sponsored hacking group known as
**[Turla](https://thehackernews.com/2025/07/secret-blizzard-deploys-malware-in-isp.html)**
has transformed its custom backdoor Kazuar into a modular peer-to-peer (P2P) botnet that's engineered for stealth and persistent access to compromised hosts.

Turla, per the U.S. Cybersecurity and Infrastructure Security Agency (CISA), is assessed to be affiliated with Center 16 of Russia's Federal Security Service (FSB). It overlaps with activity traced by the broader cybersecurity community under the names ATG26, Blue Python, Iron Hunter, Pensive Ursa, Secret Blizzard (formerly Krypton), Snake, SUMMIT, Uroburos, Venomous Bear, Waterbug, and WRAITH.

The hacking group is known for its attacks targeting government, diplomatic, and defense sectors in Europe and Central Asia, as well as
[endpoints previously breached by Aqua Blizzard](https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html)
(aka Actinium and Gamaredon) to support the Kremlin's strategic objectives.

"This upgrade aligns with Secret Blizzard's broader objective of gaining long-term access to systems for intelligence collection," the Microsoft Threat Intelligence team
[said](https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/)
in a report published Thursday. "While many threat actors rely on increasing usage of native tools (living-off-the-land binaries (LOLBins)) to avoid detection, Kazuar's progression into a modular bot highlights how Secret Blizzard is engineering resilience and stealth directly into their tooling."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

A key tool in Turla's arsenal is
[Kazuar](https://thehackernews.com/2024/12/secret-blizzard-deploys-kazuar-backdoor.html)
, a
[sophisticated .NET backdoor](https://thehackernews.com/2023/11/turla-updates-kazuar-backdoor-with.html)
that has been consistently put to use since 2017. The latest findings from Microsoft charts its evolution from a "monolithic" framework into a modular bot ecosystem featuring three distinct component types, each with its own well-defined roles. These changes enable flexible configuration, reduce observable footprint, and facilitate broad tasking.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi58cEcaYYTALrjjxOzEDzah6YL_6w8HwTluSdahy2WR1zczaIh38gTTuC5atacFNUnvEkZ1w4b_inDCoeO9QB6h4hDUgXZImhSmGK0q_BzW0M1yEJPcql-BoBkk9xd6ssx4R_iYxGN5eUGZ-49rFGtdxGTMrV3i8FpVB3XB5SmgoQYz1IUjitKRGUczVIG/s1700-e365/command.jpg) |
| Overview of Kernel, Bridge, and Worker module interactions |

Attacks distributing the malware have been found to rely on droppers like Pelmeni and ShadowLoader to decrypt and launch the modules. The three module types that form the foundation for Kazuar's architecture are listed below -

* **Kernel**
  , which acts as the central coordinator for the botnet by issuing tasks to Worker modules, manages communication with the Bridge module, maintains logs of actions and collected data, performs anti-analysis and sandbox checks, and sets up the environment by means of a configuration that specifies various parameters related to command-and-control (C2) communication, data exfiltration timing, task management, file scanning and collection, and monitoring.
* **Bridge**
  , which acts as a proxy between the leader Kernel module and the C2 server.
* **Worker**
  , which logs keystrokes, hooks Windows events, tracks tasks, and gathers system information, file listings, and Messaging Application Programming Interface (
  [MAPI](https://learn.microsoft.com/en-us/cpp/mfc/mapi)
  ) details.

The Kernel module type exposes three internal communication mechanisms (via Windows Messaging, Mailslot, and named pipes) and three different methods for contacting attacker-controlled infrastructure (via Exchange Web Services, HTTP, and WebSockets). The component also "elects" a single Kernel leader to communicate with the Bridge module on behalf of the other Kernel modules.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_cUA5Cw9wa7tMBSDOgubTj1Ftz9v7BAxDggLd1bOmuf-YOgVekjm68z2BfDgi5gKAJGIm8KlACJYcvpuXIBXtoGlw-mggBX-93_n8hh0zyXWZi-p_6vlmbsKd4AG3ytNRktnCOGA07b0ZvA-ROAgYV6WLkP2PsTGm77SuzPfTCNTovB3Epbb7tI_K462t/s1700-e365/worker.jpg) |
| How the Kernel leader coordinates Worker tasking and uses the Bridge |

"Elections occur over Mailslot, and the leader is elected based on the amount of work (length of time the Kernel module has been running) divided by interrupts (reboots, logoffs, process terminated)," Microsoft explained. "Once a leader is elected, it announces itself as the leader and tells all other Kernel modules to set SILENT. Only the elected leader is not SILENT, which allows the leader Kernel module to log activity and request tasks through the Bridge module."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Another function of the module is to initiate various threads to set up a named pipe channel between Kernel modules for inter-Kernel communications, specify an external communication method, as well as facilitate Kernel-to-Worker and Kernel-to-Bridge communication over Windows messaging or Mailslot.

The end goal of the Kernel is to poll new tasks from the C2 server, parse incoming messages, assign tasks to the Worker, update configuration, and sen...