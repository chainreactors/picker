---
title: MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key
url: https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html
source: The Hacker News
date: 2026-09-23
fetch_date: 2026-09-24T07:08:23.892468
---

# MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [MikroTrick Chain Let Attackers Take Over MikroTik Routers Without a Password or SSH Key](https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html)

**Swati Khandelwal**Sep 23, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjudzrtqX93WzCbZQoGI06WzKFtFpQsZaQB7GUao4yzBncGN3nxn0GzmYNybpL9SeKFttznMsVCZpQEQ_fD5kP_0nJRL4ZN6ZgHrXR2c33bpZN33gEyIkk6aBtx0k7znzalUe6epmrCO5VSCCH6beY_chvz9Pl0t5BbBtCLntTnNMwi3cFPXFd0p09FxA4/s1700-nu-rw-lo-l85-e365/microtik.jpg)

Two MikroTik RouterOS SSH vulnerabilities chained together let attackers take full administrative control of Internet-exposed routers without a password, SSH key, or completed authentication.

The chain, which CERT Polska calls **MikroTrick**, combines an SSH state-machine flaw (**CVE-2026-67279**) with an argument-injection bug in the RouterOS login process (**CVE-2026-86060**). Attack logs date to at least September 2, one day before MikroTik shipped patches in RouterOS 6.49.21, 7.23.4, and 7.24.2.

As [previously reported](https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html), CERT Polska warned on September 5 that attackers were using RouterOS flaws to take control of devices whose SSH service was reachable from public networks.

That warning confirmed the exploitation and urged immediate patching but did not identify which two flaws formed the chain or explain how they combined. This [latest analysis](https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/) provides both.

### How the Chain Works

SSH requires three steps in order: it establishes an encrypted connection, authenticates the user, and only then lets the client open a session and run commands. The server sends a specific message (SSH\_MSG\_USERAUTH\_SUCCESS) to confirm that authentication has passed.

CVE-2026-67279 breaks this sequence. If a client starts an SSH key renegotiation during the authentication step, vulnerable RouterOS moves straight to the command phase when the renegotiation finishes, without ever confirming the user's identity.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The flaw does not create an authenticated session or grant any privileges on its own, but it allows an unauthenticated client to reach a stage that should require a completed login.

CVE-2026-86060 turns that access into full administrative control. RouterOS launches a login program (/nova/bin/login) that receives the username and a privilege level from the SSH daemon as command-line arguments, without checking the username first. A value beginning with a hyphen is treated as a program option rather than a name.

The attacker sends -2 as the username. The login program treats this as an instruction to read its identity and privilege level from file descriptor 2, which points to the terminal the SSH session created.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiDOFlLHoidBhihDShUGo3izgYDWJ5VxOxAISWIO4yKQDLIpVzPlkfCJ8a_fZIIjJDv5SoGZYdmA2YUM-kahwadssnVGNVtBi199DOSeYb1BQu93RQMWHNKqafAr97KAFlDRNiIc4dV94O2yK6vo4MnzWfCfJ1Nx7JNnEM_J2R1aoSsnEicePws9YHJE0/s1700-nu-rw-lo-l85-e365/micro-chain.jpg)

Through the SSH channel, the attacker has already written a chosen username and the privilege value for full administrative access to that terminal. The login program accepts both and opens a fully privileged console.

### Evidence of Pre-Patch Exploitation

The chain leaves a distinctive trace in device logs: a failed login attempt for user -2. CERT Polska says logs matching this pattern appeared on the MikroTik forum as early as September 2, one day before the patches became available, and the team believes the chain was exploited before MikroTik released the fixes.

A [diagnostic report on the MikroTik forum](https://forum.mikrotik.com/t/important-security-update/272851/105) shows the attack sequence on one device: rejected authentication for -2, a forced renegotiation, a jump to the channel phase, and an exec request attempting to create a user called ops with full privileges. The SSH process crashed before the command completed on that device.

Other reports confirmed that the ops account was successfully created on affected devices. In some incidents, CERT Polska found diagnostic-file creation followed by data transfers to an attacker IP address, strongly suggesting that configuration data was copied to the attacker's infrastructure.

The MikroTrick chain is CVE-2026-67279 combined with CVE-2026-86060. Some publications have incorrectly included a third flaw, CVE-2026-67276, which CERT Polska says is a [separate SSH vulnerability](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve/) that lets an attacker forge an RSA key to log in as an existing user. That flaw requires knowledge of the account name and its public key, and gives access only to that account.

CISA [added](https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html) CVE-2026-86060 to its Known Exploited Vulnerabilities catalog on September 10, independently confirming active exploitation of the argument-injection flaw.

The chain requires SSH to be reachable from the attacker. [MikroTik says](https://mikrotik.com/supportsec/september-2026-vulnerability/) its default home configuration does not expose SSH to the Internet, but administrators who changed their firewall rules or manage devices over SSH from untrusted networks face higher risk.

No authoritative count of compromised devices has been published.

### What to Check

Patching prevents the attack but does not remove changes an attacker made before the update. After updating, administrators should check the Flagged status by running /system/device-mode/print.

The [Flagged mechanism](https://manual.mikrotik.com/docs/system-information-and-utilities/device-mode#flagged-status) detects only selected traces of compromise, and its absence does not...