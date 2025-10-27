---
title: New Lawsuit Attempting to Make Adversarial Interoperability Legal
url: https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html
source: Schneier on Security
date: 2024-05-07
fetch_date: 2025-10-06T17:20:09.099702
---

# New Lawsuit Attempting to Make Adversarial Interoperability Legal

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

## New Lawsuit Attempting to Make Adversarial Interoperability Legal

Lots of complicated details here: too many for me to summarize well. It involves an obscure Section 230 provision—and an even more obscure typo. Read [this](https://www.techdirt.com/2024/05/02/was-there-a-trojan-horse-hidden-in-section-230-all-along-that-could-enable-adversarial-interoperability/).

Tags: [copyright](https://www.schneier.com/tag/copyright/), [courts](https://www.schneier.com/tag/courts/)

[Posted on May 6, 2024 at 7:03 AM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html) •
[9 Comments](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html#comments)

### Comments

Winter •
[May 6, 2024 8:30 AM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436358)

The whole lawsuit hinges around this text in the law (c)(2)(B):

> No provider or user of an interactive computer service shall be held liable on account of any action taken to enable or make available to information content providers or others the technical means to restrict access to material described in paragraph (1)

As usual, the comment section can hide deeper insights:

> I suspect that paragraph was put there to protect porn filters from lawsuits, though it should theoretically also protect ad blockers and other kinds of middleware.

So, adblockers might be perfectly legal!

noname •
[May 6, 2024 9:06 AM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436359)

Oof. Could the typo in Section 230 add a technical snag in Professor Zuckerman’s request to immunize himself from civil liability for his middleware ‘Unfollow Everything 2.0’?

Here’s a link to the Section 230 text:

The snag is that Section (c)(2)(B) references paragraph (1), as Winter points out, rather than the preceding paragraph (A).

The case does seem fraught especially since Meta threatened Louis Barclay, the creator of Unfollow Everything [1.0] with legal action if he did not take his tool down. Barclay complied.

On the other hand, Mike Masnick notes that Meta is doing a lot of AI training scraping itself and backed down off a case earlier this year where it was suing Bright Data for scraping/data mining.

Q •
[May 6, 2024 10:37 AM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436363)

techdirt.com is inaccessible.

The title is “Just a moment…”
The text is “Enable JavaScript and cookies to continue”

It demands I make my system more insecure before I can see anything.

If only there was some easier method to display text without needing JS.

noname •
[May 6, 2024 6:28 PM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436399)

@JonKnowsNothing

You’re an amazing legal analyst. Any thoughts on the fact that this lawsuit is seeking a declaratory judgement?

> From Mike Masnick: “Also, this is not my area of expertise by any stretch of the imagination, but I remember hearing in the past that outside of IP law, courts (and especially courts in the 9th Circuit) absolutely disfavor lawsuits for declaratory judgment (i.e., a lawsuit before there’s any controversy, where you ask the court “hey, can you just check and make sure I’m on the right side of the law here…”). So I could totally see the judge saying “sorry, this is not a proper use of our time” and tossing it. In fact, that might be the most likely result.”

JonKnowsNothing •
[May 6, 2024 7:48 PM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436402)

@noname , All

re: *preemptive rulings*

IANAL

In many cases I’ve read about,

* you have to have “standing” or a reason to be in front of the court.
* you also have to have a “harm” that has occurred.

In Appeals courts, there has to be a question of Legal Interpretation, which is not the same as “new evidence”.

In courts where there is a contract dispute, the contract gives the standing and harm.

Any issue of significance will wind it’s way to SCOTUS after ~10yrs traversing the lower courts. SCOTUS is only interested in the “finer details and punctuation”, for which they rely on the lower court proceedings to provide.

SCOTUS does get involved with some extraordinary proceedings like clemency, but they do not interfere very often and leave the lower court rulings stand.

Unless there are special circumstances, I don’t think the courts will be amenable.

* You gotta stand in line like everyone else

Mike B •
[May 6, 2024 9:29 PM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436406)

@Amos:
“… US Constitution grants Congress NO AUTHORITY whatsoever to issue rules on any aspect of computers.”

Nor on any aspect of long-range ballistic missiles armed with nuclear fission or fusion warheads. Do you want an Amendment for that?

noname •
[May 6, 2024 10:10 PM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436409)

Thanks much @JonKnowsNothing! I appreciate your thoughts 🙂

echo •
[May 7, 2024 11:01 AM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436420)

Interoperability, compatability, and open standards are an alternative to the dog eat dog adversarial winner takes all battle which makes this a feminist issue!

If anything I say means a crusty three star or some shouty jobtitle cannot avoid reading a book on feminism I’m going to enjoy every moment of it.

vas pup •
[May 7, 2024 6:42 PM](https://www.schneier.com/blog/archives/2024/05/new-lawsuit-attempting-to-make-adversarial-interoperability-legal.html/#comment-436447)

Senate Hearing on Digital Replicas and Artificial Intelligence Concerns
<https://www.c-span.org/video/?535268-1/senate-hearing-digital-replicas-artificial-intelligence-concerns>

“AI cannot replicate the depth of my life journey, yet those who control it hold the power to mimic the likeness of my art, replicate it, and falsely claim my identity and intellectual property,” said musician and actor Tahliah “FKA twigs” Debrett Barnett during her opening testimony before the Senate Judiciary Subcommittee on Intellectual Property. FKA twigs appeared along with music and movie industry leaders, including Warner Music Group CEO Robert Kyncl, to testify on intellectual property concerns with digital replicas and generative artificial intelligence (AI). Several topics were addressed, including First Amendment prote...