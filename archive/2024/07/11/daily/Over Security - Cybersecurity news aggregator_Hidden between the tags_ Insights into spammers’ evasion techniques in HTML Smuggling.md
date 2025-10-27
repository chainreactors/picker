---
title: Hidden between the tags: Insights into spammers’ evasion techniques in HTML Smuggling
url: https://blog.talosintelligence.com/hidden-between-the-tags-insights-into-evasion-techniques-in-html-smuggling/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-11
fetch_date: 2025-10-06T17:47:02.504230
---

# Hidden between the tags: Insights into spammers’ evasion techniques in HTML Smuggling

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

![](/content/images/2024/06/html-smuggling.jpg)

# Hidden between the tags: Insights into spammers’ evasion techniques in HTML Smuggling

By
[Omid Mirzaei](https://blog.talosintelligence.com/author/omid/)

Wednesday, July 10, 2024 08:00

[On The Radar](/category/on-the-radar/)

* Cisco Talos has spotted several malicious email campaigns over the past few months that disguise JavaScript code within HTML email attachments, a technique commonly known as “HTML Smuggling.”
* Cisco Talos has noticed that some industry verticals were targeted more than others by email threats using the HTML smuggling technique during the observed time window. For example, companies in the human resources, insurance and healthcare domains were targeted the most, while legal, supply chain and e-commerce companies were among those targeted the least.
* A wide range of evasion techniques has been identified from the senders of these emails, finding ways to get around email gateways and even more advanced detections. These techniques range from various encoding mechanisms to encryption and obfuscation.
* These adversaries use simple methods to increase their chances of success, like playing around with email attachments, as well as more advanced techniques by combining different evasion methods or employing a single evasion method multiple times.
* Talos is releasing a new list of [CyberChef](https://gchq.github.io/CyberChef/) [recipes](https://github.com/Cisco-Talos/HTML_Reversing_Cookbook/tree/main/recipes) that enable faster and easier reversal of encoded JavaScript code contained in the observed HTML attachments. This may assist in creating automation to process and identify such emails for more effective long-term security measures.

## Introduction to HTML smuggling

HTML smuggling is a technique used by attackers to embed encoded or encrypted JavaScript code within HTML attachments or web pages. This technique has been used extensively in spear phishing email campaigns over the past few months. HTML smuggling is quite effective in bypassing perimeter security controls such as email gateways and web proxies for two main reasons: It abuses the legitimate features of HTML5 and JavaScript, and it leverages different forms of encoding and encryption.

Threat actors start by sending one or more emails with URLs or HTML attachments to their targets. When the recipient clicks on the URL or opens the attachment, the browser decodes and runs all encoded JavaScript code automatically, which will eventually download and deliver the malware to the victim’s device, or alternatively, redirect the user to the final phishing page. In some cases, the code for the malware is embedded in the HTML attachment, and the JavaScript code simply reconstructs and runs it without needing additional downloads.

## Reversing the HTML attachments

Security researchers should continuously monitor changes in threat actors’ techniques and update their detection logic and/or processes to make sure customers stay protected. Reverse engineering tools could be helpful for several reasons because they help security analysts better understand attackers’ techniques, especially those that are used to help them stay under the radar. They could be used to update the logic in detection rules or feature extraction processes for more advanced detection solutions that rely on machine learning.

By sharing the insights gained from reverse engineering with the broader cybersecurity community, organizations can contribute to collective threat intelligence efforts, helping others to prepare for and defend against similar attacks.

[CyberChef](https://www.gchq.gov.uk/news/cyberchef-cyber-swiss-army-knife) is a powerful open-source web application developed by [Government Communications Headquarters (GCHQ)](https://www.gchq.gov.uk/) that facilitates the decoding and decryption of JavaScript code in HTML attachments. It provides a variety of modules (or functions) for decoding and decryption that can be combined to build up a “recipe.” These recipes can then be exported in different formats and loaded later to be used elsewhere. A snippet of an HTML attachment is shown below.

![](https://blog.talosintelligence.com/content/images/2024/06/data-src-image-78e03d4d-1f1f-45cc-9573-633636835c4f.png)

A snippet of an HTML attachment with base64-encoded string within a script tag.

This attachment contains an encoded string in JavaScript that can be decoded using a base64-decoding function. The URL is defanged to avoid being opened by the readers by mistake.

![](https://blog.talosintelligence.com/content/images/2024/06/data-src-image-211f889c-4b15-4faf-9b49-d53cf2b6fadc.png)

An encoded string and its decoded equivalent using the “From Base64” function in CyberChef.

Talos is releasing [new recipes](https://github.com/Cisco-Talos/HTML_Reversing_Cookbook/tree/main/recipes) that security researchers can use to reverse encoded and/or encrypted JavaScript code in HTML attachments. Alternatively, these recipes could be integrated into automated feature extraction processes to improve the detection of emails containing HTML attachments. We will also share recipes that are not referenced in this blog post but have been used frequently to reverse HTML attachments. The combinations captured by these recipes show which evasion techniques threat actors use most often.

## A dive into evasion techniques

Talos has been closely monitoring email campaigns that leverage HTML smuggling over the past several months. Various evasion techniques have been identified, which threat actors use to bypass email gateways, ranging from different encoding mechanisms to encryption. In some instances, evasion techniques are chained together, but in others, a single method is employed multiple times to increase the challenge of detection. Additional...