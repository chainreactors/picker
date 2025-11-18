---
title: New EVALUSION ClickFix Campaign Delivers Amatera Stealer and NetSupport RAT
url: https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html
source: The Hacker News
date: 2025-11-17
fetch_date: 2025-11-18T03:15:21.566108
---

# New EVALUSION ClickFix Campaign Delivers Amatera Stealer and NetSupport RAT

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [New EVALUSION ClickFix Campaign Delivers Amatera Stealer and NetSupport RAT](https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html)

**Nov 17, 2025**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjThsbRJ_lhgrHOpVNJwYWI0Xc25nNa8uJ5J41VrEz8dv-B5UVNQcMoYyddfmhabn_nHz_rfrkgJbC8KYvOSwyfgbPRuCo08qaxLraEFbe-F2KQG2YoVj_pYae0ArE0YUKcx9ysHzNSGo5XCv0tz5LDsnmJTfPPLLsf7EYv3SJPhlWw5SN0yR9plhnJPTiY/s790-rw-e365/clickfix.jpg)

Cybersecurity researchers have discovered malware campaigns using the now-prevalent [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html) social engineering tactic to deploy [Amatera Stealer](https://thehackernews.com/2025/09/researchers-expose-svg-and-purerat.html) and [NetSupport RAT](https://thehackernews.com/2025/06/fake-docusign-gitcode-sites-spread.html).

The activity, observed this month, is being [tracked](https://www.esentire.com/blog/evalusion-campaign-delivers-amatera-stealer-and-netsupport-rat) by eSentire under the moniker **EVALUSION**.

[First spotted](https://thehackernews.com/2025/07/weekly-recap-chrome-0-day-ivanti.html) in June 2025, Amatera is [assessed](https://www.proofpoint.com/us/blog/threat-insight/amatera-stealer-rebranded-acr-stealer-improved-evasion-sophistication) to be an evolution of ACR (short for "AcridRain") Stealer, which was available under the malware-as-a-service (MaaS) model until sales of the malware were suspended in mid-July 2024. Amatera is available for purchase via subscription plans that go from $199 per month to $1,499 for a year.

"Amatera provides threat actors with extensive data exfiltration capabilities targeting crypto-wallets, browsers, messaging applications, FTP clients, and email services," the Canadian cybersecurity vendor said. "Notably, Amatera employs advanced evasion techniques such as WoW64 SysCalls to circumvent user-mode hooking mechanisms commonly used by sandboxes, Anti-Virus solutions, and EDR products."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

As is typically the case with ClickFix attacks, users are tricked into executing malicious commands using the Windows Run dialog in order to complete a reCAPTCHA verification check on bogus phishing pages. The command initiates a multi-step process that involves using the "mshta.exe" binary to launch a PowerShell script that's responsible for downloading a .NET downloaded from MediaFire, a file hosting service.

The payload is the Amatera Stealer DLL packed using [PureCrypter](https://thehackernews.com/2025/01/purecrypter-deploys-agent-tesla-and-new.html), a C#-based multi-functional crypter and loader that's also [advertised](https://www.esentire.com/blog/pure-crypter-malware-analysis-99-problems-but-detection-aint-one) as a MaaS offering by a threat actor named PureCoder. The DLL is injected into the "MSBuild.exe" process, following which the stealer harvests sensitive data and contacts an external server to execute a PowerShell command to fetch and run NetSupport RAT.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFYQ4vsNHSnLep2twPg_0DuE8ZpAJh9M9G0STAV7EEvAi9gpLlvJsz9FlDUN6ZdfVnRoTnoMrKNybFQqGT15zBEm-ykVsrtCzX2yzfM9daILefBiqYLHWG_vbMNoVqi70Y9gJ0fV3bauWvnmjtFFDrYuzzKsJMD84rTAXaFA2dvJqRKJvf5NrjoFrKkcne/s790-rw-e365/rats.png)

"What is particularly noteworthy in the PowerShell invoked by Amatera is a check to determine if the victim machine is part of a domain or has files of potential value, e.g., crypto wallets," eSentire said. "If neither is found, NetSupport is not downloaded."

The development dovetails with the discovery of several phishing campaigns propagating a wide range of malware families -

* Emails [containing](https://www.malwarebytes.com/blog/threats/2025/11/we-opened-a-fake-invoice-and-fell-down-a-retro-xworm-shaped-wormhole) Visual Basic Script attachments that masqueraded as invoices to deliver [XWorm](https://thehackernews.com/2025/10/xworm-60-returns-with-35-plugins-and.html) by means of a batch script that invokes a PowerShell loader
* Compromised websites [injected](https://isc.sans.edu/diary/32474) with malicious JavaScript that redirects site visitors to bogus ClickFix pages mimicking Cloudflare Turnstile checks to deliver NetSupport RAT as part of an [ongoing campaign](https://www.threatdown.com/blog/smartapesg-06-11-2024/) codenamed [SmartApeSG](https://thehackernews.com/2025/02/cybercriminals-use-eclipse-jarsigner-to.html) (aka HANEYMANEY and ZPHP)
* Using fake Booking.com sites to [display](https://www.forcepoint.com/blog/x-labs/invisible-prompts-ai-summarizer-attacks) fake CAPTCHA checks that employ ClickFix lures to run a malicious PowerShell command that drops a credential stealer when executed via the Windows Run dialog
* Emails [spoofing](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2025-11-07-IOCs-for-phishing-activity-spoofing-spam-filters.txt) internal "email delivery" notifications that [falsely claim](https://www.malwarebytes.com/blog/news/2025/11/phishing-emails-disguised-as-spam-filter-alerts-are-stealing-logins) to have blocked important messages related to outstanding invoices, package deliveries, and Request for Quotations (RFQs) in order to trick recipients into clicking on a link that siphons login credentials under the pretext of moving the messages to the inbox
* Attacks using phishing kits named Cephas (which first emerged in August 2024) and [Tycoon 2FA](https://thehackernews.com/2024/03/alert-new-phishing-attack-delivers.html) to lead users to malicious login pages for credential theft

"What makes Cephas noteworthy is that it implements a distinctive and uncommon obfuscation technique," Barracuda [said](https://blog.barracuda.com/2025/11/12/email-threat-radar-november-2025) in an analysis published last week. "The kit obscures its code by creating random invisible characters within the source code that help it evade anti-phishing scanner...