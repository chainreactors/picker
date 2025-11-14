---
title: Book Review: The Business of Secrets
url: https://www.schneier.com/blog/archives/2025/11/book-review-the-business-of-secrets.html
source: Schneier on Security
date: 2025-11-13
fetch_date: 2025-11-14T03:13:38.964667
---

# Book Review: The Business of Secrets

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

## Book Review: The Business of Secrets

**The Business of Secrets: Adventures in Selling Encryption Around the World by Fred Kinch (May 24, 2004)**

From the vantage point of today, it’s surreal reading about the commercial cryptography business in the 1970s. Nobody knew anything. The manufacturers didn’t know whether the cryptography they sold was any good. The customers didn’t know whether the crypto they bought was any good. Everyone pretended to know, thought they knew, or knew better than to even try to know.

The Business of Secrets is the self-published memoirs of Fred Kinch. He was founder and vice president of—mostly sales—at a US cryptographic hardware company called Datotek, from company’s founding in 1969 until 1982. It’s mostly a disjointed collection of stories about the difficulties of selling to governments worldwide, along with descriptions of the highs and (mostly) lows of foreign airlines, foreign hotels, and foreign travel in general. But it’s also about encryption.

Datotek sold cryptographic equipment in the era after rotor machines and before modern academic cryptography. The company initially marketed computer-file encryption, but pivoted o link encryption – low-speed data, voice, fax – because that’s what the market wanted.

These were the years where the NSA hired anyone promising in the field, and routinely classified – and thereby blocked – publication of academic mathematics papers of those they didn’t hire. They controlled the fielding of strong cryptography by aggressively using the International Traffic in Arms regulation. Kinch talks about the difficulties in getting an expert license for Datotek’s products; he didn’t know that the only reason he ever got that license was because the NSA was able to break his company’s stuff. He had no idea that his largest competitor, the Swiss company Crypto AG, was owned and controlled by the CIA and its West German equivalent. “Wouldn’t that have made our life easier if we had known that back in the 1970s?” Yes, it would. But no one knew.

Glimmers of the clandestine world peek out of the book. Countries like France ask detailed tech questions, borrow or buy a couple of units for “evaluation,” and then disappear again. Did they break the encryption? Did they just want to see what their adversaries were using? No one at Datotek knew.

Kinch “carried the key generator logic diagrams and schematics” with him – even today it’s good practice not to rely on their secrecy for security—but the details seem laughably insecure: four linear shift registers of 29, 23, 13, and 7 bits, variable stepping, and a small nonlinear final transformation. The NSA probably used this as a challenge to its new hires. But Datotek didn’t know that, at the time.

Kinch writes: “The strength of the cryptography had to be accepted on trust and only on trust.” Yes, but it’s so, so weird to read about it in practice. Kinch demonstrated the security of his telephone encryptors by hooking a pair of them up and having people listen to the encrypted voice. It’s rather like demonstrating the safety of a food additive by showing that someone doesn’t immediately fall over dead after eating it. (In one absolutely bizarre anecdote, an Argentine sergeant with a “hearing defect” could understand the scrambled analog voice. Datotek fixed its security, but only offered the upgrade to the Argentines, because no one else complained. As I said, no one knew anything.)

In his postscript, he writes that even if the NSA could break Datotek’s products, they were “vastly superior to what [his customers] had used previously.” Given that the previous devices were electromechanical rotor machines, and that his primary competition was a CIA-run operation, he’s probably right. But even today, we know nothing about any other country’s cryptanalytic capabilities during those decades.

A lot of this book has a “you had to be there” vibe. And it’s mostly tone-deaf. There is no real acknowledgment of the human-rights-abusing countries on Datotek’s customer list, and how their products might have assisted those governments. But it’s a fascinating artifact of an era before commercial cryptography went mainstream, before academic cryptography became approved for US classified data, before those of us outside the triple fences of the NSA understood the mathematics of cryptography.

*This book review originally appeared in [AFIO](https://www.afio.com/book-reviews/).*

Tags: [business of security](https://www.schneier.com/tag/business-of-security/), [cryptography](https://www.schneier.com/tag/cryptography/), [encryption](https://www.schneier.com/tag/encryption/), [history of cryptography](https://www.schneier.com/tag/history-of-cryptography/)

[Posted on November 13, 2025 at 7:09 AM](https://www.schneier.com/blog/archives/2025/11/book-review-the-business-of-secrets.html) •
[3 Comments](https://www.schneier.com/blog/archives/2025/11/book-review-the-business-of-secrets.html#comments)

### Comments

Clive Robinson •
[November 13, 2025 12:23 PM](https://www.schneier.com/blog/archives/2025/11/book-review-the-business-of-secrets.html/#comment-449857)

@ Bruce,

I’m guessing from,

> “but the details seem laughably insecure: four linear shift registers of 29, 23, 13, and 7 bits, variable stepping, and a small nonlinear final transformation.

That it was a “poorman’s stream cipher”?

lurker •
[November 13, 2025 1:25 PM](https://www.schneier.com/blog/archives/2025/11/book-review-the-business-of-secrets.html/#comment-449858)

@Bruce
Typo in subhead: should be (May 24, 2024)

Also

> descriptions of the highs and (mostly) lows of foreign airlines, foreign hotels, and foreign travel in general.

and

> A lot of this book has a “you had to be there” vibe. And it’s mostly tone-deaf.

fits with the book being self published. Are we still too close to the action for an American publisher to touch this?

There is also a review in Cryptologia for those who subscribe.

Dave •
[November 13, 2025 9:11 PM](https://www.schneier.com/blog/archives/2025/11/book-review-the-business-of-secrets.html/#comment-449865)

@lurker: Which issue of Cryptologia? I seem to have missed that one.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/11/book-review-the-business-of-secrets.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/11/book-review-the-business-of-secrets.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F11%2Fbook-review-the-business-of-secrets.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required...