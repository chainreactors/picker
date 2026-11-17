---
title: Usable Security at Luxury Hotels
url: https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html
source: Schneier on Security
date: 2026-11-16
fetch_date: 2026-11-17T09:57:54.434574
---

# Usable Security at Luxury Hotels

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

## Usable Security at Luxury Hotels

Interesting [case study](https://www.benthamsgaze.org/2026/11/11/phishing-at-the-front-desk-usable-security-in-luxury-hotels/) from luxury hotels. Attackers used a fake booking request to gain access to a reservations inbox, where they copied genuine refund requests and got fraudulent ones approved.

This is a good illustration why “just don’t click on links” is bad advice. It can’t work when answering strangers’ emails is the job. Even worse, in this case the guest-first culture punishes hesitation. More interesting, the case study shows that splitting security between owner, operator, and brand leaves nobody accountable. And this is exactly the setting where blaming staff becomes the convenient answer.

Tags: [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [fraud](https://www.schneier.com/tag/fraud/), [hotels](https://www.schneier.com/tag/hotels/), [phishing](https://www.schneier.com/tag/phishing/)

[Posted on November 16, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html) •
[10 Comments](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html#comments)

### Comments

TimH •
[November 16, 2026 7:22 AM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html/#comment-459689)

TFA: “We suspect a colleague opened the email and clicked the link, unknowingly giving the attackers access to the reservations shared inbox.”

So there was no front-end layer checking inbox content for such dubiosities? Or limiting access to specific computer MACs, or intranet IP ranges.

The ball is in the IT org’s court for not setting this up.

Same with IT who can’t set a limit of 5 CCs on emails to stop an email blast CCing every customer.

For Profit •
[November 16, 2026 8:36 AM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html/#comment-459690)

IMHO:
Responsibility for IT security: The company managing the hotel.
Which data security scheme to follow when operating under data protection regimes of multiple countries?: The most stringent one. Probably the GDPR of the EU is a good starting point.

Larry Seltzer •
[November 16, 2026 9:10 AM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html/#comment-459691)

I’d say we don’t know nearly enough to point fingers, but the general point is valid: “Proper” security practices run a risk of false positives, and even one of those is a scandal in such an establishment.
It may be that the email was filled with red flags of the sort mentioned in other comments, like many cc’s. We can’t really blame IT yet because it was sent to someone’s Gmail account. It may be that p=reject DMARC enforcement would have stopped these emails, but some number of false positives, even if small, is inevitable.
I would wager that there is, in almost all cases, something about the email that an aggressive scan would find and could flag as suspicious, and the compromise is somewhere in there. Email clients should have a prominent way to label less-egregious emails as suspicious and include tips for the reader to check, without putting them in the spam folder to be forgotten.
This means the reader, someone at the hotel in this case, has to be held responsible for following the tips, or perhaps running them past someone better equipped to do so. Many of you will say this is too much to expect of the average reader, but something has to give here.

Rontea •
[November 16, 2026 9:18 AM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html/#comment-459692)

The attackers didn’t need to hack their way in—they just had to blend into normal hotel operations. In luxury hospitality, where every email could be a VIP guest, traditional “don’t click” security guidance falls apart. The pace, service culture, and constant demand for ultra-personalized attention create the perfect conditions for attackers to exploit. Until security frameworks truly align with these operational realities, we’ll keep seeing incidents like this. It’s not user error—it’s a mismatch between policy and environment.

Clive Robinson •
[November 16, 2026 10:17 AM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html/#comment-459694)

@ Bruce, Rontea, ALL,

Unfortunately as our host @Bruce notes,

> “And this is exactly the setting where blaming staff becomes the convenient answer.”

But the questions about “convenient” need to be asked, because as @Rontea notes,

> “It’s not user error—it’s a mismatch between policy and environment.”

But consider the current “business drivers”,

> “The pace, service culture, and constant demand for ultra-personalized attention create the perfect conditions for attackers to exploit.”

Questions should arise such as,

1, Will this ever change? – Probably not.
2, Will there be ways to stop attacks whilst keeping the service culture? – Put simply no.

Have a think about AI for a moment…

Not as a solution to this problem, but as an example of why you can not fix this type of vulnerability.

“Human orientated work rules” are actually,

A, Guide rails.
B, Sandboxes.

Written for humans.

We know that there is proof that with AI “Guide rails” can always be subverted and by extension “Sandboxes” always broken out from.

So ask the question,

“**If AI systems will provably always be open to being subverted, why should we expect human work will not be?**”

The thing is anything that AI will fail at, so will humans.

Rontea •
[November 16, 2026 2:04 PM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html/#comment-459696)

@Clive Robinson
Re: “If AI systems will provably always be open to being subverted, why should we expect human work will not be?”

I think that the essence of this question isn’t whether either humans or machines are perfectly secure—they aren’t—but how we layer defenses, monitor for anomalies, and minimize the blast radius when something inevitably goes wrong.

Clive Robinson •
[November 16, 2026 4:07 PM](https://www.schneier.com/blog/archives/2026/11/usable-security-at-luxury-hotels.html/#comment-459697)

@ Rontea, ALL,

With regards,

> “I think that the essence of this question isn’t whether either humans or machines are perfectly secure —they aren’t—”

My point was not “they aren’t” but “provably they can not be” secure. In all manner of ways.

At the very least it’s a very fundamental observation of a communications channel where there is no “verified shared secret”[1].

Further few have thought through privacy for “more than two party” communications, which opens up so many vulnerabilities it’s almost “unplumbed depths”.

But what I was pointing out was not just at that lower a level in the communications stack.

Which brings us to your,

> “but how we layer defenses, m...