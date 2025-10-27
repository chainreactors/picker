---
title: A week with a "smart" car
url: https://blog.talosintelligence.com/a-week-with-a-smart-car/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-19
fetch_date: 2025-10-06T22:55:01.829912
---

# A week with a "smart" car

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

# A week with a "smart" car

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Wednesday, June 18, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

June 9 was Whit Monday — a bank holiday here in Germany — so I decided to take the whole week off. It turned out to be the perfect opportunity to try out a brand new car. Little did I know, I was about to get a crash course in modern vehicle technology (and a few unexpected life lessons).

There’s an [EU regulation](https://eur-lex.europa.eu/eli/reg/2019/2144/oj) that requires new cars to come equipped with “Advanced Vehicle Systems,” which include features like driver drowsiness and attention warnings, lane-keeping systems and intelligent speed assistance. I hadn’t swapped cars in over a decade, so I was blissfully unaware of just how intrusive these systems could be.

While I generally appreciate technology that makes our life safer, these features gave me a tough time. The car seemed to beep at me constantly, so much so that the beeping itself became a distraction. Instead of focusing on the road, I found myself trying to decipher what each alert meant. After a few kilometers, I had to pull over and consult the manual just to figure out how to disable these “helpful” assistants.

Problem solved? Not quite. Every time I turned off and restarted the car, the systems re-enabled themselves. Disabling the lane-keeping assistant was just a button press, but turning off the “intelligent” speed assistant required a convoluted sequence: six menu clicks, a long press then a short click. I had to dig out the manual every time.

You might think I’m just cutting corners, or that I should pay better attention to speed limits. But here’s the thing: Technology fails, and these systems are no exception. Sometimes the cameras miss speed signs, or worse, pick up the wrong ones. I’ve read about people putting stickers on their windshields to block the camera, only to discover the system then falls back to GPS data, which can be outdated or just plain wrong. On one occasion, it thought a car was on a 50 km/h road when the person was actually on the [Autobahn](https://edition.cnn.com/travel/article/autobahn-germany-history) directly next and parallel to the road, which famously has no speed limit.

Some drivers try to muffle the alerts by gluing the speaker, but in modern cars, the system also lowers the radio volume to make sure you hear the alarm. Pulling the fuse would disable the emergency brake, too — not something I’m willing to risk, regardless of how insurance would feel about it.

I ended up learning two important lessons that week. The first was technical: I dove into the world of Controller Area Network (CAN) bus wiring, protocols, network gateways and tools like SavvyCAN to understand how these systems work... and maybe how to disable a few, purely for educational purposes.

The second lesson hit me later, and it was more personal. In my job, I often preach about deploying multi-factor authentication (MFA) everywhere. My focus has always been on keeping out the bad guys, not on the user experience. I never understood why anyone would use apps to automatically accept authentication pushes — it seemed crazy to me. But after a a few days with the car, I finally saw things from the user’s perspective. Security tools can’t just be effective; they also have to be easy to use. Reducing friction, like using single sign-on or minimizing unnecessary clicks, matters just as much. Users also need to understand why these barriers are in place.

Tomorrow is another holiday. Maybe I’ll spend it exploring [Kali Linux 2025.2](https://www.kali.org/blog/kali-linux-2025-2-release/) and the latest CARsenal tools (formerly CAN Arsenal). Who knows? I might just tap a wire or two — for educational purposes only, of course.

## The one big thing

[Cisco Talos has discovered](https://blog.talosintelligence.com/python-version-of-golangghost-rat) that the North Korean-aligned threat actor Famous Chollima has been actively targeting cryptocurrency and blockchain professionals (primarily in India) through sophisticated phishing campaigns. Previously known for using the GolangGhost trojan, they've now introduced a Python-based variant called PylangGhost, which retains the same capabilities. Recent campaigns have targeted Windows users with the Python version, while MacOS users are still being hit with the Golang-based variant.

### Why do I care?

Even if you're not in the cryptocurrency or blockchain space, this campaign highlights how threat actors are constantly evolving their tools. It's a reminder that no matter how niche or localized an attack might seem, the techniques could easily be adapted to broader campaigns. Plus, if attackers succeed in these targeted efforts, stolen credentials could ripple across networks and platforms globally.

### So now what?

Take this as your cue to double-check your defenses. Ensure your organization's security tools can detect Python and Golang-based malware, and educate your teams on recognizing phishing attempts, especially fake job offers. Stay proactive by monitoring emerging threats like PylangGhost, because even if you're not the target today, tomorrow isn’t a guarantee.

## Top security headlines of the week

**AI Scraping Bots Are Breaking Open Libraries, Archives, and Museums**
AI bots that scrape the internet for training data are hammering the servers of libraries, archives, museums and galleries, and are in some cases knocking their collections offline. ([404 Media](https://www.404media.co/ai-scraping-bots-are-breaking-open-libraries-archives-and-museums/?ref=daily-stories-newsletter))

**Paraguay Suffered Data Breach: 7.4 ...