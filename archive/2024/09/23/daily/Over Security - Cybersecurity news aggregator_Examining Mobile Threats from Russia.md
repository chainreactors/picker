---
title: Examining Mobile Threats from Russia
url: https://blog.bushidotoken.net/2024/09/examining-mobile-threats-from-russia.html
source: Over Security - Cybersecurity news aggregator
date: 2024-09-23
fetch_date: 2025-10-06T18:25:08.409679
---

# Examining Mobile Threats from Russia

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### Examining Mobile Threats from Russia

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[September 22, 2024](https://blog.bushidotoken.net/2024/09/examining-mobile-threats-from-russia.html "permanent link")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhUPEY5Qfs5Hf5CznXYZajQFf7BcL-M5tWw75pG_m4dfHTqRHUfwYGig1gC8QGXoLh2VGNs5y1ePlBUuwz3EH6wbjszo8mHjvhQFzcqCt64xVgJFWTyhlGwGDia8ZNtQnCWKd0XzwGCpef1ng_1pjEHVvwp-CY2Wi_nT7GqY70ay25flRzo63rClvlmz4ML=w640-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEhUPEY5Qfs5Hf5CznXYZajQFf7BcL-M5tWw75pG_m4dfHTqRHUfwYGig1gC8QGXoLh2VGNs5y1ePlBUuwz3EH6wbjszo8mHjvhQFzcqCt64xVgJFWTyhlGwGDia8ZNtQnCWKd0XzwGCpef1ng_1pjEHVvwp-CY2Wi_nT7GqY70ay25flRzo63rClvlmz4ML)

## Introduction

Russian state-sponsored threat groups, such as Fancy Bear (APT28),
Cozy Bear (APT29), Turla, and Sandworm, among others, are well-known for complex
cyber-espionage operations, targeted intrusions, destructive attacks, and
disinformation campaigns. Some of the capabilities of Russian threat groups,
however, are not well-known and extend beyond the usual targeting of government
and critical infrastructure enterprise networks.

The main three Russian intelligence services (GRU, FSB,
and SVR) have also conducted less well-known and underreported intelligence
gathering campaigns against Android and iPhone users delivering spyware as well
as collecting credentials for specific mobile applications.

In this blog, I will be examining open source intelligence
(OSINT) reports, leveraging the findings and citing investigations
conducted by other threat researchers, to present my key findings and an overall
assessment of these mobile threat campaigns.

## Background on Mobile Threats from Russia

Multiple threat groups belonging to each of the three main Russian
intelligence agencies have been observed leveraging mobile spyware or targeting
the credentials of specific mobile applications over the course of the last decade.

Having dedicated mobile spyware and exploit developers or
acquiring these capabilities from external third-party vendors is expensive and
requires vast resources. It further shows the considerable investments,
willingness, and value the Kremlin places upon offensive cyber operations against
its targets.

## Android Malware used by Russia

#### Fancy Bear’s X-Agent for Android

On 22 December 2016, CrowdStrike [published](https://www.crowdstrike.com/blog/danger-close-fancy-bear-tracking-ukrainian-field-artillery-units/)
a report on X-Agent, an Android malware that CrowdStrike linked to Fancy Bear,
a threat group attributed to the [Russian
GRU Unit 26165](https://www.gov.uk/government/news/uk-enforces-new-sanctions-against-russia-for-cyber-attack-on-german-parliament). The researchers uncovered a fake Android APK posing as an application developed in Ukraine by an officer of the 55th Artillery Brigade to help reduce targeting
time for the soviet-era D-30 122mm towed howitzer. Between 2014 and 2016, Fancy
Bear reportedly distributed the Android X-Agent malware via Ukrainian military
forums. Successful deployment of the Fancy Bear malware via this fake application would have facilitated reconnaissance against Ukrainian troops, such as their
location and their communications. This sensitive information gleaned
from infected devices could easily be useful to identify positions of Ukrainian
artillery forces and target them, giving themselves a battlefield advantage.

#### Monokle

On 24 July 2019, Lookout shared a [report](https://www.lookout.com/threat-intelligence/article/monokle)
on Monokle, a custom Android spyware developed by the Russian private contractor firm Special
Technology Centre (STC). The very same STC has also been [sanctioned](https://obamawhitehouse.archives.gov/the-press-office/2016/12/29/fact-sheet-actions-response-russian-malicious-cyber-activity-and)
by the US government for supporting the GRU with Russian interference in the
2016 US presidential election. Interestingly, Monokle was developed by STC
alongside its Android antivirus solution called Defender (in Russian).

What made Monokle notable was its novel methods to
exfiltrate data from the victim's device, even without root access. It made
extensive use of Android accessibility services to collect information from
Android apps installed on the target device and could download and use an
attacker-supplied SSL/TLS certificate that enabled Adversary-in-the-Middle (AiTM) attacks.
Other capabilities of Monokle include its use of keyword dictionaries to
search for topics of interest on the device as well as recording the device's
screen when locked allowing it to steal the user's PIN, pattern, or password.

Monokle was reportedly distributed via valid Android APKs
with legitimate functionality, so users would be less suspicious of it. Lookout
has observed a low number of samples of Monokle being deployed in the wild as
early as March 2016 in highly targeted attacks. Targets of Monokle were likely
located in the Caucasus or from the Ahrar al-Sham militant group
in Syria, as well as other English-, Arabic- or Russian-speaking victims.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi-jG_G7NOzfPOJYwtADZ78qk6-c6AKU8YpaGlgPPnNWJT7TIiuJnMv2MnyyvQ-IcrPwnrC3-US1QT5XPBmArN-eJC09kCcKAJgoYYuxyfEl7GVA_Y3as5u_H1bfp0o_tIsf4W9oiMoH30TFxjLShrwlJ9b0KKiwkSL4JHSQXB_OqiQlCex3X8yOGONltS0=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEi-jG_G7NOzfPOJYwtADZ78qk6-c6AKU8YpaGlgPPnNWJT7TIiuJnMv2MnyyvQ-IcrPwnrC3-US1QT5XPBmArN-eJC09kCcKAJgoYYuxyfEl7GVA_Y3as5u_H1bfp0o_tIsf4W9oiMoH30TFxjLShrwlJ9b0KKiwkSL4JHSQXB_OqiQlCex3X8yOGONltS0)

Figure 1: Malicious
apps containing Monokle. (Source: Lookout)

#### Sandworm’s Android Campaigns

On 26 November 2019, Google [reported](https://blog.google/threat-analysis-group/protecting-users-government-backed-hacking-and-disinformation/)
they had discovered a series of Android malware campaigns tied to
Sandworm, a threat group linked to the [Russian
GRU Unit 74455](https://www.gov.uk/government/news/uk-exposes-series-of-russian-cyber-attacks-against-olympic-and-paralympic-games). The first detected Sandworm campaign targeted users in
South Korea in December 2017. They modified up to eight legitimate Android
applications with malware and uploaded them to the Google Play Store using
attacker-created developer accounts. These apps, however, had fewer than 10
total installs each. The second detected Sandworm campaign targeted users in
Ukraine and was earlier in September 2017. The adversary used a similar tactic to deploy a fake
version of the UKR.net email app on the Google Play Store, which managed to
earn around 1,000 total installs.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhVRytNfnz8IjcUoCAPBU5GZ_qy3Mk1S-2fJ-0sTlmXf-iKQDDSIAep1sfruAmf5kGbUbfR9D8P0OSgZ0xjdjL0Iqa1GazYz5lL1idFp4Y5g2pvpm26G00fjzr3OGZVVAAKDXHNp0hLdneeX59wYXturHXK2lqiKFwBFe1cHW35ojsZkyNH_4MoHCij1JgY=w640-h464)](https://blogger.googleusercontent.com/img/a/AVvXsEhVRytNfnz8IjcUoCAPBU5GZ_qy3Mk1S-2fJ-0sTlmXf-iKQDDSIAep1sfruAmf5kGbUbfR9D8P0OSgZ0xjdjL0Iqa1GazYz5lL1idFp4Y5g2pvpm26G00fjzr3OGZVVAAKDXHNp0hLdneeX59wYXturHXK2lqiKFwBFe1cHW35ojsZkyNH_4MoHCij1JgY)

Figure 2: Malicious
apps by Sandworm targeting South Korea. (Source: Google)

The third Sandworm campaign Google detected involved
spear-phishing attacks towards Android app developers also in Ukraine and was later in
November 2018. In at least one case, Sandworm managed to compromise an Android
app developer from Ukraine with several published Google Play Store apps, one
with over 200,000 installs. Using the hijacked developer account, Sandworm
built a customer backdoor into one of the legitimate apps, signed it with one
of the developer’s stolen code-signing keys, and attempted to publish it on the Google
Play Store. However, the Google Play Protect team caught the attempt at the
time of ...