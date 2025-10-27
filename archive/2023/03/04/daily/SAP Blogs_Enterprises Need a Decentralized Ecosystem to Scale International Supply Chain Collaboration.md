---
title: Enterprises Need a Decentralized Ecosystem to Scale International Supply Chain Collaboration
url: https://blogs.sap.com/2023/03/03/enterprises-need-a-decentralized-ecosystem-to-scale-international-supply-chain-collaboration/
source: SAP Blogs
date: 2023-03-04
fetch_date: 2025-10-04T08:37:43.336246
---

# Enterprises Need a Decentralized Ecosystem to Scale International Supply Chain Collaboration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Enterprises Need a Decentralized Ecosystem to Scal...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162102&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enterprises Need a Decentralized Ecosystem to Scale International Supply Chain Collaboration](/t5/technology-blog-posts-by-sap/enterprises-need-a-decentralized-ecosystem-to-scale-international-supply/ba-p/13562666)

![mehranshakeri](https://avatars.profile.sap.com/e/2/ide23c95e5bc2bffbc337cb9ade089f336735ef33f5a3b09863ffb4a25166448a4_small.jpeg "mehranshakeri")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[mehranshakeri](https://community.sap.com/t5/user/viewprofilepage/user-id/123043)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162102)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162102)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562666)

‎2023 Mar 03
8:43 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162102/tab/all-users "Click here to see who gave kudos to this post.")

1,661

* SAP Managed Tags
* [Blockchain](https://community.sap.com/t5/c-khhcw49343/Blockchain/pd-p/774381146224104075682835994387196)

* [Blockchain

  Topic](/t5/c-khhcw49343/Blockchain/pd-p/774381146224104075682835994387196)

View products (1)

Fifteen years after Bitcoin's white paper[[1]](#_ftn1), there’s still so much noise, uncertainty, and no enterprise adoption. Blockchain, DLT, DeFi, NFT, SSI, and so many other concepts are lingering between being a mere buzzword or the future of the enterprise.

In this article, I would like to share our learnings by highlighting two major and mostly overlooked impediments hindering enterprise adoption of decentralized ecosystems. These impediments remind us why software solutions are relevant for enterprise challenges. I will also share a problem that can be addressed by a decentralized approach today and propose a solution. Ultimately, I want to invite interested individuals and parties to collaborate and realize it.

## Impediments

### Importance of Requirements and Features Compatibility

Since everything started with Bitcoin, let's begin with requirements that influenced Bitcoin's architecture. Bitcoin is a peer-to-peer online payment system with no intermediary. It's been used as a reference to trade other goods and services without borders. Being an online payment system made Bitcoin a global store of value[[2]](#_ftn2) and influenced its security requirements.

"No intermediary" means no trusted coordinator, and trust comes from the reputation of an identity. Bitcoin has **no assumptions about reputation** of participants. Reputation is "quality seen or judged by people." In other words, we *judge* someone's *future* behaviour based on their *past*. Since we can't see and judge every single participant in a global peer-to-peer network, making decisions based on their past will be infeasible and a wrong expectation. Think of a global store of value managed based on reputation. It means its security is tied to the reputation of the operators. Reputation can change, but changing a global payment system because of operators’ reputation change will be burning an unsustainable global store of value.[[3]](#_ftn3) A **sustainable global** payment solution allows international participation and should live forever.

Thus, Bitcoin's choice of proof-of-work[[4]](#_ftn4) – a technical solution to verify that computation has been done correctly – rescues network security from relying on reputation. The computation would generate a block **randomly** every 10min. No matter how many valid blocks a participant has generated in the past, they must put in the same effort as others to develop a new one, again and again.

Not relying on reputation unlocks other important features. Disagreements can be solved **without** **manual interventions** by accepting the longest chain, as a rule, coded in the network. Block generation reward incentivizes contributions to the network's security without judging the contributor, which is the most inclusive form of expanding the Bitcoin community.

But Bitcoin is just a number assigned to a string compared to what humans are capable of. Our world is built on top of identity and reputation because it's impossible to code all human interactions – at least today :). That's also why our real world can't be fully automated.

Enterprises strive to scale. Complex (but intelligent and flexible) humans that **can't be automated** should be trusted to simplify processes before scaling starts. And reputation is a tool to build that trust.

People who don't have enough exposure to either decentralized or enterprise worlds tend to force tools or features from one world to another. Some think the global supply chain must be written on their blockchain! Some expect a decentralized network to provide instant finality and 1000s of transactions per second! Some believe they must know everyone in a peer-to-peer network before using it! Some even think bringing reputation from enterprise in a peer-to-peer network is the solution to global scalability of blockchain solutions!

### Too Many Networks

As there is only one internet, there can't be 1000s of networks to onboard enterprises.

To lower the risk of buying into a soon obsolete network and to avoid the cost of adopting many, enterprises wait till the space is consolidated. Or they might bootstrap their network and expect their competitors to join! Or similar reasonably selfish behaviours which worsen the situation. This feeds a vicious cycle of increasing networks that makes the matter even more complicated and slows any adoption.

On the other hand, those enterprises expecting a decentralized network as a middle ground to collaborate with competitors are willing to participate in network operation (by running a full node) to ensure its neutrality. With many networks, guaranteeing the neutrality of all might require running 1000s of nodes from 1000s of networks making collaboration unreasonably costly. Furthermore, bridging those networks via a central or peer-to-peer integration will be infeasible and not scalable globally*.*

An enterprise expects to be in one network with all its n-tier international supply chain partners. Bootstrapping a new network per application, per group of companies, or even per country won't scale.

##

## Relevant Enterprise Challenges

Enterprises need digital solutions to scale. Automation would be the very primitive expectation from software to improve efficiency and facilitate global scalability. Existing solutions, let it be an Excel file or a sophisticated ERP system, at the most address the challenges of a single business. However, today's supply chain is an intertwined global network with complex issues that can be tackled only by collaborating with all supply chain participants. This collaboration is prolonged and limited due to preferred com...