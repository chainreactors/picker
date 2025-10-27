---
title: Talos uncovers espionage campaigns targeting CIS countries, Turkey, and European institutions including Embassies and a critical EU Health care Agency
url: https://blog.talosintelligence.com/yorotrooper-espionage-campaign-cis-turkey-europe/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-15
fetch_date: 2025-10-04T09:41:19.738210
---

# Talos uncovers espionage campaigns targeting CIS countries, Turkey, and European institutions including Embassies and a critical EU Health care Agency

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

![](/content/images/2023/03/YoroTrooper_Header.jpg)

# Talos uncovers espionage campaigns targeting CIS countries, embassies and EU health care agency

By
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/)

Tuesday, March 14, 2023 07:00

[Threat Spotlight](/category/threat-spotlight/)
[SecureX](/category/securex-3/)
[Threats](/category/threats/)

* Cisco Talos has identified a new threat actor, which we are naming “YoroTrooper,” that has been running several successful espionage campaigns since at least June 2022.
* YoroTrooper’s main targets are government or energy organizations in Azerbaijan, Tajikistan, Kyrgyzstan and other Commonwealth of Independent States (CIS), based on our analysis. We also observed YoroTrooper compromise accounts from at least two international organizations: a critical European Union (EU) health care agency and the World Intellectual Property Organization (WIPO). Successful compromises also included Embassies of European countries including Azerbaijan and Turkmenistan. We assess the actor also likely targets other organizations across Europe and Turkish (Türkiye) government agencies.
* Information stolen from successful compromises include credentials from multiple applications, browser histories & cookies, system information and screenshots.
* YoroTrooper’s main tools include Python-based, custom-built and open-source information stealers, such as the [Stink stealer](https://github.com/FallenAstaroth/stink) wrapped into executables via the [Nuitka framework](https://github.com/Nuitka/Nuitka) and [PyInstaller](https://pyinstaller.org/en/stable/). For remote access, YoroTrooper has also deployed commodity malware, such as AveMaria/Warzone RAT, LodaRAT and Meterpreter.
* The infection chain consists of malicious shortcut files (LNKs) and optional decoy documents wrapped in malicious archives delivered to targets. The actor appears intent on exfiltrating documents and other information, likely for use in future operations.

---

# Introducing YoroTrooper

This new threat actor we are naming “YoroTrooper” has been targeting governments across Eastern Europe since at least June 2022, and Cisco Talos has found three different activity clusters with overlapping infrastructure that are all linked to the same threat actor. Cisco Talos does not have a full overview of this threat actor, as we were able to collect varying amounts of detail in each campaign. In some cases, for instance, we were able to fully profile a campaign, while in other cases, we only identified the infrastructure or compromised data.

![](https://blog.talosintelligence.com/content/images/2023/03/YoroTrooper_ThreatMatrix.jpg)

Our assessment is that the operators of this threat actor are Russian language speakers, but not necessarily living in Russia or Russian nationals since their victimology consists mostly of countries in the Commonwealth of Independent States (CIS). There are also snippets of Cyrillic in some of their implants, indicating that the actor is familiar with the language. Also, in some cases, the attackers are targeting Russian language endpoints (with Code Page 866), indicating a targeting of individuals speaking that specific language.

Espionage is the main motivation for this threat actor, according to the tactics, techniques and procedures (TTPs) we have analyzed. To trick their victims, the threat actor either registers malicious domains and then generates subdomains or registers typo-squatted domains similar to legitimate domains from CIS entities to host malicious artifacts. The table below contains some of the domains created by this actor.

| Malicious subdomain | Legitimate domain | Entity |
| --- | --- | --- |
| mail[.]mfa[.]gov[.]kg[.]openingfile[.]net | mfa[.]gov[.]kg | Kyrgyzstan’s Ministry of Foreign Affairs |
| akipress[.]news | akipress[.]com | AKI Press News Agency (Kyrgyzstan-based) |
| maileecommission[.]inro[.]link | commission[.]europa[.]eu | European Commission’s email |
| sts[.]mfa[.]gov[.]tr[.]mypolicy[.]top | mfa[.]gov[.]tr | Turkey’s Ministry of Foreign Affairs |
| industry[.]tj[.]mypolicy[.]top | industry[.]tj | Tajikistan’s Ministry of Industry and New Technologies |
| mail[.]mfa[.]az-link[.]email | mail[.]mfa[.]az | Azerbaijan’s Ministry of Foreign Affairs |
| belaes[.]by[.]authentication[.]becloud[.]cc | belaes[.]by | Belarusian Nuclear Power Plant (Astravets) |
| belstat[.]gov[.]by[.]attachment-posts[.]cc | belstat[.]gov[.]by | National Statistical Committee of Belarus |
| minsk[.]gov[.]by[.]attachment-posts[.]cc | minsk[.]gov[.]by | Official Website of the Government of Minsk (Belarus) |

The initial attack vectors are phishing emails with a file attached, which usually consists of an archive consisting of two files: a shortcut file and a decoy PDF file. The shortcut file is the initial trigger for the infection, while the PDF is the lure to make the infection look legitimate. The full details of the campaigns are detailed in the section below.

![](https://lh3.googleusercontent.com/utQKPqfYxa-ENrPuUOtEqkHcS7umfYN6iR8jqoxox1_CwI2HFzyo71ii3TwRnVyVYanV4NR2r7RX6Fw09U-Ui6jU_t3ay7s2ztlfPI-zmBrvZjXkpGxKaHas0UokC8hMggRHD0u4Ich7XFnl-O_NZMY)

Phishing email example.

Regarding YoroTrooper’s toolset, the actor uses several commodity remote access trojans (RAT) and credential stealers. For RATs, we have seen the usage of AveMaria/Warzone RAT, LodaRAT, and a custom-built implant based on Python. Credential stealers used by YoroTrooper are either custom scripts, which in some cases are based on the open-sourced [Lazagne](https://github.com/AlessandroZ/LaZagne/blob/b1289b8f69d41356d85403c6ecefc569588b3a68/Linux/lazagne/softwares/browsers/chromium_based.py) project or commodity stealers such as the Stink Stealer...