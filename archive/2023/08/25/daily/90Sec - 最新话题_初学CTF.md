---
title: 初学CTF
url: https://forum.90sec.com/t/topic/2301
source: 90Sec - 最新话题
date: 2023-08-25
fetch_date: 2025-10-04T11:59:36.943426
---

# 初学CTF

[90Sec](/)

# [初学CTF](/t/topic/2301)

[账号审核](/c/account/11)

[GUANZHI](https://forum.90sec.com/u/GUANZHI)

2023 年8 月 24 日 03:08

1

# flag明文 [账号审核](/c/account/11)

开始小白学习流量分析题， 当然是从最基础的开始啦，使用到的工具是**wireshark**哪有什么做流量题不用wireshark的啊
打开流量包，最先开始的思路就是搜一下flag这个字符串是否存在于流量包中

[![82bb469f50e2d27fb0e5c424afe33af8](https://forum.90sec.com/uploads/default/original/2X/f/f28a623a53b5faecd1238b446d7c8fa4c073e330.png)

82bb469f50e2d27fb0e5c424afe33af81190×788 62.2 KB](https://forum.90sec.com/uploads/default/original/2X/f/f28a623a53b5faecd1238b446d7c8fa4c073e330.png "82bb469f50e2d27fb0e5c424afe33af8")

于是第一题就这么顺利的解决掉了

像这里的话可观察到flag是存于txt中的，因为是textdata数据

`右击-->显示分组字节流`
`右击协议-->追踪流-->TCP流`

即可查看text数据：
![033ab431cdf9319eb6b185e4d358aac9](https://forum.90sec.com/uploads/default/original/2X/f/f7cccacfdca5029096a873271ff791897e9df582.png)

#### 得到flag{This\_is\_a\_f10g}

## 附：求求各位大佬帮我转正

[maplgebra](https://forum.90sec.com/u/maplgebra)

2023 年8 月 25 日 12:02

2

质量不太够。

* [首页](/)
* [类别](/categories)
* [准则](/guidelines)
* [服务条款](/tos)
* [隐私政策](/privacy)

由 [Discourse](https://www.discourse.org) 提供技术支持，启用 JavaScript 以获得最佳体验