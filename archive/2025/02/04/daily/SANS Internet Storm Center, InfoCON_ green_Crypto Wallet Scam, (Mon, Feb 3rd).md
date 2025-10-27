---
title: Crypto Wallet Scam, (Mon, Feb 3rd)
url: https://isc.sans.edu/diary/rss/31646
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-04
fetch_date: 2025-10-06T20:47:38.873473
---

# Crypto Wallet Scam, (Mon, Feb 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31642)
* [next](/diary/31650)

# [Crypto Wallet Scam](/forums/diary/Crypto%2BWallet%2BScam/31646/)

**Published**: 2025-02-03. **Last Updated**: 2025-02-03 09:10:15 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[8 comment(s)](/diary/Crypto%2BWallet%2BScam/31646/#comments)

Johannes noticed a SPAM comment on his YouTube channel:

![](https://isc.sans.edu/diaryimages/images/20250203-081829.png)

It was clear to us that this was a scam, but it wasn't clear to us how it worked.

The [seed phrase](https://en.wikipedia.org/wiki/Cryptocurrency_wallet#Seed_phrases) allows you to derive the private keys of the wallets, and gives you full control over the wallet. And as security professionals, we know you must never share private keys. So the scammer wants us to think that they shared their private keys without understanding the risk. And thus creating a (false) opportunity for dishonest people wanting to appropriate the content of the wallet. Because you have the private keys, you can move the funds out of the wallet to your own wallet.

So one could install wallet software and use the private key to control the wallet.

But let's do this a bit differently.

[Mnemonic Code Converter](https://iancoleman.io/bip39/) is an online/offline HTML page that takes seed phrases and converts them to a seed ([BIP39](https://en.bitcoin.it/wiki/BIP_0039)) and addresses ([BIP44](https://en.bitcoin.it/wiki/BIP_0044)).

Doing this for the scammer's seed phrase give this:

![](https://isc.sans.edu/diaryimages/images/20250203-083932.png)

I had to select a coin to derive the addresses. USDT (a [stablecoin](https://en.wikipedia.org/wiki/Stablecoin) for the US Dollar) is mentioned in the scam comment, but it's not an option in this page. I did some research, and discovered that USDT is a token that can be exchanged on different networks. The most popular network is Tron, and that coin is TRX. So let's try coin TRX:

![](https://isc.sans.edu/diaryimages/images/20250203-084317.png)

That address is indeed active on the Tron blockchain :

![](https://isc.sans.edu/diaryimages/images/20250203-084637.png)

This wallet contains $5000+, mostly in USDT, and a small bit in TRX. It's a real wallet, and it contains real assets. So what's the scam, why hasn't this money been moved out of the wallet yet?

One thing, notice this at the top of the page:

![](data:image/png;base64...)

This means that this is a multi-signature wallet (it has not one private key, like classic wallets, but it has multiple private keys), and that the published seed phrase doesn't give you control over the wallet. To move money out of the wallet, you need the private key of the address mentioned in the permissions (TGk...).

So that's why there is still $5000+ in this wallet.

Second thing, to move the $5000+ USDT tokens out of the wallet, you need to pay a fee with TRX tokens. And the amount of TRX tokens in the wallet is not sufficient to pay the fee. Thus you can't move the USDT tokens to your own wallet. And it's here that dishonest people get scammed.

They will move some of their own TRX into the wallet, and then use that to pay the fee to try to transfer the USDT to their own wallet (it won't work).

We can see this happening in the transaction history of this wallet:

![](https://isc.sans.edu/diaryimages/images/20250203-090029.png)

Small amounts of TRX are transfered to this wallet.

So this scam is targetting versed cryptocurrency users: you need to know that TRX coins are necessary to move USDT tokens out of a TRX wallet (I didn't know this).

But why would experienced cryptocurrency users not notice that this is a multisig wallet and that the seed phrase doesn't give them control over the wallet?

Maybe the explanation lies in the fact that the OKX wallet (mentioned in the scam comment) doesn't display that information (alledgedly, there are wallet applications that do flag multisig wallets).

After moving some TRX coins into the wallet, the transfer of USDT tokens is still not possible because of permissions, and the scam victims can't recover their TRX coins, because that transfer is also not possible because of permissions.

*I'm not well versed in cryptocurrency, please post a comment if you want to correct or complement things I explain here, or if you have different explanations. I used the following resources for my research:*

<https://www.reddit.com/r/CryptoScams/comments/1i95pk0/how_is_this_scam_working/>

[https://inleo.io/@bil.prag/crypto-scam-in-youtube-comment-5cs](https://inleo.io/%40bil.prag/crypto-scam-in-youtube-comment-5cs)

<https://www.reddit.com/r/Bitcoin/comments/10nmirl/how_to_get_publicprivate_key_of_an_address_using/>

<https://tronscan.io/#/address/TAy4omTf7uENvTm2QrT22ZY8BvdrjXUKzC>

Didier Stevens
Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[8 comment(s)](/diary/Crypto%2BWallet%2BScam/31646/#comments)

* [previous](/diary/31642)
* [next](/diary/31650)

### Comments

See also https://www.kaspersky.com/blog/cryptowallet-free-seed-phrase-scam/52810/
"The catch is that the bait is set up as a multi-signature wallet. To authorize outgoing transactions in such wallets, approval from two or more people is required, so transferring USDT to a personal wallet won’t work — even after paying the “commission”."

#### Anonymous

#### Feb 3rd 2025 8 months ago

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)