---
title: Taking over a Dead IoT Company
url: https://blog.kchung.co/taking-over-a-dead-iot-company/
source: Kevin Chung
date: 2023-01-10
fetch_date: 2025-10-04T03:26:26.048948
---

# Taking over a Dead IoT Company

[Kevin Chung](https://blog.kchung.co)

* [Home](https://blog.kchung.co)
* [Github](https://github.com/ColdHeat)
* [Twitter](https://twitter.com/kchungco)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[electronics](/tag/electronics/)

 Featured

# Taking over a Dead IoT Company

5 years after NYCTrainSign collapsed, I investigate why the company failed and end up writing an exploit to take over their fleet.

* [![Kevin Chung](/content/images/size/w100/2021/04/kchung.jpg)](/author/kchung/)

#### [Kevin Chung](/author/kchung/)

Jan 9, 2023
• 15 min read

![Taking over a Dead IoT Company](/content/images/size/w2000/2023/01/pikachu.png)

💡

Do you have a sign from NYCTrainSign? Try out [the site that I created](https://www.trainsignapi.com/) to get it working again.

Back in 2017, NYCTrainSign was a company making replicas of the countdown timers that told you how long it would be until the next train came.

![](https://blog.kchung.co/content/images/2023/01/train-sign-wsj.png)

New York City Subway Arrival Clock. Image Credit: [Wall Street Journal](https://www.wsj.com/articles/mta-board-approves-26-billion-capital-spending-plan-1446052998)

But instead of being hung up on the ceiling, you could put it on your desk as a tasteful part of your home.

The person responsible for marketing did a great job driving interest. I remember a lot of Facebook and Instagram posts showing off how the sign could be useful for cafes and pizzerias so their customers could see when they should leave for the train.

However, underneath the veneer of Instagram, the signs were full of subpar engineering and unsustainable costs.

In early 2018 the company stopped replying to social media posts and very few people had received their purchased signs. The company recommended that customers dispute the charge to try to get their money back.

Today, even new companies entering this space have had to deal with the fallout of NYCTrainSign.

![](https://blog.kchung.co/content/images/2023/01/fallout1-1.png)

![](https://blog.kchung.co/content/images/2023/01/fallout2-1.png)

![](https://blog.kchung.co/content/images/2023/01/fallout3-1.png)

![](https://blog.kchung.co/content/images/2023/01/fallout4-1.png)

Now, 5 years after the company collapsed, I acquired one of their signs to investigate why the company failed. Along the way I ended up taking over the company’s sign control domain and writing an [exploit](https://github.com/ColdHeat/nycts-api) to get full control of any signs still in the field.

# Getting a Sign

Sometime in 2021 I found someone on reddit that was selling a NYCTrainSign. They were one of the few who had received product from the company and were looking to get rid of it.

![](https://blog.kchung.co/content/images/2023/01/reddit-dm.png)

Amazingly, the original owner kept the original packaging.

![](https://blog.kchung.co/content/images/2023/01/IMG_0298.jpeg)

The Original Box

![](https://blog.kchung.co/content/images/2023/01/IMG_0299.jpeg)

The Sign

![](https://blog.kchung.co/content/images/2023/01/IMG_0304.jpeg)

The Sign Powered On

# Disassembly

The sign itself is housed in a wooden case that the company handmade. I believe the company had hired a woodworker out of college to make the cases.

![](https://blog.kchung.co/content/images/2023/01/IMG_0301.jpeg)

Rear Panel of the sign. Unclear what the hole was for.

As someone with little to no woodworking skills, the case looks pretty good. There are some bad corners but it wouldn’t look out of place in any home.

The sign internally was comprised of

* 2 LED Matrix Panels
* 1 Raspberry Pi 3
* 1 4GB MicroSD Card
* 1 LED Matrix HAT from Adafruit
* Wiring for the power supply connection
* Wiring for the LED Matrix Panels
* A small button wired to GPIO on the Pi

![](https://blog.kchung.co/content/images/2023/01/IMG_0302.jpeg)

Sign Internals. Notice the random tape and disconnected power cable.

While the case is fine, internally it shouldn’t take much to tell that the sign is not that well made.

The Pi was only half screwed on by two loose screws. The button (intended for reset) was sort of just hanging around. There’s also a giant hole for some unknown reason. The power supply connection seems like it could break with too much movement and it was actually unplugged when I first got the sign.

# The BOM is Too Damn High

A bill of materials or BOM is a list of the raw components that go into a product. Most electronics projects, especially serious ones, will have a detailed BOM that describes the item and price that it goes for.

Often the final cost of the BOM will be much lower than the retail price because of the cost of shipping, R&D, profit margin, etc. Small changes in BOM price can have a big impact on the final cost of an item. It’s not uncommon to switch vendors or parts to save just cents on the BOM.

One trick I use is that multiplying the BOM cost by 4 will often get you the retail price.

With access to a sign we can put together a hypothetical BOM:

* Raspberry Pi 3 - $35
* Adafruit LED Matrix Hat - $25
* LED Matrix \* 2 - $60 ($30 each at least)
  + One of their [tweets](https://twitter.com/NYCTRAINSIGN/status/926106932573810688) specifically cite using a specific more expensive Adafruit component (<https://www.adafruit.com/product/2278>).
* 5V 2A Power Supply - $5 (Best Guess)
  + Suspiciously this is not enough amperage to power everything at full power draw. Most guides recommend 4 to 10 amps.
* 4GB MicroSD Card - $7 (Best Guess)
* Wood Case - $15 (Best Guess)
* Miscellaneous Items
  + Wiring, Buttons, Cabling, Screws, Packaging (the sign had some cardboard, a sheet of paper, and some bubble wrap and foam) - $3 (Best Guess)

So roughly the BOM cost was $150. If we were to apply our pricing trick, the suggested retail price should be at least $600.

# They did not know the trick

Based on [archived webpages](https://web.archive.org/web/20170902053604/https%3A//nyctrainsign.com/) the NYCTrainSign team was selling signs for $600 but there are [articles mentioning prices like $300](https://ny.curbed.com/2017/10/6/16436064/nyc-train-sign-bushwick-startup-tech). Some people mention [purchases for around $200](https://www.amny.com/news/nyc-train-sign-complaints-1-18558431/) and even [only paying $100](https://www.facebook.com/nyctrainsign/photos/a.1771806073074982/2031239807131606/?comment_id=2071473833108203&__cft__[0]=AZU6tK-HrTSI1jF7QHCR2eeXREEUPpIh_EYb_XDtjF6ZOjAdpfnfXk87Hs0fZXwpWfHSimw1NUOWkzgaphiGKZ4IycHiVW3PzYpKFKsnPn3OjQY-ShjmRT6CuqF_pVnPURORwn3Ghe1m3bvHs-RGnlFVoktnyHH4P4-tp-LuRIjrqWUihkU1e96agSetL8l_hFA&__tn__=R]-R).

![](https://blog.kchung.co/content/images/2023/01/300-pricing.png)

Considering the BOM costs, $299 is practically a steal

It seems there were also plans to rent the signs at $30/month as well.

$300 is obviously too low of a price based on the BOM but yet $600 is probably too much. It’s just a sign after all.

Renting could have been an interesting idea but I think it would be very difficult to recoup the initial cash investment. Hardware businesses often need to have an initial cash injection to build inventory and then want to recoup that cash and gather profit as quickly as possible by selling their product.

# Who Sold The Shovels

There is a saying that "during a gold rush, you should sell shovels".

In our tale, Adafruit sold the shovels. By using the [Adafruit LED Matrix HAT](https://www.adafruit.com/product/2345), the BOM cost gets inflated by $25 or about 20%. The HAT is also entirely avoidable with a little engineering work.

![](https://blog.kchung.co/content/images/2023/01/image.png)

The shovel in question

This is because:

1. The HAT is not absolutely necessary. The [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library used by the sign includes [direct wiring instructions](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md) and designs for a [passive adapter board](https://github.com/hzeller/rpi-rgb-led-matrix/...