---
title: Impact of data breaches is fueling scam campaigns
url: https://blog.talosintelligence.com/data-breaches-fueling-scam-campaigns/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-12
fetch_date: 2025-10-06T17:46:04.943317
---

# Impact of data breaches is fueling scam campaigns

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

![](/content/images/2024/07/Screenshot-2024-07-10-at-15.32.46.png)

# Impact of data breaches is fueling scam campaigns

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Thursday, July 11, 2024 06:00

[On The Radar](/category/on-the-radar/)

* Data breaches have become one of the most crucial threats to organizations across the globe, and they’ve only become more prevalent and serious over time.
* A data breach occurs when unauthorized individuals gain access to sensitive, protected or confidential data. This stolen data can include personal information, financial records, intellectual property, and other critical information.
* Stolen data is a valuable commodity in the cybercriminal world and, once acquired through data breaches, is often sold on underground markets.
* A recent cryptocurrency-related scam Cisco Talos discovered highlights how data breaches are being increasingly leveraged in these types of campaigns, preying on targets’ fears around their information being out in the wild.

Over the years, data breaches have played a pivotal role in facilitating various forms of cyber-attacks.  Adversaries are leveraging on stolen data to execute more sophisticated and damaging attacks to materialize their malicious intents. The significance of data breaches extends far beyond the immediate loss of data with the implications for security, reputation and financial stability of individuals and organizations.

# Active scam campaign likely leveraging on stolen data

Cisco Talos observed an ongoing cryptocurrency heist scam since as early as January 2024, leveraging hybrid social engineering techniques such as vishing and spear phishing, impersonating individuals and legitimate authorities to compromise the victims by psychologically manipulating their trust with social skills.

Impersonating investigation officers of CySEC (Cyprus Securities and Exchange Commission), the scammers in this campaign are using a lure theme of refunding a fake seized amount from a fraudulent trading activity in Opteck trading platform to compromise the victims.

Opteck is a trading platform founded in 2011 and provides binary options trading solutions for its customers. In 2017, Opteck’s database was sold on raidforums by adversaries and even today, we still see users’ Opteck login credentials being sold on Russian dark markets, indicating the likelihood of a data breach. That same year, CySEC (Cyprus Securities and Exchange Commission) flagged Opteck as non-complaint and had suspended its license until they took action to rectify the issues. The scammers are likely leveraging the stolen data in the dark web and the news to create a more convincing lure for this campaign.

[CySEC](https://www.cysec.gov.cy/CMSPages/GetFile.aspx?guid=05d22d14-a9a2-43c4-b77b-b07e686704e3) issued other warnings in November 2022 that fraudsters are impersonating their officers and making fake offers to assist investors with compensation claims for the dealings that they may have had with the sanctioned firms.

Since January 2024, Talos has been observing that the scammer, impersonating certified investigation officers of CySEC, is attempting to contact a potential victim who is or was once a user of the Opteck trading platform. The scammers, after getting connected to a potential victim over the phone, introduces them as the investigation officers of CySEC, confirming that the potential victim was once an Opteck trading platform user. Then, they attempt to get the potential victim into a conversation, explaining a fake story of a fraudulent activity that Opteck was involved in and misusing potential victim’s cryptocurrency investments. The scammer also tried to assure the potential victims that their phone call was for refunding an amount they had seized, claiming that the amount belongs to the potential victim.

To convince the victims, scammers send an email impersonating the identities of the CySEC officers by misusing the CySEC investigating officers’ names in the CySEC’s Public Register of Certified Persons documentation from CySEC official website.  In one instance, the scammer had created a fake business card and embedded it in the phishing email to make the phishing email appear legitimate.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-638d874f-42b8-4837-aba4-35492010951b.png)

Sample 1 of the phishing email.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-4b026b61-c3f3-4471-aeea-5b0eeec71e25.png)

Sample 2 of the phishing email.

Upon compromising the victim and gaining their confidence, the scammer sends another email asking the victims’ bank statement as part of regulatory compliance verifications.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-3d9b1853-6eeb-4014-96c9-c492c29c29ba.png)

Phishing email sample 3.

They will also send a follow-up email to the victim, explaining the fake refund process that includes an identity verification stage and after that they will engage the victims in a 20-minute telephonic conversation and assisting them in withdrawing funds.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-af862d87-cbe6-4d6f-82bc-fd98f7a32ecc.png)

Phishing email sample 4.

We observed that when a victim engages in a phone conversation with the scammer, first they will create a cryptocurrency wallet in the Coinbase platform and send the wallet ID to the victim, assuring that they will give him 816 USDT as a wallet activation amount, which will be available 12 hours after activation.

In case of any errors performed by a victim, the scammer demands the victim transfer some specified ETH to another cryptocurrency wallet ID belonging to the scammer, which they are calling an AML wallet in this campaign. They also advise...