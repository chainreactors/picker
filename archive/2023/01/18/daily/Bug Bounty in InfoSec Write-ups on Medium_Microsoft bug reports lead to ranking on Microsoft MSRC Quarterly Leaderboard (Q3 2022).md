---
title: Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)
url: https://infosecwriteups.com/microsoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3-2022-c6c9f70e2ccd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-18
fetch_date: 2025-10-04T04:08:20.227955
---

# Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc6c9f70e2ccd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmicrosoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3-2022-c6c9f70e2ccd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmicrosoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3-2022-c6c9f70e2ccd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c6c9f70e2ccd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c6c9f70e2ccd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)

## Microsoft MSRC Quarterly Leaderboard from my security bug reports submitted.

[![Supakiad S. (m3ez)](https://miro.medium.com/v2/resize:fill:64:64/1*X5fh6pruB5p-7uyfDAjZIg.jpeg)](https://m3ez.medium.com/?source=post_page---byline--c6c9f70e2ccd---------------------------------------)

[Supakiad S. (m3ez)](https://m3ez.medium.com/?source=post_page---byline--c6c9f70e2ccd---------------------------------------)

5 min read

·

Dec 23, 2022

--

7

Listen

Share

Press enter or click to view image in full size

![]()

### Table of Contents

— [Part 0 — Whoami?](#c401)
 — [Part 1 — Selecting a program](#920d)
 — [Part 2 — Let the hunt begin!](#af29)
 — [Part 3 — Reporting](#dc93)
 — [Part 4 — Claims the Rewards](#ae49)
 — [Disclosure Timelines](#8792)

## Part 0 — Whoami?

Hello, I am Supakiad Satuwan, a Security Consultant from Thailand. In this article, I will go through the story of my first valid bug found on Microsoft bug bounty program. This has given me an opportunity to be ranked in MSRC 2022 Q3 Security Researcher Leaderboard. Let’s get started!

### What is MSRC?

> **The Microsoft Security Response Center(MSRC)** is part of the microsoft defender community and on the front line of microsoft security response evolution. This platform engaged with security researchers working to protect Microsoft’s customers and the broader ecosystem. For more details: [Microsoft Security Response Center](https://msrc.microsoft.com/)

## Part 1 — Selecting a program

* Before starting my bug bounty hunting journey, I navigated to [Microsoft Bounty Programs | MSRC](https://www.microsoft.com/en-us/msrc/bounty) for a list of in-scope and ongoing programs. After going through the list, I decided to work on [Microsoft Dynamics 365 and Power Platform](https://www.microsoft.com/en-us/msrc/bounty-dynamics?rtc=1) Program.

Press enter or click to view image in full size

![]()

[Microsoft Dynamics 365 and Power Platform](https://www.microsoft.com/en-us/msrc/bounty-dynamics?rtc=1)

## Part 2 —Let the hunt begin!

### Analyzing the target

* I started the hunt on Power Apps Platform.
* While analyzing the Power Apps Platform and the applications on it, I noticed that an application sent requests to <https://apps.powerapps.com>

![]()

* It caught my attention. Therefore, I navigated to the following URL:

```
https://apps.powerapps.com/authflow/authframe?telemetryLocation=global
```

Press enter or click to view image in full size

![]()

* This page displayed nothing. However, after viewing the HTML code, I noticed that the value of **telemetryLocation** parameter was reflected to the page.

Press enter or click to view image in full size

![]()

* I modified the value of **telemetryLocation** parameter from **global** to **m3ez**. The result proved that I could control telemetryLocation value.

Press enter or click to view image in full size

![]()

### Exploit start!

* After analyzing this page, I performed Cross-site Scripting (XSS) testing by injecting the following JavaScript payload:

```
</script>
```

* As a result, I discovered that the page reflected the payload without input validation or sanitization mechanism.

Press enter or click to view image in full size

![]()

* I injected the following XSS payload into **telemetryLocation** parameter:

```
</script><body/onload=alert(`m3ez`)>
```

* The final URL was

```
https://apps.powerapps.com/authflow/authframe?telemetryLocation=</script><body/onload=alert(`m3ez`)>
```

* After opening the link, the XSS payload was executed as shown in the image below.

Press enter or click to view image in full size

![]()

> PoC

## Part 3 — Reporting

After discovering and confirming that the target was vulnerable to Cross-site Scripting (XSS), I immediately began the reporting process through MSRC portal. This consists of the following steps:

* Navigated to [Report a Vulnerability | MSRC Researcher Portal](https://msrc.microsoft.com/report/vulnerability/new)
* Entered vulnerability details, including Impact, PoC, and Evidence. Then, submitted the form.

Press enter or click to view image in full size

![]()

[MSRC Researcher Portal (microsoft.com)](https://msrc.microsoft.com/report/vulnerability/new)

Press enter or click to view image in full size

![]()

* After 4 days, MSRC team replied and confirmed my report. ^\_^

Press enter or click to view image in full size

![]()

* Within the same day, Microsoft bounty team replied that they were reviewing a possible bounty award for my vulnerability report.

Press enter or click to view image in full size

![]()

* After a few hours, I received great news from the MSRC team ^\_^

Press enter or click to view image in full size

![]()

### Part 4 — Claims the Rewards

* After Microsoft bounty team confirming my report eligibility for bounty rewards, they inquired about payment providers selection for bounty awards delivery.

Press enter or click to view image in full size

![]()

> **Note**: Currently, Microsoft only supports awards delivery through either Bugcrowd or Microsoft Payment Central in order to receive bounty award payments.

* A few weeks later, I received an email from Bugcrowd which contains a submission claiming link from Microsoft Bug Bounty Program.

Press enter or click to view image in full size

![]()

* After claiming, I received my first reward from Microsoft Bug Bounty Program.

Press enter or click to view image in full size

![]()

* A few months later, my name has been ranked on 2022 Q3 [Leaderboard | MSRC Researcher Portal (microsoft.com)](https://msrc.microsoft.com/leaderboard)

Press enter or click to view image in full size

![]()

* And I have been recognized on the recent quarterly leaderboard for Microsoft MSRC and will be receiving some MSRC magic swag as a reward for my achievements!

P...