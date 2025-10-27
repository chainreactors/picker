---
title: What can we learn from the passwords used in brute-force attacks?
url: https://blog.talosintelligence.com/threat-source-newsletter-may-2-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-03
fetch_date: 2025-10-06T17:15:51.145925
---

# What can we learn from the passwords used in brute-force attacks?

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

# What can we learn from the passwords used in brute-force attacks?

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, May 2, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Brute force attacks are one of the most elementary cyber threats out there. Technically, anyone with a keyboard and some free time could launch one of them — just try a bunch of different username and password combinations on the website of your choice until you get blocked.

Nick Biasini and I [discussed some of the ways](https://talostakes.talosintelligence.com/2018149/14956921-how-to-defend-against-brute-force-attacks) that organizations can defend against brute force attacks since detection usually doesn’t fall into the usual bucket (ex., there’s nothing an anti-virus program could detect running). But a good place to start just seems to be implementing strong password rules, because people, unsurprisingly, are still using some of the most obvious passwords that anyone, attacker or not, would guess.

Along with our [advisory on a recent increase in brute force attacks](https://blog.talosintelligence.com/large-scale-brute-force-activity-targeting-vpns-ssh-services-with-commonly-used-login-credentials/) targeting SSH and VPN services Cisco Talos published a list of IP addresses associated with this activity, [along with a list of usernames and passwords](https://github.com/Cisco-Talos/IOCs/blob/main/2024/04/large-scale-brute-force-activity-targeting-vpns-ssh-services-with-commonly-used-login-credentials.txt) adversaries typically try to use to gain access to a network or service.

There are some classics on this list — the ever-present “Password” password, Passw0rd (with a zero, not an “O”) and “123456.” This tells me that users still haven’t learned their lesson. It’s somewhat funny to think about some well-funded actor just being like, “Well, let me try to ‘hack’ into this machine by using ‘123456’” as if they’re in a parody movie, but if they already can guess a username based off someone’s real name, it’s not that unlikely that password is being used somewhere.

A few other example passwords stood out to me: “Mart1x21,” because I can’t tell if this is just someone named “Martin” or a play on the month of March, and things like “Spring2024x21” and “April2024x21” because I appreciate the idea that someone using that weak of a password thinks that adding the extra three characters onto “April2024” is really going to throw an attacker off.

Looking at this list got me thinking about what some potential solutions are to the internet’s password problem, and our ever-present battle to educate users and warn them about the dangers of using weak or default passwords.

[Going passwordless](https://talostakes.talosintelligence.com/2018149/11127949) is certainly one option because if there just are no passwords to log in, there’s nothing text-based an attacker could just start guessing.

The best solution I’ve seen recently is that the U.K. literally made a law requiring hardware and software manufacturers to implement stronger security standards. The [Product Security and Telecommunications Infrastructure (PSTI)](https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime) that went into effect last month contains a range of security protections companies must follow, but they now include mandatory password rules that will force users to change default passwords when registering for new accounts and [stop them from using easy-to-guess passwords](https://news.sky.com/story/admin-and-12345-banned-from-being-used-as-passwords-in-uk-crackdown-on-cyber-attacks-13125565) like “Admin” and “12345.”

It would be great if users would just stop using these credentials on their own, but if attackers are still thinking that someone out there is using “Password” as their password, they probably are.

## The one big thing

For the first time in several quarters, business email compromise (BEC) was the most common threat in Cisco Talos Incident Response (Talos IR) engagements during the first quarter of 2024. BEC made up 46 percent of all engagements in Q1, a significant spike from Q4 2023, according to the [latest Talos IR Quarterly Trends Report](https://blog.talosintelligence.com/talos-ir-quarterly-trends-q1-2024/). Ransomware, which was the top-observed threat in the last quarter of 2023, decreased by 11 percent. Talos IR also observed a variety of threats in engagements, including data theft extortion, brute-force activity targeting VPNs, and the previously seen commodity loader Gootloader.

### Why do I care?

BEC is a tactic adversaries use to disguise themselves as legitimate members of a business and send phishing emails to other employees or third parties, often pointing to a malicious payload or engineering a scheme to steal money. The use of email-hiding inbox rules was the top-observed defense evasion technique, accounting for 21 percent of engagements this quarter, which was likely due to an increase in BEC and phishing within engagements. These are all valuable insights from the field provided in Talos IR’s full report.

### So now what?

There are some known indicators of compromise that customers can look for if they suspect The lack of MFA remains one of the biggest impediments for enterprise security. All organizations should implement some form of MFA, such as Cisco Duo. The implementation of MFA and a single sign-on system can ensure only trusted parties are accessing corporate email accounts, to prevent the spread of BEC. If you’d like to read about other lessons from recent Talos IR engagements, read the [one-pager here](https://blog.talosintelligence.com/content/files/2024/04/Talos-IR-Trends--Q1-2...