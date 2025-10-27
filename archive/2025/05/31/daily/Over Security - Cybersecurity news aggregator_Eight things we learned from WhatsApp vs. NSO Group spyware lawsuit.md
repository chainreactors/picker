---
title: Eight things we learned from WhatsApp vs. NSO Group spyware lawsuit
url: https://techcrunch.com/2025/05/30/eight-things-we-learned-from-whatsapp-vs-nso-group-spyware-lawsuit/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-31
fetch_date: 2025-10-06T22:27:26.954660
---

# Eight things we learned from WhatsApp vs. NSO Group spyware lawsuit

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

![A warning symbol overlaid on toxic fumes and a Whatsapp logo.](https://techcrunch.com/wp-content/uploads/2018/12/whatsapp-toxic.jpg?w=1024)

**Image Credits:**Bryce Durbin/TechCrunch

[Security](https://techcrunch.com/category/security/)

# Eight things we learned from WhatsApp vs. NSO Group spyware lawsuit

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

9:25 AM PDT · May 30, 2025

On May 6, [WhatsApp scored a major victory against NSO Group](https://techcrunch.com/2025/05/06/nso-group-must-pay-more-than-167-million-in-damages-to-whatsapp-for-spyware-campaign/) when a jury ordered the infamous spyware maker to pay more than $167 million in damages to the Meta-owned company.

The ruling concluded a legal battle spanning more than five years, which started in October 2019 when [WhatsApp accused NSO Group](https://techcrunch.com/2019/10/29/whatsapp-spyware-nso-group/) of hacking more than 1,400 of its users by taking advantage of a vulnerability in the chat app’s [audio-calling functionality](https://techcrunch.com/2019/05/13/whatsapp-exploit-let-attackers-install-government-grade-spyware-on-phones/).

The verdict came after a weeklong jury trial that featured several testimonies, including NSO Group’s CEO Yaron Shohat and WhatsApp employees who responded and investigated the incident.

Even before the trial began, the case had unearthed several revelations, including that NSO Group [had cut off 10 of its government customers](https://techcrunch.com/2024/11/15/nso-group-admits-cutting-off-10-customers-because-they-abused-its-pegasus-spyware-say-unsealed-court-documents/) for abusing its Pegasus spyware, [the locations of 1,223 of the victims](https://techcrunch.com/2025/04/09/court-document-reveals-locations-of-whatsapp-victims-targeted-by-nso-spyware/) of the spyware campaign, and the names of three of the spyware maker’s customers: Mexico, Saudi Arabia, and Uzbekistan.

TechCrunch read more than 1,000 pages of court transcripts of the trial’s hearings. We have highlighted the most interesting facts and revelations below.

## New testimony described how the WhatsApp attack worked

The [zero-click attack](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#zero-click-one-click-attacks), which means the spyware required no interaction from the target, “worked by placing a fake WhatsApp phone call to the target,” as WhatsApp’s lawyer Antonio Perez said during the trial. The lawyer explained that NSO Group had built what it called the “WhatsApp Installation Server,” a special machine designed to send malicious messages across WhatsApp’s infrastructure mimicking real messages.

“Once received, those messages would trigger the user’s phone to reach out to a third server and download the Pegasus spyware. The only thing they needed to make this happen was the phone number,” said Perez.

NSO Group’s research and development vice president Tamir Gazneli testified that “any zero-click solution whatsoever is a significant milestone for Pegasus.”

## NSO admitted that it kept targeting WhatsApp users after the lawsuit was filed

Following the spyware attack, WhatsApp filed its lawsuit against NSO Group in November 2019. Despite the active legal challenge, the spyware maker kept targeting the chat app’s users, according to NSO Group’s research and development vice president Tamir Gazneli.

Gazneli said that “Erised,” the codename for one of the versions of the WhatsApp zero-click vector, was in use from late 2019 up to May 2020. The other versions were called “Eden” and “Heaven,” and the three were collectively known as “Hummingbird.”

## NSO confirms it targeted an American phone number as a test for the FBI

#### Contact Us

Do you have more information about NSO Group, or other spyware companies? From a non-work device and network, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, or email.

For years, NSO Group has claimed that its spyware cannot be used against American phone numbers, meaning any cell number that starts with the +1 country code.

In 2022, [The New York Times first reported](https://www.nytimes.com/2022/01/28/magazine/nso-group-israel-spyware.html) that the company did “attack” a U.S. phone but it was part of a test for the FBI.

NSO Group’s lawyer Joe Akrotirianakis confirmed this, saying the “single exception” to Pegasus not being able to target +1 numbers “was a specially configured version of Pegasus to be used in demonstration to potential U.S. government customers.”

The FBI [reportedly chose](https://www.nytimes.com/2022/11/12/us/politics/fbi-pegasus-spyware-phones-nso.html) not to deploy Pegasus following its test.

## How NSO’s government customers use Pegasus

NSO’s CEO Shohat explained that Pegasus’ user interface for its government customers does not provide an option to choose which hacking method or technique to use against the targets they are interested in, “because customers don’t care which vector they use, as long as they get the intelligence they need.”

In other words, it’s the Pegasus system in the backend that picks out which hacking technology, known as an [exploit](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#exploit), to use each time the spyware targets an individual.

## NSO says it employs hundreds of people

Shohat disclosed a small but notable detail: NSO Group and its parent company, Q Cyber, have a combined number of employees totaling between 350 and 380. Around 50 of these employees work for Q Cyber.

## NSO’s headquarters shares the same building as Apple

In a funny coincidence, NSO Group’s [headquarters](https://www.google.com/maps/place/N.S.O.%2BGroup%2BTechnologies%2Bltd./%4032.1654515%2C34.7735432%2C14z/data%3D%213m1%214b1%214m6%213m5%211s0x151d4912074dc1...