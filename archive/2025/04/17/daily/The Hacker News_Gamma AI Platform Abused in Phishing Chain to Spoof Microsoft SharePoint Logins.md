---
title: Gamma AI Platform Abused in Phishing Chain to Spoof Microsoft SharePoint Logins
url: https://thehackernews.com/2025/04/ai-powered-gamma-used-to-host-microsoft.html
source: The Hacker News
date: 2025-04-17
fetch_date: 2025-10-06T22:09:26.666779
---

# Gamma AI Platform Abused in Phishing Chain to Spoof Microsoft SharePoint Logins

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

# [Gamma AI Platform Abused in Phishing Chain to Spoof Microsoft SharePoint Logins](https://thehackernews.com/2025/04/ai-powered-gamma-used-to-host-microsoft.html)

**Apr 16, 2025**Ravie LakshmananEmail Security / Artificial Intelligence

[![Sophisticated Email Attack Chain](data:image/png;base64... "Sophisticated Email Attack Chain")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUX8-S1oNTLuCWMAeYNrmyP1CdUMWxVnirYiO5jyS55ZR498Gx9ebnVOGHhgYMmuDdN251l6IxWjg9VxHFjoO6lMONzRLpqTVoF2puglLc-1ZLR66QPo9P5deoVFRNBwY6GwZJtm2cZJLnC_6s0-D7jf8pTYe99xtHhT8exPGV0oYqDPQXaU0Q9Ni7Qodm/s790-rw-e365/phishing.jpg)

Threat actors are leveraging an artificial intelligence (AI) powered presentation platform named [Gamma](https://gamma.app) in phishing attacks to direct unsuspecting users to spoofed Microsoft login pages.

"Attackers weaponize Gamma, a relatively new AI-based presentation tool, to deliver a link to a fraudulent Microsoft SharePoint login portal," Abnormal Security researchers Callie Hinman Baron and Piotr Wojtyla [said](https://abnormal.ai/blog/multi-stage-phishing-attack-gamma-presentation) in a Tuesday analysis.

The attack chain commences with a phishing email, in some cases sent from legitimate, compromised email accounts, to entice message recipients into opening an embedded PDF document.

In reality, the PDF attachment is nothing but a hyperlink that, when clicked, redirects the victim to a presentation hosted on Gamma that prompts them to click on a button to "Review Secure Documents."

Doing so takes the user to an intermediate page that impersonates Microsoft and instructs them to complete a Cloudflare Turnstile verification step before accessing the supposed document. This CAPTCHA barrier serves to increase the legitimacy of the attack, as well as prevent automated URL analysis by security tools.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Targets are then taken to a phishing page that masquerades as a Microsoft SharePoint sign-in portal and aims to collect their credentials.

"If mismatched credentials are provided, it triggers an 'Incorrect password' error, which indicates the perpetrators are using some sort of [adversary-in-the-middle](https://news.sophos.com/en-us/2025/03/28/stealing-user-credentials-with-evilginx/) ([AiTM](https://abnormal.ai/blog/adversary-in-the-middle-dropbox-phishing-open-enrollment)) for validating credentials in real time," the researchers noted.

The findings are part of an ongoing trend of phishing attacks that exploit legitimate services to stage malicious content and bypass email authentication checks like SPF, DKIM, and DMARC, a technique called living-off-trusted-sites ([LOTS](https://thehackernews.com/2024/10/microsoft-detects-growing-use-of-file.html)).

"This clever, multi-stage attack shows how today's threat actors are taking advantage of the blind spots created by lesser-known tools to sidestep detection, deceive unsuspecting recipients, and compromise accounts," the researchers said.

[![Sophisticated Email Attack Chain](data:image/png;base64... "Sophisticated Email Attack Chain")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiSlt2bkNOPxOOirrH2VZY8nj66zGUpEJbuwDCJxSA7lSlTi2XHotDQFj0FXUy8QVCyCrTKokJ4QhlzQUVa99W2nZMAGlFsD6ckr4DS3r0PBTVHGRbh60eq_NitCvAr4c0swC9NDMnZV7HejC3n1JbO-Q0LHxb54CCMaJG7AtGUCUjfQvFtiJMkJS2Xrn4/s790-rw-e365/ms.png)

"Rather than linking directly to a credential-harvesting page, the attackers route the user through several intermediary steps: first to the Gamma-hosted presentation, then to a splash page protected by a Cloudflare Turnstile, and finally to a spoofed Microsoft login page. This multi-stage redirection hides the true destination and makes it difficult for static link analysis tools to trace the attack path."

The disclosure comes as Microsoft, in its [latest Cyber Signals report](https://news.microsoft.com/cyber-signals/), warned of an increase in AI-driven fraud attacks to generate believable content for attacks at scale using deepfakes, voice cloning, phishing emails, authentic-looking fake websites, and bogus job listings.

"AI tools can scan and scrape the web for company information, helping attackers build detailed profiles of employees or other targets to create highly convincing social engineering lures," the company said.

"In some cases, bad actors are luring victims into increasingly complex fraud schemes using fake AI-enhanced product reviews and AI-generated storefronts, where scammers create entire websites and e-commerce brands, complete with fake business histories and customer testimonials."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Microsoft also said it has taken action against attacks orchestrated by [Storm-1811](https://thehackernews.com/2025/04/phishing-campaigns-use-real-time-checks.html) (aka STAC5777), which has abused Microsoft Quick Assist software by posing as IT support through voice phishing schemes conducted via Teams and convincing victims to grant them remote device access for subsequent ransomware deployment.

That said, there is evidence to suggest that the cybercrime group behind the Teams vishing campaign may be shifting tactics. According to a new report from ReliaQuest, the attackers have been observed employing a previously unreported persistence method using [TypeLib COM hijacking](https://cicada-8.medium.com/hijack-the-typelib-new-com-persistence-technique-32ae1d284661) and a new PowerShell backdoor to evade detection and maintain access to compromised systems.

The threat actor is said to have been developing versions of the PowerShell malware since January 2025, deploying early iterations via malicious Bing advertisements. The activity, detected two months later, targeted customers in the finance and professional, scientific, and technical services sectors, specifically focusing on executive-level employees with female-sounding names.

[![](data:image/png;base64...)](https://blogge...