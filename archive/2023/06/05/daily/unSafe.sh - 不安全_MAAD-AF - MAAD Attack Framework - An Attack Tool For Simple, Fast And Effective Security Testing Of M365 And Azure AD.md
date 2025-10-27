---
title: MAAD-AF - MAAD Attack Framework - An Attack Tool For Simple, Fast And Effective Security Testing Of M365 And Azure AD
url: https://buaq.net/go-167167.html
source: unSafe.sh - 不安全
date: 2023-06-05
fetch_date: 2025-10-04T11:44:25.272398
---

# MAAD-AF - MAAD Attack Framework - An Attack Tool For Simple, Fast And Effective Security Testing Of M365 And Azure AD

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/b49d80cdbb6b6a1cd076411002af2044.jpg)

MAAD-AF - MAAD Attack Framework - An Attack Tool For Simple, Fast And Effective Security Testing Of M365 And Azure AD

MAAD-AF is an open-source cloud attack tool developed for testing security of Microsoft 365
*2023-6-4 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-167167.htm)
阅读量:41
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjlqnY5d-DxuIyC25eShKi9KB3c0GXTWqcr54l1F5VQBiedZ5xVdYZIyjq9pHnjwlQAo7zDQcrVTZBbFGh6wZPznn_EsSmty9_0oNMJtnHWoHRt5UwCO51rZVsVIiGkI2UgsKgNndkrAbWb3RoPGmsZtFcD_NwKXJKJ2IXCASurtw0T9tZbQdYu1fTzCw=w640-h136)](https://blogger.googleusercontent.com/img/a/AVvXsEjlqnY5d-DxuIyC25eShKi9KB3c0GXTWqcr54l1F5VQBiedZ5xVdYZIyjq9pHnjwlQAo7zDQcrVTZBbFGh6wZPznn_EsSmty9_0oNMJtnHWoHRt5UwCO51rZVsVIiGkI2UgsKgNndkrAbWb3RoPGmsZtFcD_NwKXJKJ2IXCASurtw0T9tZbQdYu1fTzCw)

MAAD-AF is an open-source cloud attack tool developed for testing security of [Microsoft](https://www.kitploit.com/search/label/Microsoft "Microsoft") 365 & Azure AD environments through adversary emulation. MAAD-AF provides security practitioners [easy to use](https://www.kitploit.com/search/label/Easy%20To%20Use "easy to use") attack modules to exploit configurations across different M365/AzureAD cloud-based tools & services.

MAAD-AF is designed to make cloud security testing simple, fast and effective. Through its virtually no-setup requirement and easy to use interactive attack modules, security teams can test their security controls, detection and response capabilities easily and swiftly.

## Features

* Pre & Post-compromise techniques
* Simple interactive use
* Virtually no-setup requirements
* Attack modules for Azure AD
* Attack modules for Exchange
* Attack modules for Teams
* Attack modules for SharePoint
* Attack modules for eDiscovery

### MAAD-AF Attack Modules

* Azure AD External Recon (Includes sub-modules)
* Azure AD Internal Recon (Includes sub-modules)
* Backdoor Account Setup
* Trusted Network Modification
* Disable Mailbox Auditing
* Disable Anti-Phishing
* Mailbox Deletion Rule Setup
* Exfiltration through Mailbox Forwarding
* Gain User Mailbox Access
* External Teams Access Setup (Includes sub-modules)
* eDiscovery [exploitation](https://www.kitploit.com/search/label/Exploitation "exploitation") (Includes sub-modules)
* Bruteforce
* MFA Manipulation
* User Account Deletion
* SharePoint exploitation (Includes sub-modules)

## Getting Started

### Plug & Play - It's that easy!

1. Clone or download the MAAD-AF github repo to your windows host
2. Open [PowerShell](https://www.kitploit.com/search/label/PowerShell "PowerShell") as Administrator
3. Navigate to the local MAAD-AF directory `(cd /MAAD-AF)`
4. Run MAAD\_Attack.ps1 `(./MAAD_Attack.ps1)`

### Requirements

1. Internet accessible Windows host
2. PowerShell (version 5 or later) terminal as Administrator
3. The following PowerShell modules are required and will be installed automatically:

* [Az](https://www.powershellgallery.com/packages/Az/ "Az")
* [AzureAd](https://www.powershellgallery.com/packages/AzureAD/ "AzureAd")
* [MSOnline](https://www.powershellgallery.com/packages/MSOnline/ "MSOnline")
* [ExchangeOnlineManagement](https://www.powershellgallery.com/packages/ExchangeOnlineManagement/ "ExchangeOnlineManagement")
* [MicrosoftTeams](https://www.powershellgallery.com/packages/MicrosoftTeams/ "MicrosoftTeams")
* [AzureADPreview](https://www.powershellgallery.com/packages/AzureADPreview/ "AzureADPreview")
* [ADInternals](https://aadinternals.com/aadinternals/ "ADInternals")
* [ExchangePowershell](https://www.powershellgallery.com/packages/ExchangeOnlineManagement/3.0.0 "ExchangePowershell")
* [Microsoft.Online.SharePoint.PowerShell](https://www.powershellgallery.com/packages/Microsoft.Online.SharePoint.PowerShell/16.0.23311.12000 "Microsoft.Online.SharePoint.PowerShell")
* [PnP.PowerShell](https://github.com/pnp/powershell "PnP.PowerShell")

Tip: A 'Global Admin' [privilege](https://www.kitploit.com/search/label/Privilege "privilege") account is recommended to leverage full capabilities of modules in MAAD-AF

### Limitations

* MAAD-AF is currently only fully supported on Windows OS

## Contribute

* Thank you for considering contributing to MAAD-AF!
* Your contributions will help make MAAD-AF better.
* Join the mission to make security testing simple, fast and effective.
* There's ongoing efforts to make the source code more modular to enable easier contributions.
* Continue monitoring this space for updates on how you can easily incorporate new attack modules into MAAD-AF.

### Add Custom Modules

* Everyone is encouraged to come up with new attack modules that can be added to the MAAD-AF Library.
* Attack modules are functions that leverage access & privileges established by MAAD-AF to exploit configuration flaws in Microsoft services.

### Report Bugs

* Submit bugs or other issues related to the tool directly in the "Issues" section

### Request Features

* Share those great ideas. Submit new features to add to the MAAD-AFs functionality.

## Contact

* If you found this tool useful, want to share an interesting use-case, bring issues to attention, whatever the reason - I would love to hear from you. You can contact at: [[email protected]](http://www.kitploit.com/cdn-cgi/l/email-protection#c6aba7a7a2eba7a086b0a3a5b2b4a7e8a7af "maad-af@vectra.ai") or post in repository Discussions.

MAAD-AF - MAAD Attack Framework - An Attack Tool For Simple, Fast And Effective Security Testing Of M365 And Azure AD
![MAAD-AF - MAAD Attack Framework - An Attack Tool For Simple, Fast And Effective Security Testing Of M365 And Azure AD](https://blogger.googleusercontent.com/img/a/AVvXsEjlqnY5d-DxuIyC25eShKi9KB3c0GXTWqcr54l1F5VQBiedZ5xVdYZIyjq9pHnjwlQAo7zDQcrVTZBbFGh6wZPznn_EsSmty9_0oNMJtnHWoHRt5UwCO51rZVsVIiGkI2UgsKgNndkrAbWb3RoPGmsZtFcD_NwKXJKJ2IXCASurtw0T9tZbQdYu1fTzCw=s72-w640-c-h136)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/maad-af-maad-attack-framework-attack.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)