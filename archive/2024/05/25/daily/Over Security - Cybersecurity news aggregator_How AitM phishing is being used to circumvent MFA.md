---
title: How AitM phishing is being used to circumvent MFA
url: https://pushsecurity.com/blog/phishing-2-0-how-phishing-toolkits-are-evolving-with-aitm/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-25
fetch_date: 2025-10-06T17:19:28.365859
---

# How AitM phishing is being used to circumvent MFA

[Product](/product/)

Use cases

Resources

About

[Pricing](/pricing/)

[Book a demo](/demo/)

Try it freeLogin

[Product](/product/)Use casesResourcesAbout[Pricing](/pricing/)

LoginTry it free

[Book a demo](/demo/)

##### Explore use cases

[###### Zero-day phishing protection

Detect phishing TTPs directly in the browser and stop credential theft.](/uc/zero-day-phishing-protection)[###### Browser extension security

Shine a light on risky browser extensions.](/uc/browser-extension-security)[###### Account takeover detection

Stop ATO with stolen credential and compromised token detection.](/uc/account-takeover-detection)[###### Attack path hardening

Harden access paths with visibility, detection, and guardrails.](/uc/attack-path-hardening)[###### Incident response

Investigate and respond faster with unique browser telemetry.](/uc/incident-response)[###### Secure shadow SaaS

See and control shadow SaaS in the browser.](/uc/shadow-saas)

[Zero-day phishing protection](/uc/zero-day-phishing-protection)

[Browser extension security](/uc/browser-extension-security)

[Account takeover detection](/uc/account-takeover-detection)

[Attack path hardening](/uc/attack-path-hardening)

[Incident response](/uc/incident-response)

[Secure shadow SaaS](/uc/shadow-saas)

[Blog](/blog/)

/

Identity-based attacks

# Phishing 2.0 â how phishing toolkits are evolving with AitM

![Luke Jennings](https://images.ctfassets.net/y1cdw1ablpvd/4Hosb4zKi1dA0PUyDLMe1h/27e09d894861f2196ba794037986fb08/T016S22KZ96-U02NVQM7ZD4-57761d542d83-512.jpeg?r=max&w=3072&h=3072&fm=jpg&q=50)

Luke Jennings

Vice President, R&D

May 23, 2024 | 13 min read

Share this post

Identity-based attacks

Detection & response

## Attackers are increasingly using new phishing toolkits (open-source, commercial, and criminal) to execute Adversary in the Middle (AitM) attacks. AitM enables attackers to not just harvest credentials, but steal live sessions, allowing them to bypass traditional phishing prevention controls such as MFA, EDR, and email content filtering.

Phishing attacks have always been a go-to technique for both red teamers and real-world threat actors alike. Whether focused on harvesting creds or running malicious payloads, phishing has continued to be adapted to circumvent defenses and has remained highly effective due to this.

As MFA has become more common, classic password harvesting focused phishing attacks have become less effective. Typically, for a full account compromise, an MFA push notification or a one-time passcode (OTP) needs to be entered at the time of login. This means harvesting passwords and using them later is no longer effective alone, because an MFA factor is still required each time a valid login is performed.

Adversary-in-the-Middle (AitM) phishing is a newer variant of phishing that allows attackers to circumvent MFA protection. In this article, weâre going to look at what AitM phishing is, how it works, and what you can do about it.

## What is AitM phishing?

AitM phishing is a technique that uses dedicated tooling to act as a proxy between the target and a legitimate login portal for an application, principally to make it easier to defeat MFA protection.Â

While any login portal can be a target, attackers typically look for SSO login portals such as Microsoft Entra, Okta, or Google Workspace. This allows the target to log in successfully with a legitimate service they use and even continue to interact with it, while providing additional access to connected SSO apps if the attack is successful.Â

As itâs a proxy to the real application, the page will appear exactly as the user expects, because they are logging into the legitimate site â just taking a detour via the attackerâs device. For example, if accessing their webmail, the user will see all their real emails; if accessing their cloud file store then all their real files will be present, etc. This gives the method an increased sense of authenticity and makes the compromise less obvious to the user. However, because the attacker is sitting in the middle of this connection, they are able to observe all interactions and also take control of the authenticated session to gain control of the user account.Â

While this access is technically temporary, since the attacker is unable to re-authenticate in future without additional MFA prompts, in practice authenticated sessions can often last as long as 30 days or more if kept active. Additionally, there are a wide range of persistence techniques that allow an attacker to maintain some level of access to the user account and/or targeted application indefinitely.Â

Weâll revisit this point later, but for now letâs consider the two main techniques that are used to implement AitM phishing: Reverse web proxies and Browser-in-the-Middle techniques.

On-demand Webinar: Phishing 2.0 - Detecting Evilginx, EvilnoVNC, Muraena and Modlishka

[Watch Now](https://pushsecurity.com/resources/video/phishing-detecting-evilginx-evilnovnc-muraena-and-modlishka/)

### Reverse web proxy techniques

One common AitM phishing approach is to use tooling that acts as a reverse web proxy. For example, letâs say a victim is tricked into visiting a malicious domain. Under the hood, HTTP requests are passed between the victimâs browser and the real site via the malicious site. When the malicious site receives an HTTP request, it forwards this request on to the legitimate site it is impersonating, receives the response, and then forwards that on to the victim.Â

In practice, there are many technical challenges, such as rewriting all links and references to the impersonated site to ensure everything continues to be sent to the attacker. However, at a high level, it really is just acting as a reverse web proxy.

This is arguably the most scalable and reliable approach from an attackerâs point of view. Open-source tools that demonstrate this method include [Modlishka](https://github.com/drk1wi/Modlishka), [Muraena](https://github.com/muraenateam/muraena), and the ever popular [Evilginx](https://github.com/kgretzky/evilginx2). In the criminal world, there are also similar private toolsets available that have been used in many breaches in the past. A good example of this would be [Evilproxy](https://www.bleepingcomputer.com/news/security/evilproxy-uses-indeedcom-open-redirect-for-microsoft-365-phishing/).

One downside to this approach is that there are controls that can be put in place to block it. For example, application developers can hide obfuscated JavaScript code that will fail if the correct value is not produced, checking that the origin matches the expected (legitimate) domains or contains encrypted tokens including this material sent as part of the login process.Â

While your average small website is not going to be implementing such checks, major identity providers have a strong vested interest in evolving their defenses to block these techniques. At this point, itâs a cat-and-mouse game.Â

If you want to know more about this space, then definitely check out [Kuba Gretzkyâs talk on this at x33fcon](https://www.youtube.com/watch?v=C-Fh4sIdY8c).Â Â

### Browser-in-the-Middle (BitM) techniquesÂ

Another common approach is known as Browser-in-the-Middle (BitM). Rather than act as a reverse web proxy, this technique tricks a target into directly controlling the attackerâs own browser remotely using desktop screen sharing and control approaches, much like VNC and RDP. This enables the attacker to harvest not just the username and password, but all other associated secrets and tokens that go along with the login.Â

In this case, the victim isnât interacting with a fake website clone or proxy. They are literally remotely controlling the attackerâs browser to log in to the legitimate application without realizing. This is the virtual equivalent of an attacker handing their laptop to their victim, asking them to login to Okta for them, and then taking their laptop ...