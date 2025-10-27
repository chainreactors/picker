---
title: On Ashton Kutcher and Secure Multi-Party Computation
url: https://buaq.net/go-162946.html
source: unSafe.sh - 不安全
date: 2023-05-12
fetch_date: 2025-10-04T11:38:12.290527
---

# On Ashton Kutcher and Secure Multi-Party Computation

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/29d841944487f4c06b2dae3c9753470c.jpg)

On Ashton Kutcher and Secure Multi-Party Computation

Back in March I was fortunate to spend several days visiting Brussels, where I had a chance
*2023-5-11 23:3:56
Author: [blog.cryptographyengineering.com(查看原文)](/jump-162946.htm)
阅读量:18
收藏*

---

Back in March I was fortunate to spend several days visiting Brussels, where I had a chance to attend a panel on “[chat control](https://www.patrick-breyer.de/en/posts/chat-control/)“: the new content scanning regime being considered by the EU Commission. Among various requirements, this proposed legislation would mandate that *client-side scanning* technology be incorporated into encrypted text messaging applications like Signal, WhatsApp and Apple’s iMessage. The scanning tech would examine private messages for certain types of illicit content, including child sexual abuse media (known as CSAM), along with a broad category oftextual conversations that constitute “grooming behavior.”

I have many thoughts about the safety of the EU proposal, and you can read [some of them here.](https://blog.cryptographyengineering.com/2023/03/23/remarks-on-chat-control/) (Or you’re interested in the policy itself, you can read this [recent opinion](https://t.co/aYbfLqnKBo) by the EU’s Council’s Legal Service.) But although the EU proposal is the *inspiration* for today’s post, it’s not precisely what I want to talk about. Instead, I’d like to clear up some confusion I’ve noticed around *the specific technologies* that many have proposed to use for building these systems.

Also: I want to talk about Ashton Kutcher.

[![](https://blog.cryptographyengineering.com/wp-content/uploads/2023/04/image.png?w=1024)](https://blog.cryptographyengineering.com/wp-content/uploads/2023/04/image.png)

*Ashton Kutcher visits the EU parliament in March 2023 (photo: [Roberta Metsola](https://www.brusselstimes.com/417985/ashton-kutcher-spotted-in-the-european-parliament-promoting-childrens-rights).)*

It turns out there were a few people visiting Brussels to talk about encryption this March. Only a few days before my own visit, Ashton Kutcher gave a major speech to EU Parliament members in support of the Commission’s content scanning proposal. (And yes, I’m talking about that Ashton Kutcher, the guy who played Steve Jobs and is married to Mila Kunis.)

Kutcher has been very active in the technical debate around client-side scanning. He’s the co-founder of an organization called [Thorn](https://www.thorn.org/about-our-fight-against-sexual-exploitation-of-children/), which aims to develop cryptographic technology to enable content scanning. In March he gave an [impassioned speech](https://www.youtube.com/watch?v=aydwlbTh3NE) to the EU Parliament urging the deployment of these technologies, and remarkably he didn’t just talk about the policy side of things. When asked how to balance user privacy against the needs of scanning, he even made a concrete technical proposal: to use *[fully-homomorphic encryption](https://blog.cryptographyengineering.com/2012/01/02/very-casual-introduction-to-fully/)* (FHE) as a means to evaluate encrypted messages*.*

Now let me take a breath here before my head explodes.

I promise I am not one of those researchers who believes only subject-matter experts should talk about cryptography. Really I’m not!I write this blog because *I think cryptography is amazing* and I want everyone talking about it all the time. Seeing mainstream celebrities toss around phrases like “homomorphic encryption” isliterally a dream come true and I wish it happened every single day.

And yet, there are downsides to this much winning.

I ran face-first into some of those downsides when I spoke to policy experts about Kutcher’s proposal. Terms like *fully* *homomorphic encryption* can be confusing and off-putting to non-cryptographers. When filtered through people who are not themselves experts in the technology, these ideas can produce the impression that cryptography is magical pixie dust we can sprinkle on all the hard problems in the world. *And oh how I wish that were true.* But in the real world, cryptography is full of tradeoffs. Solving one problem often just makes new problems, or creates major new costs, or else shifts the risks and costs to other parts of the system.

So when people on various sides of the debate asked me whether “fully-homomorphic encryption” could really do what Kutcher said it would, I couldn’t give an easy five-word answer. The real answer is something like: *(scream emoji)* *it’s very complicated*. That’s a very unsatisfying thing to have to tell people. Out here in the real world the technical reality is eye-glazing and full of dragons.

Which brings me to this post.

What Kutcher is really proposing is that we to develop systems that perform *privacy-preserving computation* on encrypted data. He wants to use these systems to enable “private” scanning of your text messages and media attachments, with the promise that these systems will only detect the “bad” content while keeping your legitimate private data safe. This is a complicated and fraught area of computer science. In what goes below, I am going to discuss at a *high* *and relatively non-technical level* the concepts behind it: what we can do, what we can’t do, and how practical it all is.

In the process I’ll discuss the two most powerful techniques that we have developed to accomplish this task: namely, *multi-party computation* (MPC) and, as an ingredient towards achieving the former*, fully-homomorphic encryption* (FHE). Then I’ll try to clear up the relationship between these two things, and explain the various tradeoffs that can make one better than the other for specific applications. Although these techniques can be used for so many things, throughout this post I’m going to focus on the specific application being considered in the EU: the use of privacy-preserving computation to conduct content scanning.

This post will not require any mathematics or much computer science, but it will require some patience. So find a comfortable chair and buckle in.

### Computing on private data

Encryption is an ancient technology. Roughly speaking, it provides the ability to convert meaningful messages (and data) into a form that only you, and your intended recipient(s) can read. In the modern world this is done using [public algorithms](https://csrc.nist.gov/Projects/cryptographic-standards-and-guidelines) that everyone can look at, combined with *secret keys* that are held only by the intended recipients.

Modern encryption is really quite excellent. So as long as keys are kept safe, encrypted data can be sent over insecure networks or stored in risky locations like your phone. And while occasionally people find a flaw in an implementation of encryption, the underlying technology works very well.

But sometimes encryption can get in the way. The problem with encrypted data is that it’s, well, *encrypted*. When stored in this form, such data is virtually useless for practical purposes like performing calculations. Before you can compute on that data, you often need to first *decrypt it* and thus remove all the beautiful protections we get from encryption.

If your goal is to compute on multiple pieces of data that originate from *different parties*, the problem can become even more challenging. Who can we trust to do the computing? An obvious solution is to decrypt all that data and hand it to one very trustworthy person, who will presumably swear not to steal it or get hacked. Finding those parties can be quite challenging.

Fortunately f...