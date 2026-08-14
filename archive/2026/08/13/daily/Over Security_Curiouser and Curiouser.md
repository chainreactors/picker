---
title: Curiouser and Curiouser
url: https://blog.talosintelligence.com/curiouser-and-curiouser/
source: Over Security
date: 2026-08-13
fetch_date: 2026-08-14T04:00:34.172931
---

# Curiouser and Curiouser

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

# Curiouser and Curiouser

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Thursday, August 13, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

> *“Experiment is the mother of knowledge.” ― Madeleine L'Engle, A Wrinkle in Time*

> *“Don't slide down the rabbit hole. The way down is a breeze, but climbing back's a battle.” ― Kate Morton, The Clockmaker's Daughter*

Hacker Summer Camp has come and gone, which means it’s time for you to start planning next year’s trip. I’m surely going to recap Camp Season, right? Nope.

One of the things that I’ve really enjoyed lately is a segment on the [Beers with Talos podcast](https://beerswithtalos.talosintelligence.com/2033817/episodes/19599147-i-pay-you-200-a-month-when-threat-actors-argue-with-ai) that we call “Make Hazel a Hacker.” If you haven’t listened to it, this is a perfect time to start. Each episode we take a few minutes and pose a security question, term, or concept to Hazel and force her to come up with an idea or explanation on the spot. There are no parameters, so she’s faced with the entirety of information security — past, present, and future. I know, it’s insane. The craziest part is that (I think) Hazel came up with this idea and still volunteered to put herself in the line of fire.

As we put Hazel’s feet to the fire, one of my favorite things happens: The rest of us listen in and offer our thoughts during her brainstorming process. Invariably, we’ve got three very different answers, ideas, hints, or directions for her. It’s surely maddening for Hazel, but to me, the best part of the discussion that inevitably follows is that although they’re all different, they’re all correct.

For example, this past episode I asked her about a behavioral indicator (regarding “wallpaper.bmp”) that seems benign on its own, but can be interesting to use as a pivot for a threat hunt. We had various interesting angles to consider, backed by years of knowledge and experience. It gave us a good conversation, and that was a .bmp!

One of the most nebulous things to learn in this field is that multiple things can be both different and correct. When you are making your decisions this week — whether it’s deciding on a new pivot in your hunting, what devices to prioritize in your patching and updating, or which books or online training to focus on — take a quick second and get a second, third, and fourth opinion. Then try something that’s outside of your normal wheelhouse but sounds good when it’s proposed.

None of this is a solo sport. It’s a team game and the best plays come from a mix of perspectives, experiences, and mistakes. The “right” answer can wear many faces, and your ability to hold different truths will lead you to undiscovered territory, the rabbit hole where anomaly lives and breathes. So... welcome back from Vegas. Now go down a rabbit hole on a path you wouldn’t normally take because one of your friends (Joe) or your mortal enemy (Dave) told you that it would work.

> *“She'd been to Narnia, Wonderland, Hogwarts, Dictionopolis. She had tessered, fallen through the rabbit hole, crossed the ice bridge into the unknown world beyond.” ― Anne Ursu, Breadcrumbs*

## The one big thing

Cisco Talos [recently discovered "JWR,"](https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework) a previously undocumented, real-time phishing framework and likely variant of "The Outsider" phishing-as-a-service platform. JWR uses an open WebSocket connection that allows attackers to monitor keystrokes live and dynamically steer victims through fake checkout and login flows. Currently deployed via SMS lures impersonating regional toll and postal authorities, JWR enables operators to steal payment data, 2FA codes, identity documents, and device fingerprints.

### Why do I care?

Because JWR is operator-driven in real time, attackers can actively bypass multi-factor authentication (MFA) by prompting victims for 2FA codes exactly when needed. The sheer volume of collected data gives threat actors a comprehensive identity profile primed for extensive follow-on fraud and network compromise. Furthermore, JWR's seamless integration with legitimate e-commerce platforms like Shopify makes these lures incredibly convincing to the untrained eye.

### So now what?

Prioritize user education around SMS-based phishing (smishing), specifically regarding unsolicited delivery or toll fee messages. Monitor for unusual authentication attempts, as stolen device fingerprints and session tokens can bypass conditional access policies. Where possible, implement phishing-resistant MFA methods like FIDO2 hardware keys. For a complete list of indicators of compromise (IOCs) and coverage updates, [read the full blog.](https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework)

## Top security headlines of the week

**Ransomware hits Colombian Justice Ministry days before presidential transition**
The attack, which disrupted some services around illicit-drug monitoring and legal processes, came a day after Colombia's national CERT published threat intelligence warning that ransomware groups had increased their focus on the country. ([Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/ransomware-hits-colombian-justice-ministry-presidential-transition))

**FBI investigating North Korean remote IT staffer working for U.S. agency**
It’s unclear what agency was impacted, how long the intrusion lasted, and whether any sensitive data was stolen. Experts say it’s highly likely the staffer was a remote IT employee doing contract work on behalf of an agency. ([Federal News Network](https://federalnewsnetwork.com/technology-main/2026/08/fbi-investigat...