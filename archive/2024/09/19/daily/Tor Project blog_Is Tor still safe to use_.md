---
title: Is Tor still safe to use?
url: https://blog.torproject.org/tor-is-still-safe/
source: Tor Project blog
date: 2024-09-19
fetch_date: 2025-10-06T18:28:02.831802
---

# Is Tor still safe to use?

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Is Tor still safe to use?

by [isabela](/author/isabela) and [pavel](/author/pavel)
| September 18, 2024

![](/tor-is-still-safe/lead.png)

*+++ Update October 10th, 2024 +++*

*In response to the claims made in [Deutsche Welle's (DW)](https://www.dw.com/de/daniel-mo%C3%9Fbrucker-immer-mehr-tor-knoten-werden-%C3%BCberwacht/a-70322301) reporting, which suggests that v3 Onion Services were impacted by this attack, we cannot confirm whether the affected service had Vanguard protections enabled. Given the time frame of the attack, it is likely the affected service lacked Vanguard protections, which made Onion Services more vulnerable to relatively easy guard discovery attacks although the exact method remains unclear.*

*We are continuing to investigate this issue and will provide updates as more information becomes available.*

---

We are writing this blog post in response to an investigative news story looking into the de-anonymization of an Onion Service used by a Tor user using an old version of the long-retired application Ricochet by way of a targeted law-enforcement attack. Like many of you, we are still left with more questions than answers--but one thing is clear: Tor users can continue to use Tor Browser to access the web securely and anonymously. And the Tor Network is healthy.

Please note, that for the great majority of users worldwide that need to protect their privacy while browsing the Internet, Tor is still the best solution for them. We encourage all Tor users and relay operators to always keep software versions up to date.

From the limited information The Tor Project has, we believe that one user of the long-retired application Ricochet was fully de-anonymized through a guard discovery attack. This was possible, at the time, because the user was using a version of the software that neither had Vanguards-lite, nor the vanguards addon, [which were introduced to protect users from this type of attack](https://blog.torproject.org/announcing-vanguards-add-onion-services/). This protection exists in [Ricochet-Refresh](https://github.com/blueprint-freespeech/ricochet-refresh), a maintained fork of the long-retired project Ricochet, since version 3.0.12 released in June of 2022.

Vanguards-lite, released in Tor 0.4.7, protects against the possibility of combining an adversary-induced circuit creation with circuit-based covert channel to obtain a malicious middle relay confirmed to be next to the user's Guard. Once the Guard is obtained, netflow connection times can be used to find the user of interest. In this case, the netflow attack could proceed quickly, because the attacker was able to determine when the user was online and offline due to their Onion Service descriptor being available, combined with the low number of users on the discovered Guard.

## Responsible Disclosure

In contrast to the CCC, Chaos Computer Club, who was provided access to the documents related to the case and was able to analyze and validate the reporter's assumptions, we were only provided a vague outline and asked broad clarifying questions that left us with uncertainty of the facts, and questions of our own. While we appreciate the journalist contacting us, this same access was not given to the Tor Project.

Given the potential risk to our users, we decided to go public. We requested that anyone with additional information about the case share it with us. This would allow us to conduct our own analysis and determine the best course of action to protect our users.

To be clear, The Tor Project did not intend to ask for the sources of the story, but sought to understand what evidence existed for a de-anonymization attack to accurately respond to the investigating reporter's questions and assess our disclosure responsibilities. And we continue to have an interest in obtaining more information about how Onion Services users were de-anonymized. If we had access to the same documents as CCC, it would be possible to produce a report with more clarity regarding the actual state of the Tor network and how it affects the great majority of its users.

We need more details about this case. In the absence of facts, it is hard for us to issue any official guidance or responsible disclosures to the Tor community, relay operators, and users.

### We are calling for more information from you.

If you have any information that can help us learn more about this alleged attack, please email security@torproject.org.

If you want to encrypt your mail, you can get the OpenPGP public key for this address from [keys.openpgp.org](http://keys.openpgp.org/). Fingerprint: 835B 4E04 F6F7 4211 04C4 751A 3EF9 EF99 6604 DE41

Your assistance will help all of us take the necessary steps and precautions to keep Onion Services safe for the millions of users that rely on the protections Tor provides.

## A healthy network

It is important to note that Onion Services are only accessible from within the Tor network, which is why the discussion of exit nodes is irrelevant in this case. But we would like to share that the number of exit nodes has significantly increased over the past two years, with over 2,000 now available. To the best of our knowledge, the attacks happened between 2019-2021.

While it is fair to question the concentration of these nodes in certain countries or operations, this has very little to do with the described attack from what we learned in the articles published so far. The attacks occurred on an old version of the long-retired application Ricochet that lacked new features The Tor Project has released since to mitigate against the kind of 'timing' analysis described in the articles. The most current versions of Ricochet-Refresh have such protections in place.

Another important thing to mention is the longevity of the user connection for such 'timing' analysis to be successful. A Tor Browser user that does not maintain its connection for a long time, is less vulnerable to such analyses.

After the period of the attacks described to us, 2019-2021, our Network Health team has [flagged thousands of bad relays which the Directory Authorities then voted to remove](https://blog.torproject.org/tor-network-community-health-update/). Those included many that would come from a single operator or tried to enter the network in large scales. The Network Health team has implemented processes to identify possible large groups of relays that are suspected to be managed by single operators and bad actors and not allow them to join the network.

The Tor Project knows that diversity of relays is a pressing issue for the Tor community and we are having many conversations with our community and relay operators about this subject to understand how we can address common pain points together.

Over the last year alone, we've launched a number of new initiatives such as the [EFF's Tor University Challenge](https://www.eff.org/press/releases/eff-launches-tor-university-challenge) and the [introduction of the Tor's network health API at DEF CON 32 earlier this year](https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20presentations/DEF%20CON%2032%20-%20Silvia%20Puglisi%20Roger%20Dingledine%20-%20Measuring%20the%20Tor%20Network.pdf). Tor's bandwidth has actually increased substantially in recent years, as shown in this link: <https://metrics.torproject.org/bandwidth.html?start=2013-06-20&end=2024-09-18>. This means the Tor network is faster than it has ever been. And we continue to conduct outreach campaigns and efforts to grow the network.Â

## You can help

We encourage those who can to volunteer and contribute bandwidth and relays to grow and diversify the Tor network. By ensuring hardware, software, and geographic ...