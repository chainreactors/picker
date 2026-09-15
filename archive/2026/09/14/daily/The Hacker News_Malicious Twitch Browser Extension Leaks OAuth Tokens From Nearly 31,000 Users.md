---
title: Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users
url: https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html
source: The Hacker News
date: 2026-09-14
fetch_date: 2026-09-15T07:03:16.311228
---

# Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users

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

# [Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users](https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html)

**Ravie Lakshmanan**Sep 14, 2026Malware / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguNgykDjufnR6xGrMUSq67eZ5sCFxbYjf8J6pEXekhUnt-zCt2xaJ4jzj6I0wPMYjps9z2ufKJ-JSJ8ZqhGe4BcbtNWfRETdaB6QgIRVLw0CtnsM5q2qCpyI3kL7oBXmNixcTTcumZJHFgCKaoLY8kRIBDbPHslMmmzzb25TlESGooJuaxtXEL5qrUzkop/s1700-nu-rw-lo-l85-e365/twitch.jpg)

A malicious cross-store Twitch browser extension has leaked OAuth tokens associated with nearly 31,000 users to proxy servers operated by a Russian commercial bot service.

The extension, named "Twitch Enhanced Viewer | JeetBot," lists HISHIMIRO/jeetbot.cc as its developer and has the following identifiers on the Google Chrome Web Store and Mozilla Firefox Add-Ons store -

* **Chrome** - [pnhhdhhcadcjfckjhpmjneldiegbojfb](https://chromewebstore.google.com/detail/twitch-enhanced-viewer-je/pnhhdhhcadcjfckjhpmjneldiegbojfb) - 30,000 users (Published on June 26, 2025)
* **Firefox** - [twitchenhancedviewer@example.com](https://addons.mozilla.org/en-US/firefox/addon/twitch-enhanced-viewer/) - 604 users (Published on July 7, 2025)

Both extensions are still available for download as of writing. The extension listing description states: "JeetBot is a modern tool for streamers and viewers who appreciate quality, convenience, and control," adding it "expands Twitch capabilities: 1080p stream for regions with constraints."

"Current builds (v85.x) forward the token inline as an &auth= query parameter on a network-layer redirect to the operator's proxy," Socket security researcher Kush Pandya [said](https://socket.dev/blog/malicious-twitch-browser-extension). "The token is forwarded for every channel the user watches, except a hardcoded allowlist of ten Russian streamer channels, whose sessions are exempted from forwarding."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"The operator is a commercial Twitch, Kick, and VK Live bot SaaS that has broad Twitch host permissions and relays live authenticated sessions through its own infrastructure."

While the extension claims to offer an ad-free experience and serve region-unlocked content, it does so by routing Twitch's video-playlist requests to "usher.ttvnw[.]net" through operator-controlled proxy servers along with the user's OAuth token as an "&auth=" query parameter.

Specifically, the add-on embeds code to recover the Twitch OAuth token and send it to the proxy. The token can enable access to a user's chat, [whispers](https://help.twitch.tv/s/article/how-to-use-whispers?language=en_US) (i.e., private messages), and account settings.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHSpVwNVIShcGzSiR5NffTEvF4sCDei3eZjfIG_qOfNpKVr7I3JaIWdpXhwnMsRZCOscYF6o7CeX3uVcz-WvZjhj420gUQgTHNq5Z7gxap0EWhABE6l_mDX9eupcc5p1KsLTdmE-fXIWEhRBG8fLRFS-pVbNXS2w3RhIt-2_O_gmZfGKzCmmsEZmJkNWid/s1700-nu-rw-lo-l85-e365/fire.jpg)

Given that the token is placed in the URL query string, it gets written in cleartext into the proxy server's request logs. The token redirection mechanism, however, is excluded for a hard-coded list of 10 Twitch channels, most of them being Russian-language streamers with thousands of followers -

* pch3lk1n (580K followers)
* fasoollka (361K followers)
* flamie (132K followers)
* dosia (29 followers)
* fander (2 followers)
* almazer (4 followers)
* forzorezor (177K followers)
* akyuliych (1.1M followers)
* lagoda1337 (225K followers)
* lagoda (77.3K followers)

"For every channel outside this list, the user’s live token is forwarded to the proxy," Pandya explained. "Earlier v4.x builds (for example version 4.8, January 2026) went further, POSTing the token to a dedicated set-token endpoint on the operator host, with backups on deno.dev and deno.net."

JeetBot advertises itself as a "powerful bot for Twitch, Kick and VK Live with message speech synthesis, automatic translation, and many other features to enhance interaction with viewers." It claims to have over 26,000 active streamers and 1 billion processed messages. The site's footer identifies the operator as a Cyprus-based developer named Aleksandr Popov. On their LinkedIn profile, the developer claims JeetBot to be their pet project.

However, it appears that the developer has already taken steps to address the problem. An alert issued on the [JeetBot documentation page](https://docs.jeetbot.cc/en/base-stuff/extension/) now states that version 85.8.7 of the Firefox add-on addresses the problem and that an equivalent Chrome version is currently under review -

*In the previous implementation, the extension sent the user's Twitch OAuth token to our proxy servers to retrieve stream playlists. An OAuth token is a credential and must be protected.*

*Version 85.8.7 changes how playlists are retrieved: the user's OAuth token is no longer sent to our proxies.*

*Check your installed extension version and update to 85.8.7 or later. Older installations using the previous mechanism continue to send the token until updated.*

The documentation also urges users to temporarily disable the extension to halt further transmission of the token if the extension is not available. However, the developer warned that disabling or updating the extension does not revoke previously transmitted tokens.

When contacted for comment, Popov told The Hacker News that the exfiltration of the Twitch OAuth tokens was an oversight that has been addressed in the latest version of the extensions. The developer also noted that a Chrome update has been submitted and is still awaiting Chrome Web Store review.

"We appreciate Socket drawing attention to the token-handling and disclosure concerns," Popov said. "We have taken those concerns seriously and changed the extension’s implementation. We acknowledge that th...