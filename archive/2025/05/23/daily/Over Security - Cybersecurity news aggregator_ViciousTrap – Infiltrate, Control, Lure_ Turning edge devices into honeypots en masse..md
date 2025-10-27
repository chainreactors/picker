---
title: ViciousTrap – Infiltrate, Control, Lure: Turning edge devices into honeypots en masse.
url: https://blog.sekoia.io/vicioustrap-infiltrate-control-lure-turning-edge-devices-into-honeypots-en-masse/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-23
fetch_date: 2025-10-06T22:30:18.157048
---

# ViciousTrap – Infiltrate, Control, Lure: Turning edge devices into honeypots en masse.

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

# ViciousTrap – Infiltrate, Control, Lure: Turning edge devices into honeypots en masse.

This blog post analyzes the Vicious Trap, a honeypot network deployed on compromised edge devices.

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Felix Aimé, Jeremy Scion and Sekoia TDR](#molongui-disabled-link)
May 22 2025

0

10 minutes reading

*This article on was originally distributed as a private report to our customers.*

## Key Takeaways

* Sekoia.io investigated a threat actor nicknamed ViciousTrap, who compromised over 5,500 edge devices, turning them into honeypots.
* More than 50 brands — including SOHO routers, SSL VPNs, DVRs, and BMC controllers — are being monitored by this actor, possibly to collect exploited vulnerabilities affecting these systems.

* The actor is likely of Chinese-speaking origin, based on a weak overlap with the GobRAT infrastructure and the geographic distribution of compromised and key monitored devices.

## Introduction

In a previous [blogpost](https://blog.sekoia.io/polaredge-unveiling-an-uncovered-iot-botnet/), Sekoia’s Threat Detection & Research (TDR) team documented the exploitation of the **CVE-2023-20118** vulnerability, which was used to deploy two distinct threats: a webshell and the PolarEdge malware.

Through the observation of activity on our honeypots, it was possible to identify a third actor, nicknamed **ViciousTrap** by Sekoia.io, using the same vulnerability. The infection chain involves the execution of a shell script, dubbed **NetGhost**, which redirects incoming traffic from specific ports of the compromised router to a **honeypot-like infrastructure** under the attacker’s control allowing him to intercept network flows.

An examination of both the attacker’s behaviour via our honeypots and its broader infrastructure, thanks to internet scanning services, suggested that the same actor was also targeting a variety of other devices, including those manufactured by **D-Link**, **Linksys**, **ASUS**, **QNAP** and **Araknis Networks**, to compose its infrastructure.

Analysis of the victims pointed to more than **5,000 compromised devices**, particularly across Asia. An hypothesis is that the attacker likely attempts to **construct a distributed honeypot-like network by compromising a broad range of internet-facing equipment**. This setup would allow the actor **to observe exploitation attempts** across multiple environments and potentially **collect non-public or zero-day exploits**, and reuse access obtained by other threat actors.

In support of this hypothesis, interactions observed on TDR’s honeypots revealed attempts by the attacker to reuse a previously documented web shell to deploy their redirection script. This blogpost provides an analysis of this infection chain and shares insights into the ViciousTrap infrastructure of **April 18, 2025**.

## Infection chain

### Initial access

Initial access is obtained by the attacker through exploitation of the **CVE-2023-20118** vulnerability, which affects several Cisco SOHO routers. The first exploitation attempt attributed to this actor was observed in March 2025. Since then, activity has remained sustained, with frequent attacks occurring almost daily—and occasionally multiple times per day. All exploitation attempts originate from the single IP address **101.99.91[.]151**.

**Step 1:** The attacker exploits the CVE-2023-20118 vulnerability to download via **ftpget** and execute a bash script named **a**, as shown below.

![vicioustrap exploitation request](data:image/svg+xml...)![vicioustrap exploitation request](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/05/Frame-49.png)

**Step 2:** a bash script executes an **ftpget** command to download a file named **wget**, which is a busybox **wget** binary compiled for MIPS architecture (N32 MIPS64). The binary is saved in the `/tmp` directory of the compromised system. It was most likely manually placed on the compromised system by the attacker, as it is not available by default on this particular system. The attacker deployed this binary as it is required during the post-exploitation phase, specifically to notify the command and control (C2) server.

![vicioustrap wget download script](data:image/svg+xml...)![vicioustrap wget download script](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/05/Frame-51.png)

**Step 3:** The CVE-2023-20118 vulnerability is exploited a second time. This time, the previously dropped **wget** binary is used to retrieve and execute a second script, which includes a unique UUID in its filename for each attempt. This UUID acts as an identifier, and the Command and Control (C2) infrastructure appears to filter download requests, delivering payloads only to confirmed compromised systems by using an allow-list.

![vicioustrap request to execute redirection script](data:image/svg+xml...)![vicioustrap request to execute redirection script](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/05/Frame-50.png)

### Post Exploitation

Once the secondary script – `main.sh` (presented in the scheme on the next page) – is executed, it performs several key actions, such as:

* **Self-removal:** One of the script’s initial instructions is a rm command that deletes the script itself, likely to minimise forensic artefacts and reduce detection.
* **Targeted redirection of inbound network traffic via iptables:** The script checks whether any of the following ports —**80, 8000, or 8080**— are available (i.e., not already in use or filtered). The first available port is stored in a variable named `Dport`. It then clears any existing NAT redirection rules pointing to the attacker’s infrastructure before establishing a new redirection....