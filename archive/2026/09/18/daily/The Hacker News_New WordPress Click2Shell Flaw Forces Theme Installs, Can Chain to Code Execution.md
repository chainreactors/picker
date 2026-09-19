---
title: New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution
url: https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html
source: The Hacker News
date: 2026-09-18
fetch_date: 2026-09-19T07:02:43.144277
---

# New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution](https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html)

**Swati Khandelwal**Sep 18, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRmEdVvBEJZEaIzJ4GYHX3cDjJq5YaLQby6GeVwDl-uVl_qIR_tkRSx6aKpzoYhGVvp0E3NDIe9aum5f5N_lI-RPz6eDNGHC7vpKMa0UrlT1J1_bRJrJ8Wk0htpyFoR3ezoqh-BCJePJU914UFlL7gS45RXbWoVi3Lp49iNSkUt7eLrJyQTAEIGE-VRgY/s1700-nu-rw-lo-l85-e365/click2shell.gif)

WordPress today released patches to fix a new set of vulnerabilities in its core software, one of which could allow a crafted web link, opened by a logged-in administrator, to install a theme from the official WordPress.org directory without anyone clicking Install.

The security firm [pwn.ai](https://pwn.ai/blog/click2shell), whose researchers reported the flaw, calls the attack chain **Click2Shell**. On its own the flaw only installs a real theme that the attacker picks, but the security research team showed it could be combined with a separate weakness in a theme to run the attacker's own code on the server.

The fix shipped on September 17 in [WordPress 7.1.1](https://wordpress.org/news/2026/09/wordpress-7-1-1-maintenance-and-security-release/). Because this is a security release, WordPress advises updating right away. There is no sign the flaw has been used in real attacks.

The installed theme stays switched off, so the site's own appearance does not change and nothing looks wrong. Reaching code execution needed a second, separate flaw in the theme that was installed. As pwn.ai wrote of the core bug alone, "The Core bug does not accept an arbitrary theme ZIP by itself."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The flaw works because two parts of WordPress read the same link differently. The WordPress.org directory treats the value in the link as an ordinary theme name and returns a real theme, but the administrator's browser reuses the original text, punctuation and all, inside code meant to pick out an item on the page. Characters the attacker adds to the link send that code to the Install button, and WordPress's own script clicks it.

Because the administrator is already logged in, their session supplies the permission and the security token the install needs, so the attacker supplies neither.

An installed theme is not always idle. When WordPress builds a preview in its Customizer tool, it can load a theme's PHP code even before the theme is switched on.

The theme pwn.ai used, Mobile Repair Zone, carried a second flaw: a background handler that fetched a web address from the request, downloaded a package, and ran its code, with no check on the visitor's permission or a security token. Chained after the forced install, that handler ran the attacker's code on the server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuu1sytyKfju0A8GRRbhohmLEbGHnjGyMl8sBlMIt451Tfvcyw9bIdTw4cVK5aY2mvxP6ag2Acc3oyaM3vzkhEWiGu7vr-773CR-ZGUgsWootpUMwgKjuBpz5go3FRaRlybZDviy5f3I0YSJpkT4OlR2AGSkFR82qMRMDrRF-gaECtul7QmggksBl_7eg/s1700-nu-rw-lo-l85-e365/wp-chain.jpg)

The researchers rated the forced-install flaw on its own as high severity, with a CVSS score of 7.1, and the full chain to code execution as critical, at 9.6. WordPress has not published a severity rating of its own, and in its release it described the issue this way: "Specially crafted URLs can automatically install and preview an inactive theme from WordPress.org." No CVE identifier has been assigned yet, though pwn.ai says WordPress plans to add one.

WordPress fixed the flaw in 7.1.1, part of a security release whose fixes reach supported branches back to 4.7. Its [notes](https://wordpress.org/documentation/wordpress-version/version-7-1-1/) confirm this flaw from version 6.0 up through the releases just before the fix. Site owners should install 7.1.1, or the matching update for whichever branch they run, and sites set to update automatically will receive it on their own.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

If you cannot update at once, note that neither WordPress nor pwn.ai offered a separate workaround, and that the attack still needs a logged-in administrator to open the attacker's link. Updating WordPress core closes the demonstrated attack whatever theme a site runs.

Click2Shell is not the firm's first WordPress core flaw in recent weeks. In August, WordPress fixed [a similar flaw](https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html) pwn.ai found in the login screen and also chained to code execution, and there too WordPress described the risk more narrowly than the researchers did.

A [different WordPress core flaw](https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html) disclosed in July, called wp2shell, is not connected to pwn.ai's work. That flaw needs no login and no click, and the U.S. cybersecurity agency CISA has listed it as exploited in real attacks, which Click2Shell has not been.

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
...