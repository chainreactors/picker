---
title: Find the helpers
url: https://blog.talosintelligence.com/find-the-helpers/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-17
fetch_date: 2025-10-06T20:12:13.022189
---

# Find the helpers

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

# Find the helpers

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Thursday, January 16, 2025 14:15

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

“When I was a boy and I would see scary things in the news, my mother would say to me, ‘Look for the helpers. You will always find people who are helping.’”

 ― Fred Rogers

There’s no world where following Mr. Roger’s advice is wrong. With the wildfires raging in Greater Los Angeles now more than ever I am very aware of the need to look for the helpers. I get it, I see the news and it’s overwhelming and terrifying. So Gentle Reader I’m asking that instead of just finding the helpers – be the helper.

I’d like everyone to take a moment and think about what you can do to be a helper – not just with the catastrophic fires and the incredible destruction but in your own world. In your home life and in your work life. Nothing is more intrinsic to information security than the sharing of knowledge and information. It’s how we all got the roles that we are in now. The older I get the more joy I find in sharing anything and everything that I know. I’m proud to be a mentor in Cisco’s [Women in Cybersecurity](https://blogs.cisco.com/tag/women-in-cybersecurity) and outside of work I’ve started volunteering to teach English as a second language – and cannot tell you how rewarding both are. There are so many incredible non-profits that you can give your time and money. Do both. There are so many infosec groups that are in need of your time, your invaluable experience, and mentorship. Be the helper. Find a local group, find an internal team within your organization, and if you can’t find one – create one.

Be the helper.

Let’s use this terrible event as a driver to push us all to do more to be the helpers. After all, what would Mr. Rogers do?

## The one big thing

Cisco Talos discovered forty-four vulnerabilities, and sixty-three CVEs were discovered across ten .cgi and three .sh files, as well as the static login page, of the Wavlink AC3000 wireless router web application.

 The Wavlink AC3000 wireless router is one of the most popular gigabit routers in the US, in part due to both its potential speed capabilities and low price point. Talos is releasing these advisories in accordance with Cisco’s third-party vulnerability

### Why do I care?

An attacker can send a specially crafted set of network packets over WAN to gain root access to the router via the wcrtrl service and static login credentials. With the [ongoing state-sponsored attacks on infrastructure](https://blog.talosintelligence.com/state-sponsored-campaigns-target-global-network-infrastructure/) this is critical to a secure environment.

### So now what?

Cisco Talos has released several Snort rules and ClamAV signatures to detect and defend against the exploitation of these vulnerabilities.

# Top security headlines of the week

Hackers are exploiting a new Fortinet firewall bug to breach company networks. ([TechCrunch](https://techcrunch.com/2025/01/14/hackers-are-exploiting-a-new-fortinet-firewall-bug-to-breach-company-networks/))

CISA is urging federal agencies to patch a command injection flaw tracked as CVE-2024-12686, otherwise known as BT24-11, and has added it to the Known Exploited Vulnerabilities (KEV) Catalog. The medium-severity security bug was found as a part of BeyondTrust's Remote Support SaaS Service security investigation, which was launched after a major data breach at the US Treasury Department. ([DarkReading](https://www.darkreading.com/vulnerabilities-threats/cisa-warns-of-second-vuln-found-in-beyondtrust-breach-investigation))

Microsoft rings in 2025 with record security update. Microsoft has issued patches for an unprecedented 159 CVEs, including eight zero-days, three of which attackers are already exploiting. ([DarkReading](https://www.darkreading.com/application-security/microsoft-january-2025-record-security-update))

# Can’t get enough Talos?

* [Slew of Wavlink Vulnerabilities](https://blog.talosintelligence.com/slew-of-wavlink-vulnerabilities/)
* [Evolution and Abuse of Proxy Networks](https://blog.talosintelligence.com/the-evolution-and-abuse-of-proxy-networks/)
* [Patch Tuesday was a big one](https://blog.talosintelligence.com/january-patch-tuesday-release/)

Our latest Talos Takes podcast sees Hazel sits down with Vanja Svajcer to discuss new research on vulnerable drivers.

## Upcoming events where you can find Talos

[Cisco Live EMEA](https://www.ciscolive.com/emea.html) (February 9-14, 2025)
Amsterdam, Netherlands

## Most prevalent malware files from Talos telemetry over the past week

 SHA 256:7b3ec2365a64d9a9b2452c22e82e6d6ce2bb6dbc06c6720951c9570a5cd46fe5

MD5: ff1b6bb151cf9f671c929a4cbdb64d86

VirusTotal : [https://www.virustotal.com/gui/file/7b3ec2365a64d9a9b2452c22e82e6d6ce2bb6dbc06c6720951c9570a5cd46fe5](https://www.virustotal.com/gui/file/7b3ec2365a64d9a9b2452c22e82e6d6ce2bb6dbc06c6720951c9570a5cd46fe5%C2%A0)

Typical Filename: endpoint.query

Claimed Product: Endpoint-Collector

Detection Name: W32.File.MalParent

SHA 256:9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507

MD5: 2915b3f8b703eb744fc54c81f4a9c67f

 VirusTotal: [https://www.virustotal.com/gui/file/9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507](https://www.virustotal.com/gui/file/9f1f11a708d393e0a4109ae189bc64f1f3e312653dcf317a2bd406f18ffcc507%C2%A0)

Typical Filename: VID001.exe

Detection Name: Simple\_Custom\_Detection

SHA 256: 47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca

MD5: 71fea034b422e4a17ebb06022532fdde

VirusTotal: [https://www.virustotal.com/gui/file/47ecaab5cd6b26fe18d9759a9392bce81ba379817c53a3a468fe9060a076f8ca]...