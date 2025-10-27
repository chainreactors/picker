---
title: free4chat
url: https://buaq.net/go-131518.html
source: unSafe.sh - 不安全
date: 2022-10-19
fetch_date: 2025-10-03T20:12:05.298403
---

# free4chat

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

![]()

free4chat

A tag already exis
*2022-10-18 23:57:25
Author: [github.com(查看原文)](/jump-131518.htm)
阅读量:52
收藏*

---

A tag already exists with the provided branch name. Many Git commands accept both tag and branch names, so creating this branch may cause unexpected behavior. Are you sure you want to create this branch?

[**1**
branch](https://github.com/y35uishere/free4chat/branches)
[**0**
tags](https://github.com/y35uishere/free4chat/tags)

Code

* Use Git or checkout with SVN using the web URL.
* [Open with GitHub Desktop](https://desktop.github.com)
* [Download ZIP](https://github.com/y35uishere/free4chat/archive/refs/heads/elixir.zip)

This branch is up to date with madawei2699/free4chat:elixir.

Contribute

* This branch is not ahead of the upstream madawei2699:elixir.

  No new commits yet. Enjoy your day!

## Files

[Permalink](https://github.com/y35uishere/free4chat/tree/ce7f286c6b5186f259e8309d4c635cfa6eb27dcb)

Failed to load latest commit information.

Type

Name

Latest commit message

Commit time

[free4.chat](https://free4.chat/) is an instant audio conferencing service.

It is designed by the [local first](https://www.inkandswitch.com/local-first/) and `privacy first` principle, and is very easy to use.

> ⚠️ **This project is just using for technical test purpose, use at all your risk!**
>
> ⚠️ **There is freedom of speech, but I cannot guarantee freedom after speech.** (- Idi Amin)

## Features

* **Common**
  + Use [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) to replace http protocol of JSON-RPC
  + Compatibility
    - Make Safari(WebKit) compatibility better
* **Room**
  + Text chat, can sent text or emoji
    - Persist text messages to browser localStorage
  + Can send arbitrary data by WebRTC datachannel 🚩
  + Room permission setting, like public/private type setting
    - private room can't been seen on room discovery, and it needs password to enter. The password is [End-to-End Encryption](https://blog.excalidraw.com/end-to-end-encryption/), server only need check the answer which given by the client like the `PoW` in blockchain.
    - Public rooms discovery, like hot room list or filter rooms by type/tag
* **User**
  + User real-time collaboration, like whiteboard, you draw I guess, etc.
    - Use [CRDT](https://crdt.tech/) to impelement real-time collaboration
      * <https://github.com/liveblocks/liveblocks>
      * <https://github.com/derekkraan/delta_crdt_ex>
    - Whiteboard
      * <https://github.com/tldraw/tldraw>
  + Robot user, like game robot who can play or facilitate game
    - robot use [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) to play with user in room
    - robot can play some voice games like language learning, technical interview, etc.
      * [Gartic Phone - The Telephone Game](https://garticphone.com/lobby)
      * [ESL Game - Not only practicing English speaking](https://esl.bmpi.dev/)
      * [Gartic.io - Draw, Guess, WIN](https://gartic.io/)

## Architecture

* **Tech Stack**
  + Use Elixir/Phoenix to rewrite the backend code
  + Use Recat/Next.js to rewrite the frontend code
* **Infra**
  + ~~Use docker to deploy to PaaS platform like [Railway](https://railway.app/) or [Fly](https://fly.io/)~~
  + Use GitHub Actions + AWS Lightsail to deploy backend server
  + Backend service cluster, auto scaling, load balancing, etc.
    - Backend service use Elixir libcluster to build cluster
    - Frontend app use the client load balance strategy
    - [TURN cluster scale](https://github.com/membraneframework/membrane_ice_plugin/issues/20)
      * Fix by start turn before the libcluster, still wait the upstream library to fix it normally
  + Security enhancement, like coturn TLS setup, end-to-end encryption, etc.
    - TURN enable TLS
  + Privacy enhancement.
  + IPV6 support.

## Contribution

If you are interested in `webRTC`, `peer-to-peer(P2P)`, `real-time collaboration(CRDT)`, `distributed system` or `robot design`, you can join this project and contact with me by [twitter](https://twitter.com/madawei2699).

## Thanks

* free4.chat Elixir version is build on the top of [Membrane Framework](https://github.com/membraneframework), thanks for their heart of open source.
* [free4.chat Golang version](https://github.com/madawei2699/free4chat/tree/golang) is build on the top of [Kraken](https://github.com/bmpi-dev/kraken), [Mornin](https://github.com/lyricat/mornin.fm), [coturn](https://github.com/coturn/coturn) and [Pion](https://github.com/pion), thanks for their heart of open source.
* These websites also inspired me:
  + [Random voice and text chat rooms that you’ll love. | Speakrandom](https://www.speakrandom.com/)
  + [Practice Speaking English Online Free - Language Practice Community](https://www.free4talk.com/)
  + [Agora Real-Time Voice and Video Engagement](https://www.agora.io/en/)

文章来源: https://github.com/y35uishere/free4chat
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)