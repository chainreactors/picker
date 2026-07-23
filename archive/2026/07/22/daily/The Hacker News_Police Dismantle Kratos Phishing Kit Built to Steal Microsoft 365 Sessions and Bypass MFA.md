---
title: Police Dismantle Kratos Phishing Kit Built to Steal Microsoft 365 Sessions and Bypass MFA
url: https://thehackernews.com/2026/07/police-dismantle-kratos-phishing-kit.html
source: The Hacker News
date: 2026-07-22
fetch_date: 2026-07-23T05:11:48.222134
---

# Police Dismantle Kratos Phishing Kit Built to Steal Microsoft 365 Sessions and Bypass MFA

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Police Dismantle Kratos Phishing Kit Built to Steal Microsoft 365 Sessions and Bypass MFA](https://thehackernews.com/2026/07/police-dismantle-kratos-phishing-kit.html)

**Swati Khandelwal**Jul 22, 2026Law Enforcement / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjOaY5kPe-g7dmQXqM_VwJIUOZk8mqgDII9sHVnZgWraV6lnXp9Pu6d664E6wSS82UCkvOd7MkPhzJBnbIKwJO9SLjHaVADbVE0zaSYhZJsHeBkBIh3Y9edJnmW4Ck1ndx5OwkkA5jJMo7gP6ocN_61sO7mOCACXBvzompiLGwnZCRkn2TkaXL6Ay94Fg/s1700-e365/phishkit.jpg)

German and US law enforcement have taken down the core infrastructure of **Kratos**, described by German investigators as one of the world's most widely used criminal phishing kits, and Indonesian authorities arrested the man they say developed and ran it.

In a joint [announcement](https://www.bka.de/SharedDocs/Kurzmeldungen/DE/Kurzmeldungen/260720_Schlag_gegen_Phishing_Gruppierung_Kratos.html) on Monday, the Frankfurt public prosecutor's cybercrime unit (ZIT) and Germany's Federal Criminal Police Office (BKA) said they pulled more than 200 servers offline. Investigators estimate roughly 1,800 paying customers used Kratos to run about 15,000 phishing campaigns a month.

Kratos harvested more than passwords. The kit was designed to steal the session cookie along with the login, and that cookie is enough to walk past two-factor authentication into the account as the user, the BKA said.

ANY.RUN, which [reverse-engineered the kit](https://any.run/cybersecurity-blog/kratos-phaas-account-takeover/), found operators could pick one of two modes: a plain PHP page that only harvests credentials, or a Node.js reverse proxy designed to relay the login to Microsoft in real time and capture the resulting session. That second mode is the adversary-in-the-middle technique that has made ordinary MFA a much weaker backstop than it looks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The operation ran like a franchise, with customers the BKA called franchisees. They paid in cryptocurrency and signed up through a dedicated website and a Telegram shop to manage their accounts and organize campaigns, so even low-skill actors could point a working AiTM kit at a target.

The authorities put the number of victims since late 2024 in the hundreds of thousands, spread across more than 30 countries and concentrated in Europe and the United States. They estimate the operators earned more than 300,000 euros since 2024, and that each campaign could hit several thousand recipients.

Kratos was already being tracked. [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/03/19/when-tax-season-becomes-cyberattack-season-phishing-and-malware-campaigns-using-tax-related-lures/) identifies the same kit as **SneakyLog**, a phishing-as-a-service platform it says has run credential-and-2FA theft against Microsoft 365 since at least early 2025, and it caught one campaign in the act.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieDLVRZ5AquCWN3dspVrrAGF6LynT1mpaBTry-fAblULbjcEdPBzLPYs8p2NkyjqHdwCeifPkpIFG7GMzuub4dKSB7MJX8ZUPB0n_rIW7Hkhm17dyH-_ZiCfnVAq1K0W1unizo_P2S_R4MOA8FXzCWp-ISVe0y4UPZCURXzoBH6GUf7Xtg7pkhygq9fZA/s1700-e365/kratos.png)

On February 10, operators sent tax-themed emails to about 100 organizations, mostly in the US, across manufacturing, retail, and healthcare, each carrying a W-2 document with a QR code personalized to the recipient that led to a fake Microsoft 365 login.

Stolen Microsoft logins are rarely the end of the line. The BKA said the stolen credentials could be used for further phishing, sold to other criminals, or turned into a foothold inside companies by spreading through their Microsoft 365 environments, the familiar path from one phished inbox to business email compromise.

Carsten Meywirth, who heads the BKA's cybercrime division, said the operation shows "that even highly professional phishing infrastructures can be effectively combated." The ZIT's Benjamin Krause framed it as proof of the office's "disruptive" approach of dismantling a criminal service outright rather than only charging the people behind it.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

Microsoft is notifying users caught in the campaigns. For anyone Microsoft is notifying, the fix depends on how they were hit. Where the kit only harvested credentials, a password reset and an MFA check cover it. Where its reverse-proxy mode lifted a live session, that session survives the reset, so it has to be revoked, with high-value accounts moved to phishing-resistant sign-in.

Defenders hunting for exposure can look for the kit's tell: ANY.RUN found its login pages almost always load the paired assets barr.svg and lg.svg, then POST stolen credentials to endpoints like next.php or save.php. It rates that pairing at 90% recall with near-zero false positives.

For now, the servers are offline and, the BKA says, Kratos-powered campaigns cannot continue. What the takedown did not touch is the roughly 1,800 customers or the kit code they already hold. ANY.RUN found Kratos running on disposable domains, compromised WordPress sites, and hosting shared with other adversary-in-the-middle kits, the kind of setup that reappears under a new name once the servers go down.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**]...