---
title: Relay Your Heart Away: An OPSEC-Conscious Approach to 445 Takeover
url: https://posts.specterops.io/relay-your-heart-away-an-opsec-conscious-approach-to-445-takeover-1c9b4666c8ac?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-08-02
fetch_date: 2025-10-06T18:05:26.218966
---

# Relay Your Heart Away: An OPSEC-Conscious Approach to 445 Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1c9b4666c8ac&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Frelay-your-heart-away-an-opsec-conscious-approach-to-445-takeover-1c9b4666c8ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Frelay-your-heart-away-an-opsec-conscious-approach-to-445-takeover-1c9b4666c8ac&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-1c9b4666c8ac---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-1c9b4666c8ac---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Relay Your Heart Away: An OPSEC-Conscious Approach to 445 Takeover

[![Nick Powers](https://miro.medium.com/v2/resize:fill:64:64/1*4iCSUS4ok3rEC6CJGYKywA.png)](https://medium.com/%40zyn3rgy?source=post_page---byline--1c9b4666c8ac---------------------------------------)

[Nick Powers](https://medium.com/%40zyn3rgy?source=post_page---byline--1c9b4666c8ac---------------------------------------)

11 min read

·

Aug 1, 2024

--

Listen

Share

Even within organizations that have achieved a mature security posture, targeted NTLM relay attacks are still incredibly effective after all these years of abuse. Leveraging several of these NTLM relay primitives, specifically ones that require coercing SMB-based authentication, come with additional challenges to overcome while operating over command and control (C2). This technique will the ease abuse of several popular NTLM relay primitives by allowing attackers to control inbound 445/tcp traffic without loading a driver, loading a module into LSASS, or requiring a reboot of the target Windows machine.

## Introduction

When conducting a penetration test or red team from a device that can directly route into a target network, there is often a straightforward path to control inbound SMB-based traffic on port 445/tcp. Common scenarios include a Windows laptop plugged directly into ethernet, a deployed Linux virtual machine, VPN accessibility, etc.

In the case of Windows, the `LanmanServer` service can be disabled, followed by a reboot, and the Windows kernel is no longer bound to the target port. In the case of a Linux machine, having escalated privileges on your testing device will allow for binding to the target port.

However, conducting your offensive assessment through a C2 agent includes a few additional hurdles to overcome. A commonly problematic step is gaining is gaining control of inbound SMB-based authentication attempts on port 445/tcp from a compromised Windows host.

If you’re interested in skipping the technical analysis and getting straight to the solution, see the **Implementation Summary** section.

## Existing Solutions

### WinDivert driver

The [WinDivert](https://github.com/basil00/Divert) driver is described as a “a user-mode packet interception library that enables user-mode capturing/modifying/dropping of network packets sent to/from the Windows network stack”. Many popular open-source projects have been created to leverage this driver to redirect inbound SMB-based authentication, such as [PortBender](https://github.com/praetorian-inc/PortBender), [SharpRelay](https://github.com/pkb1s/SharpRelay), [StreamDivert](https://github.com/jellever/StreamDivert), [DivertTCPconn](https://github.com/Arno0x/DivertTCPconn), [hwfwbypass](https://github.com/MRGEffitas/hwfwbypass), and more.

### Lsarelayx

The [lsarelayx](https://github.com/CCob/lsarelayx) by [@\_EthicalChaos\_](https://x.com/_EthicalChaos_) is a “system wide NTLM relay tool designed to relay incoming NTLM based authentication to the host it is running on” by leveraging “a fake LSA authentication provider to hook the NTLM and Negotiate packages and facilitate redirecting authentication requests”.

### Disabling LanmanServer w/ Reboot

The LanmanServer service can simply be set to a ‘disabled’ start type. When the Windows machine is rebooted, 445/tcp will no longer be bound by the kernel.

## OPSEC Considerations

Leveraging a driver for post-exploitation involves several considerations, such as potential for BSOD. This is a risk we cannot afford to take in certain situations. Especially when conducting activities on high-uptime, critical infrastructure. Loading a driver, especially one publicly associated with popular abuse primitives, can also be a single point of failure regarding detection and prevention.

Loading a customer LSA authentication provider can come with similar risks, as it can affect the stability of the LSASS process. You could be one incorrectly handled error away from a forced reboot depending on your code. As a Microsoft-specific limitation of how LSA plugins work, the provider also cannot be unloaded until a reboot occurs ([without getting creative](https://github.com/CCob/lsarelayx?tab=readme-ov-file#caveats)).

Disabling the LanmanServer service also requires either forcing, or waiting for, a reboot of the target machine. This often isn’t an option due to time constraints or high-uptime needs of a production environment.

Ideally, we would be able to control traffic inbound on the target port without loading a driver, loading a module into LSASS, or rebooting the target machine.

## Technical Analysis

### Prerequisite Notes

As previously mentioned, configuring the `*LanmanServer*` service to a start type of `*disabled*` and rebooting Windows will result in the machine no longer being bound to 445/tcp by default. Another important note — when reconfiguring the `LanmanServer` service back to the default start type of `auto start` and manually starting the service, the Windows machine will again bind to 445/tcp and reloading all the necessary resources to resume normal SMB-based functionality. Remember, the goal here is to do *something* to *release* this port without requiring a reboot, loading a driver, or loading a module into LSASS. Being able to repeat and debug the same thing in reverse (i.e., binding to the port) will be helpful for understanding the potential associated code path(s) for our desired result.

### Initial Items of Interest

To start, let’s verify *what* is binding to the port we are interested in. Here’s one way to do this quickly, using PowerShell:

```
PS C:\> Get-NetTCPConnection -LocalPort 445 | ForEach-Object { Get-Process -Id $_.OwningProcess }
Handles NPM(K) PM(K) WS(K) CPU(s) Id SI ProcessName
 - - - - - - - - - - - - - - - - - - - - - - - -
 6600 0 224 7424 9,175.72 4 0 System
```

So we know the process with a handle to the socket bound on 445/tcp is `*System*`, and we can begin looking at loaded modules/drivers associated with opening and closing sockets. Using [System Informer](https://github.com/winsiderss/syste...