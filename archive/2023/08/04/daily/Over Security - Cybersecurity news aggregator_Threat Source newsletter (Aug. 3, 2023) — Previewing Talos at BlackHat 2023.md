---
title: Threat Source newsletter (Aug. 3, 2023) — Previewing Talos at BlackHat 2023
url: https://blog.talosintelligence.com/threat-source-newsletter-aug-3-2023/
source: Over Security - Cybersecurity news aggregator
date: 2023-08-04
fetch_date: 2025-10-04T12:03:21.966891
---

# Threat Source newsletter (Aug. 3, 2023) — Previewing Talos at BlackHat 2023

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

# Previewing Talos at BlackHat 2023

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, August 3, 2023 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

The time has come once again for all of us (well, not me specifically but lots of other Talos people) to descend on Las Vegas for Hacker Summer Camp. Cisco Talos will be well-represented at BlackHat and DEF CON over the course of the next few weeks with a slew of presentations, demos and appearances to speak to the security community.

As always, we’ll be at the Cisco booth at BlackHat, located just north of the main entrance (it’s #1532 if you’re searching!). If you need help finding us, [download the BlackHat app](https://page.swapcard.com/app/black-hat-events/) to see a map of the entire conference. Talos researchers will be at the booth throughout the conference to give lightning talks on a wide range of topics — everything from machine learning to the basics of spotting phishing emails. New talks will take place every other half hour starting at 10 a.m. local time on Wednesday.

We’ll also have a presence at the BlackHat Career Zone — diagonal from Startup City on the show floor at Kiosk #CZ2 — throughout the conference, where you can talk to us about current job openings, ask for advice on career advancement or just talk about future opportunities for how you could become part of our team. On Thursday, Aug. 10, from 10 a.m. - noon local time, we’ll have Talos hiring managers at the Cisco booth to also talk about potential job opportunities.

The highlight of BlackHat is our [sponsored talk on Aug. 9 at 11:30 a.m. local time](https://www.blackhat.com/us-23/sponsored-sessions/schedule/index.html#the-practitioners-advantage-why-extended-detection-and-response-xdr-is-the-right-approach-right-now-34947) in Business Hall Theater A. Nick Biasini, our head of Outreach, joins Cisco’s Vice President of Product Management for Threat, Detection and Response A.J. Shipley to talk about Cisco XDR. Learn how the newest offering from Cisco Secure combines telemetry from multiple sources and applies analytics to uncover malicious activities and attacker tactics, techniques and procedures (TTPs).

The [following week at DEF CON](https://defcon.org/html/defcon-31/dc-31-index.html), Vitor Ventura and Asheer Malhotra will be at the Crypto and Privacy Village, delivering a talk on “Mercenary” threat actors and the spyware they create on the Saturday of the conference at 6 p.m local time. Asheer and Vitor have [written extensively](https://blog.talosintelligence.com/mercenary-intellexa-predator/) about this topic and why the malware they’re creating and selling is [potentially more dangerous](https://talostakes.talosintelligence.com/2018149/13219101) than “traditional” spyware.

Keep an [eye out on our Twitter](https://twitter.com/TalosSecurity) (or X, whatever we’re calling it) for more information about a live Beers with Talos podcast recording and other opportunities to ask our researchers questions.

If you're flying out to Vegas for either conference, make sure to [bookmark our Half-Year in Review to read during your travels](https://blog.talosintelligence.com/half-year-in-review-2023/). This is a great overview of the top threats of 2023 so far this year and looks at where the cybersecurity landscape might head next.

## The one big thing

Since the discovery of the high-profile VPNFilter malware in 2018, our vulnerability research team has had a renewed focus on small and home office (SOHO) wireless routers. These are devices that are present in almost every house and business in the modern world because they are necessary to deliver the internet to multiple devices everyone possesses and relies on today. Over the past four-plus years, Talos worked with multiple vendors to [disclose and patch nearly 290 CVEs](https://blog.talosintelligence.com/router-researcher-vulnerability-spotlight-23/) in a wide range of products and libraries these routers use. This week, [we released a full rundown](https://blog.talosintelligence.com/router-researcher-vulnerability-spotlight-23/) of all these vulnerabilities and what the major takeaways are for users and the manufacturers behind these products.

### Why do I care?

Given the privileged position these devices occupy on the networks they serve, they are prime targets for attackers, so their security posture is of paramount importance. However, they are also often deployed without a sophisticated security team in place to mitigate vulnerabilities. These routers are usually connected to the internet directly and all local network traffic passes through these devices. Since VPNFilter, Talos has investigated 13 SOHO and industrial routers from various vendors. Our reports to these vendors resulted in appropriate Snort network intrusion detection coverage and several security fixes from each vendor. These fixes help customers who deploy Cisco Secure solutions and improve the security posture of anyone using these devices once the vulnerabilities are patched.

### So now what?

The most important security step a user of these devices can take is to assess each service present on the device. Verify that each service running is required for the day-to-day operation of each device and disable all extraneous services. Services that cannot be disabled should be restricted to absolute minimal access or completely blocked using alternative methods, such as firewall rules to block traffic. During the acquisition process, if possible, basic research should be done to ensure the devices have sane, secure defaults enabled, such as the use of encrypted protocols for remote access and administration, if applicable.

## Top s...