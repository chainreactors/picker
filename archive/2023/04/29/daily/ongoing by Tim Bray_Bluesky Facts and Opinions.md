---
title: Bluesky Facts and Opinions
url: https://www.tbray.org/ongoing/When/202x/2023/04/28/Bluesky
source: ongoing by Tim Bray
date: 2023-04-29
fetch_date: 2025-10-04T11:31:43.757829
---

# Bluesky Facts and Opinions

# Bluesky Facts and Opinions

Search

The Fediverse has exploded in discussion of Bluesky, now that it’s launched a beta and harvested a few celebrities.
Quite a lot of Fediverse voices have been angry and hostile, pointing out that several years of intense effort have produced a working
ActivityPub-based federated monopoly-resistant conversational social network, and asking who are these dweebs
ignoring that work and
re-inventing the wheel, probably in an attempt to enrich Jack Dorsey?!

I have a lot of sympathy with those opinions. Having said that, the assertions are not all
fact-based. So, here are facts (and a few opinions) about Bluesky, as of late April 2023.

*[If you disagree with any of my “Facts”, please send evidence and I’ll correct.]*

**Fact:** Bluesky is run by its CEO, Jay Graber.

[![Jay Graber’s LinkedIn page](JayGraber.png "Jay Graber’s LinkedIn page")](-big/JayGraber.jpg.html)

**Opinion:** Jay is a decent and smart person.

**Fact:** Bluesky is a
[Delaware Public
Benefit Limited Liability Company](https://www.cogencyglobal.com/blog/public-benefit-limited-liability-company-new-entity-on-the-block).

**Opinion:** It’s not 100% clear what that means but you should research a bit before having opinions on the subject.

**Fact:** Bluesky is owned by its team and has three directors: Jay Graber,
[Jeremie Miller](https://en.wikipedia.org/wiki/Jeremie_Miller) (the XMPP guy), and Jack Dorsey. Thanks to Ryan for
the
[research](https://snarfed.org/bluesky-corporate-ownership-and-structure).

**Fact:** Bluesky may be looked up at the Delaware
[Division of Corporations](https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx) by searching for
“bluesky pbllc” — If you have a state-of-Delaware registry account and $20 you can find out more, but
I don’t have such an account. If you do, please let me know what you find out.

**Opinion:** My impression, from what’s on the record and having been in the Bluesky conversation until mid-2022, is that
it’s really wrong to say that Jack runs or controls Bluesky, or is even involved that much.

**Fact**: Bluesky
[is open-source](https://github.com/bluesky-social/atproto-ecosystem).
*[Update: Well, mostly. There’s lots there if you go looking. Pieces are missing, but Bluesky is promising to fix that.]*

**Fact:** Bluesky’s goals are
[said to include](https://atproto.com):

1. [Selectable algorithms](https://blueskyweb.xyz/blog/4-13-2023-moderation) (including moderation), not necessarily
   per-instance.
2. Digital identity based on the
   [Decentralized Identifiers (DID)](https://www.w3.org/TR/did-core/) spec, not tied to the instance you’re using.
3. Multi-instance federation.

**Opinion:** The DID standard is immensely complex and feels sort of ramshackle and not nearly prescriptive enough.
I distrust some of the people who worked on it. But there are smart people who like it.

**Fact:** Things that Bluesky has not yet implemented:

1. Blocking. *[Update: Fixed 2023/04/28].*
2. Federation.
3. Selectable algorithms.

**Fact:** Bluesky
[received $13M in funding](https://twitter.com/bluesky/status/1518707604750430208?lang=en) sometime in 2022.

**Opinion:** That is not nearly enough to build an Internet-scale social media service.

**Opinion:** Bluesky might become VC-investable if they can exhibit insanely-fast MAU growth and the ability to attract
*and retain* celebrities.

**Opinion:** If they did get VC investment they’d be dead to me (and probably pretty soon just dead).

**Fact:** When Bluesky was announced, Jack Dorsey said that Twitter would be a client for the protocol.

**Opinion:** This was the biggest reason why Bluesky was interesting.

**Opinion:** Jack don’t work there any more and I wouldn’t bet on Elon… well, I was going to say “following through” but
then I can’t think of anything I *would* bet on Elon for, so let’s leave it there.

Question: Is Bluesky interesting? ·
**Opinion:** Not very, until they actually have Federation and selectable-algorithms in
place and shown to work at scale, and be useful. And that, as an organization, they can be worked with.

---

**Updated: 2023/04/29**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: David Chase (Apr 28 2023, at 11:53)

proscriptive or prescriptive? I can see go reasons for either word: these are things you must-not/must do.

*[[link](#c1682707995.230181)]*

From: [Staci Kramer](http://) (Apr 28 2023, at 12:00)

Thanks for breaking this down, Tim.

Opinion: another definition of “interesting” moves beyond the structure and technology. Do you want to be there? Is there a critical mass of people, ideas, energy? Can you use it and contribute without knowing how it works?

*[[link](#c1682708442.416423)]*

From: [Ryan](https://snarfed.org) (Apr 28 2023, at 14:16)

Thanks for putting this together, Tim! I've been collecting a similar list at <https://snarfed.org/bluesky-corporate-ownership-and-structure> . A few minor corrections and additions, all from posts from Jay, Bluesky, and Jack on Twitter and Bluesky:

The board is only Jay, Jack, and Jeremie, no one else. They each have 1/3 voting power.

The $13M funding from Twitter/Jack was more like a grant than investment; they took no equity stake in exchange for it. Bluesky is currently employee owned.

The web and mobile apps aren't open source yet, but the server(s) and other code are, eg <https://github.com/bluesky-social/atproto> , <https://github.com/bluesky-social/did-method-plc>

The biggest goal and protocol difference vs ActivityPub is true account portability, even if your current server goes offline or malicious. Jay has said this was the primary goal that made them not just use AP. (I'll try to find this post to cite.) Notably, when you migrate your account, your identity stays the same, unlike AP where it changes from user@domain1 to user@domain2. (Mastodon does add a non-standard human-readable "redirect" and tries to propagate followers, granted, and you can export and re-import your posts, but those are all awkward band-aids at best.)

*[[link](#c1682716610.153758)]*

From: [Ryan](https://snarfed.org) (Apr 28 2023, at 14:31)

More on account portability: <https://atproto.com/guides/overview#account-portability> . I'm with you that DIDs are ugly and sprawling and sketchy, but AT Proto's account portability only lightly depends on them. More of the key functionality is outside DIDs than inside. Also, they're carefully explicit about the small subset of types they support, right now just did:web and did:plc.

*[[link](#c1682717511.723504)]*

From: [Lars Marius Garshol](https://www.garshol.priv.no) (Apr 28 2023, at 14:52)

I don't understand: why is Bluesky of interest to anyone? The great thing about Mastodon is that it's not vulnerable to a muskopalypse (rich idiot buying the platform and destroying it). If a single company takes over, no matter how well-intentioned the founders are, suddenly the entire social medium is vulnerable to the same thing again.

And, in any case, where is the gain?

Not saying you're wrong about anything you posted, I'm just baffled why I should care.

*[[link](#c1682718723.252457)]*

From: [Buck](https://chromatin.ca) (May 01 2023, at 07:08)

It’s of interest to a lot of people because some who have been having a miserable time with Twitter have found Bluesky to be a comparatively safe place. There’s been an influx from Black Twitter, for instance, and a lot of transfeminine people, who have commented on the feeling of relief. Relevant commentary: [https://mastodon.social/@mekkaokereke@hachyderm.io/110273797250438520](https://mastodon.social/%40mekkaokereke%40hachyderm.io/110273797250438520)

*[[link](#c1682950089.348443)]*

[ongoing](https://www.tbray.org/ongoing/)

[What this is](/ongoing/WhatItIs) ·
[![Subscribe to ongoing](/ongoing/Feed.png "Subscribe to ongoing")](/ongoing/ongoing.atom)
[Truth](/ongoing/Truth) ·
[Biz](/ongoing/Biz) ·
[Tech](/ongoing/Tech)

[author](/...