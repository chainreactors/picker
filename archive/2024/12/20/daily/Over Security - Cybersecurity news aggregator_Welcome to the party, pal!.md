---
title: Welcome to the party, pal!
url: https://blog.talosintelligence.com/welcome-to-the-party-pal-2/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-20
fetch_date: 2025-10-06T19:39:53.265753
---

# Welcome to the party, pal!

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

# Welcome to the party, pal!

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, December 19, 2024 14:02

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to the final Threat Source newsletter of 2024.

Watching "Die Hard" during the Christmas season has become a widely recognized tradition for many, despite ongoing debates about its classification as a Christmas movie. I know it isn't everyone's cup of tea. Whether you like the movie or not, let me share a story about what didn't quite go as planned in my family last year.

When  some celebrities had their social media accounts compromised, I saw it as the perfect opportunity to introduce my family to the world of multi-factor authentication (MFA) for their online accounts. Our home IT setup is diverse— With Linux, Macs, Windows; Androids, iOS, we needed something cross-platform. Also, we needed a user-friendly solution as we have both standard users and IT experts (never underestimate your users). From my professional standpoint, I decided to go “all in” with hardware tokens - they work cross platform and "survive" one or the other OS installs from scratch. Providing two for each person was mandatory in case one got lost, which had happened to me already. So it wasn't a cheap exercise. In my defense, this was before the side-channel attack [EUCLEAK](https://ninjalab.io/EUCLEAK/) was discovered, which has since [expanded](https://www.heise.de/en/news/EUCLEAK-More-products-vulnerable-to-cloning-attack-10079927.html) to affect more products as noted in the first release.

In the spirit of John McClane : “Now I know what a TV dinner feels like.”

The kids found the gift "boring" and almost a year later, the adoption rate is still only 30%. Fortunately, my wife had the foresight to prepare real presents for the family, saving Christmas Eve from being a "bad guys win" scenario. (Only ~~John~~ Thor can drive somebody that crazy.)

I share this anecdote not to discourage you, but to help you avoid making the same mistake and risking your celebrations. Unless everyone gathered around the Christmas tree is an infosec professional, it might not be the time to go "Yippee-ki-yay Mr Falcon" with tech gifts.

However, spending time with loved ones is a great opportunity to discuss the trends and importance of cybersecurity. We've been highlighting compromised credentials for a long time, as seen in our previous posts [[here]](https://blog.talosintelligence.com/talos-ir-quarterly-report-q4-2023/), [[here]](https://blog.talosintelligence.com/talos-ir-quarterly-trends-q1-2024/), [[here]](https://blog.talosintelligence.com/ir-trends-ransomware-on-the-rise-q2-2024/) and [[here]](https://blog.talosintelligence.com/incident-response-trends-q3-2024/). For the fourth consecutive time in over a year, the most observed means of gaining initial access was the use of valid accounts, making it clear identity-based attacks are becoming more prevalent, and wont be gone anytime soon.

 Advocate for the use of a password managers—there are paid versions with family plans on one end, and excellent open-source alternatives on the other. Avoid storing credentials in browsers, as they can be extracted by [info-stealers](https://blog.talosintelligence.com/new-pxa-stealer/). Consider using passkeys where possible. According to the [fido alliance](https://fidoalliance.org/wp-content/uploads/2024/05/World-Password-Day-2024-Report-FIDO-Alliance.pdf), more than 20% of the world's top 100 websites support passkeys already. If passkeys are not yet enabled for one of your services? Any MFA is better than none. Even using "just" TOTP in a software container is a significant improvement over just a password.

But it's not just about enabling MFA. As Martin wrote last week, we need to close the gap by communicating and understanding the the threat landscape. When it comes to stolen credentials, share resources like https://haveibeenpwned.com/ or https://sec.hpi.de/ilc/?lang=en with your loved ones so they can check if their email has been part of a breach.

If you decide not to bother your friends & famliy (though I strongly believe [Mbappe](https://www.cbssports.com/soccer/news/kylian-mbappe-social-media-apparently-hacked-madrid-stars-account-makes-posts-taking-aim-at-lionel-messi/), [Sweeny and Odenkirk](https://x.com/zachxbt/status/1818245914580120015) would have preferred a more secure account) with Account/Password Hygiene, there are some more work related recommendations in Hazel’s “[How are attackers trying to bypass MFA](https://blog.talosintelligence.com/how-are-attackers-trying-to-bypass-mfa/)”

Whichever is your idea of Christmas, then, like Argyle said, "I gotta be here for New Year's!"

We look forward to seeing you in 2025!

## The one big thing

At the time of writing, our Vulnerability Research Team Disclosed 207 Vulnerabilities, and had another 93 reported to the respective Vendor in 2024.  Di you know  Talos has a team which investigates [software and operating system vulnerabilities](https://talosintelligence.com/vulnerability_info) in order to discover them before malicious threat actors do? Every day, they try to find vulnerabilities that have not yet been discovered, and then work to provide a fix for those before a zero-day threat could ever be executed.

### Why do I care?

We see threat actors exploiting known vulnerabilities constantly. Sometimes those CVEs are Years old.

### So now what?

Maybe you want to check for some CVEs or conduct a network security assessments.
You can our team’s [reports](https://talosintelligence.com/vulnerability_reports/),[roundups](https://blog.talosintelligence.com/category/vulnerability-roundup/),[spotlights](https://blog.talosintelligence.com/category/vulnerability-spotlight/) an...