---
title: North Korean Hackers Steal $1.5B in Cryptocurrency
url: https://www.schneier.com/blog/archives/2025/02/north-korean-hackers-steal-1-5b-in-cryptocurrency.html
source: Schneier on Security
date: 2025-02-26
fetch_date: 2025-10-06T20:38:32.591135
---

# North Korean Hackers Steal $1.5B in Cryptocurrency

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

## North Korean Hackers Steal $1.5B in Cryptocurrency

It looks like a [very sophisticated](https://arstechnica.com/security/2025/02/how-north-korea-pulled-off-a-1-5-billion-crypto-heist-the-biggest-in-history/) attack against the Dubai-based exchange Bybit:

> Bybit officials [disclosed](https://announcements.bybit.com/article/incident-update---eth-cold-wallet-incident-blt292c0454d26e9140/) the theft of more than 400,000 ethereum and staked ethereum coins just hours after it occurred. The notification said the digital loot had been stored in a “Multisig Cold Wallet” when, somehow, it was transferred to one of the exchange’s hot wallets. From there, the cryptocurrency was transferred out of Bybit altogether and into wallets controlled by the unknown attackers.
>
> […]
>
> …a subsequent investigation by Safe found no signs of unauthorized access to its infrastructure, no compromises of other Safe wallets, and no obvious vulnerabilities in the Safe codebase. As investigators continued to dig in, they finally settled on the true cause. Bybit ultimately said that the fraudulent transaction was “manipulated by a sophisticated attack that altered the smart contract logic and masked the signing interface, enabling the attacker to gain control of the ETH Cold Wallet.”

The announcement on the Bybit website is almost comical. This is the headline: “Incident Update: Unauthorized Activity Involving ETH Cold Wallet.”

[More](https://research.checkpoint.com/2025/the-bybit-incident-when-research-meets-reality/):

> This hack sets a new precedent in crypto security by bypassing a multisig cold wallet without exploiting any smart contract vulnerability. Instead, it exploited human trust and UI deception:
>
> * Multisigs are no longer a security guarantee if signers can be compromised.* Cold wallets aren’t automatically safe if an attacker can manipulate what a signer sees.* Supply chain and UI manipulation attacks are becoming more sophisticated.
>
> The Bybit hack has shattered long-held assumptions about crypto security. No matter how strong your smart contract logic or multisig protections are, the human element remains the weakest link. This attack proves that UI manipulation and social engineering can bypass even the most secure wallets. The industry needs to move to end to end prevention, each transaction must be validated.

EDITED TO ADD (3/14): There has been [a](https://www.nytimes.com/2025/03/06/technology/bybit-crypto-hack-north-korea.html) [lot](https://www.nccgroup.com/us/research-blog/in-depth-technical-analysis-of-the-bybit-hack/) [written](https://www.elliptic.co/blog/bybit-hack-largest-in-history) about the details of this hack. It’s much more complicated, and sophisticated, than the initial news articles indicated. One [summary](https://www.halborn.com/blog/post/explained-the-bybit-hack-february-2025):

> The root of the Bybit transaction was a malicious transaction designed to modify the smart contract logic of the exchange’s multi-signature wallet. This change transferred ownership of the wallet to the attacker, allowing them to transfer the funds that it contained.
>
> This malicious transaction was masked within another, benign transaction that was sent to the wallet’s signers for approval. In the masked UI, this transaction showed a transfer from the project’s cold wallet to a hot wallet with the correct address and a Safe URL.
>
> Once this transaction was approved and digitally signed by the project’s team members, the hidden malicious code handed over control of the cold wallet to the attacker. From there, the attacker was able to transfer the assets held within the cold wallet to their own account, stealing an estimated $1.4 billion from the CEX.

Tags: [cryptocurrency](https://www.schneier.com/tag/cryptocurrency/), [hacking](https://www.schneier.com/tag/hacking/), [North Korea](https://www.schneier.com/tag/north-korea/), [theft](https://www.schneier.com/tag/theft/)

[Posted on February 25, 2025 at 12:04 PM](https://www.schneier.com/blog/archives/2025/02/north-korean-hackers-steal-1-5b-in-cryptocurrency.html) •
[23 Comments](https://www.schneier.com/blog/archives/2025/02/north-korean-hackers-steal-1-5b-in-cryptocurrency.html#comments)

### Comments

Who? •
[February 25, 2025 1:00 PM](https://www.schneier.com/blog/archives/2025/02/north-korean-hackers-steal-1-5b-in-cryptocurrency.html/#comment-443336)

> *Cold wallets aren’t automatically safe if an attacker can manipulate what a signer sees.*

I do not know what “cold wallet” means in this context. A true cold wallet is an independent, usually air gapped, device; if a cold wallet displays something on the computer screen then it is not a “cold” wallet, but a fancy “hot” wallet.

What a cold wallet displays on its LCD/OLED screen is information provided by the secure element inside it. It is the information being signed. If it lacks a LCD-style display then it is not a cold wallet, and whatever you sign on it is far from being trusted as a cold wallet never depends on a software element running on a computer.

It may have some support software, but information being signed should be provided by the secure element and displayed on the device’s LCD display. In short, it should work as a smartcard with a LCD display connected to the secure element and talking only to it, never to the computer itself.

If the secure element can be manipulated to sign something different to what it displays on the screen then… well… it is not a secure element at all.

It is by design, anything different from this design cannot be considered a cold wallet.

Who? •
[February 25, 2025 1:05 PM](https://www.schneier.com/blog/archives/2025/02/north-korean-hackers-steal-1-5b-in-cryptocurrency.html/#comment-443337)

I would like to add that seed phrases and passphrases are never typed on a software tool provided by the cold wallet manufacturer. As said, these are independent (and usually air gapped) devices.

If you trust on what a computer displays “from the cold wallet” or you type the secret seed words that open your wallet on a computer, think on what you are doing twice because you are not working on a cold wallet.

Clive Robinson •
[February 25, 2025 1:07 PM](https://www.schneier.com/blog/archives/2025/02/north-korean-hackers-steal-1-5b-in-cryptocurrency.html/#comment-443338)

@ Bruce, ALL,

> “North Korean Hackers Steal $1.5B in Cryptocurrency”

Only $1.5billion, hardly worth getting out of bed for, after all it’s only bits and bytes 😉

But on a more serious note,

“Cold Wallet to Hot Wallet, how?”

“Supply chain and UI manipulation attacks”

So nothing new realy these have been going on for more than a decade one way or another. The instances might –but probably are not– be new, but these classes of attack are well known and understood.

There is therefore something else involved…

To start with, I guess the definition of “Cold Wallet” as something not ...