---
title: Google Is Suing Chinese Scammers Who Are Using Gemini
url: https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html
source: Schneier on Security
date: 2026-07-07
fetch_date: 2026-07-08T05:05:49.970757
---

# Google Is Suing Chinese Scammers Who Are Using Gemini

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

## Google Is Suing Chinese Scammers Who Are Using Gemini

Not sure [this](https://arstechnica.com/google/2026/06/google-sues-chinese-cybercrime-network-that-used-gemini-to-automate-scams/) will have any effect, but I support the effort:

> According to Google’s legal filing, Outsider Enterprise operates through Telegram. The group offers phishing-as-a-service to individuals who may not be technically savvy enough to set up fraudulent websites and text campaigns on their own. In its Telegram channels, Outsider Enterprise reportedly provided instructions on how to use Google’s Gemini AI to create websites that imitate those of Google, YouTube, and government agencies such as New York’s E-ZPass. The group offered nearly 300 scam templates.
>
> […]
>
> Google worked with AT&T, Verizon, and T-Mobile to block many of these malicious text messages, and Google notes that its on-device scam detection in Google Messages probably helped reduce the number of successful phishing attempts, too. This AI-powered feature apparently stops 10 billion scam texts every month, so it’s fair to expect it caught at least some Outsider Enterprise activity.

Another [article](https://www.digitaltrends.com/phones/scammers-used-gemini-ai-to-power-a-massive-phishing-operation-and-google-just-sued-them/).

Tags: [AI](https://www.schneier.com/tag/ai/), [China](https://www.schneier.com/tag/china/), [courts](https://www.schneier.com/tag/courts/), [cybercrime](https://www.schneier.com/tag/cybercrime/), [phishing](https://www.schneier.com/tag/phishing/), [scams](https://www.schneier.com/tag/scams/)

[Posted on July 7, 2026 at 6:43 AM](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html#comments)

### Comments

Clive Robinson •
[July 7, 2026 8:30 AM](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html/#comment-455793)

@ Bruce,

With regards,

> “Not sure this will have any effect”

Basic science says all effects have causes.

Likewise to build something solid and lasting it requires considered construction based on solid foundations.

So whilst the effect may not be immediate or obvious initially, if it forms a solid foundation then more can be built upon it.

KC •
[July 7, 2026 11:27 AM](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html/#comment-455794)

> The company has called out *seven different potential federal laws* …

Love that you can set up alerts, for example on Congress.gov, to keep tabs on these.

Big working group list proposed under the ‘National Strategy for Combating Scams Act’ ([H.R. 6425](https://www.congress.gov/bill/119th-congress/house-bill/6425) / S. 3355). Reports required for ‘STOP Scams Against Seniors Act’ ([H.R. 6426](https://www.congress.gov/bill/119th-congress/house-bill/6426) / S. 4821) … I guess they’re all bipartisan.

[Tris Simondsen](https://trissimondsen.wordpress.com) •
[July 7, 2026 1:21 PM](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html/#comment-455796)

The reason Outsider Enterprise’s phishing-as-a-service ring is so effective isn’t just a failure of Google’s API moderation, it is a structural exploitation of how generative tensor architectures fundamentally process ambiguity.

In a Zero-Trust architecture, we demand continuous validation of intent and authorization. But when a scammer prompts Gemini to generate an E-ZPass login page, the AI hits an unobservable information partition. It mathematically cannot observe the behavioral state of the user (e.g., a legitimate New York state developer vs. a malicious actor). The F-identifiable boundary is missing.

Because modern LLMs cannot maintain epistemic caution, they suffer what the Observational Sufficiency Principle (OSP) formalizes as an Equal-Weight Failure. At the tensor layer, the model takes distinct, non-verifiable latent paths and flattens them into identical downstream vectors (TM1 = TM2). Instead of halting at the boundary of what it can prove, the model executes “latent completion”, arbitrarily inventing a default state to bridge the gap, which effectively launders the scammer’s intent into functional HTML/CSS.

These scammers aren’t just bypassing content filters; they are weaponizing the AI’s architectural mandate to guess. This mathematically voids the Zero-Trust Evidence Contract, meaning we can never rely on the “execute” layer of a generative model to self-regulate security boundaries. It cannot recognize its own epistemic limits.

Please see below for the complete formal proof on why this tensor-level latent completion structurally breaks Zero-Trust:

<https://trissimondsen.wordpress.com/2026/07/06/the-equal-weight-failure-how-ai-latent-completion-voids-the-zero-trust-evidence-contract/>

Treating this as a moderation problem misses the physics of the issue. Generative AI architecture is currently incompatible with Zero-Trust.

Your thoughts?

Rontea •
[July 7, 2026 2:34 PM](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html/#comment-455797)

Law enforcement coordination and proactive industry measures, like Google’s collaboration with carriers and on-device detection, are essential, but the scale of these operations shows that defensive efforts alone can’t fully close the gap.

We’re moving into an era where AI-driven attacks will adapt as quickly as we counter them. Civil actions and domain takedowns are important signals, but without parallel international legal frameworks and cooperation, the risk remains high. Public education—and the ability to validate digital trust at scale—will likely be as important as any technical safeguard to keeping users safe.

lurker •
[July 7, 2026 2:50 PM](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html/#comment-455798)

Suing a handful of named Chinese in a New York court seems like a pretty futile way to end this madness.

Google makes guns. People use them to shoot other people. Nothing to see here. Move along please.

lurker •
[July 7, 2026 8:25 PM](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html/#comment-455815)

@Tris Simondsen, ALL

Attributing to AI machines the ability to “invent” or “guess” continues the popular anthropomorphising, even to the extent of “It cannot recognize its own epistemic limits.”

Of course not. It has no organs (organic or electro-mechanical) of recognition. It can compare an item with another it has memory of, but when the difference between them falls below the machine’s discrimination limit it deems them equal. Humans do this too while learnin...