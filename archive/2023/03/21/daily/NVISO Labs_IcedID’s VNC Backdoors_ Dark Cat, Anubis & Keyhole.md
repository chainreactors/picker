---
title: IcedID’s VNC Backdoors: Dark Cat, Anubis & Keyhole
url: https://blog.nviso.eu/2023/03/20/icedids-vnc-backdoors-dark-cat-anubis-keyhole/
source: NVISO Labs
date: 2023-03-21
fetch_date: 2025-10-04T10:08:45.510505
---

# IcedID’s VNC Backdoors: Dark Cat, Anubis & Keyhole

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# IcedID & Qakbot’s VNC Backdoors: Dark Cat, Anubis & Keyhole

[Maxime Thiebaut](https://blog.nviso.eu/author/maxime-thiebaut/ "Posts by Maxime Thiebaut")

[Videos](https://blog.nviso.eu/category/videos/), [Forensics](https://blog.nviso.eu/category/forensics/), [Reverse Engineering](https://blog.nviso.eu/category/reverse-engineering/)

March 20, 2023April 26, 2023
13 Minutes

IcedID (a.k.a. BokBot) is a popular Trojan who [first emerged in 2017 as an Emotet delivery](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/). Originally described as a banking Trojan, IcedID shifted its focus to embrace the extortion/ransom trend and nowadays acts as an initial access broker mostly delivered through malspam campaigns. Over the last few years, [IcedID has commonly been seen delivering Cobalt Strike prior to a multitude of ransomware strains](https://thedfirreport.com/category/icedid/) such as Conti or REvil.

IcedID itself is composed of multiple modules, one of which is a poorly documented VNC backdoor ([Virtual Network Computing](https://en.wikipedia.org/wiki/Virtual_Network_Computing)) acting as a cross-platform remote desktop solution. Existence of this module (branded “HDESK” or “HDESK bot”) is just partially mentioned by [Malwarebytes (2017)](https://www.malwarebytes.com/blog/news/2019/12/new-version-of-icedid-trojan-uses-steganographic-payloads) and [Kaspersky (2021)](https://securelist.com/trickbot-module-descriptions/104603/) while its usage has been widely observed and [occasionally vulgarized](https://isc.sans.edu/diary/rss/29210) as “Dark VNC”.

As part of our research efforts, NVISO has been analyzing IcedID and Qakbot’s command & control communications. **In this blog-post we will share insights into IcedID and Qakbot’s VNC backdoor(s) as seen from an attacker’s perspective**, insights we obtained by extracting and reassembling VNC ([RFC6143](https://www.rfc-editor.org/rfc/rfc6143)) traffic embedded within private and [public captures published by Brad Duncan](https://malware-traffic-analysis.net/index.html).

In this post we introduce the three variants we observed as well as their capabilities: [Dark Cat](#dark-cat-vnc), [Anubis](#anubis-vnc) and [Keyhole](#keyhole-vnc). We’ll follow by exposing [common techniques employed by the operators](#modus-operandi) before revealing [information they leaked through their clipboard data](#clipboard-leaks).

**Bokbot or Qakbot?**

This research was originally titled *“IcedID’s VNC Backdoors: Dark Cat, Anubis & Keyhole”* and focused solely on IcedID (Bokbot). [Brad however correctly pointed-out](https://infosec.exchange/%40malware_traffic/110193215515648860) that Dark Cat is only leveraged by Qakbot, samples which were mistakenly included in this research after being confused with Bokbot (IcedID).

IcedID and Qakbot VNC traffic remains extremely similar as can be observed in the following three VNC backdoors.

# HDESK Variants

During our analysis of both public and private IcedID and Qakbot network captures, we identified 3 VNC backdoor variants, all part of the HDESK strain. These backdoors are typically activated during the final initial-access stages to initiate hands-on-keyboard activity. Supposedly short for “Hidden Desktop”, HDESK leverages Windows features allowing the backdoor to create a hidden desktop environment not visible to the compromised user. Within this hidden environment, the threat actors can start leveraging the user interface to perform regular tasks such as web browsing, reading mails in Outlook or executing commands through the Command Prompt and PowerShell.

We believe with medium confidence that these backdoors share origins as the the Dark Cat interface (used by Qakbot) has traits that can later be found within Anubis and Keyhole interfaces (used by IcedID).

## Dark Cat VNC

The “Dark Cat VNC” variant was first observed in November 2021 and is believed to be the named releases `v1.1.2` and `v1.1.3` used by Qakbot. Its usage was still extensively observed by the end of 2022. Upon initial access, the home screen presents the operator with multiple options to create new sessions alongside backdoor metrics such as idle time or lock state.

![Figure 1: The Dark Cat VNC interface.](https://blog.nviso.eu/wp-content/uploads/2023/03/001200.2021-11-05T17-16-21987.jpeg)

Figure 1: The Dark Cat VNC interface.

### User Session

Figure 2: A Dark Cat `USER` session.

The `USER` session exists in three variations (`read`, standard and `black`) which allows the operator to switch the VNC view to the user’s visible desktop.

### HDESK Session

The `HDESK` session exists in three variations as well: standard, `Tmp` and `NM` (also called `bot`). This session type causes the backdoor to create a new hidden desktop not visible to the compromised user.

Based on the activity we observed, the `HDESK` sessions are (understandably) preferred by the operators.

Figure 3: A Dark Cat `HDESK` session.

As `HDESK` sessions by default do not benefit from Windows’s built-in UI, operators are presented with an alternative start-menu to launch common programs. In Dark Cat these are Chrome, Firefox, Internet Explorer, Outlook, Command Prompt, Run and the Task Manager. A Windows Shell button is also foreseen which we believe, if used, will spawn the regular Windows UI most of the users are used to. Starting with Dark Cat `v1.1.3` Edge Chromium furthermore joins the list of available software.

![Figure 4: The Dark Cat HDESK session interface.](https://blog.nviso.eu/wp-content/uploads/2023/03/001859.2021-11-05T17-16-28071.jpeg)

Figure 4: The Dark Cat `HDESK` session interface.

Besides the alternate start-menu, operators can access some settings using the top-left orange icon which includes:

* Defining the hidden windows’ sizes.
* Defining the Chrome profile to use (lite or not).
* Deleting the browser’s profile(s).
* Killing the child process(es).

Figure 5: The Dark Cat `HDESK` settings interface.

### WebCam Session

The `WebCam` sessions exist in three variations. While we were unable to capture its usage (honeypots lack webcams and operators do not attempt to use this session kind), its presence suggests IcedID’s VNC backdoors are capable of capturing compromised devices’ webcam feeds.

## Anubis VNC

The “Anubis VNC” variant was first observed in January 2022 and is believed to be the named...