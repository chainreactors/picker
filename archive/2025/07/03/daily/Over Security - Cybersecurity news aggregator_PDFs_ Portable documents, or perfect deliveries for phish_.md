---
title: PDFs: Portable documents, or perfect deliveries for phish?
url: https://blog.talosintelligence.com/pdfs-portable-documents-or-perfect-deliveries-for-phish/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-03
fetch_date: 2025-10-06T23:56:18.710406
---

# PDFs: Portable documents, or perfect deliveries for phish?

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

![](/content/images/2025/06/pdf-brand-impersonation.jpg)

# PDFs: Portable documents, or perfect deliveries for phish?

By
[Omid Mirzaei](https://blog.talosintelligence.com/author/omid/)

Wednesday, July 2, 2025 06:00

[Threat Spotlight](/category/threat-spotlight/)

* Cisco recently developed and released an update to its [brand impersonation](https://blog.talosintelligence.com/from-trust-to-trickery-brand-impersonation/) detection engine for emails. This new update enhances detection coverage and includes a wider range of brands that are delivered using PDF payloads (or attachments).
* A significant portion of email threats with PDF payloads persuade victims to call adversary-controlled phone numbers, displaying another popular social engineering technique known as Telephone-Oriented Attack Delivery (TOAD), also known as callback phishing.
* Talos observed that these threat actors often use Voice over Internet Protocol (VoIP) to remain anonymous. These phone numbers are sometimes reused on consecutive days. Additionally, Talos has identified instances of Adobe platform abuse to deliver PDF attachments to victims in TOAD emails.
* Talos plans to collect and gather intelligence around phone numbers as an additional indicator of compromise (IOC).
* Talos provides new insights into the use of QR codes and PDF annotations in email threats that impersonate legitimate brands through PDF payloads.

---

## Brand impersonation via PDF payload

The portable document format (PDF) is a standard method for sharing information electronically. Files created in other applications (e.g., Microsoft Word) are often converted into this format, which can then be viewed using PDF rendering applications like Adobe Reader, commonly available on most OSs. Thanks to its excellent portability, this file format is widely used for the mass distribution of documents to large audiences. However, in recent months, it has also been exploited for illegitimate purposes, such as brand impersonation.

Brand impersonation is a social engineering technique that exploits the popularity of well-known brands to persuade email recipients to disclose sensitive information. As discussed in [our previous blog](https://blog.talosintelligence.com/from-trust-to-trickery-brand-impersonation/), adversaries can deliver brand logos and names to victims using multiple types of payloads. One of the most common methods of delivering brand logos and names is through PDF payloads (or attachments).

In some cases, the entire email, including a brand’s logo, is embedded within a PDF attachment. Figure 1 displays an example of a QR code phishing email that impersonates the Microsoft Corporation brand. The threat actor used an enticing subject line, “Paycheck Increment,” timed strategically during periods when promotions or merit changes are likely to occur in various organizations.

![](https://blog.talosintelligence.com/content/images/2025/06/1.png)

Figure 1. A QR code phishing email impersonating the Microsoft brand.

In other cases, the company’s logo is included in a separate image or PDF attachment and is displayed to the victim as soon as they open the email. Below is an example of a QR code phishing email that impersonates both the Microsoft and Adobe Inc. brands. Figure 2 shows the Adobe logo attached to an email as an image file.

![](https://blog.talosintelligence.com/content/images/2025/06/2.png)

Figure 2. A QR code phishing email impersonating the Microsoft and Adobe brands.

A brand’s logo may not always be present in every brand impersonation attempt. For example, the following phishing email, which impersonates the Adobe brand, does not include any logos.

![](https://blog.talosintelligence.com/content/images/2025/06/3.png)

Figure 3. A phishing email impersonating the Adobe brand.

When the victim clicks on the “View the Attached online here” hyperlink, they are redirected to a phishing page impersonating a Dropbox, Inc. webpage.

![](https://blog.talosintelligence.com/content/images/2025/06/4.png)

Figure 4. Phishing page impersonating Dropbox download page.

![](https://blog.talosintelligence.com/content/images/2025/06/5.png)

Figure 5. The final phishing page of the above email, impersonating the Dropbox brand.

## Telephone-oriented attack delivery (TOAD)

A significant portion of email threats with PDF payloads persuade victims to call adversary-controlled phone numbers, displaying another popular social engineering technique: telephone-oriented attack delivery (TOAD), also known as callback phishing.

Victims are instructed to call a specific number in the PDF to resolve an issue or confirm a transaction. Once the victim calls, the attacker poses as a legitimate representative and attempts to manipulate them into disclosing confidential information or installing malicious software on their computer.

![](https://blog.talosintelligence.com/content/images/2025/06/pdf-toad-2.jpg)

Figure 6. Overview of a typical TOAD attack sequence.

Phishing typically involves sending emails or messages with malicious links or attachments that direct the victim to a counterfeit website. Callback phishing, however, does not rely on fake websites or phishing links. Instead, attackers use direct voice communication to exploit the victim's trust in phone calls and the perception that phone communication is a secure way to interact with an organization. Additionally, the live interaction during a phone call enables attackers to manipulate the victim's emotions and responses by employing social engineering tactics. Callback phishing is, therefore, a social engineering technique rather than a traditional email threat.

Most phone numbers found in email threats leveraging this social engineering technique are Voice over Internet Protocol (VoIP) numbers, as it is significantly harder to trace a V...