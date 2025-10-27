---
title: What kind of summer has it been?
url: https://blog.talosintelligence.com/threat-source-newsletter-aug-28-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-30
fetch_date: 2025-10-06T18:06:21.507896
---

# What kind of summer has it been?

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

# What kind of summer has it been?

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, August 29, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Hello Talos followers. I’m back for my annual takeover of the Threat Source newsletter. First, an update on that killer sloth movie I was so excited about in August 2023. “Slotherhouse” debuted with an impressive $137,133 at the box office, with critics hailing its various set pieces such as “death by sleeping bag balcony trap” (read that again) and “a particularly gruesome use of hair straighteners.”

Onto less grisly fare. In the times when I used to frequent the site formerly known as Twitter, my favorite account to follow was [“Sorkinese”](http://x.com/sorkinese?lang=en) – a daily elocution safari with the wit and wisdom of Aaron Sorkin characters (mainly from The West Wing). Before Sorkinese’s well timed final tweet in July last year (“The internet people have gone crazy!”) one piece of Sorkin dialogue that I always enjoyed seeing on the feed was “What kind of day has it been?.” The Wingnuts amongst you will know that Sorkin used this as the title of key episodes in several of his shows. It’s meant to signal the end of something, and a reflection of what’s important.

As summer is drawing to a close and “sweater weather” begins again in earnest, I wanted to use this opportunity to reflect a little…what kind of summer has it been?

I live in the UK, so “wet” is the first word that comes to mind. But since I allegedly work in the security industry, and this is allegedly a security newsletter, I’ll steer things in that direction. In a "here's what I made earlier" moment (hello to the small percentage of Brits who will get that reference), this is a video which features Talos’ Head of Outreach Nick Biasini. We asked him to reflect on his two biggest areas of concern/importance in the threat landscape right now:

One more quick thing – it’s now a week until we launch our new documentary, “The Light We Keep: A Project PowerUp Story.” This video will explore first-hand accounts of the chaos and consequences of electronic warfare, and how we developed a solution to maintain reliable power in the event of GPS jamming on Ukraine's electrical grid.

Keep an eye on our social channels for its release and be sure to join us for the live online launch event which will include a Q & A with myself, Joe Marshall, Matt Watchinski, and Matt Olney.

[Register for the livestream on September 5th](https://www.linkedin.com/posts/cisco-talos-intelligence-group_mark-your-calendar-and-join-us-on-september-activity-7233986016137605120-jpgu?utm_source=share&utm_medium=member_desktop)

[Watch The Light We Keep trailer](https://www.youtube.com/watch?v=le3mPDSY4jc)

## The one big thing

 BlackByte is a ransomware-as-a-service (RaaS) group believed to be an offshoot of the infamous Conti ransomware group. They have continued to leverage tactics, techniques and procedures (TTPs) that have formed the foundation of its tradecraft since its inception, continuously iterating its use of vulnerable drivers to bypass security protections and deploying a self-propagating, wormable ransomware encryptor. In recent investigations, Cisco Talos Incident Response (Talos IR) has also observed BlackByte using techniques that depart from their established tradecraft. Members of the team, in collaboration with Talos Intelligence and Interdiction, [wrote a blog detailing their findings](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/).

### Why do I care?

 During an investigation of a recent BlackByte attack, Talos IR and Talos threat intelligence personnel noted close similarities between indicators of compromise (IOCs) discovered during the investigation and other events flagged in Talos’ global telemetry. Further investigation of these similarities provided additional insights into BlackByte’s current tradecraft and revealed that the group has been significantly more active than would appear from the number of victims published on its data leak site.

### So now what?

 Talos IR has provided a full set of recommendations to help defenders protect against RAAS groups such as BlackByte. Including how to detect lateral movement. You’ll find these recommendations [in the blog](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/), alongside the MITRE ATT&CK mapping of new TTPs, and Indicators of Compromise.

## Top security headlines of the week

* Hundreds of open-source large language model (LLM) builder servers and dozens of vector databases are leaking highly sensitive information to the open Web. [Dark Reading](https://www.darkreading.com/application-security/hundreds-of-llm-servers-expose-corporate-health-and-other-online-data)
* A recent Qilin ransomware attack targeted credentials that were stored in Google Chrome browsers on a portion of the impacted network’s endpoints. Researchers said the move is an “unusual tactic, and one that could be a bonus multiplier for the chaos already inherent in ransomware situations.” [Decipher](https://duo.com/decipher/qilin-ransomware-attack-targets-credentials-stored-in-chrome)
* Labor Day warning: Protect your date with these high-tech travel tips. Talos’ Nick Biasini recently gave advice on how to spot travel related phishing emails, and how to be aware of vulnerable Bluetooth connections and WIFI spots. Share with your friends and family! [ABC News](https://wjla.com/news/local/labor-day-protect-your-data-high-tech-travel-tips-personal-cellphone-information-account-airports-bluetooth-wifi-scam-emails-phone-bump-thr...