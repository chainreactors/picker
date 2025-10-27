---
title: OAuth Redirect Flaw in Airline Travel Integration Exposes Millions to Account Hijacking
url: https://thehackernews.com/2025/01/oauth-redirect-flaw-in-airline-travel.html
source: The Hacker News
date: 2025-01-29
fetch_date: 2025-10-06T20:12:15.609255
---

# OAuth Redirect Flaw in Airline Travel Integration Exposes Millions to Account Hijacking

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

# [OAuth Redirect Flaw in Airline Travel Integration Exposes Millions to Account Hijacking](https://thehackernews.com/2025/01/oauth-redirect-flaw-in-airline-travel.html)

**Jan 28, 2025**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOUXv0_yk3eX2sxUfvsaae4dCPlljV8zmAVJl6RDy6m5fdqUWhSRmrvcMUvKZVSkbmKroQe40-YTjFcvFha4X2f38Dg6-ACzHqalZyNORNDkV8SE2m79R2obx5HQCR4j0fd0tacRZmrcEOIshrkLfSSwQ-WUiNd7HfwEHOjW6MsDRNhj4zAElsTMjN5eI2/s790-rw-e365/airline.png)

Cybersecurity researchers have disclosed details of a now-patched account takeover vulnerability affecting a popular online travel service for hotel and car rentals.

"By exploiting this flaw, attackers can gain unauthorized access to any user’s account within the system, effectively allowing them to impersonate the victim and perform an array of actions on their behalf – including booking hotels and car rentals using the victim's airline loyalty points, canceling or editing booking information, and more," API security firm Salt Labs [said](https://salt.security/blog/api-supply-chain-attacks---the-skys-the-limit) in a report shared with The Hacker News.

Successful exploitation of the vulnerability could have put millions of online airline users at risk, it added. The name of the company was not disclosed, but it said the service is integrated into "dozens of commercial airline online services" and enables users to add hotel bookings to their airline itinerary.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The shortcoming, in a nutshell, can be weaponized trivially by sending a specially crafted link that can be propagated via standard distribution channels such as email, text messages, or attacker-controlled websites. Clicking on the link is enough for the threat actor to hijack control of the victim's account as soon as the login process is complete.

Sites that integrate the rental booking service have the option to login to the latter using the credentials associated with the airline service provider, at which point the rental platform generates a link and redirects the user back to the airline's website to complete authentication via [OAuth](https://thehackernews.com/2023/05/critical-oauth-vulnerability-in-expo.html).

Once the sign in is successful, the users are directed to a website that adheres to the format "<rental-service>.<airlineprovider>.sec," from where they can use their airline loyalty points to book hotels and car rentals.

The attack method devised by Salt Labs involves redirecting the authentication response from the airline site, which includes the user's session token, to a site under the attacker's control by manipulating a "tr\_returnUrl" parameter, effectively allowing them to access the victim's account in an unauthorized manner, including their personal information.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Since the manipulated link uses a legitimate customer domain (with manipulation occurring only at the parameter level rather than the domain level), this makes the attack difficult to detect through standard domain inspection or blocklist/allowlist methods," security researcher Amit Elbirt said.

Salt Labs has described service-to-service interactions as a lucrative vector for API supply chain attacks, wherein an adversary targets the weaker link in the ecosystem to break into systems and steal private customer data.

"Beyond mere data exposure, attackers can perform actions on behalf of the user, such as creating orders or modifying account details," Elbirt added. "This critical risk highlights the vulnerabilities in third-party integrations and the importance of stringent security protocols to protect users from unauthorized account access and manipulation."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[account takeover](https://thehackernews.com/search/label/account%20takeover)[API Security](https://thehackernews.com/search/label/API%20Security)[Authentication](https://thehackernews.com/search/label/Authentication)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data privacy](https://thehackernews.com/search/label/data%20privacy)[Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP ...