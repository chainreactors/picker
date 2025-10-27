---
title: Threat Source newsletter (March 30, 2023) — It’s impossible to tell if your home security camera or doorbell is truly safe
url: https://blog.talosintelligence.com/threat-source-newsletter-march-30-2023/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-31
fetch_date: 2025-10-04T11:16:13.336260
---

# Threat Source newsletter (March 30, 2023) — It’s impossible to tell if your home security camera or doorbell is truly safe

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

# Threat Source newsletter (March 30, 2023) — It’s impossible to tell if your home security camera or doorbell is truly safe

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, March 30, 2023 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Everyone loves a good video of someone slipping on their icy steps in the winter, captured thanks to their home security camera or smart doorbell. But what about when that camera is just kind of chilling out and not catching the moment your dog takes off after that squirrel?

The world of security cameras and recording devices attached to one’s home is becoming increasingly murky by the day. Law enforcement officials are finding ways to compel the companies that manufacture and manage these devices to [turn over homeowners’ footage](https://www.politico.com/news/2023/03/07/privacy-loophole-ring-doorbell-00084979), even if the homeowner doesn’t consent to it.

And Amazon Ring, the biggest player in this space now, [may or may not be](https://gizmodo.com/amazon-ring-ransomware-gang-claims-hack-1850223835) the [target of a ransomware attack](https://www.vice.com/en/article/qjvd9q/ransomware-group-claims-hack-of-amazons-ring).

So, while consumers might be purchasing these devices to ensure their physical security, the question about if these products are good for online security is a major question mark.

As Talos’ own Joe Marshall [wrote in a guest column at Dark Reading this week](https://www.darkreading.com/ics-ot/spend-on-safety-measures-call-out-insecure-practices-for-safer-iot), “IoT vendors continue to fail us on implementing solid cybersecurity controls.” This even goes for some of the largest tech companies in the world who would conceivably have the most money to invest in securing and testing these devices before they hit the market.

There are tons of budget options on the market that, unless you are an expert vulnerability researcher, are impossible to fully vet. I just went to Amazon’s website this week and searched for “smart doorbell.” Three of the best-selling items on the first page of results use nearly the exact same thumbnail art to advertise the product. Yet when you go to their product pages, each one is listed as being manufactured or sold by a different company.

![](data:image/png;base64...)

If you’re merely reading the reviews of these products to figure out what’s right for you, or searching the internet for someone else’s review, they may mention if the resolution quality is up to snuff or if the app works well, but I doubt the reviewer has the time to physically tear apart the device looking for vulnerabilities or combing through the API for security holes. And if we can’t even trust the companies making these devices to differentiate their products based on appearance, there is no way to know how they may be prepared to respond to a data breach or what their stance is on sharing footage with law enforcement.

The same goes for security cameras. On Amazon’s [search page for “home security camera,”](https://www.amazon.com/s?k=home+security+camera&crid=1OS104AZK28LA&sprefix=%2Caps%2C72&ref=nb_sb_ss_recent_1_0_recent) the top five non-sponsored results are all made by different companies (Ring being one of them) and based on the features they offer, it’s nearly impossible to differentiate them outside of a difference in form factor. Very few of us looking to buy these pieces of equipment are qualified to say if these products are even secure, and those among us who are are probably smart enough to know not to buy these products in the first place.

I certainly wouldn’t stop anyone from buying a home security camera if they truly feel it improves their families’ safety. But I think that, no matter what brand we buy, everyone just needs to assume now that they’re taking a risk with their privacy and online security as a trade-off for catching possible package burglars.

## The one big thing

Emotet is [back from the dead once again.](https://blog.talosintelligence.com/emotet-switches-to-onenote/) Since returning, Emotet has leveraged several distinct infection chains, indicating that they are modifying their approach based on their perceived success in infecting new systems. The initial emails delivered to victims are consistent with what has been observed from Emotet over the past several years.

Why do I care?

Emotet is arguably the most infamous botnet on the threat landscape, so it’s notable any time it spins back up. This network is known to go through quiet periods and then pop back up, so this isn’t particularly surprising, but it is noteworthy because Emotet’s creators are switching up their tactics by switching to new types of lure documents to evade detection and recent changes Microsoft made to macros to try and stop attackers from using malicious Office attachments.

### So now what?

Because Emotet has been around for so long now, Cisco Secure and Talos have an exhaustive list of ways to stay protected from Emotet spam. But as a good general reminder, always make sure you triple-check the “From” field in an email to make sure it’s actually from who you think its from. And never open an attachment or click on a link in an email unless you’re sure it’s the correct destination.

### Top security headlines of the week

**Defenders and detractors of TikTok both seem unmoved** after the popular social media app’s CEO testified in front of a U.S. Congressional panel last week. Lawmakers who are in favor of a blanket ban on the app in the U.S. over data and privacy concerns were unimpressed with the answers the company’s lead provided, while others mocked lawmakers for the types of questions they asked and instead ad...