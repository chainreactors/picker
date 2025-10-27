---
title: Google Chrome Can Now Auto-Change Compromised Passwords Using Its Built-In Manager
url: https://thehackernews.com/2025/05/google-chrome-can-now-auto-change.html
source: The Hacker News
date: 2025-05-22
fetch_date: 2025-10-06T22:37:44.071354
---

# Google Chrome Can Now Auto-Change Compromised Passwords Using Its Built-In Manager

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

# [Google Chrome's Built-in Manager Lets Users Update Breached Passwords with One Click](https://thehackernews.com/2025/05/google-chrome-can-now-auto-change.html)

**May 21, 2025**Ravie LakshmananData Breach / Account Security

[![Auto-Change Compromised Passwords](data:image/png;base64... "Auto-Change Compromised Passwords")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifLMUdmPeilN25wmi9Q3ZlHfJfLZ1oE07Re2k_RBYQq35ZW7xJVyIGoM5xIR-KX76qQng3wBcfcQ81Cq0JZvjV9mgm5vxwRijGQjLHI-Wf8lN1dEP0yIcPBS8ZxjXawg1ACZFOPUMYva9hyphenhyphenNtaCEqN0VtduA5l1CBqu_DiCsgt6Bk0naRluTdQZ7_UWnyp/s790-rw-e365/chrome.gif)

Google has announced a new feature in its Chrome browser that lets its built-in Password Manager automatically change a user's password when it detects the credentials to be compromised.

"When Chrome detects a compromised password during sign in, Google Password Manager prompts the user with an option to fix it automatically," Google's Ashima Arora, Chirag Desai, and Eiji Kitamura [said](https://developer.chrome.com/blog/io25-web-identity). "On supported websites, Chrome can generate a strong replacement and update the password for the user automatically."

The feature builds upon [Password Manager](https://passwords.google.com/intro)'s existing capabilities to generate strong passwords during sign-up and flag credentials that have been detected in a data breach.

Google told The Hacker News the feature hasn't been formally launched for end users, and that it's mainly geared towards developers so they can optimize their websites for once the feature launches.

With the automated password change, Google said the idea is to reduce friction and help users keep their accounts secure without having to search for relevant account settings or abandon the process midway.

Website owners can support this feature by [adopting](https://web.dev/articles/change-password-url) the following methods -

* Use autocomplete="current-password" and autocomplete="new-password" to trigger autofill and storage
* Set up a [redirect](https://web.dev/articles/change-password-url) from <your-website-domain>/.well-known/change-password to the password change form on their website

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"It would be much easier if password managers could navigate the user directly to the change-password URL," Kitamura [said](https://web.dev/articles/change-password-url). "This is where a well-known URL for changing passwords becomes useful."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK_IjeUvceCFsecewYKlaNf9byIqTZBsX6WsLPUSy7S1_zyl5M2g6V1CqvXQn0-xgr6dXmWDAPESO4cYURnwl4n5l7X2U1aD-K1jQ7VETR6XhVLxHyaBVgpUqsjhSbv8LtwN-GiPkI_9PvVEoY9JcMgdtcsp2azQE4TcqpBTfAG5KiSqo8bEfa1HyPEb1A/s790-rw-e365/google.png)

"By reserving a well-known URL path that redirects the user to the change password page, the website can easily redirect users to the right place to change their passwords."

The development comes as companies are increasingly shifting to passkeys as a stronger alternative to protect accounts from potential takeover attacks. Earlier this month, Microsoft [said](https://thehackernews.com/2025/05/microsoft-sets-passkeys-default-for-new.html) it's making passkeys the default method when signing up for new customer accounts.

*(The story was updated after publication to make it clear that the feature is yet to be officially rolled out to end users.)*

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

[Account security](https://thehackernews.com/search/label/Account%20security)[Authentication](https://thehackernews.com/search/label/Authentication)[Chrome](https://thehackernews.com/search/label/Chrome)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Google](https://thehackernews.com/search/label/Google)[Passkeys](https://thehackernews.com/search/label/Passkeys)[password manager](https://thehackernews.com/search/label/password%20manager)[Web Development](https://thehackernews.com/search/label/Web%20Development)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![Come...