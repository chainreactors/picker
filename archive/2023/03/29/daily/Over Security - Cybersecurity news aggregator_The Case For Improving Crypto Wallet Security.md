---
title: The Case For Improving Crypto Wallet Security
url: https://blog.doyensec.com//2023/03/28/wallet-info.html
source: Over Security - Cybersecurity news aggregator
date: 2023-03-29
fetch_date: 2025-10-04T11:02:41.408834
---

# The Case For Improving Crypto Wallet Security

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# The Case For Improving Crypto Wallet Security

28 Mar 2023 - Posted by Viktor Chuchurski

## Anatomy Of A Modern Day Crypto Scam

A large number of todayâs crypto scams involve some sort of [phishing](https://en.wikipedia.org/wiki/Phishing) attack, where the user is tricked into visiting a shady/malicious web site and connecting their wallet to it. The main goal is to trick the user into signing a transaction which will ultimately give the attacker control over the userâs tokens.

Usually, it all starts with a tweet or a post on some Telegram group or Slack channel, where a link is sent advertising either a new [yield farming](https://academy.binance.com/en/articles/what-is-yield-farming-in-decentralized-finance-defi) protocol boasting large APYs, or a new NFT project which just started minting. In order to interact with the web site, the user would need to connect their wallet and perform some confirmation or authorization steps.

Letâs take a look at the common NFT `approve` scam. The user is lead to the malicious NFT site, advertising a limited [pre-mint](https://www.coindesk.com/learn/buying-nfts-during-presales-and-public-mints-things-you-should-know/) of their new NFT collection. The user is then prompted to connect their wallet and sign a transaction, confirming the mint. However, for some reason, the transaction fails. The same happens on the next attempt. With each failed attempt, the user becomes more and more frustrated, believing the issue causes them to miss out on the mint. Their concentration and focus shifts slightly from paying attention to the transactions, to missing out on a great opportunity.

At this point, the phishing is in full swing. A few more failed attempts, and the victim bites.

![Wallet Phishing](../../../public/images/wallet-scam-txs.webp)

(Image borrowed from [How scammers manipulate Smart Contracts to steal and how to avoid it](https://coinsbench.com/how-scammers-manipulate-smart-contracts-to-steal-and-how-to-avoid-it-8b4e4a052985))

The final transaction, instead of the `mint` function, calls the `setApprovalForAll`, which essentially will give the malicious actor control over the userâs tokens. The user by this point is in a state where they blindly confirm transactions, hoping that the minting will not close.

Unfortunately, the last transaction is the one that goes through. Game over for the victim. All the attacker has to do now is act quickly and transfer the tokens away from the userâs wallet before the victim realizes what happened.

These type of attacks are really common today. A user stumbles on a link to a project offering new opportunities for profits, they connect their wallet, and mistakenly hand over their tokens to malicious actors. While a case can be made for user education, responsibility, and researching a project before interacting with it, we believe that software also has a big part to play.

## The Case For Improving Crypto Wallet Security

Nobody can deny that the introduction of both blockchain-based technologies and Web3 have had a massive impact on the world. A lot of them have offered the following common set of features:

* transfer of funds
* permission-less currency exchange
* decentralized governance
* digital collectibles

Regardless of the tech-stack used to build these platforms, itâs ultimately the users who make the platform. This means that users need a way to interact with their platform of choice. Today, the most user-friendly way of interacting with blockchain-based platforms is by using a **crypto wallet**. In simple terms, a crypto wallet is a piece of software which facilitates signing of blockchain transactions using the userâs [private key](https://en.wikipedia.org/wiki/Cryptocurrency_wallet). There are multiple types of wallets including software, hardware, custodial, and non-custodial. For the purposes of this post, we will focus on software based wallets.

Before continuing, letâs take a short detour to Web2. In that world, we can say that platforms (also called services, portals or servers) are primarily built using TCP/IP based technologies. In order for users to be able to interact with them, they use a user-agent, also known as a **web browser**. With that said, we can make the following parallel to Web3:

| Technology | Communication Protocol | User-Agent |
| --- | --- | --- |
| Web2 | HTTP/TLS | Web Browser |
| Web3 | Blockchain JSON RPC | Crypto Wallet |

Web browsers are arguably much, much more complex pieces of software compared to crypto wallets - and with good reason. As the Internet developed, people figured out how to put different media on it and web pages allowed for dynamic and [scriptable](https://en.wikipedia.org/wiki/JavaScript) content. Over time, advancements in HTML and CSS technologies changed what and how content could be shown on a single page. The Internet became a place where people went to socialize, find entertainment, and make purchases. Browsers needed to evolve, to support new technological advancements, which in turn increased complexity. As with all software, complexity is the enemy, and complexity is where bugs and vulnerabilities are born. Browsers needed to implement controls to help mitigate web-based vulnerabilities such as [spoofing](https://owasp.org/www-community/attacks/Content_Spoofing), [XSS](https://owasp.org/www-community/attacks/xss/), and [DNS rebinding](https://en.wikipedia.org/wiki/DNS_rebinding) while still helping to facilitate secure communication via encrypted [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) connections.

Next, lets see what a typical crypto wallet interaction for a normal user might look like.

### The Current State Of Things In The Web3 World

Using a Web3 platform today usually means that a user is interacting with a web application ([Dapp](https://ethereum.org/en/developers/docs/dapps)), which contains code to interact with the userâs wallet and smart contracts belonging to the platform. The steps in that communication flow generally look like:

#### 1. Open the Dapp

In most cases, the user will navigate their web browser to a URL where the Dapp is hosted (ex. [Uniswap](https://app.uniswap.org)). This will load the web page containing the Dappâs code. Once loaded, the Dapp will try to connect to the userâs wallet.

![Dapp and User Wallet](../../../public/images/wallet-connect00.png)

#### 2. Authorizing The Dapp

A few of the protections implemented by crypto wallets include requiring authorization before being able to access the userâs accounts and requests for transactions to be signed. This was not the case before [EIP-1102](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1102.md). However, implementing these features helped keep users anonymous, stop Dapp spam, and provide a way for the user to manage trusted and un-trusted Dapp domains.

![Authorizing The Dapp 1](../../../public/images/wallet-connect01.png)

If all the previous steps were completed successfully, the user can start using the Dapp.

When the user decides to perform an action (make a transaction, buy an NFT, stake their tokens, etc.), the userâs wallet will display a popup, asking whether the user confirms the action. The transaction parameters are generated by the Dapp and forwarded to the wallet. If confirmed, the transaction will be signed and published to the blockchain, awaiting confirmation.

![Authorizing The Dapp 2](../.....