---
title: A Brazilian phone spyware was hacked and victims’ devices 'deleted' from server | TechCrunch
url: https://techcrunch.com/2023/08/26/brazil-webdetetive-spyware-deleted/?guccounter=1
source: Over Security - Cybersecurity news aggregator
date: 2023-08-27
fetch_date: 2025-10-04T11:59:58.380482
---

# A Brazilian phone spyware was hacked and victims’ devices 'deleted' from server | TechCrunch

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

![a collection of patterned illustrated eyes in blue and pink on a darker blue background](https://techcrunch.com/wp-content/uploads/2023/08/getty-photo-mosh-stalkerware.jpg?w=1024)

**Image Credits:**Jake O'Limb / PhotoMosh / Getty Images

[Security](https://techcrunch.com/category/security/)

# A Brazilian phone spyware was hacked and victims’ devices ‘deleted’ from server

## The Portuguese-language app WebDetetive was used to compromise over 76,000 phones to date

[Zack Whittaker](https://techcrunch.com/author/zack-whittaker/)

1:00 PM PDT · August 26, 2023

A Portuguese-language spyware called WebDetetive has been used to compromise more than 76,000 Android phones in recent years across South America, largely in Brazil. WebDetetive is also the latest phone spyware company in recent months to have been hacked.

In an undated note seen by TechCrunch, the unnamed hackers described how they found and exploited several security vulnerabilities that allowed them to compromise WebDetetive’s servers and access its user databases. By exploiting other flaws in the spyware maker’s web dashboard — used by abusers to access the stolen phone data of their victims — the hackers said they enumerated and downloaded every dashboard record, including every customer’s email address.

The hackers said that dashboard access also allowed them to delete victim devices from the spyware network altogether, effectively severing the connection at the server level to prevent the device from uploading new data. “Which we definitely did. Because we could. Because #fuckstalkerware,” the hackers wrote in the note.

The note was included in a cache containing more than 1.5 gigabytes of data scraped from the spyware’s web dashboard. That data included information about each customer, such as the IP address they logged in from and their purchase history. The data also listed every device that each customer had compromised, which version of the spyware the phone was running, and the types of data that the spyware was collecting from the victim’s phone.

The cache did not include the stolen contents from victims’ phones.

[DDoSecrets](https://ddosecrets.com/wiki/Distributed_Denial_of_Secrets), a nonprofit transparency collective that indexes leaked and exposed datasets in the public interest, received the WebDetetive data and shared it with TechCrunch for analysis.

In total, the data showed that WebDetetive had compromised 76,794 devices to date at the time of the breach. The data also contained 74,336 unique customer email addresses, though WebDetetive does not verify a customer’s email addresses when signing up, preventing any meaningful analysis of the spyware’s customers.

Techcrunch event

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss the 20th anniversary of TechCrunch, and a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

### Join 10k+ tech and VC leaders for growth and connections at Disrupt 2025

#### Netflix, Box, a16z, ElevenLabs, Wayve, Hugging Face, Elad Gil, Vinod Khosla — just some of the 250+ heavy hitters leading 200+ sessions designed to deliver the insights that fuel startup growth and sharpen your edge. Don’t miss a chance to learn from the top voices in tech. **Grab your ticket before doors open to save up to $444.**

San Francisco
|
October 27-29, 2025

[**REGISTER NOW**](https://techcrunch.com/events/tc-disrupt-2025/?utm_source=tc&utm_medium=ad&utm_campaign=disrupt2025&utm_content=ticketsales&promo=tc_inline_lb&display=)

It’s not known who is behind the WebDetetive breach and the hackers did not provide contact information. TechCrunch could not independently confirm the hackers’ claim that it deleted victims’ devices from the network, though TechCrunch did verify the authenticity of the stolen data by matching a selection of device identifiers in the cache against a publicly accessible endpoint on WebDetetive’s server.

WebDetetive is a type of phone monitoring app that is planted on a person’s phone without their consent, often by someone with knowledge of the phone’s passcode.

Once planted, the app changes its icon on the phone’s home screen, making the spyware difficult to detect and remove. WebDetetive then immediately begins stealthily uploading the contents of a person’s phone to its servers, including their messages, call logs, phone call recordings, photos, ambient recordings from the phone’s microphone, social media apps, and real-time precise location data.

Despite the broad access that these “stalkerware” (or spouseware) apps have to a victim’s personal and sensitive phone data, spyware is notoriously buggy and known for their shoddy coding, which puts victims’ already-stolen data at risk of further compromise.

## WebDetetive, meet OwnSpy

Little is known about WebDetetive beyond its surveillance capabilities. It’s not uncommon for spyware makers to conceal or obfuscate their real-world identities, given the reputational and legal risks that come with producing spyware and facilitating the illegal surveillance of others. WebDetetive is no different.

But while the breached data itself reveals few clues about WebDetetive’s administrators, much of its roots can be traced back to OwnSpy, another widely used phone spying app.

TechCrunch downloaded the WebDetetive Android app from its website (since both Apple and Google ban stalkerware apps from their app stores), and planted the app onto a virtual device, allowing us to analyze the app in an isolated sandbox without giving it any real data, such as our location. We ran a network traffic analysis to understand what data was flow...