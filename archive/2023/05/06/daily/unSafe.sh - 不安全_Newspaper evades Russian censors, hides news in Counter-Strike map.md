---
title: Newspaper evades Russian censors, hides news in Counter-Strike map
url: https://buaq.net/go-161937.html
source: unSafe.sh - 不安全
date: 2023-05-06
fetch_date: 2025-10-04T11:38:36.416612
---

# Newspaper evades Russian censors, hides news in Counter-Strike map

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

![](https://8aqnet.cdn.bcebos.com/1160897f0009641c87c5fcd9029b4380.jpg)

Newspaper evades Russian censors, hides news in Counter-Strike map

A Finnish newspaper is making clever use of popular video game titles t
*2023-5-5 20:15:0
Author: [www.malwarebytes.com(查看原文)](/jump-161937.htm)
阅读量:19
收藏*

---

A Finnish newspaper is making clever use of popular video game titles to promote press freedom and [bypass Russian media restrictions](https://www.theguardian.com/world/2023/may/03/finnish-newspaper-hides-news-reports-for-russians-in-online-game) regarding the invasion of Ukraine. The plan: Hide a secret room underneath a map, which players can stumble upon and see facts, figures, and photographs of what’s been going on.

The map is a custom built design intended to be used in the game [Counter-Strike: Global Offensive](https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/), playable via the Steam platform. We decided to take a look at how effective this is in practice, and what’s contained in the hidden room.

Is this the part where I fire up my ancient Counter-Strike account? It sure is.

## Finding the map

First thing’s first. The map is a custom build, not designed by the game developers. How do you find it? The answer is to [visit the game’s Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=2969831273). This is where custom made content for eligible games on Steam can be found, from maps and weapons to in-game objects or playable characters, depending on the title.

![The Most Popular Maps panel on the Counter-Strike: Global Offensive Workshop page](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file18100_265972_e.jpg)

The map, *de\_vonya*, currently displays as the most popular map of the week so it’s off to a good start. The map description says:

> On the surface, it seems like a normal Slavic city. However, there might be something hidden underneath.

If you click on the map to open its page, and then hit the green “Subscribe” button, the map will be available next time you load up the game.

## Finding the room

Counter-Strike is a team based first person shooter, where small teams race to complete objectives. I haven’t played in years, so I took the easy way out and set up a custom game with the only other combatants being bots. Playing against other people would be a surefire way to make a mess of this exploratory adventure.

The central idea of this map is to accidentally stumble upon the room containing the free press style content. In practice, this proves to be rather difficult.

The first problem: You can’t access the secret room unless you’re dead (don't worry, I'll come back to this). While playing normally, the door remains resolutely shut no matter what you try.

![The door to the secret room](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file65781_265972_e.jpg)

The door to the secret room can't be opened if you're alive

“How do I access the room when I’m dead,” you say? Well, when you die in Counter-Strike you can watch your teammates or you can float around the whole map and take in all of the action. In this state, you have no collision detection. In other words, players who are still alive will stop moving if they walk into an object like a wall. While dead, you’re essentially a floating camera and will pass right through it.

The second problem: Counter-Strike rounds are *short*, around a couple of minutes. They’re short enough with bot, but with actual humans playing, everything can be over very quickly indeed. Even with bots set to the easiest difficulty, three rounds had ended before I eventually found the room.

The third problem: Flying around the map is not entirely helpful with regard to finding the room. Counter-Strike makes use of a game design element called skyboxes. A [skybox](https://developer.valvesoftware.com/wiki/Skybox_Basics) is something which acts as a distant background in the game you’re playing. Imagine a big cube wrapped around the level you’re in, with the sky (or something else altogether) projected on it. No skybox, no background. The world around you would just be a black void.

If the level you’re on has a small or "low" skybox, you’ll run into problems when trying to find a hidden secret. Want to fly up and take in a bird’s eye view of the map? The moment you fly too high up, the screen goes blank (or at least blue coloured, in this level's case).

As a result, the “best” way to find the hidden room is to float around slightly underneath the floor and look for some flashing lights. If you manage to do this before the level ends prematurely, you’ll be able to locate and enter the room.

![Flashing lights indicate where the room is](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file98909_265972_e.jpg)

Flashing lights indicate the presence of the room

## Inside the room

The room itself is made up of several areas of information, with a main table located in the middle.

One wall reads:

> COUNTERSTRIKE OF THE FREE PRESS. This room contains independent journalism that is forbidden in Russia

![A message written on a wall reads "COUNTERSTRIKE OF THE FREE PRESS"](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file33681_265972_e.jpg)

![A message on a wall reads "This room contains independent journalism that is forbidden in Russia"](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file33441_265972_e.jpg)

A sign on one wall states “Russian strikes on civilian targets 2022-2023,” above a map highlighting strike locations, next to several photographs of the damage inflicted.

![A wall map allegedly shows Russian strikes on civilians](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file5922_265972_e.jpg)

One wall of monitors and overturned TV screens states “Russians left behind mass graves in Bucha and Irpin”, along with images of said actions.

![Screens show images off mass graves in Bucha and Irpin](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file87671_265972_e.jpg)

All very powerful. It is somewhat bizarre to look at a wall of photographs and text which reads “Missile strikes: he went to buy food, she and her child were killed in their home” as the game flashes up a message about the last round of Counter-Strike saying “Terrorists win. MVP: BOT Yanni for most eliminations”, though.

![Counter-Strike announces the end of the round](https://www.malwarebytes.com/blog/news/2023/05/easset_upload_file93198_265972_e.jpg)

This is certainly an innovative way to bypass Russia’s media restrictions. One has to wonder if it would be a lot easier to simply have the secret room's door open, especially as one team starts the level right next to it.

If you go looking for the room, be warned that some of the images are graphic. We've blurred some elements of the above screenshots that you may find disturbing, including dead bodies and body parts. While Steam Workshop has [policies in place](https://www.counter-strike.net/workshop/workshopfaq) for individual items like characters or weapon skins, we can't find anything for maps. Could players with an objection to the map's existence cause it to be removed from Steam? Possibly.

It's likely we'll see more maps along these lines, especially as regular map makers see the idea and decide to run with it. Could Russia ultimately ban a game like Counter-Strike over this? Also possible, but I suspect (for now at least) very unlikely.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/05/evading-russian-media-restrictions-with-custom-video-game-maps
 如有侵权请联系:admin#unsafe.sh

© [unSa...