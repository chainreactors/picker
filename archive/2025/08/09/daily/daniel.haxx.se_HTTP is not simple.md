---
title: HTTP is not simple
url: https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/
source: daniel.haxx.se
date: 2025-08-09
fetch_date: 2025-10-07T00:47:55.521465
---

# HTTP is not simple

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/06/IETF-Badge-HTTP.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# HTTP is not simple

[August 8, 2025](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [12 Comments](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/#comments)

I often hear or see people claim that *HTTP is a simple protocol*. Primarily of course from people without much experience or familiarity with actual implementations. I think I personally also had thoughts in that style back when I started working with the protocol.

After personally having devoted soon three decades on writing client-side code doing HTTP and having been involved in the IETF on all the HTTP specs produced since 2008 or so, I think I am in a decent position to give a more expanded view on it. *HTTP is not a simple protocol.* Far from it. Even if we presume that people actually mean HTTP/1 when they say that.

HTTP/1 may appear simple because of several reasons: it is readable text, the most simple use case is not overly complicated and existing tools like curl and browsers help making HTTP easy to play with.

The HTTP *idea* and *concept* can perhaps still be considered simple and even somewhat ingenious, but the actual machinery is not.

But yes, you *can* telnet to a HTTP/1 server and enter a GET / command manually and see a response. However I don’t think that is enough to qualify the entire thing as simple.

I don’t believe anyone has tried to claim that HTTP/2 or HTTP/3 are simple. In order to properly implement version two or three, you pretty much have to also implement version one so in that regard they are accumulating complexity and bring quite a lot of extra challenges in their own respective specifications.

Let me elaborate on some aspects of the HTTP/1 protocol that make me say it is not simple.

## newlines

HTTP is not only text-based, it is also *line-based*; the header parts of the protocol that is. A line can be arbitrarily long as there is no limit in the specs – but they need to have a limit in implementations to prevent DoS etc. How long can they be before a server rejects them? Each line ends with a carriage-return and linefeed. But in some circumstances only a linefeed is enough.

Also, headers are not UTF-8, they are octets and you must not assume that you can just arbitrarily pass through anything you like.

## whitespace

Text based protocols easily gets this problem. Between fields there can be one or more whitespace characters. Some of these are mandatory, some are optional. In many cases HTTP also does *tokens* that can either be a sequence of characters without any whitespace, or it can be text within double quotes (“). In some cases they are *always* within quotes.

## end of body

There is not one single way to determine the end of a HTTP/1 download – the “body” as we say in protocol lingo. In fact, there are not even two. There are at least three (Content-Length, chunked encoding and Connection: close). Two of them require that the HTTP client parses content size provided in text format. These many end-of-body options have resulted in countless security related problems involving HTTP/1 over the years.

## parsing numbers

Numbers provided as text are slow to parse and sometimes error-prone. Special care needs to be taken to avoid integer overflows, handle whitespace, +/- prefixes, leading zeroes and more. While easy to read for humans, less ideal for machines.

## folding headers

As if the arbitrary length headers with unclear line endings are not enough, they can also be “folded” – in two ways. First: a proxy can *merge* multiple headers into a single one, comma-separated – except some headers (like cookies) that cannot. Then, a server can send a header as a *continuation* of the previous header by adding leading whitespace. This is rarely used (and discouraged in recent spec versions), but a protocol detail that an implementation needs to care about because it *is* used.

## never-implemented

HTTP/1.1 ambitiously added features that at the time were not used or deployed onto the wide Internet so while the spec describes how for example HTTP Pipelining works, trying to use it in the wild is asking for a series of problems and is nothing but a road to sadness.

Later HTTP versions added features that better fulfilled the criteria that Pipelining failed to: mostly in the way of *multiplexing*.

The 100 response code is in similar territory: specified, but rarely actually used. It complicates life for new implementations. The fact that there is [a discussion](https://lists.w3.org/Archives/Public/ietf-http-wg/2025JulSep/0088.html) *this week* about particulars in the 100 response state handling, twenty-eight years since it was first published in a spec I think tells something.

## so many headers

The HTTP/1 spec details a lot of headers and their functionality, but that is not enough for a normal current HTTP implementation to support. This, because things like cookies, authentication, new response codes and much more that an implementation may want to support today are features outside of the main spec and are described in additional separate documents. Some details, like NTLM, are not even found in RFC documents.

Thus, a modern HTTP/1 client needs to implement and support and a whole range of additional things and headers to work fine across the web. “HTTP/1.1” is mentioned in *at least* 40 separate RFC documents. Some of them quite complex by themselves.

## not all methods are alike

While the syntax should ideally be possible to work exactly the same independently of which *method* that is used (sometimes referred to as *verb*), that is not how the reality works.

For example, if the method is GET we can also indeed send a body in the request similar to how we typically do with POST and PUT, but due to how it was never properly spelled out in the past, that is not interoperable today to the extent that doing it is just recipe for failure in a high enough share of attempts across the web.

This is one of the reasons why there is now work on a new HTTP method called QUERY which is basically what GET + request body should have been. But that does not simplify the protocol.

## not all headers are alike

Because of the organic way several headers were created, deployed and evolved, a proxy for example cannot blindly just combine two headers into one, as the generic rules say it could. Because there are headers that specifically don’t follow there rules and need to be treated differently. Like for example cookies.

## spineless browsers

Remember how browser implementations of protocols always tend to prefer to show the user something and *guess* the intention rather than showing an error because if they would be stringent and strict they risk that users would switch to another browsers that is not.

This impacts how the rest of the world gets to deal with HTTP, as users then come to expect that what works with the browsers should surely also work with non-browsers and their HTTP implementations.

This makes interpreting and understanding the spec secondary compared to just following what the major browsers have decided to do in particular circumstances. They may even change their stances over time and they may at times contradict explicit guidance in the specs.

## size of the specs

The first HTTP/1.1 RFC 2068 from January 1997 was 52,165 words in its plain text version – which almost tripled the size from the HTTP/1.0 document R...