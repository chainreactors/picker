---
title: Microsoft Authenticator Flaw Let Permissionless Android Apps Steal Work Account Tokens
url: https://thehackernews.com/2026/10/microsoft-authenticator-flaw-let.html
source: The Hacker News
date: 2026-10-27
fetch_date: 2026-10-28T07:49:45.737488
---

# Microsoft Authenticator Flaw Let Permissionless Android Apps Steal Work Account Tokens

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Microsoft Authenticator Flaw Let Permissionless Android Apps Steal Work Account Tokens](https://thehackernews.com/2026/10/microsoft-authenticator-flaw-let.html)

**Swati Khandelwal**Oct 27, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqk63DF3MJCMgQqpg91UsWY7mjACbBgPl50GfKwDPi7v3md6sP5l8a2BUqHABjgMN_6BzgcMx4vVKW4hR9B9pz8_XHqp5ctKqQQLw-RJwuKmVWm2MaSzEMkHIsV-Yi0V6Mq_gUYYuzTpi-BzV2-8dRVYBjtuW4nb9TbobkPwvOGTkIFTpr334JB_LZIkw/s1700-nu-rw-lo-l85-e365/msms.jpg)

Microsoft has fixed a flaw in its Authenticator app for Android that let a malicious app with no permissions pose as a trusted Microsoft app, such as Teams, and collect sign-in tokens for a victim's work account.

Microsoft tracks the flaw as [CVE-2026-80097](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-80097) and fixed it in Authenticator for Android version 6.2606.4246, so anyone using the app should update.

In the researchers' tests, the tokens gave full access to the account's email, files, and calendar. Microsoft says exploitation also needs the victim to complete a sign-in step in Authenticator, and that the flaw has not been used in attacks.

The research comes from Ofek Levin, working through a fellowship program at the security firm [Enclave](https://enclave.ai/blog/authmask-we-made-microsoft-authenticator-hand-over-tokens), which published the technical details on October 23, 2026. Microsoft assigned the CVE on September 8 and rated it 8.6 on the CVSS scale, which it labels "Important."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

On Android, Authenticator does more than show six-digit codes. It also acts as a broker: when Teams, Outlook, or another Microsoft app needs to sign a user in, it asks Authenticator, and Authenticator hands back a token, a digital pass that proves the user is logged in. Because the broker controls access to the entire account, it should be careful about which app it grants a token to.

The flaw let the wrong app get one. Authenticator exposes a component, an activity named **AccountChooserActivity**, that any app on the device can start. When the attacker's app started it, Authenticator built its token request from values the attacker's app supplied, including the name of the app it claimed to be. The app said it was Teams, and the broker believed it.

A signature check was supposed to stop this, but it did not. The check looked up the real signature of the app being impersonated and confirmed the request matched it. Because Teams was genuinely installed on the device, its real signature was there to read, so the check passed.

Authenticator could also see which app had actually made the request, Enclave found, but it did not use that to decide whether to hand over a token.

In Enclave's tests, posing as Teams and requesting Microsoft Graph tokens returned permissions to read and send mail, read and write files, and read and write calendars, among others.

Microsoft describes the result more generally: a successful attacker could authenticate as the signed-in user and reach that user's resources. The tokens apply to the work account signed into Authenticator on that device, not to other accounts.

The two accounts disagree on one point a reader should weigh. Enclave reported that its proof of concept returned tokens without any user interaction, other than the presence of a signed-in account.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Microsoft's advisory says exploitation requires installing a malicious app on the device and convincing the user to complete an authentication flow in Authenticator. Its CVSS score also indicates that the flaw requires user interaction.

Microsoft says the flaw has not been exploited and was not publicly disclosed before the fix, and rates exploitation as "less likely." It was part of the company's [September 2026 Patch Tuesday](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html) and was not one of the two Windows flaws flagged that month as already under attack. The vulnerability is not listed in the U.S. CISA Known Exploited Vulnerabilities catalog as of October 26, 2026.

The fix is to update Microsoft Authenticator for Android to version 6.2606.4246 or later, as linked in Microsoft's advisory. Organizations that manage Android devices can require that minimum version through their device management. Microsoft's advisory gives the fix but does not say whether updating cancels any token a malicious app may already have obtained, so that remains unclear from the available sources.

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

[Authentication](https://thehackernews.com/search/label/Authentication), [Identity Security](https://thehackernews.com/search/label/Identity%20Security), [Microsoft](https://thehackernews.com/search/label/Microsoft), [mobile security](https://thehackernews.com/search/label/mobile%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64......