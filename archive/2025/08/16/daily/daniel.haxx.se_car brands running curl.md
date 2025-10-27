---
title: car brands running curl
url: https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/
source: daniel.haxx.se
date: 2025-08-16
fetch_date: 2025-10-07T00:48:09.093331
---

# car brands running curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2018/08/mercedes-1737917_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# car brands running curl

[August 15, 2025](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [7 Comments](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/#comments)

Seven years ago I wrote about how [a hundred million cars were running curl](https://daniel.haxx.se/blog/2018/08/12/a-hundred-million-cars-run-curl/) and as I brought up this blog post in a discussion recently, I came to reflect over how the world might have changed since. *Is curl perhaps used in more cars now?*

Yes it is.

With the help of friendly people on Mastodon, and a little bit of Googling, the current set of car brands known to have cars running curl contains **47** names. Most of the world’s top brands:

**Acura, Alfa Romeo, Audi, Baojun, Bentley, BMW, Buick, Cadillac, Chevrolet, Chrysler, Citroen, Dacia, Dodge, DS, Fiat, Ford, GMC, Holden, Honda, Hyundai, Infiniti, Jeep, Kia, Lamborghini, Lexus, Lincoln, Mazda, Mercedes, Mini, Nissan, Opel, Peugeot, Polestar, Porsche, RAM, Renault, Rolls Royce, Seat, Skoda, Smart, Subaru, Suzuki, Tesla, Toyota, Vauxhall, Volkswagen, Volvo**

I think it is safe to claim that curl now runs in several hundred million cars.

## How do we know?

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/04/volvo-xc40-recharge.jpg)

The curl license seen in a Volvo

This is based on curl or curl’s copyright being listed in documentation and/or shown on screen on the car’s infotainment system.

The manufacturers need to provide that information per the curl license. Even if some of course still don’t.

## Some brands are missing

For brands missing in the list, we don’t know their status. There are many more car brands that we can suspect *probably* also run and use curl, but for which we have not found enough evidence for it. If you do, please let me know!

## What curl are the running?

These are all using libcurl, not the command line tool. It is not uncommon for them to run fairly old versions.

## What are they using curl for?

I can’t tell for sure as they don’t tell me. Presumably though, a modern care does a lot of Internet transfers for all sorts of purposes and curl is a reliable library for doing that. Download firmware images, music, maps or media. Upload statistics, messages, high-scores etc. Modern cars are full-blown computers plus mobile phones combined, of course they transfer data.

## Brands, not companies

The list contains 47 brands right now. They are however manufactured by a smaller number of companies, as most car companies sell cars under multiple different brands. So maybe 15 car companies?

Additionally, many of these companies buy their software from a provider who bundles it up for them. Several of these companies probably get their software from the same suppliers. So maybe there is only 7 different ones?

I have still chosen to list and talk about the *brands* because those are the consumer facing names used in everyday conversations, and they are the names we mere mortals are most likely to recognize.

## Not a single sponsor or customer

Ironically enough, while curl runs in practically almost every new modern car that comes out from factories, not a single of the companies producing the cars or the software they run, are sponsors of curl or customers of curl support. Not one.

## An Open Source sustainability story in two slides

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/08/giants-standing-on-the-shoulders-of3.jpg)

47 car brands using curl

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/08/giants-standing-on-the-shoulders-of1.jpg)

car brands sponsoring or paying for curl support

## Yes they are allowed to

We give away curl for free for everyone to use at no cost and there is no obligation for anyone to pay anyone for this. These companies are perfectly in their rights to act like this.

You could possibly argue that companies should think about their own future and make sure that dependencies they rely on and would like to keep using, also survive so that they can keep depending on these components going forward as well. But obviously that is not how this works.

curl is liberally licensed under [an MIT-like license](https://everything.curl.dev/source/opensource/license.html).

## What to do

I want curl to remain Open Source and I really like providing it in a way, under a liberal license, that makes it possible to get used everywhere. I mean, if we use the measurement of how widely used a software is, I think we can agree that curl is a top candidate.

I would like the economics and financials around the curl project to work out *anyway*, but maybe that is a utopia we can never reach. Maybe we eventually will have to change the license or something to *entice* or force a different behavior.

[cars](https://daniel.haxx.se/blog/tag/cars/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous PostHTTP is not simple](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/)[Next PostAI slop attacks on the curl project](https://daniel.haxx.se/blog/2025/08/18/ai-slop-attacks-on-the-curl-project/)

## 7 thoughts on “car brands running curl”

1. ![](https://secure.gravatar.com/avatar/19d28ec2e52f72b9a3b389229f03e0f4406b6b05584ff8c10166c0165a1da310?s=34&d=monsterid&r=g) **George** says:

   [August 15, 2025 at 08:37](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/#comment-27310)

   What do you think? curl or SQLite is used more in various hardware?

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [August 15, 2025 at 08:56](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/#comment-27311)

      @George: it is impossible to say. Both run in many billions of devices.
2. ![](https://secure.gravatar.com/avatar/d7c7334eaa6f9e3319f673c1fa60996b7ea6274092009844cabf60bee4cb43b7?s=34&d=monsterid&r=g) **[Julian Schregle](https://opensource.mercedes-benz.com/)** says:

   [August 15, 2025 at 15:22](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/#comment-27312)

   It is important to discuss the financial situation of free and open-source projects because many FOSS developers are unsung heroes: they develop high-quality software components that provide fundamental functions for our digital world, yet often remain in the background. At Mercedes-Benz, we rely on Free and Open Source Software and recognize our responsibility. For several years, we have supported a variety of FOSS projects nominated by our employees via GitHub Sponsors, and we have received a lot of positive feedback for this. In the first round, we financially supported cURL, as shown on cURL’s GitHub Sponsors page and on ours. As in previous years, we will again support selected FOSS projects this year and are excited to see which projects our colleagues will nominate.
3. ![](https://secure.gravatar.com/avatar/b7ed4e10fd258944ad4c44b2e81c951271ef049b99d6fd641b9197170bda3297?s=34&d=monsterid&r=g) **Tjark** says:

   [August 15, 2025 at 15:35](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/#comment-27313)

   Hi Daniel,

   I work for one of the car brands you mentioned (Mercedes-Benz) and these kinds of posts honestly hurt me a bit.

   Our industry should give ba...