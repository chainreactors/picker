---
title: DOM-Based Extension Clickjacking Exposes Popular Password Managers to Credential and Data Theft
url: https://thehackernews.com/2025/08/dom-based-extension-clickjacking.html
source: The Hacker News
date: 2025-08-21
fetch_date: 2025-10-07T00:50:43.778152
---

# DOM-Based Extension Clickjacking Exposes Popular Password Managers to Credential and Data Theft

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

# [DOM-Based Extension Clickjacking Exposes Popular Password Managers to Credential and Data Theft](https://thehackernews.com/2025/08/dom-based-extension-clickjacking.html)

**Aug 20, 2025**Ravie LakshmananVulnerability / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis8s2AE2HL9hS_h59LP2ylzs5MHDhwBvrz3osuRARB4BpzRakMQnL4b5FJtFiHJsBv8w1JWNQ9d2uv932WVPoWKj_MJbatN4Oprl-eA2bN3QM8G3xdbB1g0-BV-WnQclf5L4WLJbNqA1ku-i0SUX-YlWvsJfNMOwQ536TSbUGugv2syApaFvPR8rQcSqGF/s790-rw-e365/passwords.jpg)

Popular password manager plugins for web browsers have been found susceptible to clickjacking security vulnerabilities that could be exploited to steal account credentials, two-factor authentication (2FA) codes, and credit card details under certain conditions.

The technique has been dubbed Document Object Model ([DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model))-based extension clickjacking by independent security researcher Marek Tóth, who [presented the findings](https://media.defcon.org/DEF%20CON%2033/DEF%20CON%2033%20presentations/Marek%20T%C3%B3th%20-Browser%20Extension%20Clickjacking%20One%20Click%20and%20Your%20Credit%20Card%20Is%20Stolen.pdf) at the DEF CON 33 security conference earlier this month.

"A single click anywhere on an attacker-controlled website could allow attackers to steal users' data (credit card details, personal data, login credentials, including TOTP)," Tóth [said](https://marektoth.com/blog/dom-based-extension-clickjacking/). "The new technique is general and can be applied to other types of extensions."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Clickjacking](https://thehackernews.com/2025/01/new-doubleclickjacking-exploit-bypasses.html), also called UI redressing, refers to a type of attack in which users are tricked into performing a series of actions on a website that appear ostensibly harmless, such as clicking on buttons, when, in reality, they are inadvertently carrying out the attacker's bidding.

The new technique detailed by Tóth essentially involves using a malicious script to manipulate UI elements in a web page that browser extensions inject into the DOM -- for example, auto-fill prompts, by making them invisible by setting their opacity to zero.

The research specifically focused on 11 popular password manager browser add-ons, ranging from 1Password to iCloud Passwords, all of which have been found to be susceptible to DOM-based extension clickjacking. Collectively, these extensions have millions of users.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyKjg8kY4oUmTTbKC7ywAAPrqd5-SOVnv2kfAqhgXZ8Wy0FkVrFm4FFIIHOGZEHP3HES3Bku5mStscojP_LP-u883Te_rXxWHLNKeEVqDyufws-ND13vjUaPPqxplwdQgSp_eQvAkg64-Us2d0ETssICjGVPwsrx8HtoqOulNOwCM680pF26D4mI6HGVxt/s790-rw-e365/apps.png)

To pull off the attack, all a bad actor has to do is create a fake site with an intrusive pop-up, such as a login screen or a cookie consent banner, while embedding an invisible login form such that clicking on the site to close the pop-up causes the credential information to be auto-filled by the password manager and exfiltrated to a remote server.

"All password managers filled credentials not only to the 'main' domain, but also to all subdomains," Tóth explained. "An attacker could easily find XSS or other vulnerabilities and steal the user's stored credentials with a single click (10 out of 11), including TOTP (9 out of 11). In some scenarios, passkey authentication could also be exploited (8 out of 11)."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiO8vDIENgf79g72SssM8AKSQZV6s3oCi0GDgfbnF_Yixn5tqYz66fs4Z1fE0F8aA-ubOMszEpgSQbYe2QJ9Xpzl8T18IeTb8VU6spYe0P11l_Jp7TOulDnNQkxFTISrgpJvVgzL6aSt0C2u2PDyGDVPogOqRDG3DAQnK_XjMCNrvuzQtaEwwzGWYUSVCQ8/s790-rw-e365/passwords.png)

Following responsible disclosure, six of the vendors have yet to release fixes for the defect -

* 1Password Password Manager 8.11.4.27
* Apple iCloud Passwords 3.1.25
* Bitwarden Password Manager 2025.7.0
* Enpass 6.11.6
* LastPass 4.146.3
* LogMeOnce 7.12.4

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Software supply chain security firm Socket, which independently reviewed the research, [said](https://socket.dev/blog/password-manager-clickjacking) Bitwarden, Enpass, and iCloud Passwords are actively working on fixes, while 1Password and LastPass marked them as informative. It has also reached out to US-CERT to assign CVE identifiers for the identified issues.

Until fixes are available, it's advised that users disable the auto-fill function in their password managers and only use copy/paste.

"For Chromium-based browser users, it is recommended to configure site access to 'on click' in extension settings," Tóth said. "This configuration allows users to manually control auto-fill functionality."

### Update

Bitwarden has released [version 2025.8.0](https://github.com/bitwarden/clients/releases/tag/browser-v2025.8.0) of the password manager to address the clickjacking vulnerabilities. It is also advising users to pay close attention to website URLs and stay alert for phishing campaigns to avoid malicious websites.

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
[**Share o...