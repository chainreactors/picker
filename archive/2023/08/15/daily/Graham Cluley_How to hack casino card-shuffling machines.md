---
title: How to hack casino card-shuffling machines
url: https://www.bitdefender.com/blog/hotforsecurity/how-to-hack-casino-card-shuffling-machines/
source: Graham Cluley
date: 2023-08-15
fetch_date: 2025-10-04T12:04:15.048925
---

# How to hack casino card-shuffling machines

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

min read

# How to hack casino card-shuffling machines

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

August 14, 2023

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![How to hack casino card-shuffling machines](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2023/08/cards.jpeg "How to hack casino card-shuffling machines")

Security researchers have demonstrated how they were able to exploit a flaw which allowed them to hack the card-shuffling devices used in casinos and poker rooms.

The "Official Shuffler of the World Series of Poker", the DeckMate 2, came under the scrutiny of researchers from IOActive who wanted to find out if it contained vulnerabilities which could help somebody cheat in a game of cards.

To understand why the DeckMate 2 became the focus of attention, one has to know a little background on a recent controversy which flared up in the world of livestreamed poker on 29 September 2022.

As *Brobible* [describes](https://brobible.com/sports/article/garrett-adelstein-robbi-jade-lew-poker-cheating-allegations-scandal-explained/), a high-stakes poker game saw [a shock win of a seemingly poor hand](https://twitter.com/HCLPokerShow/status/1575668051948687360) by Robbi Jade Lew over Garrett Adelstein - raising accusations of cheating.

A subsequent [investigation](https://hustlercasinolive.com/j4report/) failed to find any credible evidence of wrongdoing.

But one of the investigation's conclusions made the researchers at IOActive raise an eyebrow:

> "The Deckmate shuffling machine is secure and cannot be compromised"

A claim like that heard by a vulnerability researcher is like a red flag to a bull, and this week IOActive's experts presented their the results of a months-long investigation into the security of the automated shuffling machine used in casinos worldwide.

![](https://blogapp.bitdefender.com/hotforsecurity/content/images/2023/08/deckmate2-1.jpeg)

The most recent version of the DeckMate, the DeckMate 2 released in 2012, has a number of impressive features.  Not only can it shuffle a deck of cards in just 22 seconds, but it also boasts a built-in camera which can ensure that every card is present in deck of cards before the deck is played.

New DeckMate 2 devices cost more than $20,000 and are not supposed to be available for purchase without a gaming license.  However, the researchers were able to get their hands on a second-hand DeckMate 2 and discovered it had an exposed USB port.

As the researchers [described to *Wired*](https://www.wired.com/story/card-shuffler-hack/), and in a [presentation](https://www.blackhat.com/us-23/briefings/schedule/index.html#shuffle-up-and-deal-analyzing-the-security-of-automated-card-shufflers-31741) at the BlackHat conference in Las Vegas, plugging a small device into the USB port could interfere with the DeckMate 2's operation.

Specifically, they found they could alter the firmware on the card-shuffling machine, gaining access to its internal camera in order to learn the order of the entire deck in real-time and transmit it via Bluetooth to a nearby phone.

It's easy to imagine how information about the order of the cards that were being dealt could be transmitted to a member of the audience, who could then send coded signals to the cheating player.

Although IOActive's research did not find a technique that would force the DeckMate to sort cards into a particular order, the researchers felt that would be possible if they had had more time to look into it.

Joseph Totaro, one the research team, told *Wired* that the technique would be particularly powerful if someone wanted to cheat at Texas Hold'em poker - the variant of poker being played in the controversial hand by Robbi Jade Lew over Garrett Adelstein. However, there is no suggestion that the DeckMate was compromised on that occasion.

And, of course, you would need nerves of steel to pull off a hack like this in a real casino, surrounded by hundreds of people and thousands of security cameras, rather than in a test laboratory.

tags

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

---

### Author

---

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=150&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[## Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s.

[View all posts](/en-us/blog/hotforsecurity/author/gcluley)

---

## Right now Top posts

[![Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/06/header-1.jpg "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")](/en-us/blog/hotforsecurity/beyond-free-antivirus-5-reasons-full-strength-protection "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")[Digital Privacy](/en-us/blog/hotforsecurity/tag/digital-privacy "Digital Privacy")[Tips and Tricks](/en-us/blog/hotforsecurity/tag/tips-and-tricks "Tips and Tricks")[How to](/en-us/blog/hotforsecurity/tag/how-to "How to")

[### Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices](/en-us/blog/hotforsecurity/beyond-free-antivirus-5-reasons-full-strength-protection "Beyond Free Antivirus: 5 Reasons Smart Consumers Choose Full-Strength Protection for Their Devices")

June 12, 2025

min read

[![Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/05/movie-theater-2093264_1920.jpg "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")](/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")

[Threats](/en-us/blog/hotforsecurity/tag/threats "Threats")

[### Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer](/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent "Fake Download of Mission: Impossible – The Final Reckoning Movie Deploys Lumma Stealer")

May 23, 2025

min read

[![Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w300/2025/05/interior-design-8922413_1920--1-.jpg "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")](/en-us/blog/hotforsecurity/scammers-sell-steam-accounts-games "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")

[Scam](/en-us/blog/hotforsecurity/tag/scam "Scam")

[### Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!](/en-us/blog/hotforsecurity/scammers-sell-steam-accounts-games "Scammers Sell Access to Steam Accounts with All the Latest Games – It's a Trap!")

May 16, 2...