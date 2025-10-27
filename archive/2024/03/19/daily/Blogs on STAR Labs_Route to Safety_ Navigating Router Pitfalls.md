---
title: Route to Safety: Navigating Router Pitfalls
url: https://starlabs.sg/blog/2024/route-to-safety-navigating-router-pitfalls/
source: Blogs on STAR Labs
date: 2024-03-19
fetch_date: 2025-10-04T12:09:06.958443
---

# Route to Safety: Navigating Router Pitfalls

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Route to Safety: Navigating Router Pitfalls

March 18, 2024 · 48 min · Daniel Lim Wee Soong (@daniellimws)

Table of Contents

* [Introduction](#introduction)
* [Attack Surface](#attack-surface)
  + [Admin Panel](#admin-panel)
  + [Other Services](#other-services)
* [Poor Configurations](#poor-configurations)
  + [Hardcoded Credentials](#hardcoded-credentials)
    - [Impact](#impact)
    - [Examples](#examples)
    - [Suggestions](#suggestions)
  + [Services Exposed to the Internet](#services-exposed-to-the-internet)
    - [Suggestions](#suggestions-1)
  + [Services Running as `root`](#services-running-as-root)
    - [Suggestions](#suggestions-2)
  + [Password-less `sudo`?](#password-less-sudo)
    - [Bad Example](#bad-example)
    - [Suggestions](#suggestions-3)
  + [Summary](#summary)
* [Vulnerability Classes](#vulnerability-classes)
  + [Authentication Bypass](#authentication-bypass)
    - [Examples](#examples-1)
      * [CVE-2021-32030: Mistake in authentication logic](#cve-2021-32030-mistake-in-authentication-logic)
        + [Suggestions](#suggestions-4)
      * [CVE-2020-8864: Mistake in authentication logic](#cve-2020-8864-mistake-in-authentication-logic)
        + [Suggestions](#suggestions-5)
      * [CVE-2020-8863: Expected password value is controlled by attacker](#cve-2020-8863-expected-password-value-is-controlled-by-attacker)
    - [Summary](#summary-1)
  + [Command Injection](#command-injection)
    - [Root Cause](#root-cause)
    - [Rationale for using shell commands](#rationale-for-using-shell-commands)
    - [Prevention](#prevention)
      * [Avoid `system` commands](#avoid-system-commands)
      * [Run executable with argument list](#run-executable-with-argument-list)
      * [Custom `execve`](#custom-execve)
      * [Avoid `eval` in shell scripts](#avoid-eval-in-shell-scripts)
    - [Actionable Steps](#actionable-steps)
    - [Examples](#examples-2)
      * [D-Link (C)](#d-link-c)
        + [Failed validation of IP range string](#failed-validation-of-ip-range-string)
      * [Zyxel (Python)](#zyxel-python)
        + [Fix](#fix)
      * [TP-Link (LuCI)](#tp-link-luci)
        + [Suggestions](#suggestions-6)
        + [Remarks](#remarks)
      * [DHCP server (C)](#dhcp-server-c)
        + [Patch](#patch)
  + [Buffer Overflow](#buffer-overflow)
    - [Root Cause](#root-cause-1)
    - [Prevention](#prevention-1)
      * [Use bounded functions for copying](#use-bounded-functions-for-copying)
      * [Pass buffer size as function argument](#pass-buffer-size-as-function-argument)
      * [Caveat: `strncpy`](#caveat-strncpy)
      * [Custom `strncpy`](#custom-strncpy)
      * [Caveat: `strncat`](#caveat-strncat)
      * [Custom `strncat`](#custom-strncat)
    - [Actionable Steps](#actionable-steps-1)
    - [Examples](#examples-3)
  + [Format String Bug](#format-string-bug)
    - [Prevention](#prevention-2)
    - [Actionable Steps](#actionable-steps-2)
    - [Example](#example)
* [Conclusion](#conclusion)

## Introduction[#](#introduction)

Wi-Fi routers have always been an attractive target for attackers. When taken over, an attacker may gain access to a victim’s internal network or sensitive data. Additionally, there has been an ongoing trend of attackers continually [incorporating new router exploits into their arsenal for use in botnets, such as the Mirai Botnet](https://www.zerodayinitiative.com/blog/2023/4/21/tp-link-wan-side-vulnerability-cve-2023-1389-added-to-the-mirai-botnet-arsenal).

Consumer grade devices are especially attractive to attackers, due to many security flaws in them. Devices with lower security often contain multiple bugs that attackers can exploit easily, rendering them vulnerable targets. On the other hand, there are more secure devices that offer valuable insights and lessons to learn from.

This article gives a technical overview of vulnerabilities in routers for the awareness of security teams and developers, and provides suggestions in ways to avoid making mistakes that could result in such vulnerabilities. We will also look at past vulnerabilities affecting devices of various vendors to learn from their mistakes. Although the following content focuses on routers, the lessons learnt can be applied to other network devices as well.

*Disclaimer: This article does not cover all bug classes.*

## Attack Surface[#](#attack-surface)

A router’s attack surface may be larger than one might expect. This is because there are various services running on it. Every service that receives requests from an external host, either on the local-area network (LAN) or wide-area network (WAN) interface, presents an attack surface as malformed requests may execute a vulnerable code path in the service. Below, we briefly explore the common services on routers that process external requests.

### Admin Panel[#](#admin-panel)

The admin panel of a network device hosts a large variety of configurations that could be changed by the device owner/administrator. Every input field is an attack surface as they are processed by the web service running on the device. For example, there may be an input field for blocking traffic to/from a certain IP address. The web service may handle this request in a way that is vulnerable to command injection. In short, the admin panel presents a huge attack surface to an attacker.

One may argue that this is not a very concerning attack surface, because an attacker would need to authenticate into the admin panel first in order to access this attack surface. This is true, and therefore many CVEs start with the term “authenticated”, e.g. “authenticated command injection”, which states that authentication is needed to exploit the vulnerability. However, an attacker may find an authentication bypass or there may be some endpoints on the admin panel that do not verify if the user is authenticated. An authentication bypass can be chained with an “authenticated vulnerability”; vulnerabilities on endpoints that do not require authentication are categorized with the term “unauthenticated”, e.g. “unauthenticated buffer overflow”.

### Other Services[#](#other-services)

Besides the admin panel, a router usually also runs other services that process requests for various protocols such as FTP, Telnet, Dynamic Host Configuration Protocol (DHCP) or Universal Plug and Play (UPnP). These services also present an attack surface on the router.

Some services such as DHCP or UPnP do not require authentication. Furthermore, on some devices, some services are accessible from the WAN interface, which means that a remote attacker that is not on the local network can also access these services and exploit any vulnerability on them. For services that are so accessible, it is especially important to ensure that they are secure.

## Poor Configurations[#](#poor-configurations)

First, we discuss some configuration mistakes present on some routers. The ones that we will discuss all follow the theme of access, namely

* Access via hardcoded credentials
* Access to services from a remote network
* Access to root privileges by a running service or normal user

### Hardcoded Credentials[#](#hardcoded-credentials)

The firmware of a device contains an archive of programs and configuration files that are used by the device for its operations. The same firmware is distributed to and installed on all devices of the same model. Hence, if the credentials for any service (e.g. FTP or Telnet) running on the device is h...