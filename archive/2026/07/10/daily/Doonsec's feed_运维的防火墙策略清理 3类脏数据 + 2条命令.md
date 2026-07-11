---
title: 运维的防火墙策略清理 3类脏数据 + 2条命令
url: https://mp.weixin.qq.com/s/qw0irtAU1aiI5Sa7z1twkg
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:03:02.996421
---

# 运维的防火墙策略清理 3类脏数据 + 2条命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yJLbez93flicMLKDVMJeBPfNk4Fd5WzCpG8pU4JyibzaX8Y3oIHOVk0zUUnG5FIddlgWbwUdSgk5YhFekjuFP3LibuLDjSNHr2AtH5k4Aia68wk/0?wx_fmt=jpeg)

# 运维的防火墙策略清理 3类脏数据 + 2条命令

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

策略不是越厚越安全。积下的脏规则只会拖慢匹配、埋误放行的雷。每月一次，自动瘦身。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9fQiaPs3bo2UbJ1sibeQNgnQrBEaZricm7NhG3h3EjcWx8Ee4Jdv8jQe8XDRoxLhDNjFeZEADQfVEiaXoUicH9DMlWGpSnedlce2m8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flibk9WGd03cVkeCC8vHPsX1s18jLMeWQTDSwrub4iaiamgz8HSzTohz39kzmP9ZoZ88qq2X0jVICOKpU43Ju43AM44IBFIm2uqyws/640?wx_fmt=png&from=appmsg)

上周排查一台华为防火墙不通，`display security-policy rule` 一列拉到底，hit count 为 0 的规则占了快三成。三成规则从没被命中过，还每天陪着真正干活的规则一起被顺序扫描。策略库只增不减，是运维现场最常见的慢性病。

01

## 先认清楚：3类脏数据

规则越长越乱，先分清楚你面对的是哪一类。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flickzTeFxF1kJtBh8CCHu7kAXsn8qwRb2MK12HFNRbib05WseuuxlSzYXDxHeAQ8ov9OsfnUvRCg3cVwKvKMddj9K0LyxNEtLMBc/640?wx_fmt=png&from=appmsg)

02

## 两条命令：先把家底摸清楚

别上来就删。先看见数据。

BASH

```
display security-policy rule # 打出策略列表 + 每条命中次数(hit count) # 重点看 hit count 为 0 的批次，它们是优先排查对象 # 导出后按月排序，长期零命中一眼筛出
```

BASH

```
display firewall session # 看当前会话实际匹配到哪条策略 # 某条该放行的流量死活过不去，用它确认： # 是没匹配到规则，还是被上游某条 deny 截了# 配合抓包一起看，定位最快
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93fl8ZdqFlQic1ba07Uuc6yic3NI0SMe5TvmlpwLmS1Vv72DLfjMf6V7nZian1f0aLjla8Ia4tn1F0pXPaTmkxky0u7QdTZlnvEmEru0/640?wx_fmt=png&from=appmsg)

03

## Python 批量揪出脏规则

规则几十条往上，肉眼对是折磨。导出防火墙配置，写个脚本批量比对。核心思路：解析每条规则的**源地址、目的地址、服务端口、动作**四个字段，两两组合对比。

PYTHON

```
# 把规则解析成结构化对象后两两比较 # 重复关系：四条字段完全一致      -> 标记"冗余规则" # 包含关系：A 的源/目的/服务范围 完全覆盖 B -> 标记"影子规则(B 被 A 遮蔽)" # 输出到 Excel，按"可疑程度"排序，给运维逐条确认
```

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9VDRiaDea89icGPib9gic6cgDrKOl5smOefJfjpVV3ywfxeTAb6CicVlOSDfjCic9S0UbtcUSPnmAGe467lETwuUibdZVJVJSMmsGwWE/640?wx_fmt=png&from=appmsg)

04

## 优化原则：Checklist 直接照做

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9EYUTGdd3luHVpyrNc579Qe4DqQRdbRgM3YiaibicGu3FcZoJGGFv0STFxWfyrPEeMOicPmYX80UBp2OZSbR2SxMuX7sNfyiafMYOE/640?wx_fmt=png&from=appmsg)

// 老宋的话

策略臃肿的本质不是运维懒，是没人把"清理"当成和"开通"一样的正经活。华为官方文档也把"定期清理长期不命中规则"列为优化项，说明这是共性难题。你今天花半小时排一次 hit count，省下的是以后每次故障排查时，在几百条规则里大海捞针的命。现在就去防火墙敲一条 `display security-policy rule`，看你那三成零命中里，有没有早该走的。

---

### 往期精彩

[运维的内网DNS进阶：Split Horizon 配置指南](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486737&idx=1&sn=16b7072c71aec9e71b22dc8f41519a75&scene=21#wechat_redirect)

[渗透测试从业者的全能工具箱：76,700+ Star、185+工具一键到位（HackingTool 从零到实战）](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486737&idx=1&sn=16b7072c71aec9e71b22dc8f41519a75&scene=21#wechat_redirect)

[甲方运维应急响应的日志分析利器：Klogg 大文件秒开，朴实可靠](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486706&idx=1&sn=5d012122194fb80d041c59f83bbdbf8a&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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