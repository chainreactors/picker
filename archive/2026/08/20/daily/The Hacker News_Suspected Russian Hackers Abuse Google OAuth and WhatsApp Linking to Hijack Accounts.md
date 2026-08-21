---
title: Suspected Russian Hackers Abuse Google OAuth and WhatsApp Linking to Hijack Accounts
url: https://thehackernews.com/2026/08/suspected-russian-hackers-abuse-google.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:08.306486
---

# Suspected Russian Hackers Abuse Google OAuth and WhatsApp Linking to Hijack Accounts

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Suspected Russian Hackers Abuse Google OAuth and WhatsApp Linking to Hijack Accounts](https://thehackernews.com/2026/08/suspected-russian-hackers-abuse-google.html)

**Ravie Lakshmanan**Aug 20, 2026Phishing / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEix5lAWOEf4I8fcz0CJYg-EBclOrTPnlbsf6tKT2-L8xsfQ4XqtjOq15iU6EBbIsWlqQq3e1-hIXrPe7MMg4JwSGj6mSwjSwG8V3UFMrfgYD-Lo9bKvncTGJ9lPbZoxq-1RNmKLyL_jZSiurWVgGuIxjgYYJeXW_wE51PRTDUhT7kRxp0MMpc3YflI9bntb/s1700-e365/google-whatsapp.jpg)

Three distinct suspected Russian cyber espionage threat clusters have been observed leveraging legitimate authentication flows to single out individuals working in academia, aerospace and defense, governments, and think tanks across Europe, as well as academia and think tanks within the U.S.

These clusters include **UNC6293**, **UNC7005**, and **UNC5976**.

"These clusters engage in persistent, adaptive phishing campaigns, using sophisticated social engineering tactics to compromise personal accounts across multiple platforms," Google Threat Intelligence Group (GTIG) researchers Gabby Roncone and Wesley Shields [said](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia) in a report published today.

UNC6293, [first detailed](https://thehackernews.com/2025/06/russian-apt29-exploits-gmail-app.html) by the tech giant and the Citizen Lab in June 2025, is assessed to be a sub-cluster of Ice Relic (formerly APT29), which is also tracked under the monikers Cozy Bear and Midnight Blizzard. The hacking crew was previously attributed to a campaign that abused a Google account feature called application specific passwords to seize control of victim accounts.

Since then, the threat actor has continued to engage in phishing campaigns that tend to be small in scope, targeting fewer than five users at a time, while impersonating State Department officials to perform app password phishing. The application names and lures revolve around diplomatic themes and upcoming conferences or meetings, some of which were [highlighted](https://thehackernews.com/2025/12/weekly-recap-usb-malware-react2shell.html#:~:text=Russian%20Hackers%20Spoof%20European%20Security%20Events%20in%20Phishing%20Wave) by Volexity in December 2025.

As recently as June 2026, Google said it observed the threat actor conducting OAuth phishing by requesting targets to share either the full URL or verification code after performing a legitimate login to an external provider. Once the requested verification code is provided, it allows the attackers to access the target's account.

UNC5976, the second threat group with an authentication focus, has been found to use OAuth phishing techniques and automate the collection of tokens by abusing cloud infrastructure. The adversary is believed to be active since at least March 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"To perform these OAuth phishing campaigns, UNC5976 purchased domains, usually using file-sharing-related domain names, and then created a cloud project related to that domain," GTIG said. "These domains host a fake file sharing page. After a target visits the page for a few seconds, the page displays a pop-up login dialog."

The pop-up features a "Continue with Google" button that, if clicked, redirects the victim to the legitimate Google OAuth login page, asking them to sign in to continue. Upon successful authentication, the victim is sent to a Google Cloud project URL that hosts malicious scripts designed to retrieve the authentication token from the URL and stage it for later use.

The threat actor is estimated to have created no less than 12 new domains and related infrastructure since March 2026, all of which have since been disrupted by Google. The actions are said to have prompted UNC5976 to pivot away from Google infrastructure to other providers to host their phishing pages.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8k26aQE3-IFTAuHYHtD05QWrul6yWDPNTvyW9Tse4qm0bfafL6J3rkVhAnceuyb2O6tJP1ymLWVb5q8TUtLcLpVyyn5EBUmcbt4MaGlunuq6EKELolBFeHpyuI_hhsrzLJiY-f2vJ9saK_2rHfifHdvdcKLIcCePQ8darG9N8otSkmu-qtw33vqlznlGf/s1700-e365/1.png) |
| UNC7005 WhatsApp compromise flow |

In addition, UNC5976 has been observed leveraging a rogue Excel plugin codenamed HEADRUSH that's used to deliver an HTML Application (HTA) downloaded. The malware, discovered in April 2026, is distributed via a fake domain impersonating a Ukrainian research institute. There are indications that the artifact may have been used to target a Ukrainian aerospace and imaging company, although the full scope of the infection remains unknown.

"Its operational focus is primarily centered on the military, aerospace, defense industrial base, and NGOs/think tanks," Google said. "Much of the group's geographic targeting has centered on Ukraine and Armenia."

### UNC7005 Employs Myriad Tactics

The threat actor that has emerged as the core focus of GTIG's research is UNC7005 (aka Storm-2945), which it identified in February 2026 and has been found to mainly target academia, diplomatic, and nonprofit personnel across Ukraine, Western Europe, and the U.S.

Both UNC6293 and UNC7005 are believed to be related to a sub-group within Ice Relic that's focused on initial access operations, while relying on commercial residential proxies for post-compromise activity. Like UNC6293, UNC7005 has conducted highly selective app password phishing operations aimed at individuals of interest to the Kremlin.

The hacking group has also engaged in [device code phishing](https://thehackernews.com/2025/12/russia-linked-hackers-use-microsoft-365.html) [operations](https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html) targeting both Microsoft and WhatsApp accounts, with the former making use of phishing emails containing invitations ...