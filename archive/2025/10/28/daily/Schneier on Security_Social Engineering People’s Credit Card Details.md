---
title: Social Engineering People’s Credit Card Details
url: https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html
source: Schneier on Security
date: 2025-10-28
fetch_date: 2025-10-29T03:16:17.763338
---

# Social Engineering People’s Credit Card Details

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Social Engineering People’s Credit Card Details

Good *Wall Street Journal* [article](https://www.wsj.com/tech/cybersecurity/url-scam-texts-china-gangs-68e96097?st=XcjCtr&reflink=desktopwebshare_permalink&utm_source=substack&utm_medium=email) on criminal gangs that scam people out of their credit card information:

> Your highway toll payment is now past due, one text warns. You have U.S. Postal Service fees to pay, another threatens. You owe the New York City Department of Finance for unpaid traffic violations.
>
> The texts are ploys to get unsuspecting victims to fork over their credit-card details. The gangs behind the scams take advantage of this information to buy iPhones, gift cards, clothing and cosmetics.
>
> Criminal organizations operating out of China, which investigators blame for the toll and postage messages, have used them to make more than $1 billion over the last three years, according to the Department of Homeland Security.
>
> […]
>
> Making the fraud possible: an ingenious trick allowing criminals to install stolen card numbers in Google and Apple Wallets in Asia, then share the cards with the people in the U.S. making purchases half a world away.

Tags: [China](https://www.schneier.com/tag/china/), [credit cards](https://www.schneier.com/tag/credit-cards/), [fraud](https://www.schneier.com/tag/fraud/), [scams](https://www.schneier.com/tag/scams/), [social engineering](https://www.schneier.com/tag/social-engineering/)

[Posted on October 28, 2025 at 7:01 AM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html#comments)

### Comments

K.S •
[October 28, 2025 8:52 AM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449389)

> >install stolen card numbers in Google and Apple Wallets in Asia

How are they subverting authentication at the issuing bank? You can’t just “install” CC, there is whole process for token activation that must be followed that ought to involve bank authenticating the request.

Kam-Yung Soh •
[October 28, 2025 8:56 AM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449390)

I cannot read the WSJ article, but I am aware of the “trick allowing criminals to install stolen card numbers in Google and Apple Wallets in Asia”.

Some Singapore banks now prevent that by blocking the feature unless enabled by the cardholder. Here’s a local article about it from May 2025 [ <https://www.straitstimes.com/singapore/dbs-to-roll-out-new-switch-to-prevent-phished-card-details-from-being-added-to-mobile-wallets> ].

“SINGAPORE – A new mobile banking app feature will allow DBS and POSB card holders to control who can add their cards to mobile phone wallets from mid-May.

The switch will be “off” by default. After turning it on, users have 10 minutes to add their card details before the switch automatically turns off again.”

DBA •
[October 28, 2025 9:49 AM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449392)

Amusingly, just last week I was deleting old emails from unused dump accounts that I’d created but never checked, things like webadmin@… They went back a decade or more. I was quite amused at the number of “I’ve hacked your web cam and have seen the nasty stuff that you’ve been doing, you naughty boy” sorts, not to mention the invoice fraud attempts. I was a little disappointed that none of them attempted to map my street address, but then again, I do pay for anonymization.

Paul T •
[October 28, 2025 10:16 AM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449394)

Could CC companies establish fake CC numbers that would set off alarms when used? The number would *appear* to work, like say “in process” but would somehow activate tracing? Maybe for one of these fake numbers the CC company would redirect the web service responsible for authorizing or authenticating the purchase would accept the TCP connection then just stall out. I say all this while admitting I have no idea about all the mechanics of how a CC purchase is approved. The idea is to get the IP address submitting the purchase. If even that would do any good. Probably TOR.

KC •
[October 28, 2025 10:51 AM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449395)

@ Kam-Yung Soh, does this link work for you?

[https://archive.ph/2025.10.21-192134/https://www.wsj.com/tech/cybersecurity/url-scam-texts-china-gangs-68e96097](https://archive.ph/2025.10.21-192134/https%3A//www.wsj.com/tech/cybersecurity/url-scam-texts-china-gangs-68e96097)

KC •
[October 28, 2025 10:58 AM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449396)

The Journal also has a podcast on this story, with a nice transcript.

<https://www.wsj.com/podcasts/the-journal/no-your-toll-payment-is-not-overdue/a9ed26a4-f9a2-4937-83a5-ff1c3ed8877a>

From the article: “At least 200 SIM boxes are operating in at least **38 farms across the U.S.**, in cities such as Houston, Los Angeles, Phoenix and Miami…” We’ve got farms in office spaces, crack houses, and an auto repair shop.

And the podcast: “[Some of these SIM farms are] basically pitched as sort of a gig economy job. The criminals will give you one of these boxes. You just plug it in your home, you get it on your wireless network, **and so you’re basically a spam pumping operation at that point.”**

The WSJ’s Bob McMillan *talks in greater detail* about how these scams could be pared down. Telco’s can play a role, as can phone makers, as well as banks and credit card companies.

And a note to self … ‘anytime you find yourself reaching for your wallet with a sense of urgency’

‘Just take a breath and ask yourself, “Is this a scam?”‘

Anonymous •
[October 28, 2025 12:10 PM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449397)

I get text messages threatening dire consequences if I don’t pay a “fine.” I went to one of their links to see how their supposed payment site is set up.

I found my payment was trivial, less then 5 dollars.

The unsuspecting naive and because often it takes forever to verify with a governmental agency like motor vehicles tend to pay under the assumption they’ll only be out a small amount.

But the whole point is to get their cc details. Often followed with surprisingly large charges.

BCS •
[October 28, 2025 8:25 PM](https://www.schneier.com/blog/archives/2025/10/social-engineering-peoples-credit-card-details.html/#comment-449403)

I wonder what effect it would have if US courts allowed its cit...