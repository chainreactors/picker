---
title: Deviating from specs
url: https://daniel.haxx.se/blog/2022/10/18/deviating-from-specs/
source: daniel.haxx.se
date: 2022-10-19
fetch_date: 2025-10-03T20:15:44.994483
---

# Deviating from specs

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/book-1659717_1280.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Deviating from specs

[October 18, 2022](https://daniel.haxx.se/blog/2022/10/18/deviating-from-specs/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2022/10/18/deviating-from-specs/#comments)

*tldr: we do not particular keep track nor document curl’s exact spec compliance. I cannot fathom how we could.*

Today, in October 2022, curl and libcurl combined consist of nearly 150,000 lines of source code (not counting blank lines). 19% of those are comments.

This source code pile was carefully crafted with the sole purpose of performing Internet transfers using one or more of the 28 separate supported protocols. (There are 28 different supported URL schemes, it can be discussed if they are also 28 protocols or not.)

## Which specs does curl use

It was recently proposed to me that we should document which RFCs curl adheres to and follows, and what deviants there are. In the name of helping the users understand what to expect from curl and educating the world how curl will behave.

This is indeed a noble idea and a worthy goal. We do not want to surprise users. We want them to know.

It was suggested that it might have a security impact if curl would deviate from a spec and if this is not documented clearly, users could be mislead.

## What specs

curl speaks TCP/IP (and UDP or QUIC at times), it does DNS and DNS-over-HTTPS, it speaks over proxies and it speaks a range of various application protocols to perform what asked of it. There are literally hundreds of RFCs to read to catch up on all the details.

A while ago I collected the what I consider most important RFCs to read to figure out how curl works and why. That is right now 149 specification documents at a total of over 300,000 lines of text. (It was not done very scientifically.)

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/10/important-rfcs-curl.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/10/important-rfcs-curl.jpg)

Counting the words in these 149 documents, they add up to a total of many more words than the entire Harry Potter series, and the Lord of the Rings series (including *the Hobbit*) is far behind together with War and Peace: *1.6 megawords*.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2022/10/rfc-words-curl.jpg)](https://daniel.haxx.se/blog/wp-content/uploads/2022/10/rfc-words-curl.jpg)

Luckily, specs are mostly reference literature and we rarely have to read through them all to start our journey, but we often need to go back to check details.

## Everything changes over time

The origins of curl trace back to late 1996 and it has been in constant development since then. curl, the Internet and the specifications have all changed significantly over these years.

The specifications that were around when we started have generally been updated multiple times, while we struggle to maintain behavior and functionality for our users. It is hard to spot and react to minor changes in specification updates. They might have been done to clarify a situation, but sometimes such a clarification ends up triggering a functionality change in our code.

Sometimes an update to a spec is even largely ignored by fellow protocol implementers out there in the world, and for the sake of interoperability we too then need to adjust our interpretations so that we work similarly to our peers.

Expectations from users change as values and terms are established in people’s minds rather than in specs. For example: what exactly is the “URL” you see in the browser’s top bar?

Over time, other tools and programs that also work on URLs and on the Internet, gradually change as they too development and slowly morph into the new beings we did not foresee decades ago. This change perceptions and expectations in the user base at large.

The always changing nature of the Internet creates interoperability challenges ever so often: out of the blue a team of protocol implementers can decide to interpret an existing term or a passage in a specification differently one day. When the whole world takes a turn like that, we are sometimes *forced* to follow along as that is then the new world view.

Another complication is also that curl uses (several) third party libraries for parts of its operations, and some of those details are of course also covered by RFCs.

## Guidelines

Our primary guidelines when performing Internet transfers are:

1. Follow established standard protocol specifications
2. Security is a first-tier property
3. Interop widely
4. Maintain behavior for existing features

As you can figure out for yourself, these four bullet points often collide with each other. Checking off all four is not always possible. They can be hard enough on their own.

### Protocol specifications

There are conflicting specifications. Specifications vary over time. They can be hard to interpret to figure out exactly what they say one should do.

### Security

Increasing security might at the same time break existing use cases for existing users. It might violate what the specs say. It might add friction in the ability to interoperate with others. It might not even be allowed according to specifications.

### Interop

This often mean to *not* follow specifications they way we want to read them, because apparently others do not read them the same way or sometimes they just disregard what the specs say. At times, it is hard to increase security levels by default because it would hamper interop with others.

### Maintain behavior

The scripts written 15 years ago that use curl should continue working. The applications written to use libcurl can upgrade libcurl and its Internet transfers just continue. We do not break existing established behaviors. This may very well conflict both with interop and protocol updates, and sometimes it is hard to tighten the security because it would hurt a certain share of existing users.

## How does curl deviate from which specs?

I consider this question more or less impossible to answer to, to document and to keep accurate over time. At least it would be a huge and energy-consuming effort both to get the list done but it would also be a monster task to maintain. And it would involve a lot of gray zones.

What is important to me is not what RFCs curl follows nor what or how it deviates from them. I have also basically never gotten that question from a user.

Users want reliable Internet transfers that are secure and interoperate correctly and conveniently with other “players” out there. They want consistent behavior and backwards compatibility.

If you use curl to perform feature X over protocol Y version Z, does it matter which set of RFCs that this would touch and does anyone care about the struggles we have been through when we implemented this set? How many users can even grasp or follow the implication of mentioning that for RFC XYX section A.B we decided to disregard a SHOULD NOT at times?

And how on earth would we keep that up-to-date when we do bugfixes and RFCs are updated down the line?

## No one else documents this

The browsers have several hundreds of paid engineers on staff involved and they do not provide documentation like this. Neither does any curl alternative or competitor to my knowledge.

I don’t know of any tool or software anywhere that offer such a *deviance documentation* and I can perfectly understand and sympathize with why that is so.

[cURL and libcurl]...