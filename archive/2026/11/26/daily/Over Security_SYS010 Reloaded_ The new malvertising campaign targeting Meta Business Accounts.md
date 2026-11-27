---
title: SYS010 Reloaded: The new malvertising campaign targeting Meta Business Accounts
url: https://www.bitdefender.com/en-us/blog/labs/sys010-reloaded-malvertising-campaign-targeting-meta-business-accounts
source: Over Security
date: 2026-11-26
fetch_date: 2026-11-27T10:17:24.389920
---

# SYS010 Reloaded: The new malvertising campaign targeting Meta Business Accounts

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")
* Login

  ##### Your account

  + [Bitdefender Central](https://login.bitdefender.com/central/login.html?lang=en_US&redirect_url=https:%2F%2Fcentral.bitdefender.com)
  + [GravityZone CLOUD Control Center](https://gravityzone.bitdefender.com/)
  + [MDR Portal](https://auth.mdr.bitdefender.com/login)

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

20 min read

# SYS010 Reloaded: The new malvertising campaign targeting Meta Business Accounts

[![Ionut Alexandru BALTARIU](https://blogapp.bitdefender.com/labs/content/images/size/w100/2023/10/BSP_3250.jpg "Ionut Alexandru BALTARIU")](/en-us/blog/labs/author/ionut-baltariu "Ionut Alexandru BALTARIU")[![Alina BÎZGĂ](https://blogapp.bitdefender.com/labs/content/images/size/w100/2023/12/Capture.JPG "Alina BÎZGĂ")](/en-us/blog/labs/author/alina-bizga "Alina BÎZGĂ")

[Ionut Alexandru BALTARIU](/en-us/blog/labs/author/ionut-baltariu "Ionut Alexandru BALTARIU")[Alina BÎZGĂ](/en-us/blog/labs/author/alina-bizga "Alina BÎZGĂ")

November 26, 2026

  ![SYS010 Reloaded: The new malvertising campaign targeting Meta Business Accounts](https://blogapp.bitdefender.com/labs/content/images/size/w600/2026/11/SYS010_-Fake-ads--stolen-Meta-Business-accounts.jpg "SYS010 Reloaded: The new malvertising campaign targeting Meta Business Accounts")

Bitdefender Labs has uncovered SYS010, a new malvertising campaign that uses Meta ads promoting free animated wallpaper apps to target Meta Business accounts.

The campaign uses paid ads to direct users to install malicious browser extensions that steal browser cookies, collect Meta Business data, read emails and, in some cases, delete security alerts.

## Key findings:

* **Ongoing attack**: Bitdefender Labs identified the first malicious SYS010 advertisement on October 16, 2026.
* **A new generation of SYS01:** SYS010 retains elements of the SYS01 delivery chain documented by Bitdefender Labs in 2024, but substantially rebuilds the loader, browser-extension payload and account-theft capabilities.
* **Global activity:** Bitdefender observed requests to SYS010 infrastructure from countries across Asia, Europe, North America, Africa and South America. The highest volume of observed requests came from the Philippines, Thailand, Bangladesh, Poland, Mexico, Algeria, Belgium, Mongolia and the United States.
* **A convincing decoy:** The ads promote free animated wallpaper applications for Windows. Victims download a working wallpaper app that also installs malicious components in the background.
* **No activity observed from Vietnam:** Bitdefender telemetry did not record SYS010-related activity from Vietnam. This is consistent with, but does not prove, the possibility that Vietnamese-speaking individuals may be operating the campaign while targeting people elsewhere.
* **From PHP Infostealer to PHP loader**: The PHP samples no longer steal data. They enroll the victim with the command and control (C2) server and wait for tasks, and the next stages are delivered only to the victims that the server selects.
* **The Infostealer moved into the browser**: The final payload is a malicious browser extension for Chrome, Edge and Firefox that can steal browser cookies and collect data from Facebook ad accounts, Business Managers and Pages. The Firefox version carries a valid Mozilla signature.
* **Reading and deleting emails**: The Chrome version of the extension adds a module that reads the most recent messages from the Gmail and Outlook accounts open in the browser and permanently deletes messages selected by the attackers, which can be used to hide security alerts from the victim.
* SYS010 abuses browser and device-management features intended for legitimate organizations, making the malicious extensions difficult for victims to remove.
* **Resilient infrastructure**: The loader and the extension each have their own C2 domains and can obtain new ones from authenticated messages hosted on Telegram and Cloudflare R2 (and, for the loader, on Google Docs and Google Sites). During our analysis, we observed new domains being published for both of them.
* Small businesses and creators who use Meta Pages, professional accounts or advertising tools should be especially careful with software downloads promoted through social media ads.

## A new version of SYS01

We chose the name SYS010 because 010 represents the number two in binary: the second major version of the SYS01 campaign identified by Bitdefender Labs.

The operation retains the same broad goal of stealing access to Facebook and Meta Business accounts, but its delivery chain and capabilities have changed significantly. For small businesses and creators, a compromise can mean lost access to social accounts, advertising budgets, customer messages and trusted brand channels.

## Deep dive into the malvertising campaign

The ads observed by Bitdefender Labs promote free “live wallpaper” software for Windows. One advertisement used a short video of an animated desktop wallpaper alongside a suggestive headline, then directed people to wallpapersengine[.]com, a domain designed to resemble the name of the legitimate Wallpaper Engine application.

So far, researchers have observed ads impersonating Wallpaper Engine and Live Wallpapers. One advertisement reached more than 6,000 people, and dozens of ads have been created since October.

![](https://blogapp.bitdefender.com/labs/content/images/2026/11/ad.png)![](https://blogapp.bitdefender.com/labs/content/images/2026/11/rea.png)

## From the first ad to global activity

Bitdefender Labs identified the first malicious SYS010 advertisement on October 16, 2026. Since then, Bitdefender has observed requests from devices in countries across Asia, Europe, North America, Africa and South America. The highest volume of observed requests came from the Philippines, Thailand, Bangladesh, Poland, Mexico, Algeria, Belgium, Mongolia and the United States.

The wider list of countries includes Egypt, Morocco, Serbia, Peru, Romania, Greece, the Netherlands, Madagascar, Zimbabwe, Laos, France, Cambodia, Brazil, Malaysia, Nepal, Italy, Saudi Arabia, Tunisia, Spain and Pakistan.

Notably, Bitdefender telemetry did not record SYS010-related activity from Vietnam. This is consistent with the assessment that the campaign may be operated by Vietnamese-speaking individuals while primarily targeting people in other regions. However, the absence of telemetry from one country does not establish attribution on its own.

## Distribution tactics of the malvertising campaign

Unlike the [SYS01 campaign documented in 2024](https://www.bitdefender.com/en-us/blog/labs/unmasking-the-sys01-infostealer-threat-bitdefender-labs-tracks-global-malvertising-campaign-targeting-meta-business-pages), which often pointed victims to MediaFire links, SYS010 ads lead to dedicated websites that directly download a roughly 74 MB ZIP archive.

![](https://blogapp.bitdefender.com/labs/content/images/2026/11/image.png)

The archive contains an application named Wallpaper Engine.exe. There is no traditional installation process: the victim unpacks the archive and runs *Wallpaper Engine.exe*.

![](https://blogapp.bitdefender.com/labs/content/images/2026/11/data-src-image-bf0fd93a-0ef4-44b9-89ec-8137d7cf20dc.png)

While the structure of the extracted archive looks like that of any Electron application, a closer look reveals several interesting facts:

* The main executable is not malicious. It is the unmodified, digitally signed binary of the MeisterTask desktop application (version 3.0.10, built on Electron 11.0.3), renamed to *Wallpaper Engine.exe...