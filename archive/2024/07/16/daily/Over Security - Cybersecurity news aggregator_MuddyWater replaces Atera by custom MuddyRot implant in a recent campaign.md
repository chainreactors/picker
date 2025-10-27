---
title: MuddyWater replaces Atera by custom MuddyRot implant in a recent campaign
url: https://blog.sekoia.io/muddywater-replaces-atera-by-custom-muddyrot-implant-in-a-recent-campaign/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-16
fetch_date: 2025-10-06T17:45:23.339947
---

# MuddyWater replaces Atera by custom MuddyRot implant in a recent campaign

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# MuddyWater replaces Atera by custom MuddyRot implant in a recent campaign

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR](#molongui-disabled-link)
July 15 2024

0

7 minutes reading

*This report was originally published for our customers on 20*June* 2024.*

---

*Today, the Check Point Research (CPR) team [published](https://research.checkpoint.com/2024/new-bugsleep-backdoor-deployed-in-recent-muddywater-campaigns/) a report on the same implant, providing details of recent MuddyWater campaigns.*

## Table of contents

* [Introduction](#h-introduction)
* [Technical analysis](#h-technical-analysis)
  + [Recent infection chain](#h-recent-infection-chain)
  + [MuddyRot analysis](#h-muddyrot-analysis)
  + [Persistence](#h-persistence)
  + [C2 communication of the “MuddyRot” malware](#h-c2-communication-of-the-muddyrot-malware)
  + [Reverse Shell](#h-reverse-shell)
* [Conclusion](#h-conclusion)
* [MuddyWater IOCs](#h-muddywater-iocs)

## Introduction

On June 9 2024, ClearSky [tweeted](https://x.com/ClearskySec/status/1799829814011994120) about a new campaign associated with the MuddyWater intrusion set, employed by the Iranian intelligence service MOIS (Ministry of Intelligence) against Western and Middle Eastern entities. According to the source, MuddyWater is suspected of targeting Turkey, Azerbaijan, Jordan, Saudi Arabia, and Israel, although the full list of targeted countries has not been confirmed during our investigation.

By examining the posted hashes and relevant infrastructure, we found that compared to previous campaigns, this time MuddyWater changed their infection chain and did not rely on the legitimate Atera remote monitoring and management tool (RMM) as a validator. Instead, we observed that they used a new and undocumented implant. Sekoia TDR analysts dubbed this tool ”MuddyRot”.

This report aims to compare past and current infection chains associated with MuddyWater and present a technical analysis of the “MuddyRot” malware, a new validator in the intrusion set’s arsenal.

## Technical analysis

### Recent infection chain

The MuddyWater intrusion set is known to rely primarily on two intrusion vectors when targeting Windows environments. They use public exploits to compromise internet-exposed servers, such as Exchange or SharePoint servers, and then move laterally within the network. Additionally, they send spear phishing emails from previously compromised email accounts to bypass security measures and increase the emails’ legitimacy in the recipient’s eyes.

On April 22 2024, our fellows at HarfangLab [published](https://harfanglab.io/en/insidethelab/muddywater-rmm-campaign/) a blogpost on recent MuddyWater infection chains leading to the installation of [SimpleHelp](https://simple-help.com/) (2023) and [Atera](https://www.atera.com/) (2023-2024). These infection chains involved an email (or possibly an instant messaging message) sent from a compromised account. The email included a link to an online storage service hosting a malicious ZIP archive, which contained the remote monitoring and management software.

In the recently observed campaigns, MuddyWater seems to have changed this infection chain by embedding the links in PDF files instead of emails. The one-page PDF used resembles MuddyWater’s recent emails—straightforward, without any images, and with decoys related to online courses or webinars to face cyber threats, as shown below. By clicking the embedded links, the user is redirected to a webpage hosted on the [Egnyte](https://www.egnyte.com/) service to download a ZIP archive containing the MuddyRot validator.

![Malicious PDF used by MuddyWater](data:image/svg+xml...)![Malicious PDF used by MuddyWater](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/pdfs-1024x597.png)

**Figure 1. Malicious PDF used by MuddyWater**

### **MuddyRot analysis**

The MuddyRot malware is a x64 implant developed in C with several capabilities such as reverse shell, persistence and the possibility for the operators to download and upload files from/to the compromised workstation. Upon execution, the malware carries out a series of standard tasks, such as deobfuscating strings, dynamic API loading necessary functions, and creating a mutex.

All relevant strings, such as the malware configuration, file paths, and imported methods, are obfuscated through a simple method: each character of any relevant string has its decimal value subtracted by an integer. Several integers, such as 3, 4, 5, or 6, are used for obfuscation.

![Obfuscation used by Muddywater’s rotrot implant. Source: Sekoia Threat Detection & Research Team](data:image/svg+xml...)![Obfuscation used by Muddywater’s rotrot implant. Source: Sekoia Threat Detection & Research Team](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/obf-1-1024x364.png)

**Figure 2. Obfuscation used by Muddywater’s MuddyRot implant**

The created mutex is named *DocumentUpdater,* which is checked upon execution. If it already exists, the malware stops its execution.

Moreover, to reduce its detection, the malware uses the popular and well-spread technique of dynamic import loading using the pair LoadLibrary / GetProcAddress to load methods from various DLLs. To do so, the malware uses the PE header structures to access the InMemoryOrderModuleList, a doubly linked list containing loaded modules with the structure \_LDR\_DATA\_TABLE\_ENTRY. This structure provides information about the DLLs, including their names and address, that the malware uses to determine which DLLs to load afterwards. The malware then employs GetProcAddress to retrieve addresses of functions from Kernel32.dll, Advapi32.dll, Ole32.dll, and Ws2\_32.dll.

### **Persistence**

At the very beginning of the malware execution, MuddyRot copies itself in the c:\pro...