---
title: Threat actor abuses Gophish to deliver new PowerRAT and DCRAT
url: https://blog.talosintelligence.com/gophish-powerrat-dcrat/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-23
fetch_date: 2025-10-06T18:55:15.642008
---

# Threat actor abuses Gophish to deliver new PowerRAT and DCRAT

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

![](/content/images/2024/10/powershellheader-01.jpg)

# Threat actor abuses Gophish to deliver new PowerRAT and DCRAT

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Tuesday, October 22, 2024 06:00

[RAT](/category/rat/)
[Threats](/category/threats/)

* Cisco Talos recently discovered a phishing campaign using an open-source phishing toolkit called [Gophish](https://github.com/gophish/gophish) by an unknown threat actor.
* The campaign involves modular infection chains that are either Maldoc or HTML-based infections and require the victim’s intervention to trigger the infection chain.
* Talos discovered an undocumented PowerShell RAT we’re calling PowerRAT,  as one of the payloads and another infamous Remote Access Tool (RAT) DCRAT.
* We found a few placeholders for base64 encoded PowerShell scripts in the PowerRAT, indicating that the threat actor is actively developing their tools.

# Victimology

Talos assesses with high confidence that the threat actor is targeting Russian-speaking users based on the language used in the Phishing emails, luring contents of Malicious documents, a masqueraded HTML webpage of Vkontake (VK), a popular social media application amongst Russian speakers, especially in Russia, Ukraine, Belarus, Kazakhstan, Uzbekistan, and Azerbaijan.

|  |  |
| --- | --- |
| ![](data:image/png;base64...) | ![](data:image/png;base64...) |

# Actor uses Gophish to send phishing emails

Our analysis of the malicious hyperlinks embedded in the phishing emails disclosed to us the attacker-controlled hosting domains disk-yanbex[.]ru delivered the Malicious Microsoft Word document, and an HTML file embedded with the malicious JavaScript.

The domain disk-yanbex[.]ru resolves to the IP address 34[.]236[.]234[.]165, an AWS EC2 instance with the fully qualified domain name ec2-34-236-234-165[.]compute-1[.]amazonaws[.]com, during our analysis. We also observed that the same server 34[.]236[.]234[.]165 was reverse resolving to another domain e-connection[.]ru, which also delivered malicious JavaScript-embedded HTML files. Our further analysis of the server 34[.]236[.]234[.]165 disclosed to us that the actor hosted the Gophish toolkit on the server running at port number 3333. [Gophish](https://github.com/gophish/gophish) is an Open-Source easy-to-deploy phishing toolkit that is developed to conduct security awareness training according to the tool’s developer.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-a47cae3e-74fc-48ed-b7fc-891fcbc16d1d-1.png)

Attacker hosting Gophish.

Talos analysis of the phishing email sample’s header showed us that the email was first delivered from server 34[.]236[.]234[.]165, indicating that the threat actor is misusing the Gophish framework in this campaign to deliver phishing emails to their targets.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-0b19a190-616a-4964-a3dd-7ba075e54c14.png)

Sample Phishing email header.

# Multi-modular Campaign delivers PowerRAT and DCRAT

The campaign has two initial attack vectors, one based on malicious Word documents and another based on HTML files containing malicious JavaScript. Upon activation, these would lead to the download and activation of PowerRAT or DCRAT depending on the initial vector. Both the attack chains require user intervention to trigger the infections on the compromised machines.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-8a7bb4a5-b58b-4e29-bfbc-86206837c666.jpeg)

# Maldoc-based infection delivers PowerRAT

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-31dd1180-86de-49b7-8869-e1b7667bd22c.jpeg)

When a victim opens the Microsoft Word document and enables the view contents button displayed in the document banner, the malicious VB macro program executes.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-265ba20d-5358-4b3d-a872-a7b0a9e43f97.png)

The macro program initially executes a function that decodes or translates specific encoded symbols in the lure contents of the Word document into their corresponding characters from another alphabet in Cyrillic, transforming the lure contents into readable form.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-93568815-92bb-41d9-9885-0e8a56dd1f03.png)

We spotted a base64 encoded data blob on the third page of the Word document and the actor used the text color the same as that of the document's default background color, hiding them from the victim’s view.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-fb0ca5d1-d20d-4e5f-a268-7ece44b3fa6b.png)

To identify the hidden encoded data, the macro executes a function that searches for specific strings such as “DigitalRSASignature:” and “CHECKSUM” in the content section of the Word document, and when found, it copies the data following the search strings to an array.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-8fdeb4df-fb37-4319-a6d2-532efe910b26.png)

To decode the base64 encoded data blob, the actor uses a custom function called CheckContent() in the macro. It removes any “=” characters which are the padding characters in the encoded data blob and decodes them into two parts in a byte array. The first part is the contents of a malicious HTML application (HTA) file and the second is a PowerShell loader.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-402eacb6-c297-4bd9-ac10-085533f02586.png)

The macro drops the decoded contents of the malicious HTA file to “UserCache.ini.hta” and the PowerShell loader into “UserCache.ini” in the victim machine's current user profile folder.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-bcc5855...