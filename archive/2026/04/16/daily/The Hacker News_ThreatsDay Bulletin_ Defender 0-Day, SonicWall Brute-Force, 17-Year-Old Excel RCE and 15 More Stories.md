---
title: ThreatsDay Bulletin: Defender 0-Day, SonicWall Brute-Force, 17-Year-Old Excel RCE and 15 More Stories
url: https://thehackernews.com/2026/04/threatsday-bulletin-17-year-old-excel.html
source: The Hacker News
date: 2026-04-16
fetch_date: 2026-04-17T04:51:15.435576
---

# ThreatsDay Bulletin: Defender 0-Day, SonicWall Brute-Force, 17-Year-Old Excel RCE and 15 More Stories

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

# [ThreatsDay Bulletin: Defender 0-Day, SonicWall Brute-Force, 17-Year-Old Excel RCE and 15 More Stories](https://thehackernews.com/2026/04/threatsday-bulletin-17-year-old-excel.html)

**Ravie Lakshmanan**Apr 16, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzTV_mwPjmV14aBlnHuLOX2yEZR6VGpmadgiPHtNBJV0KVNG_Oj2tnqE1cb3U9RhBXN-Mytte3jKs2n2dQwBhX2dYDETy5es4cGUkbW5bdIaV_hx8i3gWQhdaa7se1_Q8NY9t0q90EjUBNXt56_MxjT4YVV-R8D14jV3LequHu0llA84NnEK3PeU56Q54X/s1700-e365/bull-main.jpg)

You know that feeling when you open your feed on a Thursday morning and it's just... a lot? Yeah. This week delivered. We've got hackers getting creative in ways that are almost impressive if you ignore the whole "crime" part, ancient vulnerabilities somehow still ruining people's days, and enough supply chain drama to fill a season of television nobody asked for.

Not all bad though. Some threat actors got exposed with receipts, a few platforms finally tightened things up, and there's research in here that's genuinely worth your time. Grab your coffee and keep scrolling.

1. Targeted wallet breach

   [Zerion Hack Likely Linked to North Korea](https://x.com/zerion/status/2044167535231414727)

   Cryptocurrency wallet service Zerion has [disclosed](https://x.com/zerion/status/2044167535231414727) that one of its team member's devices was compromised, resulting in the theft of approximately $100K in stolen funds from internal company hot wallets. The company noted that user funds, Zerion apps, or infrastructure were not impacted by the breach. The team member is said to have been the target of an artificial intelligence (AI)-enabled social engineering attack carried by a North Korean threat actor tracked as [UNC1069](https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html). The hacking group was recently attributed to the poisoning of the popular Axios npm package. "This allowed the attacker to gain access to some of the team members' logged-in sessions and credentials as well as private keys to company hot wallets used for testing and internal purposes," Zerion said. "This was not an opportunistic attack. The actor is clearly sophisticated and well-resourced. They planned the attack thoroughly."
2. Anonymous age checks

   [E.U. Plans Bloc-Wide Age Verification App](https://ec.europa.eu/commission/presscorner/detail/en/statement_26_817)

   The European Union has announced that it will soon roll out a new online age verification app to allow users to prove their age when accessing online platforms. Users can set it up by downloading the app on their Android or iOS device using a passport or ID card. The Commission has emphasized that the app will respect users' privacy. "Users will prove their age without revealing any other personal information," President of the European Commission, Ursula von der Leyen, [said](https://ec.europa.eu/commission/presscorner/detail/en/statement_26_817). "Put simply, it is completely anonymous: users cannot be tracked. Third, the app works on any device – phone, tablet, computer, you name it. And, finally, it is fully open source – everyone can check the code." The development comes as countries around the world are undertaking various stages of regulatory action to keep cyberspace a safer place for children and minors and protect them from serious harm.
3. New Defender zero-day

   [BlueHammer Author Releases RedSun Exploit](https://github.com/Nightmare-Eclipse/RedSun)

   A researcher using the alias "Chaotic Eclipse" released a zero-day exploit called [BlueHammer](https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html) earlier this month following Microsoft's handling of the vulnerability disclosure process. Although the issue appears to have been fixed as of this month's Patch Tuesday release (CVE-2026-33825), the researcher has since [disclosed](https://x.com/ChaoticEclipse0/status/2044550275692642782) a new unpatched [Microsoft Defender privilege escalation vulnerability](https://deadeclipse666.blogspot.com/2026/04/public-disclosure-response-for-cve-2026.html). The exploit has been codenamed [RedSun](https://github.com/Nightmare-Eclipse/RedSun). "This works 100% reliably to go from unprivileged user to SYSTEM against Windows 11 and Windows Server with April 2026 updates, as well as Windows 10, as long as you have Windows Defender enabled," security researcher Will Dormann [said](https://infosec.exchange/%40wdormann/116412019416916182).
4. Legacy Excel RCE active

   [17-Year-Old Critical Excel flaw Under Exploit](https://www.cisa.gov/news-events/alerts/2026/04/14/cisa-adds-two-known-exploited-vulnerabilities-catalog)

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [added](https://www.cisa.gov/news-events/alerts/2026/04/14/cisa-adds-two-known-exploited-vulnerabilities-catalog) an old remote code execution vulnerability impacting Microsoft Office to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to remediate the shortcoming by April 28, 2026. The vulnerability in question is CVE-2009-0238, which has a CVSS score of 8.8. "Microsoft Office Excel contains a remote code execution vulnerability that could allow an attacker to take complete control of an affected system if a user opens a specially crafted Excel file that includes a malformed object," CISA [said](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
5. sudo now requires password

   [Raspberry Pi Disables Passwordless sudo](https://www.raspberrypi.com/news/a-security-update-for-raspberry-pi-os/)

   Raspberry Pi has released version 6.2 of its Raspberry Pi OS, which introduces one significant change: it disables passwordless sudo by default. As a result, users who run a sudo command for administrator-level access will be prompted to enter the current user's password. The change affects only new installations; existing setups are untouched. "Given the ever-increasing threat of cybercrime, we continually review the security of Raspberry Pi OS to ensure it is sufficiently robust to withstand potential attacks," Raspberry Pi [said](https://www.raspberrypi.com/news/a-security-update-for-raspberry-pi-os/). "This is always a tricky bal...