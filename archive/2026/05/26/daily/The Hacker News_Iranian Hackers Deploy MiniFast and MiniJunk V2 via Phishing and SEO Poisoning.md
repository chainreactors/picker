---
title: Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning
url: https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html
source: The Hacker News
date: 2026-05-26
fetch_date: 2026-05-27T06:12:49.477117
---

# Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html)

**Ravie Lakshmanan**May 26, 2026Cyber Espionage / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhL7Xqq7FlHxai3-wKrWcUujSg4cXnMJ_0LiXDaZHaZosFt3sPF1_PwcaqufOoM7q66vakQyKX5-odysTHOhtIG7ESj52Kna0i3OxaOA0sTONuH3NhkmautF8CTeiLBDzHFWjEvIT286ZnhERvK2VsvzxTdqjlEpXsbSELeqVHyr18JodeQZC-qudm2yblS/s1700-e365/iran-hackers.jpg)

The Iranian state-sponsored threat actor known as [Nimbus Manticore](https://thehackernews.com/2026/02/google-links-china-iran-russia-north.html) (aka Screening Serpens and [UNC1549](https://thehackernews.com/2026/03/149-hacktivist-ddos-attacks-hit-110.html)) has been attributed to a fresh campaign using lures impersonating organizations in the aviation and software sectors across the U.S., Europe, and the Middle East following the joint U.S.-Israeli military campaign against the country in late February 2026.

The activity, besides embracing previously undocumented techniques and enhanced capabilities, is characterized by the use of a new backdoor codenamed MiniFast (aka MiniUpdate) that appears to have been developed with assistance using artificial intelligence (AI), Check Point [said](https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/) in an analysis published last week.

Affiliated with Iran's Islamic Revolutionary Guard Corps (IRGC), Nimbus Manticore is best known for targeting defense, aviation, and telecommunication sectors using career-themed phishing lures. These campaigns have also been codenamed the Iranian Dream Job, owing to tactical similarities with [Operation Dream Job](https://thehackernews.com/2025/10/north-korean-hackers-lure-defense.html) orchestrated by North Korean hackers.

Recent attack chains linked to the threat actor have witnessed a shift in tradecraft, as evidenced by the use of AppDomain hijacking to deliver [MiniJunk](https://thehackernews.com/2025/09/unc1549-hacks-34-devices-in-11-telecom.html) in February 2026, followed by the deployment of the MiniFast backdoor in March and a reliance on SEO poisoning to distribute a trojanized version of Oracle's SQL Developer software in April.

In the first campaign observed before the onset of the war, employees in software and aviation sectors in Saudi Arabia and Australia were targeted with bogus career opportunities, tricking them into downloading a ZIP archive hosted on OnlyOffice. Launching a benign executable within the ZIP file leveraged a technique known as AppDomain hijacking to launch a rogue MiniJunk DLL.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The March 2026 campaign has been found to follow more or less the same approach, only this time the threat actor also used a trojanized Zoom installer as part of the attack sequence to launch the binary that then leverages AppDomain hijacking to deploy MiniFast. It's suspected that the activity was part of a phishing campaign using fake meeting invitations.

There are signs that Nimbus Manticore used AI-assisted development to help create MiniFast. This includes excessive error handling and defensive programming logic, repetitive function and method naming patterns with descriptive or verbose identifiers, several detailed error-reporting strings and debug-style status messages, and modular code organization despite the malware's overall simplicity.

Check Point said it also observed last month a fake website impersonating a download page for SQL Developer, duping visitors who land the page via SEO poisoning to download a weaponized installer that delivers MiniFast. The development marks the first time the threat actor has resorted to this approach for malware delivery.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzXRDWbj_dl074L-WVoKcr2SvWtXFGvuwYt1YSrphpED3YWhMkLfOMHroBdu07hL-WUW_Zb5TJBzCG7S5kQd1_fNkOANpw7lraFXK1M0FyxXL2GcurNVtxySt2BOXi7tZTB-DkJbkneLn7qC3W24MQxIsNtvt-Euhc2ZI3cQ-3mWfyHNIkub4Bns3C5w40/s1700-e365/cpr.png)

"This malware delivery method differs from Nimbus Manticore's usual infection chains, which typically rely on career-themed phishing lures," the company said. "In this campaign, the actor abuses search engine optimization techniques by registering dozens of domains that link to the bogus domain, getsqldeveloper[.]com. This is likely an attempt to increase the site's visibility through link-based reputation signals."

MiniFast is described as a fully featured backdoor designed for long-term persistence and remote command execution. It communicates with a remote server over HTTP requests to fetch tasks, upload command execution results, exfiltrate files, and download additional payload from the server. Before entering the tasking loop, the malware also beacons basic system information to the operator.

The commands supported by the backdoor are varied, enabling file operations, directory listings, process enumeration, command execution via "cmd.exe," process termination using its PID, DLL loading, ZIP archive creation, persistence via scheduled tasks, and privilege escalation via the "runas" command.

The backdoor also supports the ability to update the polling interval and jitter value applied to beacon intervals so as to randomize the frequency with which commands are retrieved from the server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglEHwHJ13hVlZTCabx2Zw9SgaAHfCoawZYfH8Ku2bDLJ9JBM0iY8iKGx0c5iD4fCGIngeqlbaHNOmcuYu7aCpxNJGoKs5LEAEWGA3diccyKaoPa7cqyDJBwLU920JR9EH1m68F7krOTfoMpr2iOmO0qlME1CH-9VlGXL2a60z-fzQFJfsYICIwNmuDVI-5/s1700-e365/MiniUpdate.png)

"What stands out is that this group's ambitions extended well beyond targeted espionage in the Middle East," Sergey Shykevich, threat intelligence group manager at Check Po...