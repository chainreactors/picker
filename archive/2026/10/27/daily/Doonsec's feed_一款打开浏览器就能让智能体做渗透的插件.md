---
title: 一款打开浏览器就能让智能体做渗透的插件
url: https://mp.weixin.qq.com/s/rj3FvOsMlnH29-V1tcS-_A
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:45:58.557128
---

# 一款打开浏览器就能让智能体做渗透的插件

# 一款打开浏览器就能让智能体做渗透的插件

Gh0xE9
Gh0xE9

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

简单来说，这是一款不需要你打开任何工具、不需要任何环境，仅需要一个 Chrome + Node.js 即可做基础渗透和日常任务的插件

笔者早在 2025 年 3 月就已经开始探索智能体在安全上的实践，这期间挫出过不少框架，从一开始的 ReACT 工程，到后面的 Harness 工程，再到淚笑师傅提出的 DAG 黑板工程，可以说从去年到现在，笔者至少见过数十种渗透智能体框架，每一款都大同小异

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaD4ZAa0ILP0Dg6jpdWf7phzJz6Pu8YKib1GVtGZxh1dHhCc3icY2ualFOnMHCtiaRbticWTIQ8diczCYic8S1j4vgicRFhthkL4xZ3qGc/640?wx_fmt=png&from=appmsg)

大多数框架无非就是调用 MCP 写好提示词，让智能体朝着某个方向去做事情

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCd0HR8pJE5dknbJxOZakenRbQtWNbe2MaPuYUraugIyDkbdJmqXLVD6ntribtSk1dmiaFSoibyQlsHN57tZ05VVWn1D41qbpfJJw/640?wx_fmt=png&from=appmsg)

这期间笔者用搓出来的智能体打过不少比赛，也用智能体去挖漏洞、打渗透、红队、CTF 等等，不可否认，智能体确实能替代一些基础操作，不过搞了这么多，笔者就在想，为何不搞一个能在浏览器上做渗透或者任务的插件，之前看 Google 用 Gemini 在浏览器上做操作，感觉很好玩，于是笔者也简单搓了一个 MVP 出来，后需要做的，就是把笔者认为最优的智能体框架给融合进去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaAHaercMMby06YxCnZXYEXBLGJBfiaNzW1BHvicjt8Pc4ejWcG5FpYtSLtSlvmQzIsbs9wMEk4r2wtBot430up0pLcQRvpzhKiarw/640?wx_fmt=png&from=appmsg)

> 项目将会开源在
> **https://github.com/icecliffs/MAPUS**

这是一款面向浏览器端的智能体渗透测试插件，打开目标站点，即可让智能体在浏览器内直接执行渗透测试任务，无需额外打开其他工具，实现浏览器内闭环操作，工具调度与本地并发能力受浏览器及设备性能影响，重计算由智能体后端承担，支持批量任务下发与批量站点测试

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ULOszTo2RiaAarDUbDye90zotIPjFxTKnWGwZBrXhIia5lxZyB7zDArazm1ibx6BlIyMwJuXJOYT9CNrqibU8RxUMLgywxm5teJrVIXk5BybeqA/640?wx_fmt=gif&from=appmsg)

直接看演示图吧，实际上能做的事情有很多，不仅仅局限于做渗透，你可以让他发评论、让他处理日常的网页事务，等等。。。或者让他扒一个企业名并保存到系统本地 txt 里

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaA5zoAicdFCnUBZiamKV65ln8NsZFu1wERtNw0qwGKJ6hn2N7iaRGdcCdhx2Tnc9gRIfeYNXT5R5zJ6z0icahA1r6qTAsXkd4SONCE/640?wx_fmt=png&from=appmsg)

不过还是建议大伙试试笔者公开的 Vaelor 这个工作台，蹲一个使用反馈😋，项目在

https://github.com/Gh0xE9/ErraticGopher

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaC6NoYemWOeNXk8QDAoibpEaib3LgDLPoIv1GhKgibsic74xdIKBP0yUH6zbnntwWmA7HnYFtG5j7RyeuKKaO5gGTUUOts7EmvH2Zg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCpOAR0eEZhyjhEl8uZgUvK9jJ6x0GGfX6NczR2LYkRpDJbDicCAaT7Z9zDcYYdVj3QPw1iaQM7RIakPEM5CYMNoUqtLhpsAfX6Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCM2kC6b68szhk5K5v3yicUfxAtIHgJt5kvdqCsFUQqrIQQq7lbM0HjdV4LdM1fGqhlRuKpIJKvd8AINuZOSia5icshu9QEWdYsPM/640?wx_fmt=png&from=appmsg)

**本工具只允许用于「你拥有所有权」或「你已取得明确书面授权」的系统。**

在没有授权的情况下对其他任何系统使用本工具，**不是"测试"，而是违法行为**——可能面临行政拘留、罚款，直至刑事处罚，且**全部后果由使用者本人独立承担**。

本项目作者 / 贡献者 / 分发者：

* **不参与、不指导、不背书**

  任何具体的测试行为
* **不对**

  任何人使用本工具造成的一切直接或间接后果（包括但不限于数据损毁、业务中断、法律责任、第三方索赔）承担任何形式的责任
* **无法也不承担**

  对使用者行为的监督义务

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCOJLaaibS5WfeiaVEibIPZAXwUlPbXSmFupTNQYQywLxbMHtpQF8lBkgEDLEh0e5GveGxZicJlevLVv8gMPX8NVwfU7S1ic3PRqB1Q/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过