---
title: Web Security is Too Hard
url: https://textslashplain.com/2026/08/04/security-is-hard-yall/
source: text/plain
date: 2026-08-04
fetch_date: 2026-08-05T04:58:20.291372
---

# Web Security is Too Hard

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Web Security is Too Hard

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-08-042026-08-04](https://textslashplain.com/2026/08/04/security-is-hard-yall/)Posted in[browsers](https://textslashplain.com/category/browsers/), [security](https://textslashplain.com/category/security/), [storytelling](https://textslashplain.com/category/storytelling/), [web](https://textslashplain.com/category/tech/web/)Tags:[best-practices](https://textslashplain.com/tag/best-practices/), [browsers](https://textslashplain.com/tag/browsers/), [phishing](https://textslashplain.com/tag/phishing/), [SmartScreen](https://textslashplain.com/tag/smartscreen/)

It started innocently enough. I saw a tweet about a new product offering from one of my favorite companies, Cloudflare.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-33.png?resize=670%2C260&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-33.png?ssl=1)

Neat! I clicked through to the site and there it is:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-32.png?resize=750%2C803&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-32.png?ssl=1)

And ***huzzah**!,* my preferred handle, `@ericlaw` is still available. **I’d better hurry** to claim it before someone else gets it!

Since I’m already a long-time Cloudflare user, I just need to sign in. That makes sense, how else will they bind the handle to my account?

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-34.png?resize=750%2C474&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-34.png?ssl=1)

Easy peasy. I’m in. Looks like there’s just one more step, I gotta authorize the new feature?

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-35.png?resize=750%2C447&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-35.png?ssl=1)

*But wait a sec!*

This looks **exactly** like one of those [Consent Phishing attacks](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/#:~:text=in%20this%20post.-,%E2%80%9CConsent%20Phishing%E2%80%9D,-In%20the%20first) that have been so popular over the last few years!

And wait, why is the entry point on `cloudflare.pay`, a site that *doesn’t* already have my credentials, rather than something within the `cloudflare.com` domain which does (e.g. `cloudflare.com/pay`)? **There is no inherent technical relationship between a .com domain and a .pay domain**. Domain names under the`.pay` sTLD are available to [anyone with $20](https://tld-list.com/tld/pay) (unlike, e.g. `[.bank](https://textslashplain.com/2023/05/13/new-tlds-not-bad-actually/)` which requires more vetting), so there’s nothing that would stop me from registering my own `cloudflarepayments.pay` domain name in just a few minutes.

And why doesn’t Cloudflare’s permission site recognize its own company’s feature? And that green checkmark looks suspicious as heck– an attacker could probably just shove that emoji inside their misleading display name, the same way that folks trying to [phish Microsoft email accounts](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/#:~:text=granting%20the%20attacker%20access%20to%20the%20content%20of%20their%20account) use misleading app names and icons:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-39.png?resize=395%2C73&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-39.png?ssl=1)

Fake Outlook OAuth phishing request

**The guys at Cloudflare are geniuses who know their stuff. This has *got* to be an attack.** It’s a clever one — I was feeling such a [sense of urgency](https://textslashplain.com/2023/10/16/security-the-impact-of-time/#:~:text=fast%2Dmoving%20attackers.-,The%20Human%20Factor,-Many%20forms%20of) because I wanted to “win” the race to get my desired handle. *Very very clever!*

Unfortunately, the Cloudflare permission page doesn’t follow [best practices](https://textslashplain.com/2023/01/11/attack-techniques-priming-attacks-on-legitimate-sites/#:~:text=nuked%20from%20orbit.-,Best%20Practices,-When%20building%20web), so there’s no “**Report suspicious request**” link I can use to let the Cloudflare folks know that their customers are under attack.

Let me go back to my Cloudflare dashboard and try to get to the Wallet feature from its sidebar. Hrm. **It’s not there.** Now, Wallet purports to be “a new feature”, so maybe the Dashboard just isn’t updated yet. A search of the docs turns up nothing. Let’s ask the AI agent in chat.

The very first thing the chat agent wants is access to my account:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-41.png?resize=438%2C370&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-41.png?ssl=1)

This feels a little weird, but the page is still `cloudflare.com` so I guess I can give the thing access to things it already has access to. Weirdly, the AI agent first proposes that I grant it **full control** rather than **read only** access, which feels like a failure of the principle of least privilege, but I don’t actually need to ask an account specific question anyway. After granting read permission, the agent allows me to ask my question:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-36.png?resize=652%2C784&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-36.png?ssl=1)

Oh, wow. **Cloudflare says it really *is* an attack!** Let’s [report the phish right away](https://textslashplain.com/2023/01/19/defense-techniques-reporting-phish/)!

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-38.png?resize=689%2C443&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-38.png?ssl=1)

A few minutes later… womp womp…

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-37.png?resize=750%2C514&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-37.png?ssl=1)

*Oh dear.*

After a few minutes of further frantic searching, it turns out that this is, in fact, a legitimate new Cloudflare product and a legitimate site, despite giving every indication of being a clever phishing attack.

It further [turns out](https://x.com/WillPapper/status/2084701868090093736) that that suspicious green checkmark is not part of the app’s untrustworthy display name but instead a ([poorly placed](https://textslashplain.com/2017/01/14/the-line-of-death/)) security UI element that a user is expected to hover over to get the security details:

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-40.png?resize=481%2C123&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/08/image-40.png?ssl=1)

The Cloudflare folks apparently want security issues [reported via HackerOne](https://www.cloudflare.com/disclosure/) (*which wouldn’t let me log in because the Cloudflare CAPTCHA HackerOne uses seems to be [broken](https://x.com/ericlaw/status/2084713054609064046)…*).

When legitimate websites sometimes act very very phishy, consider how hard it must be for URL Reputation services like [Microsoft SmartScreen](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/) and Google SafeBrowsing to block malicious sites without false positives as millions of new sites are added to the web every week.

## Lessons

**Web Developers**, please follow every best practice, **I’m *begging* you**:

* Host apps and content under your trusted domain name (e.g. `cloudflare.com/pay` or `pay.cloudflare.com`. *If you must add a new name, link to it directly from a page on your trusted domain...