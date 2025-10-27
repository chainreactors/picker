---
title: WordPress Mandates Two-Factor Authentication for Plugin and Theme Developers
url: https://thehackernews.com/2024/09/wordpress-mandates-two-factor.html
source: The Hacker News
date: 2024-09-13
fetch_date: 2025-10-06T18:31:26.960970
---

# WordPress Mandates Two-Factor Authentication for Plugin and Theme Developers

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

# [WordPress Mandates Two-Factor Authentication for Plugin and Theme Developers](https://thehackernews.com/2024/09/wordpress-mandates-two-factor.html)

**Sep 12, 2024**Ravie LakshmananWeb Security / Content Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDLlM0DLGPeohTzpRxDDt82DGLODgWPB0r5MZfp69N-V5_U-91f5QVfzD_IltbzvifomXu__TPqDeAnKrzDCQ9DHR9ug6t56F7mOj96slXPm2ItXboDUZPN_CC5v31ZFfwi2w0UCZDJ_rkJSGaH79t07OBQ0jQ3ibEMfGAvX4Hmu8UTIPGja4y03PH8i-d/s790-rw-e365/wordpress.png)

WordPress.org has announced a new account security measure that will require accounts with capabilities to update plugins and themes to activate two-factor authentication (2FA) mandatorily.

The [enforcement](https://profiles.wordpress.org/me/profile/security) is expected to come into effect starting October 1, 2024.

"Accounts with commit access can push updates and changes to plugins and themes used by millions of WordPress sites worldwide," the maintainers of the open-source, self-hosted version of the content management system (CMS) [said](https://make.wordpress.org/plugins/2024/09/04/upcoming-security-changes-for-plugin-and-theme-authors-on-wordpress-org/).

"Securing these accounts is essential to preventing unauthorized access and maintaining the security and trust of the WordPress.org community."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Besides requiring mandatory 2FA, WordPress.org said it's introducing what's called SVN passwords, which refers to a dedicated password for committing changes.

This, it said, is an effort to introduce a new layer of security by separating users' code commit access from their WordPress.org account credentials.

"This password functions like an application or additional user account password," the team said. "It protects your main password from exposure and allows you to easily revoke SVN access without having to change your WordPress.org credentials."

WordPress.org also noted that technical limitations have prevented 2FA from being applied to existing code repositories, as a result of which it has opted for a "combination of account-level two-factor authentication, high-entropy SVN passwords, and other deploy-time security features (such as Release Confirmations)."

The measures are seen as a way to counter scenarios where a malicious actor could seize control of a publisher's account, thereby introducing malicious code into legitimate plugins and themes, resulting in large-scale supply chain attacks.

The disclosure comes as Sucuri [warned](https://blog.sucuri.net/2024/08/wordpress-websites-used-to-distribute-clearfake-trojan-malware.html) of ongoing [ClearFake campaigns](https://thehackernews.com/2024/06/cybercriminals-exploit-free-software.html) targeting WordPress sites that aim to distribute an information stealer called RedLine by tricking site visitors into manually running PowerShell code in order to fix an issue with rendering the web page.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Threat actors have also been observed leveraging infected PrestaShop e-commerce sites to deploy a credit card skimmer to siphon financial information entered on checkout pages.

"Outdated software is a primary target for attackers who exploit vulnerabilities in old plugins and themes," security researcher Ben Martin [said](https://blog.sucuri.net/2024/08/prestashop-gtag-websocket-skimmer.html). "Weak admin passwords are a gateway for attackers."

Users are recommended to keep their plugins and themes up-to-date, deploy a web application firewall (WAF), periodically review administrator accounts, and monitor for unauthorized changes to website files.

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

[content management system](https://thehackernews.com/search/label/content%20management%20system)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Open Source](https://thehackernews.com/search/label/Open%20Source)[two-factor authentication](https://thehackernews.com/search/label/two-factor%20authentication)[Web Development](https://thehackernews.com/search/label/Web%20Development)[WordPress](https://thehackernews.com/search/label/WordPress)[WordPress plugin](https://thehackernews.com/search/label/WordPress%20plugin)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Fou...