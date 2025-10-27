---
title: How do cryptocurrency drainer phishing scams work?
url: https://blog.talosintelligence.com/how-do-cryptocurrency-drainer-phishing-scams-work/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-10
fetch_date: 2025-10-06T17:47:24.542595
---

# How do cryptocurrency drainer phishing scams work?

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

![](/content/images/2024/07/need-to-know-cryptoskimming.jpg)

# How do cryptocurrency drainer phishing scams work?

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Tuesday, July 9, 2024 08:00

[The Need to Know](/category/the-need-to-know/)
[Cryptocurrency](/category/cryptocurrency/)

*By* [*Teoderick Contreras*](https://twitter.com/tccontre18) *and* [*Jose Hernandez*](https://twitter.com/_josehelps) *of Splunk, with contributions from the Splunk Threat Research Team.*

Cryptodrainer scams have emerged as a significant threat in the cryptocurrency ecosystem, targeting unsuspecting individuals with the promise of easy profits while covertly siphoning their digital assets.

Initially, cryptodrainer scams primarily manifested as fraudulent investment schemes, promising high returns on investments in dubious projects or fake initial coin offerings (ICOs). These scams exploited the speculative nature of cryptocurrency markets, luring investors with the allure of quick riches and revolutionary technology. However, instead of delivering on their promises, scammers absconded with investors' funds.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-91d680c1-beb0-4e87-9c42-3f3cd1cfd7f1.png)

An example of a cryptodraining scam spread on a Jamaican news outlet’s X account in 2023 after the account was hacked.

Cryptodrainer phishing scams targeting cryptocurrency holders have become increasingly sophisticated, with scammers employing social engineering techniques to trick users into divulging their private keys or login credentials. These stolen assets were then swiftly drained from victims' wallets, often leaving them with little recourse for recovery.

In recent months, a surge in cryptodrainer phishing attacks has been observed, targeting cryptocurrency holders with sophisticated schemes aimed at tricking them into divulging their valuable credentials. These tactics involve deceptive URLs, carefully crafted to resemble legitimate cryptocurrency platforms, enticing unsuspecting users to input their sensitive login information.

One particularly concerning trend is the emergence of phishing campaigns proliferating across various social media platforms, including X (Twitter). In these instances, compromised accounts, likely hijacked by cybercriminals, are used as unwitting conduits to deliver the malicious URLs to a wider audience. The compromised accounts lend an air of legitimacy to the fraudulent scheme, thereby increasing the likelihood of unsuspecting users falling victim to the scam.

These types of platforms have long been rife for abuse and scams. Cisco Talos has previously highlighted how various aspects of “Web 3” such as the [metaverse and smart contracts](https://blog.talosintelligence.com/securing-web-3-0-metaverse-and-beyond/) have been abused to trick users into emptying their cryptocurrency wallets. [Malicious Google Forms](https://blog.talosintelligence.com/google-forms-quiz-spam/) documents have also been used as an attack vector for these scams.

## Anatomy of a crytodrainer attack

Splunk researchers used the [Splunk Attack Analyzer](https://www.splunk.com/en_us/products/attack-analyzer.html) to gain insights into the anatomy of this phishing campaign, which we believe follows the same general infection method and attack pattern of cryptodrainer scams.

Below are a few examples of phishing website pages designed to mimic legitimate cryptocurrency platforms, enticing users to disclose their cryptocurrency login credentials.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-8d4238c7-e4ee-4c3b-8ac9-483f98397c0c.png)

Phishing site web pages.

Splunk expanded our repository of potential cryptodrainer phishing URLs using the Attack Analyzer. One such example is *hxxp[://]nfts-manta[.]network/*, a site identified and flagged as a [phishing site](https://www.virustotal.com/gui/url/ecad6463dbcda98a25303afbe3a2836719bce0ebcc5dacf94c2a8fa1b1b4b5d6) by several anti-virus products, according to VirusTotal.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-8f170cc4-af4b-4235-bf8a-123743e480a2.png)

A phishing site in VirusTotal.

Splunk Attack Analyzer also provides a comprehensive overview, including the landing page screenshot of the phishing site, potential URL link redirections, detections and related artifacts, facilitating further in-depth analysis.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-f8b8cac8-b67e-4c85-8318-40039ebc08b6.png)

A screenshot of Splunk Attack Analyzer.

Upon accessing this phishing site, users are prompted to connect their cryptocurrency wallets to purportedly claim tokens. A common method observed for wallet connection involves scanning a QR code using a mobile phone. This QR code may seemingly link to the desired cryptocurrency wallet app, offering the illusion of a seamless login process. In reality, this action grants the phishing site access to the user's login credentials, enabling the unauthorized draining of their cryptocurrency wallet.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-e9673270-c54f-4921-a643-fba5765ba664.png)

A phishing website posing as Manta, a cryptocurrency application.

![](https://blog.talosintelligence.com/content/images/2024/07/data-src-image-ff948216-9532-4cb6-970c-cf6799663bad.png)

A QR code displayed on the Manta phishing site.

## Why should you care?

Understanding and staying vigilant against cryptodrainer scams is important for safeguarding your financial well-being and data security.

These scams, often executed through phishing tactics, pose significant risks to individual's finances and personal information if they are invested at all in cryptocurrency.

By remaining informed about the tactics employed by...