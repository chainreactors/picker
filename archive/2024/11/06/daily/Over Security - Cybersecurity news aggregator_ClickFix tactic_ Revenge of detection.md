---
title: ClickFix tactic: Revenge of detection
url: https://blog.sekoia.io/clickfix-tactic-revenge-of-detection/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-06
fetch_date: 2025-10-06T19:21:39.786528
---

# ClickFix tactic: Revenge of detection

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

# ClickFix tactic: Revenge of detection

This blog post provides an overview of the observed Clickfix clusters and suggests detection rules based on an analysis of the various infection methods employed.

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/TDR-badge2.png)](#molongui-disabled-link)

[Jeremy Scion and Sekoia TDR](#molongui-disabled-link)
November 5 2024

0

13 minutes reading

*This report on ClickFix was originally published for our customers on *22 October* 2024.*

## Table of contents

* [Context](#h-context)
* [ClickFix principle](#h-clickfix-principle)
* [Phantom Meet case](#h-phantom-meet-case)
  + [Behavioural detection – Endpoint](#h-behavioural-detection-endpoint)
  + [Network](#h-network)
* [CAPTCHAs case](#h-captchas-case)
  + [Behavioural detection – Endpoint](#h-clickfix-behavioural-detection-endpoint)
  + [Behavioural detection – Multisource](#h-clickfix-behavioural-detection-multisource)
  + [Hunting web access](#h-hunting-web-access)
* [Conclusion](#h-conclusion)

## Context

In May 2024, a new social engineering tactic called ClickFix emerged, featuring a ClearFake cluster that the Sekoia Threat Detection & Research (TDR) team closely monitored and analysed in a private report. This tactic involves displaying fake error messages in web browsers to deceive users into copying and executing a given malicious PowerShell code, finally infecting their systems.

The previous [blog post ClickFix tactic: The Phantom Meet](https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/) outlines the ClickFix cluster, which leverages fake video conferencing pages (such as Google Meet or Zoom) to distribute infostealers. A private report released shortly after, describes a larger cluster that uses fake CAPTCHAs pages for the same purpose.

In this blog post, we delve into the various infection chains and highlight detection opportunities based on the available data sources in addition to threat intelligence.

## ClickFix principle

Regardless of the template used (Google Meet, Captcha, etc.), the infection process is consistent.  The user is guided through a series of steps that ultimately compromise their machine. The sequence of events is as follows:

1. The user is instructed  from the web page to press “Windows + R”, a keyboard shortcut to open the Run command dialog box;
2. Press “Ctrl + V” to paste a malicious command previously copied from the clipboard via JavaScript function;
3. Press “Enter” to execute the command, mainly PowerShell or Mshta, which is designed to download and run a payload.

From the workstation’s perspective, using the “Windows + R” shortcut ensures that the process executing the malicious command runs under Explorer.exe as its parent process. This makes the activity appear more legitimate, and from the attacker’s perspective, reducing the risk of detection.

The infection chains may vary, but three main scenarios emerge: one targeting macOS and two affecting Windows.

* For macOS, clicking the “fix it” button triggers the direct download and execution of malware – in this case, Amos Stealer -) in the form of a .dmg file.
* On the Windows side, the infection chains differ depending on the ClickFix cluster being used, whether it’s through fake meeting pages (e.g., Phantom Meet) or deceptive CAPTCHAs. Each cluster utilizes a distinct approach to deliver its payload. In the first scenario, the infection chain starts with the execution of a malicious **mshta** command. In the second scenario, **PowerShell** is used to initiate the infection process.

![ClickFix infection routine](data:image/svg+xml...)![ClickFix infection routine](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/10/infection-1024x745.png)

*Figure 1. ClickFix infection routine*

## Phantom Meet case

We discovered several websites masquerading as the homepage of a Google Meet video conference. The sites displayed pop-up windows falsely indicating problems with the microphone and headset, as shown on the figure below.

![ClickFix cluster masquerading Google Meet video conference displaying a pop-up faking technical issues](data:image/svg+xml...)![ClickFix cluster masquerading Google Meet video conference displaying a pop-up faking technical issues](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/10/clickfix-gmeet-1024x761.png)

*Figure 2. ClickFix cluster masquerading Google Meet video conference displaying a pop-up faking technical issues*

In this instance, as outlined in [our previous blog post](https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/), the command copied from ClickFix executes a VBScript. This is achieved  through an HTML Application embedded in an HTML page, which is downloaded by mshta.exe. The VBScript performs the following actions:

1. Terminates its parent process (mshta.exe).
2. Downloads executables using bitsadmin.exe.
3. Retrieves the victim’s public IP address using the api.ipify[.]org service and sends this, along with the execution status, to the C2 server.

The resulting process tree is particularly noticeable and serves as a strong indicator of compromise.

### Behavioural detection – Endpoint

* ProcessTree detection

A quick win is to detect PowerShell or bitsadmin processes where the parent process is mshta.exe and the command line contains a URL.

```
detection:
  selection:
    process.parent.name: 'mshta.exe'
    process.parent.command_line|contains:
      - 'http://'
      - 'https://'
    process.name:
      - 'bistadmin.exe'
      - 'timeout.exe'
      - 'cmd.exe'
  condition: selection
```

In the rule above, the selection criteria are deliberately strict to correspond to the ClickFix phantom case scenario. However, it would be beneficial to detect a wider list of child processes, including powershell.exe or rundll32.exe.

* Bitsadmin

**bitsadmin.exe** is a command-line tool used to m...