---
title: Maximizing IOC Impact
url: https://www.netresec.com/?page=Blog&month=2026-06&post=Maximizing-IOC-Impact
source: NETRESEC Network Security Blog
date: 2026-06-08
fetch_date: 2026-06-09T06:03:09.427977
---

# Maximizing IOC Impact

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Monday, 08 June 2026 07:00:00 (UTC/GMT)

## [Maximizing IOC Impact](/?page=Blog&month=2026-06&post=Maximizing-IOC-Impact)

I’ve been thinking about threat intelligence lately. Specifically: indicators of compromise (IOC), how and where to share them to cause maximum pain to adversaries and help as many organizations as possible protect themselves.

![Network IOCs are without doubt causing less pain to adversaries than other IOCs. But they are causing pain!](https://media.netresec.com/images/network-iocs-meme_809x692.png)

I regularly analyze malware traffic from sandboxes such as [ANY.RUN](https://app.any.run/), [Triage](https://tria.ge/), [JoeSandbox](https://www.joesandbox.com/) and [Hybrid Analysis](https://hybrid-analysis.com/). Pulling fresh PCAPs is an easy way to find malware command-and-control (C2) traffic to previously unknown C2 servers. This method can even reveal new and unreported C2 protocols. I often use [CapLoader](https://www.netresec.com/?page=CapLoader) and [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) to extract network IOCs, such as:

* Domain names
* IP:port
* URIs
* JA3 / JA3S hashes
* JA4 fingerprints
* X.509 certificate thumbprints
* packet pattern/signature

These indicators can be found in the lower sections of David J. Bianco’s [pyramid of pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html). But that doesn’t mean they’re not worth sharing — they’re easy to detect, have low false-positive rates, and are very actionable. Their main drawback is short lifetime, so rapid and wide IOC distribution matters.

![ASCII IOC Pyramid of Pain](https://media.netresec.com/images/IOC-Pyramid-of-Pain_2048x1123.webp)

*Image: ASCII pyramid from [Optimizing IOC Retention Time](https://netresec.com/?b=25Be9dd)*

False positives are a real concern, so manual verification of an IOC is required before sharing. Many IOCs are already reported to threat-intel sharing platforms, like [ThreatFox](https://threatfox.abuse.ch/), [OTX](https://otx.alienvault.com/) or one of the many [MISP](https://www.misp-project.org/communities/) instances out there, but I frequently find ones that aren’t. When I discover an IOC, I typically consider these options:

* Report directly to the hosting provider, registrar or network owner.
* Share with a national or sector CERT.
* Share with an ISAC.
* Publish to threat-sharing platforms ([ThreatFox](https://threatfox.abuse.ch/)/[URLhaus](https://urlhaus.abuse.ch/)/[OTX](https://otx.alienvault.com/)/[MISP](https://www.misp-project.org/communities/)/[AbuseIPDB](https://www.abuseipdb.com/)/etc).
* Publish in a [blog](https://netresec.com/?b=261f535) [post](https://netresec.com/?b=262adb9) or on [social](https://infosec.exchange/%40netresec/115905237000922504) [media.](https://infosec.exchange/%40netresec/116046513072954545)

I generally pick outlets case-by-case. Sometimes by convenience, sometimes by where I expect to achieve the greatest impact. Is there a single best destination? Often not, it depends.

Sending an IOC to every channel is comprehensive, but time-consuming. Ideally, a verified IOC drop point that automatically propagates to all the right places would be fantastic! But as far as I know, no such service exists.

I mostly look at malware that hit many victims, which is why it makes sense to prioritize fast, broad distribution (free threat-intel services and blog/social posts). But I have also investigated APT attacks and state-sponsored campaigns, such as [Man-on-the-Side attacks](https://www.youtube.com/watch?v=AIlFENir-8E), [SSL](https://netresec.com/?b=14AA3E6) [MITM](https://netresec.com/?b=14955CB) attacks [in China](https://netresec.com/?b=1328C6B) as well as DNS traffic from [Cozy Bear’s SolarWinds hack](https://netresec.com/?b=21A27a0). The right place to share IOCs for APT attacks is often different than for mainstream malware. For targeted or sensitive operations, I recommend reaching out to victims, CERTs or a trusted intermediary.

![crossroads signs](https://media.netresec.com/images/crossroads_1800x1064.webp)

Factors affecting the choice of IOC sharing method:

* Scope and scale of impact: Mass-distribution malware should be blocked widely. Notify specific victims or CERTs on targeted attacks.
* Lifetime and volatility: Short-lived IOCs (IPs, domains) benefit from fast, broad distribution. Longer-lived indicators are better shared in reports or blog posts that provide more depth and context.
* False-positive risk: Prefer channels that support easy updates/removals and allow others to validate or comment.
* Remediation: If a takedown or abuse report is appropriate, contact providers or registrars directly.
* Victimology: Choose platforms aligned with who needs to act. ISACs/CERTs for sectors, targeted notifications for known victims, open feeds for broad coverage.

Many companies and organizations engage in mutual sharing in closed trust groups, expecting that by sharing with others, they will return the favor. This creates a "win-win" situation for the trust group members, while the wider community misses out. As someone who doesn't require IOCs, I find that this approach can limit my reach. I prefer to get information out to as many people as possible, as quickly as possible, with minimum effort.
I’ve also noticed a growing commercialization of threat intelligence, which is both good and bad. It can provide funding for threat-intel platforms, but may also limit reach when threat feeds and APIs get paywalled.

Workflow for IOC sharing:

1. Identify a potential malicious indicator (IP/domain/JA4 etc).
2. Pivot on the indicator to verify maliciousness and check for false positives.
3. If uncertain, ask in a trust-group, forum or request input on social media.
4. Check existing public feeds and databases for the IOC.
5. Assess urgency, impact, and victimology.
6. If new and high-impact: submit to one or several open sharing platforms.
7. If you have additional context: share it in a blog post or social notice.
8. If targeted or sensitive: notify the appropriate CERT or affected organizations privately.
9. If abuse/takedown is feasible: report to provider/registrar or request assistance from a national CERT.

I’m interested in hearing how others approach this. What works for you, and how do you maximize IOC sharing with minimal effort? Reach out via [social](https://infosec.exchange/%40netresec/116713213615485124) [media](https://bsky.app/profile/netresec.com/post/3mnr4qrmzb22n), [email](https://www.netresec.com/?page=AboutNetresec) or share your thoughts in a writeup or blog post. Also, if you run an automated IOC propagation service, please [reach out](https://www.netresec.com/?page=AboutNetresec)!

Posted by Erik Hjelmvik on Monday, 08 June 2026 07:00:00 (UTC/GMT)

Tags:
#[IOC](/?page=Blog&tag=IOC)​
#[C2](/?page=Blog&tag=C2)​
#[ThreatFox](/?page=Blog&tag=ThreatFox)​

Short URL:
<https://netresec.com/?b=26653f3>

### Recent Posts

» [Maximizing IOC Impact](/?page=Blog&month=2026-06&post=Maximizing-IOC-Impact)

» [PolarProxy 2.0.1 Released](/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released)

» [CapLoader 2.1.0 Released](/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released)

» [PolarProxy 2.0 Released](/?page=Blog&month=2026-05&post=PolarProxy-2-0-Released)

» [Remcos Alerts from FlowCarp in EveBox](/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox)

» [FlowCarp Identifies Protocols](/?page=Blog&month=2026-05&post=FlowCarp-Identifies-Protocols)

» [CISA mixup of IOC domains](/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains)

» [njRAT runs MassLogger](/?page=...