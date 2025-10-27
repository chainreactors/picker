---
title: Lower email spoofing incidents (and make your marketing team happy) with BIMI
url: https://blog.nviso.eu/2022/12/13/lower-email-spoofing-incidents-and-make-your-marketing-team-happy-with-bimi/
source: NVISO Labs
date: 2022-12-14
fetch_date: 2025-10-04T01:23:17.977571
---

# Lower email spoofing incidents (and make your marketing team happy) with BIMI

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Lower email spoofing incidents (and make your marketing team happy) with BIMI

[Karsten De Baere](https://blog.nviso.eu/author/karsten-de-baere/ "Posts by Karsten De Baere")

[Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/), [Blue Team](https://blog.nviso.eu/category/blue-team/)

December 13, 2022December 13, 2022
4 Minutes

## Introduction

Over the last couple of years, we saw the amount of phishing attacks skyrocket. According to F5, a multi-cloud security and application provider, there was a 220% increase of incidents during the height of the global pandemic compared to the yearly average. It’s expected that every year there will be an additional increase of 15% in phishing attempts, making it one of the most threatening security risks for a company’s IT department.

## Email Spoofing

While several malicious actors try to target an employee with an email from what looks like a (very) legitimate domain, there are also a lot of email spoofing incidents, which are more difficult to distinguish from non-phishing emails for the target employee. Its goal is to fool users into believing that the message comes from a person or entity they either know or can trust. The sender sends an email using forged email headers to convince an email client software of the legitimacy of the message. By examining the header of the mail closely, it is possible to find the false address. But many users will not suspect a fraudulent email from the sender he knows. So, they can easily click malicious links or send sensitive data without considering the risks involved.

## SPF, DKIM and DMARC

There are several known frameworks to prevent email spoofing, and these are already commonly used by businesses: SPF, DKIM and DMARC. This to the extent that some mail servers will reject emails that do not comply with these frameworks.

Sender Policy Framework (SPF) works by verifying the identity of the sender of an email by comparing the sender’s IP address to a list of authorized IP addresses that are published in the domain’s DNS records.

With DomainKeys Identified Mail (DKIM), a digital signature is attached to the email which can be used by the recipient to verify the authenticity of the sender.

And finally, Domain-based Message Authentication, Reporting, and Conformance (DMARC). By building on the SPF and DKIM standards, it provides a more comprehensive approach to email authentication. DMARC allows the owner of a domain to publish a policy in their DNS records that specifies which mechanisms are used to authenticate emails sent from their domain, and what to do if an email fails authentication.

When correctly configuring your DNS, you can already go a long way into lowering the chances of a spoofing attempt. But there is still the low risk of messages with malicious links arriving in the inbox of the receiver or legitimate mails being flagged as spam and eventually deleted. By setting up BIMI, you can have that extra security layer while giving your sent emails more exposure with your brand logo.

## What is BIMI?

BIMI (Brand Indicators for Message Identification) is a recently (2020) introduced email standard, which makes use of the brand logo of the business as a security control. When configured correctly, client mail software can verify the legitimacy of the received mail by comparing it with the BIMI record in the DNS of the sender.

![BIMI-group logo](https://blog.nviso.eu/wp-content/uploads/2022/12/bimi_square2.png)

## Preparation for BIMI

When setting up BIMI you need to correctly configure SPF, DKIM and DMARC. Otherwise, the receiver mail software will already fail verification before it even checks the added brand logo. This means:

* Email service providers are added to the SPF record and set to hard fail (‘-all’)
* DKIM is configured for all the email service providers and the public key is reachable
* DMARC is fine-tuned. Recommended is to have the policy set on quarantine or reject, and pct to 100.

So, make sure these are checked and analyse the DMARC reports before implementing BIMI.

At the moment of writing this blog, there is still a limited list of mailbox providers that supports the implementation and verification of BIMI. Google and Apple mail are one of the most used providers in this list ([Link](https://bimigroup.org/bimi-infographic/)), but many will join in the future as BIMI will become a more commonly used standard. Noticeably, Microsoft (Outlook) has not even considered to implement the email standard.

![BIMI Example in Gmail Inbox](https://blog.nviso.eu/wp-content/uploads/2022/12/Screenshot_20221205_214524_Gmail-1024x960.jpg)

## BIMI Setup

The majority of the work is creating the [BIMI SVG Logo files](https://bimigroup.org/creating-bimi-svg-logo-files/). We recommend using an SVG formatted file which is hosted publicly and can be accessed via HTTPS. It can help to use the [SVG conversion tool](https://bimigroup.org/svg-conversion-tools-released/) from the BIMI-group.

When the SVG is in place, you can add the DNS record which begins with the tag “v=BIMI1” and includes the parameter “l=logoURL” where you fill in the link to your externally accessible logo. You can use the [BIMI Inspector](https://bimigroup.org/bimi-generator/), which generates a record for you.

Optionally you can use VMC (Verified Mark Certificate), a proof that you own the trademark for your brand logo. By adding this you increase the legitimacy, but this isn’t required yet. This is included in the DNS record together with the URL pointing to the logo’s location.

## Conclusion

Now you know what BIMI is, why should you consider configuring this email standard? There are two major reasons:

1. It providers extra security against email spoofing
2. it makes your sent mails standout between all the other marketing mails.

If you want more info on the standard, we recommend checking the website of the group: <https://bimigroup.org/>

## About the author

![Karsten De Baere](https://blog.nviso.eu/wp-content/uploads/2022/12/De-Baere-Karsten-202200304_Edit.jpg)

Karsten De Baere

Karsten is a Senior Security Consultant in the Cyber Strategy and Architect team at NVISO. He assists organisation with assessing and implementing new practices in the SSDLC. In his off time, Karsten likes to do extensive research on new security topics and play with the latest automation gadgets.

[LinkedIn]...