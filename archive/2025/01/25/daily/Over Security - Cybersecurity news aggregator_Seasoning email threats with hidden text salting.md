---
title: Seasoning email threats with hidden text salting
url: https://blog.talosintelligence.com/seasoning-email-threats-with-hidden-text-salting/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-25
fetch_date: 2025-10-06T20:12:43.302348
---

# Seasoning email threats with hidden text salting

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

![](/content/images/2024/12/hiddentextsalting_header.jpg)

# Seasoning email threats with hidden text salting

By
[Omid Mirzaei](https://blog.talosintelligence.com/author/omid/)

Friday, January 24, 2025 08:37

[Threats](/category/threats/)
[Threat Spotlight](/category/threat-spotlight/)

* Cisco Talos observed an increase in the number of email threats leveraging hidden text salting (also known as "poisoning") in the second half of 2024.
* Hidden text salting is a simple yet effective technique for bypassing email parsers, confusing spam filters, and evading detection engines that rely on keywords. The idea is to include some characters into the HTML source of an email that are not visually recognizable.
* Talos observed this technique being used for various purposes, including evading brand name extraction by email parsers, confusing language detection procedures, and evading spam filters and detection engines in HTML smuggling.

## Introduction to hidden text salting

Hidden text salting (or "poisoning") is an effective technique employed by threat actors to craft emails that can evade parsers, confuse spam filters, and bypass detection systems that rely on keywords. In this approach, features of the Hypertext Markup Language (HTML) and Cascading Style Sheets (CSS) are used to include comments and irrelevant content that are not visible to the victim when the email is rendered in an email client but can impact the efficacy of parsers and detection engines.

Due to the simplicity of hidden text salting and the number of ways threat actors can insert gibberish content in emails, this approach can introduce significant challenges to email parsers, spam filters, and detection engines.

## Technical explanation

Talos has observed the use of hidden text salting for multiple purposes, such as evading brand name extraction by email parsers. Below is an example of a phishing email that impersonates the Wells Fargo brand.

![](https://blog.talosintelligence.com/content/images/2024/12/image-2.png)

A phishing email impersonating the Wells Fargo brand.

The HTML source of the above email is shown below. The **<style>** tag is used to define style information for an email via CSS. Inside the **<style>** element, one can specify how HTML elements should render in a browser or email client. The **<style>** element must be included inside the **<head>** section of the document. In this example, threat actors have set the **display** property to **inline-block**. When **inline-block** is used instead of **inline**, one can set a width and height on the element. In this case, the block’s width is set to zero. Additionally, the **overflow** property is set to “hidden,” resulting in the content outside the element box not being shown to the victim when the email is rendered in the email client.

![](https://blog.talosintelligence.com/content/images/2024/12/image-3.png)

The HTML source snippet of the above phishing email shows how the 'width' property in CSS is used to hide the irrelevant characters inserted between the letters of the Wells Fargo brand.

As a second example, the following email shows a phishing email, sent to another customer, that impersonates the Norton LifeLock brand.

![](https://blog.talosintelligence.com/content/images/2024/12/image-4.png)

A phishing email impersonating the Norton LifeLock brand.

In this case, threat actors have inserted Zero-Width SPace (ZWSP) and Zero-Width Non-Joiner (ZWNJ) characters between the letters of Norton LifeLock to evade detection. Although these characters are not visible to the naked eye, they are still considered characters or strings of characters by most email parsers. Therefore, one can consider them invisible characters.

![](https://blog.talosintelligence.com/content/images/2024/12/image-5.png)

The HTML source snippet of the above phishing email, with Zero-Width SPace (ZWSP) and Zero-Width Non-Joiner (ZWNJ) characters inserted between the letters of the Norton LifeLock brand.

Hidden text salting has also been used to confuse language detection procedures, thus evading possible spam filters that rely on such procedures. The example below shows a phishing email that impersonates the Harbor Freight brand. As it is visually obvious, the language of this email is English.

![](https://blog.talosintelligence.com/content/images/2024/12/image-6.png)

A phishing email impersonating the Harbor Freight brand.

However, a closer inspection of the email’s headers shows that the language of this email has been identified as French, as it is saved in the [**LANG** field](https://learn.microsoft.com/en-us/defender-office-365/message-headers-eop-mdo#x-microsoft-antispam-message-header-fields) of Microsoft's **X-Forefront-Antispam-Report anti-spam** header. The LANG field specifies the language in which the message was written, and the **X-Forefront-Antispam-Report** header contains information about the message and how it was processed. This header is added to each message by [Exchange Online Protection (EOP)](https://learn.microsoft.com/en-us/defender-office-365/eop-about), Microsoft's cloud-based filtering service.

![](https://blog.talosintelligence.com/content/images/2024/12/image-7.png)

A snippet of the above email’s header shows French as the identified language of this email by Microsoft's cloud-based filtering service, called EOP.

When the HTML source of this email is inspected, several French words and sentences are found that are visually hidden. In this case, threat actors have used the **display** property of the **div** element to hide the French words, thus confusing the language detection module of Microsoft.

![](https://blog.talosintelligence.com/content/images/2024/12/image-8.png)

The HTML source snippet of the above phishing email, with French characters that are hidden using the d...