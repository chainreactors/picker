---
title: What happened in Vegas (that you actually want to know about)
url: https://blog.talosintelligence.com/what-happened-in-vegas-that-you-actually-want-to-know-about/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-15
fetch_date: 2025-10-07T00:49:14.524840
---

# What happened in Vegas (that you actually want to know about)

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

# What happened in Vegas (that you actually want to know about)

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, August 14, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Last week I flew 5,000 miles to Las Vegas for Black Hat USA. After navigating the casino carpet labyrinth and finding the only venue in Nevada that serves a proper English breakfast tea with milk (lifesaver), I’ve decided Black Hat feels exactly like trying to run in a dream — you’re always heading somewhere, never quickly, and the water costs $8.

I don’t mean to complain (although, as a Brit, I’m practically obligated to file a formal grievance about the weather, tea or queue length). In truth, it was a brilliant week, and I got to watch my fellow Talosians deliver some outstanding presentations and research.

Rather than recap everything we did (our [YouTube channel](https://www.youtube.com/%40CiscoTalosIntelligenceGroup) will have plenty of research highlights soon), here are three standouts:

* **Joe Marshall’s live incident-response exercise** – Joe ran *Backdoors & Breaches*, an interactive card game originally developed with NetHope and NGO-ISAC for humanitarian non-governmental organizations. At Black Hat, he adapted it for a lunch-and-learn with over 60 participants, guiding them through a simulated cybersecurity crisis. If you’re curious, you can [find the cards online here](https://github.com/ngoisac/play.backdoorsandbreaches.com/tree/main). With a websharing tool, you can stream it to any size audience and have people play along virtually. You can also read more about Joe’s experience developing the game, alongside a video walkthrough, in his [new blog post.](https://blog.talosintelligence.com/backdoors-breaches-how-talos-is-helping-humanitarian-aid-ngos-prepare-for-cyber-attacks/)
* **Amy Chang’s AI guardrail bypass research** – Amy’s booth talk revealed a novel way to break the guardrails of generative AI by tricking it into repeating human-written content verbatim, a technique called “*decomposition.”* Her work drew attention from media outlets including [TechRepublic](https://www.techrepublic.com/article/news-cisco-talos-generative-ai-llm-decomposition/), [SecurityWeek](https://www.securityweek.com/ai-guardrails-under-fire-ciscos-jailbreak-demo-exposes-ai-weak-points/) and [WebProNews](https://www.webpronews.com/cisco-talos-unveils-decomposition-technique-exposing-llm-training-data/).
* **Philippe Laulheret’s *ReVault* presentation** – Philippe, from our Vulnerability Research and Discovery team, revealed vulnerabilities in embedded security chips affecting millions of laptops, potentially allowing attackers to bypass Windows login or install persistent malware. A few days ago, he published a longer version of his investigation, so you can now [read the full technical deep dive](https://blog.talosintelligence.com/revault-when-your-soc-turns-against-you-2/) covering the research process and exploit breakdown.

We’ll have more to share soon, including a behind-the-scenes tour of the Black Hat Network Operations Center (NOC).

## The one big thing

Cisco Talos has identified a [widespread malvertising campaign](https://blog.talosintelligence.com/ps1bot-malvertising-campaign/) distributing a multi-stage malware framework Talos calls “PS1Bot,” which uses PowerShell and C# modules to steal sensitive information, log keystrokes, capture screenshots, and maintain persistent access on infected systems. PS1Bot employs in-memory execution and modular updates, targeting browser credentials, cryptocurrency wallets, and more, while minimizing its footprint to evade detection. The campaign has been active and rapidly evolving throughout 2025.

### Why do I care?

Casual browsing and downloading seemingly safe files can lead to infection, putting your personal data, passwords and financial info at risk — especially if you use cryptocurrency wallets or save passwords in browsers.

### So now what?

Be extra cautious when downloading files from search results or ads, keep your security software updated, and use dedicated password managers and security tools instead of storing sensitive info in browsers. Stay informed about evolving threats like PS1Bot, as attackers are constantly updating their tactics. Talos' [blog](https://blog.talosintelligence.com/ps1bot-malvertising-campaign/) also provides Snort SIDs and ClamAV detections.

## Top security headlines of the week

**Russian government hackers said to be behind US federal court filing system hack**
The Russian government is allegedly behind the data breach affecting the U.S. court filing system known as PACER, according to The New York Times. ([TechCrunch](https://techcrunch.com/2025/08/12/russian-government-hackers-said-to-be-behind-us-federal-court-filing-system-hack-report/))

**North Korean Kimsuky hackers exposed in alleged data breach**
The North Korean state-sponsored hacking group known as Kimsuky has reportedly suffered a data breach after two hackers stole the group's data and leaked it publicly online. ([Bleeping Computer](https://www.bleepingcomputer.com/news/security/north-korean-kimsuky-hackers-exposed-in-alleged-data-breach/?utm_source=tldrinfosec))

**Exclusive: Brosix and Chatox promised to keep your chats secured. They didn’t.**
A researcher contacted DataBreaches after finding an unsecured backup with 155.3 GB of unique compressed files. The researcher first logged the backup as exposed in late April. ([DataBreaches](https://databreaches.net/2025/08/05/exclusive-brosix-and-chatox-promised-to-keep-your-chats-secured-they-didnt/?utm_source=tldrinfosec))

**Netherlands: Citrix Netscaler flaw CVE-2025-6543 exploited to breach orgs**
The ...