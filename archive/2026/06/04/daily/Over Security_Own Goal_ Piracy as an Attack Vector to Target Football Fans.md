---
title: Own Goal? Piracy as an Attack Vector to Target Football Fans
url: https://www.threatfabric.com/blogs/own-goal-piracy-as-an-attack-vector-to-target-football-fans
source: Over Security
date: 2026-06-04
fetch_date: 2026-06-05T06:14:26.063623
---

# Own Goal? Piracy as an Attack Vector to Target Football Fans

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
  + [FUSION FIRESIDE](https://www.threatfabric.com/fusion-fireside)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## Own Goal? Piracy as an Attack Vector to Target Football Fans

04 June 2026

![](https://www.threatfabric.com/hubfs/TF_Blog_Piracy_SOCIAL.jpg)

### Jump to

Major football events consistently drive audiences toward streaming platforms. In Spain, with millions of football enthusiasts and where premium competitions such as the UEFA Champions League are tied to paid services like Movistar Plus, a portion of viewers continues to look for free alternatives.

In the period before the recent UEFA Champions League final between PSG and Arsenal, our MTI research team observed a clear increase in unofficial IPTV apps containing malware, notably apps masquerading as RojaDirecta apps for Android. Timing-wise this correlated with an increase in [legal actions](https://cronicaglobal.elespanol.com/culemania/palco/20260219/nuevo-rojadirecta-sucedaneos-liga-telefonica-ordenar-bloqueo/1003742734489_0.html) to take down websites promoting these apps.

With the World Cup approaching, similar patterns are expected to repeat at a larger scale, because the underlying issue is not limited to Spain. We are closely tracking similar campaigns targeting other countries in Europe, like for example Italy.

## Opening the door for attackers

At the center of this trend is a simple but important shift in user behaviour: **Users intentionally bypass official app stores**, removing built-in protections, in order to access apps that offer pirated content – especially sports related.

This decision is what enables the rest of the attack chain.

In this case, attackers are not exploiting vulnerabilities. They exploit users, their desire for free content and their trust in alternative app stores and streaming apps. The following circumstances and trends stack up to further increase the fraud risk:

* Major live sporting events have shifted from free national broadcast networks to exclusive paid subscription and streaming services as media rights have skyrocketed.
* More third-party app stores have become available due to regulatory changes.
* Mobile is the fastest growing banking channel, with the Android operating system having the biggest market share in Spain ([68% in April 2026](https://gs.statcounter.com/os-market-share/mobile/spain)).
* The amount of observed mobile banking malware families for Android is increasing year-over-year.
* Malware has gained more sophisticated capabilities, including full Device Takeover (DTO), credential theft (using overlays and keylogging), MFA bypass (intercepting SMS, push notifications and authenticator apps), and remote device control.

![](https://www.threatfabric.com/hs-fs/hubfs/image-png-Jun-01-2026-01-09-12-8584-PM.png?width=720&height=449&name=image-png-Jun-01-2026-01-09-12-8584-PM.png)

![](https://www.threatfabric.com/hs-fs/hubfs/image-png-Jun-01-2026-01-09-49-8263-PM.png?width=720&height=405&name=image-png-Jun-01-2026-01-09-49-8263-PM.png)

*Increase in banking malware families and malicious apps masqueraded as IPTV apps over time.*

![PictureHook](https://www.threatfabric.com/hs-fs/hubfs/PictureHook.png?width=720&height=486&name=PictureHook.png)
*Command-and-Control  (C2) panel of the Hook banking malware*

## RojaDirecta and the demand for free football

In Spain, RojaDirecta remains one of the most recognised names in free sports streaming. The platform itself does not host video content. It aggregates and organizes links to streams hosted elsewhere, presenting them in a convenient schedule format that is easy to navigate.

Because it facilitates access to copyrighted broadcasts without compensating rights holders, it has faced years of legal pressure. Many domains have been blocked in Spain, but demand has not disappeared. Instead, the ecosystem has expanded into mirror sites, clones, and mobile apps using similar branding. And that is where the risk becomes more concrete.

![](https://www.threatfabric.com/hs-fs/hubfs/undefined-Jun-01-2026-12-34-31-6370-PM.png?width=723&height=320&name=undefined-Jun-01-2026-12-34-31-6370-PM.png)

*Example of an ad linking to malicious app masquerading as a RojaDirecta app*

![](https://www.threatfabric.com/hs-fs/hubfs/undefined-Jun-01-2026-12-34-43-5746-PM.png?width=273&height=480&name=undefined-Jun-01-2026-12-34-43-5746-PM.png)

*Example of a website stimulating installation of a malicious app masquerading as a RojaDirecta app*

## The critical step: Leaving official app stores

Unofficial RojaDirecta-style apps are not distributed through Google Play or other trusted marketplaces. Users typically encounter them on websites or ads and are asked to download and install them manually.

That step is crucial. By doing so, users:

* Bypass protections designed to screen apps for malicious behaviour.
* Accept installation warnings that would otherwise act as barriers.
* Grant permissions to the app that technically opens the door for attackers.

At this point, attackers do not need to exploit software vulnerabilities. The protections have already been removed by the user decision to install the app.

## How criminals take advantage

Threat actors use this environment to distribute malware through apps that appear functional or familiar. The approach aligns closely with how users already behave when searching for free streams, especially during high-demand events like the Champions League final or the World Cup.

Common distribution methods include:

* Search results and ads leading to fake download pages
* Websites imitating RojaDirecta or similar platforms
* Social media promotions targeting football audiences

These pages are designed to look legitimate enough to complete a single action: installing the app. And because IPTV and similar apps are already associated with unofficial distribution, this step often does not raise concerns.

## From streaming app to malware infection

Once installed, the app may offer limited or full app functionality for the user, while silently delivering a malicious payload. In recent campaigns observed in Spain (and also Italy), this has included banking malware from several powerful malware families like [Massiv](https://www.threatfabric.com/blogs/massiv-when-your-iptv-app-terminates-your-savings) and [Perseus](/blogs/perseus-dto-malware-that-takes-notes).

Tools such as [Zombinder](https://www.threatfabric.com/blogs/zombinder-ermac-and-desktop-stealers) are used to embed malicious code into otherwise usable applications. The result is an app that appears to work as expected while compromising the device in the background.

A typical sequence looks like this:

* A user searches for a free stream of a football match.
* A site referencing RojaDirecta appears in the results (this can be an ad).
* The user downloads and installs an app from that site.
* The app requests ...