---
title: Inside the ransomware playbook: Analyzing attack chains and mapping common TTPs
url: https://blog.talosintelligence.com/common-ransomware-actor-ttps-playbooks/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-11
fetch_date: 2025-10-06T17:47:09.949427
---

# Inside the ransomware playbook: Analyzing attack chains and mapping common TTPs

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

![](/content/images/2024/07/talos-evergreen-ransomware-2000x1000.jpg)

# Inside the ransomware playbook: Analyzing attack chains and mapping common TTPs

By
[James Nutland](https://blog.talosintelligence.com/author/james/)

Wednesday, July 10, 2024 06:00

[On The Radar](/category/on-the-radar/)

Given the recent slate of massive ransomware attacks that have disrupted everything from [hospitals](https://www.bbc.com/news/articles/c288n8rkpvno) to [car dealerships](https://www.bloomberg.com/news/articles/2024-06-21/cdk-hackers-want-millions-in-ransom-to-end-car-dealership-outage), Cisco Talos wanted to take a renewed look at the top ransomware players to see where the current landscape stands.

Based on a comprehensive review of more than a dozen prominent ransomware groups, we identified several commonalities in tactics, techniques and procedures (TTPs), along with several notable differences and outliers.

Talos’ studies indicate that the most prolific ransomware actors prioritize gaining initial access to targeted networks, with valid accounts being the most common mechanism. Phishing for credentials often precedes these attacks, a trend observed across all incident response engagements, consistent with our [2023 Year in Review](https://blog.talosintelligence.com/cisco-talos-2023-year-in-review/) report. Over the past year, many groups have increasingly exploited known and zero-day vulnerabilities in public-facing applications, making this a prevalent initial access vector.

### Watch: Discussion of latest ransomware trends

The [AlphV/Blackcat](https://blog.talosintelligence.com/from-blackmatter-to-blackcat-analyzing/) and [Rhysida](https://blog.talosintelligence.com/rhysida-ransomware/) groups stood out with the broadest range of TTPs, demonstrating significant tactical diversity. Conversely, groups like [BlackBasta](https://blog.talosintelligence.com/decryptor-babuk-tortilla/), [LockBit](https://blog.talosintelligence.com/ransomware-affiliate-model/https%3A/blog.talosintelligence.com/ransomware-affiliate-model/) and Rhysida not only encrypted data and defaced victim systems to maximize impact. Distinctively, the [Clop ransomware group](https://blog.talosintelligence.com/active-exploitation-of-moveit/) primarily focused on extortion through data theft rather than typical encryption tactics and is one of the only actors to exploit zero-day vulnerabilities.

Our findings are based on a comprehensive analysis of 14 ransomware groups between 2023 and 2024. We selected the ransomware groups based on volume of attacks, impact on customers, and atypical threat actor behavior. Our research includes data from the actors’ public leak sites, Cisco Talos Incident Response (Talos IR), Talos internal tracking efforts and [open-source reporting](https://top-attack-techniques.mitre-engenuity.org/).

During this research period, Talos IR was actively engaged in responding to a considerable number of ransomware attacks heavily targeting the United States. These attacks spanned a broad spectrum of industries, notably impacting the manufacturing and information sectors, employing various techniques to encrypt data and demand ransoms, with their activities resulting in significant levels of financial losses and business disruption.

![](https://blog.talosintelligence.com/content/images/2024/07/ransomware1.jpg)

Over the past year, we have witnessed major shifts in the ransomware space with the emergence of multiple new ransomware groups, each exhibiting unique goals, operational structures and victimology. The diversification highlights a shift toward more boutique-targeted cybercriminal activities, as groups such as Hunters International, Cactus and Akira carve out specific niches, focusing on distinct operational goals and stylistic choices to differentiate themselves.

## An advanced arsenal: Notable TTPs employed by ransomware actors

Utilizing the MITRE ATT&CK framework as a baseline, we identified the primary TTPs utilized by major ransomware threat actors over the past three years which involved a detailed examination of each TTP, its execution methods, and relevant sub-techniques, that highlight unique TTPs not previously emphasized in MITRE’s top ATT&CK techniques.

Key findings indicate that many of the most prominent groups in the ransomware space prioritize establishing initial access and evading defenses in their attack chains, highlighting these phases as strategic focal points. Within the past year, many groups have exploited critical vulnerabilities in public-facing applications, becoming a prevalent attack vector, which we addressed later, indicating an increased need for appropriate security controls and patch management.

Echoing a trend identified in our [Talos Year in Review report](https://blog.talosintelligence.com/cisco-talos-2023-year-in-review/), our data supported the conclusion that ransomware actors continue to apply a significant focus to defense evasion tactics to increase dwell time in victim networks. Typical popular defense evasion methods include the disablement and modification of security software such as anti-virus programs, endpoint detection solutions, or security features in the operating system to prevent the detection of the ransomware payload. Adversaries will also often obfuscate malicious software by packing and compressing the code, eventually unpacking itself in memory when executed. They’ll also modify the system registry to disable security alerts, configure the software to execute at startup, or block certain recovery options for users.

![](https://blog.talosintelligence.com/content/images/2024/07/ransomware-04.jpg)

The most prevalent credential access technique Talos IR engagements have seen in 2023 and 2024 is the dumping of LSASS memory contents. Ransomware threat actors were seen often targeting th...