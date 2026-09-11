---
title: We've got one word for it, and it's usually the wrong one
url: https://blog.talosintelligence.com/weve-got-one-word-for-it-and-its-usually-the-wrong-one/
source: Over Security
date: 2026-09-10
fetch_date: 2026-09-11T06:52:55.530044
---

# We've got one word for it, and it's usually the wrong one

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

# We've got one word for it, and it's usually the wrong one

By
[Joe Marshall](https://blog.talosintelligence.com/author/joe-marshall/)

Thursday, September 10, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Ask anybody in this industry what the work does to the health of the people who do it and you get one word back: burnout. It's a fine word, in and of itself. It’s easy to reach for, understandable to everyone… and it's the wrong one, most of the time.

So, story time. Last year I gave an interview with the amazing Hazel Burton about VPNFilter, and [my run-in with burnout](https://podcasts.apple.com/bo/podcast/you-cant-patch-burnout-when-cybersecurity-takes-a-toll/id1497572268?i=1000729675999). I was a manager during that time, and it took a toll on me and on the people around me, and when it was over I didn't have language for what had happened. Neither did my peers. Neither did my leadership. Nobody was withholding help from me… we just didn't have the words.

Enter this summer, and I was afforded a unique opportunity to mentor some MBA students on burnout in cybersecurity. I know a thing or two about it, so I leapt at a chance to share and help grow future leaders. But I decided I was going to do more than share and relieve my experiences in this industry – I wanted to give back to them and the security industry. So, I fell down a fascinating and revealing research hole and learned better words to describe my experiences over my career.

I spent my summer reviewing trauma case studies, clinical and academic literature on trauma in career fields like first responders, doctors, social workers, and the military. There are many decades of research focusing on trauma in those fields. Subsequently, my brain is packed full of better words! For example, **burnout** is exhaustion from chronic workload, and it eases when the load eases. We know this one well. **Secondary traumatic stress** is what absorbing somebody else's trauma does to you, and it looks like trauma. Think the CTI analyst exposed to horrible things on the dark web. **Vicarious trauma** is what years of other people's worst days do to how you see the world. It changes your beliefs, not your mood. Work in cybersecurity long enough, and it can pile up on your views. **Moral injury** is the damage from being made to act against your own values, or stopped from doing what you knew was right. This one can affect anyone who’s ever owned an outcome, but not the decision, and that’s common in this industry.

One word, four injuries, and four different fixes. All of them are present in the industry that is cybersecurity. The problem? We’re just a young industry. Compared to medical, helping professions, or social workers, we’re incredibly immature with understanding the consequences of the work and the toll it takes on us. Next week I’ll be revealing my research and a peer-deployable framework to help others process, cope, and respond in healthy ways to keep us all in a better mental space, and staying in this good fight of protecting others.

I'm still not good at this. I'm writing it all down because I was bad at it in a way that cost me something. There's more of this in my talk at [CYBR.SEC.CON](https://www.cybrseccon.com/) next week if you're in Houston.

Go ask somebody how they're doing and wait for the answer. Be present for them. It matters.

Take care of yourselves, and take care of each other.

## The one big thing

Cisco Talos is disclosing a [complex WebDAV infection chain](https://blog.talosintelligence.com/clearfake-webdav-infection-chain/) discovered after investigating an incident at a Ukrainian government organization. Attributed to a Russian threat actor tracked as UAT-10820, the campaign delivers the Amatera stealer alongside secondary payloads like ZigCryptoStealer and NetSupport Manager. Despite the high-profile initial victim, we assess with moderate confidence that this is an opportunistic, broad-based cryptocurrency and credential-stealing operation rather than a highly targeted attack.

### Why do I care?

Threat actors are getting really creative with their delivery mechanisms and evasion tactics. By abusing legitimate infrastructure like the BNB Smart Chain for bulletproof hosting and leveraging fake CAPTCHA prompts, attackers can easily bypass traditional web filters. Additionally, the secondary payloads pack a serious punch. The inclusion of a vulnerable driver to terminate EDR software and the deployment of unauthorized remote access tools give attackers deep, persistent control over infected systems.

### So now what?

Security teams should monitor for unusual WebDAV activity and the execution of disguised DLLs through "rundll32.exe" using suspicious ordinal calls. Make sure to educate your users on the dangers of copying and pasting commands from fake verification prompts. Since the Amatera payload often resides entirely in memory, defenders should also ensure their endpoint solutions are configured for robust memory scanning. Finally, you can find a comprehensive [list of indicators of compromise (IOCs)](https://blog.talosintelligence.com/clearfake-webdav-infection-chain/) in the full blog.

## Top security headlines of the week

**New Microsoft Defender 'ShieldCrash' zero-day grants SYSTEM access**
An anonymous security researcher known as Nightmare Eclipse has released a new Microsoft Defender zero-day exploit named "ShieldCrash" right after Microsoft rolled out its September 2026 Patch Tuesday security updates. ([Bleeping Computer](https://www.bleepingcomputer.com/news/security/new-microsoft-defender-shieldcrash-zero-day-grants-system-access/))

**North Korean hackers deploy new Linux espionage toolkit**
The stealthy toolkit em...