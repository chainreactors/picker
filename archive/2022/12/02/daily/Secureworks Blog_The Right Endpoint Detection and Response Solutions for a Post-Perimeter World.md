---
title: The Right Endpoint Detection and Response Solutions for a Post-Perimeter World
url: https://www.secureworks.com/blog/the-right-endpoint-detection-and-response-solutions-for-a-post-perimeter-world
source: Secureworks Blog
date: 2022-12-02
fetch_date: 2025-10-04T00:19:26.694384
---

# The Right Endpoint Detection and Response Solutions for a Post-Perimeter World

[Skip to Main Content](#main-content)[Skip to Footer](#cmp-footer-a1fbb96a)

[Sophos completes Secureworks acquisition](https://www.sophos.com/en-us/press/press-releases/2025/02/sophos-completes-secureworks-acquisition)

* [Experiencing a Breach?](https://www.sophos.com/en-us/products/incident-response-services/emergency-response)
* Contact Us
* Support
* [Blog](/blog)
* English

[![logo](/-/media/images/logos/logo_new.svg?iar=0&hash=61254867B6545667A8E17DD1352849AF)](/ "Secureworks")

* Platform
* Services
* Solutions
* About
* Partners
* Resources

[Request Demo](/contact/request-demo-xdr)

Blog

# The Right Endpoint Detection and Response Solutions for a Post-Perimeter World

The endpoint isn’t the end anymore. It’s time to rethink how you’re defending it.

![The Right Endpoint Detection and Response Solutions for a Post-Perimeter World](/-/media/images/insights/blog/2022/the-right-endpoint-detection-and-response-solutions-for-a-post-perimeter-world/the-right-endpoint-detection-and-response-solutions-for-a-post-perimeter-world-360x190.png?h=190&iar=0&w=360&hash=75BDB687E9AD18E964AE9D36CF1AC87B?io=transform:fit,width:4568,height:2568)

[Kyle Falkenhagen](/author/Kyle-Falkenhagen)

December 1, 2022

At one time, it made sense to think about cybersecurity primarily in terms of endpoints and perimeters. After all, if you configured your firewall correctly and had effective anti-malware defenses on all your systems, your risk of a high-impact breach would be substantially diminished.

But if you still believe this — or if you’re behaving like those who still mistakenly believe this — you’re in more trouble than you think. Endpoint detection and response solutions – and the environments in which they perform — have changed dramatically. The truth is this: You have no perimeter.

And your endpoint protections, while certainly useful, when used alone are entirely inadequate for mitigating risk at scale in 2023 and beyond.

The empirical evidence couldn’t be clearer. Your end users are too easily phished. Your digital entwinement with your supply chain, customers, and partners is too intimate. And threat actors are too good at what they do.

You therefore face a set of stark, urgent choices when it comes to choosing the right endpoint detection and response solutions. Adopt Zero Trust or don’t. Embrace whole security or don’t. Deploy XDR or don’t. And if you don’t, be ready to accept the consequences.

## Hard Evidence From the Field

If you’re the cynical type who believes such talk is merely the fearmongering of a security vendor, c[onsider these concrete examples of recent intrusions](/resources/rp-irs-learning-from-incident-response-april-june-2022) that the Secureworks Incident Response team was called in to help clean up.

* In one, the threat actor first compromised an MSP — and then leveraged that foothold to escalate privileges and map the network. They installed a ScreenConnect client, dumped the LSASS to extract credentials, ran netscan.exe, and then moved laterally. This allowed them to view files on other accounts and install MegaSync to exfiltrate files — always uninstalling it after each session to avoid detection — and eventually deployed ransomware via PowerShell scripts.

  Sure, that’s a miss from the MSP. But every organization has connections like that to [contractors](/resources/rp-irs-learning-from-incident-response-april-june-2022). So, every organization is vulnerable to someone else’s security lapses.

* In another case, an organization that generally required MFA still had some utility accounts that only required single-factor authentication. A threat actor discovered these accounts, installed Cobalt Strike, gathered credentials, and mapped the network. Within 24 hours, the threat actor escalated privileges, moved laterally, exfiltrated more than 30 GB of data and documents, stole the Active Directory database, and used Group Policy Objects to deploy and execute GOLD HAWTHORNE’s Hive ransomware.

  So, no, there’s no such thing as Almost Zero Trust. It’s either Zero Trust or it’s vulnerable.

* Finally, there’s the example of the pro-Ukraine employees who knowingly downloaded and executed software that facilitated DDoS attacks against IP addresses geolocated in Russia — exposing the organization to malware and retaliatory attacks.

  The human beings that use your network, in other words, may have their own agenda.

## Zero Trust and Whole Security

These real-world examples and others underscore how critical it is for organizations to adopt Zero Trust and what some of us refer to as “whole security.” The reality is that previous iterations of traditional endpoint detection and response solutions have not achieved the holistic perspective required to be a whole security solution.

Zero Trust is a well-known concept in our world. It means that all access requires strong authentication based on multiple factors — potentially including multifactor proof of identity, location, and cross-checking of potential anomalies such as time-of-day and session duration. Zero Trust also means that access is diligently restricted to “just enough” — and is not propagated beyond explicitly required purposes.

Fundamentally, Zero Trust also means that you always assume there is a breach of your perimeter. The unavoidable truth this brings up — both operationally and conceptually — is that perimeter-focused security isn't really security. Instead, teams need to look at whole security as a way to avoid breaches.

Whole security is a related concept that’s sort of a superset of Zero Trust. While Zero Trust assumes a breach, whole security actively seeks to discover and identify it. And it does so by constantly scanning the environment for the breadcrumbs an attacker may leave — not just on endpoints, but across the network and the cloud as well. That’s what distinguishes the new model of whole security from the traditional model of endpoint/perimeter-centric security.

Zero Trust and whole security are thus much more than abstract concepts to which one can choose to follow. They are operational principles that SecOps teams must aggressively employ if they are to sufficiently mitigate the growing volume of threats against which perimeter/endpoint defenses alone are impotent.

## How to Strengthen Cyber Defenses in a Post-Perimeter World

You cannot implement Zero Trust and whole security with EDR-centric SecOps, because EDR by its very nature presupposes that endpoint telemetry is the best way to discover active threats.

But endpoint telemetry alone is not the best way to discover active threats. Active threats are best discovered — and are most accurately and promptly identified — by picking up all the detectable “breadcrumbs” threat actors leave across endpoints, networks, cloud, and other IT assets.

And for that, you must evolve beyond EDR by:

1. Extending your detection across your entire IT landscape to not only discover threats at your endpoint, but also the stealthy threats that move across silos and often go undetected if a pattern isn’t discovered.
2. Collaborate quickly around investigations by pulling in historical log data, threat intelligence and other experts who can quickly verify that a threat is a true positive and identify root cause.
3. Build in fast response actions that don’t just remediate threats at the endpoint but across all systems.

*In fact, there are now proven solutions on the market that do just that known as extended detection and response (XDR). XDR alone delivers the telemetry integration necessary for fast, effective threat detection.* EDR doesn’t do it. Neither do SOAR or SIEM. Only with XDR can you quickly detect scattered APT breadcrumbs, confidently identify known TTEs by those breadcrumbs, and thereby interdict APTs more rapidly and decisively — greatly reducing the odds of adverse impacts.

Of course, XDR alone won’t keep your organization safe. You also need to implement Zero Trust controls, intensify your ...