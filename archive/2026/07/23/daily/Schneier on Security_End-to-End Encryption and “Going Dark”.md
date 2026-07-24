---
title: End-to-End Encryption and “Going Dark”
url: https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html
source: Schneier on Security
date: 2026-07-23
fetch_date: 2026-07-24T05:05:43.725001
---

# End-to-End Encryption and “Going Dark”

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

## End-to-End Encryption and “Going Dark”

New paper: “[Encryption and Globalization 15 Years Later: End-to-End Encryption and the Third Round of the ‘Going Dark’ Debate](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6959699)“:

> **Abstract**: This Article updates and expands on 2012 research on encryption and globalization, analyzing what the authors call “Round 3” of the Going Dark Debate: the current controversies over end-to-end encryption (E2EE). Governments around the world have proposed, and in some cases enacted, laws limiting E2EE for law enforcement and national security purposes.
>
> This Article explains the underlying technologies and market developments for a law and policy audience to assess those proposals critically. The Article proceeds in three parts tracking three rounds of the Going Dark Debate. Round 1 covers the Crypto Wars of the 1990s, when U.S. export controls on strong encryption ultimately fell in 1999. Round 2 covers the period roughly 2010 to 2015, when encryption-in-transit became widespread but lawful access remained available through cloud providers, giving rise to what the authors called a “golden age of surveillance” rather than a period of going dark. Round 3 addresses the current debate over E2EE, where no entity between sender and recipient can read the plaintext.
>
> The Article’s first major contribution is identifying five technically distinct scenarios for how E2EE operates in practice, each with different implications for lawful access. These scenarios reveal a substantial gap between the assumption that E2EE categorically blocks lawful access and the reality of how communications are sent and received. Second, the Article shows that E2EE is not limited to messaging; instead, it is embedded throughout the modern technology stack, including in Transport Layer Security, Secure Shell, Virtual Private Networks, and Zero Trust Architecture, the last of which is now legally required under U.S. and EU law. Any law broadly limiting E2EE would thus have severe serious consequences for cybersecurity, commerce, and government operations. The Article concludes that the two key lessons from Round 2—the least trusted country problem and the golden age of surveillance—remain true in Round 3, and that new government claims for restricting effective encryption deserve great skepticism.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [backdoors](https://www.schneier.com/tag/backdoors/), [crypto wars](https://www.schneier.com/tag/crypto-wars/), [encryption](https://www.schneier.com/tag/encryption/), [law enforcement](https://www.schneier.com/tag/law-enforcement/)

[Posted on July 23, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html) •
[5 Comments](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html#comments)

### Comments

Clive Robinson •
[July 23, 2026 9:26 AM](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html/#comment-456157)

@ Bruce, ALL,

The battle for “end to end encryption (E2EE) is effectively over.

The work of Claude Shannon and Gus Simmons shows that any “golden” key / backdoor etc will always be defeated and that new paper from NIST further shows why any “guardrail system” will always be 1ql.

The “new battle” those who raise the Spector of “going dark” is going to wage is “user content” via “client side scanning” carried out either locally or remotely by AI. But for those who can dig through the NIST paper will find that it’s findings are fully transferrable to the issue of defeating “client side llscanning”…

In effect the technical decision has been fully decided, and the proof is in,

“Going dark” can not be stopped”

They have in effect lost not battle but the whole war.

The problem is that the authoritarians will not give up on the idea thus will fight any which way they can…

KC •
[July 23, 2026 11:28 AM](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html/#comment-456159)

Re: “Round 3”

The golden age of surveillance is alive and well.

Rather than pulling back on E2EE, the authors provide a good review of E2EE access scenarios in practice.

**Five “endness” scenarios are illustrated in diagrams 3A-3E:** true E2EE, cloud backup, SAAS, on-device scanning, and the Ghost protocol.

And this is not to mention the ubiquitous data already available through social graphs, IoT devices, cameras, AI, etc…

A great risk of stymieing E2EE is the “Least Trusted Country” principle. “*That is, a backdoor accessible remotely by one country is also technically available to all other countries.*”

US and EU law already require the use of E2EE for Zero Trust Architecture (ZTA), including for critical infrastructure.

As evidenced, E2EE is an indispensable part of the solution for security.

Snarki, child of Loki •
[July 23, 2026 1:30 PM](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html/#comment-456161)

This is coming from the same morons that were trying to push “key escrow”.

Which, okay, you want all my keys? They won’t fit in an email/webform, so:

for (j=0;j<512;j++) {
for(k=0; k<256; k++) {
print("%s",k);
}
print("\n");
}

have fun!

s h o r t u r l . at / b9bRW •
[July 23, 2026 5:06 PM](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html/#comment-456166)

A case of severe corruption in the government. An innocent US Citizen destroyed by dirty corrupt cops, and terrorists in the offices of public prosecutor and public defender.
Heartless monsters who perverted the law, justice and the whole truth covered up an attempted murder.
s h o r t u r l . at / b9bRW

The Great EYE Is Upon You! •
[July 24, 2026 12:25 AM](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html/#comment-456169)

> ⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⠀⠈⣷⣄⠀⠀⠀⠀⣾⣷⠀⠀⠀⠀⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⠀⠀⢿⠿⠃⠀⠀⠀⠉⠉⠁⠀⠀⠐⠿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⣠⣶⣿⣿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⣿⡿⣿⣿⣷⣦⡀⠀⠀⠀
> ⠀⢀⣼⣿⣿⠟⠁⢠⣿⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⣿⡀⠙⢿⣿⣿⣦⠀⠀
> ⣰⣿⣿⡟⠁⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⣿⡇⠀⠀⠙⣿⣿⣷⡄
> ⠈⠻⣿⣿⣦⣄⠀⠸⣿⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⣿⠃⢀⣤⣾⣿⣿⠟⠁
> ⠀⠀⠈⠻⣿⣿⣿⣶⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣿⣾⣿⣿⡿⠋⠁⠀⠀
> ⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⠀⠀⢰⣷⡦⠀⠀⠀⢀⣀⣀⠀⠀⠀⢴⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠙⢷⠀⠀⠀⠀⠀⠀⠀⠀
> ⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
> Fifteen birds in five fir-trees,
> Their feathers were fanned in a fiery breeze.
> What funny little birds – they had no wings.
> Oh, what shall we do with the funny little things?
> Oh, what shall we do with the funny little things?
>
> Roast them alive or stew ’em in a pot!
> Fry them, boil them, eat them hot?
> Bake ’em! Toast ’em! Fry ’em! Roast ’em
> Till beards blaze and eyes glaze;
> Till hair swells and skins crack,
> Fat melts and bones black
> In cinders lie beneath the sky!
...