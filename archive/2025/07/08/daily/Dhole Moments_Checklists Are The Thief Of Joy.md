---
title: Checklists Are The Thief Of Joy
url: https://soatok.blog/2025/07/07/checklists-are-the-thief-of-joy/
source: Dhole Moments
date: 2025-07-08
fetch_date: 2025-10-06T23:26:57.467180
---

# Checklists Are The Thief Of Joy

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Bullshit](https://soatok.blog/category/bullshit/) [Security Community](https://soatok.blog/category/technology/software-security/security-community/) [Security Industry](https://soatok.blog/category/technology/software-security/security-industry/)

# Checklists Are The Thief Of Joy

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [July 7, 2025](https://soatok.blog/2025/07/07/checklists-are-the-thief-of-joy/)

![Checklists Are The Thief Of Joy](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/07/BlogHeader-2025-Checklists.png?fit=1200%2C675&ssl=1)

I have never seen security and privacy comparison tables (henceforth referred to simply as “checklists” for brevity) used for any other purpose but deception.

![The words "Stop this bullshit!" in purple text juxtaposed over an example of a comparison checklist (this one's about password managers).](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/07/checklist-bullshit.png?resize=720%2C107&ssl=1)

After pondering this observation, I’m left seriously doubting if these checklists have any valid use case except to manipulate the unsuspecting.

> Please keep in mind that I’m talking about [something very specific](https://web.archive.org/web/20250418202609/https%3A//docs.google.com/spreadsheets/d/1b2zEEU8_YPsgo3nY1BJ72qgLXteP7Yt0_mnlYJ8m0RI/edit) ([alternative archive](https://archive.ph/33EG5)) that shows up in security tool evangelism rather than the vague concept of a list with checkboxes.
>
> There are entire industries that use checklists as a safety tool. I’m not talking about that.
>
> This also isn’t a post about “security compliance” or initiatives like the OWASP Top 10.
>
> If you see someone on social media kneejerk react as if that’s what I was saying, point them to this excerpt and ask them to read the whole damn thing, not just the title.

But before we get into that, I’d like to share *why* we’re talking about this today.

Recently, another person beat me to the punch of implementing MLS (RFC 9420) in TypeScript. When I shared a link to their release announcement, one Fediverse user [replied](https://mastodon.uno/%40miniBill/114797932927924398), “How does this compare to Signal’s protocol?”

Great! A fair question from a curious mind. Love to see it.

![Grin Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/03/soatoktelegramswave3-01.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

But when I started drafting a response, I realized that any attempt to write any sort of structured comparison would be misleading. They’re different protocols with different security goals, and there’s no way to encapsulate this nuance in a grid of green, yellow, and red squares to indicate trustworthiness.

But that doesn’t stop bullshit [like this](https://web.archive.org/web/20250707152409/https%3A//www.securemessagingapps.com/) ([alternate archive](https://archive.is/SlynX)) from existing.

![Confused protogen](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-confused.png?resize=409%2C512&ssl=1)

[Harubaki](https://harubaki.carrd.co/)

This is a wonderful case study in how to deceive someone with facts.

When you first load the page, the first thing you’re shown is some “summary” fields, including a general “Is this app recommended?” field with “Yes”/”No”. This short-circuits the decision-making for people too lazy or clueless to read on.

And then immediately after that, the **very first thing** you’re given is jurisdiction information.

![An excerpt from the website linked above, where they emphasize "jurisdiction" before any cryptography details.](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/07/image.png?resize=768%2C236&ssl=1)

This is a website that bills itself as a comparison for “secure messaging apps”.

Users shouldn’t *have to* care about jurisdiction if the servers cannot ever read their messages in the first place. Any app that fails to meet this requirement should wholesale be disqualified.

The most important questions that actually matter to security:

1. Is end-to-end encryption turned on by default?
2. Can you (accidentally, maliciously) turn it off?

If the answers aren’t “yes” and “no”, respectively, your app belongs in the garbage. Do not pass Go.

But this checklist wasn’t written by a cryptography expert. If it were, there would be more information about the protocols used than a collection of primitives used under-the-hood with arbitrary coloring.

![The "cryptographic primitives" row from the checklist website.](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/07/image-1.png?resize=768%2C113&ssl=1)

Why does “X25519 / XSalsa20 256 / Poly1305” get a green box but “Curve25519 256 / XSalsa20 256 / Poly1305-AES 128” get a yellow box? Actually, why does it refer to the same algorithm as X25519 and Curve25519 in different cells? Hell if I know. I’d wager the author doesn’t, either.

Now, I don’t want to belabor the point and pick on this checklist in particular. It’s not that this specific checklist is the problem. It’s that all checklists are.

The entire idea of using checklists to compare apps like this is fundamentally flawed. It’s like trying to mentally picture an 1729-dimensional object on a 2-dimensional screen.

Not only will you inevitably be wrong, but your audience will think you’re somehow being objective while you do it.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/08/soatok-sus.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

## How Do You Compare Signal to MLS?

Since I brought it up above, I might as well talk about this here.

The Signal Protocol was designed to provide state-of-the-art encryption for text messages between mobile phone users. It has since slowly expanded its scope to include desktop users and people that don’t want to give their phone numbers to strangers. Signal does a lot of cool stuff, and I’ve spent a weekend [reviewing how its cryptography is implemented](https://soatok.blog/2025/02/18/reviewing-the-cryptography-used-by-signal/). Signal didn’t give a hoot about interop, and probably won’t for the foreseeable future, either.

The MLS protocol is an IETF RFC intended to standardize a reasonable protocol for encrypted messaging apps. It was meant to eventually be interoperable across apps/devices.

Signal uses [a deniable handshake protocol](https://signal.org/docs/specifications/x3dh/#deniability). MLS [does not](https://www.rfc-editor.org/rfc/rfc9420.html#name-authentication).

Signal tries to hide the social graph from the delivery service. MLS does not.

Signal’s approach to group messaging is an abstraction over 1:1 messaging, with zero-knowledge proofs to hide group memberships from the Signal server. Because this is an abstraction, it’s trivial to send a different message to each member of a group, and consistent histories are not guaranteed.

MLS proposes an efficient scheme for continuously agreeing on a group secret key. This kind of setup makes [invisible salamanders style attacks](https://soatok.blog/2024/09/10/invisible-salamanders-are-not-what-you-think/) on a group conversation untenable.

There are a lot of additional things that libsignal offers out-of-the-box, that you won’t get with MLS. Soon, key transparency may be on the list of things Signal offers but MLS doesn’t.

Ultimately, both protocols are good. They’re certainly way better choices than OpenPGP, OMEMO, Olm, MTProto, etc.

When I began drafting ideas for e...