---
title: Sophisticated Telegram Based Scam Designed to Fool Fragment Users
url: https://medium.com/@p05h/sophisticated-telegram-based-scam-designed-to-fool-fragment-users-7d06334db111
source: Over Security - Cybersecurity news aggregator
date: 2025-09-03
fetch_date: 2025-10-02T19:34:38.795367
---

# Sophisticated Telegram Based Scam Designed to Fool Fragment Users

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7d06334db111&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40p05h%2Fsophisticated-telegram-based-scam-designed-to-fool-fragment-users-7d06334db111&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40p05h%2Fsophisticated-telegram-based-scam-designed-to-fool-fragment-users-7d06334db111&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Sophisticated Telegram Based Scam Designed to Fool Fragment Users

[![p05h](https://miro.medium.com/v2/resize:fill:64:64/1*5qvBoGcddVWLZ8_jfmm6sA.jpeg)](/%40p05h?source=post_page---byline--7d06334db111---------------------------------------)

[p05h](/%40p05h?source=post_page---byline--7d06334db111---------------------------------------)

6 min read

·

Nov 17, 2024

--

20

Listen

Share

In the early hours of Tuesday 12th November 2024 I was checking out the listing for an auction I’m running on [Fragment](https://fragment.com/) — the marketplace which allows Telegram users to buy and sell collectable usernames and phone numbers — when all of a sudden a message popped up from a stranger asking if my username was for sale.

Press enter or click to view image in full size

![]()

@aviatora — the first and most sophisticated of many scammers to approach me regarding my Telegram username.

I replied “yes” stating that there was already a very generous bidder for it who’d kindly offered 180 TON (~$1,000 USD at time of writing). I informed them that if they would like to place a bid then they were more than welcome to do so on Fragment. Moments later they made me this offer directly in our chat:

Press enter or click to view image in full size

![]()

At more than 5x the offer I already had, it piqued my curiosity!

My existing bidder had originally approached me saying that he was representing a crypto business and that my username was one of several they needed to collect because it was in alignment with their brand. He’d provided me with all the proof I needed and walked me through the process of setting up the listing on Fragment as it was my first time selling on there. It made perfect sense as there was a clear motivation for him buying my username and I know that his organisation has deep pockets, so his kind offer didn’t seem too outlandish. On the other hand, this random Aviatora character had no clear motivation for buying my obscure username at 5x the current bid, so I instantly smelt a rat.

At first glance it seemed that the link they’d provided as proof of their bid was legitimate, but upon right clicking and inspecting the destination it was clear that it directed to a Telegram bot as opposed to Fragment’s site.

## 🚨They’d messed with the wrong guy!🚨

It was about 2am at this point but I wanted to keep them on the hook and couldn’t resist doing some digging, so I fired up Kali Linux on my VM and got to work.

The link was pointing here: [https://t.me/FragmentOffersRoBot/start?startapp={MY\_USERNAME\_FOR\_SALE}\_price\_1000](https://t.me/FragmentOffersRoBot/start?startapp=username_menelaus_trojan_price_1000) (edited out my username there)…

It looked doubly fishy as they’d capitalised that ‘B’ in ‘RoBot’ which suggests their intended username was already taken or burned from previous scamming work.

Upon clicking the link in my safe Kali security lab it loaded a Telegram Mini App.

Press enter or click to view image in full size

![]()

The interface of the Mini App closely resembling the real Fragment auction page, but with subtle differences.

In the above image you can see that the interface closely matches that of a specific username auction page on Fragment. While all the fields look broken and glitchy here, the clever thing about the extension to their URL ‘[start?startapp={MY\_USERNAME\_FOR\_SALE}\_price\_1000](https://t.me/FragmentOffersRoBot/start?startapp=username_menelaus_trojan_price_1000)' was that it actually populated all the fields correctly in their app with my username and their fantastical bid of 1,000 TON.

However, the subtle but important difference with their version was that it included that ‘Accept the offer’ button. This is not a feature of a Fragment auction. Normally, the vendor has to wait for the seven day auction period to complete before the highest bidder is awarded your username.

I can clearly see how this scam would work so well on unsuspecting users, though. Preying on peoples’ greed is a powerful technique. If you’ve already got a bid on there and someone offers you considerably more than the asking price, then suddenly you see the option to accept the offer and close the deal immediately, I’m sure many would jump at the opportunity.

### Of course, what actually happens is that you connect your TON wallet to their dodgy backend and you are instantly rinsed of all your funds. [🤦](https://emojipedia.org/person-facepalming)

## Digging Deeper

Sniffing the network traffic with Burp Suite showed me that the Mini App was being fed from this website:

[http://fragmentauctions.lol](http://fragmentauctions.lol/)

Press enter or click to view image in full size

![]()

What [http://fragmentauctions.lol](http://fragmentauctions.lol/) shows when visiting directly from a browser.

It’s since been removed and when visiting directly from a normal browser you get the standard phishing warning above.

Their site was hosted with these [Zomro](https://zomro.com/) guys currently based here (Fokkerweg 300, 1438 AN Oude Meer, Netherlands).

Press enter or click to view image in full size

![]()

The hosts of [http://fragmentauctions.lol](http://fragmentauctions.lol/)

A pretty dodgy, B-rate looking hosting company, to be honest. Started in Ukraine, so probably a haven for scams?

> Slava Ukraini, guys!

The registrant for the domain was clearly a Russian, though:

Press enter or click to view image in full size

![]()

No surprises there!

The other piece of evidence at this stage that supported the Russian origin was that from my sniffing I could see that the backend of [http://fragmentauctions.lol](http://fragmentauctions.lol/) was also talking to another site [http://mamkasubacheva.pics](http://mamkasubacheva.pics/) (which throws a 404 when you visit it directly), clearly some sort of Slavic name.

## Following the Money

Turning my attention to the TON crypto wallet that was to be on the receiving end of the scam:

<https://tonscan.org/address/UQB33wP5PbYA5kW9ClswlBF4np5AMaYW59YVRMSCGVsoMjci#tokens>

I could see that it contains around **$165,000!** spread across various tokens.

Looking at the history it seems that they aren’t being very smart about covering their tracks, though. They’re clearly using this wallet for all manner of shitcoin trading and ongoing scamming.

Where it gets interesting, is if you Google the wallet address, the first result that appears is relating to a token for a game launch on DYOR.io.

Press enter or click to view image in full size

![]()

Game Hunters token presale on DYOR (<https://dyor.io/presale/gamehunters>).

Looks like the first investor in the presale for this token was our scammer:

Press enter or click to view image in full size

![]()

I’...