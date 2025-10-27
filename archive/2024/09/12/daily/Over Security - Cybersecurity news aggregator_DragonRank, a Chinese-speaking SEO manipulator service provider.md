---
title: DragonRank, a Chinese-speaking SEO manipulator service provider
url: https://blog.talosintelligence.com/dragon-rank-seo-poisoning/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-12
fetch_date: 2025-10-06T18:30:21.578307
---

# DragonRank, a Chinese-speaking SEO manipulator service provider

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

![](/content/images/2024/09/dragonrank-header.jpg)

# DragonRank, a Chinese-speaking SEO manipulator service provider

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Tuesday, September 10, 2024 00:00

[Threats](/category/threats/)
[Threat Spotlight](/category/threat-spotlight/)

# Key Takeaways

* Cisco Talos is disclosing a new threat called “DragonRank” that primarily targets countries in Asia and a few in Europe, operating PlugX and BadIIS for search engine optimization (SEO) rank manipulation.
* DragonRank exploits targets’ web application services to deploy a web shell and utilizes it to collect system information and launch malware such as PlugX and BadIIS, running various credential-harvesting utilities.
* Their PlugX not only used familiar sideloading techniques, but the Windows Structured Exception Handling (SEH) mechanism ensures that the legitimate file can load the PlugX without raising suspicion.
* We have confirmed more than 35 IIS servers had been compromised and deployed the BadIIS malware across a diverse array of geographic regions, including Thailand, India, Korea, Belgium, Netherlands and China in this campaign.
* Talos also discovered DragonRank’s commercial website, business model and instant message accounts. We used this information to assess with medium to high confidence the DragonRank hacking group is operated by a Simplified Chinese-speaking actor.

# Victimology: Countries, verticals and what is happening

Talos has recently uncovered a cluster of activity we’re calling “DragonRank” distributed across a diverse array of geographic regions, including Thailand, India, Korea, Belgium, Netherlands and China. They have cast a wide net in terms of industries, encompassing sectors such as jewelry, media, research services, healthcare, video and television production, manufacturing, transportation, religious and spiritual organizations, IT services, international affairs, agriculture, sports, and even niche markets like feng shui. This broad spectrum of targets indicates a wide-reaching and non-targeted approach to their operations.

![](https://blog.talosintelligence.com/content/images/2024/09/data-src-image-be2c1313-8249-4890-b14c-d6d9b5905dc5.jpeg)

These activities employ tools and tactics, techniques, and procedures (TTPs) typically linked to Simplified Chinese-speaking hacking groups. The hacking group’s primary goal is to compromise Windows Internet Information Services (IIS) servers hosting corporate websites, with the intention of implanting the BadIIS malware. BadIIS is a malware used to manipulate search engine crawlers and disrupt the SEO of the affected sites. With those compromised IIS servers, DragonRank can distribute the scam website to unsuspecting users.

The threat actor engages in SEO manipulation by altering or exploiting search engine algorithms to improve a website's ranking in search results. They conduct these attacks to drive traffic to malicious sites, increase the visibility of fraudulent content, or disrupt competitors by artificially inflating or deflating rankings. These attacks can harm a company's online presence, lead to financial losses, and damage its reputation by associating the brand with deceptive or harmful practices.

The actor takes the compromised websites and promotes them, effectively turning these sites into platforms for scam operations. The scam websites we observed in this campaign utilize keywords related to porn and sex, and the configuration data of the keywords from the command and control (C2) servers have been translated to multiple languages. Talos has confirmed more than 35 IIS servers had been compromised and acted as a conduit for this attack. The following example pictures show the configured data from C2 server and infected scam websites we observed from search engine results.

![](https://blog.talosintelligence.com/content/images/2024/09/data-src-image-2dfa4092-722f-45ae-89a4-722fa124b2d9.png)![](https://blog.talosintelligence.com/content/images/2024/09/data-src-image-bcb7f3ec-bc16-4e4b-958a-c8496f84a8e5.png)![](https://blog.talosintelligence.com/content/images/2024/09/data-src-image-819085d0-a11c-4f7d-871e-cf176ef0ee6e.png)

# Who they are

The findings revealed that DragonRank is actively engaging in black hat SEO practices to promote their business online, thereby boosting their clients' internet visibility by unethical means. However, we discovered that the DragonRank hacking group operates differently from traditional black hat SEO cybercrime groups. These groups usually compromise as many website servers as possible to manipulate search engine traffic, but DragonRank emphasizes lateral movement and privilege escalation. Their objective is to infiltrate additional servers within the target's network and maintain control over them. We assess that they are relatively new to the black hat SEO industry, and they functioned more as a hacking group specializing in targeted attacks or penetration testing in the past.

Based on the objective DragonRank and the C2 servers extracted from their PlugX malware, we utilized relevant keywords to conduct a search engine investigation. For instance, searching "tttseo.com" on Google showed numerous instances of DragonRank’s advertisements, which had been inserted across various legitimate websites. The content of these ads consistently centered on methods for black hat SEO services. By altering our IP address to appear as if we were accessing the internet from another country (we used Japan as an example), we conducted keyword searches which confirmed that DragonRank has disseminated their targeted keywords globally. Additionally, it has come to our attention that the actor is offering services for bulk posting on social media platforms.

![](https://blog.talosintelligence.com/content/images/2024/...