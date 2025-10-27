---
title: Phishing Campaign Uses UpCrypter in Fake Voicemail Emails to Deliver RAT Payloads
url: https://thehackernews.com/2025/08/phishing-campaign-uses-upcrypter-in.html
source: The Hacker News
date: 2025-08-26
fetch_date: 2025-10-07T00:50:44.139198
---

# Phishing Campaign Uses UpCrypter in Fake Voicemail Emails to Deliver RAT Payloads

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

# [Phishing Campaign Uses UpCrypter in Fake Voicemail Emails to Deliver RAT Payloads](https://thehackernews.com/2025/08/phishing-campaign-uses-upcrypter-in.html)

**Aug 25, 2025**Ravie LakshmananMalware / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglw0T7Z0nG4FzLOEDAtjMBNAhsLUkI6kgiUFV8N91SBKhVVCO94H0gtmAR0t4ToHAzgB6vxlVpKXbOO0xXzr64urfmtMQH3O4e7r21n7G-RwwG2kWJlg-3dKUPCNJISnRdLoldwL9rYJSASCJHbCIa4N2reiVeczen6Pp251UHSXNvOIvFXrnvrtjryGY8/s790-rw-e365/CYBER.jpg)

Cybersecurity researchers have flagged a new phishing campaign that's using fake voicemails and purchase orders to deliver a malware loader called **UpCrypter**.

The campaign leverages "carefully crafted emails to deliver malicious URLs linked to convincing phishing pages," Fortinet FortiGuard Labs researcher Cara Lin [said](https://www.fortinet.com/blog/threat-research/phishing-campaign-targeting-companies-via-upcrypter). "These pages are designed to entice recipients into downloading JavaScript files that act as droppers for UpCrypter."

Attacks propagating the malware have been primarily targeting manufacturing, technology, healthcare, construction, and retail/hospitality sectors across the world since the start of August 2025. The vast majority of the infections have been observed in Austria, Belarus, Canada, Egypt, India, and Pakistan, among others.

UpCrypter functions as a conduit for various remote access tools (RATs), such as [PureHVNC RAT](https://thehackernews.com/2025/05/fake-kling-ai-facebook-ads-deliver-rat.html), [DCRat](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html) (aka DarkCrystal RAT), and [Babylon RAT](https://thehackernews.com/2024/02/new-mispadu-banking-trojan-exploiting.html), each of which enable an attacker to take full control of compromised hosts.

The starting point of the infection chain is a phishing email using themes related to voicemail messages and purchases to deceive recipients into clicking on links that direct to fake landing pages, from where they are prompted to download the voice message or a PDF document.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The lure page is designed to appear convincing by not only displaying the victim's domain string in its banner but also fetching and embedding the domain's logo within the page content to reinforce authenticity," Fortinet said. "Its primary purpose is to deliver a malicious download."

The downloaded payload is a ZIP archive containing an obfuscated JavaScript file, which subsequently contacts an external server to fetch the next-stage malware, but only after confirming internet connectivity and scanning running processes for forensic tools, debuggers, or sandbox environments.

The loader, in turn, contacts the same server to obtain the final payload, either in the form of plain text or embedded within a harmless-looking image, a technique called steganography.

Fortinet said UpCrypter is also distributed as an MSIL (Microsoft Intermediate Language) loader that, like its JavaScript counterpart, conducts anti-analysis and anti-virtual machine checks, after which it downloads three different payloads: an obfuscated PowerShell script, a DLL, and the main payload.

The attack culminates with the script embedding data from the DLL loader and the payload during execution, thus allowing the malware to be run without writing it to the file system. This approach also has the advantage of minimizing forensic traces, thereby allowing the malware to fly under the radar.

"This combination of an actively maintained loader, layered obfuscation, and diverse RAT delivery demonstrates an adaptable threat delivery ecosystem capable of bypassing defenses and maintaining persistence across different environments," Lin said.

The disclosure comes as Check Point detailed a large-scale phishing campaign abusing Google Classroom to distribute more than 115,000 phishing emails aimed at 13,500 organizations across multiple industries between August 6 and 12, 2025. The attacks target organizations in Europe, North America, the Middle East, and Asia.

"Attackers exploited this trust by sending fake invitations that contained unrelated commercial offers, ranging from product reselling pitches to SEO services," the company [said](https://blog.checkpoint.com/email-security/phishing-in-the-classroom-115000-emails-exploit-google-classroom-to-target-13500-organizations/). "Each email directed recipients to contact scammers via a WhatsApp phone number, a tactic often linked to fraud schemes."

The attack bypasses security systems because it leverages the trust and reputation of Google Classroom's infrastructure to bypass key email authentication protocols, such as SPF, DKIM, and DMARC, and helps land the phishing emails in users' inboxes.

These campaigns are part of a larger trend where threat actors take advantage of legitimate services like [Microsoft 365 Direct Send](https://thehackernews.com/2025/07/hackers-using-pdfs-to-impersonate.html) and [OneNote](https://thehackernews.com/2023/04/microsoft-tightens-onenote-security-by.html), not to mention abuse free artificial intelligence (AI)-powered website builders like [Vercel v0](https://thehackernews.com/2025/07/vercels-v0-ai-tool-weaponized-by.html) and Flazio, as well as other platforms such as [Discord CDN](https://sublime.security/blog/multi-rmm-attack-splashtop-streamer-and-atera-payloads-delivered-via-discord-cdn-link/), [SendGrid](https://cofense.com/blog/phishing-in-the-cloud-sendgrid-campaign-exploits-account-security), [Zoom](https://sublime.security/blog/living-off-trusted-sites-zoom-service-abuse-credential-phishing-attack/), ClickFunnels, Jotform, and X's [t[.]co](https://sublime.security/blog/using-the-x-twitter-link-shortener-t-co-to-hide-an-aitm-credential-phishing-payload/) link shortener – an approach known as [living-off-trusted-sites](https://sublime.security/blog/phishing-for-xfinity-credentials-with-...