---
title: Attackers are impersonating a road toll payment processor across the U.S. in phishing attacks
url: https://blog.talosintelligence.com/threat-source-newsletter-may-30-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-31
fetch_date: 2025-10-06T16:51:34.082396
---

# Attackers are impersonating a road toll payment processor across the U.S. in phishing attacks

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

# Attackers are impersonating a road toll payment processor across the U.S. in phishing attacks

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, May 30, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

My wife ([no stranger to weird types of scams](https://blog.talosintelligence.com/threat-source-newsletter-sept-7-23/)) recently received a fake text message from someone claiming to be New Jersey’s E-ZPass program saying that she had an outstanding balance from highway tolls that she owed, prompting her to visit a site so she could pay and avoid additional fines.

There was plenty of reason to believe this was a legitimate ask. Her family is from New Jersey, so we make frequent trips there, paying $20-plus in tolls along the way. We had also just completed a trip from there a few weeks prior (though I’m not sure if this was a coincidence to the timing of the spam text or not), and we both have E-ZPass accounts.

For the uninitiated, or anyone who lives in a country where taxes are paid as normal and therefore pay for appropriate road repairs, E-ZPass is a small device drivers in more than a dozen countries in the U.S. can register for so they can automatically pay tolls along highways rather than having to stop and use cash or coins, or spending a few extra minutes manually processing a transaction.

Each state or city has its own agencies that deal with E-ZPass, each with its own payment processing system and website. For this case with New Jersey, the phishing site the scammers set up was shockingly convincing and looked remarkably similar to the legitimate New Jersey E-ZPass website.

![](https://blog.talosintelligence.com/content/images/2024/05/Screenshots.jpg)

The phishing website set up by scammers (left) meant to look like the legitimate New Jersey E-ZPass website (right).

Once we logged into our legitimate E-ZPass account to check to make sure we had, in fact, paid all the appropriate tolls, I alerted my team about this scam, and we appropriately blocked the phishing URL in question in Cisco Secure products.

Since this victory and foray into threat hunting, I have learned that this is a problem everywhere, not just for New Jersey drivers.

Since this experience, E-ZPass has sent out an alert in all the states they operate in warning about these types of scams. Drivers from [New York](https://www.nj.com/news/2024/04/get-a-toll-violation-text-from-e-zpass-its-a-fake.html) to [Georgia](https://www.11alive.com/article/news/verify/scams-verify/texts-about-outstanding-toll-balances-are-scams/) and [Pennsylvania](https://www.paturnpike.com/news/details/2024/04/07/pa-turnpike-alerts-e-zpass-users-of-phishing-scam) have received these types of texts with equally convincing phishing text messages and lure pages.

It’s unclear what the adversaries’ goals are in this case, but it’s probably safe to assume they’re looking to collect users’ credit card information after they go in to pay the alleged overdue toll. They could also be collecting E-ZPass login information to collect further data about the drivers.

In April, the FBI also warned of SMS phishing scams, in which adversaries pretended to be toll collection services from [three different U.S. states](https://ic3.gov/Media/Y2024/PSA240412). SunPass, the equivalent to E-ZPass in Florida, also [alerted about similar scams](https://www.wusf.org/transportation/2024-04-25/sunpass-users-phishing-text-message-scam-targeting-general-public) around the same time as these E-ZPass scams started being reported. And in March, the FasTrak service in California [warned of the same problems](https://www.sfchronicle.com/crime/article/bay-area-fastrak-scam-19363141.php).

My hunch is that these types of services are being impersonated all over the U.S. for several reasons — thousands of drivers use these services (especially in states with a high commuter population), which makes it likely that whoever receives the text will be familiar with these devices and will have recently driven on a highway that makes drivers pay tolls. The amounts they’re asking for are also small, no more than $5 USD, so it doesn’t set off any immediate alarm bells, unlike similar scams that ask for hundreds of dollars for health care services. The requests coming through as SMS messages also make the targets more likely to open them on their mobile devices, which may not have the same security in place as a laptop or managed company device.

No individual state or local agency is immune from this style of scam, so if you’re ever in doubt of receiving a text like this, it’s best to call your area government program in question and ask them about any suspicious activity before clicking on any links or submitting payment information.

## The one big thing

Cisco Talos’ Vulnerability Research team has helped to disclose and patch [more than 20 vulnerabilities over the past three weeks](https://blog.talosintelligence.com/vulnerability-roundup-may-29-2024/), including two in the popular Adobe Acrobat Reader software. Acrobat, one of the most popular PDF readers currently available, contains two out-of-bounds read vulnerabilities that could lead to the exposure of sensitive contents of arbitrary memory in the application. There are also eight vulnerabilities in a popular line of PLC CPU modules commonly used in automated environments. We have more detailed information in our full [Vulnerability Roundup](https://blog.talosintelligence.com/vulnerability-roundup-may-29-2024/) from this week.

### Why do I care?

Several vulnerabilities were identified in the AutomationDirect P3 line of CPU modules. The P3-550E is the most recent CPU module released in the Productivity3000 line of Programmable Automation Controllers from AutomationDirec...