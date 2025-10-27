---
title: A Guide to Phishing Attacks
url: https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html
source: Schneier on Security
date: 2023-01-28
fetch_date: 2025-10-04T05:06:14.588409
---

# A Guide to Phishing Attacks

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

## A Guide to Phishing Attacks

This is a [good list](https://tidbits.com/2023/01/16/an-annotated-field-guide-to-identifying-phish/) of modern phishing techniques.

Tags: [cyberattack](https://www.schneier.com/tag/cyberattack/), [phishing](https://www.schneier.com/tag/phishing/)

[Posted on January 27, 2023 at 7:02 AM](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html) •
[9 Comments](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html#comments)

### Comments

Clive Robinson •
[January 27, 2023 10:29 AM](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html/#comment-416717)

@ ALL,

It’s been said before that there are three basic reasons phishing works,

1, Human trust, is usually the opposit of security trust.

There are others such as “greed” and “avarice” but they are small fish.

So phishing works, and will almost always work.

Thus the “techniques” or “methods” whilst of interest to researchers, is actually not that interesting to others.

It’s like you get taught at school that all such stories are based on the dozen or so Greek Tragedies by Aeschylus, Euripides, and Sophocles. Unless of cause they are comedies or satire, that apparently the Greeks also wrote the originals of… You get the idea…

The sad reality is once you actually know the base elements, you can see how they underlie all such “human weakness” attacks.

CJ •
[January 27, 2023 11:27 AM](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html/#comment-416720)

The most sophisticated phishing attempt I’ve seen in the wild (and one which isn’t mentioned in that article) is Conversation Hijacking:

<https://www.zdnet.com/article/what-is-phishing-how-to-protect-yourself-from-scam-emails-and-more/>
<https://www.veeam.com/blog/conversation-hijacking-phishing-scam.html>
<https://www.hornetsecurity.com/en/security-information/email-conversation-thread-hijacking/>

The one that I’d seen was extremely well-done; the actual text of the phishing attempt had been literally taken from an earlier point in the conversation, so it felt authentic, and since it purported to be coming from an outside vendor we were working with, the relative unfamiliarity of the specific URL wouldn’t necessarily raise red flags.

Really the only immediately-obvious tell was that it was resurrecting a thread which had finished up a few months’ previously. Obviously investigating email headers and such brought some other discrepancies to light, but most folks wouldn’t be looking for that in an already-established email thread. All in all, a scary attack — I could see myself falling for something like this in the future, even though I consider myself quite knoweldgeable and careful. Especially if the thread that got hijacked was a recent one.

I suppose the one saving grace for that kind of attack is that it relies on *someone’s* machine getting compromised in the first place; otherwise the phishing bot wouldn’t have the existing thread to work off of. So hopefully that keeps incidents down a bit.

CJ •
[January 27, 2023 11:43 AM](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html/#comment-416722)

(errr, re: that first zdnet.com URL, clearly I copied the wrong one. That was meant to be another one specifically about the conversation-hijacking thing. Alas!)

Ted •
[January 27, 2023 10:28 PM](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html/#comment-416776)

I like how the author puts numbered red dots next to the “phishy” signs of five different phishing emails.

He does a great job articulating what caught his eye and why.

I’m going to go on a limb and say it would be fun to play a game where you could try to find and label *phishy* elements.

The one that @CJ saw – conversation hijacking – sounds like a real doozy.

Steve •
[January 27, 2023 10:47 PM](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html/#comment-416779)

@ Clive Robinson Before school and during school we are taught, “Be polite, cooperative, and helpful”, it helps others, we will be helped in turn, it feels nice, and is good for society. In high school, college and the workplace we cooperate on group projects. For security we are taught, “Be suspicious of everything, your boss probably doesn’t need to transfer $8,000 to a random band account out of the blue, your boss probably doesn’t need iTunes gift cards right now, it may not be the actual IT department on the phone”, basically don’t be cooperative and helpful. Unfortunately this goes against the 2 decades of prior teaching and conditioning. Plus we still want/need to help out our fellow employees, just not attackers posing as employees. It’s a tricky problem.

Clive Robinson •
[January 28, 2023 4:02 AM](https://www.schneier.com/blog/archives/2023/01/a-guide-to-phishing-attacks.html/#comment-416788)

@ Steve,

Re : Being nice.

> “It’s a tricky problem.”

It is, especially when as anthropologists point out “being social” is actually effectively genetic, and may be due to evolution.

As you may not know, the size of the human head, thus the brain is limited by the size of what is politely called the “birth canal”.

As a result the head of a baby is actually “compressed” and expands significantly over the next few days after birth as the skull bones move into place.

It has been argued that this process is part of the reason human babies do not “get up and run with the herd” within an hour of birth. Or as with arachnida:araneae start spining geometrically complex webs.

As a very loose analogy human babies are like PCs once were and the spiders like the microcontroler in your coffee machine. Whilst the coffee machine “worked out of the box” the PC did not, it needed a little love and attention and software be loaded to give it it’s working personality and function.

Thus for babies to survive to become viable parents they need the support of their parents / family / troop / society. Being nice or atleast the ability to fake being nice is a survival trait.

It’s also been argued that adolescence where children undergo a major psychological change and thus appear almost as an “alien species” occurs because they have reached a point where they can survive independently. Thus they are faced with a choice along a scale of total independence from others to total dependence on others. Either end of the scale actually being evolutionary undesirable.

So the argument is being “social, is an essential built in” of humans more so in women than men as they are the initial primary care givers[1].

So… If being “social” is evolutionarily desirable, but also a “security anti-pattern” not only does it raise a series of interesting questions[2], it also tells us implicitly that phishing is not going to go away.

But it also has a more curious question lurking withi...