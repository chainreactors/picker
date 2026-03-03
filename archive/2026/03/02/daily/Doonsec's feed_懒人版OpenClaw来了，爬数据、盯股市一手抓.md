---
title: 懒人版OpenClaw来了，爬数据、盯股市一手抓
url: https://mp.weixin.qq.com/s/T7gOabm83UADKQrB4mazMQ
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:08:46.839172
---

# 懒人版OpenClaw来了，爬数据、盯股市一手抓

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1N1JeeKBorfFNjjEO5AjvcbT8tz5OzfpN5y1HKLffibrfTwYu8c1spQq7N1UIP80gic7cbk10nn9e9QWpfsY4RiabKVgHPGeLEPgkXCFKkmf7Q/0?wx_fmt=jpeg)

# 懒人版OpenClaw来了，爬数据、盯股市一手抓

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器中沉浸阅读

> 在上篇文章中，我们讲到了在本地部署`OpenClaw`。在部署和使用中遇到了各种坑，对小白上手来说有点困难。

# 自建`OpenClaw`存在问题

**01 安装硬件环境**

`OpenClaw`支持跨平台部署，考虑到很多生产环境在Windows中，在windows安装需要安装`Git``Node.js`等依赖环境，同时由于网络问题，安装容易失败。坑也比较多！

所以，笔者建议在Linux环境通过一键安装命令进行安装！从而对硬件有一定要求！

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcjPCj2hyyA42za0MicSdywicfictQaAZjWTianqLic22PlE6VhvtKLmvqRlU4lq4Q0ciclbImulKywsCjRFI6u47XJrE0l4uBRg9jjY/640?wx_fmt=png&from=appmsg)

**02 网络环境问题**

在安装完成后，我们只能在本地玩耍。想要通过企业微信、飞书、钉钉等工具实现和`OpenClaw`对话，还是需要公网IP的支持。

**03 模型选择**

`OpenClaw`的强大支撑，来源与大模型的支持，在上篇文章中，我们采用的是千问模型，因此还需要考虑选择对应的模型。

而想要解决以上问题，我们不得不需要购买公网服务器，而这又脱离了我们的初衷！有没有更加简单有效的方案呢？既能体验`OpenClaw`带给我们的便捷，又不考虑其他繁琐的配置和硬件呢？我发现Kimi最近出了一个自己的龙虾KimiClaw，不仅部署简单，实测也相当不错。

# 关于Kimi Claw

将`OpenClaw`和`Kimi`结合，搭建专属你的 7×24 在线 AI 助手。 内置技能库，股票分析、竞品监控一键搞定。支持自定义人设，可以是严谨分析师，也可以是幽默搭子。 零门槛部署，自动云端配置，无需服务器。

# 快速开始

访问https://www.kimi.com/bot，点击开始创建。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcWgylrKlO8VRLtWjticeibIxt8DiclG2icPQyficB3CPwu6GghGqYNx41ZAQz9jolC64hZ7HvSI15SSaiaek8ltYW4Dbjke8Qw13fkk/640?wx_fmt=png&from=appmsg)![稍等片刻](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreZpS45Oufq7kia44ozsQvxdq93ibx3e5ibFezPT4pYf11Aqb8dpM886wdlUnWIHfOCYqllH9h97hvHVIRUuaOjKr2tLM6XnEdKgw/640?wx_fmt=png&from=appmsg)

稍等片刻

初始化完成后，界面如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcztvGhHCG88ZlB4yxuR2Edg4gHZ2g4O0BkHoyuT7u7mpNf0FicIjtAgcriaqkFBxIcfjCm4dntp4CTrVYzKj7sUzbn4uiawlZJ5o/640?wx_fmt=png&from=appmsg)

为了后期更加方便，我们可以给KimiClaw起个名字，顺便告诉他是谁！

点击右上角的设置按钮，可以看到当前环境KimiClaw能干什么？

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordwPfRf73W7pYdUYic5eibGhpmibYVUGFaKnvAU6NVTUnosUibXXiaHv2Ik3ZicpsialmZ4m460HRDLes9dwcicVv2ZA2rIWicG7NibAzXaI/640?wx_fmt=png&from=appmsg)

同时，你也可以介绍下自己，同时定义它的主要任务。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcMflgqlFFeDiaTT9SeVeQqOwLtMaM8dL0bXo4yDWjQ3v85ZXEg96ISPYjEEZLjgZUNjqOqiaYBbZlEq5pyCEXX91gHLop3SG67c/640?wx_fmt=png&from=appmsg)

打开终端后，我们便可以看到常见的Linux终端。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfYGicWiavic5JWHiaVBZCI7E784ydt2SpCsrww2S73HnBGxvVfSGDq8lkXWibIibm7jGWzDfHmhuBFlLBo8T2CjKw1yX8f7HhZFFjQo/640?wx_fmt=png&from=appmsg)

输入`openclaw onboard`命令，你可以自定义

![可自行定义](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcR893HkEV2qrdJqrl3At5vW10ZuwichPLovCdlb1H6NEH46cDpN2ue0CbpNefVQfSzQLoDy5WqazJ8l5DdSK2VXKlwPNIrqKII/640?wx_fmt=png&from=appmsg)

可自行定义

# 小试牛刀

现在，一切准备就绪，让我们一起开始吧！

**01 爬虫**

这次，我采用爬取博客标题、发布时间、阅读量为例！

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreuYHwOyX0Woia8iaQy3FUnqZZw3DH9U9jK26AeVPY75nTudvttMJmpcQztiaHdoh7WVwr3wun8zFKgIStiaBRtztuyMiaRymBbAiczw/640?wx_fmt=png&from=appmsg)

爬虫完成后，直接给我结果。而在此过程中，我不在乎是如何写代码、如何配置环境、如何解决依赖。而我只需要结果。

![任务完成效果](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorclKibSX56N0SukX7EyqicK1ibGxHsEtqMt6TrIibST20a02Eibd8IJhSNibOZjvl8mZWyyUuHbFJxwLFPqxSTiar8FFicUQHGNAVRv30A/640?wx_fmt=png&from=appmsg)

任务完成效果

![爬取结果预览](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreOZ5qQKA7qLibjcNGPVQFnCUp65tRkDtsLpU8KOhn14BKZ9NAV768N59UdEEZCLzeVGKsicMF6M1f1MWwrtz5RpT7qI4qPkibWwQ/640?wx_fmt=png&from=appmsg)

爬取结果预览

**02 渗透测试**

作为大表哥的秘书，没点网络安全技能怎么能行。接下来我们用`namp`神器对相关设备进行端口扫描。效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfjaQFt22X35ZibxLXHFgUhpzY0CjutyogUuPW4meMiaSlEhz9o4ZMGb29ReFeL6Et40o9Rr0sOWOvtzLU2pZWA14ialUicgutxSjo/640?wx_fmt=png&from=appmsg)![安全建议](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBordsukpKknZibv7M199LPIc5rxIGIVB7jniaD6cfiaEz3oAG3SO6EDiciceicukZxVqahia7ZddzwKwt7OMnn1GGYZyb8d4TOGTRzeQVAw/640?wx_fmt=png&from=appmsg)

安全建议

另外，我们可以在终端中通过`apt`可直接安装相关安全软件。“肾透”如此简单！

**03 编程开发**

优秀的工具，怎么能少得了编程呢？这里我们让其编写一个贪吃蛇游戏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfGc1yUohbZtWRzanoklXJ7ZOLuWq0yZBusbQBib2PwLYDmIQKFkkjpdRrFAvQ2emORZBd87ibSpKcZTAA4JGn52UqFumx76tKZU/640?wx_fmt=png&from=appmsg)

# 2.4 配置飞书机器人

接下来，我们前往飞书开发者平台，配置机器人。

![点击【创建企业自建应用】](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorciaVOsic1U3sibkRj4BX7R3glsxickQxuOY8laRSCTicg548hqGS7dYp2txffu4gypI30aGy5YFh9QybjcDvTSF1ibOWLTt8q25Ziabc/640?wx_fmt=png&from=appmsg)

点击【创建企业自建应用】

![设置 App 名称和描述](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreX1UjazegZt6kRdULosyH7dWnXttRTR4Gia91pDG2s6SzTnu7rqjrGo9jMDc9ePq8ypkZfHK3cMoloT1yvkQSgeWNJqaoia5rh0/640?wx_fmt=png&from=appmsg)

设置 App 名称和描述

点击添加机器人，创建机器人服务。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorc7icL5pzbpiaae9fMM9ZZl0hRqrN6rd765iaicWNznib8Kc6TQQ5mpJSibzP2MkhC1PDswYN0Gkicd0Igbzwl16B3v5I7yxhFs0iaCW6I/640?wx_fmt=png&from=appmsg)

进入权限设置页面，复制下面的内容添加到【批量导入/导出权限】，如果你需要其他权限也可以根据情况自行添加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBore5z1ZWiagnNF1QZjHWbKZr8OqZq6mia8e3Dqe5QI9PkSTbdJ3iaI9qYb9pKQia3CO21eqpsX4NusV1nKpXlqZcjKHSPQLXMhbSszQ/640?wx_fmt=png&from=appmsg)

```
{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
   "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "contact:user.employee_id:readonly",
      "contact:user.base:readonly",
      "event:ip_list",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:message.reactions:read",
      "im:resource"
    ],
    "user": ["aily:file:read", "aily:file:write", "im:chat.access_event.bot_p2p_chat:read"]
  }
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBordb16nvial8mh6BABbRyhGHkNhWcMM2v9mypcuCHkeJpkwEDccOzUsoq3MCtzCYhGWd0hKM32Aol4cDzicVdxpY3wugVQM5b23kA/640?wx_fmt=png&from=appmsg)

复制凭证发给 Kimi Claw， 进入 凭证与基础信息 页。复制 `App ID`和 `App Secret` 一起发给 Kimi Claw，并告知它这是飞书机器人的应用凭证 等待Kimi Claw 配置完成后，让它重启自己使配置生效，或手动点击设置内的`重启 Kimi Claw`。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcqLSYFLqXGD7IlMR7V9TYtNQFM6axyEYrxCicnYKI0QJGHVpprLXWTWUZzD7SADsoKPNucVCnCqgcL1hJiaodkMKTMrnZW9eITE/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreKbvEjGIEKTBBFS1MfUzCDMe0Lsn0jQFGicKZslfs16fAD03z3z7GDpiasUBaibdwWQ7kjhWMCy1HUPcibEUSkVUx2epeGxdtgVcA/640?wx_fmt=png&from=appmsg)

接下来，根据提示，开始完成下面配置。

进入你的应用后台 → 事件与回调： 事件配置方式：选择「`使用长连接接收事件`」

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorenibc3RRz6NmicTtdWefGF6pqVBn01ibXicbIUtSZUVbHuYlA1JFuVsOhIX472fJCFn5Q4Kk6uO6y4EuL8zmGhv9MDQNia5DJicT7oY/640?wx_fmt=png&from=appmsg)![添加对应事件](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreAlicsLpGPk8f9jEorAGerLxXb6DOItrEzTSrcwK1LRNmic4NcF9tmuF3cmcVG8UXmm3EHbjmHLF6KStb0ibuFgKKoeZhR6Zibgzk/640?wx_fmt=png&from=appmsg)

添加对应事件

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfLUFdpCrxaCOv6Zqjd15llH0pJ3Yn30HzTsFFuDmiblA8nvJRVykpwMicGiaap9u1oa2xvGP1Pftu1XaibzErSELjNrVE65pLrl9c/640?wx_fmt=png&from=appmsg)

切换到版本管理与发布，点击发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcQNk7we8RHBdsKRbOvma6lo5frgVyUB4vgBzzAe28ic5cYdbjr795R3ZYQtibjf5uO9sXImR2qXvpFVKhOrBRcyH6G2sbJFdZBE/640?wx_fmt=png&from=appmsg)

完成后，我们便可以在APP端和机器人对话，并实现相关操作了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/1N1JeeKBorfxZLXtZAfvsJvOMu2L7QUibyrOfkddRy2V0mhib7ibs1h6kxUFTiaEaODCxPDn8yLOya4r34yQbbA2NWWurDdv6DqONW81P0BwP00/640?wx_fmt=jpeg&from=appmsg)

接入飞书后，我们便可以使用多维表格，对数据进行处理。如对股票信息进行分析和处理。

查询小米过去30天的股价情况。并将数据写入飞书多维表格，并基于飞书多维表格创建一个可视化大屏，方便我分析股票信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1N1JeeKBorcoDW5IMHt4Wicu3jF6wDTtiafBiaBPeicoOJibfDS1tStXWwugJYYGUJ6YUbSFCsokMw6I5OhkGj5p7KN3mXPXqXCFic8Sd8iahqDE5w/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorf6kmD5yWA2hgFJh3Py1YF2Bt5yszxK5cQBAL0qmX5QvU4LjeJaPNZIDHMWGW80OMojbbq0uub04ZKXWp1YqAg8MBX2hQMd0H4/640?wx_fmt=png&from=appmsg)

# 总结

利用Kimi Claw 解决了自建OpenClaw的缺憾。让使用和体验更加简单，虽然目前只有会员可以使用，但相比于买一台Macmini，或者企查查等数据库服务，相信AI的接入，我们的生活和工作会更加便捷!

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQu...