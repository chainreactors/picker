---
title: How 'Browser-in-the-Middle' Attacks Steal Sessions in Seconds
url: https://thehackernews.com/2025/05/how-browser-in-middle-attacks-steal.html
source: The Hacker News
date: 2025-05-29
fetch_date: 2025-10-06T22:32:07.224916
---

# How 'Browser-in-the-Middle' Attacks Steal Sessions in Seconds

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

# [How 'Browser-in-the-Middle' Attacks Steal Sessions in Seconds](https://thehackernews.com/2025/05/how-browser-in-middle-attacks-steal.html)

**May 28, 2025**The Hacker NewsBrowser Security / Credential Theft

[![Browser-in-the-Middle](data:image/png;base64... "Browser-in-the-Middle")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqUfE7vhQlt_FGPQxgDpoGbuzlbx9Qj3QO4ml9ugy8GBIfP9plavq2jrkz1OInbXzyFw4HHl2RINtlelpKlxgJAppkGfsxwBAh8c7zIqKSKY0FOaneNzYp3uKHJm14r03kiV_w-F7nbWgr-Un6lYo1Wn9Lpz9e54D9XRSWCuHo0hSrPoBKqWYdUfK9xAI/s790-rw-e365/BANKING.jpg)

Would you expect an end user to log on to a cybercriminal's computer, open their browser, and type in their usernames and passwords? Hopefully not! But that's essentially what happens if they fall victim to a Browser-in-the-Middle (BitM) attack.

Like Man-in-the-Middle (MitM) attacks, BiTM sees criminals look to [control the data flow between the victim's computer and the target service](https://link.springer.com/article/10.1007/s10207-021-00548-5), as University of Salento researchers Franco Tommasi, Christian Catalano, and Ivan Taurino have outlined in a paper for the International Journal of Information Security. However, there are several key differences.

## Man-in-the-Middle vs Browser-in-the-Middle

A MiTM attack utilizes a proxy server that places itself between the victim's browser and the legitimate target service at the application layer. It needs some kind of malware to be placed and run on the victim's computer.

But a BiTM attack is different. Instead, the victim thinks they're using their own browser – conducting their normal online banking, for instance – when instead they're actually running a transparent remote browser.

As the paper notes, it's as though the user were "sitting in front of the attacker's computer, using the attacker's keyboard", meaning the attacker can capture, record, and alter the data exchange between the victim and the service they're accessing.

## Anatomy of a BiTM attack

So how does it work? A typical BitM attack occurs in three phases:

1. **Phishing:** The victim is tricked into clicking on a malicious hyperlink that points to the attacker's server and authenticates their web application.
2. **Fake browser:** The victim is connected to the attacker's server and to the transparent web browser via the insertion of malicious javascript. The attack will utilize programs such as keyloggers to empower the criminals to intercept and utilize the victim's data.
3. **Targeting web applications:** The victim uses all their usual services online, without realizing that they are utilizing a transparent browser. Their credentials are now exposed to the criminal.

## Session tokens

The attack works by [targeting session tokens](https://cloud.google.com/blog/topics/threat-intelligence/session-stealing-browser-in-the-middle). This enables the attackers to subvert even multi-factor authentication (MFA); once the user has finished their MFA, a session token is usually stored in their browser. [As researchers from Google subsidiary Mandiant have noted](https://cloud.google.com/blog/topics/threat-intelligence/session-stealing-browser-in-the-middle), if the token itself can be stolen, then MFA no longer matters:

"Stealing this session token is the equivalent of stealing the authenticated session, meaning an adversary would no longer need to perform the MFA challenge." This makes the tokens a useful target for both red team operators – who test a system's defenses – and more worryingly, genuine adversaries.

By employing a BitM framework in targeting authenticated session tokens, attackers enjoy the benefits of a rapid targeting capability, as they can reach any website in just seconds with little need for configuration, notes Mandiant. When an application is targeted, the legitimate site is served through the attacker-controlled browser, making it extremely difficult for the victim to tell the difference between a real site and its fake counterpart.

Cookies or OAuth tokens are snatched just before encryption, while rapid exfiltration means the stolen tokens can be relayed to attacker servers in seconds.

## Mitigation strategies

These sophisticated attacks can cause significant damage, but there are ways to avoid or mitigate the consequences. At the widest level, users must always take extreme care over the links they access, perhaps previewing the site before actually clicking on any links. Here are some other options:

* **Extension control**: It could make sense to [enforce enterprise-wide whitelists/blacklists via browser policies](https://www.csoonline.com/article/569493/whitelisting-explained-how-it-works-and-where-it-fits-in-a-security-program.html), permitting system access only for approved actions or entities. However, it's a blunt tool and can be time-consuming to enforce.
* **Token hardening**: Issue short-lived, rotating tokens with sliding expiration. This provides in-built security in the case of stolen or [leaked tokens](https://cloud.google.com/apigee/docs/api-platform/antipatterns/oauth-long-expiration#:~:text=Best%20practice,-Use%20an%20expiration&text=A%20good%20starting%20point%20for,lifetime%20of%20the%20access%20tokens.).
* **Content Security Policy (CSP)**: A robust CSP tool [enables developers to lock down applications, reducing vulnerability to content injection](https://www.w3.org/TR/CSP3/) and other threats.
* **Behavioral monitoring**: Send any browser-level telemetry to [security information and event management (SIEM) tools](https://www.microsoft.com/en-gb/security/business/security-101/what-is-siem). Alert on unusual API calls or token refresh patterns.
* **Browser isolation**: Run risky sites in sandboxed containers or remote browsing services.
* **Test your defenses:** Quarterly red-team drills that address browser-based threats can also help identify any vulnerabilities in your browsers.

## Passwords in a New Era

The conclusion is depressingly clear: BiTM attacks can circumvent traditional security approaches,...