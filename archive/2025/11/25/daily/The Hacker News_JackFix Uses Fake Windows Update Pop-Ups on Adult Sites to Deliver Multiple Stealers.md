---
title: JackFix Uses Fake Windows Update Pop-Ups on Adult Sites to Deliver Multiple Stealers
url: https://thehackernews.com/2025/11/jackfix-uses-fake-windows-update-pop.html
source: The Hacker News
date: 2025-11-25
fetch_date: 2025-11-26T03:17:15.474939
---

# JackFix Uses Fake Windows Update Pop-Ups on Adult Sites to Deliver Multiple Stealers

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

# [JackFix Uses Fake Windows Update Pop-Ups on Adult Sites to Deliver Multiple Stealers](https://thehackernews.com/2025/11/jackfix-uses-fake-windows-update-pop.html)

**Nov 25, 2025**Ravie LakshmananWindows Security / Malvertising

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpwmpMC2coSECbndEHIVrYYNz9k16YYM0KkZjT69eMkozDT-LMxy920BF8Hxw34C-Vy_FCTwhZUSJQqQOzgp8UlcEBdb90C5iGVfM67fJ2gP9KNx0H0tJ_sJXcfRgpdbW-5DWKKrGEc0dHzHbnnNiVxIdZhxr_BGNclG-UFRyH1jsAxTh88zI6lc5OXId8/s2600/update-windows.jpg)

Cybersecurity researchers are calling attention to a new campaign that's leveraging a combination of [ClickFix](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html) lures and fake adult websites to deceive users into running malicious commands under the guise of a "critical" Windows security update.

"Campaign leverages fake adult websites (xHamster, PornHub clones) as its phishing mechanism, likely distributed via malvertising," Acronis [said](https://www.acronis.com/en/tru/posts/fake-adult-websites-pop-realistic-windows-update-screen-to-deliver-stealers-via-clickfix/) in a new report shared with The Hacker News. "The adult theme, and possible connection to shady websites, adds to the victim's psychological pressure to comply with sudden 'security update' installation."

[ClickFix-style attacks](https://thehackernews.com/2025/09/new-filefix-variant-delivers-stealc.html) have surged over the past year, typically tricking users into running malicious commands on their own machines using prompts for technical fixes or completing CAPTCHA verification checks. According to [data](https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/) from Microsoft, ClickFix has become the most common initial access method, accounting for 47% of attacks.

The latest campaign displays highly convincing fake Windows update screens in an attempt to get the victim to run malicious code, indicating that attackers are moving away from the traditional robot-check lures. The activity has been codenamed **JackFix** by the Singapore-based cybersecurity company.

Perhaps the most concerning aspect of the attack is that the phony Windows update alert hijacks the entire screen and instructs the victim to open the Windows Run dialog, press Ctrl + V, and hit Enter, thereby triggering the infection sequence.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

It's assessed that the starting point of the attack is a fake adult site to which unsuspecting users are redirected via malvertising or other social engineering methods, only to suddenly serve them an "urgent security update." Select iterations of the sites have been found to include developer comments in Russian, hinting at the possibility of a Russian-speaking threat actor.

"The Windows Update screen is created entirely using HTML and JavaScript code, and pops up as soon as the victim interacts with any element on the phishing site," security researcher Eliad Kimhy said. "The page attempts to go full screen via JavaScript code, while at the same time creating a fairly convincing Windows Update window composed of a blue background and white text, reminiscent of Windows' infamous blue screen of death."

What's notable about the attack is that it heavily leans on obfuscation to conceal ClickFix-related code, as well as blocks users from escaping the full-screen alert by disabling the Escape and F11 buttons, along with F5 and F12 keys. However, due to faulty logic, users can still press the Escape and F11 buttons to get rid of the full screen.

The initial command executed is an MSHTA payload that's launched using the legitimate mshta.exe binary, which, in turn, contains JavaScript designed to run a PowerShell command to retrieve another PowerShell script from a remote server. These domains are designed such that directly navigating to these addresses redirects the user to a benign site like Google or Steam.

"Only when the site is reached out to via an irm or iwr PowerShell command does it respond with the correct code," Acronis explained. "This creates an extra layer of obfuscation and analysis prevention."

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgehldlFCaX9n-99QvcSY5MMSbWUc3Cl0IemlQhsYOu89UEr9WfzeR0wzTapGnewC-qsIBiEZlYUkqVEE8wOVaqVmO-rowQkO3PPeGf8xAycaBDP_Nj3DdJ0xAd6OdsVyWrE2KFh5uB9Tb1unBbrTc_7YgrjVj_MlbYjgN8SWHEA6sB9zhZkDvXcXWWdDTp/s2600/POWER.jpg) |
| UAC request to grant attackers admin privileges |

The downloaded PowerShell script also packs in various obfuscation and anti-analysis mechanisms, one of which is the use of garbage code to complicate analysis efforts. It also attempts to elevate privileges and creates Microsoft Defender Antivirus exclusions for command-and-control (C2) addresses and paths where the payloads are staged.

To achieve privilege escalation, the malware uses the [Start-Process cmdlet](https://powershellcommands.com/start-process-powershell-verb-runas) in conjunction with the "-Verb RunAs" parameter to launch PowerShell with administrative rights and continuously prompts for permission until it's granted by the victim. Once this step is successful, the script is designed to drop additional payloads, such as simple remote access trojans (RATs) that are programmed to contact a C2 server, presumably to drop more malware.

The PowerShell script has also been observed to serve up to eight different payloads, with Acronis describing it as the "most egregious example of spray and pray." These include Rhadamanthys Stealer, Vidar Stealer 2.0, RedLine Stealer, Amadey, as well as other unspecified loaders and RATs.

"If only one of these payloads manages to run successfully, victims risk losing passwords, crypto wallets, and more," Kimhy said. "In the case of a few of these loaders -- the attacker may choose to bring in other payloads into the attack, and the attack can quickly escalate further."

[![CIS Build Kits](data:image/png;...