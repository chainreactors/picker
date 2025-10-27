---
title: Bulbature, beneath the waves of GobRAT
url: https://blog.sekoia.io/bulbature-beneath-the-waves-of-gobrat/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-03
fetch_date: 2025-10-06T18:54:43.648321
---

# Bulbature, beneath the waves of GobRAT

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

# Bulbature, beneath the waves of GobRAT

Since mid 2023, Sekoia Threat Detection & Research team (TDR) investigated an infrastructure which controls compromised edge devices transformed into Operational Relay Boxes used to launch offensive cyber attack.

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR, Amaury G. and Felix Aimé](#molongui-disabled-link)
October 2 2024

0

31 minutes reading

## Key Takeaways

* Since mid 2023, Sekoia Threat Detection & Research team (TDR) investigated an infrastructure which controls compromised edge devices transformed into Operational Relay Boxes used to launch offensive cyber attack.

* The infrastructure has constantly evolved with a total of 63 servers identified and analysed, and is still operating at the time of publication of this report.

* On some servers, it is possible to find installation scripts as well as the GobRAT and Bulbature malware. Other servers provide a view of the administration interface used to manage compromised hosts and launch attacks.

* Several traces lead us to suggest that this infrastructure might be used by several operators originating from China.

## Table of contents

* [Context](#h-context)
* [Initial findings](#h-initial-findings)
* [Down the rabbit hole: Infrastructure overall](#h-down-the-rabbit-hole-infrastructure-overall)
  + [Infection chain used to compromise edge devices](#h-infection-chain-used-to-compromise-edge-devices)
    - [ORBs](#h-orbs)
    - [Staging servers](#h-staging-servers)
    - [Bash scripts](#h-bash-scripts)
    - [Malware interactions](#h-malware-interactions)
  + [Proxies provider interface](#h-proxies-provider-interface)
    - [Browsing the “Security Tunnel” view](#h-browsing-the-security-tunnel-view)
    - [Browsing the “Nodes” view](#h-browsing-the-nodes-view)
  + [GobRAT administration interface](#h-gobrat-administration-interface)
    - [Browsing home page](#h-browsing-home-page)
    - [Browsing the “Task List” view](#h-browsing-the-task-list-view)
    - [Browsing the “Plugin” view](#h-browsing-the-plugin-view)
    - [Browsing other views](#h-browsing-other-views)
    - [Browsing views that are not displayed](#h-browsing-views-that-are-not-displayed)
    - [Other open directories](#h-other-open-directories)
* [Victimology identified form the open directories on the GobRAT administration interface](#h-victimology-identified-form-the-open-directories-on-the-gobrat-administration-interface)
* [Conclusion](#h-conclusion)
* [Indicators of compromise](#h-indicators-of-compromise)
* [Appendi x : Bash scripts](#h-appendi-x-bash-scripts)

## Context

On 9 October 2023, the Threat Detection & Research (TDR) team published a private report regarding an **attack campaign on edge devices** also documented by the [JPCERT/CC](https://blogs.jpcert.or.jp/en/2023/05/gobrat.html) on 29 May 2023. Since then, **the network infrastructure has remained active** and dozens of new hosts were deployed with the same characteristics as those initially identified. These hosts are monitored via the Sekoia C2 Tracker project and are capitalised within the Sekoia Intelligence Center (IC).

In our 2023 report, we assessed that this infrastructure was very likely used to support operations of multiple intrusion sets, likely of Chinese origin, due to certain traces attributing the attacks and the victimology observed, which mainly included **edge devices transformed into Operational Relay Boxes (ORB).** For some years now, we observe that China uses **edge devices as ORB to conduct offensive cyber campaigns**, as previously reported in link with the [Quad7 operator](https://blog.sekoia.io/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets/) or the [APT31 infrastructure](https://blog.sekoia.io/walking-on-apt31-infrastructure-footprints/). Although there was few open source information on GobRAT, TDR decided to investigate this threat in depth.

This investigation is still in progress as of October 2024, and we will focus on **highlighting the infrastructure** and **the different types of hosts** identified. The cut-off date for indicators included in this report is 5 September 2024.

## **Initial findings**

The initial findings came from a self-signed certificate that was used on a staging host identified by the JPCERT/CC:

|  |  |
| --- | --- |
| **Subject DN** | C=AU, ST=Some-State, O=Internet Widgits Pty Ltd |
| **Issuer DN** | C=AU, ST=Some-State, O=Internet Widgits Pty Ltd |
| **Serial Number** | Decimal: 587046745646849621397962336094648657285118811505 |
| **Validity Period** | 2021-05-16T06:47:34 to 2031-05-14T06:47:34 |
| **SHA-256** | 3ab014dd8cc7878c4e840be84b111e6fa71de221c42c14b0becaf3827a744ab9 |
| **SHA-1** | d0d3975b5b900b3af2dce973428475f022b16f60 |
| **MD5** | af4ad0bd9221ffc63ae5acff4034834a |

In 2023, when other staging hosts were analysed, one host was using a second, distinct certificate:

|  |  |
| --- | --- |
| **Subject DN** | O=mkcert development certificate, OU=a@a-virtual-machine |
| **Issuer DN** | O=mkcert development CA, OU=a@a-virtual-machine, CN=mkcert a@a-virtual-machine |
| **Serial Number** | Decimal: 77481536472298673143899330019234134150 |
| **Validity Period** | 2021-12-21T01:38:57 to 2024-03-21T01:38:57 |
| **SHA-256** | 27b6567f260dd689200bbda0794341b1edcf6039cfc1ae7adf0bc6477a16a1f9 |
| **SHA-1** | 74fe94844a337da4bdc2988609fb3c4df3f3b78d |
| **MD5** | e4b7b3a2610ad706a83667a5bac7cd31 |

Since we started monitoring the infrastructure, it was the first time – and only occasion – that a second certificate was observed, likely an error by the operator. It led us to uncover two new host types correlating the overall infrastructure.Since 2023, these two certificates were used to **identify 63 different hosts**, including **20 that were still active** at the time of writing.

In th...