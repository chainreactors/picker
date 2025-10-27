---
title: Ethereum Reboots Crypto Investigation
url: https://www.secjuice.com/ethereum-reboots-crypto-investigation/
source: Instapaper: Unread
date: 2024-09-02
fetch_date: 2025-10-06T18:26:31.442707
---

# Ethereum Reboots Crypto Investigation

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[OSINT](/tag/osint/)

# Ethereum Reboots Crypto Investigation

The smart blockchain created a crypto ecosystem of NFTs, DeFi, and Dapps, along with new kinds of investigations.

* [![Tom Caliendo](/content/images/size/w100/2022/07/square-profile.png)](/author/tom-caliendo/)

#### [Tom Caliendo](/author/tom-caliendo/)

Aug 31, 2024
• 7 min read

![Ethereum Reboots Crypto Investigation](/content/images/size/w2000/2024/08/Capture-1.PNG)

At the risk of using and overused phrase, the Ethereum Blockchain "revolutionized crypto" by also being a virtual computer that can execute code. Ethereum gave us smart contracts and the ability to create NFTs, DeFi and so much else.

In turn, this opened up a whole new world of opportunities for investigation. For crypto investigators, this is arguably akin to the change in OSINT before and after social media.

This post walks through some foundational aspects of investigations on the Ethereum Blockchain, including researching an Ethereum address, smart contracts, and NFTs.

### **Etherscan.io and Ethereum Address Research**

Starting at the Etherscan.io main page, you can search an address in its search function and pull up a profile page for the address.

![](https://www.secjuice.com/content/images/2024/06/image-4.png)

At the top of the page we see the address’s Eth balance, the token holdings, and on the right under “Multi Chain,” it shows that the address is used (by the same owner) on 11 different block chains.

![](https://theosintguide.com/wp-content/uploads/2024/02/ac4b8-image.png?w=1024)

Under token holdings, we see the address holds $4,547 worth of tokens, with six kinds of tokens. Clicking the pulldown menu shows the 6 kinds of tokens, including NFTs and ERC-20 tokens. This is a more complicated subject, but basically ERC-20 tokens are used to represent other cryptocurrencies on the Ethereum block chain.

![](https://theosintguide.com/wp-content/uploads/2024/02/42ca8-image-4.png?w=454)

Returning to the “Multi Chain“ section on the right side, you can click on “Blockscan” to pull up more detailed information on the address’s presence on other blockchains.

This opens a page on Blockscan.com showing each block chain with the address and a link to blockchain explorers for each of those chains. The links open the specific address’s profile page with each blockchain explorer website.

There is also a tab showing all of the address’s transactions on each blockchain mixed together in chronological order.

![](https://theosintguide.com/wp-content/uploads/2024/02/848ce-image-3.png?w=1024)

Back to the main address page on etherscan.io. Lower down is a list of previous transactions. Ether transactions are identified under the “Transactions” tab

![](https://theosintguide.com/wp-content/uploads/2024/02/6c083-image-1.png?w=1024)

### **Smart Contracts**

![](https://theosintguide.com/wp-content/uploads/2024/04/0_3.webp?w=1024)

A smart contract is essentially an that works on the Ethereum blockchain. independent automated contract. Officially defined as a digital contract written as a piece of code, stored on the blockchain, and automatically executed when certain pre-established conditions are met.

Each token has its own smart contract which is on the Ethereum blockchain. These contracts are often used as the foundation for additional contracts using the same token.

Smart contracts are written in a programming code called Solidity, and when a transaction calls a contract it calls a function from the code.

A contract written to the blockchain cannot be changed, so a proxy contract allows updates to be done while keeping the first contract the same. The foundational contracts have functions or actions that can be called upon by subsequent smart contracts for the same token.

People and contracts can both create additional contracts. The new contract will have a profile page that identifies the original contract’s address and list it as the “Parent Address”.

**Transaction with Smart Contract in It**

This is what a token (in this case, an NFT) purchase transaction looks like on etherscan.io, it shows someone’s Ethereum address (“Ox7…”) interact with the smart contract used for this specific token/NFT

You see the term “From” twice. On top, the “From” refers to the Token buyer’s Ethereum address. The second usage of “From” (in the sections “ERC-1155 Tokens Transferred:”), the From address is the seller of the NFT.

![](https://theosintguide.com/wp-content/uploads/2024/02/6c0b8-image.png?w=1024)

**Investigating Smart Contracts**

Investigate a contract by looking at the Read and the Write section to see the functions / methods available.

If you pull up a contract in etherscan.io you can see every time it has been called by a transaction.

When a transaction calls a contract it calls a function from the code which we can see in the transactions list of the address.

Some basic questions to ask when investigating a smart contract are, Who owns this contract? What does the contract do? What are the Total Assets? Who is the ultimate owner / the parent address?

Whenever you are looking at a contract address page in etherscan.io, you will see the parent address listed on the same page. Keeping going up through tree of creators until you reach an address that isn’t a contract, this is the owner or creator. That is an address to a investigate. Also, when you are looking for the “parent contract,” Google the different contract addresses to see if they have names, especially the parent contract.

Search “similar” contracts (click on contract in the contract’s address page and then on the right side click where it says “more options” and choose “similar”) can be useful when you are looking at a scam contract and want to find others.

“Liquidity Pools” (check smart contracts for the method “addLiquidity”) you make a deposit into a liquidity pool and then a 2nd person swaps Ethereum for token or vice versa with a 3rd person and there is a fee charged from that transaction. You will then make money from your deposit that is being transferred.

### **Non Fungible Tokens**

![](https://www.secjuice.com/content/images/2024/06/image-6.png)

There are some basic research methods for a Non-Fungible Token (NFT).

This will avoid the deeper questions of what is an NFT. So for now we’ll use the gross oversimplification of describing an NFT as a picture with a unique ID that people buy and sell with cryptocurrency.

SIDE NOTE: A slightly less oversimplified explanation would be to say that an NFT is a unique digital asset stored on a blockchain that represents ownership or proof of authenticity of a specific item, such as art, music, or virtual real estate. Unlike cryptocurrencies like Bitcoin, NFTs are indivisible and cannot be exchanged on a one-to-one basis, making each token distinct and valuable in its own right.

Let’s get started.

For the sake of this example, let’s start with the NFT’s Token ID (a long string that is the NFT’s unique identifier). Here is a Token ID:

9961498451080298818169728249433222030914980129654055269747476883220178403329

Start at opensea.io (OpenSea is a marketplace for NFTs, other marketplaces include SuperRare, and Rarible)

Generally, you can use Opensea by simply entering a search term, including Items, collections, or account names...