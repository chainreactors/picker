---
title: China Possibly Hacking US “Lawful Access” Backdoor
url: https://www.schneier.com/blog/archives/2024/10/china-possibly-hacking-us-lawful-access-backdoor.html
source: Schneier on Security
date: 2024-10-09
fetch_date: 2025-10-06T18:57:58.807136
---

# China Possibly Hacking US “Lawful Access” Backdoor

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

## China Possibly Hacking US “Lawful Access” Backdoor

The *Wall Street Journal* is [reporting](https://www.wsj.com/tech/cybersecurity/u-s-wiretap-systems-targeted-in-china-linked-hack-327fc63b) that Chinese hackers (Salt Typhoon) penetrated the networks of US broadband providers, and might have accessed the backdoors that the federal government uses to execute court-authorized wiretap requests. Those backdoors have been mandated by law—CALEA—since 1994.

It’s a weird story. The first line of the article is: “A cyberattack tied to the Chinese government penetrated the networks of a swath of U.S. broadband providers.” This implies that the attack wasn’t against the broadband providers directly, but against one of the intermediary companies that sit between the government CALEA requests and the broadband providers.

For years, the security community has pushed back against these backdoors, pointing out that the technical capability cannot differentiate between good guys and bad guys. And here is one more example of a backdoor access mechanism being targeted by the “wrong” eavesdroppers.

Other [news](https://www.reuters.com/technology/cybersecurity/chinese-hackers-breached-us-court-wiretap-systems-wsj-reports-2024-10-06/) [stories](https://edition.cnn.com/2024/10/05/politics/chinese-hackers-us-telecoms/index.html).

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [CALEA](https://www.schneier.com/tag/calea/), [China](https://www.schneier.com/tag/china/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [hacking](https://www.schneier.com/tag/hacking/)

[Posted on October 8, 2024 at 7:00 AM](https://www.schneier.com/blog/archives/2024/10/china-possibly-hacking-us-lawful-access-backdoor.html) •
[27 Comments](https://www.schneier.com/blog/archives/2024/10/china-possibly-hacking-us-lawful-access-backdoor.html#comments)

### Comments

Clive Robinson •
[October 8, 2024 12:34 PM](https://www.schneier.com/blog/archives/2024/10/china-possibly-hacking-us-lawful-access-backdoor.html/#comment-440994)

Funny in a sad way but I used CALEA as an example of a bad idea put into legislation just a short time back.

The thing that most do not realise is that the actual “back door” does not need to be present, just the hooks for it in the system.

I doubt many remember back the twenty years to the Greek Olympics, but the main cellphone provider did Vodafone did not have the CALEA software installed in it’s equipment. But because the switches had it as a paid for option the low level hooks etc were in place in them.

The CIA/NSA used “the games” as an excuse to “check security”, and in the process a backdoor was dropped onto the hooks and more than a hundred senior Greek Government individuals had their phones put under surveillance, as well as some of their families and arabic business men.

For reasons not clear but incompetence by a CIA officer was indicated the backdoor was found. As an enquiry got under way and started to home in on events a phone company employee was found dead and he was blamed. Initially claimed to be a suicide it was later found to be murder with fingers pointed at the US.

The point everyone should remember is that when designing communications systems, you must design them in a way that backdoors are not only not possible but indicative behaviour will get flagged up quickly.

Otherwise on the sensible view expressed in Claude Shannon’s pithy maxim of,

“The enemy knows the system”[1],

the enemy will try to build an illicit backdoor in if you give them any crack to exploit.

Such “defensive engineering” to stop it is not something the vast majority of software and other systems developers understand and it’s long over due as an industry that ICT “Got it’s ‘sand’ together” on the matter.

Whilst E2EE when properly done –and it’s mostly not– can protect the “message contents” it does not protect much of anything else about the communications. That is the actual traffic meta-data and meta-meta-data allows not just “Traffic Analysis” but other forms of analysis and correlation by which information can be reasoned.

[1] Actually a rewording of Dutch Prof Auguste Kerckhoffs’s 2nd principle from the early 1880’s.

Who? •
[October 8, 2024 12:40 PM](https://www.schneier.com/blog/archives/2024/10/china-possibly-hacking-us-lawful-access-backdoor.html/#comment-440995)

NOBUS at its best.

I hope some day one of these mandated-by-law backdoors will be used to make a truly destructive attack against U.S. critical infraestructures, so they start taking cybersecurity seriously and radically change their minds with relation to government backdoors.

I am sorry for being so harsh, but weakening computer and network (well… both are the same as the old Sun Microsystems slogan said, right?) security has nothing to do with cybersecurity. A secure computer is a secure device, secure against adversaries and secure against us too. I will say more, if NSA finds a vulnerability in a software project developed outside the United States, they should communicate the vulnerability to the developers of that software project too, at least if that software is used in the United States.

No one should play in the cybersecurity field by weakening the security of computer systems, at least not if they play in the “good guys” team.

Well, take this event as a warning note. I am not able to read an article behind a paywall, so I am unsure about what this attack means, but hope it will not be too difficult to fix. And, no, the fix is not changing the backdoor to a different one. The only acceptable fix is closing the backdoor forever.

Who? •
[October 8, 2024 12:46 PM](https://www.schneier.com/blog/archives/2024/10/china-possibly-hacking-us-lawful-access-backdoor.html/#comment-440996)

Another point of view, this one from a non-paywalled source:

hxxps://www.securityweek.com/chinas-salt-typhoon-hacked-att-verizon-report/

There is no much information about this incident right now.

Clive Robinson •
[October 8, 2024 1:15 PM](https://www.schneier.com/blog/archives/2024/10/china-possibly-hacking-us-lawful-access-backdoor.html/#comment-440997)

The story is unclear but people need to consider the following,

1, Many phone “back bones” are IP based networks.

2, The CALEA “back doors” are at the communications switches.

3, The Guard labour monitoring are nolonger munching down on doughnuts in a van, but sitting munching at office desks “somewhere”

4, The switches and guard labour are linked via existing –virtual–networking systems.

Thus this alleged attack may actually be on the virtual network that snakes across the US to the likes of FBI offices in any of the states, not just the state the CALEA “tee” is in place.

Oh on another “point of the minute that is “almost the same MO” but different industry…

It appears a water supply organisation is,

“Slamming the stable door, to the sound of distant hoof beats”...