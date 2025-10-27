---
title: PyPI Warns of Ongoing Phishing Campaign Using Fake Verification Emails and Lookalike Domain
url: https://thehackernews.com/2025/07/pypi-warns-of-ongoing-phishing-campaign.html
source: The Hacker News
date: 2025-07-30
fetch_date: 2025-10-06T23:57:39.193927
---

# PyPI Warns of Ongoing Phishing Campaign Using Fake Verification Emails and Lookalike Domain

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

# [PyPI Warns of Ongoing Phishing Campaign Using Fake Verification Emails and Lookalike Domain](https://thehackernews.com/2025/07/pypi-warns-of-ongoing-phishing-campaign.html)

**Jul 29, 2025**Ravie LakshmananPhishing / Developer Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRKoKyTG1vCW6-50V_5WrmFvTmEvvKttYiAvH_713-cjhKXKEDxigpXgI0c6KtS8gru-kAOKa_yjr2B12TgtZMRlq1zSKo-E6O9-G0WNq3ud5psPnx1ScYO89FfZsC182jfxewCSaAW-gvXeF3ZS1jKGGkajI_d6qsn1iWAnH8Y4oVQxLkgJZ5Fhop7iqK/s790-rw-e365/python.jpg)

The maintainers of the Python Package Index (PyPI) repository have issued a warning about an ongoing phishing attack that's targeting users in an attempt to redirect them to fake PyPI sites.

The attack involves sending email messages bearing the subject line "[PyPI] Email verification" that are sent from the email address **noreply@pypj[.]org** (note that the domain is not "**pypi[.]org**").

"This is not a security breach of PyPI itself, but rather a phishing attempt that exploits the trust users have in PyPI," Mike Fiedler, PyPI Admin, [said](https://blog.pypi.org/posts/2025-07-28-pypi-phishing-attack/) in a post Monday.

The email messages instruct users to follow a link to verify their email address, which leads to a replica phishing site that impersonates PyPI and is designed to harvest their credentials.

But in a clever twist, once the login information is entered on the bogus site, the request is routed to the legitimate PyPI site, effectively fooling the victims into thinking that nothing is amiss when, in reality, their credentials have been passed on to the attackers. This method is harder to detect because there are no error messages or failed logins to trigger suspicion.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

PyPI said it's looking at different methods to handle the attack. In the meanwhile, it's urging users to inspect the URL in the browser before signing in and refrain from clicking on the link if they have already received such emails.

If you're unsure whether an email is legitimate, a quick check of the domain name—letter by letter—can help. Tools like browser extensions that highlight verified URLs or password managers that auto-fill only on known domains can add a second layer of defense. These kinds of attacks don't just trick individuals; they aim to gain access to accounts that may publish or manage widely used packages.

"If you have already clicked on the link and provided your credentials, we recommend changing your password on PyPI immediately," Fiedler said. "Inspect your account's Security History for anything unexpected."

It's currently not clear who is behind the campaign, but the activity bears striking similarities to a [recent npm phishing attack](https://thehackernews.com/2025/07/malware-injected-into-6-npm-packages.html) that employed a typosquatted domain "npnjs[.]com" (as opposed to "npmjs[.]com") to send identical email verification emails to capture users' credentials.

The attack ended up compromising seven different npm packages to deliver a malware called Scavenger Stealer to gather sensitive data from web browsers. In one case, the attacks paved the way for a JavaScript payload that captured system information and environment variables, and exfiltrated the details over a WebSocket connection.

Similar attacks have been seen across npm, GitHub, and other ecosystems where trust and automation play a central role. Typosquatting, impersonation, and reverse proxy phishing are all tactics in this growing category of social engineering that exploits how developers interact with tools they rely on daily.

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

[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Developer Security](https://thehackernews.com/search/label/Developer%20Security)[email security](https://thehackernews.com/search/label/email%20security)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Phishing](https://thehackernews.com/search/label/Phishing)[PyPI](https://thehackernews.com/search/label/PyPI)[Python](https://thehackernews.com/search/label/Python)[social engineering](https://thehackernews.com/search/label/social%20engineering)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[typosquatting](https://thehackernews.com/search/label/typosquatting)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Sec...