---
title: Infy Hackers Resume Operations with New C2 Servers After Iran Internet Blackout Ends
url: https://thehackernews.com/2026/02/infy-hackers-resume-operations-with-new.html
source: The Hacker News
date: 2026-02-05
fetch_date: 2026-02-06T04:10:23.274808
---

# Infy Hackers Resume Operations with New C2 Servers After Iran Internet Blackout Ends

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Infy Hackers Resume Operations with New C2 Servers After Iran Internet Blackout Ends](https://thehackernews.com/2026/02/infy-hackers-resume-operations-with-new.html)

**Ravie Lakshmanan**Feb 05, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8ERbt8WNDNB0dUBHa1RW4Js_8AhSmorSisyOplVJjamDe87uMfCCGeqM_VrKwRGteNlpjh3NfFHjriXs81bWsrgjtX75RGERc1AFNBWFKLTtm-geYPNn4aVPeDVNzcoqmDrMImn7YPl1sqja6zKy7aAFO5baubav3qk8AMIFj5MAh2GpkSoI1YL4PSKMk/s1700-e365/iranian-hackers.jpg)

The elusive Iranian threat group known as **Infy** (aka Prince of Persia) has evolved its tactics as part of efforts to hide its tracks, even as it readied new command-and-control (C2) infrastructure coinciding with the [end of the widespread internet blackout](https://www.bbc.com/news/articles/cz7y2ddgl23o) the regime imposed at the start of January 2026.

"The threat actor stopped maintaining its C2 servers on January 8 for the first time since we began monitoring their activities," Tomer Bar, vice president of security research at SafeBreach, [said](https://www.safebreach.com/blog/prince-of-persia-part-ii/) in a report shared with The Hacker News.

"This was the same day a country-wide internet shutdown was imposed by Iranian authorities in response to recent protests, which likely suggests that even government-affiliated cyber units did not have the ability or motivation to carry out malicious activities within Iran."

The cybersecurity company said it observed renewed activity on January 26, 2026, as the hacking crew set up new C2 servers, one day before the Iranian government relaxed internet restrictions within the country. The development is significant, not least because it offers concrete evidence that the adversary is state-sponsored and backed by Iran.

Infy is just one of many state-sponsored hacking groups operating out of Iran that conduct espionage, sabotage, and influence operations aligned with Tehran's strategic interests. But it's also one of the oldest and lesser-known groups that has managed to stay under the radar, not attracting attention and operating quietly since 2004 through "laser-focused" attacks aimed at individuals for intelligence gathering.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

In a report [published](https://thehackernews.com/2025/12/iranian-infy-apt-resurfaces-with-new.html) in December 2025, SafeBreach disclosed new tradecraft associated with the threat actor, including the use of updated versions of Foudre and Tonnerre, with the latter employing a Telegram bot likely for issuing commands and collecting data. The latest version of Tonnerre (version 50) has been codenamed Tornado.

Continued visibility into the threat actor's operations between December 19, 2025, and February 3, 2026, has uncovered that the attackers have taken the step of replacing the C2 infrastructure for all versions of Foudre and Tonnerre, along with introducing Tornado version 51 that uses both HTTP and Telegram for C2.

"It uses two different methods to generate C2 domain names: first, a new DGA algorithm and then fixed names using blockchain data de-obfuscation," Bar said. "This is a unique approach that we assume is being used to provide greater flexibility in registering C2 domain names without the need to update the Tornado version."

There are also signs that Infy has weaponized a 1-day security flaw in WinRAR (either [CVE-2025-8088 or CVE‑2025‑6218](https://thehackernews.com/2026/01/google-warns-of-active-exploitation-of.html)) to extract the Tornado payload on a compromised host. The change in attack vector is seen as a way to increase the success rate of its campaigns. The specially-crafted RAR archives were uploaded to the VirusTotal platform from Germany and India in mid-December 2025, suggesting the two countries may have been targeted.

Present within the RAR file is a self-extracting archive (SFX) that contains two files -

* AuthFWSnapin.dll, the main Tornado version 51 DLL
* reg7989.dll, an installer that first checks if Avast antivirus software is not installed, and if yes, creates a scheduled task for persistence and executes the Tornado DLL

Tornado establishes communication with the C2 server over HTTP to download and execute the main backdoor and harvest system information. If Telegram is chosen as the C2 method, Tornado uses the bot API to exfiltrate system data and receive more commands.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfO2sB4YSORbo6G1cAKK0Tb_Qj1K6pyZVirjVhuSjMs2NuXUQ-9nUTkfJulnxxskMPsA2UwFZSPKb2kOdWTGHvmCs6kYGr4ouxfWOiQa8fT4_htejQvFeGHku6UglEwCUPa8wmkbBVw2mOz8ar8Uaab8iKB6u1QXIqiIU3hgELfovmwtloM4qKyEl2pr7g/s1700-e365/strom.jpg)

It's worth noting that version 50 of the malware used a Telegram group named سرافراز (literally translates to "sarafraz," meaning proudly) that featured the Telegram bot "@ttestro1bot" and a user with the handle "@ehsan8999100." In the latest version, a different user called "[@Ehsan66442](https://t.me/Ehsan66442)" has been added in place of the latter.

"As before, the bot member of the Telegram group still doesn't have permissions to read the group's chat messages," Bar said. "On December 21, the original user @ehsan8999100 was added to a new Telegram channel named Test that had three subscribers. The goal of this channel is still unknown, but we assume it is being used for command and control over the victim’s machines."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

SafeBreach said it [managed](https://www.forcepoint.com/blog/x-labs/tapping-telegram-bots) to [extract](https://checkmarx.com/blog/when-the-hunter-becomes-the-hunted/) all messages within the private Telegram group, enabling access to all exfiltrated Foudre and Tonnerre files since February 16, 2025, including 118 files and 14 shared links containing encoded commands sent to Tonnerre by the threat actor. An analysis of this data has ...