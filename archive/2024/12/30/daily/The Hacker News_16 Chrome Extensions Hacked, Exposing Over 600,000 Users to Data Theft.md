---
title: 16 Chrome Extensions Hacked, Exposing Over 600,000 Users to Data Theft
url: https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html
source: The Hacker News
date: 2024-12-30
fetch_date: 2025-10-06T19:37:12.679480
---

# 16 Chrome Extensions Hacked, Exposing Over 600,000 Users to Data Theft

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

# [Dozens of Chrome Extensions Hacked, Exposing Millions of Users to Data Theft](https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html)

**Dec 29, 2025**Ravie LakshmananEndpoint Protection / Browser Security

[![Chrome Extensions](data:image/png;base64... "Chrome Extensions")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhf0TaLIhru3us2482mUHwROB8pWy907nz9LpW2rQn3K3q6PnUIOl9XTENTLnAkxohRwfUXDMup6_-wbDCzSfOUwyKG6k0vHzhj9ry_x84dL4W-hqAOoYsK1cEcRbbBO4BYhZSxCG3BhqB-RU2UfV_7tfex7ukGe4g9EzykjYfzEgmwwdhyiCNdE64ZecaK/s790-rw-e365/chrome.png)

A new attack campaign has targeted known Chrome browser extensions, leading to at least 35 extensions being compromised and exposing over 2.6 million users to data exposure and credential theft.

The attack targeted publishers of browser extensions on the Chrome Web Store via a phishing campaign and used their access permissions to insert malicious code into legitimate extensions in order to steal cookies and user access tokens.

The first company to shed light the campaign was cybersecurity firm Cyberhaven, one of whose employees was targeted by a phishing attack on December 24, allowing the threat actors to publish a malicious version of the extension.

On December 27, Cyberhaven [disclosed](https://www.cyberhaven.com/blog/cyberhavens-chrome-extension-security-incident-and-what-were-doing-about-it) that a threat actor compromised its browser extension and injected malicious code to communicate with an external command-and-control (C&C) server located on the domain cyberhavenext[.]pro, download additional configuration files, and exfiltrate user data.

The phishing email, which purported to come from Google Chrome Web Store Developer Support, sought to induce a false sense of urgency by claiming that their extension was at imminent risk of removal from the extension store citing a violation of [Developer Program Policies](https://developer.chrome.com/docs/webstore/program-policies).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It also urged the recipient to click on a link to accept the policies, following which they were redirected to a page for granting permissions to a malicious OAuth application named "Privacy Policy Extension."

"The attacker gained requisite permissions via the malicious application ('Privacy Policy Extension') and uploaded a malicious Chrome extension to the Chrome Web Store," Cyberhaven [said](https://www.cyberhaven.com/engineering-blog/cyberhavens-preliminary-analysis-of-the-recent-malicious-chrome-extension) in a separate technical write-up. "After the customary Chrome Web Store Security review process, the malicious extension was approved for publication."

"Browser extensions are the soft underbelly of web security," says Or Eshed, CEO of [LayerX Security](https://layerxsecurity.com/), which specializes in browser extension security. "Although we tend to think of browser extensions as harmless, in practice, they are frequently granted extensive permissions to sensitive user information such as cookies, access tokens, identity information, and more.

"Many organizations don't even know what extensions they have installed on their endpoints, and aren't aware of the extent of their exposure."

Jamie Blasco, CTO of SaaS security company Nudge Security, [identified additional domains resolving](https://x.com/jaimeblascob/status/1872445912175534278) to the same IP address of the C&C server used for the Cyberhaven breach.

Further investigation has uncovered [more extensions](https://docs.google.com/spreadsheets/d/15xOLbYgz5DQnCWYE6a_LXGcqYC_bNPPzdBqdLofz6-E/edit?gid=0#gid=0) [Google Sheets] that are suspected of having been compromised, according to browser extension security platforms [Secure Annex](https://secureannex.com/blog/cyberhaven-extension-compromise/) and [Extension total](https://www.extensiontotal.com/cyberhaven-incident-live):

* AI Assistant - ChatGPT and Gemini for Chrome
* Bard AI Chat Extension
* GPT 4 Summary with OpenAI
* Search Copilot AI Assistant for Chrome
* TinaMInd AI Assistant
* Wayin AI
* VPNCity
* Internxt VPN
* Vidnoz Flex Video Recorder
* VidHelper Video Downloader
* Bookmark Favicon Changer
* Castorus
* Uvoice
* Reader Mode
* Parrot Talks
* Primus
* Tackker - online keylogger tool
* AI Shop Buddy
* Sort by Oldest
* Rewards Search Automator
* ChatGPT Assistant - Smart Search
* Keyboard History Recorder
* Email Hunter
* Visual Effects for Google Meet
* Earny - Up to 20% Cash Back
* Where is Cookie?
* Web Mirror
* ChatGPT App
* Hi AI
* Web3Password Manager
* YesCaptcha assistant
* Bookmark Favicon Changer
* Proxy SwitchyOmega (V3)
* GraphQL Network Inspector
* ChatGPT for Google Meet
* GPT 4 Summary with OpenAI

These additional compromised extensions indicate that Cyberhaven was not a one-off target but part of a wide-scale attack campaign targeting legitimate browser extensions.

Secure Annex's founder John Tuckner told The Hacker News that there is a possibility that the campaign has been ongoing since April 5, 2023, and likely even further back based on the registration dates of the domains used: nagofsg[.]com was registered in August 2022 and sclpfybn[.]com was registered in July 2021.

"I've linked the same code present in the Cyberhaven attacks to related code (let's say Code1) in an extension called 'Reader Mode,'" Tuckner said. "The code in 'Reader Mode' contained Cyberhaven attack code (Code1) and an additional indicator of compromise "sclpfybn[.]com" with its own additional code (Code2)."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Pivoting on that domain led me to the seven new extensions. One of those related extensions called "Rewards Search Automator" had (Code2) which masked itself as 'safe-browsing' functionality but was exfiltrating data."

"'Rewards Search Automator' also contained masked 'ecommerce' functionality (Code3) with a new domain 'tnagofsg[.]com' which is functionally incredibly si...