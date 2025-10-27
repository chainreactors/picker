---
title: North Korea Uses GitHub in Diplomat Cyber Attacks as IT Worker Scheme Hits 320+ Firms
url: https://thehackernews.com/2025/08/north-korea-uses-github-in-diplomat.html
source: The Hacker News
date: 2025-08-21
fetch_date: 2025-10-07T00:50:48.855568
---

# North Korea Uses GitHub in Diplomat Cyber Attacks as IT Worker Scheme Hits 320+ Firms

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [North Korea Uses GitHub in Diplomat Cyber Attacks as IT Worker Scheme Hits 320+ Firms](https://thehackernews.com/2025/08/north-korea-uses-github-in-diplomat.html)

**Aug 20, 2025**Ravie LakshmananCyber Espionage / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaFqPEijE5RkgBG-Yxd25JY3N4pTzdCj-P_TwuKg-mHi5ZR-BfH-22ZHQHl8YUpDDqfzQVlQu-X94QUohgVzA9bdx0ACqnLYbJP2YPYvqoiV-7bul8hRjMU7A9u28ETszlqcLZljnC9xLI4HB8eztuhGHXB6HQIQsnTaYXK3mCezEVYUJioMbu36O1Xeib/s790-rw-e365/github.jpg)

North Korean threat actors have been attributed to a coordinated cyber espionage campaign targeting diplomatic missions in their southern counterpart between March and July 2025.

The activity manifested in the form of at least 19 spear-phishing emails that impersonated trusted diplomatic contacts with the goal of luring embassy staff and foreign ministry personnel with convincing meeting invites, official letters, and event invitations.

"The attackers leveraged GitHub, typically known as a legitimate developer platform, as a covert command-and-control channel," Trellix researchers Pham Duy Phuc and Alex Lanstein [said](https://www.trellix.com/blogs/research/dprk-linked-github-c2-espionage-campaign/).

The infection chains have been observed to rely on trusted cloud storage solutions like Dropbox and Daum Cloud, an online service from South Korean internet conglomerate Kakao Corporation, in order to deliver a variant of an open-source remote access trojan called Xeno RAT that grants the threat actors to take control of compromised systems.

The campaign is assessed to be the work of a North Korean hacking group called Kimsuky, which was [recently linked](https://thehackernews.com/2025/07/north-korean-hackers-target-web3-with.html#kimsuky-s-use-of-clickfix-continues) to phishing attacks that employ GitHub as a stager for an Xeno RAT known as MoonPeak. Despite the infrastructure and tactical overlaps, there are indications that the phishing attacks match China-based operatives.

The email messages, per Trellix, are carefully crafted to appear legitimate, often spoofing real diplomats or officials so as to entice recipients into opening password-protected malicious ZIP files hosted on Dropbox, Google Drive, or Daum. The messages are written in Korean, English, Persian, Arabic, French, and Russian.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The spear-phishing content was carefully crafted to mimic legitimate diplomatic correspondence," Trellix said. "Many emails included official signature, diplomatic terminology, and references to real events (e.g., summits, forums, or meetings)."

"The attackers impersonated trusted entities (embassies, ministries, international organizations), a long-running Kimsuky tactic. By strategically timing lures alongside real diplomatic happenings, they enhanced the credibility."

Present within the ZIP archive is a Windows shortcut (LNK) masquerading as a PDF document, launching which results in the execution of PowerShell code that, in turn, runs an embedded payload, which reaches out to GitHub for fetching next-stage malware and establishes persistence through scheduled tasks. In parallel, a decoy document is displayed to the victims.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE0CphDsCvPz9trkD5fp3JVKPfjoLuuASLlPHV4AaG0i7jgnXd6KRMVmAU2St0zsLN4B5fRNb7S0uJAbIJN0jf2C56ysj-4OGqNuT_-B9pGUj_mlbFugziAD2TV7B-GkuAlxYX6-i9Pp7-HTEdWDPWxZHRnXXZBQju8Cs4hBAKFCU0L-T55r3nmdRfBqGT/s790-rw-e365/espionage-campaign-1.jpg)

The script is also designed to harvest system information and exfiltrate the details to an attacker-controlled private GitHub repository, while simultaneously retrieving additional payloads by parsing the contents of a text file ("onf.txt") in the repository to extract the Dropbox URL hosting the MoonPeak trojan.

"By simply updating onf.txt in the repository (pointing to a new Dropbox file), the operators could rotate payloads to infected machines," Trellix explained.

"They also practiced 'rapid' infrastructure rotation: log data suggests that the ofx.txt payload was updated multiple times in an hour to deploy malware and to remove traces after use. This rapid update cycle, combined with the use of cloud infrastructure, helped the malicious activities fly under the radar."

Interestingly, the cybersecurity company's time-based analysis of the attackers' activity has found it to be largely originating from a timezone that's consistent with China, with a smaller proportion aligning with that of the Koreas. To add to the intrigue, a "perfect 3-day pause" was observed coinciding with Chinese national holidays in early April 2025, but not during North or South Korean holidays.

This has raised the possibility that the campaign, mirroring Chinese operational cadence while operating with motives that align with North Korea, is likely the result of -

* North Korean operatives working from Chinese territory
* A Chinese APT operation mimicking Kimsuky techniques, or
* A collaborative effort leveraging Chinese resources for North Korean intelligence gathering efforts

With North Korean cyber actors [frequently stationed](https://thehackernews.com/2021/02/us-charges-3-north-korean-hackers-over.html#canadian-american-citizen-charged-for-money-laundering) in [China and Russia](https://www.csis.org/analysis/hidden-enablers-third-countries-north-koreas-cyber-playbook), as observed in the case of the [remote information technology (IT) worker fraud scheme](https://thehackernews.com/2025/07/us-sanctions-firm-behind-n-korean-it.html), Trellix said with medium-confidence that the operators are operating from China or are culturally Chinese.

"The use of Korean services and infrastructure was likely intentional to blend into the South Korean network," Trellix said. "It's a known Kimsuky trait to operate out of Chinese and Russian IP space while targeting South Korea, often u...