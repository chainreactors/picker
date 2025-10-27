---
title: The Security Vulnerabilities of Message Interoperability
url: https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html
source: Schneier on Security
date: 2023-03-30
fetch_date: 2025-10-04T11:10:02.565863
---

# The Security Vulnerabilities of Message Interoperability

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

## The Security Vulnerabilities of Message Interoperability

Jenny Blessing and Ross Anderson have [evaluated](https://www.lightbluetouchpaper.org/2023/03/24/interop-one-protocol-to-rule-them-all/) the security of systems designed to allow the various Internet messaging platforms to interoperate with each other:

> The Digital Markets Act ruled that users on different platforms should be able to exchange messages with each other. This opens up a real Pandora’s box. How will the networks manage keys, authenticate users, and moderate content? How much metadata will have to be shared, and how?
>
> In our latest paper, [One Protocol to Rule Them All? On Securing Interoperable Messaging](https://arxiv.org/abs/2303.14178), we explore the security tensions, the conflicts of interest, the usability traps, and the likely consequences for individual and institutional behaviour.
>
> Interoperability will vastly increase the attack surface at every level in the stack ­ from the cryptography up through usability to commercial incentives and the opportunities for government interference.

It’s a good idea in theory, but will likely result in the overall security being the worst of each platform’s security.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [authentication](https://www.schneier.com/tag/authentication/), [economics of security](https://www.schneier.com/tag/economics-of-security/), [privacy](https://www.schneier.com/tag/privacy/), [psychology of security](https://www.schneier.com/tag/psychology-of-security/)

[Posted on March 29, 2023 at 7:03 AM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html) •
[30 Comments](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html#comments)

### Comments

Andy •
[March 29, 2023 10:07 AM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html/#comment-419975)

A weakened security is what the governments want anyway, don’t they? And now they’ll credit themselves for helping the consumer

Clive Robinson •
[March 29, 2023 11:35 AM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html/#comment-419976)

@ Bruce, ALL,

Re : Is a message defined by content?

As Prof Ross Anderson notes,

> *“The Digital Markets Act ruled that users on different platforms should be able to exchange messages with each other.”*

That is ambiguous because a “message” is not defined.

A message at it’s lowest level just a communication, that is it does not have to have any content in it.

Such messages are seen in “keep alives” and “anti-brownout” systems, the actual transfer of the communication is the message, not anything the message might contain.

At the next level up a message can be saod to consist of a “Bag of Bits”(BoB) with or without any meya data that might make it understandable in some way. In this respect it is now like a file contents, but without any file meta-information.

And so on up, each layer defined by a new standard and meta-data and meta-meta-data.

When you think about it eqch layer can be viewed as a Shannon Channel, and as such can be within another Shannon Channel and contain further Shannon Channels. So in effect just like a Russian Matryoshka doll.

Leaving the question,

“Which doll is the doll? And how do you decide?”.

In short the law, it’s self to work in one way has to fail in a different way.

This is a problem that arises when you treat “information objects” as though they are “physical objects” they are not the same, not even close.

So any system that can connect to another system both passes and fails the same legal test… And whilst it can always be said “It will fail” the test, you can never with any ceryainty say “It will pass the test” because that is a logical imposibility…

Not that this appears to concern the legislators or legal bretherin. The Legislators claim they have acted, and the legal bretherin just see endless billable hours to argue…

Clive Robinson •
[March 29, 2023 11:59 AM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html/#comment-419977)

@ ALL,

Re : EU DMA Perspective,

For those who need to considet the EU DMA in a different way, “The Conversation” gave a perspective view,

<https://theconversation.com/can-the-eus-digital-markets-act-rein-in-big-tech-192373>

Importantly note the failure of current “take over” legislation brought in back in the “Bricks and Mortar Business Days”.

Likewise how online businesses in particular could simply re-form themselves around the legislation to negate it’s effectiveness.

Oh and it also has some quite useful links on the subject…

Winter •
[March 29, 2023 12:01 PM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html/#comment-419978)

@Clive

> That is ambiguous because a “message” is not defined.

I think judges will have absolutely no problem in deciding this: If A sends a message (text/speech/picture) to B, then be must receive the text/speech/picture in a legible form. Period.

iAPX •
[March 29, 2023 12:09 PM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html/#comment-419979)

@Winter

I could not wait to see that in action, with the receiver using a dumb phone and thus limited to SMS…

RealFakeNews •
[March 29, 2023 12:42 PM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html/#comment-419980)

Making them interoperable is easy. The catch is where is the plaintext handled?

This is just another way to break message security.

As always, seperate the security from the transmission system.

Renee W •
[March 29, 2023 12:57 PM](https://www.schneier.com/blog/archives/2023/03/the-security-vulnerabilities-of-message-interoperability.html/#comment-419981)

@ Clive Robinson,

> That is ambiguous because a “message” is not defined.

I find the use of the word “should” a bigger problem. Laws are generally written as “shall” and “shall not”, not “should” (which almost contradicts the idea of a “rule”). It seems to just be a bad summary, though. The terms “mandate” and “requires” are used at the end of page 1, with the caveat that only “the largest” platforms are affected.

[Here’s the actual regulation.](https://eur-lex.europa.eu/eli/reg/2022/1925) “The gatekeeper shall make at least the following basic functionalities referred to in paragraph 1 interoperable where the gatekeeper itself provides those functionalities to its own end users: … end-to-end text messaging … sharing of images, voice messages, videos and other attached files”. “[W]ithin 2 years…: end-to-end text messaging within groups … sharing of images, voice me...