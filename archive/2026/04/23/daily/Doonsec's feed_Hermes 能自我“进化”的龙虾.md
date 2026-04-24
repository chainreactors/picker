---
title: Hermes 能自我“进化”的龙虾
url: https://mp.weixin.qq.com/s/KL77bJyxVzTgzRmy9B0xRg
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:51:26.904667
---

# Hermes 能自我“进化”的龙虾

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVly0svMbV21t5vBOoogUhhcUD87wT2jIpibIrAibicjyviahKrQeicmHw8NZJplYTEXkf7W0ybicE3HVes7pGSSibjshr4vg6FIx0YAr8/0?wx_fmt=jpeg)

# Hermes 能自我“进化”的龙虾

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 595，阅读大约需 3 分钟

+ 前言
+ 使用体验
+ 快速安装
+ 配置 model、skills 和 mcp

- model
- skills
- mcp

+ 演示 Java 代码审计
+ 总结

## 前言

今天朋友圈有人转发下面的文章。

[我们发现了 Hermes Agent 的第一个远程代码执行漏洞，但这已经不重要了](https://mp.weixin.qq.com/s?__biz=MzA5NDYyNDI0MA==&mid=2651960454&idx=1&sn=4f80bd8d5539a8888c3586bf8bc6a36e&scene=21#wechat_redirect)

Hermes 可以简单当初可以成长的龙虾。他会定期检查之前的上下文，然后生成新的提示词放在自己的目录下，启动前阅读。这种情况可以让使用者越用越顺手。

项目地址：https://github.com/NousResearch/hermes-agent

![aba7c01405b9ef89f3c0a9d4d668b947.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm6ceaqqbx4QCUtm71IDtShT1BDDP7MKDPOoOmx1ybicAKrqQozU44ZiatHdydG3e2ia9gVRSWYMMRL9rjr0q8oKQDg0O2phtCQGc/640?from=appmsg "null")

aba7c01405b9ef89f3c0a9d4d668b947.png

Hermes 不支持直接装在 Windows 上，如需要，要在虚拟机或者 WSL 上安装。

## 使用体验

一键安装 Hermes 中，额外下载的工具比较多，感觉比较臃肿。使用有卡顿感，不够丝滑。

其次，比一般的 Agent 的更消耗 Tokens。

不知道为什么，Hermes 连接大模型很容易中途断线（好像是并发的问题），稳定性不如 Cluade code。

## 快速安装

ubuntu22

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

![bb86f28233d828a143224dd73bb004f3.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkVjs2K5yt4RToffo0SVz6TPfDXOXKIOXFZeAzEfcT6StE8UQdFv7LiazmKnTCELvARZw3EibNibZiaUibdepvS6Fk00afY6D6474W0/640?from=appmsg "null")

bb86f28233d828a143224dd73bb004f3.png

使用

```
source ~/.bashrc
hermes
```

![b2ea630cbc47df9389dda41333c29d09.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnRu4HVMgEW6ZKBHkWV623UnRwM3jWs32bd4PWI4xumORZHDtApT8TfBHzVJic5He2DcmocdEiaR1qWKBFOcughbWwsibIkeGibYw8/640?from=appmsg "null")

b2ea630cbc47df9389dda41333c29d09.png

命令行选项

```
hermes              # Interactive CLI — start a conversation
hermes model        # Choose your LLM provider and model
hermes tools        # Configure which tools are enabled
hermes config set   # Set individual config values
hermes gateway      # Start the messaging gateway (Telegram, Discord, etc.)
hermes setup        # Run the full setup wizard (configures everything at once)
hermes claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes update       # Update to the latest version
hermes doctor       # Diagnose any issues
```

官方文档：https://hermes-agent.nousresearch.com/docs/getting-started/quickstart

## 配置 model、skills 和 mcp

配置这三样用 cc-switch 很方便，在最新版本 3.14.0 的 cc-switch 中已经支持 Hermes 了。

地址：
https://github.com/farion1231/cc-switch/releases/tag/v3.14.0

安装

```
sudo dpkg -i CC-Switch-v3.14.0-Linux-x86_64.deb
# 如果报错，修复依赖并自动安装缺失的库
sudo apt install -f -y
# 重新执行
sudo dpkg -i CC-Switch-v3.14.0-Linux-x86_64.deb
```

运行

```
cc-switch
```

如下图标就是 Hermes
![6ce0cee38d8b5eec9e709c438be067f0.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkicEZ7jxyDzaM0lkibv3FmHK9ViaJoLDiaRJGMgBcdC6aXYZ0fy80qz9Flr9uzopcxPZNZxLfSN9wuZIjku59JSBGvJoJMo5JRq7g/640?from=appmsg "null")

6ce0cee38d8b5eec9e709c438be067f0.png

### model

以智谱 GLM 为例
![81e0781351b997e6518e3d6fb69a2b04.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkkuNpUR39nFcDXfuRmwj01qfviczA9RRibUopy96kodJ3JicGyZHZfSicrXqCL9u180ibCDNEhCf0o5yIWI0Z4m26Q4BmBoxcaCzSI/640?from=appmsg "null")

81e0781351b997e6518e3d6fb69a2b04.png

选择 Zhipu GLM
![2c69247a827c81fd12264c24ce5383f0.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlfJskRZY8KprJibQwawLqkbTmrMAQpwvokibicGbnzbibQ56x3TpsUpUUNvb0ibsWicicKOMJpSS8ZH7fibdrNAf472rbm4UGKO6EribcQ/640?from=appmsg "null")

2c69247a827c81fd12264c24ce5383f0.png

![6f14bada6a57c537d034d25c02e89775.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmBhAx3SmrVboM4QVefyY3tGibrKQXiaWp6zjvBNCHquwX3kicBGHcia4Fia8eITRlYlDOaH1LgM4uPiaicEkS8Yjibia7O16eEKIM1Vic8s/640?from=appmsg "null")

6f14bada6a57c537d034d25c02e89775.png

智谱 API key 获取：https://bigmodel.cn/apikey/platform

```
glmtest
https://open.bigmodel.cn/api/anthropic
```

![7193b1e555ad51e3c710c80fa7ea5bd6.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVn4aBUth0vrgfXGJ5Bibyjcp5zfl16Kibziby7Gfbpu0bZY9ae0rsHbmp8Dap6b9Y9YWR8FTMUC20ksGxtzsAIFMz5yhKd3AUvJYs/640?from=appmsg "null")

7193b1e555ad51e3c710c80fa7ea5bd6.png

```
glm-4.6
```

![ee0b4ae1660b32d7ec14a54644c9662a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkvWQFibP2ISnmr15RZO3l9zTnicFyy0hicyesuIRjuGagGtazD2eDcIKvdib3zDGTxRfgKalm7ywjywa7MMhv7NibastA0P0GibXVUc/640?from=appmsg "null")

ee0b4ae1660b32d7ec14a54644c9662a.png

结果
![8b29b85da57b096abeac7946b745a028.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkp3GLjAUBLYH0aeHgaJdcqXjdRyvmgKvxMTiacllVsiabibw31kkStJVaMf32qGRiacOLRX7PEET6ibKlppByKSCMcjMia2dKxLpnY0/640?from=appmsg "null")

8b29b85da57b096abeac7946b745a028.png

### skills

先更改 cc-switch 配置 skills 的方式，软连接的 skills，Hermes 无法识别
![a3890ae15774aa38a035043182556a56.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmCKN52HHic8cxTXmzj89yp9YW9zmOEQqsc0RIPRZS3UntLjrkhwIsGGN2Thw2vjFKSLWCqapSoy6Jbg8hMOMGrDgLj6dpf5Ne4/640?from=appmsg "null")

a3890ae15774aa38a035043182556a56.png

以 wxmini-security-audit 为例
https://github.com/sssmmmwww/wxmini-security-audit

下载 zip，导入
![f1fc68507c68ba9a38c2f08d92f73b41.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn4Zb3O1nSUd6SLGib0TLmLtkuWGJcsEouPWcZWeKU3VMnoMxTcSfgX9x0LELexMUwZJUTH5yMWfUwMy2sCKq0iaqCL5ib19TVWxM/640?from=appmsg "null")

f1fc68507c68ba9a38c2f08d92f73b41.png

成功获取 skills
![e314a945a572c82b9359cf015017a568.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlGAQSLI4276mHBPceqw3SlFD7StmeUaeZ09L1ynNHA62gOJsbalgmz0eibTGmVPAUELtBjhPF1VV4p8mEV1boiajydvHJU2VpGE/640?from=appmsg "null")

e314a945a572c82b9359cf015017a568.png

### mcp

![b716d46140963fd6b3c4ef0f4dd1d76b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm3ObQsmBEXCxf7HF2A3Kmn986Vcza3h9uwU0n0K2P0YHdNGbPoOptOx3Tn2YsSs7B4MNsiauoUeR6ibeTBUSGoLqYxSJZeE1Qw4/640?from=appmsg "null")

b716d46140963fd6b3c4ef0f4dd1d76b.png

比如 cfr

```
{
  "type": "stdio",
  "command": "uvx",
  "args": [
    "java-decompile-mcp"
  ],
  "env": {
    "CFR_PATH": "/home/gold/Desktop/hermes/tools/cfr-0.152.jar"
  },
  "disabled": false
}
```

![fd5884bc00794d0efc2ab87d9ba21560.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnqjAiaZrO8ibCa5fuuU5wv0QEElW5wbDmnOib69xXhBoTWO9QDxe95L4SZo519RaZLyslK1ticVzf9a1oB8FLcEXLZA3Dtz0jLfpk/640?from=appmsg "null")

fd5884bc00794d0efc2ab87d9ba21560.png

```
hermes mcp list
```

结果
![646d40bba6b414192c9ff9df0c7751a7.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkKHYicSKQEOquX5nOmN2VXZgsgaZ9dJf0hT5amr2f7rpBe1YSIl8I06gvVNh9FG3RGaiaibNQ72rsOMuGg6alC0GuBydTjFu69Mc/640?from=appmsg "null")

646d40bba6b414192c9ff9df0c7751a7.png

## 演示 Java 代码审计

JavaSecLab

```
git clone https://github.com/whgojp/JavaSecLab
```

skills
项目地址：项目地址：https://github.com/RuoJi6/java-audit-skills

```
/java-audit-pipeline 审计当前目录下的项目JavaSecLab
```

结果
![96853604ebe25ba706f585ce878f51c3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlaodh79BUq7L3LAHyWlZTEo0tnvKZYEN9tibX653FL0JF1oQHDPVicOu7LouphIZDCO849e0Zt2vhPuuHoBiaw7wu70XJweeuPvc/640?from=appmsg "null")

96853604ebe25ba706f585ce878f51c3.png

好吧，Hermes 你在此不要走动，我去充个词元

最终结果
![07d5d91022b5cfbc1db7b8768f1d99bf.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVl5HWSzZdujRSlTrlQPBOrjArkP9JCPYLwsXiaZAfkh2RvgphO6Hh7sENjItwDLuoemJEiaIkVu11c8lN9MEnWyIkibYsLiaaupu4k/640?from=appmsg "null")

07d5d91022b5cfbc1db7b8768f1d99bf.png

## 总结

cc-switch 确实好用，帮忙管理mcp、skills。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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