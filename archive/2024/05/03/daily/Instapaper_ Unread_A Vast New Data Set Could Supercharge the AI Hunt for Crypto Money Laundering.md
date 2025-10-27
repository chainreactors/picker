---
title: A Vast New Data Set Could Supercharge the AI Hunt for Crypto Money Laundering
url: https://www.wired.com/story/ai-crypto-tracing-model-money-laundering/
source: Instapaper: Unread
date: 2024-05-03
fetch_date: 2025-10-06T17:17:13.348465
---

# A Vast New Data Set Could Supercharge the AI Hunt for Crypto Money Laundering

[Skip to main content](#main-content)

Menu

[![Wired](/verso/static/wired-us/assets/logo.svg)](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[![Wired](/verso/static/wired-us/assets/logo.svg)](/)

Account

Account

[Newsletters](/newsletter?sourceCode=navbar)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=navbar)

[Podcasts](/podcasts/)

[Video](/video/)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Fai-crypto-tracing-model-money-laundering%2F&source=VERSO_NAVIGATION)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Fai-crypto-tracing-model-money-laundering%2F&source=VERSO_NAVIGATION)

[Andy Greenberg](/author/andy-greenberg/)

[Security](/category/security)

May 1, 2024 9:00 AM

# A Vast New Data Set Could Supercharge the AI Hunt for Crypto Money Laundering

Blockchain analysis firm Elliptic, MIT, and IBM have released a new AI model—and the 200-million-transaction dataset it's trained on—that aims to spot the “shape” of bitcoin money laundering.

![Ladder coming out of a Bitcoin logo](https://media.wired.com/photos/6631a1936dc0c77846852ed5/3:2/w_2560%2Cc_limit/Crypto-Money-Laundering-Security-GettyImages-1543076825.jpg)

Illustration: rob dobi/Getty Images

Save StorySave this story

Save StorySave this story

One task where [AI](https://www.wired.com/story/guide-artificial-intelligence/) tools have proven to be particularly superhuman is analyzing vast troves of data to find patterns that humans can't see, or automating and accelerating the discovery of those we can. That makes [Bitcoin's](https://www.wired.com/tag/bitcoin/) blockchain, a public record of nearly a billion transactions between pseudonymous addresses, the perfect sort of puzzle for AI to solve. Now, a new study—along with a vast, newly released trove of crypto crime training data—may be about to trigger a leap forward in automated tools' ability to suss out illicit money flows across the Bitcoin economy.

On Wednesday, researchers from cryptocurrency tracing firm Elliptic, MIT, and IBM [published a paper](https://www.elliptic.co/blog/our-new-research-enhancing-blockchain-analytics-through-ai) that lays out a new approach to finding money laundering on Bitcoin's blockchain. Rather than try to identify cryptocurrency wallets or clusters of addresses associated with criminal entities such as dark-web black markets, thieves, or scammers, the researchers collected patterns of bitcoin transactions that led from one of those known bad actors to a cryptocurrency exchange where dirty crypto might be cashed out. They then used those example patterns to train an AI model capable of spotting similar money movements—what they describe as a kind of detector capable of spotting the “shape” of suspected money laundering behavior on the blockchain.

Now, they're not only releasing an experimental version of that AI model for detecting bitcoin money laundering but also publishing the training data set behind it: a 200-million transaction trove of Elliptic's tagged and classified blockchain data, which the researchers describe as the biggest of its kind ever to be made public by a thousandfold. “We're providing about a thousand times more data, and instead of labeling illicit wallets, we're labeling examples of money laundering which might be made up of chains of transactions,” says Tom Robinson, Elliptic's chief scientist and cofounder. “It's a paradigm shift in the way that blockchain analytics is used.”

Blockchain analysts have used machine learning tools for years to automate and sharpen their tools for tracing crypto funds and identifying criminal actors. In 2019, in fact, Elliptic already partnered with MIT and IBM to [create a AI model for detecting suspicious money movements](https://arxiv.org/abs/1908.02591) and released a much smaller data set of around 200,000 transactions that they had used to train it.

For this new research, by contrast, the same team of researchers took a much more ambitious approach. Rather than try to classify single transactions as legitimate or illicit, Elliptic analyzed collections of up to six transactions between Bitcoin address clusters it had already identified as illicit actors and the exchanges where those previously identified shady entities sold their crypto, positing that the patterns of transactions between criminals and their cashout points could serve as examples of money laundering behavior.

Working from that hypothesis, Elliptic assembled 122,000 of these so-called subgraphs, or patterns of known money laundering within a total data set of 200 million transactions. The research team then used that training data to create an AI model designed to recognize money laundering patterns across Bitcoin's entire blockchain.

As a test of their resulting AI tool, the researchers checked its outputs with one cryptocurrency exchange—which the paper doesn't name—identifying 52 suspicious chains of transactions that had all ultimately flowed into that exchange. The exchange, it turned out, had already flagged 14 of the accounts that had received those funds for suspected illicit activity, including eight it had marked as associated with money laundering or fraud, based in part on know-your-customer information it had requested from the account owners. Despite having no access to that know-your-customer data or any information about the origin of the funds, the researchers' AI model had matched the conclusions of the exchange's own investigators.

Correctly identifying 14 out of 52 of those customer accounts as suspicious may not sound like a high success rate, but the researchers point out that only 0.1 percent of the exchange's accounts are flagged as potential money laundering overall. Their automated tool, they argue, had essentially reduced the hunt for suspicious accounts to more than one in four. “Going from ‘one in a thousand things we look at are going to be illicit’ to 14 out of 52 is a crazy change,” says Mark Weber, one of the paper's coauthors and a fellow at MIT's Media Lab. “And now the investigators are actually going to look into the remainder of those to see, wait, did we miss something?”

Elliptic says it's already been privately using the AI model in its own work. As more evidence that the AI model is producing useful results, the researchers write that analyzing the source of funds for some suspicious transaction chains identified by the model helped them discover Bitcoin addresses controlled by a Russian dark-web market, a cryptocurrency “mixer” designed to obfuscate the trail of bitcoins on the blockchain, and a Panama-based Ponzi scheme. (Elliptic declined to identify any of those alleged criminals or services by name, telling WIRED it doesn't identify the targets of ongoing investigations.)

Perhaps more important than the practical use of the researchers' own AI model, however, is the potential of Elliptic's training data, which the researchers have [published](https://www.kaggle.com/organizations/ellipticco) on the Google-owned machine learning and data science community site Kaggle. “Elliptic could have kept this for themselves,” says MIT's Weber. “Instead there was very much an open source ethos here of contributing something to the community that will allow everyone, even their competitors, to be better at anti-money-laundering.” Elliptic notes that the data it released is anony...