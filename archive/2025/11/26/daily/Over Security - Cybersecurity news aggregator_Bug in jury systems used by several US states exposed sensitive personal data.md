---
title: Bug in jury systems used by several US states exposed sensitive personal data
url: https://techcrunch.com/2025/11/26/bug-in-jury-systems-used-by-several-us-states-exposed-sensitive-personal-data/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-26
fetch_date: 2025-11-27T03:12:50.535242
---

# Bug in jury systems used by several US states exposed sensitive personal data

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-lockup.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)
* [Disrupt 2025](https://techcrunch.com/events/tc-disrupt-2025/)

* [Events](/events/)
* [Podcasts](/podcasts/)
* [Newsletters](/newsletters/)

Search

Submit

Site Search Toggle

Mega Menu Toggle

### Topics

[Latest](/latest/)

[AI](/category/artificial-intelligence/)

[Amazon](/tag/amazon/)

[Apps](/category/apps/)

[Biotech & Health](/category/biotech-health/)

[Climate](/category/climate/)

[Cloud Computing](/tag/cloud-computing/)

[Commerce](/category/commerce/)

[Crypto](/category/cryptocurrency/)

[Enterprise](/category/enterprise/)

[EVs](/tag/evs/)

[Fintech](/category/fintech/)

[Fundraising](/category/fundraising/)

[Gadgets](/category/gadgets/)

[Gaming](/category/gaming/)

[Google](/tag/google/)

[Government & Policy](/category/government-policy/)

[Hardware](/category/hardware/)

[Instagram](/tag/instagram/)

[Layoffs](/tag/layoffs/)

[Media & Entertainment](/category/media-entertainment/)

[Meta](/tag/meta/)

[Microsoft](/tag/microsoft/)

[Privacy](/category/privacy/)

[Robotics](/category/robotics/)

[Security](/category/security/)

[Social](/category/social/)

[Space](/category/space/)

[Startups](/category/startups/)

[TikTok](/tag/tiktok/)

[Transportation](/category/transportation/)

[Venture](/category/venture/)

### More from TechCrunch

[Staff](/about-techcrunch/)

[Events](/events/)

[Startup Battlefield](/startup-battlefield/)

[StrictlyVC](https://strictlyvc.com/)

[Newsletters](/newsletters/)

[Podcasts](/podcasts/)

[Videos](/video/)

[Partner Content](/sponsored/)

[TechCrunch Brand Studio](/brand-studio/)

[Crunchboard](https://www.crunchboard.com/)

[Contact Us](/contact-us/)

![Concept illustration depicting messy litigation with an illustrated gavel on a multicolored background](https://techcrunch.com/wp-content/uploads/2023/11/gavel-messy-legal.jpg?w=1024)

**Image Credits:**Bryce Durbin / TechCrunch

[Security](https://techcrunch.com/category/security/)

# Bug in jury systems used by several US states exposed sensitive personal data

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

8:00 AM PST · November 26, 2025

Several public websites designed to allow courts across the United States and Canada to manage the personal information of potential jurors had a simple security flaw that easily exposed their sensitive data, including names and home addresses, TechCrunch has exclusively learned.

A security researcher, who asked not to be named for this story, contacted TechCrunch with details of the easy-to-exploit vulnerability, and identified at least a dozen juror websites made by government software maker Tyler Technologies that appear to be vulnerable, given that they run on the same platform.

The sites are all over the country, including California, Illinois, Michigan, Nevada, Ohio, Pennsylvania, Texas, and Virginia.

Tyler told TechCrunch that it is fixing the flaw after we alerted the company to the information exposures.

The bug meant it was possible for anyone to obtain the information about jurors who are selected for service. To log into these platforms, a juror is provided a unique numerical identifier assigned to them, which could be [brute-forced](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#brute-force) since the number was sequentially incremental. The platform also did not have any mechanism to prevent anyone from flooding the login pages with a large number of guesses, a feature known as “rate-limiting.”

In early November, the security researcher told TechCrunch that they identified at least one jury management portal for a county in Texas as vulnerable. Inside that portal, TechCrunch saw full names, dates of birth, occupation, email addresses, cell phone numbers, and home and mailing addresses.

Other exposed data included information shared in the questionnaires that potential jurors are required to fill out to see if they are qualified to serve on a jury.

In the portal seen by TechCrunch, the questions asked about the person’s gender, ethnicity, education level, employer, marital status, children, if the person was a citizen, whether they were older than 18, and whether they have been convicted or faced indictment for a theft or felony.

The vulnerability could have exposed personal health data inside a juror’s profile in some cases. For example, if a juror had requested to be exempted from service for health reasons, they may have disclosed what medical reason they think disqualifies them. TechCrunch saw an example of that, too.

#### Contact Us

Do you have more information about vulnerabilities in Tyler Technologies’ products? Or other government tech? From a non-work device, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or email.

TechCrunch alerted Tyler of the issue on November 5. Tyler acknowledged the vulnerability on November 25.

In a statement, Tyler spokesperson Karen Shields said that the company’s security team confirmed “a vulnerability exists where some juror information may have been accessible via a brute force attack.”

“We have developed a remediation to prevent unauthorized access and are communicating next steps with our clients,” the statement said.

The spokesperson did not respond to a series of follow-up questions, including whether Tyler has the technical means to determine if there was any malicious access to jurors’ personal information, and whether it plans to notify people whose data was exposed.

This is not the first time Tyler left sensitive personal data exposed on the internet. In 2023, a security researcher found that, due to a separate security flaw, [some U.S. online court record systems exposed sealed, confidential, and sensitive data](https://techcrunch.com/2023/11/30/us-court-records-systems-vulnerabilities-exposed-sealed-documents/), such as witness lists and testimony, mental health evaluations, detailed allegations of abuse, and corporate trade secrets.

In that case, Tyler fixed vulnerabilities in its Case Management System Plus product, which was used across the state of Georgia.

Two other government technology providers were exposing data in that case: Catalis, through its CMS360 product, a system used across several U.S. states; and Henschen & Associates, through its CaseLook court record system, used in Ohio.

Topics

[cybersecurity](https://techcrunch.com/tag/cybersecurity/), [Exclusive](https://techcrunch.com/tag/exclusive/), [information security](https://techcrunch.com/tag/information-security/), [infosec](https://techcrunch.com/tag/infosec/), [judiciary](https://techcrunch.com/tag/judiciary/), [Security](https://techcrunch.com/category/security/), [security vulnerability](https://techcrunch.com/tag/security-vulnerability/), [Tyler](https://techcrunch.com/tag/tyler/), [Tyler Technologies](https://techcrunch.com/tag/tyler-technologies/)

![Lorenzo Franceschi-Bicchierai](https://techcrunch.com/wp-content/uploads/2025/07/Lorenzo-headshot-2023-cropped.jpeg?w=150)

Lorenzo Franceschi-Bicchierai

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Writer at TechCrunch, where he covers hacking, cybersecurity, surveillance, and privacy.

You can contact or verify outreach from Lorenzo by emailing lorenzo@techcrunch.com, via encrypted message at +1 917 257 1382 on Signal, and @lorenzofb on Keybase/Telegram.

[View Bio](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

![Event Logo](https://techcrunch.c...