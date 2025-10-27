---
title: Malicious QR Codes How big of a problem is it, really
url: https://blog.talosintelligence.com/malicious_qr_codes/
source: Instapaper: Unread
date: 2024-11-22
fetch_date: 2025-10-06T19:23:10.583706
---

# Malicious QR Codes How big of a problem is it, really

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

# Malicious QR Codes: How big of a problem is it, really?

By
[Jaeson Schultz](https://blog.talosintelligence.com/author/jaeson-schultz/)

Wednesday, November 20, 2024 06:00

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

* QR codes are disproportionately effective at bypassing most anti-spam filters, as most filters are not designed to recognize that a QR code is present in an image and decode the QR code. According to Cisco Talos’ data, roughly 60% of all email containing a QR code is spam.
* Talos discovered two effective methods for defanging malicious QR codes, a necessary step to make them safe for consumption. Users could obscure the data modules, the black and white squares within the QR code that represent the encoded data. Alternatively, users could remove one or more of the position detection patterns — large square boxes located in corners of the QR code used to initially identify the code's orientation and position.
* Further complicating detection, both by users and anti-spam filters, Talos found QR code images that are “QR code art.” These images blend the data points of a QR code seamlessly into an artistic image so the result does not appear to be a QR code at all.

Prior to 1994, most code scanning technology utilized one-dimensional barcodes. These one-dimensional barcodes consist of a series of parallel black lines of varying width and spacing. We are all familiar with these codes, like the type you might find on the back of a cereal box from the grocery store. However, as the use of barcodes increased, their limitations became problematic, especially considering that a one-dimensional barcode can only hold up to 80 alphanumeric characters of information. To eliminate this limitation, a company named Denso Wave created the very first “Quick Response“ codes (QR codes).

QR codes are a two-dimensional matrix bar code that can encode just over 7,000 numeric characters, or up to approximately 4,300 alphanumeric characters. While they can represent almost any data, most frequently we encounter QR codes that are used to encode URLs.

# Quantifying the QR code problem

Talos extracts QR codes from images inside email messages and attached PDF files for analysis. QR codes in email messages make up between .01% and .2% of all email worldwide. This equates to roughly one out of every 500 email messages. However, because QR codes are disproportionately effective at bypassing anti-spam filters, a significant number find their way into users’ email inboxes, skewing users’ perception of the overall problem.

Also, of course, not all email messages with a QR code inside are spam or malicious. Many email users send QR codes as part of their email signature, or you may also find legitimate emails containing QR codes used as signups for events, and so on. However, according to Talos’ data, **roughly 60% of all email containing a QR code is spam**.

Truly malicious QR codes can be found in a much smaller number of messages. These emails contain links to phishing pages, etc. The most common malicious QR codes tend to be multifactor authentication (MFA) requests used for phishing user credentials.

![](https://blog.talosintelligence.com/content/images/2024/11/Screenshot-2024-11-05-at-14.39.07.png)

An example MFA phishing email utilizing a QR code.

One of the problems that defenders may encounter when dealing with users’ scanning of QR codes received via email, assuming the user’s device is not connected to the corporate wi-fi, is that subsequent traffic between the victim and the attacker will traverse the cellular network, largely outside the purview of corporate security devices. This can complicate defense, because few/no alerts from security devices will notify security teams that this has occurred.

# Why are malicious QR codes hard to detect?

Because QR codes are displayed in images, it can be difficult for anti-spam systems to identify problematic codes. Identifying and filtering these messages requires the anti-spam system to recognize that a QR code is present in an image, decode the QR code, then analyze the link (or other data) present in the decoded data. As spammers are always looking for innovative ways to bypass spam filters, using QR codes has been a valuable technique for spammers to accomplish this.

As anti-spam systems improve their capability to detect malicious QR codes in images, enterprising attackers have instead decided to craft their QR codes using Unicode characters.

![](https://blog.talosintelligence.com/content/images/2024/11/DHL-QR-unicode.png)

**An email containing a QR code constructed from Unicode characters (defanged).**

The graphical parts of the image are contained within a PDF file. The PDF metadata indicates it was created from HTML using the tool wkhtmltopdf. Converting the PDF back into HTML shows the Unicode that is being used to construct the QR code.

![](https://blog.talosintelligence.com/content/images/2024/11/Screenshot-2024-11-01-at-11.26.41.png)

**HTML used to construct a malicious QR Code from Unicode characters.**

# Defanging QR codes

When sharing malicious URLs, it is common to change the protocol from “http” to “hxxp”, and/or to add brackets (“[]”) around one of the dots in the URL. This makes it so browsers and other applications do not render the link as an active URL, ensuring that users do not inadvertently click on the malicious URL. This is a process known as “defanging.” Unfortunately, while defanging URLs is commonplace, many people do not defang malicious QR codes. For example, below is a [news article from BBC](https://www.bbc.com/news/articles/clynnkrgj24o) about criminals who put QR code stickers on parking meters in an attempt to harvest payment credentials from unsuspecting victims.

![](https://blog.talosintelligence.com/content/imag...