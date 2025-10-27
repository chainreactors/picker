---
title: My cookie spec problem
url: https://daniel.haxx.se/blog/2025/03/01/my-cookie-spec-problem/
source: daniel.haxx.se
date: 2025-03-02
fetch_date: 2025-10-06T21:57:07.391202
---

# My cookie spec problem

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/03/cookie.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# My cookie spec problem

[March 1, 2025](https://daniel.haxx.se/blog/2025/03/01/my-cookie-spec-problem/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [4 Comments](https://daniel.haxx.se/blog/2025/03/01/my-cookie-spec-problem/#comments)

Before [RFC 6265](https://daniel.haxx.se/blog/2011/04/28/the-cookie-rfc-6265/) was published in 2011, the world of cookies was a combination of anarchy and guesswork because the only “spec” there was was not actually a spec but just [a brief text](https://curl.se/rfc/cookie_spec.html) lacking a lot of details.

RFC 6265 brought order to a world of chaos. It was good. It made things a lot better. With this spec, it was suddenly much easier to write compliant and interoperable cookie implementations.

I think these are plain facts. I have written cookie code since 1998 and I thus know this from my own personal experience. Since I believe in open protocols and doing things right, I participated in the making of that first cookie spec. As a non-browser implementer I think I bring a slightly different perspective and different angle to what many of the other involved people have.

## Consensus

The cookie spec was published by the IETF and it was created and written in a typical IETF process. Lots of the statements and paragraphs were discussed and even debated. Since there were many people and many opinions involved, of course not everything I think should have been included and stated in the spec ended up the way *I* wanted them to, but in a way that the consensus seemed to favor. That is just natural and the way of the process. Everyone involved accept this.

## I have admitted defeat, twice

The primary detail in the spec, or should I say one of the important style decisions, is one that I disagree with. A detail that I have tried to bring up again when the cookie spec was up for a revision and a new draft was made (still known as 6265bis since it has not become an official RFC yet). A detail that I have failed the get others to agree with me about to an enough degree to have it altered. I have failed twice. The update will ship with this *feature* as well.

## Cookie basics

Cookies are part of (all versions of ) HTTP but are documented and specified in a separate spec. It is a classic client-server setup where `Set-Cookie:` response headers are sent from a server to a client, the client stores the received cookies and sends them back to servers according to a set of rules and matching criteria using the `Cookie:` request header.

## Set-Cookie

This is the key header involved here. So how does it work? What is the syntax for this header we need to learn so that we all can figure out how servers and clients should be implemented to do cookies interoperable?

As with most client-server protocols, one side generates this header, the other side consumes it. They need to agree on how this header works.

## My problem is two

The problem is that this header’s syntax is defined twice in the spec. *Differently*.

[Section 4.1](https://datatracker.ietf.org/doc/html/rfc6265#section-4.1) describes the header from server perspective while [section 5.2](https://datatracker.ietf.org/doc/html/rfc6265#section-5.2) does it from a client perspective.

If you like me have implemented HTTP for almost thirty years you are used to reading protocol specifications and in particular HTTP related specification. HTTP has numerous headers described and documented. No other HTTP documents describe the syntax for header fields differently in separate places. Why would they? They are just single headers.

This double-syntax approach comes as a surprise to many readers, and I have many times discussed cookie syntax with people who have read the 6265 document but only stumbled over and read one of the places and then walked away with only a partial understanding of the syntax. I don’t blame them.

The spec insists that servers *should* send a rather conservative Set-Cookie header but knowing what the world looks like, it simultaneously recommends the client side for the same header to be much more liberal because servers might not be as conservative as this spec tells the server to be. Two different syntax.

The spec tries to be prescriptive for servers: *thou shall do it like this*, but we all know that cookies were wilder than this at the time 6265 was published and because we know servers won’t stick to these “new” rules, a client can’t trust that servers are that nice but instead need to accept a broader set of data. So clients are told to accept much more. A different syntax.

## Servers do what works

As the spec tells clients to accept a certain syntax and widely deployed clients and cookie engines gladly accept this syntax, there is no incitement or motive for servers to change. The *do this if you are a good server* instruction serves as an ideal, but there is no particularly good way to push anyone in that direction because it works perfectly well to use the extended syntax that the spec says that the clients need to accept.

## A spec explaining what is used

What I want? I want the Set-Cookie header to be described in a single place in the spec with a single unified syntax. The syntax that is used and that is interoperable on the web today.

It would probably even make the spec shorter, it would remove confusion and it would certainly remove the risk that people think just one of the places is the canonical syntax.

Will I bring this up again when the cookie spec is due for refresh again soon? Yes I will. Because I think it would make it a much better spec.

Do I accept defeat and accept that I am on the losing side in an argument when nobody else seems to agree with me? Yes to that as well. Just because I think like this does in no way mean that this is objectively *right* or that this is the way to go in a future cookie spec.

[cookies](https://daniel.haxx.se/blog/tag/cookies/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostAdding curl release candidates](https://daniel.haxx.se/blog/2025/02/28/adding-curl-release-candidates/)[Next Post19000 curl commits](https://daniel.haxx.se/blog/2025/03/14/19000-curl-commits/)

## 4 thoughts on “My cookie spec problem”

1. ![](https://secure.gravatar.com/avatar/e3728bb535d8309361a2e541df14e3383d9e946cf97417a14e0ae3bbed09daf0?s=34&d=monsterid&r=g) **Willy** says:

   [March 1, 2025 at 19:29](https://daniel.haxx.se/blog/2025/03/01/my-cookie-spec-problem/#comment-27138)

   You’re not alone Daniel. I don’t like this double definition either and I already hated it in 6265. I also don’t like that a protocol document provides an algorithm explaining how I have to implement it because it does not necessarily match what I can do in my implementation. For me it has to describe the general syntax (the large one), indicate what servers SHOULD NOT do even if we know that currently some do, and indicate what clients MAY do to have dissuade servers from sending bad stuff and encourage them to be fixed. By narrowing the SHOULD NOT and MAY over time we could have got rid of a lot of this mess, and maybe by now quotes would have been ubiquitous to protect the date so that we could finally have merged multiple set-cookie headers!

   I too guess we’ll have yet another spec in 10-15 years aiming at fixing the exact same problems again…
2. ![](https://secure.gravatar.com/avatar/6d446c3138833e2143a1e5bf2f8ccdc7e13c82b4b71af2f8ad...