---
title: Study of 85 Crypto Wallet Extensions Finds Address Leaks and Cross-Site Tracking Risks
url: https://thehackernews.com/2026/07/study-of-85-crypto-wallet-extensions.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:49:59.853607
---

# Study of 85 Crypto Wallet Extensions Finds Address Leaks and Cross-Site Tracking Risks

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

# [Study of 85 Crypto Wallet Extensions Finds Address Leaks and Cross-Site Tracking Risks](https://thehackernews.com/2026/07/study-of-85-crypto-wallet-extensions.html)

**Swati Khandelwal**Jul 14, 2026Cryptocurrency / Identity Protection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLw92quWqf4LGudVaNPBRwhiCIP4ZEBpolIRqMKbQuG6hzrXUSx89QCQT1IjMWF_6v7GEkYGOi0kYoc-ES_fELZm6pg1P8lVpRxv5mYmpzAHQMm6A_XC_fXWSWlRVh1JfjFc8wXlqtyGWovxUOOhQn8HiG4XutLeKlyv5aLY2R4UKlHTcD2pgXANePlhBq/s1700-e365/wallet-fingerprint.jpg)

Researchers at KU Leuven tested 85 of the most popular crypto wallets that run as browser extensions and found that the wallets themselves leak enough to link and track the people using them.

The way these wallets talk to websites and blockchain servers can tie a person's separate addresses together and let outsiders follow them from site to site. And on a site that already holds a name or email, the same leaks can put a real name to an "anonymous" crypto identity.

This is not a hack. The wallets behave exactly as they were built to. The 85 extensions together have about 35 million users listed on the Chrome Web Store.

The team, from the university's DistriNet security group, [posted the paper](https://arxiv.org/abs/2607.06141) this month and will present it at the PETS 2026 privacy conference in Calgary in late July.

They ran real wallets against real Web3 sites and mapped out five privacy weaknesses in how wallets and websites interact. When they reported the most far-reaching one to the wallet makers before publishing, most declined to call it a bug at all.

## Problem 1: Your separate addresses get linked

Many people keep several wallet addresses on purpose, to keep parts of their financial life apart. That only works if nobody can tell the addresses belong to the same person. But to show your balance, a wallet constantly pings outside servers, and those requests carry your address, in the clear, to whoever runs the server.

When a wallet puts two of your addresses in one request, that server learns they are yours. Seventeen wallets exposed connections between a user's separate addresses. Thirteen did it the obvious way, bundling two addresses into one request. Four more gave themselves away by firing separate requests within milliseconds of each other, a weaker but still useful signal.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Together, those wallets cover about 23 million of the installs studied. Whoever runs the server, or anyone who later gets its data, can stitch the addresses into one profile.

## Problem 2: Logging out often doesn't log you out

This problem and the next one share a starting point: a website can tell which wallets you have installed. Each wallet announces itself to any page it loads, so a script can read the exact set you carry, a fingerprint that works even if you never connect a wallet and even if you block cookies.

The researchers found that 36 of the 85 wallets do this, and their users make up about 82% of the installs studied. Those same 36 are the group behind the numbers below.

When you connect a wallet to a site and later disconnect, you assume the site loses access. Often it doesn't, for two separate reasons.

First, many sites never actually tell the wallet to cut off access. Of the 30 popular Web3 apps the team tested, only 11 sent a real revoke command when a user clicked Disconnect or Logout. The rest just cleared their own screen.

Second, even when the command is sent, many wallets ignore it. In 22 of those 36 wallets, the site could still read your address after asking the wallet to revoke it, and that access survived clearing cookies and restarting the browser.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhG2czK7APdAvT5WhdBeQfESX2LWZh5nHvZm8WAfSng3TcKecpPETM7zM4CvTIlF0Ta1vOp03TDWgODT-wywsrhv3D4IPa7APAU4pwUVZrCFn_xNXhoHCyqWY6DimXJbet7AbWr1AZ8QTZtkdBXSHyyx6_iviW8SC9zHieGWBLT27E3BnG9nDzRWvtLWxnL/s1700-e365/wallets.jpg)

That makes the address a powerful tracking tag. It is globally unique, and unlike a cookie, it does not disappear when you clear your browser. The stale permission sits inside the extension until you open the wallet's "Connected Sites" list and remove the site by hand; until then, a script on the page keeps reading the address in the background.

## Problem 3: A wallet you once connected to can expose you on other sites

The last problem reaches the furthest. Of those same 36 wallets, 23 will hand out your address from inside a frame that one page has loaded from another site. On its own, that does nothing. The catch is what a shared tracker can do with it.

Say the same tracking script runs on a crypto app you once connected to and on an ordinary, unrelated website. On the ordinary site, the tracker quietly loads that crypto app inside an invisible frame.

The app's page was already authorized by the wallet, and these wallets answer from inside the frame, so the wallet hands the address back to the script with no click from the user. The app has to allow being embedded for this to work, though plenty of them do.

Link that address to a name or email the site already has on file, and a pseudonymous crypto profile turns into a named person. A wallet address is a public record of its balances, transactions, and token holdings. Tie that to a real identity and a browsing history, and an attacker has a named target whose money is now in view.

The researchers showed this path is real and usable; they did not claim trackers are already running it at scale.

## What to do, and how the industry responded

For users, the fixes are only partial. Open your wallet and clear out old site permissions you no longer use. That stops the stale-address tracking from Problem 2, but it does nothing about the address leaks to servers or the installed-wallet fingerprint.

The researchers' [demo](https://wallet-p...