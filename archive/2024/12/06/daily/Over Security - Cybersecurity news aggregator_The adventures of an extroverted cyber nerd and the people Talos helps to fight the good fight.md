---
title: The adventures of an extroverted cyber nerd and the people Talos helps to fight the good fight
url: https://blog.talosintelligence.com/the-adventures-of-an-extroverted-cyber-nerd-and-the-people-talos-helps-to-fight-the-good-fight/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-06
fetch_date: 2025-10-06T19:40:14.879976
---

# The adventures of an extroverted cyber nerd and the people Talos helps to fight the good fight

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

# The adventures of an extroverted cyber nerd and the people Talos helps to fight the good fight

By
[Joe Marshall](https://blog.talosintelligence.com/author/joe-marshall/)

Thursday, December 5, 2024 14:02

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

I am unbelievably lucky to do the work that I do. My title is technically ‘Senior Security Strategist’. It’s a very fancy title, but basically: I get to research threats with my colleagues and friends to keep people safe here at Talos. I also get to travel and talk to our customers and communities about that work and how we fight that good fight. This has taken me to some interesting places - from Ukraine to California and lots of places in between. Not bad for a guy from a small town in Alabama.

This gig isn’t for everyone. You must have some extroverted tendencies, and as the youth would say, some ‘rizz’. It’s not enough to talk about something like, say, ransomware. You need to be able to explain it in high technical detail if needed and then explain it to a board of C-levels and speak the language of business they understand. And you need to do it in an engaging way to keep your audiences bought in. It’s a unique blend of security practitioner expertise and the ability to communicate that to audiences, some technical, some not.

If you’re thinking this also requires some kind of social media influencer level of Hemsworth caliber good looks and hyper charisma, have no fear. I’m about as much a security influencer as Chris Farley was a Beverly Hills ninja. I am just a security nerd who likes to talk. Like I said - I'm very lucky.

Sometimes this gig takes you to very unexpected places. A couple of weeks ago I found myself at the [Ford Foundation Center for Social Justice](https://www.fordfoundation.org/). I was there to attend and support the [NGO-ISAC](https://www.ngoisac.org/) annual summit. The NGO-ISAC ‘is a non-profit organization improving the cybersecurity of US-based nonprofits.’ They do amazing work supporting cyber security for non-governmental organizations that help protect and promote civil society. We’re also fortunate at Talos to be a partner with them and donate time and resources to support their mission of helping the helpers.

We are proud to be partners and volunteer our time with NGO-ISAC and it’s members. If you ever want to be truly humbled, spend time with an NGO and learn about what they do. The energy and heart those people have is incredible and will inspire you. They help feed the hungry, cloth the homeless, protect refugees, promote democracies, and generally help take care of some of the most vulnerable people and institutions our society relies upon. They also traditionally struggle with cybersecurity - security investments and practitioner expertise can be difficult to obtain when your budgets are built upon donations to support your mission. They are the embodiment of fighting the good fight, and we at Talos will always have the time to help them help others.

While I was there, we debuted a custom NGO version of Backdoors & Breaches I helped co-develop with the NGO-ISAC. It was a real hit, and we ran demo games that resonated very well with the audiences. Helping teach cybersecurity to NGOs is fantastic. If we can help them stay secure, there’s so many others who will be helped by it. Also, keep your eyes peeled for a blog post in January about how we designed and created a custom expansion for Backdoors & Breaches.

Also, the Ford Foundation? Amazing building. It’s in the heart of NYC and is an island of pure serenity. They have an indoor atrium/park that is next level. They pipe in some absolute jazz bangers throughout the entire building that, mixed with the decor, exudes a class I've rarely encountered in my travels. If I could make a blanket out of that entire vibe and wrap myself up in it, I'd do it.

# The one big thing

[QR Codes, am I right?](https://blog.talosintelligence.com/malicious_qr_codes/) Sometimes you can scan one with your phone and maybe win a free cheeseburger, sometimes it can take you to a fake O365 phishing site. The tricky bit with QR codes in e-mails is how easily they can avoid spam filters. My man Jaeson Schultz did some great research on attacks, prevalence, and detection of QR codes in e-mail messages. The parts on AI-generated QR imagery are fantastic – be careful what you scan!

### Why do I care?

E-mail phishing and evading defenses are a tried and tested tactic with attackers. QR codes are another method of attack, and because they can be difficult to defang/detect, defenders have to work extra hard to understand those threats and stop them.

### So now what?

Exercise serious caution when scanning a QR code. If possible, detonate those suspicious QR code e-mails in a sandbox, like [Threat Grid](https://www.cisco.com/c/en/us/products/security/threat-grid/index.html).

# Top security headlines of the week

At least 97 major water systems in the US have serious cybersecurity vulnerabilities and compliance issues, raising concerns that cyberattacks could disrupt businesses, industry, and the lives of millions of citizens. ([Dark Reading](https://www.darkreading.com/vulnerabilities-threats/leaky-cybersecurity-holes-water-systems-risk))

The NSA updated its mobile devices security best practices report. Reboot those phones at least once a week friends.  ([ZDNet](https://www.zdnet.com/article/why-you-should-power-off-your-phone-once-a-week-according-to-the-nsa/))

The United States and other Western nations released guidance Tuesday designed to evict the China-linked group in the wake of the high-profile hack. ([CyberScoop](https://cyberscoop.com/u-s-government-says-salt-typhoon-is-still-in-telecom-networ...