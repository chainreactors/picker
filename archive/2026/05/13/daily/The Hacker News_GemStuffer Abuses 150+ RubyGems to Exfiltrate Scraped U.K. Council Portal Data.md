---
title: GemStuffer Abuses 150+ RubyGems to Exfiltrate Scraped U.K. Council Portal Data
url: https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html
source: The Hacker News
date: 2026-05-13
fetch_date: 2026-05-14T05:47:23.872118
---

# GemStuffer Abuses 150+ RubyGems to Exfiltrate Scraped U.K. Council Portal Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [GemStuffer Abuses 150+ RubyGems to Exfiltrate Scraped U.K. Council Portal Data](https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html)

**Ravie Lakshmanan**May 13, 2026Software Supply Chain / Data Exfiltration

[![RubyGems to Exfiltrate](data:image/png;base64... "RubyGems to Exfiltrate")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZpbB_p88zZf6q_DhwCbgnYn2okFYqa7pwIPmknojvkOC3heteNMp3C6bzD_6WKChB4yVK0wLyoJ_-DebN0c229j-twjPyMAC-qkfGs1tjlaEoNg30fpEDh9DIByfz_h4nKhalTC_Su-FP0AYxywL_x85ILq1t-QFPtuMa_-KbLKlfsX15kvGpPCs1OZpw/s1700-e365/rubygemss.jpg)

Cybersecurity researchers are calling attention to a new campaign dubbed **GemStuffer** that has targeted the RubyGems repository with more than 150 gems that use the registry as a data exfiltration channel rather than for malware distribution.

"The packages do not appear designed for mass developer compromise," Socket [said](https://socket.dev/blog/gemstuffer). "Many have little or no download activity, and the payloads are repetitive, noisy, and unusually self-contained."

"Instead, the scripts fetch pages from U.K. local government democratic services portals, package the collected responses into valid .gem archives, and publish those gems back to RubyGems using hardcoded API keys."

The development comes as [RubyGems temporarily disabled](https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html) new account registration following what has been described as a major malicious attack. While it's not clear if the two sets of activities are related, the application security company said GemStuffer fits the "same abuse pattern," which involves using newly created packages with junk names to host the scraped data.

At a high level, the campaign abuses RubyGems as a place to stage the scraped council content. It does this by fetching hard-coded U.K. council portal URLs, packaging the HTTP responses into valid .gem archives, and publishing those archives to RubyGems using embedded registry credentials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

In some cases, the payload embedded within the gem creates a temporary RubyGems credential environment under "/tmp," overrides the HOME environment variant, builds a gem locally, and pushes it to RubyGems using the [gem command-line interface](https://guides.rubygems.org/command-reference/) (CLI), as opposed to depending on pre-existing RubyGems credentials on the target machine.

Other variants of the malicious gems have been found to eschew the CLI component in favor of uploading the archive directly to the RubyGems API via an HTTP POST request. Once the new gems have been published, all an attacker has to do is run a "gem fetch" command with the gem name and version to access the scraped data.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0V7MWewzbZaFDyNMTLnFqDjp9QCTGnACc4IX6_mr3Fl-9cyS3n5qqyXqbqyb2SZrw0w4LxPugUMLfAuehtWWhNkJgUY-EtXw_0mTZzS72p9IJhEIKbvY18yOBOX43JSfa1cZ_MxPKA7UcHAxEK3zDEXi7bblmpTFDebs1X6RcS3qbMfMTDLr3A6yyl4fd/s1700-e365/payload.jpg)

The novel scraping campaign has been found to target public-facing ModernGov portals used by Lambeth, Wandsworth, and Southwark, with an aim to collect committee meeting calendars, agenda item listings, linked PDF documents, officer contact information, and RSS feed content.It's not clear what exactly the end goals are, as the information appears to be publicly accessible anyway.

Socket has assessed that the systematic bulk collection and archival of this data raises the possibility that the attacker may be leveraging the "council portal access as a pivot to demonstrate capability against government infrastructure."

"It may be registry spam, a proof-of-concept worm, an automated scraper misusing RubyGems as a storage layer, or a deliberate test of package registry abuse," Socket said. "But the mechanics are intentional: repeated gem generation, version increments, hardcoded RubyGems credentials, direct registry pushes, and scraped data embedded inside package archives."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data exfiltration](https://thehackernews.com/search/label/data%20exfiltration), [Package Registry](https://thehackernews.com/search/label/Package%20Registry), [Ruby](https://thehackernews.com/search/label/Ruby), [RubyGems](https://thehackernews.com/search/label/RubyGems), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain), [Web Scraping](https://thehackernews.com/search/label/Web%20Scraping)

⚡ Top Stories This Week

[![30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](data:image/svg+xml;base64... "30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign")

30,000 Facebook Accounts Hacked via Google AppSheet Phishing Campaign](https://thehackernews.com/2026/05/30000-facebook-accounts-hacked-via.html)

[![Trellix Confirms Source Code Breach With Unauthorized Repository Access](data:image/svg+xml;base64... "Trellix Confirms Source Code Breach With Unauthorized Repository Access")

Trell...