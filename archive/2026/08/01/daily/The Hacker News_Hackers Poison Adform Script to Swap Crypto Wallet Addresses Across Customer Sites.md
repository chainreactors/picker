---
title: Hackers Poison Adform Script to Swap Crypto Wallet Addresses Across Customer Sites
url: https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html
source: The Hacker News
date: 2026-08-01
fetch_date: 2026-08-02T05:11:27.212221
---

# Hackers Poison Adform Script to Swap Crypto Wallet Addresses Across Customer Sites

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

![cybersecurity](data:image/svg+xml;base64...)

# [Hackers Poison Adform Script to Swap Crypto Wallet Addresses Across Customer Sites](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)

**Swati Khandelwal**Aug 01, 2026Web Security / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX-el4ovGAmKfllRfhupL0SzdEoZKlouDb1_YmhCOl3owxN1ks0Do-WphuD77rka_3ukbqvPxSmFYMdBKBirYyw0DJpvSxVP5riGBR_vd7wKwnpgZfNm0RFEDLTzsvzzQB7qGtawMvpccd700dfNM2zZeFTy9cyHf4oFyHSASKRU3gmxbMgTJRtDFsSNs/s1700-e365/adform.jpg)

Attackers modified a JavaScript file served by advertising technology company **Adform**, turning it into a browser-side tool that rewrites cryptocurrency wallet addresses.

Adform detected the incident on July 27, 2026, removed the malicious code, notified affected clients, and reported it to authorities.

Anyone who visited a site carrying the affected script on July 27 and copied a Bitcoin, Ethereum, or Tron address may have pasted a different address inserted by the malicious code instead.

Adform is telling people to clear their browser cache because the altered file may remain cached after the fix, and to check any wallet address before sending funds.

Adform says the code was not designed to install software or establish persistence and operated only while an affected page remained open. The captured sample also rewrites addresses entered directly into form fields, so clipboard copying was not the only path to replacement.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The public timeline is unresolved. Adform's notice identifies July 27 as the affected date; Kevin Beaumont says he saw malicious activity via Adform over the past week.

The compromised resource is trackpoint-async.js, served from s2.adform[.]net. Adform's [implementation documentation](https://www.adformhelp.com/hc/en-us/articles/10023216886545-Custom-Naming-JavaScript) says the tracking code can run on one page, several sections, or unconditionally across an entire website. Compromising that shared resource gave the attackers a route into unrelated downstream sites without having to breach each one separately. The shared deployment path makes this a supply-chain compromise.

While the affected page remained open, one [altered address at the point of payment](https://thehackernews.com/2026/06/silent-swap-crypto-clipper-uses-fake.html) could redirect a transfer.

Beaumont, an independent security researcher, [disclosed the compromise](https://doublepulsar.com/adform-compromised-to-serve-crypto-stealer-via-supply-chain-attack-2f1ec024f33e) and wrote, "Even if you notice the address is wrong and recopy the wallet, it keeps replacing it." Beaumont reported that the file and its associated URLs, domains, and IP addresses returned no detections on VirusTotal at the time. Max Maass [published a captured copy](https://gist.github.com/malexmave/8ef5eabc7b6866698f1ea8a811c75b57) of the script on July 27.

The captured sample contains two malicious blocks appended to the legitimate library. Their replacement strings are obfuscated with a six-byte XOR key. The first watches for the copy event, tries to read the clipboard every four seconds, and to replace matching addresses.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0IfWlG7YonGjtlSbTvbsC7tFerNFekBkKivQQD5nGwGskIokt72gXtGgsgKihLFQpMP62VKTW9z-a1XB7WscFUwZijQug8RueyPSA9dxtrL2O0VRoPt-AbeG8cZfwMkgNEomvj91ZMrLbiF8lIhhJrByEU2jFHL1T53dpT24JW0R44nQU8AypLxRvRME/s1700-e365/code-crypto-ad.jpg)

It also attempts an HTTP request to 84.32.102[.]230:7744 on page load that includes the hostname and path of the page the visitor is on.

The second block walks the document's text nodes, rewrites values in input, textarea, and contenteditable elements, and restores the cursor position after a rewrite. It hooks the value setter on input and textarea elements, so programmatic writes are rewritten in transit.

It also intercepts copy, cut, paste, and input events. Both blocks contain hardcoded replacement strings for Bitcoin, Ethereum, and Tron address patterns, and Beaumont said the addresses appeared to vary.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Adform says it found no evidence that the code transmitted visitors' IP addresses or information about websites they visited. It added in [its incident notice](https://site.adform.com/resources/newsroom/security-incident-company-update/) that "Technical analysis indicates that such transmission may have been possible." The first payload's request is built to send a page hostname and path to the outside server; whether it reached the operator is not established by the sample.

Most of the scope is still missing: how many websites carried the file, how many visitors were exposed, how the attackers reached Adform's deployment path, and whether any funds were diverted. The duration gap also prevents a defensible exposure estimate because Adform's July 27 affected-date statement and Beaumont's longer observation remain unreconciled. Adform's public incident notice lists no indicators of compromise.

Adform's [2025 annual report](https://site.adform.com/media/zwkpcmh5/adform-annual-report-2025.pdf) says the company had roughly 1,800 customers, enabled 1.5 billion ads to be displayed daily, and served or transacted ads in more than 180 countries during 2025.

Those figures describe the platform, not this incident. A more useful number is how many page loads actually received the altered resource, a count Adform has not published. Adform has not publicly identified the attacker.

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
[**Share on Hack...