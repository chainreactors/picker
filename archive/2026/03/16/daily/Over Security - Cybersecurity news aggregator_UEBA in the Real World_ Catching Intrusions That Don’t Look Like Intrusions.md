---
title: UEBA in the Real World: Catching Intrusions That Don’t Look Like Intrusions
url: https://blog.sekoia.io/ueba-in-the-real-world-catching-intrusions-that-dont-look-like-intrusions/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-16
fetch_date: 2026-03-17T04:16:58.554853
---

# UEBA in the Real World: Catching Intrusions That Don’t Look Like Intrusions

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

[SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/ "SOC Insights & Other News")

# UEBA in the Real World: Catching Intrusions That Don’t Look Like Intrusions

[![](data:image/svg+xml...)![](https://secure.gravatar.com/avatar/28c7f8195a566b04453ac6788eb103d6eb119e36e8d17886f6057379433ab6b0?s=52&d=mm&r=g)](#molongui-disabled-link)

[David Greenwood](#molongui-disabled-link)
March 13 2026

0

8 minutes reading

Most SOC detections are built for the attacker who trips a wire: a suspicious hash, a known IP, a noisy exploit chain, a payload that spawns the “wrong” process. But a lot of modern intrusions don’t look like that. They look like normal users doing normal things, because attackers increasingly authenticate instead of breaking in, and then operate through legitimate tools (IdPs, SaaS APIs, cloud consoles, remote admin utilities). That’s exactly why “simple indicator and pattern matching detection rules” routinely miss early-stage compromise, and why UEBA (entity/user behavior analytics, often lumped under UEBA) matters: it shifts detection from “is this artifact known-bad?” to “is this behavior wrong for this identity, this device, this workload, and this point in time?”

This isn’t a marketing argument; it’s what the frontline data says. [Verizon’s DBIR](https://www.verizon.com/business/resources/reports/2024-dbir-data-breach-investigations-report.pdf?utm_source=chatgpt.com) continues to show credential abuse as a dominant initial access path, and highlights how often breaches begin with stolen credentials rather than exotic malware. MITRE ATT&CK also frames “Valid Accounts” (T1078) as a core technique because it lets adversaries blend in and evade many controls. If your detection posture is heavily “IOC-first,” you’re playing on the attacker’s home turf; if you can model and score behavior across identities and entities, you start to see the seams.

Below are five practitioner-grade cases where UEBA catches what rules often don’t, grounded in real research and real intrusion patterns, with the kinds of signals you can actually operationalize.

---

## Case 1: “Valid accounts” lateral movement that never triggers malware rules

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/03/ChatGPT-Image-Mar-16-2026-11_03_54-AM-1024x683.png)

A common SOC failure mode is treating authentication as a binary: either the login succeeded (so it’s fine) or it failed (so it’s suspicious). But attackers love valid credentials precisely because they turn the front door into a stealth channel. MITRE’s “Valid Accounts” technique notes detection ideas that are fundamentally behavioral: unusual login times, unusual hosts, impossible travel, new services touched, simultaneous sessions, and privilege use that’s atypical for that account. This is the classic space where indicator-based detections struggle because there’s nothing inherently “bad” about Kerberos tickets, RDP, SMB, WinRM, PsExec, or cloud console logins, those are normal tools.

What UEBA buys you operationally is a way to score the sequence and context rather than any one event. A pattern that looks like “user A authenticates to a new host → touches 12 endpoints in 20 minutes → accesses an admin share they never access → spawns remote execution from an unusual workstation” is high-signal, even if every individual event is “legitimate.” In practice, you’re correlating identity telemetry (IdP, AD), endpoint telemetry (logon types, new service creation), and network context (new internal destinations, authentication fan-out). The point isn’t to replace rules; it’s to catch the attacker who is deliberately behaving like rules expect.

---

## Case 2: Stolen credentials + MFA fatigue: the human becomes the bypass

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/03/ChatGPT-Image-Mar-16-2026-11_06_49-AM-1024x683.png)

As MFA adoption rises, attackers increasingly pivot to social engineering that targets the approval workflow rather than the password. Microsoft has explicitly described “MFA fatigue” (push spamming) as a growing issue and provides guidance for mitigating it; the technique relies on bombarding users with push prompts until they accept one. This attack class is a perfect example of why static detections fail: a single successful MFA approval isn’t suspicious by itself, and the IP might even be “close enough” (VPN exit nodes, cloud proxies, residential ISPs).

UEBA’s advantage is seeing the behavioral build-up to the approval. For example: multiple MFA prompts in a short window, repeated sign-in attempts from new device fingerprints, a first-time IP/geolocation for that identity, then a sudden shift into high-value actions (accessing finance mailboxes, creating inbox rules, downloading a large SharePoint subtree, adding devices, or resetting sessions). Even when you do build rules like “>N MFA prompts,” attackers can tune around thresholds; UEBA lets you incorporate personal baselines (how often does this user ever trigger MFA prompts?), peer baselines (how often do users in this department do the subsequent actions?), and entity baselines (is this device normally associated with this identity?).

If you want a concrete hook for the article: Microsoft’s own write-up on MFA fatigue is clear that this is about user context and approvals, not malware.

---

## Case 3: OAuth abuse and “legitimate” API access that never hits EDR

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/03/ChatGPT-Image-Mar-16-2026-11_09_04-AM-1024x683.png)

OAuth app abuse is one of the cleanest demonstrations of why indicator-driven detection is insufficient. Microsoft has documented threat actors misusing OAuth applications to automate financially driven attacks, where compromised user accounts are used to create/modify OAuth apps and grant high privileges so ...