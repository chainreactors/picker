---
title: RATatouille: Cooking Up Chaos in the I2P Kitchen
url: https://blog.sekoia.io/ratatouille-cooking-up-chaos-in-the-i2p-kitchen/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-12
fetch_date: 2025-10-06T20:38:33.844368
---

# RATatouille: Cooking Up Chaos in the I2P Kitchen

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

# RATatouille: Cooking Up Chaos in the I2P Kitchen

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Pierre Le Bourhis](#molongui-disabled-link)
February 11 2025

0

28 minutes reading

*This article was originally distributed as a private FLINT report to our customers on 29 January 2025.*

## Table of contents

* [Introduction](#h-introduction)
* [Sample overview](#h-sample-overview)
* [I2PRAT Malware Loader](#h-i2prat-malware-loader)
  + [Privileges review](#h-privileges-review)
  + [RPC elevation](#h-rpc-elevation)
  + [Parent ID spoofing](#h-parent-id-spoofing)
  + [How I2PRAT Uses Dynamic API Resolution for Evasion ?](#h-how-i2prat-uses-dynamic-api-resolution-for-evasion)
  + [Anti debug](#h-anti-debug)
  + [String obfuscation](#h-string-obfuscation)
* [I2PRAT (C2) Communication via I2P](#h-i2prat-c2-communication-via-i2p)
* [Defense deactivation](#h-defense-deactivation)
* [I2PRAT installer](#h-i2prat-installer)
* [I2PRAT components](#h-i2prat-components)
  + [I2PRAT DLLs breakdown](#h-i2prat-dlls-breakdown)
* [I2PRAT C2 hunting](#h-i2prat-c2-hunting)
* [I2PRAT Detection Opportunities](#h-i2prat-detection-opportunities)
  + [Privilege Escalation](#h-privilege-escalation)
  + [Privilege Escalation via process migration](#h-privilege-escalation-via-process-migration)
  + [Catch C2 communication](#h-catch-c2-communication)
  + [I2PRAT detection](#h-i2prat-detection)
  + [Change RDP settings](#h-change-rdp-settings)
  + [Rogue service creation](#h-rogue-service-creation)
  + [Detection overview in sandbox](#h-detection-overview-in-sandbox)
* [Conclusion](#h-conclusion)

## Introduction

During our daily tracking and analysis routine at TDR (Threat Detection & Research), we have been monitoring a technique known as ClickFix[1](#cd69ae21-02b4-4efc-b12e-b43a43a2485f)[2](#7cc6c067-fe73-4dd6-a928-01b992955067). One of the payloads dropped in a campaign starting from November 2024 drew our attention due to the absence of a signature and the lack of documented behaviour and network patterns in public reports. This discovery initiated our investigation into the new piece of malware **I2PRAT**.

The malware was recently identified as a multi-stage RAT (Remote Access Trojan). The first stage is protected by an initial layer of obfuscation, which is a commodity packer. Developed in C++, the malware employs several advanced techniques to fully compromise its victims. This FLINT report covers the various techniques identified during its reverse engineering. These techniques range from **defense evasion**, such as **parent process ID spoofing**, to privilege escalation by **abusing RPC** mechanisms, and include **dynamic API resolution**. This report also covers the functionalities of the RAT named **I2PRAT** that employ the **I2P network** to anonymise its final Command and Control (C2). The last part of this FLINT gives tracking and detection opportunities on the different stages of the newly identified threat.

## Sample overview

Before delving into the analysis of this undocumented threat, here is an overview of the infection chain. The malware is composed of **three layers**, the first one is perceived as a **binder / packer**, which executes in memory the second stage. This second stage, is the first topic covered in this FLINT, it is a **sophisticated loader** that employs various techniques to elevate its privilege and bypass defenses.

Finally, the remaining subject is the analysis of an utility used to expose the compromised devices on the **I2P anonymisation network** to provide the attacker with consequent **bot access**.

![ClickFix campaign delivering advanced loader that drops I2PRAT](data:image/svg+xml... "ClickFix campaign delivering advanced loader that drops I2PRAT")![ClickFix campaign delivering advanced loader that drops I2PRAT](https://lh7-qw.googleusercontent.com/docsz/AD_4nXdX3_Kd-KA-jp42XFAuQVTP_lbTvWbOHTebT6MrfCbedLSFmcsUxyR4jvIQBhSF16xlMRCE5VzAKNzzw6hOFRiYcTkoKjCfrc9smXWwKQNsev2eeDQuvIYhHCSB5pDzUeM2JYF3Gw?key=3aml_519Fq9rOf4AnidXQNW3 "ClickFix campaign delivering advanced loader that drops I2PRAT")

*Figure 1. ClickFix campaign delivering advanced loader that drops I2PRAT*

## I2PRAT Malware Loader

### Privileges review

The first task the malware (p.exe in the Figure 1) performs on the infected device is to verify its privileges. To do this, it retrieves the token information[3](#13cc2b37-927e-48bd-a5da-8a9ae0ee7c5c) for its process. It uses the NtOpenProcess function to acquire a handle to itself. It then obtains the associated access token using NtOpenProcessToken with the desired access set to TOKEN\_QUERY, which allows querying most information classes via the NtQueryInformationToken function.

The malware looks for the information class “TokenOrigin | TokenType”. The TokenOrigin contains the **Locally Unique IDentifier** (LUID) for the logon session, and the TokenInformation is a pointer to a **Security Identifier** (SID). The SID is then passed to the GetSidSubAuthority function (from Advapi32.dll), which returns a **relative identifie**r (RID). The RID is used to verify that the current process has the SECURITY\_MANDATORY\_SYSTEM\_RID, which is the RID of the NT Authority\SYSTEM account.

Subsequently, the malware also queries the current process token information by requesting the token information class “TokenAuditPolicy | TokenOwner”. However, to query the TokenAuditPolicy, the current account must have the SeSecurityPrivilege, as it serves as a verification method for the malware.

Depending on the results of these privilege verifications, the malware behaves differently. There are three possible scenarios:

* If the current process is not run by the SYSTEM account and does not have the SeSecurityPriv...