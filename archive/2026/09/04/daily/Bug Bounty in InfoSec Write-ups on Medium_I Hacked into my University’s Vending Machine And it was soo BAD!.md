---
title: I Hacked into my University’s Vending Machine And it was soo BAD!
url: https://infosecwriteups.com/i-hacked-into-my-universitys-vending-machine-and-it-was-soo-bad-c411c2b968f4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-09-04
fetch_date: 2026-09-05T06:29:03.904241
---

# I Hacked into my University’s Vending Machine And it was soo BAD!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-hacked-into-my-universitys-vending-machine-and-it-was-soo-bad-c411c2b968f4&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-hacked-into-my-universitys-vending-machine-and-it-was-soo-bad-c411c2b968f4&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c411c2b968f4-----------------------------------------)

·

1. [How it works](/?source=post_page-----c411c2b968f4-----------------------------------------#f9f7 "How it works")
2. [Don’ts and Don’ts](/?source=post_page-----c411c2b968f4-----------------------------------------#3e39 "Don’ts and Don’ts")
3. [Hardcoded username and password](/?source=post_page-----c411c2b968f4-----------------------------------------#f950 "Hardcoded username and password")
4. [Rate limiting](/?source=post_page-----c411c2b968f4-----------------------------------------#922c "Rate limiting")
5. [The interesting part](/?source=post_page-----c411c2b968f4-----------------------------------------#6e2e "The interesting part")
6. [Responsible disclosure](/?source=post_page-----c411c2b968f4-----------------------------------------#4aa1 "Responsible disclosure")
7. [So what did I actually learn?](/?source=post_page-----c411c2b968f4-----------------------------------------#2263 "So what did I actually learn?")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c411c2b968f4-----------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

[Hacker](https://medium.com/tag/hacker?source=post_page---header_tags--c411c2b968f4-----------------------------------------)

[Software Development](https://medium.com/tag/software-development?source=post_page---header_tags--c411c2b968f4-----------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--c411c2b968f4-----------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page---header_tags--c411c2b968f4-----------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--c411c2b968f4-----------------------------------------)

# I Hacked into my University’s Vending Machine And it was soo BAD!

[![Amogh V K](https://miro.medium.com/v2/resize:fill:64:64/1*7TVG4o5BkE12WNIIGXa8Zw.jpeg)](https://medium.com/%40amogh.vk.2005?source=post_page---byline--c411c2b968f4-----------------------------------------)

[Amogh V K](https://medium.com/%40amogh.vk.2005?source=post_page---byline--c411c2b968f4-----------------------------------------)

6 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc411c2b968f4&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-hacked-into-my-universitys-vending-machine-and-it-was-soo-bad-c411c2b968f4&source=---header_actions--c411c2b968f4---------------------post_audio_button--------------------)

Share

Okay some time ago i hacked into the vending machine which is in MIT-BLR ( *J Vend* ) iykyk, which now I’m opening it to everyone.

Before I begin Im not here to leak the apk also not here to say HOW I DID IT coz it will definitely cause me trouble ( Though i didnt exploit it myself as its againt my principles) but I can give you hints how you can do it.

I’ve seen people say they tired and they failed it’s just that they suck at it that’s all. took me a few weeks to figure it out found a shit load of vulnerabilities \* aka its worse than a vibe coded app \*

I mean who in the world just puts their auth key, user name and password hardcoded into the front end? like seriously dude? its in prod!!!!

but for the first time I thought about being a soo called *Responsible Citizen* i.e keeping it private and I mailed the company and its founders, and guess what?

*NO REPLY*

So I thought..

fine.

If you won’t listen to me privately, let’s talk publicly.

Soo why am I posting this?

I think that Hacking is bad, *I guess*? but what ever listing out vulnerability isn’t.

Soo imma give all my findings and lets see who gets there first

## How it works

from the TOP you log in via google mail
 ↓
You get assigned a user ID where all the orders and history is stored
 ↓
you place an item to cart and order ID is assigned and you press pay
 ↓
the server send the item price from the DB to the app aka hard( Im not shitting devs that’s how bad the design is )
 ↓
and the app fires Razorpay with that money
 ↓
you pay and when its sucessful and the back-end verifies the you click vend and the item vends.

Press enter or click to view image in full size

![]()

as you can see i perm chnaged the cart value to rs. 1 irrespective of the cart value it fetches rs. 1 and razor pay asks me to pay rs. 1

and this is how the rs. 1 hack looks inside the app

then the main scrutiny starts. the server fetches the db price with the order id and the amount payed, if razor pay amount you paid associated with the order id is == the product price in DB, wallah the server fires GET myorder.php?… the motor in the vending machine and it vends or else it dosent.

now let’s get into the fun part a test for you if you know any thing about true hacking.

## Don’ts and Don’ts

it’s purposeful btw not a typo

here is how a regular human things,

1. I will try to skip payment
2. I will try to change the amount before it reaches the razorpay
3. I will reuse the payment ID or order ID to vend multiple times
4. I will force trigger the motor to vend.
5. I will force refund
6. I will fordge the Razorpay signature to pay less and show more ( try it if you wanna end up in jail )

If this came into your mind even after reading the first half this isn’t for you. better luck trying for the next decade.

Now I will list the true vulnerability.

## Hardcoded username and password

Press enter or click to view image in full size

![]()

well well look at this idk if you can see but lmao

Where does it fit in?

yep.

*/phpmyadmin*

Press enter or click to view image in full size

![]()

Tho it sounds easy it isn’t.

Obv the user has changed the password and now we need to find if the user actually exists.

How do we find out?

my boy SQL INJECTION will help.

And yes, this is where things start getting interesting.

I found that the application had exposed information that should absolutely not have been exposed to the client.

Using CVE-2017–1000017 The acess was denied for the hardcoded username with password:yes, i...