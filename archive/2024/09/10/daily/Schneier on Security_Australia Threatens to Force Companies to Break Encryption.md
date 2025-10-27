---
title: Australia Threatens to Force Companies to Break Encryption
url: https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html
source: Schneier on Security
date: 2024-09-10
fetch_date: 2025-10-06T18:31:03.891530
---

# Australia Threatens to Force Companies to Break Encryption

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

## Australia Threatens to Force Companies to Break Encryption

In 2018, Australia passed the Assistance and Access Act, which—among other things—gave the government the [power](https://www.upguard.com/blog/australias-assistance-and-access-act) to force companies to break their own encryption.

> The Assistance and Access Act includes key components that outline investigatory powers between government and industry. These components include:
>
> * Technical Assistance Requests (TARs): TARs are voluntary requests for assistance accessing encrypted data from law enforcement to teleco and technology companies. Companies are not legally obligated to comply with a TAR but law enforcement sends requests to solicit cooperation.* Technical Assistance Notices (TANs): TANS are compulsory notices (such as computer access warrants) that require companies to assist within their means with decrypting data or providing technical information that a law enforcement agency cannot access independently. Examples include certain source code, encryption, cryptography, and electronic hardware.* Technical Capability Notices (TCNs): TCNs are orders that require a company to build new capabilities that assist law enforcement agencies in accessing encrypted data. The Attorney-General must approve a TCN by confirming it is reasonable, proportionate, practical, and technically feasible.

It’s that final one that’s the real problem. The Australian government can force tech companies to build backdoors into their systems.

This is law, but near as anyone can tell the government has never used that third provision.

Now, the director of the Australian Security Intelligence Organisation (ASIO)—that’s basically their FBI or MI5—is threatening to do just that:

> ASIO head, Mike Burgess, says he may soon use powers to compel tech companies to cooperate with warrants and unlock encrypted chats to aid in national security investigations.
>
> […]
>
> But Mr Burgess says lawful access is all about targeted action against individuals under investigation.
>
> “I understand there are people who really need it in some countries, but in this country, we’re subject to the rule of law, and if you’re doing nothing wrong, you’ve got privacy because no one’s looking at it,” Mr Burgess said.
>
> “If there are suspicions, or we’ve got proof that we can justify you’re doing something wrong and you must be investigated, then actually we want lawful access to that data.”
>
> Mr Burgess says tech companies could design apps in a way that allows law enforcement and security agencies access when they request it without comprising the integrity of encryption.
>
> “I don’t accept that actually lawful access is a back door or systemic weakness, because that, in my mind, will be a bad design. I believe you can ­ these are clever people ­ design things that are secure, that give secure, lawful access,” he said.

We in the encryption space call that last one “[nerd harder](https://boingboing.net/2018/01/12/imaginary-numbers.html).” It, and the rest of his remarks, are the same tired talking points we’ve heard again and again.

It’s going to be an awfully big mess if Australia actually tries to make Apple, or Facebook’s WhatsApp, for that matter, break its own encryption for its “targeted actions” that put every other user at risk.

Tags: [Australia](https://www.schneier.com/tag/australia/), [backdoors](https://www.schneier.com/tag/backdoors/), [crypto wars](https://www.schneier.com/tag/crypto-wars/), [encryption](https://www.schneier.com/tag/encryption/), [laws](https://www.schneier.com/tag/laws/)

[Posted on September 9, 2024 at 7:03 AM](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html) •
[25 Comments](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html#comments)

### Comments

Agammamon •
[September 9, 2024 7:18 AM](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html/#comment-440407)

> . . . but in this country, we’re subject to the rule of law, and if you’re doing nothing wrong, you’ve got privacy because no one’s looking at it,” Mr Burgess said.

Except that ‘this country’ is Australia – not exactly known as a bastion of personal freedom among the Western countries.

And ask people in the US/UK/Canada/France/Germany/Etc how well ‘if you’ve done nothing wrong, you have nothing to worry about’ works.

mw •
[September 9, 2024 8:04 AM](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html/#comment-440408)

That is exactly the reason why an end-to-end encryption is essitial where the private key never leaves the device and is solely in possession of the end users. So a man-in-the-middle, like tech providers, is never able to decrypt any message. In the best case the key is stored on a HSM device, but not on a TPM that isn’t fully under control of the user.

Rontea •
[September 9, 2024 8:28 AM](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html/#comment-440410)

One of the great commandments of science is, “Mistrust arguments from authority”.

Tim Bradshaw •
[September 9, 2024 8:46 AM](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html/#comment-440411)

From a historical perspective I think it would be interesting to know how many times we’ve been through the sequence of

1. government agency announces that they are going to force organisations to backdoor their encryption;
2. justified articles, like this one, pointing out that would be very bad;
3. pause (while presumably, behind the scenes, somebody patiently explains to the agency concerned that what they want is not mathematically possible and what the can have is extremely undesirable);
4. nothing happens;
5. pause, go to 1.

I wish I had kept a record of them all.

B.J. Herbison •
[September 9, 2024 9:45 AM](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html/#comment-440412)

Is the third element verbatim? Giving access to “encrypted data” is easy, just give it

It’s letting them see the unencrypted version of the encrypted data that’s unreasonable, disproportionate, impractical, and technically infeasible (if the system is designed correctly).

Sean •
[September 9, 2024 11:59 AM](https://www.schneier.com/blog/archives/2024/09/australia-threatens-to-force-companies-to-break-encryption.html/#comment-440414)

Simplest fix is for all those companies to blacklist the entire continent, and any device will authenticate with “due to your government implementing act XXXXX, this will break our product. You can contact your local MP at , email and this address”, an action that likely will mean they w...