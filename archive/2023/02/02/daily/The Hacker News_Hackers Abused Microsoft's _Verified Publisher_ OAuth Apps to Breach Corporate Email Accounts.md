---
title: Hackers Abused Microsoft's "Verified Publisher" OAuth Apps to Breach Corporate Email Accounts
url: https://thehackernews.com/2023/02/hackers-abused-microsofts-verified.html
source: The Hacker News
date: 2023-02-02
fetch_date: 2025-10-04T05:32:10.944695
---

# Hackers Abused Microsoft's "Verified Publisher" OAuth Apps to Breach Corporate Email Accounts

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

# [Hackers Abused Microsoft's "Verified Publisher" OAuth Apps to Breach Corporate Email Accounts](https://thehackernews.com/2023/02/hackers-abused-microsofts-verified.html)

**Feb 01, 2023**Ravie LakshmananEnterprise Security / Authentication

[![Microsoft OAuth Apps hacking](data:image/png;base64... "Microsoft OAuth Apps hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6xx_j9CYuzquVXuuDAM23W3Brj52Kbkfv7J_-dmCr6Mrf4naea1FtHEB2rdQjTutfx7kXnhY50wVTer6hMWkygha53hjqvcEUMf9_03y59ypJVB5r5EC7GFVHx_cw3hc50A0xQApCdA9PTznYvICSi0VpDtGMsDKmNxcYg7Qe1e5R4zWkAePDXzdF/s790-rw-e365/ms.png)

Microsoft on Tuesday said it took steps to disable fake Microsoft Partner Network (MPN) accounts that were used for creating malicious [OAuth](https://en.wikipedia.org/wiki/OAuth) applications as part of a phishing campaign designed to breach organizations' cloud environments and steal email.

"The applications created by these fraudulent actors were then used in a consent phishing campaign, which tricked users into granting permissions to the fraudulent apps," the tech giant [said](https://msrc-blog.microsoft.com/2023/01/31/threat-actor-consent-phishing-campaign-abusing-the-verified-publisher-process/). "This phishing campaign targeted a subset of customers primarily based in the U.K. and Ireland."

Consent phishing is a [social engineering attack](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/protect-against-consent-phishing) wherein users are tricked into granting permissions to malicious cloud applications, which can then be weaponized to gain access to legitimate cloud services and sensitive user data.

The Windows maker said it became aware of the campaign on December 15, 2022. It has since alerted affected customers via email, with the company noting that the threat actors abused the consent to exfiltrate mailboxes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

On top of that, Microsoft said it implemented additional security measures to improve the vetting process associated with the [Microsoft Cloud Partner Program](https://partner.microsoft.com/) (formerly MPN) and minimize the potential for fraudulent behavior in the future.

The disclosure coincides with a report [released](https://www.proofpoint.com/us/blog/cloud-security/dangerous-consequences-threat-actors-abusing-microsofts-verified-publisher) by Proofpoint about how threat actors have successfully exploited Microsoft's "[verified publisher](https://learn.microsoft.com/en-us/azure/active-directory/develop/publisher-verification-overview)" status to infiltrate the cloud environments of organizations.

What's notable about the campaign is that by mimicking popular brands, it was also successful at fooling Microsoft in order to gain the blue verified badge. "The actor used fraudulent partner accounts to add a verified publisher to OAuth app registrations they created in Azure AD," the company explained.

These attacks, which were first observed on December 6, 2022, employed lookalike versions of legitimate apps like Zoom to deceive targets into authorizing access and facilitate data theft. Targets included financial, marketing, managers, and senior executives.

[![Microsoft OAuth Apps hacking](data:image/png;base64... "Microsoft OAuth Apps hacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigA1R0rfCJ8lzrsgZgPy5yKT0ks9H0Xk8IiwQneiksO76f2DeFqsGUE-jyNNF72d8-MOrwP7rJZ_8yaBNSA87BZpgVu72cIZ9OPbJ4XC2SLu_SgppObmgUeUEB3X2CtLhUMalWw2ah2yGSOvDXoITM0eC4AN5NzP3WtAsqMS6OF5_n-zVo_BZy1mWm/s790-rw-e365/ms.png)

Proofpoint noted the malicious OAuth apps had "far-reaching delegated permissions" such as reading emails, adjusting mailbox settings, and gaining access to files and other data connected to the user's account.

It also said that unlike a [previous campaign](https://www.proofpoint.com/us/blog/email-and-cloud-threats/how-attackers-use-compromised-accounts-create-and-distribute-malicious) that compromised existing Microsoft verified publishers to take advantage of OAuth app privileges, the latest attacks are designed to impersonate legitimate publishers to become verified and distribute the rogue apps.

Two of the apps in question were named "Single Sign-on (SSO)," while the third app was called "Meeting" in an attempt to masquerade as video conferencing software. All three apps, created by three different publishers, targeted the same companies and leveraged the same attacker-controlled infrastructure.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The potential impact to organizations includes compromised user accounts, data exfiltration, brand abuse of impersonated organizations, business email compromise (BEC) fraud, and mailbox abuse," the enterprise security firm said.

The campaign is said to have come to a close on December 27, 2022, a week after Proofpoint informed Microsoft of the attack on December 20 and the apps were disabled.

The findings demonstrate the sophistication that has gone into mounting the attack, not to mention bypass Microsoft's security protections and misuse the trust users place in enterprise vendors and service providers.

This is not the first time bogus OAuth apps have been used to target Microsoft's cloud services. In January 2022, Proofpoint detailed another threat activity dubbed [OiVaVoii](https://www.proofpoint.com/us/blog/cloud-security/oivavoii-active-malicious-hybrid-cloud-threats-campaign) that targeted high-level executives to seize control of their accounts.

Then in September 2022, Microsoft [revealed](https://thehackernews.com/2022/09/hackers-using-malicious-oauth-apps-to.html) that it dismantled an attack that made use of rogue OAuth applications deployed on compromised cloud tenants to ultimately takeover Exchange servers and distribute spam.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQU...