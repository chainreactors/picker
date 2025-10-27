---
title: New PXA Stealer targets government and education sectors for sensitive information
url: https://blog.talosintelligence.com/new-pxa-stealer/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-15
fetch_date: 2025-10-06T19:21:20.414636
---

# New PXA Stealer targets government and education sectors for sensitive information

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

# New PXA Stealer targets government and education sectors for sensitive information

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/),
[Alex Karkins](https://blog.talosintelligence.com/author/alex/),
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan-raghuprasad/)

Thursday, November 14, 2024 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[Stealer](https://blog.talosintelligence.com/category/stealer/)

* Cisco Talos discovered a new information stealing campaign operated by a Vietnamese-speaking threat actor targeting government and education entities in Europe and Asia.
* We discovered a new Python program called PXA Stealer that targets victims’ sensitive information, including credentials for various online accounts, VPN and FTP clients, financial information, browser cookies, and data from gaming software.
* PXA Stealer has the capability to decrypt the victim’s browser master password and uses it to steal the stored credentials of various online accounts.
* The attacker has used complex obfuscation techniques for the batch scripts used in this campaign.
* We discovered the attacker selling credentials and tools in the Telegram channel “Mua Bán Scan MINI,” which is where the [CoralRaider](https://blog.talosintelligence.com/coralraider-targets-socialmedia-accounts/) adversary operates, but we are not sure if the attacker belongs to the CoralRaider threat group or another Vietnamese cybercrime group.

# Victimology and targeted information

The attacker is targeting the education sector in India and government organizations in European countries, including Sweden and Denmark, based on Talos telemetry data.

The attacker’s motive is to steal the victim’s information, including credentials for various online accounts, browser login data, cookies, autofill information, credit card details, data from various cryptocurrency online and desktop wallets, data from installed VPN clients, gaming software accounts, chat messengers, password managers, and FTP clients.

![](https://blog.talosintelligence.com/content/images/2024/11/data-src-image-5df54283-fcc9-48f5-8628-ec88cbd419b6.jpeg)

# Attacker’s infrastructure

Talos discovered that the attacker was hosting malicious scripts and the stealer program on a domain, tvdseo[.]com, in the directories “/file”, “/file/PXA/”, “/file/STC/”, and “/file/Adonis/”. The domain belongs to a Vietnamese professional search engine optimization (SEO) service provider; however, we are not certain whether the attacker has compromised the domain to host the malicious files or has subscribed to get legitimate access while still using it for their malicious purposes.

We found that the attacker is using the Telegram bot for exfiltrating victims’ data. Our analysis of the payload, PXA Stealer, disclosed a few Telegram bot tokens and the chat IDs – controlled by the attacker.

|  |
| --- |
| Attacker-controlled Telegram bot token |
| 7545164691:AAEJ4E2f-4KZDZrLID8hSRSJmPmR1h-a2M4  7414494371:AAGgbY4XAvxTWFgAYiAj6OXVJOVrqgjdGVs |
| Attacker-controlled Telegram chat IDs |
| -1002174636072  -1002150158011  -4559798560  -4577199885  -4575205410 |

# Attacker’s underground activities

We identified attacker’s Telegram account “Lone None,” which was hardcoded in the PXA Stealer program and analyzed various details of the account, including the icon of Vietnam’s national flag and a picture of the emblem for Vietnam’s Ministry of Public Security, which aligns with our assessment that the attacker is of Vietnamese origin. Also, we found Vietnamese comments in the PXA Stealer program, which further strengthen our assessment.

|  |  |
| --- | --- |
| ![](data:image/png;base64...) | ![](data:image/jpeg;base64...) |

The attacker’s Telegram account has biography data that includes a link to a private antivirus checker website that allows users or buyers to assess the detection rate of a malware program. This website provides a platform for potential threat actors to evaluate the effectiveness and stealth capabilities of the malware before purchasing it, indicating a sophisticated level of service and professionalism in the threat actor's operations.

![](https://blog.talosintelligence.com/content/images/2024/11/Screenshot-2024-11-12-at-4.23.39-PM.png)

We also discovered that the attacker is active in an underground Telegram channel, “Mua Bán Scan MINI,” mainly selling Facebook accounts, Zalo accounts, SIM cards, credentials, and money laundry data. Talos observed that this Vietnamese actor is also seen in the Telegram group in which the CoralRaider actor operates. However, we are not certain whether the actor is a member of the CoralRaider gang or another Vietnamese cybercrime group.

Talos discovered that the attacker is also promoting another underground Telegram channel, “Cú Black Ads – Dropship," by sharing a few automation tools to manage large numbers of user accounts in their channel and conducting the exchanging or selling of information related to social media accounts, proxy services, and a batch account creator tool.

|  |  |
| --- | --- |
| ![](data:image/png;base64...) | ![](data:image/png;base64...) |

The tools shared by the attacker in the group are automated utilities designed to manage several user accounts. These tools include a Hotmail batch creation tool, an email mining tool, and a Hotmail cookie batch modification tool. The compressed packages provided by the threat actor often contain not only the executable files for these tools but also their source code, allowing users to modify them as needed.

![](https://blog.talosintelligence.com/content/images/2024/11/Screenshot-2024-11-12-at-4.20.44-PM.png)

Hotmail batch creation tool from telegram channel.

![](https://blog.talosintelligence.com/content/images/2024/11/Screenshot-2024-11...