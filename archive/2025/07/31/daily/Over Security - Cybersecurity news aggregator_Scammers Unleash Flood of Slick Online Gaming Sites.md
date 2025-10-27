---
title: Scammers Unleash Flood of Slick Online Gaming Sites
url: https://krebsonsecurity.com/2025/07/scammers-unleash-flood-of-slick-online-gaming-sites/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-31
fetch_date: 2025-10-06T23:54:02.984632
---

# Scammers Unleash Flood of Slick Online Gaming Sites

Advertisement

[![](/b-action1/1.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Scammers Unleash Flood of Slick Online Gaming Sites

July 30, 2025

[34 Comments](https://krebsonsecurity.com/2025/07/scammers-unleash-flood-of-slick-online-gaming-sites/#comments)

Fraudsters are flooding Discord and other social media platforms with ads for hundreds of polished online gaming and wagering websites that lure people with free credits and eventually abscond with any cryptocurrency funds deposited by players. Here’s a closer look at the social engineering tactics and remarkable traits of this sprawling network of more than 1,200 scam sites.

The scam begins with deceptive ads posted on social media that claim the wagering sites are working in partnership with popular social media personalities, such as [Mr. Beast](https://en.wikipedia.org/wiki/MrBeast), who recently launched a gaming business called **Beast Games**. The ads invariably state that by using a supplied “promo code,” interested players can claim a $2,500 credit on the advertised gaming website.

![](https://krebsonsecurity.com/wp-content/uploads/2025/07/reddit-gambwex.png)

The gaming sites all require users to create a free account to claim their $2,500 credit, which they can use to play any number of extremely polished video games that ask users to bet on each action. At the scam website gamblerbeast[.]com, for example, visitors can pick from dozens of games like **B-Ball Blitz**, in which you play a basketball pro who is taking shots from the free throw line against a single opponent, and you bet on your ability to sink each shot.

The financial part of this scam begins when users try to cash out any “winnings.” At that point, the gaming site will reject the request and prompt the user to make a “verification deposit” of cryptocurrency — typically around $100 — before any money can be distributed. Those who deposit cryptocurrency funds are soon asked for additional payments.

However, any “winnings” displayed by these gaming sites are a complete fantasy, and players who deposit cryptocurrency funds will never see that money again. Compounding the problem, victims likely will soon be peppered with come-ons from “recovery experts” who peddle dubious claims on social media networks about being able to retrieve funds lost to such scams.

KrebsOnSecurity first learned about this network of phony betting sites from a Discord user who asked to be identified only by their screen name: “**Thereallo**” is a 17-year-old developer who operates multiple Discord servers and said they began digging deeper after users started complaining of being inundated with misleading spam messages promoting the sites.

“We were being spammed relentlessly by these scam posts from compromised or purchased [Discord] accounts,” Thereallo said. “I got frustrated with just banning and deleting, so I started to investigate the infrastructure behind the scam messages. This is not a one-off site, it’s a scalable criminal enterprise with a clear playbook, technical fingerprints, and financial infrastructure.”

After comparing the code on the gaming sites promoted via spam messages, Thereallo found they all invoked the same API key for an online chatbot that appears to be in limited use or else is custom-made. Indeed, a scan for that API key at the threat hunting platform **Silent Push** reveals at least 1,270 recently-registered and active domains whose names all invoke some type of gaming or wagering theme.

![](https://krebsonsecurity.com/wp-content/uploads/2025/07/scambling-withdrawalerror.png)

Thereallo said the operators of this scam empire appear to generate a unique Bitcoin wallet for each gaming domain they deploy.

“This is a decoy wallet,” Thereallo explained. “Once the victim deposits funds, they are never able to withdraw any money. Any attempts to contact the ‘Live Support’ are handled by a combination of AI and human operators who eventually block the user. The chat system is self-hosted, making it difficult to report to third-party service providers.”

Thereallo discovered another feature common to all of these scam gambling sites [hereafter referred to simply as “scambling” sites]: If you register at one of them and then very quickly try to register at a sister property of theirs from the same Internet address and device, the registration request is denied at the second site.

“I registered on one site, then hopped to another to register again,” Thereallo said. Instead, the second site returned an error stating that a new account couldn’t be created for another 10 minutes.

![](https://krebsonsecurity.com/wp-content/uploads/2025/07/scambling-spinora.png)

The scam gaming site spinora dot cc shares the same chatbot API as more than 1,200 similar fake gaming sites.

“They’re tracking my VPN IP across their entire network,” Thereallo explained. “My password manager also proved it. It tried to use my dummy email on a site I had never visited, and the site told me the account already existed. So it’s definitely one entity running a single platform with 1,200+ different domain names as front-ends. This explains how their support works, a central pool of agents handling all the sites. It also explains why they’re so strict about not giving out wallet addresses; it’s a network-wide policy.”

In many ways, these scambling sites borrow from the playbook of “[pig butchering](https://krebsonsecurity.com/2022/07/massive-losses-define-epidemic-of-pig-butchering/)” schemes, a rampant and far more elaborate crime in which people are gradually lured by flirtatious strangers online into investing in fraudulent cryptocurrency trading platforms.

Pig butchering scams are typically powered by people in Asia who have been kidnapped and threatened with physical harm or worse unless they sit in a cubicle and scam Westerners on the Internet all day. In contrast, these scambling sites tend to steal far less money from individual victims, but their cookie-cutter nature and automated support components may enable their operators to extract payments from a large number of people in far less time, and with considerably less risk and up-front investment.

Silent Push’s **Zach Edwards** said the proprietors of this scambling empire are spending big money to make the sites look and feel like some fancy new type of casino.

“That’s a very odd type of pig butchering network and not like what we typically see, with much lower investments in the sites and lures,” Edwards said.

[Here is a list of all domains](https://krebsonsecurity.com/wp-content/uploads/2025/07/deduped_scambling_domains.txt) that Silent Push found were using the scambling network’s chat API.

*This entry was posted on Wednesday 30th of July 2025 02:46 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[B-Ball Blitz](https://krebsonsecurity.com/tag/b-ball-blitz/) [Beast Games](https://krebsonsecurity.com/tag/beast-games/) [Discord](https://krebsonsecurity.com/tag/discord/) [Mr. Beast](https://krebsonsecurity.com/tag/mr-beast/) [scambling](https://krebsonsecurity.com/tag/scambling/) [Silent Push](https://krebsonsecurity.com/tag/silent-push/) [Thereallo](https://krebsonsecurity.com/tag/thereallo/) [Zach Edwards](https:/...