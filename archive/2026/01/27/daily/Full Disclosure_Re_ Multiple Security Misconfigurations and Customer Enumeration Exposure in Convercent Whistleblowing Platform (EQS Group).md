---
title: Re: Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)
url: https://seclists.org/fulldisclosure/2026/Jan/25
source: Full Disclosure
date: 2026-01-27
fetch_date: 2026-01-28T03:35:24.539012
---

# Re: Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# Re: Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)

---

*From*: Marco Ermini via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 23 Jan 2026 18:41:47 +0000

---

```
Hello everyone,

Kindly let me introduce myself. This is the first – and potentially, last – message on this mailing list. I am Marco,
the CISO of EQS Group. Kindly allow me to address some of the statements expressed publicly here.

About the Convercent application

Convercent was acquired by OneTrust in 2021, and in turn, EQS has acquired it from OneTrust at the end of 2024. Before
being acquired by EQS, the Convercent application has not received much love in the latest years, and EQS has since
then proceeded to migrate its customers to the EQS Compliance COCKPIT, which is a modern, supported, and secure SaaS.
The Convercent application is sunset and will be finally switched off by mid of 2026.

Currently, Convercent is supported by EQS on a best-effort basis; despite that, EQS Group has committed to fix all
critical vulnerabilities until the last customer is fully migrated. We want our customers to migrate to our best
service because it is better – not rush them in our new product because what we inherited from an acquisition is
insecure.

The vulnerabilities

The two issues disclosed are either minor in nature or do not constitute vulnerabilities. One was a lack of certain
HTTP headers (some of the reported ones where wrong, but regardless, still hardly something CVE-worthy), and the second
was about an “exposed” API; however, it is public by design as this is how the application works: it is a page where
customers – who have explicitly agreed and signed off to be present – are added to a drop-down list, fed from this
public API. The web page exposes the list of customers by design.

While we may reasonably question whether this page reflects current secure-by-design standards, this brings zero added
risk to any of the EQS customers and Convercent users.

I strongly disagree with the ideas that those “vulnerabilities” could become CVEs – regardless of the status of the
SaaS security and how CVEs are handled. Therefore, we proceeded to ask for their removal from the CVSS database, so not
to alarm our customers with false positives. The responsible CNA agreed immediately to remove them (thank you very
much, VulnCheck!).

Communication with our customers

EQS Group communicates with its customers through established and appropriate channels – notably, our Trust Center –
and not via anonymous mailing lists. Customers have received and will continue to receive all the notifications they
have contractually required to obtain, and where relevant, additional context beyond those obligations.

Customers have received a briefing about the activity happening on this mailing list via our Trust Center.

The status of SaaS Security

As EQS Group is a CNA candidate, we participate and closely follow discussions between MITRE, CISA, and the German BSI,
about vulnerability reporting for SaaS. While we have not heard any news on this front since the last two years, EQS
Group remains committed to aligning with applicable best practices as they evolve.

We believe that meaningful progress in SaaS security is best achieved through structured, collaborative forums with
clear governance, rather than responding to ad-hoc reports of unvetted findings. EQS Group already participates to
proper, professional working groups on SaaS security, for instance through the Cloud Security Alliance. If other
working groups will emerge through any of the official organisms already mentioned, we will certainly participate.

In general, as a principle, CVEs have been created many years ago, at a time where “the Cloud” did not exist in its
current form. They were conceived so that users who procured a software from a development company and installed it on
their system, could be notified when the software they have installed, manifested a security issue. In that way, they
could procure the patch and fix it before a misuse could happen.

Now, except for very particular and edge cases, this is largely inapplicable to SaaS, where there is very little users
can do and solely rely on the Cloud Service Provider to fix any vulnerability. There is almost never any real ground
for a SaaS provider to notify a customer – unless of course a breach has been detected, but in that case we are way
beyond a CVE and we are on a different territory. For a SaaS, even knowing that the application had a bug, does not
help the user in any way. This is why typically CVEs as a concept are not the proper tool to address SaaS
vulnerabilities, and in general, rushing to disclose them only damages the users; a disclosure does not help them in
any way.

Response to the “Responsible" Disclosure

About the “responsible" disclosure: EQS Group receives a significant volume of “vulnerability notifications” like that
one. Almost all of them are low or irrelevant issues from anonymous users looking to make a buck; they are typically
about a missing HTTP headers or lack of optional DNS records. Given the scale of our environment, it can happen that
some record is not updated, but this has little relevance to the security of our platforms. We also cannot always reply
to all those messages, and most of them seem AI or automatically generated.

The notification from “Yuffie Kisaragi” was sent to us on the 4th of December and went to Junk due to the low
reputation of the email used. The author then rushed to obtain two CVE IDs less than two weeks later and subsequently
lost no time posting them on this list.

EQS Group is certainly not perfect, but if these would have been real vulnerabilities, I argue that this would have not
qualified as a “responsible” disclosure by any reasonable standard.

Further communications

EQS Group’s vulnerability handling policy is listed here<https://www.eqs.com/report-a-vulnerability/#handle> –
https://www.eqs.com/report-a-vulnerability/ – and we strongly suggest anyone to read it before they issue a report.

In this regard, we would like to point out the followings:

  1.  For several reasons – legal, commercial, policy, and ethical – EQS Group is unable to respond to requests for
payment of bounties outside of an official bug bounty program.
  2.  EQS Group does nor remunerate bugs that were already discovered internally and were already in resolution.
  3.  EQS Group strongly discourages non-approved, un-vetted testing on EQS Group’s infrastructure. They can and will
be perceived as hostile activity. Testing is encouraged only within officially approved bug bounty programs, in respect
to the established rules of engagement.
  4.  Kindly avoid pointless reports on MTA-STS records, DMARC, quantum ciphers, and other junk like that. It makes our
life easier.

Thank you for your attention.

Best regards / mit freundlichen Grüßen / Cordiali saluti

Dr Marco Ermini (He/Him)
Chief Information Security Officer (CISO)

Marco.Ermini () eqs com<mailto:Marco.Ermini () eqs com;>

[LinkendIn]<https://www.linkedin.com/in/marcoermini/>
Vereinbaren Sie einen Termin mit mir<https://outlook.office365.com/owa...