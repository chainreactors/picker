---
title: The 2024 Threat Landscape State of Play
url: https://blog.talosintelligence.com/the-2024-threat-landscape-state-of-play/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-07
fetch_date: 2025-10-06T18:30:10.741944
---

# The 2024 Threat Landscape State of Play

# Cisco Talos Blog

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

![](/content/images/2024/09/TTP.jpg)

# The 2024 Threat Landscape State of Play

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Friday, September 6, 2024 08:59

[The Need to Know](/category/the-need-to-know/)

As we head into the final furlong of 2024, we caught up with Talos’ Head of Outreach Nick Biasini to ask him what sort of year it’s been so far in the threat landscape.

In this video, Nick outlines his two major areas of concern. He also focusses on one state-sponsored actor that has been particularly active this year (Clue: It rhymes with “Bolt Teaspoon”), and we talk about why the infostealer market has gone through a maturing phase, and why that’s an issue for defenders.

After you’ve watched the video, I’ve highlighted some of our threat spotlight blogs from the year so far below, which may be worth a revisit.

## 2024 in threat research:

**Jan. 18:**[**Exploring malicious Windows drivers**](https://blog.talosintelligence.com/exploring-malicious-windows-drivers-part-1-introduction-to-the-kernel-and-drivers/)

Drivers have long been of interest to threat actors, whether they are exploiting vulnerable drivers or creating malicious ones. Malicious drivers are difficult to detect and successfully leveraging one can give an attacker full access to a system. Part 1 of our Driver series served as a starting point for learning about malicious drivers while part 2, released in June, covered the I/O system, IRPs, stack locations, IOCTLs and more.

**Feb. 8:**[**New Zardoor backdoor used in long-term cyber espionage operation targeting an Islamic organization**](https://blog.talosintelligence.com/new-zardoor-backdoor/)

Talos discovered a new, stealthy espionage campaign that likely persisted since at least March 2021. The observed activity affects an Islamic non-profit organization using backdoors for a previously unreported malware family we have named “Zardoor.”

**Feb. 15:**[**TinyTurla Next Generation — Turla APT spies on Polish NGOs**](https://blog.talosintelligence.com/tinyturla-next-generation/)

This backdoor we called “TinyTurla-NG” (TTNG) was similar to Turla’s previously disclosed implant, TinyTurla, in coding style and functionality implementation.

**Feb. 20:**[**Astaroth, Mekotio & Ousaban abusing Google Cloud Run in LATAM-focused malware campaigns**](https://blog.talosintelligence.com/google-cloud-run-abuse/)

Since September 2023, we observed a significant increase in the volume of malicious emails leveraging the Google Cloud Run service to infect potential victims with banking trojans.

**Feb. 27:**[**TimbreStealer campaign targets Mexican users with financial lures**](https://blog.talosintelligence.com/timbrestealer-campaign-targets-mexican-users/)

Talos observed a phishing spam campaign targeting victims in Mexico, luring users to download a new obfuscated information stealer we’re calling TimbreStealer, which has been active since at least November 2023.

**March 5:**[**GhostSec’s joint ransomware operation and evolution of their arsenal**](https://blog.talosintelligence.com/ghostsec-ghostlocker2-ransomware/)

We observed a surge in GhostSec’s malicious activities this past year. GhostSec evolved with a new GhostLocker 2.0 ransomware, a Golang variant of the GhostLocker ransomware.

**April 9:**[**Starry Addax targets human rights defenders in North Africa with new malware**](https://blog.talosintelligence.com/starry-addax/)

We disclosed a new threat actor we deemed “Starry Addax” targeting mostly human rights activists, associated with the Sahrawi Arab Democratic Republic (SADR) cause with a novel mobile malware.

**April 16:**[**Large-scale brute-force activity targeting VPNs, SSH services with commonly used login credentials**](https://blog.talosintelligence.com/large-scale-brute-force-activity-targeting-vpns-ssh-services-with-commonly-used-login-credentials/)

Talos actively monitored a global increase in brute-force attacks against a variety of targets, including Virtual Private Network (VPN) services, web application authentication interfaces and SSH services since at least March 18, 2024.

**April 17:**[**OfflRouter virus causes Ukrainian users to upload confidential documents to VirusTotal**](https://blog.talosintelligence.com/offlrouter-virus-causes-upload-confidential-documents-to-virustotal/)

During a threat-hunting exercise, Talos discovered documents with potentially confidential information originating from Ukraine. The documents contained malicious VBA code, indicating they may be used as lures to infect organizations.

**April 23:**[**Suspected CoralRaider continues to expand victimology using three information stealers**](https://blog.talosintelligence.com/suspected-coralraider-continues-to-expand-victimology-using-three-information-stealers/)

Talos discovered a new PowerShell command-line argument embedded in the LNK file to bypass anti-virus products and download the final payload into the victims’ host.

**April 24:**[**ArcaneDoor — New espionage-focused campaign found targeting perimeter network devices**](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)

ArcaneDoor was a campaign that was the latest example of state-sponsored actors targeting perimeter network devices from multiple vendors. Coveted by these actors, perimeter network devices are the perfect intrusion point for espionage-focused campaigns.

**May 22:**[**From trust to trickery: Brand impersonation over the email attack vector**](https://blog.talosintelligence.com/from-trust-to-trickery-brand-impersonation/)

Cisco developed and released a new feature to detect brand impersonation in emails when adversaries pretend to be a legitimate corporation.

**May 31:**[**New banking trojan “CarnavalHeist” targets Brazil with overlay at...