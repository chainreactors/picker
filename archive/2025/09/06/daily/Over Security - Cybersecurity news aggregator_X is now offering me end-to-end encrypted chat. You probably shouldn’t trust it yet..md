---
title: X is now offering me end-to-end encrypted chat. You probably shouldn’t trust it yet.
url: https://techcrunch.com/2025/09/05/x-is-now-offering-me-end-to-end-encrypted-chat-you-probably-shouldnt-trust-it-yet/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-06
fetch_date: 2025-10-02T19:45:17.788709
---

# X is now offering me end-to-end encrypted chat. You probably shouldn’t trust it yet.

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-lockup.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)
* [Disrupt 2025](https://techcrunch.com/events/tc-disrupt-2025/)

* [Events](/events/)
* [Podcasts](/podcasts/)
* [Newsletters](/newsletters/)

Search

Submit

Site Search Toggle

Mega Menu Toggle

### Topics

[Latest](/latest/)

[AI](/category/artificial-intelligence/)

[Amazon](/tag/amazon/)

[Apps](/category/apps/)

[Biotech & Health](/category/biotech-health/)

[Climate](/category/climate/)

[Cloud Computing](/tag/cloud-computing/)

[Commerce](/category/commerce/)

[Crypto](/category/cryptocurrency/)

[Enterprise](/category/enterprise/)

[EVs](/tag/evs/)

[Fintech](/category/fintech/)

[Fundraising](/category/fundraising/)

[Gadgets](/category/gadgets/)

[Gaming](/category/gaming/)

[Google](/tag/google/)

[Government & Policy](/category/government-policy/)

[Hardware](/category/hardware/)

[Instagram](/tag/instagram/)

[Layoffs](/tag/layoffs/)

[Media & Entertainment](/category/media-entertainment/)

[Meta](/tag/meta/)

[Microsoft](/tag/microsoft/)

[Privacy](/category/privacy/)

[Robotics](/category/robotics/)

[Security](/category/security/)

[Social](/category/social/)

[Space](/category/space/)

[Startups](/category/startups/)

[TikTok](/tag/tiktok/)

[Transportation](/category/transportation/)

[Venture](/category/venture/)

### More from TechCrunch

[Staff](/about-techcrunch/)

[Events](/events/)

[Startup Battlefield](/startup-battlefield/)

[StrictlyVC](https://strictlyvc.com/)

[Newsletters](/newsletters/)

[Podcasts](/podcasts/)

[Videos](/video/)

[Partner Content](/sponsored/)

[TechCrunch Brand Studio](/brand-studio/)

[Crunchboard](https://www.crunchboard.com/)

[Contact Us](/contact-us/)

![X (formerly Twitter) logo on a cracked wall](https://techcrunch.com/wp-content/uploads/2023/08/twitter-x-logo-musk-2.jpg?w=1024)

**Image Credits:**TechCrunch

[Security](https://techcrunch.com/category/security/)

# X is now offering me end-to-end encrypted chat — you probably shouldn’t trust it yet

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

9:04 AM PDT · September 5, 2025

X, formerly Twitter, has [started rolling out](https://techcrunch.com/2025/09/04/xs-encrypted-dm-feature-xchat-is-rolling-out-more-broadly/) its new encrypted messaging feature called “Chat” or “XChat.”

The company claims the new communication feature is [end-to-end encrypted](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#end-to-end-encryption), meaning messages exchanged on it can only be read by the sender and their receiver, and — in theory — no one else, including X, can access them.

Cryptography experts, however, are warning that X’s current implementation of encryption in XChat should not be trusted. They’re saying it’s far worse than Signal, a technology widely considered the state of the art when it comes to end-to-end encrypted chat.

![](https://techcrunch.com/wp-content/uploads/2025/09/xchat-encrypted-chat-enable.png)

In XChat, once a user clicks on “Set up now,” X prompts them to create a four-digit PIN, which will be used to encrypt the user’s private key. This key is then stored on X’s servers. The private key is essentially a secret cryptographic key assigned to each user, serving the purpose of decrypting messages. As in many end-to-end encrypted services, a private key is paired with a public key, which is what a sender uses to encrypt messages to the receiver.

This is the first red flag for XChat. Signal stores a user’s private key on their device, not on its servers. How and where exactly the private keys are stored on the X servers is also important.

Matthew Garrett, a security researcher [who published a blog post](https://mjg59.dreamwidth.org/71646.html) about XChat in June, when X announced the new service and slowly [started rolling it out](https://techcrunch.com/2025/05/30/xs-new-dm-feature-xchat-is-rolling-out-in-beta/), wrote that if the company doesn’t use hardware security modules, or HSMs, to store the keys, then the company could tamper with the keys — brute-forcing them for example since they are only four digits — and potentially decrypt messages. HSMs are servers made specifically to make it harder for the company that owns them to access the data inside.

An X engineer [said](https://x.com/cambridgemike/status/1932260008278012265?s=46) in a post in June that the company does use HSMs, but neither he nor the company has provided any proof so far. “Until that’s done, this is ‘trust us, bro’ territory,” Garrett told TechCrunch.

The second red flag, [which X admits](https://help.x.com/en/using-x/encrypted-direct-messages#:~:text=Currently%2C%20we%20do,release%20that%20will%3A) on the XChat support page, is that the current implementation of the service could allow “a malicious insider or X itself” to compromise encrypted conversations.

This is what is technically called an “[adversary-in-the-middle](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#adversary-in-the-middle),” or AITM attack. That makes the whole point of an end-to-end encrypted messaging platform moot.

Garrett said that X “gives you the public key whenever you communicate with them, so even if they’ve implemented this properly, you can’t prove they haven’t made up a new key” and performed an AITM attack.

Another red flag is that none of XChat’s implementation, at this point, is open source, unlike Signal’s, which is [openly documented in detail](https://signal.org/docs/). X [says](https://help.x.com/en/using-x/encrypted-direct-messages#:~:text=open%20source%20our%20implementation%20and%20describe%20the%20encryption%20technology%20in%20depth%20through%20a%20technical%20whitepaper%20later%20this%20year.) it aims to “open source our implementation and describe the encryption technology in depth through a technical whitepaper later this year.”

Finally, X doesn’t offer “[perfect forward secrecy](https://threema.com/en/faq/perfect-forward-secrecy),” a cryptographic mechanism by which every new message is encrypted with a different key, which means that if an attacker compromises the user’s private key, they can only decrypt the last message, and not all the preceding ones. The company itself also [admits](https://help.x.com/en/using-x/encrypted-direct-messages#:~:text=the%20near%20future.-,Forward%20secrecy%C2%A0,-If%20the%20private) this shortcoming.

As a result, Garrett doesn’t think XChat is at a point where users should trust it just yet.

“If everyone involved is fully trustworthy, the X implementation is technically worse than Signal,” Garrett told TechCrunch. “And even if they were fully trustworthy to start with, they could stop being trustworthy and compromise trust in multiple ways … If they were either untrustworthy or incompetent during initial implementation, it’s impossible to demonstrate that there’s any security at all.”

Garrett isn’t the only expert raising concerns. Matthew Green, a cryptography expert who teaches at Johns Hopkins University, agrees.

“For the moment, until it gets a full audit by someone reputable, I would not trust this any more than I trust current unencrypted DMs,” Green told TechCrunch. (XChat is a separate feature that lives, at least for now, with the legacy Direct Messages.)

![](https://techcrunch.com/wp-content/uploads/2025/09/x-chat-menu.png)

X did not respond to several questions sent to its press email address.

Topics

[Apps](https://techcrunch.com/category/apps/), [cryptography](https://techcrunch.com/tag/cryptography/), [cybersecurity](https://...