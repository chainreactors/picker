---
title: Researchers Expose PWA JavaScript Attack That Redirects Users to Adult Scam Apps
url: https://thehackernews.com/2025/05/researchers-expose-pwa-javascript.html
source: The Hacker News
date: 2025-05-22
fetch_date: 2025-10-06T22:37:42.200742
---

# Researchers Expose PWA JavaScript Attack That Redirects Users to Adult Scam Apps

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

# [Researchers Expose PWA JavaScript Attack That Redirects Users to Adult Scam Apps](https://thehackernews.com/2025/05/researchers-expose-pwa-javascript.html)

**May 21, 2025**Ravie LakshmananMobile Security / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhydi4fQLPSBhlVYVzutq0_FgZWIesILSmMyeE7x5Q0XPXMANqsyjuLYFISEr6NeszIBN44TUw19bho4j8xx6Tzxz2bUa-1JtGN7kH1sKM9NWVApgrlWxR-GHhwBO5PhyphenhyphenmRmB83_lKt-e5V2VTANLDmCd8awr_tv1Q8-FRXHEIx7pWV2KiS2bMCyrbCyUbS/s790-rw-e365/js-malware.jpg)

Cybersecurity researchers have discovered a new campaign that employs malicious JavaScript injections to redirect site visitors on mobile devices to a Chinese adult-content Progressive Web App (PWA) scam.

"While the payload itself is nothing new (yet another adult gambling scam), the delivery method stands out," c/side researcher Himanshu Anand [said](https://cside.dev/blog/chinese-adult-content-scam-targets-mobile-users-through-pwa-injection) in a Tuesday analysis.

"The malicious landing page is a full-blown Progressive Web App ([PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/What_is_a_progressive_web_app)), likely aiming to retain users longer and bypass basic browser protections."

The campaign is designed to explicitly filter out desktop users, primarily focusing on mobile users. The activity has been described as a client-side attack that uses third-party JavaScript and only triggers on mobile devices.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The use of PWAs, a type of application built using web technologies that provide a user experience similar to that of a native app built for a specific platform like Windows, Linux, macOS, Android, or iOS, is seen as an attempt to sidestep security protections.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVW9_7srILA5_zUt3EnrIKeWKezErKB7V6RQp94-38OoladE2Tkdkm3r9zoDVVvOA1TPn9EXN9LLOabgVgtsVqQ0eUfZIxrvqBs6cnhOSu4eDe0bdMSbQapn9gXQC4PrHtLDOcCb6nsESKlkfmj4CrPzWk0pFFvKxMTfq8drqmXvcK28XLPJvIOwWunSSv/s790-rw-e365/apps.jpg)

The attacks involve injecting websites with JavaScript code that acts as a loader to trigger the redirection when the site is visited from devices running on Android, iOS, and iPadOS, among others.

The redirections are designed to lead the users to adult content websites or other intermediary redirect pages advertising apps for viewing adult content. The pages subsequently take the victims to a fake app store listing for the supposed Android and iOS apps in question.

"The use of PWAs suggests attackers are experimenting with more persistent phishing methods," Anand said. "The mobile-only focus allows them to evade many detection mechanisms."

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

[Android](https://thehackernews.com/search/label/Android)[browser security](https://thehackernews.com/search/label/browser%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[iOS](https://thehackernews.com/search/label/iOS)[JavaScript](https://thehackernews.com/search/label/JavaScript)[mobile security](https://thehackernews.com/search/label/mobile%20security)[Phishing](https://thehackernews.com/search/label/Phishing)[Progressive Web Apps](https://thehackernews.com/search/label/Progressive%20Web%20Apps)[scam](https://thehackernews.com/search/label/scam)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More")

⚡ Weekly Recap: Oracle 0-Day, BitLocker Bypass, VMScape, WhatsApp Worm and More](https://thehackernews.com/2025/10/weekly-recap-oracle-0-day-bit...