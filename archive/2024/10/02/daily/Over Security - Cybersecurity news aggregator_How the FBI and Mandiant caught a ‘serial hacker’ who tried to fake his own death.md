---
title: How the FBI and Mandiant caught a ‘serial hacker’ who tried to fake his own death
url: https://techcrunch.com/2024/10/01/how-the-fbi-and-mandiant-caught-a-serial-hacker-who-tried-to-fake-his-own-death/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-02
fetch_date: 2025-10-06T18:55:50.760172
---

# How the FBI and Mandiant caught a ‘serial hacker’ who tried to fake his own death

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

![An illustration of Jesse Kipf's mugshot. Kipf plead guilty to hacking several U.S. states death registry systems to fake his own death.](https://techcrunch.com/wp-content/uploads/2024/09/jesse-kipf-hacker-faked-death.jpg?w=1024)

**Image Credits:**Bryce Durbin/TechCrunch

[Security](https://techcrunch.com/category/security/)

# How the FBI and Mandiant caught a ‘serial hacker’ who tried to fake his own death

## Jesse Kipf was a prolific hacker who sold access to systems he hacked, had contacts with a notorious cybercrime gang, and tried to use his hacking skills to get off the grid for good.

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

8:00 AM PDT · October 1, 2024

In the early hours of January 20, 2023, a doctor’s user account logged onto the Hawaii Electronic Death Registration System from out of state to certify the death of a man named Jesse Kipf. The death certificate listed the cause as “acute respiratory distress syndrome” due to COVID-19 a week earlier. And with that, Kipf was unceremoniously registered as deceased in several government databases.

On the same day, a hacker nicknamed “FreeRadical” posted the same death certificate on a hacking forum in an attempt to monetize the access they had to the system. “Access level is medical certifier which means you can create and certify a death in this panel,” the hacker wrote.

In the post, the hacker included a partial screenshot of the fake death certificate, but they also made a critical mistake. FreeRadical forgot to redact the purported state of birth of the person in the death certificate and left a small part of the state government’s seal showing in the corner of the screenshot.

On the other side of the country in Colorado, Austin Larsen, a senior threat analyst at Google’s cybersecurity firm Mandiant, along with his colleagues, spotted the post online as part of their routine threat intelligence gathering, which includes monitoring cybercrime forums. By homing in on the badly cropped screenshot of the fake death certificate, Larsen and his colleagues realized the forum post was evidence FreeRadical had hacked the U.S. state government of Hawaii.

Three days after finding the hacking forum post, Larsen notified Hawaii state officials that its government systems had been hacked.

“It is likely the actor compromised a medical certifier account,” the notification read, according to a screenshot of Larsen’s message shared with TechCrunch in an interview earlier in September.

Larsen’s warning set in motion a federal investigation that would reveal that the doctor’s user account used to file the death certificate was compromised by none other than Jesse Kipf himself, the person who had supposedly died. Prosecutors would later allege in a court document that Kipf faked his own death to avoid paying his ex-wife around $116,000 owed to support their daughter.

Kipf, whom prosecutors later called a “serial hacker” with “ample technical knowledge towards making a living by stealing from others,” had made a series of mistakes, including using his home internet from Somerset, Kentucky, to directly connect to the Hawaii death registration system, which eventually led federal agents right to his door.

As a result, the U.S. Department of Justice [criminally charged](https://www.justice.gov/usao-edky/pr/pulaski-county-man-indicted-cyber-intrusion-identity-theft-and-bank-fraud) Kipf in late November 2023 with a series of hacking crimes. Kipf, prosecutors alleged, had hacked computer systems belonging to three U.S. states, as well as two vendors of large hotel chains. The Department of Justice’s press release, as well as the indictment published at the same time, did not include many of the details that prosecutors had claimed Kipf had done. [Forbes had reported](https://www.forbes.com/sites/thomasbrewster/2023/11/17/hacker-faked-his-own-death-then-claimed-to-have-sold-marriott-customer-data-to-russians-fbi-says/) a few days earlier that Kipf allegedly hacked the Hawaii Department of Health.

Earlier in September, Mandiant’s Larsen, along with FBI Special Agent Andrew Satornino, and Assistant U.S. Attorney for the Eastern District of Kentucky Kate Dieruf, sat down with TechCrunch to reveal how they found Kipf and brought him to justice. The three spoke to TechCrunch ahead of a talk they gave at the Mandiant cybersecurity conference, mWISE.

Kipf, according to Larsen, Satornino, and Dieruf, as well as the court documents of his case, was a prolific hacker with multiple identities.

Satornino said Kipf was an “initial access broker,” meaning a hacker who breaks into systems and then tries to sell access to those systems to other cybercriminals. In affidavits supporting search warrants against Kipf, the FBI special agent wrote that Kipf had committed credit card fraud to purchase food from food delivery services — and was arrested for it in 2022; used fake Social Security numbers to apply for loans; had more than a dozen U.S. driver’s licenses on his computer; and had hacked Marriott hotel vendors.

Kipf likely got the credentials he used in the Hawaii hack from an information-stealing malware that infected the unnamed doctor’s computer, which then ended up on a Telegram channel for hackers. Kipf used the nickname “GhostMarket09” to operate a credential stealing service, Larsen said.

Apart from GhostMarket09, Larsen said that Mandiant identified several other monikers that Kipf used on different hacking forums, as well as Telegram, which included: “theelephantshow,” “﻿﻿yelichanter,” and “﻿﻿ayohulk.” Having that list of monikers, Larsen said he manually reviewed thousands of messages sent by Kipf under his various online personas, going through a database that Mandiant created by scraping the hacking forums, “semi-public chats,” and Telegram channels.

Larsen said that Mandiant identified the FreeRa...