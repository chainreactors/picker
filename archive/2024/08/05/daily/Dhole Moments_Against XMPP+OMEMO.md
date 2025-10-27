---
title: Against XMPP+OMEMO
url: https://soatok.blog/2024/08/04/against-xmppomemo/
source: Dhole Moments
date: 2024-08-05
fetch_date: 2025-10-06T18:00:58.079274
---

# Against XMPP+OMEMO

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

[Cryptography](https://soatok.blog/category/cryptography/) [Open Source](https://soatok.blog/category/technology/open-source/) [Software Security](https://soatok.blog/category/technology/software-security/)

# Against XMPP+OMEMO

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [August 4, 2024](https://soatok.blog/2024/08/04/against-xmppomemo/)
* [19 Comments on Against XMPP+OMEMO](https://soatok.blog/2024/08/04/against-xmppomemo/#comments)

![Against XMPP+OMEMO](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/08/BlogHeader-2024-XMPP-OMEMO.png?fit=1200%2C675&ssl=1)

XMPP is a messaging protocol (among other things) that needs no introduction to any technical audience. Its various implementations have proliferated through technical communities for decades.

Many large tech companies today used to run XMPP servers. However, the basic protocol transmitted plaintext. If you were lucky, it was plaintext over SSL/TLS, but servers could still see all of your message contents.

OMEMO ([XEP-0384](https://xmpp.org/extensions/xep-0384.html)) is an attempt to staple end-to-end encryption onto the XMPP ecosystem.

It’s largely inspired by, and based on, an earlier version of the Signal protocol, so you might be tempted to believing that it’s good.

**In my opinion, it’s not.**

OMEMO is not the worst attempt at making XMPP encrypted (see: [XEP-0027](https://xmpp.org/extensions/xep-0027.html) for that), but it still [doesn’t meet the bar for the kind of private messaging app that Signal is](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/), and is not a viable competitor to Signal.

To understand why this is true, you only need check whether OMEMO is on by default (it isn’t), or whether OMEMO can be turned off even if your client supports it (it can).

Both of these conditions fail the requirements I outlined under the **End-to-End Encryption** header in that other blog post.

And that’s all that I should have needed to say on the matter.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-cooking.png?resize=512%2C470&ssl=1)

Art: [Harubaki](https://harubaki.carrd.co/)

Unfortunately, the Internet is full of cargo cults built around specific technologies, and their followers have an emotional interest in muddying the waters.

Criticize one, and their rivals will come out of the woodwork to say, “This is why I use $FooBar instead of $BazQuux!” and insist that *their* preferred solution is the secure one–with all the confident incorrectness of a climate change denier.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/08/SoatokNerdRage.png?resize=512%2C376&ssl=1)

Art: [AJ](https://sfw.furaffinity.net/user/ajlovesdinos/)

Let me explain why I don’t recommend XMPP and OMEMO for private messaging.

But before I do, a quick reminder that me criticizing XMPP+OMEMO isn’t an endorsement of weird or stupid alternatives, like using PGP.

Also, this post is about the entire XMPP + OMEMO ecosystem, not *just* the OMEMO specification.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/02/Soatok-ScruffKerfluff.png?resize=768%2C614&ssl=1)

Art: [ScruffKerfluff](https://scruffkerfluff.carrd.co/)

## Why People Like XMPP

Quite simply, people like XMPP because it’s federated, which means they can control who gets access to their data. This is also one reason why people like Matrix, Mastodon, NextCloud, etc. It gives them a sense of control over their data that a centralized platform doesn’t. You can feel like you’re controlling your own destiny, whether or not that’s true. And those emotions can be a powerful thing.

[Unlike Moxie](https://signal.org/blog/the-ecosystem-is-moving/), I don’t inherently think federated technology is always bad.

There *are* mechanisms you can employ to roll the entire ecosystem forward and keep everyone up-to-date with security fixes to an underlying protocol. Being frozen in time is a real problem in federation, but not an inevitability.

Unfortunately, XMPP is the perfect exhibit for anyone that wants to argue in favor of Moxie’s perspective on federation.

### OMEMO Problem 1: Protocol Freeze

When I decided to set out to survey the XMPP+OMEMO ecosystem, the first question that came to mind is, “Which implementation is everyone using?”

The answer is probably [Conversations](https://codeberg.org/iNPUTmice/Conversations). Other answers I heard were Gajim and *forks of Conversations*.

We’ll get back to Conversations later, but right now, I want to address a bigger problem with the XMPP+OMEMO ecosystem.

The latest draft of XEP-0384 is version 0.8.3, published in January 2022.

Despite this, almost every OMEMO implementation I can find is still on version 0.3.0 (or earlier) of the OMEMO specification.

![Drakeposting No Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-07.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

The easiest way to tell if they aren’t implementing version 0.4.0 or newer is the absence of AES-256-CBC in their codebase.

See for yourself. All of the following implement version 0.3.0 or older of the OMEMO specification:

* [libomemo](https://github.com/gkdr/libomemo), dependents:
  + [weechat-xmpp](https://github.com/bqv/weechat-xmpp/)
* [Conversations](https://codeberg.org/iNPUTmice/Conversations/src/branch/master/src/main/java/eu/siacs/conversations/crypto/axolotl/XmppAxolotlMessage.java#L38), forks:
  + [blabber.im](https://codeberg.org/kriztan/blabber.im)
  + [Monocles](https://codeberg.org/monocles/monocles_chat)
  + Quicksy
  + [Snikket](https://github.com/snikket-im/snikket-android)
* [Converse.js](https://github.com/conversejs/converse.js/blob/5017efb780973d704f237c478ba52b23d901e1bf/src/plugins/omemo/utils.js#L135-L144)
* [Gajim](https://dev.gajim.org/gajim/gajim-plugins/-/blob/beb90a83a7a07d570c3b809fac45ae739478dd3b/omemo/omemo/aes_gcm.py)
* [jaxmpp](https://github.com/tigase/jaxmpp/blob/8aafe24baa76ac2a5b7db4d130db6f11bc241237/jaxmpp-omemo/src/main/java/tigase/jaxmpp/core/client/xmpp/modules/omemo/OmemoExtension.java#L33), dependents:
  + [Stork IM](https://github.com/tigase/stork/blob/1d892d6cf42dee19eee45e0d7883d4ae8d84fc85/app/src/main/java/org/tigase/messenger/phone/pro/service/XMPPService.java#L88)
* [jabber-web](https://github.com/redsolution/xabber-web/blob/2d903bb049a855d7b42e4b68b535ad504d9120dd/src/utils/utils.js#L486-L487)
* [MartinOMEMO](https://github.com/tigase/MartinOMEMO/blob/master/Sources/MartinOMEMO/OMEMOModule.swift#L94), dependents:
  + [Siskin IM](https://github.com/tigase/siskin-im/blob/d77818f97597e0ea12c4004b91851776ab71e3b1/SiskinIM/database/model/conversations/Chat.swift#L24)

The only implementations I found that supported newer protocol versions were [Profanity](https://github.com/profanity-im/profanity/blob/beeddda5685d401214d08ac65b25df74efaf5c53/src/omemo/crypto.c#L243-L265) and [Kaidan](https://invent.kde.org/network/kaidan) (via [QXmpp](https://github.com/qxmpp-project/qxmpp/blob/94232e798de18099322bee71400f246c9193047a/src/omemo/OmemoCryptoProvider.cpp#L189-L200)).

EDIT: Thanks to [tant](https://nrw.social/%40tant) for pointing me to [this list of versions](https://xmpp.org/extensions/#xep-0384-implementations).

### What To Even Focus On?

A question comes to mind: Which version of the specification should an enterprising security researcher look at?

![Contemplating, Thinking Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/...