---
title: Two clicks from empty – IPFS-powered crypto drainer scams leveraging look-alike CDNs
url: https://www.netcraft.com/blog/ipfs-powered-crypto-drainer-scams-leveraging-look-alike-cdns/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-11
fetch_date: 2025-10-06T17:46:10.875655
---

# Two clicks from empty – IPFS-powered crypto drainer scams leveraging look-alike CDNs

[**GUIDE:** The Total Economic Impact芒聞垄 of Netcraft Brand Protection | Download now 芒聠聮](../lp/forrester-tei-study)

[Pricing](../get-pricing)

[Contact Us](../contact)

[Report Fraud](https://report.netcraft.com/)

[Login](https://services.netcraft.com/)

Platform

Solutions

[Why Netcraft](../why-netcraft)

Resources

Company

[GET Demo](../book-a-demo)

[**GUIDE:** The Total Economic Impact芒聞垄 of Netcraft Brand Protection | Download now 芒聠聮](../lp/forrester-tei-study)

[**GUIDE:** The Total Economic Impact芒聞垄 of Netcraft Brand Protection | Download now 芒聠聮](../lp/forrester-tei-study)

[Pricing](../get-pricing)

[Contact Us](../contact)

[Report Fraud](https://report.netcraft.com/)

[Login](https://services.netcraft.com/)

Platform

Solutions

[Why Netcraft](../why-netcraft)

Resources

Company

[GET Demo](../book-a-demo)

[**GUIDE:** The Total Economic Impact芒聞垄 of Netcraft Brand Protection | Download now 芒聠聮](../lp/forrester-tei-study)

[## ALL POSTS](../resources/blog)

[## ALL POSTS](../resources/blog)

[## ALL POSTS](../resources/blog)

# Two clicks from empty 芒聙聯 IPFS-powered crypto drainer scams leveraging look-alike CDNs

By

By

By

Harry Freeborough

Harry Freeborough

Harry Freeborough

|

|

|

July 10, 2024

July 10, 2024

July 10, 2024

![](https://framerusercontent.com/images/jxxRGtMLzq6QxJ4GYRCCbx2QFQ.svg?width=27&height=28)

![](https://framerusercontent.com/images/qxE8AF5N0tvgi2NQPrJxo2Fjec8.svg?width=27&height=28)

![](https://framerusercontent.com/images/iPf6JKc4mxyBKQ0kzbQ3awaw.svg?width=27&height=28)

![Reddit logo](https://framerusercontent.com/images/SgQ1svDD2syGHlolx4eeBq0UPA.svg?width=28&height=29)

![](https://framerusercontent.com/images/C9tHS9Dzuj53JYDeDjMhPBKywc.png?width=1424&height=718)

![](https://framerusercontent.com/images/C9tHS9Dzuj53JYDeDjMhPBKywc.png?width=1424&height=718)

![](https://framerusercontent.com/images/C9tHS9Dzuj53JYDeDjMhPBKywc.png?width=1424&height=718)

![](https://framerusercontent.com/images/C9tHS9Dzuj53JYDeDjMhPBKywc.png?width=1424&height=718)

**More than $40k lost to crypto drainer scams leveraging IPFS and malicious code hidden behind look-alike CDN imitations.**

At Netcraft, we芒聙聶ve been disrupting [cryptocurrency-based scams for over 10 years](https://www.netcraft.com/blog/deceptive-search-engine-ads-used-in-bitcoin-wallet-attacks/), including more than 15,000 IPFS phishing takedowns since 2016. As we closely monitor evolving threats and criminal innovation, modern technologies like Web3 APIs have made crypto scams easier and more accessible than ever before.

Cryptocurrencies remain a particular target for criminals due to their decentralized nature; no central arbiter of transactions means that victims have no way to reverse mistakes, nor any avenue to redress any losses incurred.

In this blog post, we芒聙聶ll cover crypto drainers, a type of payment diversion fraud that takes advantage of Web3 APIs to trick victims into giving away their cryptocurrency coins and tokens. Just two clicks on a copycat website to 芒聙聵claim a free token芒聙聶 could irreversibly transfer all their crypto assets to criminals.

## Crypto drainers and Web3 wallet APIs

Web3 wallet APIs are designed to allow websites to interact with users芒聙聶 cryptocurrency wallets, and function as a bridge between applications and the blockchain. They can only run in a Web3-enabled browser (such as [Brave](https://brave.com/)), or with a browser extension like [MetaMask](https://metamask.io/). The wallet APIs allow sites to request the user sign a specific message, or to send some cryptocurrency to a specific address.

In a standard crypto draining scam, a cybercriminal will claim to be offering free cryptocurrency tokens to the user, most commonly in the form of minting new coins. This is used to trick the victim into connecting their wallet to a malicious website, which can then obtain the victim芒聙聶s cryptocurrency address.

![](https://framerusercontent.com/images/mkdfKzUOq6nOt4Ir2tohvMRhcY.png?width=686&height=476)

*Figure 1 - Cryptocurrency drainer at nonextpepe[.]com.*

Once connected, the criminal can request signatures or transactions for this wallet. It芒聙聶s important to note that connecting a wallet alone does **not** allow the site to steal its contents. However, once connected, the drainer will typically lure the victim into 芒聙聵claiming their token芒聙聶 by requesting a transaction. If approved, this will transfer the victim芒聙聶s entire balance into a wallet controlled by the criminal, effectively 芒聙聵draining芒聙聶 the victim芒聙聶s wallet.

![](https://framerusercontent.com/images/U5M3b64TuAI5UklM3D8U90yOpoU.png?width=276&height=498)

*Figure 2 Drainer-generated transaction for the whole wallet's balance*

The criminals behind these drainer scams count on victims being sufficiently excited or distracted by the promise of free cryptocurrency tokens that they do not realize that by approving the transaction, they芒聙聶re losing everything in their wallet. In the example below, the Ethereum balance is sent to smart contract **0x676CA33022fB1a41c6cFE47Eac2E896F398e5783**, which forwards everything received to the wallet **0x9f335dfa31bfb56dfa153efd4092c96ca22fd789** (and provides nothing in return). The destination address alone has received over 25ETH, totaling over $40,000 based on exchange rate at time of transfer.

![](https://framerusercontent.com/images/BME3o7SODpV0YXy0lZM9qiSNMcI.png?width=616&height=412)

*Figure 3 Draining snippet for nonextpepe[.]com*

## Cryptocurrency copycats

Crypto drainers will often mimic legitimate cryptocurrency projects, using familiar tokens, names, and branding to trick victims into approving malicious transactions. In this example, Lista is a real cryptocurrency project, [https://lista.org](https://lista.org/), with its decentralized stablecoin **lisUSD** pegged to the USD. Netcraft analysts have identified a crypto drainer site, **claim-lista[.]org**which has copied the entire Lista site.

![](https://framerusercontent.com/images/G1PJoegjjsynY2HRlzdINKZe5dA.png?width=967&height=1024)

*Figure 4 Lista's legitimate site (top) with the copycat site (claim-lista[.]org) below.*

The malicious site claims that a 芒聙聵limited time airdrop芒聙聶 event is currently available (an airdrop is typically an event in which new coins or tokens can be claimed for free to garner publicity). Clicking the **Claim Allocation** button displays a transaction request for the victim to confirm. If they do this, their entire balance is sent to a wallet and 芒聙聯 unsurprisingly 芒聙聯 no coin or token is provided in return.

Examining the malicious site芒聙聶s source code displays markers left from a website copying tool, which reveals that the site is a direct duplication of the real cryptocurrency project.

![](https://framerusercontent.com/images/WQ9e9GzztaDtILQIZnh6uCfSCm4.png?width=970&height=146)

*Figure 5 Source code of malicious site with markers from a website copying tool*

Website copying tools allow the criminals behind these crypto drainer campaigns to quickly spoof legitimate cryptocurrency projects at scale, requiring only small modifications (and minimal technical skills) to insert the malicious draining payload.

## IPFS gateways

IPFS stands for I**nterPlanetary File System** (**IPFS**); it is a decentralized storage and delivery network . Unlike the conventional web, where most content is hosted on centralized servers, IPFS embodies the Web 3.0 ethos and is based on peer-to-peer (P2P) networking, without requiring third parties or centralized authorities. This means that it芒聙聶s harder to take down malicious content on the network, making IPFS ideal for cybercriminals when [running phishing attack campaigns](https://www.netcraft.com/blog/disrupting-ipfs-phishing-attacks/).

While IPFS URLs aren芒聙聶t directly accessible in most popular browsers, they are accessible through various **IPFS gateways** such as [ipfs.io](http://ipfs.io/). Netcraft analysts have already detected criminals using IPFS gateways for crypto ...