---
title: New Phishing-as-a-Service Platform Lets Cybercriminals Generate Convincing Phishing Pages
url: https://thehackernews.com/2023/05/new-phishing-as-service-platform-lets.html
source: The Hacker News
date: 2023-05-14
fetch_date: 2025-10-04T11:39:40.098492
---

# New Phishing-as-a-Service Platform Lets Cybercriminals Generate Convincing Phishing Pages

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

# [New Phishing-as-a-Service Platform Lets Cybercriminals Generate Convincing Phishing Pages](https://thehackernews.com/2023/05/new-phishing-as-service-platform-lets.html)

**May 13, 2023**Ravie Lakshmanan

[![phishing-as-a-service](data:image/png;base64... "phishing-as-a-service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_ZekiVccFBIrXHIe1c1BBk1Ife1M0o_veVo7RXHR8JBNu40r4_Z4TY7SqSbfHnHIuIWtLrbPd40Dq1Ejdeli9di3E58AWn_em9Ww_KHwe0hI1kSVIJN8Du1OVqHaj1SNGeLTVK6A7qeXG6CommSAEoD7MwHdSlrTpdjfFY7XQKm_4a16ri6_3CHb0/s790-rw-e365/ms.png)

A new [phishing-as-a-service](https://www.cyberark.com/resources/threat-research-blog/phishing-as-a-service) (PhaaS or PaaS) platform named **Greatness** has been leveraged by cybercriminals to target business users of the Microsoft 365 cloud service since at least mid-2022, effectively lowering the bar to entry for phishing attacks.

"Greatness, for now, is only focused on Microsoft 365 phishing pages, providing its affiliates with an attachment and link builder that creates highly convincing decoy and login pages," Cisco Talos researcher Tiago Pereira [said](https://blog.talosintelligence.com/new-phishing-as-a-service-tool-greatness-already-seen-in-the-wild/).

"It contains features such as having the victim's email address pre-filled and displaying their appropriate company logo and background image, extracted from the target organization's real Microsoft 365 login page."

Campaigns involving Greatness have mainly manufacturing, health care, and technology entities located in the U.S., the U.K., Australia, South Africa, and Canada, with a spike in activity detected in December 2022 and March 2023.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Phishing kits like Greatness offer threat actors, rookies or otherwise, a [cost-effective](https://thehackernews.com/2022/11/robin-banks-phishing-service-for.html) and [scalable one-stop shop](https://thehackernews.com/2023/04/researchers-uncover-thriving-phishing.html), making it possible to design convincing login pages associated with various online services and bypass two-factor authentication (2FA) protections.

Specifically, the authentic-looking decoy pages function as a [reverse proxy](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/) to harvest credentials and time-based one-time passwords (TOTPs) entered by the victims.

[![phishing-as-a-service](data:image/png;base64... "phishing-as-a-service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYavUOtnKLxTb9d9UyL3rmxzgU4t_qa7yI4FQgRwPnVDuKORZpdFSZN8PIEpyT-OTxvEmoFT2TOlvK0cKqFU1KtI6uo0rzD75aVIGForeeVAO7jcldA7C4Ayjt6mUEIvxlY_v8qkE8bYvMF29KgSRTf7EZ8DqNkCZ9IaKzC2rk1nZQkWJwBlMlXinw/s790-rw-e365/service.png)

Attack chains begin with malicious emails containing an HTML attachment, which, upon opening, executes obfuscated JavaScript code that redirects the user to a landing page with the recipient's email address already pre-filled and prompts for their password and MFA code.

The entered credentials and tokens are subsequently forwarded to the affiliate's Telegram channel for obtaining unauthorized access to the accounts in question.

The [AiTM phishing kit](https://thehackernews.com/2023/03/microsoft-warns-of-large-scale-use-of.html) also comes with an administration panel that enables the affiliate to configure the Telegram bot, keep track of stolen information, and even build booby-trapped attachments or links.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

What's more, each affiliate is expected to have a valid API key in order to be able to load the phishing page. The API key also prevents unwanted IP addresses from viewing the phishing page and facilitates behind-the-scenes communication with the actual Microsoft 365 login page by posing as the victim.

[![phishing-as-a-service](data:image/png;base64... "phishing-as-a-service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_dmitmriFBwbqwR3HnHYV5LG5FJiNfA8y2nMIiNYp2twG7hLhgTVyyR0hiLEJ5vbyTZo7RzaC3q7QP_j7V2kgrT7PASi38miKxUe-_Jim6VZn-dQuot40uq5PYLTzpEhraASe81RMk3bAiHZabmZXYQZMdyHYvmpiuJnVWRrHRT9dyn4MF4OVbU9x/s790-rw-e365/talos.png)

"Working together, the phishing kit and the API perform a 'man-in-the-middle' attack, requesting information from the victim that the API will then submit to the legitimate login page in real time," Pereira said.

"This allows the PaaS affiliate to steal usernames and passwords, along with the authenticated session cookies if the victim uses MFA."

The findings come as Microsoft [has begun](https://learn.microsoft.com/en-us/azure/active-directory/authentication/how-to-mfa-number-match) enforcing number matching in Microsoft Authenticator push notifications as of May 8, 2023, to improve 2FA protections and fend off [prompt bombing attacks](https://thehackernews.com/2022/08/cisco-confirms-its-been-hacked-by.html).

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

[AitM Attack](https://thehackernews.com/search/label/AitM%20Attack)[Microsoft](https://thehackernews.com/search/label/Microsoft)[phishing-as-a-service](https://thehackernews.com/search/label/phishing-as-a-service)

[![c](...