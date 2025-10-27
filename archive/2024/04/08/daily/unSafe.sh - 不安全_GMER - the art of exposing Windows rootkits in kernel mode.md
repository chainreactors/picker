---
title: GMER - the art of exposing Windows rootkits in kernel mode
url: https://buaq.net/go-232828.html
source: unSafe.sh - 不安全
date: 2024-04-08
fetch_date: 2025-10-04T12:14:38.681836
---

# GMER - the art of exposing Windows rootkits in kernel mode

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/0d9765801c46f70f568c044cbded46c5.jpg)

GMER - the art of exposing Windows rootkits in kernel mode

*2024-4-7 22:31:14
Author: [www.reddit.com(查看原文)](/jump-232828.htm)
阅读量:27
收藏*

---

Open navigation

Go to Reddit Home

Get the Reddit app

[Log In](https://www.reddit.com/login/)Log in to Reddit

Open settings menu

* [Log In / Sign Up](https://www.reddit.com/login/)
* [Advertise on Reddit](https://ads.reddit.com?utm_source=web3x_consumer&utm_name=user_menu_cta)
* [Shop Collectible Avatars](https://www.reddit.com/avatar/shop)

### Get the Reddit app

Scan this QR code to download the app now

Or check it out in the app stores

[Go to ReverseEngineering](https://www.reddit.com/r/ReverseEngineering/)

[r/ReverseEngineering](https://www.reddit.com/r/ReverseEngineering/)

[r/ReverseEngineering](https://www.reddit.com/r/ReverseEngineering/)

A moderated community dedicated to all things reverse engineering.

---

•

[igor\_sk](https://www.reddit.com/user/igor_sk/)

ADMIN

MOD

[![](https://external-preview.redd.it/gmer-the-art-of-exposing-windows-rootkits-in-kernel-mode-v0-lIr0oRdwj_-jALOBhouG2mGkHBcFyRdk_awFtEP1H88.jpg?width=640&crop=smart&auto=webp&s=d93154e86f71dfcaa533e2051055feab79bf46e3)](https://artemonsecurity.blogspot.com/2024/04/gmer-art-of-exposing-windows-rootkits.html)[![r/ReverseEngineering - GMER - the art of exposing Windows rootkits in kernel mode](https://external-preview.redd.it/gmer-the-art-of-exposing-windows-rootkits-in-kernel-mode-v0-lIr0oRdwj_-jALOBhouG2mGkHBcFyRdk_awFtEP1H88.jpg?width=640&crop=smart&auto=webp&s=d93154e86f71dfcaa533e2051055feab79bf46e3)](https://artemonsecurity.blogspot.com/2024/04/gmer-art-of-exposing-windows-rootkits.html)

![r/ReverseEngineering - GMER - the art of exposing Windows rootkits in kernel mode](https://artemonsecurity.blogspot.com/2024/04/gmer-art-of-exposing-windows-rootkits.html)

[artemonsecurity.blogspot.com](https://artemonsecurity.blogspot.com/2024/04/gmer-art-of-exposing-windows-rootkits.html)

- &nbsp;
- &nbsp;

---

- TOPICS

- Gaming

* [Valheim](https://reddit.com/t/valheim/)
* [Genshin Impact](https://reddit.com/t/genshin_impact/)
* [Minecraft](https://reddit.com/t/minecraft/)
* [Pokimane](https://reddit.com/t/pokimane/)
* [Halo Infinite](https://reddit.com/t/halo_infinite/)
* [Call of Duty: Warzone](https://reddit.com/t/call_of_duty_warzone/)
* [Path of Exile](https://reddit.com/t/path_of_exile/)
* [Hollow Knight: Silksong](https://reddit.com/t/hollow_knight_silksong/)
* [Escape from Tarkov](https://reddit.com/t/escape_from_tarkov/)
* [Watch Dogs: Legion](https://reddit.com/t/watch_dogs_legion/)

- Sports

* [NFL](https://reddit.com/t/nfl/)
* [NBA](https://reddit.com/t/nba/)
* [Megan Anderson](https://reddit.com/t/megan_anderson/)
* [Atlanta Hawks](https://reddit.com/t/atlanta_hawks/)
* [Los Angeles Lakers](https://reddit.com/t/los_angeles_lakers/)
* [Boston Celtics](https://reddit.com/t/boston_celtics/)
* [Arsenal F.C.](https://reddit.com/t/arsenal_fc/)
* [Philadelphia 76ers](https://reddit.com/t/philadelphia_76ers/)
* [Premier League](https://reddit.com/t/premier_league/)
* [UFC](https://reddit.com/t/ufc/)

- Business

* [GameStop](https://reddit.com/t/gamestop/)
* [Moderna](https://reddit.com/t/moderna/)
* [Pfizer](https://reddit.com/t/pfizer/)
* [Johnson & Johnson](https://reddit.com/t/johnson_johnson/)
* [AstraZeneca](https://reddit.com/t/astrazeneca/)
* [Walgreens](https://reddit.com/t/walgreens/)
* [Best Buy](https://reddit.com/t/best_buy/)
* [Novavax](https://reddit.com/t/novavax/)
* [SpaceX](https://reddit.com/t/spacex/)
* [Tesla](https://reddit.com/t/tesla/)

- Crypto

* [Cardano](https://reddit.com/t/cardano/)
* [Dogecoin](https://reddit.com/t/dogecoin/)
* [Algorand](https://reddit.com/t/algorand/)
* [Bitcoin](https://reddit.com/t/bitcoin/)
* [Litecoin](https://reddit.com/t/litecoin/)
* [Basic Attention Token](https://reddit.com/t/basic_attention_token/)
* [Bitcoin Cash](https://reddit.com/t/bitcoin_cash/)

- Television

* [The Real Housewives of Atlanta](https://reddit.com/t/the_real_housewives_of_atlanta/)
* [The Bachelor](https://reddit.com/t/the_bachelor/)
* [Sister Wives](https://reddit.com/t/sister_wives/)
* [90 Day Fiance](https://reddit.com/t/90_day_fiance/)
* [Wife Swap](https://reddit.com/t/wife_swap/)
* [The Amazing Race Australia](https://reddit.com/t/the_amazing_race_australia/)
* [Married at First Sight](https://reddit.com/t/married_at_first_sight/)
* [The Real Housewives of Dallas](https://reddit.com/t/the_real_housewives_of_dallas/)
* [My 600-lb Life](https://reddit.com/t/my_600lb_life/)
* [Last Week Tonight with John Oliver](https://reddit.com/t/last_week_tonight_with_john_oliver/)

- Celebrity

* [Kim Kardashian](https://reddit.com/t/kim_kardashian/)
* [Doja Cat](https://reddit.com/t/doja_cat/)
* [Iggy Azalea](https://reddit.com/t/iggy_azalea/)
* [Anya Taylor-Joy](https://reddit.com/t/anya_taylorjoy/)
* [Jamie Lee Curtis](https://reddit.com/t/jamie_lee_curtis/)
* [Natalie Portman](https://reddit.com/t/natalie_portman/)
* [Henry Cavill](https://reddit.com/t/henry_cavill/)
* [Millie Bobby Brown](https://reddit.com/t/millie_bobby_brown/)
* [Tom Hiddleston](https://reddit.com/t/tom_hiddleston/)
* [Keanu Reeves](https://reddit.com/t/keanu_reeves/)

---

- RESOURCES

- [About Reddit](https://www.redditinc.com)
 - [Advertise](https://ads.reddit.com?utm_source=web3x_consumer&utm_name=left_nav_cta)
 - [Help](https://www.reddithelp.com)
 - [Blog](https://redditblog.com/)
 - [Careers](https://www.redditinc.com/careers)
 - [Press](https://www.redditinc.com/press)

---

 - [Communities](https://www.reddit.com/best/communities/1/)
 - [Best of Reddit](https://www.reddit.com/posts/2023/)
 - [Topics](https://www.reddit.com/topics/a-1/)

---

 - [Content Policy](https://www.redditinc.com/policies/content-policy)
 - [Privacy Policy](https://www.reddit.com/policies/privacy-policy)
 - [User Agreement](https://www.redditinc.com/policies/user-agreement)

[Reddit, Inc. © 2024. All rights reserved.](https://redditinc.com)

文章来源: https://www.reddit.com/r/ReverseEngineering/comments/1by5uoi/gmer\_the\_art\_of\_exposing\_windows\_rootkits\_in/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)