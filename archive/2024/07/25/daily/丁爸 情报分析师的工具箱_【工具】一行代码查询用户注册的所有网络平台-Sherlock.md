---
title: 【工具】一行代码查询用户注册的所有网络平台-Sherlock
url: https://mp.weixin.qq.com/s?__biz=MzI2MTE0NTE3Mw==&mid=2651145276&idx=1&sn=0fa592dd90a1b7a2c177f88da392849c&chksm=f1af3306c6d8ba1091fb0fb7d18fbb318735ffff86dcf9762f418876361bd573efef217efd62&scene=58&subscene=0#rd
source: 丁爸 情报分析师的工具箱
date: 2024-07-25
fetch_date: 2025-10-06T17:43:45.229778
---

# 【工具】一行代码查询用户注册的所有网络平台-Sherlock

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5y7NfMVmfTtAd6GjBcZQXZRN4ICDxtYplMkquKZfSFhK7chpa0NUqHmynAYYbT2GpFXFU3KnkyMow/0?wx_fmt=jpeg)

# 【工具】一行代码查询用户注册的所有网络平台-Sherlock

原创

丁爸

丁爸 情报分析师的工具箱

今天给大家推送查询用户在数百个网站注册情况的开源情报工具：Sherlock

工具地址：https://sherlockproject.xyz/

github地址：https://github.com/sherlock-project/sherlock

![](https://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5y7NfMVmfTtAd6GjBcZQXZRGz1lWAntS96uic1sEJ4lDVWWJuzJRdo62Jwr033jZ1RDWDtbENbPeZA/640?wx_fmt=png&from=appmsg)

输入一个用户名，该工具可以查询该用户名在四百多个网站是否有注册账号。

工具支持在Python、Brew、Apt、BlackArch、Docker、GitHub等环境运行：

![](https://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5y7NfMVmfTtAd6GjBcZQXZRXYicIluAtziatmdTHZTnIGSYicD5oXn9Lt9kBalEt7dgFb58w18Phia5DA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5y7NfMVmfTtAd6GjBcZQXZRpNwzjiaRib2VxiaoB2qZFzkhyBNSsfggLTnUEpMQhMAprRs51MIWPyK0Q/640?wx_fmt=png&from=appmsg)

比如我选择在Docker环境下运行，因为我的电脑安装了Docker

首先在电脑左下角搜索框输入“cmd"查找“应用”启动“命令提示符”：

![](https://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5y7NfMVmfTtAd6GjBcZQXZRgD2IJ2ic1YBlpJK3dyZHw3YpmbvTWhOvKlvg9BQXdb7O5hUl7JGdnTA/640?wx_fmt=png&from=appmsg)

**在命令符窗口输入：**

**docker pull sherlock/sherlock**

![](https://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5y7NfMVmfTtAd6GjBcZQXZRtDpM9KG7J9o3bgxQO7fYRwGiaDQTTiawVSwia1QW5TxWEiaJE1e8HxqmbQ/640?wx_fmt=png&from=appmsg)

**再在命令符窗口输入：**

**docker run --rm -t sherlock/sherlock user123**

**我的演示将代码中的用户名：****“******user******123****”替换成了“****trump****”**

**搜索结果显示“trump”这个用户名在166个网站有注册信息：**

![](https://mmbiz.qpic.cn/mmbiz_png/B0AKMb5va5y7NfMVmfTtAd6GjBcZQXZR0OVITxvGfLNOxRG0cwQGbpVqgfgEav3x3fibhLanMCG8IY28ic5ZxYxA/640?wx_fmt=png&from=appmsg)

[\*] Checking username trump on:

[+] 1337x: https://www.1337x.to/user/trump/

[+] 9GAG: https://www.9gag.com/u/trump

[+] About.me: https://about.me/trump

[+] Academia.edu: https://independent.academia.edu/trump

[+] Airbit: https://airbit.com/trump

[+] AllMyLinks: https://allmylinks.com/trump

[+] Anilist: https://anilist.co/user/trump/

[+] Apple Developer: https://developer.apple.com/forums/profile/trump

[+] Archive of Our Own: https://archiveofourown.org/users/trump

[+] Archive.org: https://archive.org/details/@trump

[+] Audiojungle: https://audiojungle.net/user/trump

[+] Bandcamp: https://www.bandcamp.com/trump

[+] Behance: https://www.behance.net/trump

[+] BiggerPockets: https://www.biggerpockets.com/users/trump

[+] BodyBuilding: https://bodyspace.bodybuilding.com/trump

[+] BuyMeACoffee: https://buymeacoff.ee/trump

[+] BuzzFeed: https://buzzfeed.com/trump

[+] Championat: https://www.championat.com/user/trump

[+] Chess: https://www.chess.com/member/trump

[+] Clapper: https://clapperapp.com/trump

[+] Clubhouse: https://www.clubhouse.com/@trump

[+] Codeberg: https://codeberg.org/trump

[+] Codecademy: https://www.codecademy.com/profiles/trump

[+] Codechef: https://www.codechef.com/users/trump

[+] Codeforces: https://codeforces.com/profile/trump

[+] Codepen: https://codepen.io/trump

[+] ColourLovers: https://www.colourlovers.com/lover/trump

[+] Crowdin: https://crowdin.com/profile/trump

[+] Cults3D: https://cults3d.com/en/users/trump/creations

[+] DEV Community: https://dev.to/trump

[+] DailyMotion: https://www.dailymotion.com/trump

[+] Dealabs: https://www.dealabs.com/profile/trump

[+] Discogs: https://www.discogs.com/user/trump

[+] Disqus: https://disqus.com/trump

[+] Docker Hub: https://hub.docker.com/u/trump/

[+] Dribbble: https://dribbble.com/trump

[+] Duolingo: https://www.duolingo.com/profile/trump

[+] Exposure: https://trump.exposure.co/

[+] EyeEm: https://www.eyeem.com/u/trump

[+] Fameswap: https://fameswap.com/user/trump

[+] Finanzfrage: https://www.finanzfrage.net/nutzer/trump

[+] Flightradar24: https://my.flightradar24.com/trump

[+] Flipboard: https://flipboard.com/@trump

[+] Freelancer: https://www.freelancer.com/u/trump

[+] Freesound: https://freesound.org/people/trump/

[+] GaiaOnline: https://www.gaiaonline.com/profiles/trump

[+] Genius (Artists): https://genius.com/artists/trump

[+] Genius (Users): https://genius.com/trump

[+] Giant Bomb: https://www.giantbomb.com/profile/trump/

[+] Giphy: https://giphy.com/trump

[+] GitHub: https://www.github.com/trump

[+] GitLab: https://gitlab.com/trump

[+] Gitee: https://gitee.com/trump

[+] GoodReads: https://www.goodreads.com/trump

[+] Grailed: https://www.grailed.com/trump

[+] Gravatar: http://en.gravatar.com/trump

[+] Gutefrage: https://www.gutefrage.net/nutzer/trump

[+] Hackaday: https://hackaday.io/trump

[+] HackerNews: https://news.ycombinator.com/user?id=trump

[+] HackerOne: https://hackerone.com/trump

[+] Hashnode: https://hashnode.com/@trump

[+] HubPages: https://hubpages.com/@trump

[+] Hubski: https://hubski.com/user/trump

[+] HudsonRock: https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-username?username=trump

[+] Imgur: https://imgur.com/user/trump

[+] Instagram: https://instagram.com/trump

[+] Issuu: https://issuu.com/trump

[+] Itemfix: https://www.itemfix.com/c/trump

[+] Kick: https://kick.com/trump

[+] Kongregate: https://www.kongregate.com/accounts/trump

[+] Launchpad: https://launchpad.net/~trump

[+] LeetCode: https://leetcode.com/trump

[+] Letterboxd: https://letterboxd.com/trump

[+] LibraryThing: https://www.librarything.com/profile/trump

[+] Lichess: https://lichess.org/@/trump

[+] Linktree: https://linktr.ee/trump

[+] LiveJournal: https://trump.livejournal.com

[+] MMORPG Forum: https://forums.mmorpg.com/profile/trump

[+] Medium: https://medium.com/@trump

[+] MixCloud: https://www.mixcloud.com/trump/

[+] Monkeytype: https://monkeytype.com/profile/trump

[+] MyAnimeList: https://myanimelist.net/profile/trump

[+] MyMiniFactory: https://www.myminifactory.com/users/trump

[+] Mydramalist: https://www.mydramalist.com/profile/trump

[+] Myspace: https://myspace.com/trump

[+] NationStates Nation: https://nationstates.net/nation=trump

[+] NationStates Region: https://nationstates.net/region=trump

[+] Naver: https://blog.naver.com/trump

[+] Needrom: https://www.needrom.com/author/trump/

[+] NintendoLife: https://www.nintendolife.com/users/trump

[+] Nyaa.si: https://nyaa.si/user/trump

[+] Pastebin: https://pastebin.com/u/trump

[+] Patreon: https://www.patreon.com/trump

[+] Periscope: https://www.periscope.tv/trump/

[+] Pinkbike: https://www.pinkbike.com/u/trump/

[+] ProductHunt: https://www.producthunt.com/@trump

[+] PromoDJ: http://promodj.com/trump

[+] Redbubble: https://www.redbubble.com/people/trump

[+] Replit.com: https://replit.com/@trump

[+] ReverbNation: https://www.reverbnation.com/trump

[+] Rumble: https://rumble.com/user/trump

[+] Scribd: https://www.scribd.com/trump

[+] Shpock: https://www.shpock.com/shop/trump/items

[+] Sketchfab: https://sketchfab.com/trump

[+] Slack: https://trump.slack.com

[+] Slashdot: https://slashdot.org/~trump

[+] SlideShare: https://slideshare.net/trump

[+] Slides: https://slides.com/trump

[+] Smule: https://www.smule.com/trump

[+] Snapchat: https://www.snapchat.com/add/trump

[+] SoundCloud: https://soundcloud.com/trump

[+] Sporcle: https://www.sporcle.com/user/trump/people

[+] Spotify: https://open.spotify.com/user/trump

[+] Star Citizen: https://robertsspaceindustries.com/citizens/trump

[+] Steam Community (Group): https://steamcommunity.com/groups/trump

[+] Steam Community (User): https://steamcommunity.com/id/trump/

[+] Strava: https://www.strava.com/athletes/trump

[+] TETR.IO: https://ch.tetr.io/u/trump

[+] Tenor: https://tenor.com/users/trump

[+] ThemeForest: https://themeforest.net/user/trump

[+] TorrentGalaxy: https://torrentgalaxy.to/profile/trump

[+] TradingView: https://www.tradingview.com/u/trump/

[+] TrashboxRU: https://trashbox.ru/users/trump

[+] Trello: https://trello.com/trump

[+] Tuna: https://tuna.voicemod.net/user/trump

[+] Typeracer: https://data.typeracer.com/pit/profile?user=trump

[+] Ultimate-Guitar: https://ultimate-guitar.com/u/trump

[+] Unsplash: https://unsplash.com/@trump

[+] ...