---
title: An iCloud Backdoor Would Make Our Phones Less Safe
url: https://www.schneier.com/blog/archives/2025/02/an-icloud-backdoor-would-make-our-phones-less-safe.html
source: Schneier on Security
date: 2025-02-27
fetch_date: 2025-10-06T20:39:33.784152
---

# An iCloud Backdoor Would Make Our Phones Less Safe

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

## UK Demanded Apple Add a Backdoor to iCloud

Last month, the UK government [demanded](https://www.washingtonpost.com/technology/2025/02/07/apple-encryption-backdoor-uk/) that Apple weaken the security of iCloud for users worldwide. On Friday, Apple took steps to comply for users in the United Kingdom. But the British law is written in a way that requires Apple to give its government access to anyone, anywhere in the world. If the government demands Apple weaken its security worldwide, it would increase everyone’s cyber-risk in an already dangerous world.

If you’re an iCloud user, you have the option of turning on something called “[advanced data protection](https://support.apple.com/en-us/102651),” or ADP. In that mode, a majority of your data is end-to-end encrypted. This means that no one, not even anyone at Apple, can read that data. It’s a restriction enforced by mathematics—cryptography—and not policy. Even if someone successfully hacks iCloud, they can’t read ADP-protected data.

Using a controversial power in its 2016 Investigatory Powers Act, the UK government wants Apple to re-engineer iCloud to add a “backdoor” to ADP. This is so that if, sometime in the future, UK police wanted Apple to eavesdrop on a user, it could. Rather than add such a backdoor, Apple disabled ADP in the UK market.

Should the UK government persist in its demands, the ramifications will be profound in two ways. First, Apple can’t limit this capability to the UK government, or even only to governments whose politics it agrees with. If Apple is able to turn over users’ data in response to government demand, every other country will expect the same compliance. China, for example, will likely demand that Apple out dissidents. Apple, already [dependent](https://www.businessinsider.com/apple-dependent-on-china-economy-manufacturing-problem-2023-9) on China for both sales and manufacturing, won’t be able to refuse.

Second: Once the backdoor exists, others will attempt to surreptitiously use it. A technical means of access can’t be limited to only people with proper legal authority. Its very existence invites others to try. In 2004, hackers—we don’t know who—[breached](https://spectrum.ieee.org/the-athens-affair) a backdoor access capability in a major Greek cellphone network to spy on users, including the prime minister of Greece and other elected officials. Just last year, China [hacked](https://foreignpolicy.com/2024/12/19/salt-typhoon-hack-explained-us-china-cyberattack/) U.S. telecoms and gained access to their systems that provide eavesdropping on cellphone users, [possibly including](https://www.nytimes.com/2024/10/26/us/politics/salt-typhoon-hack-what-we-know.html) the presidential campaigns of both Donald Trump and Kamala Harris. That operation resulted in the FBI and the Cybersecurity and Infrastructure Security Agency [recommending](https://www.cisa.gov/sites/default/files/2024-12/guidance-mobile-communications-best-practices.pdf) [that](https://www.forbes.com/sites/zakdoffman/2024/12/06/fbi-warns-iphone-and-android-users-stop-sending-texts/) everyone use end-to-end encrypted messaging for their own security.

Apple isn’t the only company that offers end-to-end encryption. Google [offers](https://security.googleblog.com/2018/10/google-and-android-have-your-back-by.html) the feature as well. WhatsApp, iMessage, Signal, and Facebook Messenger offer the same level of security. There are other end-to-end encrypted cloud storage providers. Similar levels of security are available for phones and laptops. Once the UK forces Apple to break its security, actions against these other systems are sure to follow.

It seems unlikely that the UK is not coordinating its actions with the other “Five Eyes” countries of the United States, Canada, Australia, and New Zealand: the rich English-language-speaking spying club. Australia passed a [similar law](https://www.homeaffairs.gov.au/about-us/our-portfolios/national-security/lawful-access-telecommunications/assistance-and-access-industry-assistance-framework) in 2018, giving it authority to demand that companies weaken their security features. As far as we know, it has never been used to force a company to re-engineer its security—but since the law allows for a gag order we might never know. The UK law has a gag order as well; we only know about the Apple action because a whistleblower [leaked it](http://www.washingtonpost.com/technology/2025/02/07/apple-encryption-backdoor-uk/) to the *Washington Post*. For all we know, they may have demanded this of other companies as well. In the United States, the FBI has [long advocated](https://www.fbi.gov/news/speeches/going-dark-are-technology-privacy-and-public-safety-on-a-collision-course) for the same powers. Having the UK make this demand now, when the world is distracted by the foreign-policy turmoil of the Trump administration, might be what it’s been waiting for.

The companies need to resist, and—more importantly—we need to demand they do. The UK government, like the Australians and the FBI in years past, argues that this type of access is necessary for law enforcement—that it is “[going dark](https://www.fbi.gov/news/speeches/going-dark-are-technology-privacy-and-public-safety-on-a-collision-course)” and that the internet is a lawless place. We’ve heard this kind of talk since the [1990s](https://archive.epic.org/crypto/legislation/freeh_797.html), but its scant evidence doesn’t hold water. Decades of court cases with electronic evidence show again and again the police collect evidence through a variety of means, most of them—like traffic analysis or informants—having nothing to do with encrypted data. What police departments need are better computer investigative and forensics capabilities, not backdoors.

We can [all help](https://blog.cryptographyengineering.com/2025/02/12/u-k-asks-to-backdoor-icloud-backup-encryption/). If you’re an iCloud user, consider [turning this feature on](https://support.apple.com/en-us/108756). The more of us who use it, the harder it is for Apple to turn it off for those who need it to stay out of jail. This also puts pressure on other companies to offer similar security. And it helps those who need it to survive, because enabling the feature couldn’t be used as a de facto admission of guilt. (This is a benefit of using WhatsApp over Signal. Since so many people in the world use WhatsApp, having it on your phone isn’t in itself suspicious.)

On the policy front, we have two choices. [We](https://www.schneier.com/wp-content/uploads/2016/02/paper-key-escrow.pdf) [can’t](https://www.schneier.com/wp-content/uploads/2016/02/paper-keys-under-doormats.pdf) [build](https://www.schneier.com/wp-content/uploads/2024/01/Bugs_in_Our_Pockets.pdf) security systems that work for some people and not others. We can either make our communications and devices as secure as possible against everyone who wants acc...