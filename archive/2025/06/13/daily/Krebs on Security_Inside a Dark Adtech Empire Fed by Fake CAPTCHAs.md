---
title: Inside a Dark Adtech Empire Fed by Fake CAPTCHAs
url: https://krebsonsecurity.com/2025/06/inside-a-dark-adtech-empire-fed-by-fake-captchas/
source: Krebs on Security
date: 2025-06-13
fetch_date: 2025-10-06T22:59:50.686707
---

# Inside a Dark Adtech Empire Fed by Fake CAPTCHAs

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Inside a Dark Adtech Empire Fed by Fake CAPTCHAs

June 12, 2025

[55 Comments](https://krebsonsecurity.com/2025/06/inside-a-dark-adtech-empire-fed-by-fake-captchas/#comments)

Late last year, security researchers made a startling discovery: Kremlin-backed disinformation campaigns were bypassing moderation on social media platforms by leveraging the same malicious advertising technology that powers a sprawling ecosystem of online hucksters and website hackers. A new report on the fallout from that investigation finds this dark ad tech industry is far more resilient and incestuous than previously known.

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/maladtech.png)

In November 2024, researchers at the security firm **Qurium** published an investigation into “[Doppelganger](https://www.cybercom.mil/Media/News/Article/3895345/russian-disinformation-campaign-doppelgnger-unmasked-a-web-of-deception/),” a disinformation network that promotes pro-Russian narratives and infiltrates Europe’s media landscape by pushing fake news through a network of cloned websites.

Doppelganger campaigns use specialized links that bounce the visitor’s browser through a long series of domains before the fake news content is served. Qurium [found](https://www.qurium.org/forensics/when-kehr-meets-vextrio/) Doppelganger relies on a sophisticated “domain cloaking” service, a technology that allows websites to present different content to search engines compared to what regular visitors see. The use of cloaking services helps the disinformation sites remain online longer than they otherwise would, while ensuring that only the targeted audience gets to view the intended content.

Qurium discovered that Doppelganger’s cloaking service also promoted online dating sites, and shared much of the same infrastructure with **VexTrio**, which is thought to be the oldest malicious traffic distribution system (TDS) in existence. While TDSs are commonly used by legitimate advertising networks to manage traffic from disparate sources and to track who or what is behind each click, VexTrio’s TDS largely manages web traffic from victims of phishing, malware, and social engineering scams.

## BREAKING BAD

Digging deeper, Qurium noticed Doppelganger’s cloaking service used an Internet provider in Switzerland as the first entry point in a chain of domain redirections. They also noticed the same infrastructure hosted a pair of co-branded affiliate marketing services that were driving traffic to sketchy adult dating sites: **LosPollos[.]com** and **TacoLoco[.]co**.

The LosPollos ad network incorporates many elements and references from the hit series “Breaking Bad,” mirroring the fictional “Los Pollos Hermanos” restaurant chain that served as a money laundering operation for a violent methamphetamine cartel.

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/lospollos_mainpage.png)

The LosPollos advertising network invokes characters and themes from the hit show Breaking Bad. The logo for LosPollos (upper left) is the image of Gustavo Fring, the fictional chicken restaurant chain owner in the show.

Affiliates who sign up with LosPollos are given JavaScript-heavy “**smartlinks**” that drive traffic into the VexTrio TDS, which in turn distributes the traffic among a variety of advertising partners, including dating services, sweepstakes offers, bait-and-switch mobile apps, financial scams and malware download sites.

LosPollos affiliates typically stitch these smart links into **WordPress** websites that have been hacked via known vulnerabilities, and those affiliates will earn a small commission each time an Internet user referred by any of their hacked sites falls for one of these lures.

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/lospollos_subdomain_linkedIn_announcement.png)

The Los Pollos advertising network promoting itself on LinkedIn.

According to Qurium, TacoLoco is a traffic monetization network that uses deceptive tactics to trick Internet users into enabling “push notifications,” a [cross-platform browser standard](https://tools.ietf.org/html/rfc8030) that allows websites to show pop-up messages which appear outside of the browser. For example, on Microsoft Windows systems these notifications typically show up in the bottom right corner of the screen — just above the system clock.

In the case of VexTrio and TacoLoco, the notification approval requests themselves are deceptive — disguised as “CAPTCHA” challenges designed to distinguish automated bot traffic from real visitors. For years, VexTrio and its partners have successfully tricked countless users into enabling these site notifications, which are then used to continuously pepper the victim’s device with a variety of phony virus alerts and misleading pop-up messages.

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/maliciouspushcaptcha.png)

Examples of VexTrio landing pages that lead users to accept push notifications on their device.

According to [a December 2024 annual report](https://www.godaddy.com/resources/news/godaddy-annual-cybersecurity-report) from **GoDaddy**, *nearly 40 percent of compromised websites in 2024 redirected visitors to VexTrio via LosPollos smartlinks*.

## ADSPRO AND TEKNOLOGY

On November 14, 2024, Qurium [published research](https://www.qurium.org/forensics/when-kehr-meets-vextrio/) to support its findings that LosPollos and TacoLoco were services operated by **Adspro Group**, a company registered in the Czech Republic and Russia, and that Adspro runs its infrastructure at the Swiss hosting providers **C41** and **Teknology SA**.

Qurium noted the LosPollos and TacoLoco sites state that their content is copyrighted by **ByteCore AG** and **SkyForge Digital AG**, both Swiss firms that are run by the owner of Teknology SA, **Giulio Vitorrio Leonardo Cerutti**. Further investigation revealed LosPollos and TacoLoco were apps developed by a company called **Holacode**, which lists Cerutti as its CEO.

The apps marketed by Holacode include numerous VPN services, as well as one called **Spamshield** that claims to stop unwanted push notifications. But in January, Infoblox said they tested the app on their own mobile devices, and found it hides the user’s notifications, and then after 24 hours stops hiding them and demands payment. Spamshield subsequently changed its developer name from Holacode to **ApLabz**, although Infoblox noted that the Terms of Service for several of the rebranded ApLabz apps still referenced Holacode in their terms of service.

Incredibly, Cerutti threatened to sue me for defamation before I’d even uttered his name or sent him a request for comment (Cerutti sent the unsolicited legal threat back in January after his company and my name were merely tagged in an Infoblox post on LinkedIn about VexTrio).

Asked to comment on the findings by Qurium and Infoblox, Cerutti vehemently denied being associated with VexTrio. Cerutti asserted that his companies all strictly adhere to the regulations of the countries in which they operate, and that they have been completely transparent about all of their operations.

“We are a group operating in the advertising and marketing space, with an affiliate net...