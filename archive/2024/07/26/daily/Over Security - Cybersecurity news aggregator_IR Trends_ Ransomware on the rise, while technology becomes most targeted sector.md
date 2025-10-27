---
title: IR Trends: Ransomware on the rise, while technology becomes most targeted sector
url: https://blog.talosintelligence.com/ir-trends-ransomware-on-the-rise-q2-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-26
fetch_date: 2025-10-06T17:44:22.713118
---

# IR Trends: Ransomware on the rise, while technology becomes most targeted sector

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

# IR Trends: Ransomware on the rise, while technology becomes most targeted sector

By
[Nicole Hoffman](https://blog.talosintelligence.com/author/nicole/)

Thursday, July 25, 2024 06:00

[Talos IR trends](https://blog.talosintelligence.com/category/ctir-trends/)
[Cisco Talos Incident Response](https://blog.talosintelligence.com/category/cisco-talos-incident-response/)

Business email compromise (BEC) and ransomware were the top threats observed by Cisco Talos Incident Response (Talos IR) in the second quarter of 2024, together accounting for 60 percent of engagements.

Although there was a decrease in BEC engagements from [last quarter](https://blog.talosintelligence.com/talos-ir-quarterly-trends-q1-2024/), it was still a major threat for the second quarter in a row. There was a slight increase in ransomware where Talos IR responded to Mallox and Underground Team ransomware for the first time this quarter, as well as the previously seen Black Basta and BlackSuit ransomware operations.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-3361828e-2877-4c32-a314-19d9550709fb.jpeg)

For the third quarter in a row, the most observed means of gaining initial access was the use of compromised credentials on valid accounts, which accounted for 60 percent of engagements this quarter, a 25 percent increase from the previous quarter.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-f22236fc-b88c-4abf-8cff-d200d203bb19.jpeg)

Technology was the most targeted vertical this quarter, accounting for 24 percent of engagements, closely followed by healthcare, pharmaceuticals and retail. There was a 30 percent increase in engagements affecting the technology sector from the previous quarter. Organizations in the technology sector may be seen as gateways into other industries and organizations given their significant role in supplying and servicing a wide range of sectors, making them attractive targets for adversaries.

Technology organizations often have extensive digital assets supporting critical infrastructure, which means they have minimal tolerance for downtime and may, therefore, be more likely to pay extortion demands.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-74bbe456-ab55-4381-a8f9-8a3e1000f127.jpeg)

Talos IR also observed a slight increase in network device targeting this quarter, accounting for 24 percent of engagements. This activity included password-spraying, vulnerability scanning and exploitation.

## Watch discussion on the report's biggest trends

##

## Surge in BEC continues

Within BEC attacks, adversaries will compromise legitimate business email accounts and use them to send phishing emails to obtain sensitive information, such as account credentials. Adversaries can also use compromised accounts to send emails with fraudulent financial requests, such as changing bank account information related to payroll or vendor invoices.

In a few of the observed BEC incidents that involved a method of phishing as an infection vector, adversaries leveraged SMS phishing, or “smishing,” to compromise accounts. This involves adversaries sending fraudulent text messages to trick recipients into sharing personal information or clicking on malicious links.

Targeting employees’ personal mobile devices can be an effective method for initial access because they may not have the same security controls as their corporate devices. Organizations should ensure SMS phishing scams are included in security awareness training for employees.

[Talos IR Quarterly Trends Report (Q2 2024)

Download a one-page version of our report here!

Talos IR Q224.pdf

168 KB

download-circle](https://blog.talosintelligence.com/content/files/2024/07/Talos-IR-Q224.pdf "Download")

In one engagement, adversaries compromised a user’s account by sending a phishing email to the employee’s personal email address that redirected the user to a fake login page. The user had passwordless authentication through an authenticator application but received a multi-factor authentication (MFA) push notification and accepted it, granting the adversary access.

In another cluster of activity, adversaries used compromised credentials obtained through unknown means to access a valid email account. The adversary then created Microsoft Outlook mailbox rules to send emails to a folder named “deleted” before using the compromised account to send out over a thousand phishing emails to internal and external recipients. The phishing emails contained a link that led to a fake login page intended to harvest credentials.

## Ransomware trends

Ransomware accounted for 30 percent of engagements this quarter, a 22 percent increase from the previous quarter. Talos IR observed Mallox and Underground Team ransomware families for the first time this quarter. Talos IR also responded to the previously seen Black Basta and BlackSuit ransomware this quarter, which we recently assessed are [two of the top players](https://blog.talosintelligence.com/common-ransomware-actor-ttps-playbooks/) within the current ransomware landscape.

Notably, 80 percent of ransomware engagements this quarter lacked proper MFA implementation on critical systems, such as virtual private networks (VPNs), playing a role in allowing adversaries to gain initial access. In addition, command obfuscation, such as Base64 encoding, was observed within 40 percent of ransomware engagements this quarter, likely to evade detection by disguising the true intent of the commands.

### Mallox

In a Mallox ransomware engagement, adversaries compromised and encrypted a single Microsoft SQL server, consistent with public reporting on Mallox ransomware attacks. There were no signs of data staging, exfiltration or lateral movement. Talos IR could not determine the initia...