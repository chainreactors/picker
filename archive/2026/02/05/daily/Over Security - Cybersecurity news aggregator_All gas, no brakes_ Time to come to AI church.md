---
title: All gas, no brakes: Time to come to AI church
url: https://blog.talosintelligence.com/all-gas-no-brakes-time-to-come-to-ai-church/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-05
fetch_date: 2026-02-06T04:09:58.564024
---

# All gas, no brakes: Time to come to AI church

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# All gas, no brakes: Time to come to AI church

By
[Joe Marshall](https://blog.talosintelligence.com/author/joe-marshall/)

Thursday, February 5, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Brothers and sisters, gather close for a moment. We are all security followers here gathered in fellowship and community, with one joyful spirit to fight the good fight and do good out there in the security world.

It is with that spirit that I have to mention [Clawdbot](https://openclaw.ai/). Clawdbot (aka Moltbot or OpenClaw) is a locally run open-source agentic application that acts on your behalf. Want to check into a flight? Reply to an email? Vibe code Skynet? Clawdbot's got you. As of writing this, it has 157k stars on Github. To make it work, the only teeny tiny thing you have to do is feed Clawdbot all of your private information (like logins, passwords, and API keys) and you’re off to the races. No big deal, right? It completely acts on your behalf, with little input if that’s what you desire. If that just made the hair on the back of your neck stand up a little, yeah, me too.

By now, the security hot mess that is Clawdbot has made its way from obscurity into the mainstream news, [and it’s all bad](https://cybersecuritynews.com/clawdbot-chats-exposed/). Shocker.

This is important. I cannot stress this enough. Everyone in the room who ran as fast as possible and installed Clawd/Moltbot, I need you to rethink things. To make this agentic platform act on your request and/or autonomously, you mustsurrender private information to an unvetted, unsecured agentic engine. Now, as a result, your logins, passwords, and more are [sitting in a plaintext file](https://www.theregister.com/2026/01/27/clawdbot_moltbot_security_concerns/), ripe for easy stealing.

And then there’s the Skills. You can teach your wildly productive agent to do new things! Edit a spreadsheet! Write GPOs! Play a game of [global thermonuclear war](https://youtu.be/KXzNo0vR_dU?si=Od4a8Ld5LYrCFlHS)! The sky is the limit. All it requires is you to give over complete system admin/root access to your Clawd agent. Just understand that Skills are unvetted and unsecured, and already are [being actively exploited](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html).

As disciples of security, we understand installing first and asking questions later is practically asking to get pwnt. It has never panned out well for the end user, but usually [quite well for attackers](https://www.microsoft.com/en-us/security/blog/2025/05/21/lumma-stealer-breaking-down-the-delivery-techniques-and-capabilities-of-a-prolific-infostealer/) who very much understand the threat landscape. Clawdbot is no exception.

I need you to be highly skeptical of any AI tool rush. Do not be consumed by The Hype. Much like OpenAI’s Atlas, AI tools are being aggressively released to the market and installed, often with [security vulnerabilities everywhere](https://www.axios.com/2025/10/28/atlas-chatgpt-openai-web-browser-security-privacy). Resist the urge to throw yourself upon tools or platforms that have rushed to address a market need — they usually had no forethought about security, or just push an unreasonable assumption of risk on the end user.

Security is being sacrificed on the altar of convenience, as AI outpaces our ability to secure it. Brothers and sisters, I’m not asking you to reject the future. AI is going to neat places. I’m asking you to guard yourself as you walk into it.

## The one big thing

In Talos’ [latest blog](https://blog.talosintelligence.com/knife-cutting-the-edge/), we share the discovery of "DKnife," a modular Linux-based attack framework that compromises routers and edge devices to intercept network traffic, steal credentials, and deliver malware. Active since at least 2019, DKnife can hijack legitimate software updates and bypass endpoint security, posing a significant risk to both users and organizations.

### Why do I care?

DKnife can take over routers and edge devices, letting attackers spy on users, steal passwords, and install malware without being easily noticed. Because it can break through traditional antivirus defenses and target many types of devices, even networks with good security could be at risk if these gateway devices are not protected.

### So now what?

Review and harden the security of routers, gateways, and other Linux-based edge devices. Audit for unauthorized firmware or binaries, make sure you’re enforcing strong authentication and certificate validation, and monitor for unusual traffic patterns or update behaviors. Implement network segmentation and make sure your devices are getting updates directly from trusted vendors.

## Top security headlines of the week

You mean, other than the mess that is Clawdbot? Sorry, the first headline shows we’re not escaping that any time soon:

**Weaponized VS Code add-on** **ClawdBot** **sneaks in** **ScreenConnect** **RAT**
Security researchers flagged a malicious VS Code extension named “ClawdBot Agent” on the Visual Studio Marketplace. Microsoft swiftly removed it after a report, but not before it tricked developers into installing a fully functional trojan. ([Cyber Press](https://cyberpress.org/clawdbot-vs-code-rat-sneaks-in/))

**Windows malware uses Pulsar RAT for live chats while stealing data**
A newly discovered Windows malware campaign combines the Pulsar RAT with Stealerv37, using Donut loader shellcode injection into explorer.exe to operate entirely in memory while evading traditional antivirus detection. ([HackRead](https://hackread.com/windows-malware-pulsar-rat-live-chats-steal-data/?utm_source=tldrinfosec))

**eScan** **confirms update server breached to push malici...