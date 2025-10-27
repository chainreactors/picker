---
title: Russian Software Company Pretending to Be American
url: https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html
source: Schneier on Security
date: 2022-11-17
fetch_date: 2025-10-03T23:03:33.316842
---

# Russian Software Company Pretending to Be American

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

## Russian Software Company Pretending to Be American

Computer code developed by [a company called Pushwoosh](https://www.reuters.com/technology/exclusive-russian-software-disguised-american-finds-its-way-into-us-army-cdc-2022-11-14/) is in about 8,000 Apple and Google smartphone apps. The company pretends to be American when it is actually Russian.

> According to company documents publicly filed in Russia and reviewed by Reuters, Pushwoosh is headquartered in the Siberian town of Novosibirsk, where it is registered as a software company that also carries out data processing. It employs around 40 people and reported revenue of 143,270,000 rubles ($2.4 mln) last year. Pushwoosh is registered with the Russian government to pay taxes in Russia.

On social media and in US regulatory filings, however, it presents itself as a US company, based at various times in California, Maryland, and Washington, DC, Reuters found.

What does the code do? Spy on people:

> [Pushwoosh provides code](https://tmsnrt.rs/3fV0CYE) and data processing support for software developers, enabling them to profile the online activity of smartphone app users and send tailor-made push notifications from Pushwoosh servers.
>
> On its website, Pushwoosh says it does not collect sensitive information, and Reuters found no evidence Pushwoosh mishandled user data. Russian authorities, however, have [compelled local companies](https://www.reuters.com/business/autos-transportation/russia-draws-up-law-force-taxi-firms-share-data-with-fsb-document-2022-03-29/) to hand over user data to [domestic security agencies](https://www.reuters.com/technology/how-crypto-giant-binance-built-ties-russian-fsb-linked-agency-2022-04-22/).

I have called supply chain security “an insurmountably hard problem,” and this is just another example of that.

EDITED TO ADD (12/12): [Here](https://internetsafetylabs.org/blog/news-press/reuters-breaks-story-on-dangerous-sdk-pushwoosh-found-by-isl/) is a list of apps that use the Pushwoosh SDK.

Tags: [Russia](https://www.schneier.com/tag/russia/), [smartphones](https://www.schneier.com/tag/smartphones/), [supply chain](https://www.schneier.com/tag/supply-chain/)

[Posted on November 16, 2022 at 6:03 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html) •
[30 Comments](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html#comments)

### Comments

Bob Paddock •
[November 16, 2022 8:03 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html/#comment-412470)

Is there any connection to AppMetrica?:

“AppMetrica is part of Yandex — one of the largest internet companies in Europe based in Amsterdam, Netherlands and headquartered in Moscow, Russia. Yandex started out as a search engine in 1997. Over time, it has evolved into an ecosystem of various end-user products — like Yandex.Translate, Yandex.Browser and Yandex.Zen — and a network of technologies for businesses and developers based on the latest innovations in machine learning and data science.”

Yandex does have less tendencies to censor things that other places do.

Ken\_A •
[November 16, 2022 8:12 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html/#comment-412471)

This was brought up where I work as well. While it is probably prudent to block or stop doing business with this company today I wonder if companies vet every vendor they use like this? And do the same standards apply to China, Saudia Arabia, or any other country that we typically think is suppressive?

Clive Robinson •
[November 16, 2022 9:10 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html/#comment-412476)

@ ALL,

From the article,

> *“Russian authorities, however, have compelled local companies to hand over user data to domestic security agencies.”*

So have very many other countries including Switzerland forcing a company to hand over details to a French “Witch Hunt” of political nature.

Once upon a time they did not have to do this, they simply sat on the “upstream router” and slurped up all the data just as the US NSA and UK GCHQ SigInt agencies did.

However the drive a few years back to get rid of “http” and use only “https” put quite a gimp in many authoritarian plans.

Thus bad though they are such “compelling” is proof that we can collectively “push back” against authoritarians at least sufficiently for some light to fall on a few of their otherwise hidden activities.

Grima Squeakersen •
[November 16, 2022 11:17 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html/#comment-412482)

The creation by a commercial enterprise of what to all intents are shell companies with a physical presence in various locations in order to gain business and legal advantage is hardly a novelty; it arouses my curiosity why our host would so emphasize it here. Is it solely because the company in question has a strong connection to Russia? Would identical behaviour from a company with roots in, say, Kyiv, have been called out in the same manner? Just curious…

Ted •
[November 16, 2022 11:26 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html/#comment-412485)

One of the authors of the Reuters article tweeted a link to an Internet Safety Labs post. They provide a (long) list of apps that contain the Pushwoosh SDK.

<https://twitter.com/pearswick/status/1592320094038032384>

<https://internetsafetylabs.org/blog/news-press/reuters-breaks-story-on-dangerous-sdk-pushwoosh-found-by-isl/>

Ted •
[November 16, 2022 11:44 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html/#comment-412486)

@Grima Squeakersen

> Is it solely because the company in question has a strong connection to Russia?

Think also about sanctions and FTC laws. There’s a bit more on this in the article.

Clive Robinson •
[November 16, 2022 11:57 AM](https://www.schneier.com/blog/archives/2022/11/russian-software-company-pretending-to-be-american.html/#comment-412487)

@ Grima Squeakersen,

To answer your implied question, the hint might be @Bruce’s line of,

> *“What does the code do? Spy on people”*

Which at the minimum is a legitimate security question. Not the first time it’s come up nor I suspect the last.

Now you could repeate,

> “The creation by a commercial enterprise of what to all intents are shell companies with a physical presence in various locations in order to gain business and legal advantage is hardly a novelty”

No it’s not, Israeli “spyware” companies have done it, US funded “spyware” companies have done it, so have several other European Nations where “spyware” companies are based have done it.

Ou...