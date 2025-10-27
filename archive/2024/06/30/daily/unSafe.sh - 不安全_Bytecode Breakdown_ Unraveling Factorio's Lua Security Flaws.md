---
title: Bytecode Breakdown: Unraveling Factorio's Lua Security Flaws
url: https://buaq.net/go-247944.html
source: unSafe.sh - 不安全
date: 2024-06-30
fetch_date: 2025-10-06T16:54:37.997515
---

# Bytecode Breakdown: Unraveling Factorio's Lua Security Flaws

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

![](https://8aqnet.cdn.bcebos.com/5d89bf789480e4eecce0aaaba8bedb2b.jpg)

Bytecode Breakdown: Unraveling Factorio's Lua Security Flaws

*2024-6-29 23:25:18
Author: [www.reddit.com(查看原文)](/jump-247944.htm)
阅读量:11
收藏*

---

Open navigation

Go to Reddit Home

Get the Reddit app

[Log In](https://www.reddit.com/login/)Log in to Reddit

Open settings menu

* [Log In / Sign Up](https://www.reddit.com/login/)
* [Advertise on Reddit](https://accounts.reddit.com/adsregister?utm_source=web3x_consumer&utm_name=user_menu_cta)
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

[tnavda](https://www.reddit.com/user/tnavda/)

ADMIN

MOD

[![](https://external-preview.redd.it/bytecode-breakdown-unraveling-factorios-lua-security-flaws-v0-x409mGPPR5R0Rl9qM6VunrWhy1UzVY1-O6JMpbE98-E.jpg?width=640&crop=smart&auto=webp&s=5e25ea04af7a64729826a09b0af9d13a77aa7b25)](https://memorycorruption.net/posts/rce-lua-factorio/)[![r/ReverseEngineering - Bytecode Breakdown: Unraveling Factorio's Lua Security Flaws](https://external-preview.redd.it/bytecode-breakdown-unraveling-factorios-lua-security-flaws-v0-x409mGPPR5R0Rl9qM6VunrWhy1UzVY1-O6JMpbE98-E.jpg?width=640&crop=smart&auto=webp&s=5e25ea04af7a64729826a09b0af9d13a77aa7b25)](https://memorycorruption.net/posts/rce-lua-factorio/)

[memorycorruption.net](https://memorycorruption.net/posts/rce-lua-factorio/)

- &nbsp;
- &nbsp;

---

- TOPICS

- Internet Culture (Viral)

* [Amazing](https://reddit.com/t/amazing/)
* [Animals & Pets](https://reddit.com/t/animals_and_pets/)
* [Cringe & Facepalm](https://reddit.com/t/cringe_and_facepalm/)
* [Funny](https://reddit.com/t/funny/)
* [Interesting](https://reddit.com/t/interesting/)
* [Memes](https://reddit.com/t/memes/)
* [Oddly Satisfying](https://reddit.com/t/oddly_satisfying/)
* [Reddit Meta](https://reddit.com/t/reddit_meta/)
* [Wholesome & Heartwarming](https://reddit.com/t/wholesome_and_heartwarming/)

- Games

* [Action Games](https://reddit.com/t/action_games/)
* [Adventure Games](https://reddit.com/t/adventure_games/)
* [Esports](https://reddit.com/t/esports/)
* [Gaming Consoles & Gear](https://reddit.com/t/gaming_consoles_and_gear/)
* [Gaming News & Discussion](https://reddit.com/t/gaming_news_and_discussion/)
* [Mobile Games](https://reddit.com/t/mobile_games/)
* [Other Games](https://reddit.com/t/other_games/)
* [Role-Playing Games](https://reddit.com/t/role_playing_games/)
* [Simulation Games](https://reddit.com/t/simulation_games/)
* [Sports & Racing Games](https://reddit.com/t/sports_and_racing_games/)
* [Strategy Games](https://reddit.com/t/strategy_games/)
* [Tabletop Games](https://reddit.com/t/tabletop_games/)

- Q&As

* [Q&As](https://reddit.com/t/q_and_as/)
* [Stories & Confessions](https://reddit.com/t/stories_and_confessions/)

- Technology

* [3D Printing](https://reddit.com/t/3d_printing/)
* [Artificial Intelligence & Machine Learning](https://reddit.com/t/artificial_intelligence_and_machine_learning/)
* [Computers & Hardware](https://reddit.com/t/computers_and_hardware/)
* [Consumer Electronics](https://reddit.com/t/consumer_electronics/)
* [DIY Electronics](https://reddit.com/t/diy_electronics/)
* [Programming](https://reddit.com/t/programming/)
* [Software & Apps](https://reddit.com/t/software_and_apps/)
* [Streaming Services](https://reddit.com/t/streaming_services/)
* [Tech News & Discussion](https://reddit.com/t/tech_news_and_discussion/)
* [Virtual & Augmented Reality](https://reddit.com/t/virtual_and_augmented_reality/)

- Pop Culture

* [Celebrities](https://reddit.com/t/celebrities/)
* [Creators & Influencers](https://reddit.com/t/creators_and_influencers/)
* [Generations & Nostalgia](https://reddit.com/t/generations_and_nostalgia/)
* [Podcasts](https://reddit.com/t/podcasts/)
* [Streamers](https://reddit.com/t/streamers/)
* [Tarot & Astrology](https://reddit.com/t/tarot_and_astrology/)

- Movies & TV

* [Action Movies & Series](https://reddit.com/t/action_movies_and_series/)
* [Animated Movies & Series](https://reddit.com/t/animated_movies_and_series/)
* [Comedy Movies & Series](https://reddit.com/t/comedy_movies_and_series/)
* [Crime, Mystery, & Thriller Movies & Series](https://reddit.com/t/crime_mystery_and_thriller_movies_and_series/)
* [Documentary Movies & Series](https://reddit.com/t/documentary_movies_and_series/)
* [Drama Movies & Series](https://reddit.com/t/drama_movies_and_series/)
* [Fantasy Movies & Series](https://reddit.com/t/fantasy_movies_and_series/)
* [Horror Movies & Series](https://reddit.com/t/horror_movies_and_series/)
* [Movie News & Discussion](https://reddit.com/t/movie_news_and_discussion/)
* [Reality TV](https://reddit.com/t/reality_tv/)
* [Romance Movies & Series](https://reddit.com/t/romance_movies_and_series/)
* [Sci-Fi Movies & Series](https://reddit.com/t/scifi_movies_and_series/)
* [Superhero Movies & Series](https://reddit.com/t/superhero_movies_and_series/)
* [TV News & Discussion](https://reddit.com/t/tv_news_and_discussion/)

---

- RESOURCES

- [About Reddit](https://www.redditinc.com)
 - [Advertise](https://accounts.reddit.com/adsregister?utm_source=web3x_consumer&utm_name=left_nav_cta)
 - [Help](https://www.reddithelp.com)
 - [Blog](https://redditblog.com/)
 - [Careers](https://www.redditinc.com/careers)
 - [Press](https://www.redditinc.com/press)

---

 - [Communities](https://www.reddit.com/best/communities/1/)
 - [Best of Reddit](https://www.reddit.com/posts/2024/global/)
 - [Topics](https://www.reddit.com/topics/a-1/)

---

 - [Content Policy](https://www.redditinc.com/policies/content-policy)
 - [Privacy Policy](https://www.reddit.com/policies/privacy-policy)
 - [User Agreement](https://www.redditinc.com/policies/user-agreement)

[Reddit, Inc. © 2024. All rights reserved.](https://redditinc.com)

文章来源: https://www.reddit.com/r/ReverseEngineering/comments/1drdnlu/bytecode\_breakdown\_unraveling\_factorios\_lua/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)