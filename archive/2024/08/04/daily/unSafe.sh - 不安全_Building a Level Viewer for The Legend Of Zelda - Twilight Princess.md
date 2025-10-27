---
title: Building a Level Viewer for The Legend Of Zelda - Twilight Princess
url: https://buaq.net/go-254121.html
source: unSafe.sh - 不安全
date: 2024-08-04
fetch_date: 2025-10-06T18:02:26.648670
---

# Building a Level Viewer for The Legend Of Zelda - Twilight Princess

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

![](https://8aqnet.cdn.bcebos.com/d0ae512d35cb97722ca842bc23a6d36f.jpg)

Building a Level Viewer for The Legend Of Zelda - Twilight Princess

This project is definitely one of the most advanced of mine. I started programming a web BMD viewer
*2024-8-3 21:0:15
Author: [hackernoon.com(查看原文)](/jump-254121.htm)
阅读量:12
收藏*

---

This project is definitely one of the most advanced of mine. I started programming a web BMD viewer for Twilight Princess (Nintendo GameCube) because I love this game and as a game producer, I am fascinated by analyzing levels and immersing myself in the details of how they were made. This project is a way for me to explore that passion and gain a deeper understanding of the game I love. It's a challenging and rewarding learning experience. I am excited to see where this project will take me and what new discoveries I will make along the way. Until now this project took me months and months of research. Research that is based on the work of more than 20 other people who investigated and shared their knowledge and findings about rarc, bmd, gcm yaz0, j3d, tev etc. I came across some person that I wrote down to give them Credit:

Thanks goes out to: ("LordNed", "thakis", "Jasper St. Pierre", "Kiwi", "Dolphin Emulator Team", "Gamma", "Zan") - for their pioneering efforts!

| ![](https://api.fenixfox-studios.com/assets/840bdbb4-cc0f-425f-9181-e810b23f0aaa?auto=format&fit=max&w=3840) | ![](https://api.fenixfox-studios.com/assets/12764695-c395-42f6-a5e7-3bb140fa3da5?auto=format&fit=max&w=3840) |
| --- | --- |
| ![](https://api.fenixfox-studios.com/assets/07767ea4-4e87-4eef-9549-3ce8dd4586fd?auto=format&fit=max&w=3840) | ![](https://api.fenixfox-studios.com/assets/2e1d517a-ec01-4bd0-857b-81b208ffdf4d?auto=format&fit=max&w=3840) |

> Water, Fog, animated Textures are features currently on the roadmap

## Demonstration

The program was programmed using three.js and webGL. It runs at a constant 60fps in the chrome browser. Unfortunately I can not share the interactive Viewer (models, rooms etc.) with you, cause I don't want to see how far the limits for fair use of research are. Enjoy my montage:

[https://api.fenixfox-studios.com/assets/d43523dd-5cbe-4da4-9c7d-2d275690050a](https://api.fenixfox-studios.com/assets/d43523dd-5cbe-4da4-9c7d-2d275690050a?ref=hackernoon.com)

## Specifications

BMD and BDL are the file formats used by Nintendo for storing model data in its GameCube and Wii games. They are part of Nintendo's J3DGraph library, which is a component of the larger JSYSTEM toolkit. BMD first appeared in the game Luigi's Mansion. It was then the only model format used in Super Mario Sunshine. The Wind Waker further introduced the BDL format, which is an extension of BMD with an additional section for material FIFO instructions called MDL3. MDL3 is used to improve rendering efficiency. Super Mario Galaxy 2 was the last game to use this model format.

JSYSTEM is a proprietary game development toolkit used by Nintendo to create games for its consoles. It includes various libraries and tools for tasks such as 3D modeling, animation, and physics. J3DGraph is a library within JSYSTEM that provides functions for handling 3D graphics and is responsible for the BMD and BDL file formats. BMD stands for Binary MoDel and BDL stands for Binary Display List.

The JSYSTEM toolkit was discovered by reverse engineers and game modders in the early 2000s, when they began to analyze and decompile the code of Nintendo GameCube and Wii games. They found that many of the games shared similar code structures and libraries, which led them to suspect the existence of a common development toolkit. After much research and experimentation, they were able to identify and extract the JSYSTEM libraries from the games, and began to document and reverse-engineer its various components, including the J3DGraph library and the BMD and BDL file formats.

As the understanding of JSYSTEM grew, modders began to develop their own tools for working with the JSYSTEM format and started to create their own custom models, textures and even create new games using the JSYSTEM libraries. This led to the creation of a vibrant modding community that continues to exist today, with many modders sharing their findings and tools online.

## Development

In the beginning, I wasn't really interested in the actual \*.dol or \*.gcm container formats because other people had already done a great job providing ready-to-use tools (created gcm reader later myself). After a bit of searching, I found folders that looked like they might contain some interesting stuff, like rooms and other elements. Large areas, such as Faron Woods, were divided into chunks and saved into separate files, which would later be merged to form the complete area.

![](https://api.fenixfox-studios.com/assets/44ba96bd-6fea-45d8-8e05-6179a9b7dc9d?auto=format&fit=max&w=1920)

But I wanted to start easy. Maybe something simple! After unpacking most of the stuff in the folder, I sorted the files by size and found a super simple object. When I checked the file in [HexWorkshop](http://www.hexworkshop.com/history/6_80/?ref=hackernoon.com), I stumbled upon markers like VTX, INF, DRW, and SHP. From the vertex positions, I could tell it was a flat box with a simple door knob. I soon realized it was the door from the lake bed temple.

![](https://api.fenixfox-studios.com/assets/1e574910-2740-4049-8167-1a15ef0f16cb?auto=format&fit=max&w=3840)

I knew what the object might look like, and I knew where to look for the basic information like vertex coordinates as well as texture information.

[BMD-Format Documentation](https://github.com/LordNed/WindEditor/wiki/BMD-and-BDL-Model-Format?ref=hackernoon.com)

You have to be careful since some of the information are simply incorrect for your case. Certain attributes were just different from what those docs are telling. But having a format sheet like that is all you need in order to extract a 3d model and its texture!

![](https://api.fenixfox-studios.com/assets/c28ca19b-51ed-4b72-af2a-6f4c13fe2918?auto=format&fit=max&w=3840)

After my successful attempt to extract at least on simple object, I thought that it would be time to dig further and tackle a complete area! Armed with the same algorithm that I just wrote I picked the file named R00\_00. I was hoping that it would be Ordon Village or Faron Woods. But that didn't matter cause all I got was a pile of garbage. Clearly a case of wrong vertex order. Can you tell by looking at this image what room it is?

![](https://api.fenixfox-studios.com/assets/dae044bb-e0c7-40f9-938f-cc40ad93f697?auto=format&fit=max&w=3840)

Shape by shape, I slowly tested the waters. Here and there, cliffs and gravestones started to appear. It became clear that I was looking at the Kakariko Graveyard area.

| ![](https://api.fenixfox-studios.com/assets/f90ea571-bd75-4e99-b932-e11b32c3aff4?auto=format&fit=max&w=3840) | ![](https://api.fenixfox-studios.com/assets/ec7fd256-51d5-4ada-9177-b627e4b0d67a?auto=format&fit=max&w=2048) |
| --- | --- |

After quite some time, I was able to produce this result: certain objects were missing, some faces were inverted, and not a single texture seemed to be correctly applied.

| ![](https://api.fenixfox-studios.com/assets/2ac07642-b6fc-448a-b659-02ec3c740bb1?auto=format&fit=max&w=3840) | ![](https://api.fenixfox-studios.com/assets/d04bfbf8-2194-40a8-a1ff-9665c335d908?auto=format&fit=max&w=3840) |
| --- | --- |

The solution was somewhat confusing. Although certain shapes had specific material indices defined, they didn't have a straightforward 1:1 relationship. Instead, you had to look at the ...