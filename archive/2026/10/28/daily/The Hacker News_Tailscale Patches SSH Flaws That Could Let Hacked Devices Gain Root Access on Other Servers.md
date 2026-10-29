---
title: Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers
url: https://thehackernews.com/2026/10/tailscale-patches-ssh-flaws-that-could.html
source: The Hacker News
date: 2026-10-28
fetch_date: 2026-10-29T07:52:56.400007
---

# Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers](https://thehackernews.com/2026/10/tailscale-patches-ssh-flaws-that-could.html)

**Swati Khandelwal**Oct 28, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4t7YUY-idhgGJFpEuulM5zELQR4QNB-UKmsh7cyB5cdMH4AU_zumf3K27WBWgAw6ra28TvALm5fFeLrV_1wHJXeYy3azE1TcblP-1JSCPLF3mq-WKjUOXy3K-pfjhHtiwGkCoYhxfEMZGielHz2Bit6mLoNlnElmauP0RNcbXelNkAHIWI4s92qrymUQ/s1700-nu-rw-lo-l85-e365/tailscale-patches.jpg)

Tailscale has released [version 1.104.4](https://github.com/tailscale/tailscale/releases/tag/v1.104.4) to fix flaws in its built-in SSH server that could let an attacker reach services and files on other servers that only the root user should be able to touch.

The flaws are in how Tailscale SSH forwards network connections, a job the Tailscale background process carries out with root privileges. To use them, an attacker must already control a device that the network's access rules permit to open an SSH session to the target, with forwarding allowed in that rule.

The flaws come from a report called [Tailworm](https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html), published days before the fix by Erica Windisch of Cyberdione Labs, who tested released versions of the Tailscale client and the self-hosted headscale control server in a lab.

Tailscale SSH decides who can connect using a device's identity and the network's policy file, not a password or key, so an attacker does not need stolen credentials, only a foothold on a device the policy already trusts.

The flaws "don't allow an unauthenticated attacker to connect to arbitrary Tailscale SSH servers," Tailscale said, and an attacker can still reach only the machines the policy file already allows.

Tailscale SSH's server runs only on Linux and the open-source macOS build; the attacker's own device can be any platform.

The problem is in socket forwarding. When a permitted SSH session forwarded a connection to a Unix socket on the server, the Tailscale process checked the path but then operated as root. A timing trick let an attacker swap in a different path after that check, defeating the safeguard meant to limit which sockets forwarding could reach.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

In Windisch's own tests, forwarding to the Docker control socket produced a root shell and read the system password file, /etc/shadow, with no administrator rights. Tailscale's bulletin describes the reach more narrowly, saying an attacker could get to root-only sockets such as the Docker socket or the tailscaled local API.

In 1.104.4, Tailscale changed the server to carry out forwarding as the logged-in user rather than as root, and to rely on the operating system's own file permissions in place of its earlier path check. The release covers 4 [security bulletins](https://tailscale.com/security-bulletins):

* TS-2026-014: the SSH socket-forwarding flaws above, which let a permitted session reach root-only sockets such as the Docker socket or the tailscaled local API.
* TS-2026-015: a way for a permitted SSH session to use up a server's memory and crash the Tailscale process, cutting all Tailscale networking on that node.
* TS-2026-016: a flaw in tailscale serve where a forward to a Unix socket could reach the tailscaled local API, giving remote control of the node, plus a related socket-swap issue.
* TS-2026-017: a flaw where, with TLS serve and 2 or more mounts, one request could receive another mount's permission headers.

### What to Do

Users of Tailscale SSH should update to version 1.104.4 or later. If you cannot update a server yet, you can turn off SSH forwarding on it by setting TS\_SSH\_DISABLE\_FORWARDING=1 in the tailscaled service environment and restarting the service, which Tailscale says turns off forwarding without disabling Tailscale SSH and blocks several of the more serious findings.

Tailscale also recommends reviewing SSH access rules so that only the users and devices that need access have it.

Tailscale suggests using SSH check mode, which requires a user to sign in again before a session starts, for sensitive systems. Check mode does not stop these forwarding flaws: it guards the start of a session, whereas the forwarding occurs within a session that has already been approved.

If a server may already have been compromised, Windisch's report says the fix alone is not enough. A stolen device key stays valid until the device is deleted at the control plane, because reimaging the machine does not revoke it. Tailscale's notices do not cover this case.

The picture is worse on headscale, the self-hosted control server. On headscale, SSH forwarding is granted on every accepted session and cannot be turned off in the policy, so Windisch's report says every SSH grant there should be treated as giving root. The newest headscale release, version 0.29.5 from October 13, does not fix the reported issues.

### Is It a Worm?

Windisch called the chain "wormable." In her tests, one compromised device could spread to every device the policy allowed, with no passwords, no stolen keys, and no user action, in under a second per step.

Two controls stopped the spread in those tests. Writing access rules as single device-to-device pairs held it back, and binding device keys to hardware such as a TPM kept a stolen identity from being reused elsewhere.

Tailscale rejected the worm description. The findings do not describe self-replicating malware that spreads between machines on its own, the company said, but lateral movement limited to the connections a policy file already allows.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

It called the privilege-escalation problems ["serious security issues,"](https://tailscale.com/ssh-investigation-update) said it had reproduced th...