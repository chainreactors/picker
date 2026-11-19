---
title: UAT-12643: Suspected North Korea-aligned actor blends blockchain resilience with targeted infostealing
url: https://blog.talosintelligence.com/uat-12643-suspected-north-korea-aligned-actor-blends-blockchain-resilience-with-targeted-infostealing/
source: Over Security
date: 2026-11-18
fetch_date: 2026-11-19T09:47:18.048201
---

# UAT-12643: Suspected North Korea-aligned actor blends blockchain resilience with targeted infostealing

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

# UAT-12643: Suspected North Korea-aligned actor blends blockchain resilience with targeted infostealing

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Wednesday, November 18, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[RAT](https://blog.talosintelligence.com/category/rat/)
[Stealer](https://blog.talosintelligence.com/category/stealer/)

* Cisco Talos discovered malicious infrastructure associated with a financially motivated threat group we are tracking as UAT-12643.
* The actor’s arsenal has several payloads including the Go-based Overlord remote access trojan (RAT), a Python-based infostealer internally labelled “Good Game,” and a multi-cryptocurrency clipboard hijacker.
* The threat actor is likely operating a campaign targeting cryptocurrency holders, gaming platform account owners, and VoIP software users based on the lure file names of the initial vectors and the payloads.
* The Overlord RAT implements a command-and-control (C2) resilience technique in which encrypted server URLs are embedded in Solana blockchain transaction memos.

---

## Victimology

The threat actor is potentially targeting victims in Europe, according to the payload’s keyword-based file harvesting capability, which specifically targeted documents that had file names in English, French, Spanish, and Portuguese.

Based on the lure themes and payload file names, the potential victim pool spans across multiple verticals. A lure financial statement decoy PDF — launched when the Good Game stealer is executed — indicates targeting finance and accounting staff. The Viber trojanized installer lure targets messaging platform users, while additional payload variants of files named microsip indicate targeting VoIP softphone operators, consistent with call-center or business telephone environments. Cryptocurrency and gaming users are also targeted by both the clipboard hijacker and the infostealer.

## Potential links to North Korea-aligned actors

Talos assesses with low confidence that UAT-12643 is a North Korea-aligned advanced persistent threat (APT) actor based on overlaps in tactics, techniques, and procedures (TTPs) with those of the other known North Korean APT actors.

In the current campaign, Talos observed that the actor is using the Overlord RAT as one of their payloads. The threat cluster called UNK\_DeadDrop, likely a North Korean threat actor, had employed the Overlord RAT in their earlier campaigns as reported by the security researchers in [June 2026](https://www.proofpoint.com/us/blog/threat-insight/dont-fear-repo-unkdeaddrop-phishing-campaign-targets-developers-steal).

The Overlord RAT variant observed in this campaign implements a blockchain C2 resilience technique with Solana blockchain transactions. This technique was first reported in [March 2026](https://intel.breakglass.tech/post/lazarus-group-is-using-the-solana-blockchain-as-a-dead-drop-c2-channel-and-nobody-noticed-for-4-months), employed by the Lazarus APT group. Although the implementation methodology differs (earlier, it was through Node.js), the technique of leveraging Solana transaction memo stayed consistent.

Talos is aware that Overlord RAT and Solana blockchain hosting technique is also leveraged by other threat actors in their campaigns, as reported by external security researchers in [October 2026](https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html).

## Threat actor infrastructure

Talos observed that the actor hosted the malicious files on a server with IP address “41[.]216[.]188[.]11”, running a Flask-based file delivery service on port 8000 with resumable byte-range download support, and serving the payload staging directory. Due to the actor’s operational security failure, the server’s root folder was exposed to the internet, and Talos’ analysis of the exposed folder showed us actor’s tool sets, and the port numbers configured on the C2 server for different services.

|  |  |  |
| --- | --- | --- |
| Port number | Service | Payload file name |
| 8000 | Flask file-drop (HTTP) | Payload.exe, MyApp2.exe, HTA files |
| 5173 | Overlord RAT WebSocket C2 | Ovl.exe, Client.exe |
| 5656 | Python stealer TCP C2 | Ova.exe, MyApp2.exe |
| 5959 | Python stealer TCP C2 | Microsip-config.exe, microsip-config1.exe |

The actor does not use the traditional data exfiltration approach of transferring the data to the C2 server; instead, the stolen data is exfiltrated using two different services. The actor used the discord webhook, which receives an immediate notification that contains a victim’s fingerprint and a single click download link. The stolen data archive is uploaded to “gofile[.]io” and is later accessed by the actor through the download link.

We also observed the actor’s LNK generation script among the samples of the staging directory, indicating the actor’s lure creation workflow. The script accepts a payload URL and icon type (PDF, Word, or Windows Update) and generates a COM-based LNK with the spoofed and hidden execution.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/11/LNK.png)

Figure 1. Sample Windows shortcut generation script.

## Initial access vectors

Talos observed that the actor uses three different methods to gain initial access to victims’ environments. They have instrumented Windows shortcuts, HTA files, and XML files, so the embedded malicious instructions execute and grant initial access. In this campaign, we have not observed how the actor delivers these malicious initial vector files to victims’ machines.

### Weaponized LNK

One of the initial access vectors is the usage of the weaponized LNK files paired with the icons spoofed from legitimate system binaries to appear as a legitimate file in the Windows Explorer.
...