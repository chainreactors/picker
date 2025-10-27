---
title: Session Hijacking 2.0 — The Latest Way That Attackers are Bypassing MFA
url: https://thehackernews.com/2024/09/session-hijacking-20-latest-way-that.html
source: The Hacker News
date: 2024-10-01
fetch_date: 2025-10-06T18:56:08.946868
---

# Session Hijacking 2.0 — The Latest Way That Attackers are Bypassing MFA

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

# [Session Hijacking 2.0 — The Latest Way That Attackers are Bypassing MFA](https://thehackernews.com/2024/09/session-hijacking-20-latest-way-that.html)

**Sep 30, 2024**The Hacker NewsIdentity Theft / Phishing Attack

[![Session Hijacking 2.0](data:image/png;base64... "Session Hijacking 2.0")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGW0lZj7oHgxlFyqyVYeABeWOtJ0f1yCo3uEtX7NYKEKjBwWGxTN4cgCKVVMxMOLkuNHPKtSPE4JJh9OwZqiYpWZhuSp3Ot27UDre4KFVk6L_KJVG9vkDlTUiGbMLgsasP555PC2FXHoW_5GMSOXagojvR5U8va1D4KhaJjKpG5OX5F5Fwsm7N67qF0CA/s790-rw-e365/session-hijacking.png)

Attackers are increasingly turning to session hijacking to get around widespread MFA adoption. The [data supports this](https://pushsecurity.com/blog/what-the-rise-of-infostealers-says-about-identity-attacks/#id-the-state-of-infostealers-today), as:

* 147,000 token replay attacks were detected by Microsoft in 2023, a 111% increase year-over-year (Microsoft).
* Attacks on session cookies now happen in the same order of magnitude as password-based attacks (Google).

But session hijacking isn't a new technique – so what's changed?

## **Session hijacking has a new look**

When we think of the classic example of session hijacking, we think of old-school Man-in-the-Middle (MitM) attacks that involved snooping on unsecured local network traffic to capture credentials or, more commonly, financial details like credit card data. Or, by conducting client-side attacks compromising a webpage, running malicious JavaScript and using cross-site scripting (XSS) to steal the victim's session ID.

Session hijacking looks quite different these days. No longer network-based, modern session hijacking is an identity-based attack performed over the public internet targeting cloud-based apps and services.

While the medium is different, the objectives are largely the same: Steal valid session material – cookies, tokens, IDs – in order to resume the session from the attacker's device (a different remote device, browser, and location).

Unlike legacy session hijacking, which often fails when faced with basic controls like encrypted traffic, VPNs, or MFA, modern session hijacking is much more reliable in bypassing standard defensive controls.

It's also worth noting that the context of these attacks has changed a lot. Whereas once upon a time you were probably trying to steal a set of domain credentials used to authenticate to the internal Active Directory as well as your email and core business apps, nowadays the identity surface looks very different – with tens or hundreds of separate accounts per user across a sprawling suite of cloud apps.

## **Why do attackers want to steal your sessions?**

**In short: Stealing live sessions enables attackers to bypass authentication controls like MFA.** If you can hijack an existing session, you have fewer steps to worry about – no messing about with converting stolen usernames and passwords into an authenticated session.

While in theory session tokens have a limited lifetime, in reality, they can remain valid for longer periods (usually around 30 days) or even indefinitely as long as activity is maintained.

As mentioned above, there's a lot that an attacker can gain from compromising an identity. If it's an IdP identity like an Okta or Entra account with SSO access to your downstream apps, perfect! If not, well maybe it's a valuable app (like Snowflake, perhaps?) with access to the bulk of your customer data. Or maybe it's a less attractive app, but with interesting integrations that can be exploited instead.

It's no surprise that identity is being talked about as the new security perimeter, and that identity-based attacks continue to hit the headlines.

[If you want to know more about the state of identity attacks in the context of SaaS apps, check out this report looking back on 2023/4.](https://pushsecurity.com/resources/book/saas-attacks-report/?utm_source=ext&utm_medium=paid&utm_content=hn)

Not all methods of session hijacking are the same, however, which means that they react differently to the controls they come up against. This creates different pros and cons based on the attacker's chosen approach.

## **Comparing session hijacking approaches**

To hijack a session, you need to first steal the session cookies associated with a live user session. In the modern sense, there are two main approaches to this:

* Using modern phishing toolkits such as AitM and BitM.
* Using tools that target browser data such as infostealers.

It's worth noting that both of these methods target both typical credential material (e.g. usernames and passwords) as well as session cookies. Attackers aren't necessarily making a choice to go after session cookies instead of passwords – rather, the tools they're using support both, widening the means available to them. If accounts without MFA are identified (and there are still a lot of those) then passwords will do just fine.

### Modern phishing attacks: AitM and BitM

Modern phishing toolkits see the victim complete any MFA checks as part of the process. In the case of AitM, the tool acts as a proxy, meaning the attacker can intercept all the authentication material – including secrets such as session tokens. BitM goes one step further and sees the victim tricked into remotely controlling the attacker's browser – the virtual equivalent of an attacker handing their laptop to their victim, asking them to login to Okta for them, and then taking their laptop back afterward.

Unlike traditional MitM which is often highly opportunistic, AitM tends to be much more targeted – as it's the product of a phishing campaign. While AitM scales much better than traditional MitM attacks (which were very local) with AitM you're naturally focused on accounts belonging to a specific application or service based on whatever app you're emulating, or site you're impersonating.

[We talked about AitM and BitM phishing and how to detect and block it in much more detail in a recent Hacker News article: If you missed it, check it ...