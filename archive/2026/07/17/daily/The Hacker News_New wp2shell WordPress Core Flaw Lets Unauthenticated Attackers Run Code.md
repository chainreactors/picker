---
title: New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code
url: https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html
source: The Hacker News
date: 2026-07-17
fetch_date: 2026-07-18T04:46:39.296152
---

# New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code

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

# [New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code](https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html)

**Swati Khandelwal**Jul 17, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRULLT1q8L6AtUB7jgKywi_KSF8VGKkOF9yC3Snt81K1aD2XSEV1jgfIe331rXUWGqhmAyFgr1USssr4_CQmuE7HLAn0ShaQ0pHY_yvNYMjQdHtpV8i-vlk2ickhJSJDSN3amGox_DMR5hemMlrgXIk8kHoHlYKZncjpiV3ibF77ax1Yn0fEjxtgxy7tY/s1700-e365/wordpress-core.jpg)

An anonymous HTTP request can run code on a WordPress site. The bug is in core, so a bare install with zero plugins is exploitable.

Every 6.9 and 7.0 site was in range until Friday, when WordPress shipped 6.9.5 and 7.0.2 and enabled what it calls forced updates through its auto-update system.

Adam Kues at Assetnote, Searchlight Cyber's attack surface management arm, found the flaw and reported it through WordPress's [HackerOne program](https://hackerone.com/wordpress). The [writeup](https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core), published under the name **wp2shell**, says the attack has "no preconditions and can be exploited by an anonymous user."

The firm is sitting on the technical details for now and has put up a [checker](https://wp2shell.com/) at wp2shell.com instead, so owners can test their own instance.

WordPress released 6.9.5 and 7.0.2 on July 17, 2026, closing a pre-auth RCE in core that an anonymous request can trigger against a default install with no plugins. Two ranges are affected:

* 6.9.0 through 6.9.4, fixed in 6.9.5
* 7.0.0 through 7.0.1, fixed in 7.0.2

WordPress has not said whether the forced push reaches sites that turned auto-updates off. Check what you are actually running rather than assume it landed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

7.1 beta2 carries the same fix. Sites still on 6.8 have an update waiting too, but 6.8.6 is for the second SQL injection bug in the same round, reported by a different team.

Searchlight's post estimates that over 500 million websites run WordPress. That figure is the total install base, not the vulnerable population: the flawed code only exists from 6.9 onward, and 6.9 shipped on [December 2, 2025](https://wordpress.org/documentation/wordpress-version/version-6-9/). So every affected site is running a release less than eight months old, and neither advisory says how many sites that covers.

WordPress is more forthcoming about the bug class than the researcher is. Its [release post](https://wordpress.org/news/2026/07/wordpress-7-0-2-release/) describes Kues's finding as "a REST API batch-route confusion and SQL injection issue leading to Remote Code Execution." The release covers one critical and one high severity flaw, and WordPress does not say which is which.

The [version page](https://wordpress.org/documentation/wordpress-version/version-7-0-2/) lists the three files 7.0.2 touched, covering both fixes: /wp-includes/rest-api/class-wp-rest-server.php, /wp-includes/class-wp-query.php, and /wp-includes/rest-api.php. The batch endpoint is not new. WordPress has shipped it since [5.6 in November 2020](https://make.wordpress.org/core/2020/11/20/rest-api-batch-framework-in-wordpress-5-6/) and documented the request format publicly ever since. Nothing published so far explains what changed in 6.9 to open it.

Neither advisory carries a CVE ID or a CVSS score, and no CVE record had appeared by July 18. CVE-keyed scanners and inventories will not flag this one, and CISA needs a CVE before it can add anything to the [KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). Track it by version number instead.

## If you can't update today

Every mitigation Searchlight offers comes down to keeping anonymous callers off the batch endpoint. Three options, all of them stopgaps until you update, and all of them capable of breaking legitimate integrations:

* At a WAF, block both /wp-json/batch/v1 and rest\_route=/batch/v1. The firm is explicit that both have to go, because a rule covering only the /wp-json path leaves the query-string route open.
* [Disable WP REST API](https://wordpress.org/plugins/disable-wp-rest-api/), which kills unauthenticated REST access wholesale.
* A short [drop-in plugin](https://wp2shell.com/) that publishes and rejects anonymous /batch/v1 requests at rest\_pre\_dispatch.

No exploitation attempt has been reported as of July 18. With no CVE to tag and no public signature to match, nobody is really looking yet.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Mass exploitation of WordPress is an industry now. Before its server leaked in June, one caching-plugin flaw alone got the [WP-SHELLSTORM](https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html) crew into more than 17,000 sites by its own count. That bug was already public, already patched, and only worked on a non-default setting.

When Drupal patched an anonymous SQL injection in its own core in May, Searchlight turned that public fix into a [same-day teardown](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/) with two working proofs of concept. That was someone else's bug and someone else's patch, and nothing obliges the firm to do the same to its own. But a day is what it took, and the people who set that clock are the ones now betting silence buys defenders time.

WordPress core is open source, and 7.0.1 and 7.0.2 both sit in the [public release archive](https://wordpress.org/download/releases/), so the comparison is available to anyone who wants it. That is the ...