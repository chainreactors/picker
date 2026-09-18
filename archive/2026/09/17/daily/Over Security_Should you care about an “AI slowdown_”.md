---
title: Should you care about an “AI slowdown?”
url: https://blog.talosintelligence.com/should-you-care-about-an-ai-slowdown/
source: Over Security
date: 2026-09-17
fetch_date: 2026-09-18T06:53:11.827425
---

# Should you care about an “AI slowdown?”

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

# Should you care about an “AI slowdown?”

By
[David J. Bianco](https://blog.talosintelligence.com/author/david-j-bianco/)

Thursday, September 17, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

There’s been a lot of talk recently about [slowing down the pace of AI development](https://darioamodei.com/post/we-must-pace-the-frontier). And yes, there are legitimate moral, ethical, geopolitical, and safety concerns with the use of AI. It’s not clear yet whether an AI slowdown *could* happen, let alone whether it *should* ([hat tip to Dr. Ian Malcolm](https://www.youtube.com/watch?v=F_7RvW-avZ8&t=115s)). I admit, I’m not really qualified to opine on the impacts unrestricted AI might have on bioterrorism, the balance of international power, or even our chances of being eaten by dinosaurs. What I *can* tell you, though, is that any sort of “AI slowdown” is not likely to have much of an impact on cybersecurity.

There are a few reasons to think this. The most obvious one is that **models are already really good**. We’re at the point where the newest models bring only incremental improvements in cybersecurity capabilities. Arguably, they’ve been getting better so fast that our ability to use them effectively for defensive tasks hasn’t kept up. On the offensive side, practically every recent model is already able to mine decades of tech debt to uncover an uncomfortable number of vulnerabilities. Instead of chasing model improvements, our best strategy might be to improve our agentic harnesses and frameworks, essentially giving us better capabilities with our existing models.

Maybe even more importantly, **many of us are still not** [**eating our cyber-vegetables**](https://www.youtube.com/watch?v=4xasOElEVd4&t=270s). I get it: AI is hot. It’s sexy. It brings the money and the board’s attention. But no matter how great your AI is, if it’s sitting on the typical two-and-a-half-legged stool that is most IT environments, you’re still going to have compromises and breaches no matter how much AI you throw at it. We’ve known for a long time now that good security depends on things like asset and role inventories, identity management, least privilege, and segmented networks. They’re not as shiny as AI, but they’re more impactful in terms of making it harder for threats both human and agentic to successfully carry out attacks. This is not to say that you shouldn’t be looking at AI until you’ve solved all your other security problems; just don’t look *only* to AI.

Regardless of whether we slow the pace of AI development or not, we still have plenty of places to make significant security improvements using the models we already have access to. By making better use of what we already have and by investing in well-known security fundamentals, we can come out ahead no matter whether AI development accelerates, slows down, or is trapped in a kitchen with a pack of hungry velociraptors.

*P.S. I’ve got some speaking engagements coming up soon (see below). If you see me, don’t be shy about asking for a Pyramid of Pain sticker or button!*

### The one big thing

Cisco Talos is sharing [new insights](https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026) into Japan's ransomware landscape, where incidents rose nearly 5 percent in the first half of 2026. This increase is driven by two prominent actors: "The Gentlemen," a rapidly expanding ransomware-as-a-service group, and "Qilin," which is leveraging generative AI to streamline its attacks. Both groups are aggressively targeting small- and medium-sized enterprises with double-extortion tactics.

### Why do I care?

Adversaries are working smarter, not harder. Qilin uses large language models to generate destructive scripts, accelerating their attack speed and lowering the barrier to entry. Meanwhile, The Gentlemen relies on legitimate red-teaming frameworks like AdaptixC2 to blend in, making lateral movement difficult to detect. This combination of AI-driven efficiency and stealthy techniques puts organizations at risk of data theft and operational disruption.

### So now what?

Strictly manage internet-accessible devices and lock down credentials. Start by auditing VPNs, disabling unused features, and enforcing multi-factor authentication (MFA) across all administrative and third-party accounts. Ensure you have robust endpoint detection to monitor for suspicious remote access or attempts to disable backups. Finally, update your defenses using the Snort rules [provided in the full blog](https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026) to help detect and block this activity.

## Top security headlines of the week

**Indonesia hit by Android banking app-cloning campaign**
Indonesia has emerged as an early testing ground for a new Android banking malware technique that uses Google's Work Profile feature to help fraudsters evade banking security controls. ([Dark Reading](https://www.darkreading.com/mobile-security/indonesia-android-banking-app-cloning-campaign))

**Apple patches 200 vulnerabilities with new iOS 27, macOS Golden Gate 27 releases**
Approximately 100 of the resolved security defects affect both the mobile and desktop operating systems. The fixes target more than 90 platform components, including AppleKeyStore, Authentication Services, Foundation, Safe Browsing, Sandbox, Security, TCC, and WebKit. ([SecurityWeek](https://www.securityweek.com/apple-patches-200-vulnerabilities-with-new-ios-27-macos-golden-gate-27-releases/))

**ClickFix attacks are tricking Mac and Windows users into hacking themselves**
Hackers posting fake ads on Reddit, linking to a page that looks like HBO Max but contains a ClickFix lure...