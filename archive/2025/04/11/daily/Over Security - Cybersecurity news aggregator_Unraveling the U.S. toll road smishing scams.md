---
title: Unraveling the U.S. toll road smishing scams
url: https://blog.talosintelligence.com/unraveling-the-us-toll-road-smishing-scams/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-11
fetch_date: 2025-10-06T22:06:10.141874
---

# Unraveling the U.S. toll road smishing scams

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

![](/content/images/2025/04/smishing-tolls-1.jpg)

# Unraveling the U.S. toll road smishing scams

By
[Azim Khodjibaev](https://blog.talosintelligence.com/author/azim/),
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/),
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Thursday, April 10, 2025 10:30

[Threat Spotlight](/category/threat-spotlight/)
[phishing](/category/phishing/)

* Cisco Talos has observed a widespread and ongoing financial theft SMS phishing (smishing) campaign since October 2024 that targets toll road users in the United States of America.
* We observed that the campaign targets people across several states in the U.S. according to the domain names used in the smishing messages.
* Talos assesses with moderate confidence that the toll road smishing attacks are being carried out by multiple financially motivated threat actors using the smishing kit developed by “Wang Duo Yu”, according to the intelligence obtained by Talos.

---

## Toll road smishing attacks

Since the middle of Oct. 2024, Talos has seen ongoing smishing attacks impersonating U.S toll road automatic payment services (such as E-ZPass) with the intent of financial theft. The actors have so far sent SMS messages to individuals in about eight states in the U.S., including Washington, Florida, Pennsylvania, Virginia, Texas, Ohio, Illinois and Kansas. Talos identified these states via spoofed domains containing the states’ two-letter abbreviations that we observed in the SMS messages.

The actors send an SMS notification for an outstanding bill claiming that the potential victim owes a small amount of money, under $5 USD. They warn of potential late fees, prompting victims to visit a spoofed domain for the payment.

![](https://blog.talosintelligence.com/content/images/2025/04/data-src-image-20b4ef42-9fbd-4d92-a026-5e58371ab17b.png)

Sample phishing SMS messages.

When the victim visits the domain, they are prompted to solve a fake image-based CAPTCHA, after which it redirects the victims to a fake webpage with the legitimate toll service's logo. This webpage prompts the victims to enter their name and ZIP code to view their fake bill. The fake bill displays the victim's name with a message showing that they owe approximately $4 and warning of a $35 late payment fee.

![](https://blog.talosintelligence.com/content/images/2025/04/data-src-image-470afbaf-b9fa-4e04-90ec-f4e88fd63b6f.jpeg)

After the victim views their fake bill, they click the “Proceed Now” button which redirects them to another fake webpage. This site prompts the victim to enter their name, address, phone number and credit card information, which the threat actor eventually steals. Due to the limited visibility of the threat actor phishing infrastructure, Talos is unsure if there are any further payloads delivered to the victims' devices.

In April 2024, [FBI’s Internet Crime Complaint Center (IC3)](https://www.ic3.gov/PSA/2024/PSA240412) warned about a similar toll road smishing campaign where the threat actor used the same brand impersonation technique but with a slight difference in the SMS message language, monetary values and formatting.

Targeting toll road users in multiple states indicates the likelihood of the threat actor leveraging user information publicly leaked from large databases. For example, the threat actor behind the 2024 [National Public Data leak](https://support.microsoft.com/en-us/topic/national-public-data-breach-what-you-need-to-know-843686f7-06e2-4e91-8a3f-ae30b7213535) released billions of records publicly which were then shared on private Telegram channels for further abuse. However, Talos currently does not have any evidence to suggest that the toll road smishing campaign is fueled by the National Public Data leaks.

## Phishing infrastructure

Talos observed that the actors have used several typosquatted domains in the SMS phishing messages to convince the potential victims to visit them. These typosquatted phishing domains were created during Oct. and Nov. 2024 and were observed resolving to one of the following IP addresses: 45[.]152[.]115[.]161 and 82[.]147[.]88[.]22.

As of March 2025, Talos is still seeing new domains registered by the threat actors for the toll road scams, implying that the campaign is ongoing. During our research period, these newly registered domains resolved to the IP address 43[.]156[.]47[.]209.

![](https://blog.talosintelligence.com/content/images/2025/04/data-src-image-f9f2fa33-fb22-4994-a7fc-593abb414124.jpeg)

## Smishing kits likely used in the U.S. toll road scams

Talos assesses with moderate confidence that multiple threat actors are operating the toll road smishing campaign by leveraging a smishing kit developed by the actor known as “Wang Duo Yu", according to the intelligence obtained by Talos.

We have observed similar smishing kits being used by the organized cybercrime group known as the "[Smishing Triad](https://malpedia.caad.fkie.fraunhofer.de/actor/smishing_triad)." This group has conducted large-scale smishing attacks targeting mail services in multiple countries, including the United States Postal Service (USPS), as well as the financial and commercial sectors previously reported by [Resecurity](https://www.resecurity.com/blog/article/smishing-triad-targeted-usps-and-us-citizens-for-data-theft).

Talos discovered references to specific phishing kits that are targeting toll systems in the DY Tongbu Telegram channel on "老王同步源码开发教学" translated to "Lao Wang Synchronized Source Code Development Tutorial."

![](https://blog.talosintelligence.com/content/images/2025/04/data-src-image-d6705a27-aaf2-4e27-88e5-c53ffc480617.png)

Public Lao Wang Synchronized Source Code Development Tutorial Telegram channel.

The Telegram channel shared details about a phishing module that allegedly spoofs th...