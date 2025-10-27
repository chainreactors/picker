---
title: Experts Detect Multi-Layer Redirect Tactic Used to Steal Microsoft 365 Login Credentials
url: https://thehackernews.com/2025/07/experts-detect-multi-layer-redirect.html
source: The Hacker News
date: 2025-08-01
fetch_date: 2025-10-07T00:49:33.590550
---

# Experts Detect Multi-Layer Redirect Tactic Used to Steal Microsoft 365 Login Credentials

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

# [Experts Detect Multi-Layer Redirect Tactic Used to Steal Microsoft 365 Login Credentials](https://thehackernews.com/2025/07/experts-detect-multi-layer-redirect.html)

**Jul 31, 2025**Ravie LakshmananPhishing / Threat Intelligence

[![Microsoft 365 Credential Theft Attempts](data:image/png;base64... "Microsoft 365 Credential Theft Attempts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1ulF8cugZ2yWSj-9HHCQQC0Hxj3aOXBCT9QRBVV28T0TwBuWRO9jTTQWHVip3ZHrtkwPM_xtLMO4CTv8bi3dG5La6FjlXtY6Jd3ShhscdYravCifcKBMP6hyphenhyphenP91u_xURqpAOmSSWCvuoxuu0cFSzJmi55MsaCfFUrWzdunKw5a24gt1mHVo4iD547q0jM/s790-rw-e365/phishing.jpg)

Cybersecurity researchers have disclosed details of a new phishing campaign that conceals malicious payloads by abusing link wrapping services from Proofpoint and Intermedia to bypass defenses.

"Link wrapping is designed by vendors like Proofpoint to protect users by routing all clicked URLs through a scanning service, allowing them to block known malicious destinations at the moment of click," the Cloudflare Email Security team [said](https://www.cloudflare.com/threat-intelligence/research/report/attackers-abusing-proofpoint-intermedia-link-wrapping-to-deliver-phishing-payloads/).

"While this is effective against known threats, attacks can still succeed if the wrapped link hasn't been flagged by the scanner at click time."

The activity, observed over the last two months, once again illustrates how threat actors find different ways to [leverage legitimate features and trusted tools](https://cofense.com/blog/google-redirect-abuse-in-2024-key-trends-tactics) to their advantage and perform malicious actions, in this case, redirecting victims to Microsoft 365 phishing pages.

It's noteworthy that the abuse of link wrapping involves the attackers gaining unauthorized access to email accounts that already use the feature within an organization, so that any email message containing a malicious URL sent from that account is automatically rewritten with the wrapped link (e.g., urldefense.proofpoint[.]com/v2/url?u=<malicious\_website>).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Another important aspect concerns what Cloudflare calls "multi-tiered redirect abuse," in which the threat actors first cloak their malicious links using a URL shortening service like Bitly, and then send the shortened link in an email message via a Proofpoint-secured account, causing it to be obscured a second time.

This behavior effectively creates a redirection chain, where the URL passes through two levels of obfuscation – Bitly and Proofpoint's URL Defense – before taking the victim to the phishing page.

In the attacks observed by the web infrastructure company, the phishing messages masquerade as voicemail notifications, urging recipients to click on a link to listen to them, ultimately directing them to a bogus Microsoft 365 phishing page designed to capture their credentials.

Alternate infection chains employ the same technique in emails that notify users of a supposed document received on Microsoft Teams and trick them into clicking on booby-trapped hyperlinks.

A third variation of these attacks impersonates Teams in emails, claiming that they have unread messages and that they can click on the "Reply in Teams" button embedded in the messages to redirect them to credential harvesting pages.

"By cloaking malicious destinations with legitimate urldefense[.]proofpoint[.]com and url[.]emailprotection URLs, these phishing campaigns' abuse of trusted link wrapping services significantly increases the likelihood of a successful attack," Cloudflare said.

When contacted by The Hacker News for comment, Proofpoint said it's aware of threat actors abusing URL redirects and URL protection in ongoing phishing campaigns, and that it's a technique the company has observed from multiple security service providers who provide similar email protection or URL rewrite solutions, such as Cisco and Sophos.

The enterprise security firm also noted that it flags these campaigns via its behavioral artificial intelligence (AI) detection engine, and messages bearing such URLs are discarded and the final URLs at the end of the redirect chain are blocked to prevent exploitation.

"In these campaigns, a threat actor can either abuse an open redirect to link to a rewritten URL, or compromise an email account that belongs to someone with some type of email protection," Proofpoint threat researchers said.

"Then, they send an email with a phishing link to the account they have compromised. The security service rewrites the URL, and the threat actor makes sure the link is not blocked. Then, the threat actor will take the rewritten URL and include it in various redirect chains."

"Whenever threat actors choose to use a re-written URL from any security service, including Proofpoint, it means that as soon as the security service blocks the final URL, the entire attack chain will be blocked for every recipient of the campaign, whether the recipient was a customer of the security service or not."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes amid a [spike](https://news.sophos.com/en-us/2025/02/05/svg-phishing/) in [phishing](https://blog.knowbe4.com/245-increase-in-svg-files-used-to-obfuscate-phishing-payloads) [attacks](https://securelist.com/svg-phishing/116256/) that [weaponize](https://www.cloudflare.com/threat-intelligence/research/report/svgs-the-hackers-canvas/) Scalable Vector Graphics ([SVG](https://www.ibm.com/think/x-force/weaponized-svgs-inside-a-global-phishing-campaign-targeting-financial-institutions)) files to [get around](https://www.ontinue.com/resource/blog-svg-smuggling/) traditional anti-spam and anti-phishing protections and initiate multi-stage malware infections.

"Unlike JPEG or PNG files, SVG files are written in XML and support JavaScript and HTML code," the New Jersey Cybersecurity and Communications Integration ...