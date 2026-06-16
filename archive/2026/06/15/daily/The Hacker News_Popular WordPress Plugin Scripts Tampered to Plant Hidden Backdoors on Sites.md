---
title: Popular WordPress Plugin Scripts Tampered to Plant Hidden Backdoors on Sites
url: https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html
source: The Hacker News
date: 2026-06-15
fetch_date: 2026-06-16T07:17:04.180650
---

# Popular WordPress Plugin Scripts Tampered to Plant Hidden Backdoors on Sites

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Popular WordPress Plugin Scripts Tampered to Plant Hidden Backdoors on Sites](https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html)

**Swati Khandelwal**Jun 15, 2026Web Security / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5TE5Z8cG6zx7J64PdC2qxAh0h0o-KRwA1vEBvunxSEWkh5QmlsaIe2zKWUL7yX28chYs9zWMwA6eBcmTzfRIaKtyI53hKlLTSar9d4EMnjPQiY8KoQ0JldPkCQvc6B4EbO2ktcQV07rr4nf_RFBnA_eNHXChsNTOzvB3Fv7-0ENUDa8W8ut1rAdVOFAjh/s1700-e365/wordpress.jpg)

An attacker tampered with trusted JavaScript files used by WordPress sites running **PushEngage**, **OptinMonster**, and **TrustPulse**, turning those files into a way to break into the sites.

When a site administrator was logged in as the file loaded, the code created an admin account under the attacker's control and installed a hidden plugin that opened a way back in. Ordinary visitors did not trigger it.

Any site that was hit should be treated as compromised. All three plugins are run by one company, Awesome Motive, which had not commented on the two larger plugins as of June 15.

Security firm [Sansec](https://sansec.io/research/optinmonster-supply-chain-attack) disclosed the wider campaign on June 13, finding the same malicious code in JavaScript served for all three plugins.

PushEngage followed a day later with its own [incident notice](https://www.pushengage.com/security-incident-tampered-script-served-via-pushengage/), confirming an attacker had served tampered copies of its script and that sites loading them could be taken over.

PushEngage, acquired by Awesome Motive years ago, is so far the only one of the three to issue guidance; OptinMonster and TrustPulse users have heard nothing official.

The window was not the same for each plugin. Sansec saw the malicious code in OptinMonster and TrustPulse for only about 25 minutes on June 12, first around 22:17 UTC and gone by 22:42. PushEngage's exposure ran longer: several hours on June 12, and its script was still being served from some of the CDN's servers into June 14.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

So the two plugins with the most sites had the smallest window, and PushEngage had the largest.

Sansec estimates that the three plugins reach more than 1.2 million sites between them, the bulk of that OptinMonster, which alone has over a million active installs. PushEngage's [WordPress plugin](https://wordpress.org/plugins/pushengage/) has more than 9,000. That figure is reach, not damage: it counts sites that run the plugins, not sites that were broken into.

## How the attack worked

The poisoned script did nothing on a normal page view. It acted only when a logged-in WordPress administrator loaded it, then used that admin's session to take over.

That design is also why the WordPress dashboard cannot tell you whether you were hit: the backdoor is built to stay out of the admin screens, so the only reliable check is on the server itself.

In PushEngage's case, the tampered files were its normal embeds, pushengage-web-sdk.js and pushengage-subscription.js, served from clientcdn.pushengage.com, the content-delivery network that pushes PushEngage's script out to customer sites. OptinMonster and TrustPulse were hit through separate Awesome Motive CDN endpoints.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnM_Hcm_lzwpzJ7zh3B0KkvLzEmQOl1rBjZvoS5DaBpMy5XTOXCqaSMRG5oSa3OhG52Cxif24nrtpW6eacmsH8LLu7yblRSmB7Va8GwaYSYu_v6GW0y-VKjPecMnxz-g3tI84RZkQ1BfWixVPgIcvl4JK8N5E37aciLGD-uU1xQkVseW9b9usBLzYIj-s0/s1700-e365/wp-push.jpg)

PushEngage says the rest of its systems were untouched: it found no sign that its main application or the servers holding customer data were reached.

By PushEngage's own account, once the script ran with an administrator logged in, it:

1. used that admin's session to act with full permissions,
2. created a new admin account under the attacker's control,
3. installed a plugin that does not show up in the dashboard, and
4. sent the new login details and site information to tidio[.]cc, a fake domain made to look like the real tidio.com.

Sansec found the same sequence across all three plugins. The tidio[.]cc domain was registered on April 28, weeks before the attack, which points to a planned operation rather than a quick smash and grab.

The hidden plugin is the real prize. It opens what is known as a web shell, a remote command channel: anyone who knows the right URL can run code on the server without logging in. From there the attacker can read or change any file, copy the database, plant more backdoors, inject card-skimming code, redirect visitors, or steal data.

The extra admin account is a simple way back in if you delete the plugin but miss the account. And because the attacker can run code freely, removing the named plugin and account may not be enough; both Sansec and PushEngage say to assume other backdoors could remain.

## How the attacker got in

This is the part the two accounts disagree on. PushEngage says the attacker first broke into the server running its marketing website, through a known flaw in **UpdraftPlus**, a WordPress backup plugin. That server is separate from the systems that run the product and store customer data.

What mattered was not the server itself but a key sitting on it: a CDN API key. With that key, the attacker did not need to break into PushEngage's main systems. It could simply change the files the CDN was already delivering to customer sites.

Sansec is not convinced the entry point is settled. It says the breached system is still unknown, with Awesome Motive's own servers the most likely place, the CDN account possible, and the CDN provider, BunnyNet, unlikely.

Sansec's public analysis does not examine or endorse the UpdraftPlus theory; that account comes from PushEngage alone, about its own environment. UpdraftPlus does have a separate authentication-bypass bug, [CVE...