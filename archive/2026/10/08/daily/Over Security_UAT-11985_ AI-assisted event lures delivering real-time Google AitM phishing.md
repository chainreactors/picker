---
title: UAT-11985: AI-assisted event lures delivering real-time Google AitM phishing
url: https://blog.talosintelligence.com/uat-11985/
source: Over Security
date: 2026-10-08
fetch_date: 2026-10-09T08:12:07.754964
---

# UAT-11985: AI-assisted event lures delivering real-time Google AitM phishing

[Blog](/)

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

# UAT-11985: AI-assisted event lures delivering real-time Google AitM phishing

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Thursday, October 8, 2026 06:01

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[AI](https://blog.talosintelligence.com/category/ai/)
[APT](https://blog.talosintelligence.com/category/apt/)

* Cisco Talos identified an advanced persistent threat (APT) spear-phishing campaign against individuals affiliated with Taiwan research organizations. The operation leveraged legitimate public event themes and impersonated reputable academic and policy institutions to establish credibility.
* The phishing emails exhibited highly consistent structure, rhetoric, and personalization patterns, suggesting the threat actor likely used AI-assisted content generation to rapidly customize invitation lures for different targets while maintaining a common social engineering framework.
* Beyond traditional email phishing, the actor incorporated QR code phishing (quishing) techniques by modifying legitimate event posters with malicious QR codes, expanding the attack surface beyond email recipients to secondary victims who may encounter printed materials.
* The campaign deployed an advanced adversary-in-the-middle (AitM) phishing framework that impersonated Google authentication pages and utilized a hybrid HTTP and WebSocket architecture to synchronize authentication workflows in real time, enabling the interception of credentials and multi-factor authentication (MFA) challenges.
* After technical analysis of the phishing kit, Talos assesses with moderate confidence that the user interface was originally developed in Simplified Chinese and later adapted for Traditional Chinese and English. The localization architecture, Simplified Chinese default language branch, and mainland-Chinese lexical usage collectively suggest a developer whose primary working language is Simplified Chinese.

---

In mid-2026, Talos observed an APT spear-phishing campaign targeting Taiwan-based research organizations. The threat actor appeared to reuse legitimate or plausible public event information, then embedded a hyperlink to actor-controlled infrastructure, while the displayed URL appeared benign. Several invitation emails exhibited nearly identical syntactic structures despite discussing different geopolitical topics, suggesting the content was generated from a reusable prompt template rather than independently authored. While Talos cannot conclusively determine whether the emails were fully generated by a large language model (LLM), the campaign demonstrates strong evidence of AI-assisted content production and personalization.

## Spear-phishing mail

Based on the phishing emails we observed, the threat actor impersonated legitimate institutions in Taiwan such as Taiwan European Union Centre, NCCU Institute of International Relations, and Taiwan Research Institute. Below is a deep analysis of the mail contents.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/fig1.png)

Figure 1. Impersonated Taiwan European Union Centre [event](https://www.eutw.org.tw/article_show/m/19/s/77?l=tw&id=2447).

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/fig2.png)

Figure 2. Impersonated NCCU Institute of International Relations [event](https://www.facebook.com/nccuiir/photos/-%E5%8D%97%E6%B5%B7%E4%BB%B2%E8%A3%81%E6%A1%88%E5%8D%81%E5%B9%B4%E5%BE%8C%E5%9C%8B%E9%9A%9B%E6%B3%95%E8%88%87%E6%B5%B7%E6%B4%8B%E7%A7%A9%E5%BA%8F%E7%9A%84%E5%86%8D%E5%BB%BA%E6%A7%8B2016%E5%B9%B47%E6%9C%8812%E6%97%A5%E5%8D%97%E6%B5%B7%E4%BB%B2%E8%A3%81%E6%A1%88%E8%A3%81%E6%B1%BA%E5%87%BA%E7%88%90%E5%B0%8D%E8%81%AF%E5%90%88%E5%9C%8B%E6%B5%B7%E6%B4%8B%E6%B3%95%E5%85%AC%E7%B4%84%E7%9A%84%E8%A7%A3%E9%87%8B%E8%88%87%E9%81%A9%E7%94%A8%E5%B3%B6%E7%A4%81%E5%9C%B0%E4%BD%8D%E6%AD%B7%E5%8F%B2%E6%80%A7%E6%AC%8A%E5%88%A9%E4%B8%BB%E5%BC%B5%E5%B0%88%E5%B1%AC%E7%B6%93%E6%BF%9F%E5%8D%80%E6%AC%8A%E5%88%A9%E7%BE%A9%E5%8B%99%E4%BB%A5%E5%8F%8A%E5%8D%80%E5%9F%9F%E6%B5%B7/1521637003086346/).

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/fig3.png)

Figure 3. Impersonated Taiwan Research Institute [event](http://www.tnef.org.tw/upload/events/20260706144552.pdf).

An email recipient contacted the organizations concerned to verify the purported senders. However, none of the organizations could confirm that the three senders were employees or representatives of the institutions named in the emails. This suggests that the threat actor fabricated the sender identities while using legitimate organizational names and publicly available event information as cover.

All three emails follow a highly consistent, three-part structure, indicating the use of a common template. The opening section provides a polished (but overly elaborate) description of the geopolitical or policy context. It relies heavily on grandiose yet vague expressions such as “the global strategic landscape,” “reshaping the great-power order,” “three-dimensional analysis,” “forward looking and in-depth analysis,” and “high intensity professional dialogue” to create an impression of academic authority and subject matter expertise. Although the language is generally fluent, the excessive use of policy jargon and abstract strategic terminology makes the content appear formulaic.

The second section is customized for the recipient and uses targeted flattery to encourage engagement. Similar phrases including “admiration,” “authoritative perspective,” “highly perceptive,” and “key practical dimensions” appear across the three messages. These compliments are broadly applicable and contain few verifiable details about the recipient’s actual work, suggesting that the actor personalize...